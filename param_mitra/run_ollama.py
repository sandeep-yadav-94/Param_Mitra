import subprocess
from config import OLLAMA_MODEL

def run_gpt4all(prompt):
    try:
        print("\n[Soch rha hu Bhai...]")
        result = subprocess.run(
            ['ollama', 'run', OLLAMA_MODEL, prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error running model: {str(e)}"