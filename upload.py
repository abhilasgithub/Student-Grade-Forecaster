from fastapi import FastAPI, HTTPException
import joblib
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()


try:
    model = joblib.load(r"C:\Users\abhil\filename.pkl")
    logger.info("Model loaded successfully from C:\\Users\\abhil\\filename.pkl")
except FileNotFoundError:
    logger.error("Model file not found at C:\\Users\\abhil\\filename.pkl")
    model = None
except Exception as e:
    logger.error(f"Failed to load model: {str(e)}")
    model = None

@app.post("/predict")
def predict(
    telugu: float,
    hindi: float,
    english: float,
    maths: float,
    science: float,
    social: float
):
    logger.info(
        f"Received prediction request - Telugu: {telugu}, Hindi: {hindi}, "
        f"English: {english}, Maths: {maths}, Science: {science}, Social: {social}"
    )

    if model is None:
        logger.error("Model is not loaded. Cannot make predictions.")
        raise HTTPException(status_code=500, detail="Model is not available")

    try:
        features = [[
            telugu,
            hindi,
            english,
            maths,
            science,
            social
        ]]

        if model is None:
            raise HTTPException(status_code=500, detail="Model is not available")

        prediction = model.predict(features)[0]
        result = {
            "Telugu": telugu,
            "Hindi": hindi,
            "English": english,
            "Maths": maths,
            "Science": science,
            "Social": social,
            "predicted_percentage": round(float(prediction), 2)
        }


        logger.info(f"Prediction successful: {result['predicted_percentage']}")
        return result

    except ValueError as Value_error:
        logger.error(f"Invalid input values: {str(Value_error)}")
        raise HTTPException(status_code=400, detail=f"Invalid input values: {str(e)}")
    except Exception as exception_error:
        logger.error(f"Prediction failed: {str(exception_error)}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")