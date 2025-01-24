import subprocess
import sys

def install_modules(file_path):
    try:
        # Open the file and read the module names
        with open(file_path, 'r') as file:
            modules = file.readlines()

        # Install each module using pip
        for module in modules:
            module = module.strip()  # Remove any leading/trailing whitespace
            if module:
                subprocess.check_call([sys.executable, "-m", "pip", "install", module])

        print("All modules installed successfully!")

    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing {module}: {e}")

# Example usage
install_modules('libraryperm.txt')
