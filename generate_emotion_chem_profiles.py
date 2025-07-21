import csv
import os
import random
import numpy as np
from nltk.corpus import wordnet as wn
import nltk

# Ensure wordnet is available
try:
    wn.synsets('test')
except LookupError:
    nltk.download('wordnet')

emotions = [
    'awe','schadenfreude','liminality','serenity','melancholy','euphoria','nostalgia','frustration',
    'anticipation','perplexity','jealousy','compassion','apprehension','apathy','solace','yearning',
    'ardor','ennui','jubilation','remorse','suspicion','gratitude','trepidation','astonishment',
    'pride','shame','admiration','wonder','guilt','confusion','respect','relief','love','hatred',
    'contempt','trust','anger','fear','sadness','happiness','disgust','surprise','hope','despair',
    'ecstasy','anxiety','boredom','curiosity','envy','acceptance','defeat','determination',
    'embarrassment','humility','indignation','inspiration','joy','loneliness','obsession','optimism',
    'pessimism','regret','resilience','satisfaction','synergy','tranquility','vulnerability','warmth',
    'zeal','agitation','bewilderment','calmness','discouragement','empathy','fascination','glee',
    'heartbreak','kinship','longing','mischief','openness','panic','quiescence','resentment','triumph',
    'unease','wistfulness','exuberance','gloom','detachment','forbearance','bliss','drive','elation',
    'fatigue','generosity','hurt','illumination','joviality','kindness'
]

fallback = {
    'schadenfreude': ['gloating', 'malicious joy'],
    'liminality': ['in-betweenness', 'threshold state'],
    'euphoria': ['ecstasy', 'elation'],
    'nostalgia': ['homesickness', 'reminiscence'],
    'perplexity': ['confusion', 'bewilderment'],
    'jealousy': ['envy', 'possessiveness'],
    'gratitude': ['thankfulness', 'appreciation'],
    'trepidation': ['dread', 'unease'],
    'astonishment': ['amazement', 'surprise'],
    'hatred': ['loathing', 'abhorrence'],
    'happiness': ['joyfulness', 'contentment'],
    'despair': ['hopelessness', 'desperation'],
    'anxiety': ['nervousness', 'worry'],
    'humility': ['modesty', 'meekness'],
    'indignation': ['outrage', 'resentment'],
    'optimism': ['hopefulness', 'positivity'],
    'pessimism': ['negativity', 'fatalism'],
    'resilience': ['toughness', 'adaptability'],
    'synergy': ['cooperation', 'teamwork'],
    'vulnerability': ['exposure', 'susceptibility'],
    'empathy': ['understanding', 'compassion'],
    'wistfulness': ['longing', 'pensiveness']
}

def get_synonyms(word):
    syns = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            name = l.name().replace('_', ' ')
            if name.lower() != word.lower() and name.lower() not in syns:
                syns.append(name.lower())
            if len(syns) >= 2:
                return syns[:2]
    # Fallback
    if word in fallback:
        for s in fallback[word]:
            if s.lower() not in syns:
                syns.append(s.lower())
            if len(syns) >= 2:
                return syns[:2]
    # Pad if still not enough
    while len(syns) < 2:
        syns.append(word)
    return syns[:2]

def description(emotion):
    return f"{emotion.capitalize()} is a nuanced emotion that surfaces in particular moments, shaping thoughts, behaviors, relationships, insights, and personal growth for many."

random.seed(42)
os.makedirs('data', exist_ok=True)
outfile = os.path.join('data', 'emotion_chem_profiles.csv')

with open(outfile, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['emotion','dopamine','serotonin','oxytocin','cortisol','norepinephrine','syn1','syn2','description'])
    for emotion in emotions:
        levels = np.random.dirichlet(np.ones(5)) * 100
        levels = [round(v,2) for v in levels]
        syn1, syn2 = get_synonyms(emotion)
        desc = description(emotion)
        writer.writerow([emotion] + levels + [syn1, syn2, desc])

print(f"CSV saved to {outfile}")
