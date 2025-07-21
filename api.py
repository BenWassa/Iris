from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the emotion profile dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'emotion_chem_profiles.csv')
emotion_df = pd.read_csv(DATA_PATH)

# Define the neurotransmitter columns
chemical_cols = ['dopamine', 'serotonin', 'oxytocin', 'cortisol', 'norepinephrine']
emotion_vectors = emotion_df[chemical_cols].values

# Normalize vectors for cosine similarity
normed_vectors = emotion_vectors / np.linalg.norm(emotion_vectors, axis=1, keepdims=True)

# Create Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/infer', methods=['POST'])
def infer_emotion():
    data = request.json
    try:
        # Create and normalize input vector
        input_vector = np.array([
            data['dopamine'],
            data['serotonin'],
            data['oxytocin'],
            data['cortisol'],
            data['norepinephrine']
        ], dtype=float).reshape(1, -1)
        input_norm = input_vector / np.linalg.norm(input_vector)

        # Calculate cosine similarity
        similarities = cosine_similarity(input_norm, normed_vectors).flatten()

        # Find best match
        best_idx = int(np.argmax(similarities))
        best_emotion = emotion_df.iloc[best_idx]['emotion']
        confidence = round(float(similarities[best_idx]), 4)
        description = emotion_df.iloc[best_idx]['description']

        return jsonify({
            'emotion': best_emotion,
            'confidence': confidence,
            'description': description
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
