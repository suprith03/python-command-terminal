import psutil

def system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    processes = len(psutil.pids())
    return (
        f"CPU Usage: {cpu}%\n"
        f"Memory Usage: {memory.percent}% ({round(memory.used / (1024 ** 3), 2)} GB / {round(memory.total / (1024 ** 3), 2)} GB)\n"
        f"Running Processes: {processes}"
    )
