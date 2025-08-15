from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def prepare_input_data(data):
    """Transform input data to match model expectations"""
    # Create DataFrame with base numeric columns
    df = pd.DataFrame([{
        'amount': data['amount'],
        'oldbalanceOrg': data['oldbalanceOrg'],
        'newbalanceOrig': data['newbalanceOrig'],
        'oldbalanceDest': data['oldbalanceDest'],
        'newbalanceDest': data['newbalanceDest']
    }])
    
    # Add one-hot encoded transaction type columns
    transaction_types = ['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']
    for type_name in transaction_types:
        df[f'type_{type_name}'] = 1 if data['type'] == type_name else 0
    
    # Add time-based features
    current_time = datetime.now()
    df['hour_of_day'] = current_time.hour
    df['day_of_week'] = current_time.weekday()
    
    # Ensure correct column order
    expected_columns = [
        'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 
        'newbalanceDest', 'type_CASH_IN', 'type_CASH_OUT', 'type_DEBIT',
        'type_PAYMENT', 'type_TRANSFER', 'hour_of_day', 'day_of_week'
    ]
    
    return df[expected_columns]

def load_models():
    """Load ML models with error handling"""
    models = {}
    models_path = 'ml_engineering/model_training/pylance/'
    
    if not os.path.exists(models_path):
        logger.error(f"Models directory not found: {models_path}")
        return models
        
    for model_file in os.listdir(models_path):
        if model_file.endswith('.pkl'):
            try:
                model_name = model_file.replace('FraudIQ_Pipeline_', '').replace('.pkl', '')
                model_path = os.path.join(models_path, model_file)
                logger.info(f"Loading model: {model_file}")
                models[model_name] = joblib.load(model_path)
                logger.info(f"Successfully loaded: {model_file}")
            except Exception as e:
                logger.error(f"Error loading {model_file}: {str(e)}")
                continue
    
    return models

# Load models when starting the application
logger.info("Initializing model loading...")
models = load_models()
logger.info(f"Loaded {len(models)} models successfully")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = {
            'amount': float(request.form['amount']),
            'oldbalanceOrg': float(request.form['oldbalanceOrg']),
            'newbalanceOrig': float(request.form['newbalanceOrig']),
            'oldbalanceDest': float(request.form['oldbalanceDest']),
            'newbalanceDest': float(request.form['newbalanceDest']),
            'type': request.form['type']
        }
        
        # Prepare input data
        df = prepare_input_data(data)
        
        # Check if models are available
        if not models:
            return jsonify({
                'error': 'No models available',
                'status': 'error'
            })
        
        # Select and validate model
        selected_model = request.form['model']
        if selected_model not in models:
            return jsonify({
                'error': f'Model {selected_model} not found',
                'status': 'error'
            })
            
        model = models[selected_model]
        
        # Make prediction
        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]
        
        return jsonify({
            'prediction': int(prediction),
            'probability': float(probability),
            'status': 'success'
        })
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        })

if __name__ == '__main__':
    app.run(debug=True)