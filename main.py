for index in range(4):
    basic.show_leds("""
        # # # # #
        # . . . .
        # . . . .
        # . . . .
        # # # # #
        """)
    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)
    basic.show_leds("""
        # # # # #
        # . . . .
        # # # # #
        . . . . #
        # # # # #
        """)
    basic.pause(500)
    basic.clear_screen()
    basic.pause(500)