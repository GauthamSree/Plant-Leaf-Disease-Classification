import * as Constants from './Constants'
import './PredClasses.css'

const PredClasses = () =>  {
    return(
    <div className="Predwrapper">
        <div className="boxContainer">
            <h3>Description</h3>
            <div> 
                <p>
                    The model developed using EfficientNet B3 deep learning architecture helps 
                    to predict plant leaf diseases from leaf images. The accuracy of the model is 99.875%.
                    PyTorch was used to train this model using the mixed precision functionality (torch.cuda.amp.GradScaler).  
                    Early Stopping callback was used to avoid overfitting of the model, 
                    which monitors performance of the loss value on validation split.
                </p>
            </div>
        </div>
        <div className="boxContainer">
            <h3>Prediction Classes</h3>
            <div className="classContainer"> 
                {
                    Constants.classes.map((classname, idx) => 
                    <div id={idx} className="fieldText"><span>{idx + 1} : <span className='resultText'>{classname}</span></span></div>)
                }
            </div>
        </div>
    </div>
    )
}

export default PredClasses;