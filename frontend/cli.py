import readline
from backend.terminal import execute_command
from backend.nlp import parse_natural_command

HISTORY_FILE = ".terminal_history"

try:
    readline.read_history_file(HISTORY_FILE)
except FileNotFoundError:
    open(HISTORY_FILE, "wb").close()

def completer(text, state):
    commands = ["ls", "cd", "pwd", "mkdir", "rm", "stats", "help", "exit"]
    results = [c for c in commands if c.startswith(text)] + [None]
    return results[state]

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

def run_terminal():
    print("=== Python Command Terminal ===")
    print("Type 'help' for available commands. Type 'exit' to quit.")
    print("Tip: You can also type natural language queries (e.g., 'create a folder test')\n")

    while True:
        try:
            command = input("> ").strip()
            if not command:
                continue

            if command.lower() == "exit":
                print("Exiting terminal...")
                readline.write_history_file(HISTORY_FILE)
                break

            nlp_command = parse_natural_command(command)
            if nlp_command:
                print(f"[AI] Interpreted as: {nlp_command}")
                command = nlp_command

            output = execute_command(command)
            print(output)

        except KeyboardInterrupt:
            print("\nUse 'exit' to quit.")
        except EOFError:
            print("\nExiting terminal...")
            readline.write_history_file(HISTORY_FILE)
            break
