# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define mc = Character('[name]', color="#c8ffc8")
define dog = Character('[dogname]', color="#000000")
define cash = 1000
# The game starts here.
label start:
    play music "ambient.mp3" fadein 10.0 fadeout 1.0
    python:
        name = renpy.input("What is your name?")
        # You can use .strip() on this variable if
        # you want to remove spaces

    "Oh man, I can't wait to buy Call of Duty 16"

    "But I have only $[cash], and I still need to pay rent, food, etc"
    mc "Can I have a loan?"
    "Is that a dog!"
    if layout.yesno_prompt(None, "Save the dog?"):
        if cash > 1500:
            jump savedog
        else:
            "I can't afford a dog, shame it's going to die"
            jump deaddog
    else:
        jump deaddog

label savedog:
    python:
        dogname = renpy.input("What will you name it?")

    dog "I am a talking dog."
    return

label deaddog:
    play music "sad.mp3" fadein 1.0
    "The dog dies, the end."
    return
