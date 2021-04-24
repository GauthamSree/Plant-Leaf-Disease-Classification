import './Footer.css'

const Footer = () => {
    return( 
    <div className='footwrapper'>
        <footer>
            <div> 
                <p>
                    This website can be used to predict plant disease which uses a image classification 
                    model to predict the disease. User can click on "Try Out Sample" to test few random 
                    images pulled from backend and predicted on our trained Model. The result shows the 
                    prediction class to which the image uploaded belongs to and the confidence of the model prediction.
                </p>
            </div>
            <div className='byclass'>By Gautham Sreekumar</div>
        </footer>
    </div>
    )
}

export default Footer;