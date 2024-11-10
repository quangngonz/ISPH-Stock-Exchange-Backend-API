import os

def print_structure(path, indent=""):
    # List all items in the current directory
    items = os.listdir(path)
    
    # Exclude hidden folders, files starting with a period, and __pycache__ folder
    items = [item for item in items if not item.startswith('.') and item != '__pycache__']
    
    # Loop through each item in the directory
    for index, item in enumerate(items):
        full_path = os.path.join(path, item)
        
        # Print the folder or file with the appropriate indentation
        if os.path.isdir(full_path):
            # Print directory with "│" for directories, and recurse into it
            print(f"{indent}├── {item}/")
            # Recurse into subdirectories with increased indentation
            print_structure(full_path, indent + "│   ")
        else:
            # Print file
            print(f"{indent}├── {item}")

# Specify the root folder of your project
project_path = os.getcwd()
print(f"{project_path.split('/')[-1]}/")  # Print the project root name
print_structure(project_path, indent="│   ")
