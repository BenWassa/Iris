# Project Iris

**A poetic, science-informed tool to *see* your neurochemistry.**

Transform your inner neurochemical "cocktail" int## 🚧 Roadmap

1️⃣ ~~**Wireframe** basic sliders, dot, and anchors~~ ✅ **Complete**  
2️⃣ **Connect Backend** — API integration for live emotion inference  
3️⃣ **Add Visualization** — 2D emotion space canvas with D3.js  
4️⃣ **Enhance Interactivity** — heatmap trails and emotion anchors  
5️⃣ **Add Playback** — session scrubber to replay emotional journeys  
6️⃣ **Write Footnotes** — disclaimers & sources to explain "illustrative" natureing emotional map through an interactive visualization that maps 5 key neurotransmitters to 91+ unique emotions.

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
- **91 unique emotions** across 4 categories: Positive (39), Negative (43), Neutral (4), Mixed (5)
- **5 neurochemicals** per emotion with values 0-100
- **Rich metadata**: primary/secondary synonyms, descriptive text, emotion categories
- **Biologically-informed mappings**: High cortisol → stress emotions, high oxytocin → bonding emotions

### **Core Algorithm**
- **Cosine similarity matching** between input vector and emotion database
- **Confidence scoring** based on vector similarity (0.0-1.0)
- **Robust handling** of edge cases (zero vectors, extreme values)

---

## 🧪 Testing Status

**✅ All 18 tests passing** - Comprehensive test suite covering:

- **Functional tests**: Basic emotion inference, confidence scoring
- **Edge cases**: Zero vectors, extreme values, missing inputs  
- **Pattern validation**: High cortisol → fear, high oxytocin → love
- **Database integrity**: No duplicates, valid ranges, proper categories
- **API endpoints**: Flask backend response validation
- **Robustness**: Input validation, consistency checks

### **🔄 Current Status**
✅ **Core Engine** — Emotion inference with 91-emotion database  
✅ **Testing Suite** — Comprehensive pytest coverage (18 tests passing)  
✅ **Data Validation** — Neurochemical profile validation scripts  
✅ **Flask API Backend** — RESTful endpoint for emotion inference with CORS support  
✅ **Frontend Prototype** — Interactive HTML demo with live sliders and emotion display  
✅ **Documentation** — Code documentation and usage examples

### **📋 Next Steps**
1️⃣ **API Integration** — Connect HTML frontend to Python backend  
2️⃣ **Enhanced Visualization** — Add emotion space canvas and heatmap trails  
3️⃣ **Session Playback** — Temporal emotion tracking and replay functionality  
4️⃣ **Responsive Design** — Mobile-optimized interface and accessibility features

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

| Dimension | What it means | How it’s shown |
|-----------|----------------|----------------|
| Valence   | Pleasant ↔ Unpleasant | Hue (red ↔ grey ↔ teal) |
| Arousal   | Calm ↔ Excited | Saturation (pale ↔ vivid) |
| Dominance | Power/Control | Lightness (dark = low control, bright = high control) |

Heatmaps show where your states cluster over time.  
Plutchik-style “emotion anchors” let you snap to common states (joy, anger, trust, etc.).

---

## 🧩 Key Features

✅ **Live Sliders** — adjust neurochemical “levels”  
✅ **Real-time Dot** — see your emotional point drift  
✅ **Category Anchors** — click to jump to a classic emotion  
✅ **Session Replay** — comet tail playback of your day  
✅ **Heatmap History** — see patterns form over days/weeks  
✅ **Accessible Colours** — built-in colour-blind toggle  
✅ **Privacy-first** — local-only by default; cloud optional with consent

---

## ⚙️ Tech Stack

### **Current Implementation (Backend)**
- 🐍 **Python 3.13** with pandas & numpy for data processing
- 🧠 **Cosine Similarity Engine** for neurochemical-to-emotion mapping
- 📊 **91-Emotion Database** with 5-dimensional neurochemical profiles
- 🧪 **pytest** for testing infrastructure
- 🌐 **Flask API** with CORS support for cross-origin requests

### **Frontend Prototype (HTML/CSS/JS)**
- 🎛️ **Interactive Sliders** for 5 neurochemicals with real-time updates
- 🎨 **Gradient UI** with glassmorphism design and smooth animations
- 📱 **Responsive Design** optimized for desktop and mobile devices
- ⚡ **Client-side Processing** with JavaScript cosine similarity implementation

### **Planned Enhancements**
- 📊 **D3.js Canvas** for 2-D emotion space visualization
- 🔥 **Heatmap Trails** showing emotion history over time
- ⏱️ **WebWorkers** for smooth rendering performance
- 🔒 **LocalStorage** for private session saves

---

## 🚧 Roadmap

1️⃣ **Wireframe** basic sliders, dot, and anchors  
2️⃣ **Prototype** heatmap with dummy data (CSV)  
3️⃣ **Tune Mapping** — validate slider → emotion labels with test users  
4️⃣ **Add Playback** — basic scrubber to replay a session  
5️⃣ **Write Footnotes** — disclaimers & sources to explain “illustrative” nature

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
- [See full refs](#) (TODO: add links in `/docs/`)

---

## 🪶 Name Origin

> *Iris*: Greek goddess of the rainbow — a bridge from invisible signals to visible colour.  
> *Iris*: The eye’s aperture — a metaphor for “seeing” the hidden self.


