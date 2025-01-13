import sys
import time

# Characters for the spinner
spinner = ['|', '/', '-', '\\', '-']


# Spinner function
def spin(duration=5, interval=0.2):
    end_time = time.time() + duration  # Run spinner for `duration` seconds
    while time.time() < end_time:
        for frame in spinner:
            # Print the spinner character
            sys.stdout.write(f'\r{frame} ')
            sys.stdout.flush()  # Force the output to display immediately
            time.sleep(interval)  # Wait for `interval` seconds


# Run the spinner
spin()
