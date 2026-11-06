import subprocess
import sys


def run_cli(commands):
    return subprocess.run(
        [sys.executable, "src/main.py"],
        input=commands,
        text=True,
        capture_output=True,
        timeout=5,
    )


def test_accepts_multiple_commands_and_exits():
    result = run_cli("oi\n\najuda\nexit\nignorar\n")

    assert result.returncode == 0, result.stderr
    assert result.stdout.count("Ingenium ready.") == 1
    assert "Comando recibido: oi" in result.stdout
    assert "Comando recibido: ajuda" in result.stdout
    assert result.stdout.count("Comando recibido:") == 2
    assert "ignorar" not in result.stdout

def test_exits_cleanly_at_end_of_input():
    result = run_cli("oi\n")

    assert result.returncode == 0, result.stderr
    assert "Comando recibido: oi" in result.stdout