import math, random, statistics
import datetime, time
import os, sys, shutil, json

print("Square root:", math.sqrt(25))

print("Random number:", random.randint(1, 10))

print("Average:", statistics.mean([10, 20, 30]))

print("Date:", datetime.date.today())

print("Time:", time.time())

print("Directory:", os.getcwd())

print("Python version:", sys.version)

print("Disk space:", shutil.disk_usage("."))

data = {"name": "john", "age": 20}

print("JSON:", json.dumps(data))

print("Program completed")

