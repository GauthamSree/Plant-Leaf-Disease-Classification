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

model = LeafModel(num_classes=38)
model.load('models/EfficientNet_model2_onlyModel.pth', device='cpu')

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

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn main:app --reload