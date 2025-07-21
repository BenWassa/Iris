# Project Iris


**A poetic, science-informed tool to *see* your neurochemistry.**

Transform your inner neurochemical "cocktail" into a living emotional map through an interactive, real-time visualization that maps 5 key neurotransmitters to core emotions in a 2D Valence–Arousal space.

---

## 🚀 Major 2025 Upgrade: Enhanced Emotion Dot Visualization

- **Smooth SVG-based dot animation** with cubic-bezier transitions (0.8s)
- **Valence–Arousal grid** with quadrant color coding and glassmorphic styling
- **Real-time API integration**: slider input → backend inference → instant visual feedback
- **Modular JavaScript**: `emotionCoords.js` (emotion mapping), `updateEmotionDot.js` (visual logic)
- **Quadrant-based color system**: Excitement (cyan), Stress (red), Depression (blue), Contentment (teal)
- **Mobile-responsive** and accessible UI
- **Demo/test controls** for rapid prototyping and user education

---

---

## 🔬 Current Implementation

### **Emotion Inference Engine**

```python
from engine import infer_emotion

# Input: neurochemical levels (0-100 scale)
result = infer_emotion({
    'dopamine': 20,      # Reward/motivation
    'serotonin': 30,     # Well-being/mood regulation  
    'oxytocin': 15,      # Bonding/trust
    'cortisol': 10,      # Stress response
    'norepinephrine': 25 # Alertness/arousal
})

# Output: (emotion_label, confidence_score)
# Example: ('serenity', 0.87)
```

### **Database Schema**
- **5 core emotions** covering fundamental emotional states: Happiness, Anger, Sadness, Fear, Disgust
- **5 neurochemicals** per emotion with values 0-100
- **Rich metadata**: descriptive text and emotion categories (Positive/Negative)
- **Biologically-informed mappings**: High cortisol → stress emotions, high oxytocin → bonding emotions

### **Core Algorithm**
- **Cosine similarity matching** between input vector and emotion database
- **Confidence scoring** based on vector similarity (0.0-1.0)
- **Robust handling** of edge cases (zero vectors, extreme values)

---

## 🧪 Testing Status

**✅ All 19 tests passing** - Comprehensive test suite covering:

- **Functional tests**: Basic emotion inference, confidence scoring
- **Edge cases**: Zero vectors, extreme values, missing inputs  
- **Pattern validation**: High cortisol → fear, high oxytocin → love
- **Database integrity**: No duplicates, valid ranges, proper categories
- **API endpoints**: Flask backend response validation (including zero vector handling)
- **Robustness**: Input validation, consistency checks

### **🔄 Current Status**
✅ **Core Engine** — Emotion inference with 5-emotion core database  
✅ **Testing Suite** — Comprehensive pytest coverage (19 tests passing)  
✅ **Data Validation** — Neurochemical profile validation scripts  
✅ **Flask API Backend** — RESTful endpoint for emotion inference with CORS support  
✅ **Frontend Prototype** — Interactive HTML demo with live sliders and emotion display  
✅ **API Integration** — Frontend connects to backend for real-time emotion inference  
✅ **Documentation** — Code documentation and usage examples

### **📋 Next Steps**
1️⃣ **Enhanced Visualization** — Add emotion space canvas and heatmap trails  
2️⃣ **Session Playback** — Temporal emotion tracking and replay functionality  
3️⃣ **Responsive Design** — Mobile-optimized interface and accessibility features
4️⃣ **Expanded Database** — Consider adding more emotions beyond core 5

---

## 📌 What is Iris?

**Project Iris** transforms your inner neurochemical “cocktail” into a *living emotional map*.  
Adjust sliders for **dopamine**, **oxytocin**, **serotonin**, and **cortisol** — watch your emotional dot drift across a **Valence–Arousal–Dominance** canvas, with colours and motion that mirror your state.

No clinical promises — just a creative mirror for reflection and self-awareness.

---

## 🧬 Core Idea

> 🧭 *Neurochemistry in → Emotion out → Visual feedback → Reflection.*

**Why?**  
- Neurochemicals modulate felt states.
- Felt states cluster in a 2–3D emotion space.
- Spatial mapping + colour + motion = intuitive understanding.

---


## 🎨 Visual System

| Dimension | What it means         | How it’s shown                |
|-----------|----------------------|-------------------------------|
| Valence   | Pleasant ↔ Unpleasant| X-axis, color hue, left↔right |
| Arousal   | Calm ↔ Excited       | Y-axis, color intensity, up↔down |
| Quadrant  | Emotional cluster     | Dot color: cyan/red/blue/teal |

**Dot color by quadrant:**
- Excitement: **Cyan** (#00FFE0)
- Stress: **Red** (#FF6B6B)
- Depression: **Blue** (#6B73FF)
- Contentment: **Teal** (#4ECDC4)

**Glassmorphic** SVG canvas with grid, axis labels, and quadrant markers. Dot animates smoothly between positions. Responsive and touch-friendly.

---


## 🧩 Key Features

✅ **Live Sliders** — adjust neurochemical “levels”
✅ **Real-time Dot** — see your emotional point drift in a 2D Valence–Arousal space
✅ **Quadrant Color Coding** — dot color reflects emotional quadrant
✅ **Glassmorphic UI** — modern, gradient, and blurred backgrounds
✅ **Modular JS** — easy to extend and maintain
✅ **API Integration** — instant feedback from backend inference
✅ **Demo/Test Controls** — try any emotion instantly
✅ **Accessible & Responsive** — works on all devices
✅ **Privacy-first** — local-only by default; cloud optional with consent

---

## ⚙️ Tech Stack

### **Current Implementation (Backend)**
- 🐍 **Python 3.13** with pandas & numpy for data processing
- 🧠 **Cosine Similarity Engine** for neurochemical-to-emotion mapping
- 📊 **5-Emotion Core Database** with 5-dimensional neurochemical profiles
- 🧪 **pytest** for testing infrastructure
- 🌐 **Flask API** with CORS support for cross-origin requests


### **Frontend (HTML/CSS/JS)**
- 🎛️ **Interactive Sliders** for 5 neurochemicals with real-time updates
- 📊 **SVG Emotion Dot Visualization** with quadrant color coding
- 🎨 **Modular Design**: `emotionCoords.js`, `updateEmotionDot.js`
- 🎭 **Glassmorphism UI** with gradients and blur
- 📱 **Responsive Design** for desktop and mobile
- ⚡ **Live Backend Integration** with Flask API


### **Planned Enhancements**
- 🔥 **Heatmap Trails** showing emotion history over time
- ⏱️ **WebWorkers** for smooth rendering performance
- 🔒 **LocalStorage** for private session saves

---


## 🚧 Roadmap

1️⃣ **Wireframe** basic sliders, dot, and anchors  
2️⃣ **API Integration** — live emotion inference  
3️⃣ **Enhanced Visualization** — SVG dot, quadrant color, glassmorphism  
4️⃣ **Heatmap/Playback** — session replay and trails  
5️⃣ **Accessibility & Mobile** — full responsive support  
6️⃣ **Expanded Database** — more emotions, richer mapping

---

## ⚠️ Ethics & Boundaries

Iris is *not* a diagnostic tool.  
It’s an *interactive art–science mirror* for personal insight.  
No data leaves your device without clear consent.

---


## 📚 References

- Russell’s Circumplex Model  
- PAD / VAD Emotion Space  
- Plutchik’s Wheel of Emotions  
- Geneva Emotion Wheel  
- [See full refs](#) (see `/docs/`)

---

## 🪶 Name Origin

> *Iris*: Greek goddess of the rainbow — a bridge from invisible signals to visible colour.  
> *Iris*: The eye’s aperture — a metaphor for “seeing” the hidden self.


