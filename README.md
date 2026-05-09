# 🛂 Visa Status Prediction App

A Machine Learning web app that predicts visa approval status based on applicant details.
Built with **FastAPI** (backend) and **Streamlit** (frontend).

## Project Structure

```
Fastapi_ML/
├── model/
│   ├── predict.py          # ML prediction logic
│   └── visa_best_model.pkl # Trained model
├── schema/
│   └── userinput.py        # Pydantic input schema
├── app.py                  # Streamlit frontend
├── main.py                 # FastAPI backend
├── requirements.txt
└── .env
```

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv myenv
myenv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Run the App

Just run Streamlit — FastAPI starts automatically in the background:
```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

## API

The FastAPI server runs at `http://127.0.0.1:8000`

- Docs: `http://127.0.0.1:8000/docs`
- Endpoint: `POST /predict`

### Sample Request
```json
{
  "age": 26,
  "height": 5.9,
  "Degree": "Graduate",
  "workexperience": 2,
  "income_lpa": 10,
  "crimerecord": "no",
  "city": "Hyderabad",
  "Nationality": "INDIAN"
}
```

### Sample Response
```json
{
  "message": {
    "predicted_category": "Certified",
    "confidence": 0.91,
    "class_probabilities": {
      "Certified": 0.91,
      "Denied": 0.09
    }
  }
}
```
