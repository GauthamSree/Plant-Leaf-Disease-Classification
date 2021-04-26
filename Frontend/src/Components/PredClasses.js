import * as Constants from './Constants'
import './PredClasses.css'

const PredClasses = () =>  {
    return(
    <div className="Predwrapper">
        <div className="boxContainer">
            <h3>Materials And Methods</h3>
            <div> 
                <p>
                    We have used EfficientNet-b3 as our base model. To train this model, 
                    we used Pytorch, images from kaggle. We have used EarlyStopping callback 
                    to stop training when the validation loss is getting worse 
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