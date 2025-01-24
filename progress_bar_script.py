# progress_bar_script.py

from tqdm import tqdm
import time
import os

def read_progress(file_path):
    try:
        with open(file_path, 'r') as f:
            percentage = float(f.read().strip())
            return percentage
    except:
        return None

def main(file_path):
    with tqdm(total=100, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]') as pbar:
        while True:
            percentage = read_progress(file_path)
            if percentage is not None:
                pbar.n = percentage
                pbar.refresh()
                if percentage >= 100:
                    break
            time.sleep(0.1)

if __name__ == "__main__":
    file_path = 'progress.txt'
    open(file_path, 'w').close()  # Ensure the file is empty
    main(file_path)
