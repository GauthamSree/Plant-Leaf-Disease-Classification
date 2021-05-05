import './App.css';
import React, { useState, useEffect } from 'react'
import Header from './Components/Header'
import Footer from './Components/Footer'
import FileUpload from './Components/FileUpload'
import Result from './Components/Result'
import PredClasses from './Components/PredClasses'
import Progress from './Components/Progress'
import axios from "axios";
import { HashRouter as Router, Switch, Route } from 'react-router-dom';


function App() {
  
  const instance = axios.create({
     baseURL: process.env.REACT_APP_API_URL || "https://plant-disease-fastapi.herokuapp.com/api"
  })
  
  const [prediction, setPrediction] = useState([])
  const [formData, setFileUploaded] = useState([])
  const [isPredicting, setIsPredicting] = useState(false)
  const noPrediction = !prediction || (prediction && prediction.length === 0)
  
  const onFileUpload = (e) => {
    let form = new FormData()
    let fileSelected = e.target.files[0] 
    form.append('file', fileSelected)
    setFileUploaded(form)
    console.log(fileSelected)
    try {
      let reader = new FileReader()
      reader.onloadend = () => {
        const imgBox = document.getElementById('imageid')
        const text = document.getElementById('imagespan')
        const cancelBtn = document.getElementById('cancel-btn')
        imgBox.src = reader.result;
        imgBox.style.display = "block";
        cancelBtn.style.display = "block";
        text.style.display = "none";
      }
      reader.readAsDataURL(fileSelected)
    } catch(e) {
      console.log(e)
    }
  }
  
  const onPredict = async (e) => {
    setIsPredicting(true)
    instance.post('/predict/', formData, {timeout: 60 * 30 * 1000})
    .then((response) => {
      setIsPredicting(false)
      setPrediction(response.data)
      console.log(response.data)
    }, (error) => {
      document.getElementById("progress").innerHTML = "Response Timeout. Please Try Again";
      console.log(error)
    });
  }

  const onCancelImage = () => {
    setFileUploaded([])
    setPrediction([])
    setIsPredicting(false)
    const imgBox = document.getElementById('imageid')
    const text = document.getElementById('imagespan')
    const cancelBtn = document.getElementById('cancel-btn')
    imgBox.src = '';
    imgBox.alt = "No file Uploaded";
    imgBox.style.display = "none";
    cancelBtn.style.display = "none";
    text.style.display = "block";
  }

  const onSample = async () => {
    const imgBox = document.getElementById('imageid')
    const text = document.getElementById('imagespan')
    const cancelBtn = document.getElementById('cancel-btn')
    instance.get('/sample_image/', { 
      responseType: 'blob',
      headers: {
        'Cache-Control': 'no-store',
        'Pragma': 'no-cache',
      }
    }).then((response) => {
      const file = new File([response.data], "image.jpg")
      let form = new FormData()
      form.append('file', file)
      setFileUploaded(form)
      imgBox.src = URL.createObjectURL(response.data);
      console.log(response.data)
    }, (error) => {
      console.log(error)
    });
    imgBox.alt = "Backend not yet started";    
    imgBox.style.display = "block";
    cancelBtn.style.display = "block";
    text.style.display = "none";
  }

  useEffect(() => {
    instance.get('/').then((response) => {
      console.log(response.data)
    }, (error) => {
      console.log(error)
    });
  });

  return (
    <Router>
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/">
            <FileUpload onPredict={onPredict} onFileUpload={onFileUpload} onCancelImage={onCancelImage} onSample={onSample} />
            {isPredicting && <Progress />}
            {!noPrediction && <Result {...prediction}/>}
          </Route>
          <Route exact path="/prediction_classes">
            <PredClasses />
          </Route>
        </Switch>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
