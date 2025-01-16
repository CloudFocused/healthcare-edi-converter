#!/bin/bash

# Set PYTHONPATH to the nested folder
export PYTHONPATH=$(pwd)
export PYTHONWARNINGS="ignore"

# Print the PYTHONPATH for verification
echo "PYTHONPATH is set to: $PYTHONPATH"

# Run Tests
python3 -m unittest tests/test_convert837.py -v