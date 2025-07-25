from functions.is_subdir import is_subdir
import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        if not is_subdir(working_directory,file_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))
        
        dir_path=abs_target_path.rsplit('/',1)[0]
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    
        with open(abs_target_path, "w") as file:
            file.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error: {e}"
        
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="write or overwrite the content in the provided file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File name with path relative to working directory to which the provided content will be written or overwritten",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content that will be written to the specifed file, constrained to the working directory.",
            )
        },
    ),
)