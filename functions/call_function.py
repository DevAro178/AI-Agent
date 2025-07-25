import os
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def call_function(function_call_part, verbose=False):
    function_name=function_call_part.name
    result=None
    working_dir='./calculator'
    try:
        
        if verbose:
            print(f"Calling function: {function_name}({function_call_part.args})")
        else:
            print(f" - Calling function: {function_name}")
        
        match function_name:
            case 'get_files_info':
                function_result=get_files_info(working_dir,**function_call_part.args)
            
            case 'get_file_content':
                function_result=get_file_content(working_dir,**function_call_part.args)
            
            case 'write_file':
                function_result=write_file(working_dir,**function_call_part.args)
            
            case 'run_python_file':
                function_result=run_python_file(working_dir,**function_call_part.args)
            
            case _:
                return types.Content(
                            role="tool",
                            parts=[
                                types.Part.from_function_response(
                                    name=function_name,
                                    response={"error": f"Unknown function: {function_name}"},
                                )
                            ],
                        )
            
        return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=function_name,
                            response={"result": function_result},
                        )
                    ],
                )
    
    except Exception as e:
        return types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=function_name,
                            response={"error": e},
                        )
                    ],
                )