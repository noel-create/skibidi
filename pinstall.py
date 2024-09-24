import subprocess
import sys

# List of required packages
required_packages = [
    'flask', 'flask-socketio', 'opencv-python-headless', 'numpy', 'mss',
    'pyngrok', 'pyautogui', 'Pillow', 'nextcord', 'requests',
    'keyboard', 'python-dateutil', 'pywin32'
]

# Function to install packages
def install_packages():
    try:
        # Loop through and install each package using pip
        for package in required_packages:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print("All packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {e.cmd}. Error: {e}")

# Call the function to install packages
install_packages()
sys.exit()