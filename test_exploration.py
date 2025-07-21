#!/usr/bin/env python3
"""
Test exploration script to understand the emotion inference engine behavior.
"""

from src.engine import infer_emotion, _df, CHEM_COLS
import pandas as pd
import numpy as np

def test_basic_emotions():
    """Test some basic emotional patterns"""
    print("🧪 Basic Emotion Pattern Tests")
    print("=" * 50)
    
    test_cases = [
        # High dopamine + low cortisol = positive emotions
        {
            'name': 'High Dopamine (Joy/Euphoria)',
            'levels': {'dopamine': 80, 'serotonin': 20, 'oxytocin': 10, 'cortisol': 5, 'norepinephrine': 15}
        },
        # High cortisol = stress/anxiety
        {
            'name': 'High Cortisol (Stress/Fear)',
            'levels': {'dopamine': 10, 'serotonin': 15, 'oxytocin': 5, 'cortisol': 85, 'norepinephrine': 20}
        },
        # High serotonin = contentment
        {
            'name': 'High Serotonin (Contentment)',
            'levels': {'dopamine': 15, 'serotonin': 80, 'oxytocin': 20, 'cortisol': 10, 'norepinephrine': 10}
        },
        # High oxytocin = love/bonding
        {
            'name': 'High Oxytocin (Love/Bonding)',
            'levels': {'dopamine': 20, 'serotonin': 25, 'oxytocin': 80, 'cortisol': 10, 'norepinephrine': 15}
        },
        # Balanced = neutral
        {
            'name': 'Balanced (Neutral)',
            'levels': {'dopamine': 20, 'serotonin': 20, 'oxytocin': 20, 'cortisol': 20, 'norepinephrine': 20}
        }
    ]
    
    for case in test_cases:
        emotion, confidence = infer_emotion(case['levels'])
        print(f"{case['name']:25} -> {emotion:15} (confidence: {confidence:.3f})")

def test_edge_cases():
    """Test edge cases and extreme values"""
    print("\n🔬 Edge Case Tests")
    print("=" * 50)
    
    edge_cases = [
        # All zeros
        {
            'name': 'All Zeros',
            'levels': {'dopamine': 0, 'serotonin': 0, 'oxytocin': 0, 'cortisol': 0, 'norepinephrine': 0}
        },
        # All max
        {
            'name': 'All Maximum',
            'levels': {'dopamine': 100, 'serotonin': 100, 'oxytocin': 100, 'cortisol': 100, 'norepinephrine': 100}
        },
        # Only dopamine
        {
            'name': 'Only Dopamine',
            'levels': {'dopamine': 100, 'serotonin': 0, 'oxytocin': 0, 'cortisol': 0, 'norepinephrine': 0}
        }
    ]
    
    for case in edge_cases:
        emotion, confidence = infer_emotion(case['levels'])
        emotion_str = emotion if emotion is not None else "None"
        print(f"{case['name']:25} -> {emotion_str:15} (confidence: {confidence:.3f})")

def analyze_database():
    """Analyze the emotion database statistics"""
    print("\n📊 Database Analysis")
    print("=" * 50)
    
    # Category distribution
    print("Emotion Categories:")
    category_counts = _df['emotion_category'].value_counts()
    for category, count in category_counts.items():
        print(f"  {category:10}: {count:2d} emotions")
    
    # Chemical ranges
    print(f"\nNeurochemical Ranges:")
    for chem in CHEM_COLS:
        min_val = _df[chem].min()
        max_val = _df[chem].max()
        mean_val = _df[chem].mean()
        print(f"  {chem:15}: {min_val:5.1f} - {max_val:5.1f} (avg: {mean_val:5.1f})")
    
    # Extreme emotions
    print(f"\nExtreme Emotions:")
    for chem in CHEM_COLS:
        max_idx = _df[chem].idxmax()
        min_idx = _df[chem].idxmin()
        print(f"  Highest {chem:12}: {_df.loc[max_idx, 'emotion']:15} ({_df.loc[max_idx, chem]:.1f})")
        print(f"  Lowest  {chem:12}: {_df.loc[min_idx, 'emotion']:15} ({_df.loc[min_idx, chem]:.1f})")

if __name__ == '__main__':
    test_basic_emotions()
    test_edge_cases()
    analyze_database()
