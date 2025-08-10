from django.shortcuts import render
from django.http import JsonResponse
import pickle
import os

# Create your views here.
def load_emotion_model():
    """
    Load the emotion prediction model from the .pkl file
    """
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'DecisonTreeModel.pickle')
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        return None

def predictor_form(request):
    """
    View to display the emotion prediction input form
    """
    return render(request, 'predictor_form.html')

def predict_emotion(request):
    """
    View to predict emotion based on menstrual cycle data
    """
    if request.method == 'GET':
        # Get parameters from request
        cycle_day = int(request.GET.get('cycle_day', 14))
        hormone_level = int(request.GET.get('hormone_level', 50))
        previous_emotion = request.GET.get('previous_emotion', 'happy')
        
        # Load the model
        model = load_emotion_model()
        
        if model is None:
            return JsonResponse({'error': 'Model not found'}, status=500)
        
        # In a real application, you would use the model to make predictions
        # For this example, we'll just return the sample data from the model
        prediction = model.get('predictions', {})
        
        # Render the results template with the prediction data
        context = {
            'cycle_day': cycle_day,
            'hormone_level': hormone_level,
            'previous_emotion': previous_emotion,
            'predicted_emotion': prediction,
            'model_info': {
                'model_type': model.get('model_type'),
                'accuracy': model.get('accuracy')
            }
        }
        return render(request, 'predictor_results.html', context)
    
    return JsonResponse({'error': 'Only GET requests are supported'}, status=400)
