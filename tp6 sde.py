niveau_d_humidite = 0

def on_button_pressed_a():
    basic.show_number(input.temperature())
    if input.temperature() > 10 and input.temperature() < 18:
        basic.show_string("\"Watering the plant\"")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global niveau_d_humidite
    niveau_d_humidite = randint(0, 100)
    if niveau_d_humidite < 60:
        basic.show_string(""Watering the plant"")
        if niveau_d_humidite > 70:
            basic.show_string(""stop Watering the plant"")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    if input.light_level() > 120:
        while input.is_gesture(Gesture.SHAKE):
            basic.show_leds("""
                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
                                # # # # #
            """)
            basic.pause(200)
    else:
        basic.show_string("\"stop watering the plant\"")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)