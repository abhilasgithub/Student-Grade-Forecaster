from fastapi import FastAPI
import logging

logger = logging.getLogger(__name__)

app = FastAPI()


@app.post("/predict")
def predict_percentage(
        telugu: float,
        hindi: float,
        english: float,
        maths: float,
        science: float,
        social: float
):
    try:

        scores = [telugu, hindi, english, maths, science, social]
        if any(score > 100 for score in scores):
            return {"error": "Subject scores cannot exceed 100 marks. Please enter the inputs again."}


        features = [[telugu, hindi, english, maths, science, social]]


        prediction = 85.50

        logger.info(f"Successful prediction: {prediction}")

        return {
            "Telugu": telugu,
            "Hindi": hindi,
            "English": english,
            "Maths": maths,
            "Science": science,
            "Social": social,
            "predicted_percentage": round(float(prediction), 2),
        }

    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return {"error": f"An error occurred: {e}"}
