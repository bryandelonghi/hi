def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    basic.show_string("bye")
basic.forever(on_forever)
