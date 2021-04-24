import './FileUpload.css'
import React, { useRef } from 'react'

const FileUpload = ( { onPredict, onFileUpload, onCancelImage, onSample } ) =>  {
    const inputRef = useRef()
    return( 
    <div>
        <div className="wrapper">
            <div className="formContainer">
                <div className="imageContainer">
                    <div className="imageHolder">
                        <button id="cancel-btn" onClick={onCancelImage}><i className="fas fa-times"></i></button>
                        <img id="imageid" src="" alt="No file Uploaded"></img>
                        <span id="imagespan"><i className="fas fa-cloud-upload-alt"></i> Image Preview</span>
                    </div>
                </div>
                <div className="buttonContainer">
                    <input ref={inputRef} type="file" onChange={onFileUpload} accept="image/*" hidden="hidden"></input>
                    <button id="custom-button" onClick= {() => {
                        inputRef.current.click()
                    }}>Choose an Image</button>
                    <button onClick={onSample}>Try Out Sample</button>
                    <button onClick={onPredict}>Predict</button>
                </div>
            </div>
        </div>
    </div>
    )
}

export default FileUpload;


