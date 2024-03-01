# This is Base Skeleton Structure for Creating Project Structure Related Files

# Package for Interacting with Operating System
import os   

# Package handle file paths in a platform (OS) -independent manner
from pathlib import Path  

# Package for Log The Important Events
import logging


logging.basicConfig(
    level=logging.INFO,
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
    )

# format print the message like: [2024-03-01 15:30:45: INFO]: This is an informational message.

while True:
    project_name = input("Enter the Project Name: ")
    if project_name != '':
        break

logging.info(f"Creating project by name: {project_name}")

# List of files Required for Project Structure:
list_of_files = [
    ".github/workflows/.gitkeep",        # GitHub Actions workflow file: To Checks Certain Checks
    f"src/{project_name}/__init__.py",   # Package init file: To Consider all .py files as Pkg
    f"tests/__init__.py",                # Tests init file
    f"tests/unit/__init__.py",           # Unit tests init file: To use this files a test the functionslities
    f"tests/integration/__init__.py",    # Integration tests init file
    "init_setup.sh",                     # Initialization setup script
    "requirements.txt",                  # Main requirements file
    "requirements_dev.txt",              # Development requirements file
    "setup.py",                          # Package setup script
    "pyproject.toml",                    # pyproject.toml configuration file
    'setup.cfg',                         # Setup configuration file
    "tox.ini"                            # tox configuration file: TO test Package on different diffrent Environment
]

# Code of Creating Files related to Projects:
for filepath in list_of_files:
    filepath = Path(filepath)   # To Handle Path based on Operating System
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        # Creating Empty Directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Creating Empty File
        with open(filepath, "w") as f:   
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")