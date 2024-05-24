from screenShot import screenShot
from text import text
import keyboard
import time

def simulate_q_key_press():
    keyboard.press_and_release('q')

def on_enter_pressed(event):
    global done
    if event.name == 'enter':
        while not done:
            SS = screenShot()
            SS.takeScreenShots()
            t = text()
            arr = t.getModNames() 
            print(arr)

            # if arr[0] in allowedEasy:
            #     done = True
            # else:
            #     simulate_q_key_press()
            #     time.sleep(0.25)

def main():
    global done
    done = False

    global allowedEasy
    allowedEasy = ['[EASY] Lootsplosion']
    allowedMedium = []
    allowedHard = []
    AllowedVeryHard = []
    keyboard.on_press(on_enter_pressed)
    while not done:
        time.sleep(0.1)

if __name__ == "__main__":
    main()









# '[EASY] Big Kick Energy'
# '[EASY] Galaxy Brain'
# '[EASY] Lootsplosion'
# '[EASY] Speed Demon'
# '[EASY] More Than Okay Boomer'
# '[EASY] Slayer'

# [MEDIUM] Healy Avenger
# [MEDIUM] Charred Mode
# [MEDIUM] High Voltage
# [MEDIUM] Acid Reign
# [MEDIUM] Chilling Them Softly
# [MEDIUM] Totally Radical
# [MEDIUM] Mob Mentality
# [MEDIUM] Freeze Tag
# [MEDIUM] Floor is Lava
# [MEDIUM] Pain Tolerance

# [HARD] Chain Gang
# [HARD] Drone Ranger
# [HARD] Pool Party
# [HARD] Laser Fare
# [HARD] Boundary Issues
# [HARD] Ticked Off

# [VERY HARD] Buddy System
# [VERY HARD] Post Mortem
# [VERY HARD] Dazed and Infused
# [VERY HARD] Rogue Lite
# [VERY HARD] Not the Face
# [VERY HARD] Holy Crit