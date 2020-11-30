import os
import sys

from example import csv_addition

# Recommended to import AFL last
import afl
afl.init()

csv_addition(sys.stdin.read())

# Recommended as speeds up exiting
os._exit(0)
