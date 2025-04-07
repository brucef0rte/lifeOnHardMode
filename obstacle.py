# Using the same animation technique from animation.py
# Create a list of frame numbers from frames list
# If player input is received within correct frame # range
# Player successfully passes obstacle
# If not: -2 Stamina & try again

import time, os, keyboard, math

skull = '''
       @@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@/      \@@@/   @
@@@@@@@@@@@@@@@@\      @@  @___@
@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@
@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@
 @@@@@@@@@@@@@@@/,/,/./'/_|.\'\,\\
   @@@@@@@@@@@@@|  | | | | | | | |
                 \_|_|_|_|_|_|_|_|'''

frames = [
    '''
    |   |   |   |   |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
    '''
    | o |   |   |   |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
        '''
    |   | o |   |   |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
        '''
    |   |   | o |   |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
            '''
    |   |   |   | o |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
            '''
    |   |   |   |   | o |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',
]
win = [
        '''
    |   |   | o |   |   |
    | X | X |   | X | X |
    |   |   |   |   |   |
    ''',        '''
    |   |   |   |   |   |
    | X | X | o | X | X |
    |   |   |   |   |   |
    ''',
        '''
    |   |   |   |   |   |
    | X | X |   | X | X |
    |   |   | o |   |   |
              |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    ''',
]
delay = 1.25
# count the frames, return numbers to list
def cel_maker(frames):
    frame_count = len(frames)
    frame_ints = []
    for i in range(frame_count):
        frame_ints.append(i)
     # create tuples of frame, frame #
    cels = zip(frames, frame_ints)
    cels = list(cels)
    return cels

# create list of tuples for each animation
main_animation = cel_maker(frames) * 100
win_frames = cel_maker(win)

def winAnimation():
    for frame in win_frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You win!!!")
        print(frame[0])
        time.sleep(delay)

key_pressed = False  # Global flag to track keypress

def on_key_event(event):
    global key_pressed
    if event.name == "a":  # Check if the "A" key was pressed
        key_pressed = True

keyboard.hook(on_key_event)  # Hook the keypress event

def game_loop(cels):
    global key_pressed
    target_index = (len(cels) // 2) / 100  # Example: Target index is halfway through the frames
    for frame, index in cels:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
        print("Press A when it's safe to pass!")
        print(f"Current Index: {index}, Target Index: {target_index}")
        print(frame)

        # Reset key_pressed for each frame
        key_pressed = False
        start_time = time.time()
        while time.time() - start_time < delay:
            if key_pressed and index == target_index:
                winAnimation()
                return
            elif key_pressed:
                print(f"{skull}")
                return

        # Continue to the next frame after the delay


while True:
    game_loop(main_animation)
    break