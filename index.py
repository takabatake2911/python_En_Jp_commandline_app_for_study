import random
import time

with open("data.csv") as f:
    data = f.read().split("\n")

random.shuffle(data)

for i,row in enumerate(data):
    words = row.split(",")
    print(f"============ {i+1}問目 ===========")
    print(words[0])
    time.sleep(1)
    print(words[1])
    time.sleep(0.5)
