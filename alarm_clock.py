import datetime
import time
import pygame



def set_time(alarm):
    print(f"Alarm set for {alarm}")
    sound_file = "Projects\stay.mp3"
    is_running=True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time==alarm:
            print("Wake up")

            pygame.mixer.init() #mixer = to load or play he song
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running=False
        time.sleep(1)



if __name__=="__main__":
    alarm = input("enter the alarm time(HH:MM:SS): ")
    set_time(alarm)