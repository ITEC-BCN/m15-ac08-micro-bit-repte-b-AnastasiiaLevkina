tempo = 0

def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global tempo
    tempo = input.rotation(Rotation.PITCH)
    music.play(music.string_playable("C5 B A G F E D C ", tempo),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)
