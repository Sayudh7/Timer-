# Timer
A simple, beginner-friendly Python command-line countdown timer with built-in audio alerts for Windows.
# Simple Python Countdown Timer

A lightweight, beginner-friendly command-line countdown timer written in Python. It tracks hours, minutes, and seconds, and alerts you with a series of audio beeps when the time is up!

## 🚀 Features

* **Dynamic Time Formatting:** Automatically converts total seconds into a standard `HH:MM:SS` countdown format.
* **Real-time Updates:** Updates the clock every second directly in your terminal.
* **Audio Alert:** Uses the Windows `winsound` library to play 3 distinct beeps when the countdown reaches zero.

## 📋 Prerequisites

This script uses the **`winsound`** module, which is built into Python but **only works on Windows operating systems**. 

* Python 3.x Installed
* Windows OS (for the audio alert feature)

## 🔧 How to Run

1.  **Clone the repository** (or download the script file):
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
    ```
2.  **Navigate to the project directory**:
    ```bash
    cd YOUR_REPOSITORY_NAME
    ```
3.  **Run the script**:
    ```bash
    python timer.py
    ```
4.  Enter the total number of seconds you want to count down when prompted!

## 🛠️ How It Works

The script takes your input in total seconds and uses basic math to break it down:
* `hours`: Total seconds divided by 3600.
* `minutes`: Remaining seconds divided by 60.
* `seconds`: The remainder after extracting hours and minutes.

It uses a `for` loop combined with `time.sleep(1)` to pause for exactly one second between updates, creating the countdown effect.

---
💡 *This is a beginner-friendly project created to practice basic loops, math operators, and standard Python libraries.*
