from functions.is_subdir import is_subdir
import os,subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    if not is_subdir(working_directory,file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    abs_file_path=os.path.abspath(os.path.join(working_directory, file_path))
    
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        res=subprocess.run(args=['python',abs_file_path,*args],timeout=30,capture_output=True,cwd=os.path.abspath(working_directory))
        
        output=[]
        
        if res.returncode!=0:
            output.append(f"Process exited with code {res.returncode}")
        
        if res.stdout:
            output.append(f"STDOUT: {res.stdout}")
        else:
            output.append("No output produced.")
            
        if res.stderr:
            output.append(f"STDERR: {res.stderr}")
        
        return "\n".join(output)
        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run the python file from the provided file_path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File name with path relative to working directory that will be executed.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Additional arguments that will be provided to the subprocess.run() while invoking the provided file_path.",
            )
        },
    ),
)