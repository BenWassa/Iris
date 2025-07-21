from engine import infer_emotion

def test_sad_like():
    emo, conf = infer_emotion(
        {"dopamine":20,"serotonin":30,"oxytocin":25,"cortisol":70,"norepinephrine":60}
    )
    assert conf > 0.6
