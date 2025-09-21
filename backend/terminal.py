from .commands import list_files, change_directory, print_working_directory, make_directory, remove
from .system_monitor import system_stats

def execute_command(command):
    tokens = command.strip().split()
    if not tokens:
        return ""

    cmd = tokens[0]
    args = tokens[1:]

    if cmd == "ls":
        return list_files(args[0]) if args else list_files()
    elif cmd == "cd":
        return change_directory(args[0]) if args else "Error: Path required"
    elif cmd == "pwd":
        return print_working_directory()
    elif cmd == "mkdir":
        return make_directory(args[0]) if args else "Error: Directory name required"
    elif cmd == "rm":
        return remove(args[0]) if args else "Error: File or directory name required"
    elif cmd == "stats":
        return system_stats()
    elif cmd == "help":
        return (
            "Available commands:\n"
            "ls [path] - List files\n"
            "cd <path> - Change directory\n"
            "pwd - Show current directory\n"
            "mkdir <dirname> - Create new directory\n"
            "rm <path> - Remove file/directory\n"
            "stats - Show system stats\n"
            "exit - Quit terminal"
        )
    else:
        return f"Error: Command '{cmd}' not found. Type 'help' for available commands."
