#!/usr/bin/env python3
"""
Enhanced API Integration Test for Project Iris
Tests the enhanced emotion dot visualization integration with the backend API.
"""

import requests
import json
import time

API_URL = 'http://localhost:5000/infer'

def test_enhanced_visualization_integration():
    """Test the enhanced emotion visualization with different patterns"""
    print("🎯 Testing Enhanced Emotion Dot Visualization Integration")
    print("=" * 60)
    
    test_cases = [
        {
            'name': 'High Dopamine → Happiness (Excitement Quadrant)',
            'data': {'dopamine': 80, 'serotonin': 70, 'oxytocin': 60, 'cortisol': 10, 'norepinephrine': 40},
            'expected_quadrant': 'Excitement',
            'expected_color': '#00FFE0'
        },
        {
            'name': 'High Cortisol → Fear (Stress Quadrant)',
            'data': {'dopamine': 20, 'serotonin': 10, 'oxytocin': 5, 'cortisol': 80, 'norepinephrine': 60},
            'expected_quadrant': 'Stress',
            'expected_color': '#FF6B6B'
        },
        {
            'name': 'High Anger Pattern (Stress Quadrant)',
            'data': {'dopamine': 30, 'serotonin': 20, 'oxytocin': 10, 'cortisol': 70, 'norepinephrine': 90},
            'expected_quadrant': 'Stress',
            'expected_color': '#FF6B6B'
        },
        {
            'name': 'Low Energy → Sadness (Depression Quadrant)',
            'data': {'dopamine': 15, 'serotonin': 25, 'oxytocin': 20, 'cortisol': 60, 'norepinephrine': 15},
            'expected_quadrant': 'Depression',
            'expected_color': '#6B73FF'
        },
        {
            'name': 'Balanced Neutral Pattern',
            'data': {'dopamine': 50, 'serotonin': 50, 'oxytocin': 50, 'cortisol': 50, 'norepinephrine': 50},
            'expected_quadrant': 'Variable',
            'expected_color': '#00FFE0'
        }
    ]
    
    print("🧪 Testing API responses and visualization coordinates...")
    print()
    
    for i, case in enumerate(test_cases, 1):
        print(f"{i}. {case['name']}")
        print(f"   Input: {case['data']}")
        
        try:
            response = requests.post(API_URL, json=case['data'], timeout=5)
            
            if response.status_code == 200:
                result = response.json()
                emotion = result['emotion']
                confidence = result['confidence']
                description = result['description']
                
                # Get emotion coordinates for visualization
                coords = get_emotion_coordinates(emotion)
                
                print(f"   ✅ Emotion: {emotion} (confidence: {confidence:.3f})")
                print(f"   📍 Coordinates: Valence={coords['valence']:.2f}, Arousal={coords['arousal']:.2f}")
                print(f"   🎨 Quadrant: {coords['quadrant']} (Color: {coords['color']})")
                print(f"   📝 Description: {description}")
                
                # Validate visualization mapping
                validate_visualization_mapping(emotion, coords, case)
                
            else:
                print(f"   ❌ API Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Connection Error: {e}")
            print(f"   💡 Make sure to start the API server with: python api.py")
        
        print()
        time.sleep(0.1)  # Small delay for better readability

def get_emotion_coordinates(emotion):
    """Get the visualization coordinates for an emotion"""
    emotion_coords = {
        'happiness': {'valence': 0.9, 'arousal': 0.85, 'quadrant': 'Excitement', 'color': '#00FFE0'},
        'anger': {'valence': 0.2, 'arousal': 0.9, 'quadrant': 'Stress', 'color': '#FF6B6B'},
        'sadness': {'valence': 0.25, 'arousal': 0.3, 'quadrant': 'Depression', 'color': '#6B73FF'},
        'fear': {'valence': 0.15, 'arousal': 0.8, 'quadrant': 'Stress', 'color': '#FF6B6B'},
        'disgust': {'valence': 0.2, 'arousal': 0.45, 'quadrant': 'Depression', 'color': '#6B73FF'}
    }
    
    return emotion_coords.get(emotion, {
        'valence': 0.5, 'arousal': 0.5, 'quadrant': 'Neutral', 'color': '#00FFE0'
    })

def validate_visualization_mapping(emotion, coords, test_case):
    """Validate that the emotion maps to the expected visualization properties"""
    valence = coords['valence']
    arousal = coords['arousal']
    
    # Validate coordinate ranges
    if 0.0 <= valence <= 1.0 and 0.0 <= arousal <= 1.0:
        print(f"   ✅ Coordinates within valid range")
    else:
        print(f"   ⚠️  Coordinates outside valid range: V={valence}, A={arousal}")
    
    # Calculate SVG coordinates (matching the frontend logic)
    canvas_width, canvas_height = 600, 500
    margin = {'left': 60, 'right': 60, 'top': 50, 'bottom': 50}
    plot_width = canvas_width - margin['left'] - margin['right']
    plot_height = canvas_height - margin['top'] - margin['bottom']
    
    svg_x = margin['left'] + (valence * plot_width)
    svg_y = margin['top'] + ((1 - arousal) * plot_height)
    
    print(f"   📐 SVG Position: ({svg_x:.1f}, {svg_y:.1f})")
    
    # Validate quadrant logic
    expected_quadrant = determine_quadrant(valence, arousal)
    if expected_quadrant == coords['quadrant']:
        print(f"   ✅ Quadrant mapping correct: {expected_quadrant}")
    else:
        print(f"   ⚠️  Quadrant mismatch: Expected {expected_quadrant}, got {coords['quadrant']}")

def determine_quadrant(valence, arousal):
    """Determine emotional quadrant based on valence and arousal"""
    if valence > 0.5 and arousal > 0.5:
        return 'Excitement'
    elif valence <= 0.5 and arousal > 0.5:
        return 'Stress'
    elif valence <= 0.5 and arousal <= 0.5:
        return 'Depression'
    else:
        return 'Contentment'

def test_visualization_performance():
    """Test the performance of rapid visualization updates"""
    print("⚡ Testing Enhanced Visualization Performance")
    print("=" * 45)
    
    rapid_test_patterns = [
        {'dopamine': 90, 'serotonin': 80, 'oxytocin': 70, 'cortisol': 5, 'norepinephrine': 30},
        {'dopamine': 10, 'serotonin': 10, 'oxytocin': 5, 'cortisol': 85, 'norepinephrine': 80},
        {'dopamine': 15, 'serotonin': 20, 'oxytocin': 15, 'cortisol': 70, 'norepinephrine': 10},
        {'dopamine': 80, 'serotonin': 60, 'oxytocin': 90, 'cortisol': 10, 'norepinephrine': 20},
        {'dopamine': 25, 'serotonin': 30, 'oxytocin': 20, 'cortisol': 80, 'norepinephrine': 25}
    ]
    
    start_time = time.time()
    successful_requests = 0
    
    for i, pattern in enumerate(rapid_test_patterns):
        try:
            response = requests.post(API_URL, json=pattern, timeout=2)
            if response.status_code == 200:
                result = response.json()
                coords = get_emotion_coordinates(result['emotion'])
                successful_requests += 1
                print(f"   Request {i+1}: {result['emotion']} → ({coords['valence']:.2f}, {coords['arousal']:.2f})")
        except:
            print(f"   Request {i+1}: ❌ Failed")
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\n📊 Performance Results:")
    print(f"   Total requests: {len(rapid_test_patterns)}")
    print(f"   Successful: {successful_requests}")
    print(f"   Total time: {total_time:.3f}s")
    print(f"   Average per request: {total_time/len(rapid_test_patterns):.3f}s")

def test_frontend_integration():
    """Test the frontend integration capabilities"""
    print("🌐 Testing Frontend Integration Features")
    print("=" * 42)
    
    print("✅ Enhanced features to test in browser:")
    print("   • Smooth SVG dot animations (0.8s cubic-bezier transitions)")
    print("   • Quadrant-based color coding (4 different colors)")
    print("   • Interactive emotion buttons for demo mode")
    print("   • Enhanced glassmorphic styling with gradient overlays")
    print("   • Modular JavaScript architecture with ES6 modules")
    print("   • Mobile-responsive design with touch-friendly controls")
    print("   • Real-time slider integration with live API updates")
    print("   • Graceful error handling with center position reset")
    print()
    print("🎯 Test these features in your browser:")
    print("   1. Open docs/index.html")
    print("   2. Move sliders and watch smooth dot transitions")
    print("   3. Click emotion buttons to test demo mode")
    print("   4. Observe color changes based on emotional quadrants")
    print("   5. Test mobile responsiveness on different screen sizes")

if __name__ == '__main__':
    print("🎭 Project Iris - Enhanced Visualization Integration Test")
    print("=" * 65)
    print()
    
    # Test API integration with enhanced visualization
    test_enhanced_visualization_integration()
    print()
    
    # Test performance
    test_visualization_performance()
    print()
    
    # Test frontend features
    test_frontend_integration()
    print()
    
    print("🎯 Integration testing complete!")
    print("💡 Start the API server with: python api.py")
    print("🌐 Open docs/index.html to see the enhanced visualization in action!")
            'data': {'dopamine': 30, 'serotonin': 30, 'oxytocin': 20, 'cortisol': 30, 'norepinephrine': 30}
        }
    ]
    
    for case in test_cases:
        try:
            response = requests.post(API_URL, json=case['data'], timeout=5)
            if response.status_code == 200:
                result = response.json()
                print(f"{case['name']:20} -> {result['emotion']:12} (conf: {result['confidence']:.3f})")
                print(f"{'':20}    {result['description'][:60]}...")
            else:
                print(f"{case['name']:20} -> ERROR: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{case['name']:20} -> CONNECTION ERROR: {e}")
        print()

def test_emotion_coordinates():
    """Display the emotion coordinates for visualization"""
    print("\n🎯 Emotion Visualization Coordinates")
    print("=" * 50)
    
    coords = {
        'happiness': {'valence': 0.9, 'arousal': 0.85},
        'anger': {'valence': 0.2, 'arousal': 0.9},
        'sadness': {'valence': 0.25, 'arousal': 0.3},
        'fear': {'valence': 0.15, 'arousal': 0.8},
        'disgust': {'valence': 0.2, 'arousal': 0.45}
    }
    
    for emotion, coord in coords.items():
        quadrant = get_quadrant(coord['valence'], coord['arousal'])
        print(f"{emotion:12} -> Valence: {coord['valence']:.2f}, Arousal: {coord['arousal']:.2f} ({quadrant})")

def get_quadrant(valence, arousal):
    """Determine which quadrant an emotion falls into"""
    if valence > 0.5 and arousal > 0.5:
        return "Excitement"
    elif valence < 0.5 and arousal > 0.5:
        return "Stress"
    elif valence < 0.5 and arousal < 0.5:
        return "Depression"
    else:
        return "Contentment"

if __name__ == '__main__':
    test_emotion_inference()
    test_emotion_coordinates()
