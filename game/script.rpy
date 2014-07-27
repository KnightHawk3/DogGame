################################################################################
## Dog Game
##
## Copyright (c) 2014 Melody Kelly and Tiana Collier
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.
##
################################################################################

# Declare characters used by this game.
define mc = Character('[name]', color="#c8ffc8")
define dog = Character('[dogname]', color="#000000")
define vet = Character('Vet', color="#000000")
image mc normal = "mc.png"
image dog normal = "dog.gif"
image vet normal = 'vet.png'

# Amount you have in dollars, decimal places are cents
define cash = 1500
# Happiness Percentage
define happiness = 80

# The game starts here.
label start:
    play music "ambient.mp3" fadein 10.0 fadeout 1.0
    python:
        name = renpy.input("What is your name?")
        dogname = renpy.input("What is your dog's name?")
        # You can use .strip() on this variable if
        # you want to remove spaces

    show vet normal at right
    show mc normal at left

    vet "I have bad news for you."
    "When I hear this, my heart sinks to my stomach. Frankly, I don't really know what to expect."
    vet "Our little friend [dogname] here has a bad case of osteosarcoma."

    mc "I don't know what that means and I don't like the sound of it."

    vet "Ah, sorry."
    vet "Put simply, [dogname] has bone cancer... It's normally treatable, but the cancer has spread past [dogname]'s limbs to the point where treatment won't yield much of a result."
    vet "Actually, there's not a whole lot we can do for [dogname] at this point other than give them painkillers."

    mc "What's that meant to mean?"
    vet "..."

    "There's a short silence as he tries to find the right words."
    "Truth be told, I already know what he's trying to say. I just don't know if I believe it."

    vet "..."
    vet "It means [dogname] may not have much longer to live."
    mc "..."

    "And silence suffocates the room again, save for the noise of the TV in the background."
    "The vet looks just as uncomfortable as I feel, really. What more is there to say?"
    show dog normal at center
    "Feeling anxious under his gaze, I look down at [dogname], and he wags his tail at me in acknowledgement."
    "Despite the news, [dogname] seems blissfully unaware of the situation."

    mc "Oh..."

    "A dismayed remark is the only thing that seems to come out of my mouth. I feel like an idiot standing there with my mouth open, but somehow I can't voice any of the questions on the tip of my tongue."
    "Maybe it was the sheer tension of the situation that was causing that."

    mc "..."
    mc "How long?"

    "My voice is small, and when I look up to meet the vet's eyes I sense the tiniest bit of guilt in his expression."

    vet "I... really couldn't tell you. Could be tomorrow, could be two months, could be six. Not any longer than that, though."

    "And that's that. That's it. Come six months and [dogname] is as good as dead. It finally hits me that [dogname], my companion for the past two years, is going to be dead in six month's time."
    "The revelation is too sudden to inspire tears. Instead, all I feel is a deep-rooted sense of sadness, and an emptiness in my chest that makes me feel almost hollow."

    mc "Is there nothing I can do, then?"

    "It's then that the vet seems to regain some of his composure."

    vet "Well, you have two options. You can put down [dogname], which is easy and painless, or you can continue to look after 'em until they pass away."
    vet "The only catch there is that they're gonna be in a bit of pain, unless you provide pain medication, but even then the effectiveness isn't guaranteed."

    "I'm immediately torn. I was hoping for a simple solution, but when presented with a situation like this, I'm immediately thrown into turmoil."
    "[dogname] has stayed by my side for two years and become an irreplaceable part of my life. I can't bear to say goodbye now, but I also can't bear sitting and waiting and not knowing when [dogname] is going to die."

    mc "There's no way of treating this?"
    vet "None."

    "He shakes his head firmly, and somehow it only sends me further into indecision."

    vet "What do you want to do?"

    "His gaze seems to soften a bit, but it doesn't detract from the sense of urgency his statement gives. What /should/ I do?"
    "I feel like I should make the decision now. If I don't make it now, I'll never make it."
    "A quick, painless death?"
    "Or do I let [dogname] live a longer, albeit steadily deteriorating life?"

    hide mc normal
    hide vet normal
    menu:
        "A quick, painless death?":
            jump putdown
        "Or do I let [dogname] live a longer, albeit steadily deteriorating life?":
            jump letlive

label putdown:
    play music "sad.mp3" fadein 1.0
    "Bye bye doggie :^("
    return

label letlive:
    "Hello doggie :^)"
    return
