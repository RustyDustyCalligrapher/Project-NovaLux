import time
import os

ASCII_ART = r"""
           .     .       .  .   . .   .   . .    +  .
     .     .  :     .    .. :. .___---------___.
          .  .   .    .  :.:. _\"._||_||_||_||_||__
       .  :       .  .  .:../ /_/ /_/ /_/ /_/ /_/ /\
           .   . :: +. :.:/ ||_||_||_||_||_||_||/::\
    .  :    .     . _ ::::/::\__/__/__/__/__/__/:::\
     .. . .   . - : :.:./ / /__/__/__/__/__/__/\:::\
       .     .     . :..|::||   WAKING JOY...   |::|
           +   .    .:..|::||    PLEASE WAIT    |::|
                  .  .::\::/____________________/::/
       .   .  +   . .:::""                         """"""" 
"""

LAUNCH_MESSAGE = "\nJoy is awakening..."

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wake_sequence():
    clear()
    print("Launching Project NovaLux")
    for c in "Initializing thoughts...":
        print(c, end='', flush=True)
        time.sleep(0.05)
    time.sleep(1)
    print("\nLoading memories...")
    time.sleep(1)
    print("\nEstablishing connection...")
    time.sleep(1.5)
    clear()
    print(ASCII_ART)
    time.sleep(2)
    print(LAUNCH_MESSAGE)
    time.sleep(2)
    print("\n✅ Joy is now awake. Access her at http://localhost:7860")

if __name__ == "__main__":
    wake_sequence()
