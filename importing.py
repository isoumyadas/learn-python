# Pattern 1: Import the whole module
import math
# Now use : math.sqrt(16)


# Pattern 2 : Import specific items from a module
from math import sqrt, pi
# Now use : sqrt(6)

# =======================================================================

import random

number = random.randint(2,99)
print("number:: ", number)

choice = random.choice(["apple", "mango", "messi", "ronaldo", "sunil", "gurpreet"])
print(f"choice:: {choice}")

# ========================================================================

import datetime
import time

# today = datetime.date.today()
today = datetime.date.fromtimestamp(time.time()) # this is same as above

print(f"today: {today}")

import os

current_dir = os.getcwd()
print(f"current directory: {current_dir}")

import json

data = {"name": "messi", "profession": "pro footballer"}
json_string = json.dumps(data)
print(f"json string:: {json_string}")

# ==========================================================================

# Importing as alias

import pandas as pd
df = pd.DataFrame(data)

# To install libs use ' pip install pandas '
