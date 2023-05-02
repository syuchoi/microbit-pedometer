input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    stepCount = 0
})
input.onGesture(Gesture.Shake, function () {
    stepCount += 1
    if (stepCount == 10 || stepCount == 100 || stepCount == 1000 || stepCount == 10000) {
        melody()
    }
})
function melody () {
    music.playTone(196, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(262, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(659, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(784, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Half))
    music.playTone(659, music.beat(BeatFraction.Eighth))
    music.rest(music.beat(BeatFraction.Eighth))
    music.playTone(784, music.beat(BeatFraction.Whole))
}
let stepCount = 0
music.setTempo(134)
basic.forever(function () {
    basic.showNumber(stepCount)
})
