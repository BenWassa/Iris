from engine import infer_emotion

def test_sad_like():
    """Test that high cortisol + low dopamine patterns map to negative emotions"""
    emo, conf = infer_emotion(
        {"dopamine":20,"serotonin":30,"oxytocin":25,"cortisol":70,"norepinephrine":60}
    )
    assert conf > 0.6

def test_joy_like():
    """Test that high dopamine + low cortisol patterns map to positive emotions"""
    emo, conf = infer_emotion(
        {"dopamine":80,"serotonin":25,"oxytocin":15,"cortisol":5,"norepinephrine":20}
    )
    assert conf > 0.8
    # Should be a positive emotion
    from src.engine import _df
    emotion_category = _df[_df['emotion'] == emo]['emotion_category'].iloc[0]
    assert emotion_category == 'Positive'

def test_fear_pattern():
    """Test that high cortisol patterns map to fear-like emotions"""
    emo, conf = infer_emotion(
        {"dopamine":5,"serotonin":15,"oxytocin":5,"cortisol":85,"norepinephrine":20}
    )
    assert conf > 0.9
    assert emo in ['fear', 'anxiety', 'panic', 'terror', 'dread']

def test_love_pattern():
    """Test that high oxytocin patterns map to bonding emotions"""
    emo, conf = infer_emotion(
        {"dopamine":20,"serotonin":25,"oxytocin":80,"cortisol":10,"norepinephrine":15}
    )
    assert conf > 0.8
    # Should be related to bonding/connection
    assert emo in ['love', 'ardor', 'admiration', 'trust', 'compassion', 'empathy']
