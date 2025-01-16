#!/bin/bash

# Set PYTHONPATH to the nested folder
export PYTHONPATH=$(pwd)
export PYTHONWARNINGS="ignore"


# Run Tests
python3 -m unittest tests/test_convert837.py -v