import time
import winsound
x=int(input("enter the seconds"))
for i in reversed(range(1,x+1)):
    seconds=i%60
    minutes=int(i/60)%60
    hours=int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("time's up")
# Play a sound
for y in range(0,3):
    frequency = 2500  # Set Frequency (Hz)
    duration = 1000   # Set Duration (ms) - 1000 ms = 1 second
    winsound.Beep(frequency, duration)
    time.sleep(1)