from tqdm import tqdm
import time

def read_progress(file_path):
    """Reads progress value from a file."""
    try:
        with open(file_path, 'r') as f:
            percentage = float(f.read().strip())
            return percentage
    except:
        return 0  # Default to 0% if file cannot be read

def update_progress(file_path, percentage):
    """Writes progress value to a file."""
    with open(file_path, 'w') as f:
        f.write(f"{percentage:.2f}")

def inner_progress(inner_file_path, total_steps):
    """Handles the inner progress bar based on a percentage file."""
    with tqdm(
        total=total_steps,
        desc="Inner Progress",
        position=1,  # Second line
        bar_format="{l_bar}{bar}| {percentage:.0f}% [{elapsed}<{remaining}]",
        leave=False,  # Replace after finish
    ) as inner_pbar:
        while True:
            percentage = read_progress(inner_file_path)
            inner_pbar.n = percentage
            inner_pbar.refresh()  # Update the display
            if percentage >= 100:
                break
            time.sleep(0.1)

def main(outer_file_path, inner_file_path, total_outer_iterations, inner_iterations):
    """Handles the overall and inner progress bars."""
    with tqdm(
        total=total_outer_iterations,
        desc="Overall Progress",
        position=0,  # First line
        bar_format="{l_bar}{bar}| {percentage:.0f}% [{elapsed}<{remaining}]",
        leave=True,  # Leave after finish
    ) as overall_pbar:
        while True:
            percentage = read_progress(outer_file_path)
            overall_pbar.n = (percentage / 100) * total_outer_iterations
            overall_pbar.refresh()  # Update the display

            # Check if overall progress is complete
            if percentage >= 100:
                break

            # Run the inner progress bar
            inner_progress(inner_file_path, inner_iterations)
            update_progress(inner_file_path, 0)

            # Update the outer progress file after inner bar completion
            current_outer_percentage = percentage + (100 / total_outer_iterations)
            update_progress(outer_file_path, current_outer_percentage)
            time.sleep(0.1)

if __name__ == "__main__":
    # File paths for progress tracking
    outer_file_path = "outer_progress.txt"
    inner_file_path = "inner_progress.txt"

    # Initialize progress files
    update_progress(outer_file_path, 0)  # Set outer progress to 0%
    update_progress(inner_file_path, 0)  # Set inner progress to 0%

    # Progress bar configuration
    total_outer_iterations = read_progress("zsize.txt")  # Number of overall steps
    inner_iterations = 100  # Total steps in the inner progress bar (treated as percentage)

    # Run the main function
    main(outer_file_path, inner_file_path, total_outer_iterations, inner_iterations)
    
