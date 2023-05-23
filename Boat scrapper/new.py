from tqdm import tqdm
import time
import os

total_iterations = 100

for i in tqdm(range(total_iterations)):
    time.sleep(0.1)  # Simulating some work

# Clear the terminal screen
os.system('cls' if os.name == 'nt' else 'clear')
