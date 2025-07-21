/**
 * Project Iris - Enhanced Emotion Dot Visualization
 * Handles smooth 2D emotion visualization with SVG animations
 */

import { emotionCoords, canvasConfig, plotDimensions, getEmotionQuadrant } from './emotionCoords.js';

// Animation configuration
const animationConfig = {
    duration: '0.8s',
    easing: 'cubic-bezier(0.4, 0, 0.2, 1)',
    glowIntensity: 10
};

// Convert valence/arousal coordinates to SVG pixel coordinates
export function coordsToSVG(valence, arousal) {
    const x = canvasConfig.margin.left + (valence * plotDimensions.width);
    const y = canvasConfig.margin.top + ((1 - arousal) * plotDimensions.height); // Flip Y axis
    return { x, y };
}

// Main emotion dot update function with enhanced features
export function updateEmotionDot(emotionName) {
    const emotionData = emotionCoords[emotionName];

    if (!emotionData) {
        console.warn(`No coordinates found for emotion: ${emotionName}`);
        return;
    }

    const coords = emotionData;
    const svgCoords = coordsToSVG(coords.valence, coords.arousal);
    
    // Get DOM elements
    const dot = document.getElementById('emotion-dot');
    const label = document.getElementById('emotion-label');
    
    if (!dot || !label) {
        console.warn('Emotion visualization elements not found');
        return;
    }

    // Update dot position with smooth animation
    dot.setAttribute('cx', svgCoords.x);
    dot.setAttribute('cy', svgCoords.y);
    
    // Update label position and text
    label.setAttribute('x', svgCoords.x);
    label.setAttribute('y', svgCoords.y - 20);
    label.textContent = emotionName.charAt(0).toUpperCase() + emotionName.slice(1);
    
    // Add enhanced visual feedback
    updateDotVisualFeedback(dot, emotionData);
    
    // Log for debugging
    console.log(`🎯 Updated emotion visualization: ${emotionName} → [${coords.valence.toFixed(2)}, ${coords.arousal.toFixed(2)}] (${emotionData.quadrant})`);
}

// Enhanced visual feedback for emotion transitions
function updateDotVisualFeedback(dot, emotionData) {
    // Update dot color based on quadrant
    const quadrantColors = {
        'Excitement': '#00FFE0',     // Cyan for positive high-arousal
        'Stress': '#FF6B6B',         // Red for negative high-arousal  
        'Depression': '#6B73FF',     // Blue for negative low-arousal
        'Contentment': '#4ECDC4'     // Teal for positive low-arousal
    };
    
    const color = quadrantColors[emotionData.quadrant] || '#00FFE0';
    dot.setAttribute('fill', color);
    dot.style.filter = `drop-shadow(0 0 ${animationConfig.glowIntensity}px ${color})`;
}

// Global function for external integration (matches emotion_dot_visualization.html API)
export function updateEmotionVisualization(emotion) {
    return updateEmotionDot(emotion);
}

// Initialize dot in center position
export function initializeEmotionDot() {
    const dot = document.getElementById('emotion-dot');
    const label = document.getElementById('emotion-label');
    
    if (dot && label) {
        // Center position
        const centerX = canvasConfig.width / 2;
        const centerY = canvasConfig.height / 2;
        
        dot.setAttribute('cx', centerX);
        dot.setAttribute('cy', centerY);
        label.setAttribute('x', centerX);
        label.setAttribute('y', centerY - 20);
        label.textContent = 'Adjust Sliders';
    }
}

// Utility function to simulate emotion transitions for testing
export function simulateEmotionInference(emotion) {
    const emotionData = emotionCoords[emotion];
    if (!emotionData) return null;
    
    return {
        emotion: emotion,
        confidence: Math.random() * 0.3 + 0.7, // 0.7-1.0
        description: emotionData.description,
        quadrant: emotionData.quadrant,
        coordinates: {
            valence: emotionData.valence,
            arousal: emotionData.arousal
        }
    };
}

// Auto-demo functionality for testing
export function startEmotionDemo() {
    const emotions = Object.keys(emotionCoords);
    let index = 0;
    
    const demoInterval = setInterval(() => {
        updateEmotionDot(emotions[index]);
        console.log(`🎭 Demo: Showing ${emotions[index]}`);
        index = (index + 1) % emotions.length;
    }, 3000);
    
    // Return interval ID so it can be stopped
    return demoInterval;
}

// Make functions available globally for integration
if (typeof window !== 'undefined') {
    window.updateEmotionVisualization = updateEmotionVisualization;
    window.updateEmotionDot = updateEmotionDot;
    window.coordsToSVG = coordsToSVG;
    window.initializeEmotionDot = initializeEmotionDot;
}
