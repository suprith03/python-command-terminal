import os
import shutil

def list_files(path="."):
    try:
        return "\n".join(os.listdir(path))
    except FileNotFoundError:
        return f"Error: Directory '{path}' not found."

def change_directory(path):
    try:
        os.chdir(path)
        return f"Changed directory to {os.getcwd()}"
    except FileNotFoundError:
        return f"Error: Directory '{path}' not found."
    except NotADirectoryError:
        return f"Error: '{path}' is not a directory."

def print_working_directory():
    return os.getcwd()

def make_directory(dirname):
    try:
        os.mkdir(dirname)
        return f"Directory '{dirname}' created."
    except FileExistsError:
        return f"Error: Directory '{dirname}' already exists."

def remove(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            return f"File '{path}' removed."
        elif os.path.isdir(path):
            shutil.rmtree(path)
            return f"Directory '{path}' removed."
        else:
            return f"Error: '{path}' not found."
    except Exception as e:
        return f"Error: {str(e)}"
