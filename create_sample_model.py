import pickle

# Sample data that might represent a trained model for emotion prediction
# In a real application, this would be a trained machine learning model
sample_model = {
    'model_type': 'emotion_predictor',
    'features': ['cycle_day', 'hormone_level', 'previous_emotion'],
    'predictions': {
        'happy': 0.7,
        'sad': 0.2,
        'angry': 0.1
    },
    'accuracy': 0.85
}

# Save the sample model to a .pkl file
with open('predictor/models/emotion_model.pkl', 'wb') as f:
    pickle.dump(sample_model, f)

print("Sample emotion_model.pkl file created successfully!")
 
