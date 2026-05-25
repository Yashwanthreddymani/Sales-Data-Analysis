import subprocess
import sys


def run_command(command):
    """Run terminal command"""
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as error:
        print(f"Error: {error}")
        return False


def setup_project():
    print("Setting up Sales Data Analysis Project...")

    # Install required libraries
    print("\nInstalling requirements...")
    run_command("pip install -r requirements.txt")

    # Launch Jupyter Notebook
    print("\nOpening Jupyter Notebook...")
    run_command("jupyter notebook")


if __name__ == "__main__":
    setup_project()
