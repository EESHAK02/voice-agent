from components.asr import transcribe
def test_asr_returns_text():
    audio_data, sr = load_test_audio()
    text = transcribe(audio_data, sr)

    assert isinstance(text, str)
    assert len(text) > 0
