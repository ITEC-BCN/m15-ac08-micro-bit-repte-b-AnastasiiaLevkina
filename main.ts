let tempo = 0
input.onButtonPressed(Button.A, function () {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Dadadadum), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    tempo = input.rotation(Rotation.Pitch)
    music.play(music.stringPlayable("C5 B A G F E D C ", tempo), music.PlaybackMode.UntilDone)
})
