import pickle
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'visa_best_model.pkl')
with open(MODEL_PATH, 'rb') as f:
    model_data = pickle.load(f)

model = model_data['best_model']
scaler = model_data['scaler']
label_encoders = model_data['label_encoders']
feature_columns = model_data['feature_columns']

MODEL_VERSION = '1.0.0'

class_labels = label_encoders['visa_status'].classes_.tolist()

def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])

    # Encode categorical columns
    for col in ['Degree', 'crimerecord', 'city', 'Nationality']:
        df[f'{col}_encoded'] = label_encoders[col].transform(df[col])
        df.drop(columns=[col], inplace=True)

    # Reorder columns to match training
    df = df[feature_columns]

    # Scale features
    df_scaled = scaler.transform(df)

    predicted_encoded = model.predict(df_scaled)[0]
    probabilities = model.predict_proba(df_scaled)[0]
    confidence = max(probabilities)

    predicted_class = label_encoders['visa_status'].inverse_transform([predicted_encoded])[0]
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }

if __name__ == "__main__":

    #Testing data
    sample_input = {
        "age": 26,
        "height": 5.9,
        "Degree": "Graduate",
        "workexperience": 2,
        "income_lpa": 10,
        "crimerecord": "no",
        "city": "Hyderabad",
        "Nationality": "INDIAN"
    }
    result = predict_output(sample_input)
    print(result)
