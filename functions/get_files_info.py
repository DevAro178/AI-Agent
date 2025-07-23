import os

def get_files_info(working_directory, directory="."):
    try:
        dir_path=os.path.join(working_directory, directory)
        
        if working_directory not in os.path.abspath(dir_path):
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


