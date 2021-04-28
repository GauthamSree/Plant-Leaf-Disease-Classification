from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import random

from PlantDisease import *

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = LeafModel(num_classes=33)
model.load('models/Custom-EfficientNet_Model.pth', device='cpu')

@app.get("/")
def home():
    return {"message": "Serving Machine Learning Models"}

@app.get("/api")
def index():
    return {'message': 'Hello World!'}


@app.post("/api/predict/")
async def predict_api(file: UploadFile = File(...)):
    image =  process_image(await file.read())
    y_pred, classIdx = model.predict_one_image(image, 'cpu')
    y_soft = softmax_output(y_pred)
    predicted_class = classes[int(classIdx)]
    percentage = float(np.max(y_soft, axis=1) * 100)
    confidence = "{:.2f}%".format(percentage)
    return {'Prediction': predicted_class, "Confidence" : str(confidence)}

@app.get("/api/sample_image/")
def predict_api():
    testImg = random.choice(sample_images)
    return FileResponse("test_images/" + testImg)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)