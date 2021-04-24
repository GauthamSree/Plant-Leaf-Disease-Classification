import './Result.css'

const Result = ({Prediction, Confidence}) =>  {
    return (
    <div>
        <div className="box">
            <h3>Result</h3>
            <div className="field">
                <span>Prediction: <span className='resultText'>{Prediction}</span></span>
                <span>Confidence: <span className='resultText'>{Confidence}</span></span>
            </div>
        </div>
    </div>
    )
}

export default Result;