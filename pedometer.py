def on_button_pressed_a():
    global minimode
    if minimode == True:
        minimode = False
    else:
        minimode = True
    printLED()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global stepCount
    stepCount += 1
    # Fix lag issues
    if stepCount < 10 and ledON == True:
        printLED()
    if stepCount > 1 and Math.log(stepCount) / Math.log(10) % 1 == 0 and stepCount <= 10000:
        melody()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def printLED():
    basic.clear_screen()
    if minimode == False:
        basic.show_number(stepCount)
    else:
        if stepCount % 2 == 0:
            basic.show_icon(IconNames.SMALL_SQUARE)
        else:
            basic.show_icon(IconNames.SQUARE)

def on_button_pressed_ab():
    global stepCount
    basic.clear_screen()
    stepCount = 0
    # Fix lag issues
    if ledON == True and minimode == False:
        basic.show_number(stepCount)
    else:
        basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global ledON
    if ledON == True:
        basic.clear_screen()
        ledON = False
    else:
        ledON = True
    if stepCount < 10 and ledON == True:
        printLED()
input.on_button_pressed(Button.B, on_button_pressed_b)

def melody():
    music.play_tone(196, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(262, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(659, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(784, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(659, music.beat(BeatFraction.EIGHTH))
    music.rest(music.beat(BeatFraction.EIGHTH))
    music.play_tone(784, music.beat(BeatFraction.WHOLE))
minimode = False
ledON = False
stepCount = 0
music.set_tempo(134)
basic.show_number(stepCount)
ledON = True
minimode = False

def on_forever():
    if stepCount >= 10 and ledON == True:
        printLED()
    elif stepCount >= 10 and ledON == False:
        basic.clear_screen()
basic.forever(on_forever)
