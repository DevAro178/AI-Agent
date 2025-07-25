from google.genai import types
import os
from functions.is_subdir import is_subdir

def get_files_info(working_directory, directory="."):
    try:
        dir_path=os.path.join(working_directory, directory)
        
        if not is_subdir(working_directory,directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(dir_path):
            return f'Error: "{directory}" is not a directory'
        
        contents=os.listdir(dir_path)
        content_string=[]
        for file in contents:
            file_path=os.path.join(dir_path,file)
            is_file=os.path.isfile(file_path)
            file_size=os.path.getsize(file_path)
            content_string.append(f"- {file}: file_size={file_size} bytes, is_dir={not is_file}")
            
        return "\n".join(content_string)
    
    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
