import re
import subprocess
import sys
from pathlib import Path

CLI_PATH = Path(__file__).resolve().parents[1] / "src" / "main.py"


def run_cli(commands):
    return subprocess.run(
        [sys.executable, "-X", "utf8", str(CLI_PATH)],
        input=commands,
        encoding="utf-8",
        capture_output=True,
        timeout=10,
    )


def test_status_reports_metrics_on_each_call():
    result = run_cli("status\nstatus\nexit\n")

    assert result.returncode == 0, result.stderr
    assert len(re.findall(r"CPU: \d+(?:\.\d+)?%", result.stdout)) == 2
    assert len(re.findall(r"Memória: \d+(?:\.\d+)? (?:GB|GiB)", result.stdout)) == 2
    assert len(re.findall(r"Tempo ligado: \d+h \d+min", result.stdout)) == 2


def test_handles_unknown_commands_and_ignores_blank_input():
    result = run_cli("oi\n   \najuda\nexit\nignorar\n")

    assert result.returncode == 0, result.stderr
    assert result.stdout.count("Ingenium ready.") == 1
    assert "Comando desconhecido: oi" in result.stdout
    assert "Comando desconhecido: ajuda" in result.stdout
    assert result.stdout.count("Comando desconhecido:") == 2
    assert "ignorar" not in result.stdout


def test_exits_cleanly_at_end_of_input():
    result = run_cli("oi\n")

    assert result.returncode == 0, result.stderr
    assert "Comando desconhecido: oi" in result.stdout