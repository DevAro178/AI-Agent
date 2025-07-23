from functions.is_subdir import is_subdir
import os

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
        