#!/usr/bin/env python3
"""
Validate that the emotion mappings in the database make neurobiological sense.
"""

from src.engine import _df, CHEM_COLS
import pandas as pd

def analyze_emotion_chemistry():
    """Analyze if the chemical profiles make sense for different emotion categories"""
    print("🧬 Neurochemical Analysis by Emotion Category")
    print("=" * 60)
    
    # Group by emotion category and analyze averages
    category_stats = _df.groupby('emotion_category')[CHEM_COLS].agg(['mean', 'std']).round(2)
    
    for category in ['Positive', 'Negative', 'Neutral', 'Mixed']:
        if category in category_stats.index:
            print(f"\n{category.upper()} EMOTIONS:")
            for chem in CHEM_COLS:
                mean_val = category_stats.loc[category, (chem, 'mean')]
                std_val = category_stats.loc[category, (chem, 'std')]
                print(f"  {chem:15}: {mean_val:6.1f} ± {std_val:5.1f}")

def find_interesting_patterns():
    """Find emotions with interesting neurochemical patterns"""
    print("\n🔍 Interesting Neurochemical Patterns")
    print("=" * 60)
    
    # High dopamine emotions (reward/motivation)
    high_dopamine = _df.nlargest(5, 'dopamine')[['emotion', 'emotion_category', 'dopamine']]
    print("\nHighest Dopamine (Reward/Motivation):")
    for _, row in high_dopamine.iterrows():
        print(f"  {row['emotion']:15} ({row['emotion_category']:8}): {row['dopamine']:5.1f}")
    
    # High cortisol emotions (stress)
    high_cortisol = _df.nlargest(5, 'cortisol')[['emotion', 'emotion_category', 'cortisol']]
    print("\nHighest Cortisol (Stress):")
    for _, row in high_cortisol.iterrows():
        print(f"  {row['emotion']:15} ({row['emotion_category']:8}): {row['cortisol']:5.1f}")
    
    # High serotonin emotions (well-being)
    high_serotonin = _df.nlargest(5, 'serotonin')[['emotion', 'emotion_category', 'serotonin']]
    print("\nHighest Serotonin (Well-being):")
    for _, row in high_serotonin.iterrows():
        print(f"  {row['emotion']:15} ({row['emotion_category']:8}): {row['serotonin']:5.1f}")
    
    # High oxytocin emotions (bonding)
    high_oxytocin = _df.nlargest(5, 'oxytocin')[['emotion', 'emotion_category', 'oxytocin']]
    print("\nHighest Oxytocin (Bonding/Love):")
    for _, row in high_oxytocin.iterrows():
        print(f"  {row['emotion']:15} ({row['emotion_category']:8}): {row['oxytocin']:5.1f}")

def validate_biological_plausibility():
    """Check if the emotion-chemistry mappings are biologically plausible"""
    print("\n✅ Biological Plausibility Check")
    print("=" * 60)
    
    # Check if positive emotions generally have lower cortisol
    positive_cortisol = _df[_df['emotion_category'] == 'Positive']['cortisol'].mean()
    negative_cortisol = _df[_df['emotion_category'] == 'Negative']['cortisol'].mean()
    
    print(f"Average cortisol in positive emotions: {positive_cortisol:.1f}")
    print(f"Average cortisol in negative emotions: {negative_cortisol:.1f}")
    
    if positive_cortisol < negative_cortisol:
        print("✅ PASS: Positive emotions have lower cortisol (less stress)")
    else:
        print("❌ FAIL: Expected positive emotions to have lower cortisol")
    
    # Check if fear has high cortisol
    fear_row = _df[_df['emotion'] == 'fear']
    if not fear_row.empty:
        fear_cortisol = fear_row['cortisol'].iloc[0]
        print(f"\nFear cortisol level: {fear_cortisol:.1f}")
        if fear_cortisol > 50:
            print("✅ PASS: Fear has high cortisol (stress response)")
        else:
            print("❌ FAIL: Expected fear to have high cortisol")
    
    # Check if love/bonding emotions have high oxytocin
    bonding_emotions = ['love', 'compassion', 'empathy', 'trust']
    bonding_oxytocin = []
    for emotion in bonding_emotions:
        emotion_row = _df[_df['emotion'] == emotion]
        if not emotion_row.empty:
            bonding_oxytocin.append(emotion_row['oxytocin'].iloc[0])
    
    if bonding_oxytocin:
        avg_bonding_oxytocin = sum(bonding_oxytocin) / len(bonding_oxytocin)
        overall_avg_oxytocin = _df['oxytocin'].mean()
        print(f"\nAverage oxytocin in bonding emotions: {avg_bonding_oxytocin:.1f}")
        print(f"Overall average oxytocin: {overall_avg_oxytocin:.1f}")
        
        if avg_bonding_oxytocin > overall_avg_oxytocin:
            print("✅ PASS: Bonding emotions have above-average oxytocin")
        else:
            print("❌ FAIL: Expected bonding emotions to have high oxytocin")

if __name__ == '__main__':
    analyze_emotion_chemistry()
    find_interesting_patterns()
    validate_biological_plausibility()
