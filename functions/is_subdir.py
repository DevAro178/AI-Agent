import os

def is_subdir(working_directory,file_path):

    abs_working_dir = os.path.abspath(working_directory)
    abs_target_path = os.path.abspath(os.path.join(working_directory, file_path))

    return abs_target_path.startswith(abs_working_dir)