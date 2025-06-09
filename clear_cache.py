import shutil
import os

def clear_cache():
    # Remove __pycache__ directory
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
        print("Cache cleared successfully!")

if __name__ == "__main__":
    clear_cache() 