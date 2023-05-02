def on_button_pressed_a():
    global stepCount
    basic.clear_screen()
    stepCount = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global stepCount
    stepCount += 1
    if stepCount == 10 or stepCount == 100 or stepCount == 1000 or stepCount == 10000:
        melody()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

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
stepCount = 0
music.set_tempo(134)

def on_forever():
    basic.show_number(stepCount)
basic.forever(on_forever)
