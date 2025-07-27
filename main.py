import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)

def main():
    try:
        user_prompt = sys.argv[1]
        verbose = len(sys.argv) > 2 and sys.argv[2] == '--verbose'

        system_prompt = """You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]

        for i in range(20):
            response = client.models.generate_content(
                model='gemini-2.0-flash-001',
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
                )
            )

            if verbose:
                print(f"\nIteration {i+1}")
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print("Response tokens:", response.usage_metadata.candidates_token_count)

            for candidate in response.candidates:
                messages.append(candidate.content)

            if not response.function_calls and response.text:
                print("Final response:")
                print(response.text)
                break

            if response.function_calls:
                for function_call in response.function_calls:
                    function_result = call_function(function_call, verbose)

                    if not function_result.parts or not hasattr(function_result.parts[0].function_response, 'response'):
                        raise Exception("Missing function response content.")

                    messages.append(
                        types.Content(role="tool", parts=[function_result.parts[0]])
                    )

                    if verbose:
                        print(f"-> {function_result.parts[0].function_response.response}")
            else:
                if verbose:
                    print("No function calls, and no final response.")
                break
        else:
            print("Maximum iterations reached without a final response.")
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")
        print("Usage: python main.py \"your prompt here\" [--verbose]")
        sys.exit(1)

if __name__ == "__main__":
    main()
