#Check Alarm after adding Sound Effects

import pygame

pygame.mixer.init()
alarm_sound = pygame.mixer.Sound('alarm.wav')  # Replace with your sound file

def check_alarm(alarm_hour, alarm_minute):
    while True:
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Wake up! It's time!")
            alarm_sound.play()
            time.sleep(10)  # Keep the sound playing for 10 seconds
            break
        time.sleep(10)
