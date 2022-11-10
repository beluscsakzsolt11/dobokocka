dobokocka = 0

def on_gesture_shake():
    global dobokocka
    basic.show_leds("""
        # . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.show_leds("""
        # # . . .
                # # . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    basic.pause(1)
    basic.show_leds("""
        # # # . .
                # # # . .
                # # # . .
                . . . . .
                . . . . .
    """)
    basic.pause(20)
    basic.show_leds("""
        # # # # .
                # # # # .
                # # # # .
                # # # # .
                . . . . .
    """)
    basic.pause(120)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.pause(2000)
    dobokocka = randint(1, 6)
    if dobokocka == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    if dobokocka == 2:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . .
        """)
    if dobokocka == 3:
        basic.show_leds("""
            . . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . .
        """)
    if dobokocka == 4:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . . . .
                        . . . . .
                        # . . . #
        """)
    if dobokocka == 5:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        . . # . .
                        . . . . .
                        # . . . #
        """)
    if dobokocka == 6:
        basic.show_leds("""
            # . . . #
                        . . . . .
                        # . . . #
                        . . . . .
                        # . . . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
