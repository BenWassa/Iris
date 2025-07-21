export const emotionData = [
    {
        emotion: 'happiness',
        dopamine: 80,
        serotonin: 70,
        oxytocin: 60,
        cortisol: 10,
        norepinephrine: 40,
        description: 'A state of joy, contentment, and positivity.'
    },
    {
        emotion: 'anger',
        dopamine: 30,
        serotonin: 20,
        oxytocin: 10,
        cortisol: 70,
        norepinephrine: 90,
        description: 'A surge of intensity often tied to injustice or frustration.'
    },
    {
        emotion: 'sadness',
        dopamine: 20,
        serotonin: 30,
        oxytocin: 25,
        cortisol: 60,
        norepinephrine: 20,
        description: 'A deep emotional state of loss, reflection, or hurt.'
    },
    {
        emotion: 'fear',
        dopamine: 15,
        serotonin: 10,
        oxytocin: 5,
        cortisol: 80,
        norepinephrine: 80,
        description: 'A heightened alertness in the face of perceived danger.'
    },
    {
        emotion: 'disgust',
        dopamine: 10,
        serotonin: 25,
        oxytocin: 5,
        cortisol: 50,
        norepinephrine: 15,
        description: 'A visceral rejection of something repulsive or wrong.'
    }
];

// Keys in neurotransmitter vector
const CHEM_KEYS = ['dopamine', 'serotonin', 'oxytocin', 'cortisol', 'norepinephrine'];

export function inferEmotion(values) {
    // values: {dopamine: num, serotonin: num, ...}
    const inputVec = CHEM_KEYS.map(k => values[k] || 0);
    const vecNorm = Math.hypot(...inputVec);
    if (vecNorm === 0) {
        return { emotion: null, confidence: 0 };
    }

    let best = null;
    let bestSim = -1;
    for (const row of emotionData) {
        const rowVec = CHEM_KEYS.map(k => row[k]);
        const rowNorm = Math.hypot(...rowVec);
        const dot = rowVec.reduce((sum, val, idx) => sum + val * inputVec[idx], 0);
        const sim = dot / (rowNorm * vecNorm);
        if (sim > bestSim) {
            bestSim = sim;
            best = row;
        }
    }
    return { emotion: best.emotion, confidence: bestSim, description: best.description };
}
