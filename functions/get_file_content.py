import sys,os
import functions.config as config

def get_file_content(working_directory, file_path):
    full_path=os.path.abspath(os.path.join(working_directory,file_path.lstrip('/') if file_path.startswith('/') else file_path))
    
    if file_path not in full_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    

    try:
        with open(full_path, "r") as file:
            content = file.read(config.CHARACTER_LIMIT)
            return f'{content}[...File "{file_path}" truncated at 10000 characters]' if len(content) == 10000 else content
    except Exception as e:
        return f"Error: {e}"