def generate_audio(text):
    from gtts import gTTS
    import os
    audio_path = "/tmp/audio.mp3"
    tts = gTTS(text)
    tts.save(audio_path)
    return audio_path
