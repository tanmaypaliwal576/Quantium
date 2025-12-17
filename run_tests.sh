#!/bin/bash --> run all the files 

# Exit immediately if any command fails
set -e

# Activate the virtual environment
source .venv/Scripts/activate

# Run the test suite
pytest

# If pytest succeeds, exit with code 0
exit 0
