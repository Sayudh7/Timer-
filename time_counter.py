import time
import winsound

seconds_input = int(input("Enter seconds: "))

if seconds_input <= 0:
    print("Enter a positive number")
else:
    for remaining in range(seconds_input, 0, -1):
        hours = remaining // 3600
        minutes = (remaining // 60) % 60
        seconds = remaining % 60

        print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="")
        time.sleep(1)

    print("\nTime's up!")

    frequency = 2500
    duration = 1000

    for _ in range(3):
        winsound.Beep(frequency, duration)
        time.sleep(1)
