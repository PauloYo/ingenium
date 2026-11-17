import psutil

def status():
    memory = psutil.virtual_memory()
    cpu_percent = psutil.cpu_percent(interval=1)
    uptime_seconds = max(0, int(__import__("time").time() - psutil.boot_time()))
    hours, remainder = divmod(uptime_seconds, 3600)
    minutes = remainder // 60

    print(f"CPU: {cpu_percent:.1f}%")
    print(
        f"Memória: {memory.used / (1000 ** 3):.2f} GB usados de "
        f"{memory.total / (1000 ** 3):.2f} GB ({memory.percent:.1f}%)"
    )
    print(f"Tempo ligado: {hours}h {minutes}min")

if __name__ == "__main__":
    status()