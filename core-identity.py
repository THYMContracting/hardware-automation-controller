import os
import subprocess
from groq import Groq

# ==========================================
# Project: Autonomous Hardware Controller (core_identity.py)
# Author: Alex Thomas
# Purpose: A diagnostic bridge between LLM intelligence and hardware interfaces.
# ==========================================

class HardwareController:
    def __init__(self):
        # SECURE KEY MANAGEMENT: Use environment variables for production/portfolios
        self.api_key = os.environ.get("GROQ_API_KEY", "YOUR_API_KEY_HERE")
        self.client = Groq(api_key=self.api_key)
        self.model = "llama-3.3-70b-versatile"

    def list_files(self, path="."):
        """Utility tool to inventory local diagnostic files."""
        try:
            return os.listdir(path)
        except Exception as e:
            return f"Error accessing path: {e}"

    def run_terminal_command(self, command):
        """
        Executes hardware-level commands (e.g., ADB for mobile diagnostics).
        Demonstrates the ability to bridge software and physical hardware.
        """
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return result.stdout if result.stdout else result.stderr
        except Exception as e:
            return f"Command execution failed: {e}"

    def process_diagnostic_query(self, user_prompt):
        """
        Sends hardware status to the LLM to receive autonomous 
        troubleshooting or modification steps.
        """
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a hardware diagnostic engine. Use terminal tools to assist the user."
                },
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
            model=self.model,
        )
        return chat_completion.choices[0].message.content

if __name__ == "__main__":
    # Initialize the controller
    controller = HardwareController()
    
    # Example execution: Checking for connected hardware via ADB
    print("Checking connected hardware devices...")
    device_status = controller.run_terminal_command("adb devices")
    print(device_status)
