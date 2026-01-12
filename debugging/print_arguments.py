#!/usr/bin/python3
"""
print_arguments.py - Print only command line arguments
Fixed version: Skips script filename (argv[0])
"""

import sys

# Print only the arguments, not the script name
for arg in sys.argv[1:]:
    print(arg)
