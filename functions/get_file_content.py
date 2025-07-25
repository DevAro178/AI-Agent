import sys,os
import functions.config as config
from google.genai import types
from functions.is_subdir import is_subdir

def get_file_content(working_directory, file_path):
    full_path=os.path.abspath(os.path.join(working_directory, file_path))
    
    if not is_subdir(working_directory,file_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    

    try:
        with open(full_path, "r") as file:
            content = file.read(config.CHARACTER_LIMIT)
            return f'{content}[...File "{file_path}" truncated at 10000 characters]' if len(content) == 10000 else content
    except Exception as e:
        return f"Error: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Return the contents of specified file in string format, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File name with path relative to working directory whose content's will be returned in string format.",
            ),
        },
    ),
)
