input.onButtonPressed(Button.A, function () {
    if (minimode == true) {
        minimode = false
    } else {
        minimode = true
    }
    printLED()
})
input.onGesture(Gesture.Shake, function () {
    stepCount += 1
    // Fix lag issues
    if (stepCount < 10 && ledON == true) {
        printLED()
    }
    if (stepCount > 1 && Math.log(stepCount) / Math.log(10) % 1 == 0 && stepCount <= 10000) {
        melody()
    }
})
function printLED () {
    basic.clearScreen()
    if (minimode == false) {
        basic.showNumber(stepCount)
    } else {
        if (stepCount % 2 == 0) {
            basic.showIcon(IconNames.SmallSquare)
        } else {
            basic.showIcon(IconNames.Square)
        }
    }
}
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    stepCount = 0
    // Fix lag issues
    if (ledON == true && minimode == false) {
        basic.showNumber(stepCount)
    } else {
        basic.showIcon(IconNames.Yes)
    }
})
input.onButtonPressed(Button.B, function () {
    if (ledON == true) {
        basic.clearScreen()
        ledON = false
    } else {
        ledON = true
    }
    if (stepCount < 10 && ledON == true) {
        printLED()
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
let minimode = false
let ledON = false
let stepCount = 0
music.setTempo(134)
basic.showNumber(stepCount)
ledON = true
minimode = false
basic.forever(function () {
    if (stepCount >= 10 && ledON == true) {
        printLED()
    } else if (stepCount >= 10 && ledON == false) {
        basic.clearScreen()
    }
})
