import datetime
import time
import os
from playsound import playsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting...")
    
    while True:
        # Get current time in HH:MM:SS format
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        if current_time == alarm_time:
            print("⏰ WAKE UP! Time to get moving!")
            
            # Replace 'alarm.mp3' with the path to your actual audio file
            try:
                playsound('alarm.mp3')
            except Exception as e:
                # Fallback beep if the audio file isn't found
                print("\a") 
            break
            
        # Wait 1 second before checking again to save CPU
        time.sleep(1)

# Set your alarm time here (24-hour format: HH:MM:SS)
# Example: "07:30:00" for 7:30 AM or "18:15:00" for 6:15 PM
TARGET_TIME = "14:30:00" 

set_alarm(TARGET_TIME)
