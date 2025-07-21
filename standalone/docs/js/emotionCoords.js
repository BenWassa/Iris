/**
 * Project Iris - Enhanced Emotion Coordinate Mapping
 * Defines the valence-arousal coordinates for each core emotion with rich metadata
 */

// Enhanced emotion coordinate mapping with descriptions and quadrant info
export const emotionCoords = {
    happiness: { 
        valence: 0.9, 
        arousal: 0.85, 
        description: "High energy, positive state",
        quadrant: "Excitement"
    },
    anger: { 
        valence: 0.2, 
        arousal: 0.9, 
        description: "High energy, negative state",
        quadrant: "Stress"
    },
    sadness: { 
        valence: 0.25, 
        arousal: 0.3, 
        description: "Low energy, negative state",
        quadrant: "Depression"
    },
    fear: { 
        valence: 0.15, 
        arousal: 0.8, 
        description: "High alertness, threat response",
        quadrant: "Stress"
    },
    disgust: { 
        valence: 0.2, 
        arousal: 0.45, 
        description: "Low-moderate energy, aversive",
        quadrant: "Depression"
    }
};

// Quadrant definitions for emotional interpretation
export const emotionQuadrants = {
    'high-valence-high-arousal': 'Excitement',
    'low-valence-high-arousal': 'Stress',
    'low-valence-low-arousal': 'Depression',
    'high-valence-low-arousal': 'Contentment'
};

// Determine which quadrant an emotion falls into
export function getEmotionQuadrant(valence, arousal) {
    const isHighValence = valence > 0.5;
    const isHighArousal = arousal > 0.5;
    
    if (isHighValence && isHighArousal) return 'Excitement';
    if (!isHighValence && isHighArousal) return 'Stress';
    if (!isHighValence && !isHighArousal) return 'Depression';
    return 'Contentment';
}

// Canvas configuration for SVG visualization
export const canvasConfig = {
    width: 600,
    height: 500,
    margin: { left: 60, right: 60, top: 50, bottom: 50 }
};

// Calculate plot dimensions
export const plotDimensions = {
    width: canvasConfig.width - canvasConfig.margin.left - canvasConfig.margin.right,
    height: canvasConfig.height - canvasConfig.margin.top - canvasConfig.margin.bottom
};