import sys
import os

# Get the current directory of this conftest.py file
current_dir = os.path.dirname(os.path.realpath(__file__))

# Append the root directory of your project to sys.path
root_dir = os.path.join(current_dir, "..")
sys.path.append(root_dir)
