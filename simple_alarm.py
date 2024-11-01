import time
from datetime import datetime

def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format (24-hour): ")
    try:
        # Parse the input time
        alarm_hour, alarm_minute = map(int, alarm_time.split(":"))
        return (alarm_hour, alarm_minute)
    except ValueError:
        print("Invalid time format! Please enter in HH:MM format.")
        return set_alarm()

def check_alarm(alarm_hour, alarm_minute):
    while True:
        # Get the current time
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        # Check if current time matches the alarm time
        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Wake up! It's time!")
            # Optional: Play a sound here (see below for sound instructions)
            break
        time.sleep(10)  # Check every 10 seconds

def main():
    print("Welcome to the Simple Alarm Clock")
    alarm_hour, alarm_minute = set_alarm()
    print(f"Alarm set for {alarm_hour:02}:{alarm_minute:02}")
    check_alarm(alarm_hour, alarm_minute)

if __name__ == "__main__":
    main()
