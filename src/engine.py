import os
import pandas as pd
import numpy as np

# Load emotion chemical profiles on import
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'emotion_core_5.csv')
_df = pd.read_csv(DATA_PATH)

CHEM_COLS = ['dopamine', 'serotonin', 'oxytocin', 'cortisol', 'norepinephrine']


def infer_emotion(neuro_dict):
    """Infer the closest emotion from a neurotransmitter map.

    Parameters
    ----------
    neuro_dict : dict
        Dictionary with the five neurotransmitter keys.

    Returns
    -------
    tuple
        (label, confidence) where confidence is the cosine similarity in [0, 1].
    """
    vec = np.array([neuro_dict[c] for c in CHEM_COLS], dtype=float)
    vec_norm = np.linalg.norm(vec)
    if vec_norm == 0:
        return None, 0.0

    matrix = _df[CHEM_COLS].values
    norms = np.linalg.norm(matrix, axis=1)
    sims = (matrix @ vec) / (norms * vec_norm)
    best_idx = int(np.argmax(sims))
    label = _df.loc[best_idx, 'emotion']
    confidence = float(sims[best_idx])
    return label, confidence


if __name__ == '__main__':
    sample_inputs = [
        {'dopamine': 20, 'serotonin': 30, 'oxytocin': 15, 'cortisol': 10, 'norepinephrine': 25},
        {'dopamine': 50, 'serotonin': 10, 'oxytocin': 20, 'cortisol': 5, 'norepinephrine': 15},
    ]
    for sample in sample_inputs:
        label, conf = infer_emotion(sample)
        print(f"Input {sample} -> {label} (confidence {conf:.2f})")

