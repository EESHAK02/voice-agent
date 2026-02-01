from components.audio_process import record_audio
from components.asr import transcribe
from components.llm import generate_response
from components.tts import synthesize_speech

def test_full_voice_pipeline():
    audio, sr = record_audio(duration=3)
    text = transcribe(audio, sr)

    history = init_session()
    add_turn(history, "user", text)

    reply = generate_response(text, history)
    add_turn(history, "assistant", reply)

    out_audio, out_sr = synthesize_speech(reply)

    assert out_audio is not None
