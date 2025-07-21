#!/usr/bin/env python3
"""
Comprehensive test suite for the emotion inference engine.
"""

import pytest
import numpy as np
from src.engine import infer_emotion, _df, CHEM_COLS

class TestEmotionInference:
    """Test cases for emotion inference functionality"""
    
    def test_basic_functionality(self):
        """Test that the function returns expected types"""
        sample_input = {
            'dopamine': 20, 'serotonin': 30, 'oxytocin': 15, 
            'cortisol': 10, 'norepinephrine': 25
        }
        emotion, confidence = infer_emotion(sample_input)
        
        assert isinstance(emotion, str)
        assert isinstance(confidence, float)
        assert 0.0 <= confidence <= 1.0
    
    def test_zero_vector_edge_case(self):
        """Test behavior with all-zero input"""
        zero_input = {
            'dopamine': 0, 'serotonin': 0, 'oxytocin': 0, 
            'cortisol': 0, 'norepinephrine': 0
        }
        emotion, confidence = infer_emotion(zero_input)
        
        assert emotion is None
        assert confidence == 0.0
    
    def test_high_confidence_matches(self):
        """Test that exact database matches return high confidence"""
        # Use the first emotion from the database for exact match
        first_emotion = _df.iloc[0]
        exact_input = {chem: first_emotion[chem] for chem in CHEM_COLS}
        
        emotion, confidence = infer_emotion(exact_input)
        
        assert emotion == first_emotion['emotion']
        assert confidence > 0.99  # Should be nearly 1.0 for exact match
    
    def test_all_valid_emotions_in_database(self):
        """Test that inferred emotions are always in the database"""
        test_cases = [
            {'dopamine': 50, 'serotonin': 20, 'oxytocin': 10, 'cortisol': 5, 'norepinephrine': 15},
            {'dopamine': 10, 'serotonin': 80, 'oxytocin': 30, 'cortisol': 40, 'norepinephrine': 20},
            {'dopamine': 30, 'serotonin': 10, 'oxytocin': 60, 'cortisol': 15, 'norepinephrine': 35},
        ]
        
        valid_emotions = set(_df['emotion'].values)
        
        for case in test_cases:
            emotion, confidence = infer_emotion(case)
            assert emotion in valid_emotions or emotion is None
    
    def test_consistency(self):
        """Test that the same input always produces the same output"""
        test_input = {
            'dopamine': 25, 'serotonin': 35, 'oxytocin': 20, 
            'cortisol': 15, 'norepinephrine': 30
        }
        
        # Run multiple times
        results = [infer_emotion(test_input) for _ in range(5)]
        
        # All results should be identical
        first_result = results[0]
        for result in results[1:]:
            assert result == first_result
    
    def test_extreme_values(self):
        """Test behavior with extreme values"""
        extreme_cases = [
            # Very high single neurotransmitter
            {'dopamine': 100, 'serotonin': 0, 'oxytocin': 0, 'cortisol': 0, 'norepinephrine': 0},
            {'dopamine': 0, 'serotonin': 100, 'oxytocin': 0, 'cortisol': 0, 'norepinephrine': 0},
            # All maximum
            {'dopamine': 100, 'serotonin': 100, 'oxytocin': 100, 'cortisol': 100, 'norepinephrine': 100},
        ]
        
        for case in extreme_cases:
            emotion, confidence = infer_emotion(case)
            # Should still return valid results (confidence may vary)
            assert isinstance(confidence, float)
            assert 0.0 <= confidence <= 1.0
    
    def test_known_emotional_patterns(self):
        """Test recognition of known emotional patterns"""
        # Test case that should map to sadness-like emotions (high cortisol, low dopamine)
        sad_pattern = {
            'dopamine': 5, 'serotonin': 15, 'oxytocin': 20, 
            'cortisol': 70, 'norepinephrine': 25
        }
        emotion, confidence = infer_emotion(sad_pattern)
        
        # Should match a negative emotion with reasonable confidence
        emotion_row = _df[_df['emotion'] == emotion].iloc[0]
        assert emotion_row['emotion_category'] in ['Negative']
        assert confidence > 0.5
    
    def test_input_validation_robustness(self):
        """Test that the function handles various input formats"""
        # Test with float values
        float_input = {
            'dopamine': 20.5, 'serotonin': 30.7, 'oxytocin': 15.2, 
            'cortisol': 10.1, 'norepinephrine': 25.9
        }
        emotion, confidence = infer_emotion(float_input)
        assert isinstance(emotion, str)
        assert isinstance(confidence, float)
    
    def test_missing_neurotransmitter_raises_error(self):
        """Test that missing neurotransmitters raise appropriate errors"""
        incomplete_input = {
            'dopamine': 20, 'serotonin': 30, 'oxytocin': 15
            # Missing cortisol and norepinephrine
        }
        
        with pytest.raises(KeyError):
            infer_emotion(incomplete_input)

class TestDatabase:
    """Test cases for the emotion database integrity"""
    
    def test_database_loading(self):
        """Test that the database loads correctly"""
        assert len(_df) > 0
        assert all(col in _df.columns for col in CHEM_COLS)
        assert 'emotion' in _df.columns
        assert 'emotion_category' in _df.columns
    
    def test_no_duplicate_emotions(self):
        """Test that all emotions in the database are unique"""
        emotions = _df['emotion'].values
        assert len(emotions) == len(set(emotions))
    
    def test_valid_neurochemical_ranges(self):
        """Test that all neurochemical values are non-negative"""
        for chem in CHEM_COLS:
            assert all(_df[chem] >= 0), f"Negative values found in {chem}"
    
    def test_emotion_categories_valid(self):
        """Test that emotion categories are from expected set"""
        valid_categories = {'Positive', 'Negative', 'Neutral', 'Mixed'}
        actual_categories = set(_df['emotion_category'].unique())
        assert actual_categories.issubset(valid_categories)

if __name__ == '__main__':
    # Run tests when executed directly
    pytest.main([__file__, '-v'])
