import time
import random

quotes = [
    "Docker makes life easier!",
    "Containers are the future 🚀",
    "Keep coding, keep learning!",
    "Practice makes perfect!",
    "Cloud + DevOps = Power!"
]

while True:
    print("\n🟢 Random Motivation:")
    print(random.choice(quotes))
    time.sleep(3)
