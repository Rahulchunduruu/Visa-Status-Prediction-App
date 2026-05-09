from fastapi import FastAPI,Path,HTTPException
from model.predict import predict_output
from schema.userinput import Item

app = FastAPI(
    title="Loan Default Prediction API",
    description="A Simple FastAPI for Loan Default Prediction",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {"message": "Namaste, LORD!"}

@app.post('/predict')
def prediction(data:Item):
    result = predict_output(data.model_dump())
    #print(result)
    return {"message": result}
    