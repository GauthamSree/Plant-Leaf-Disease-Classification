(this.webpackJsonpplantweb=this.webpackJsonpplantweb||[]).push([[0],{35:function(e,t,a){},37:function(e,t,a){},38:function(e,t,a){},45:function(e,t,a){},46:function(e,t,a){},47:function(e,t,a){},48:function(e,t,a){},67:function(e,t,a){"use strict";a.r(t);var c=a(1),n=a.n(c),s=a(27),i=a.n(s),l=(a(35),a(30)),o=a(11),r=a.n(o),d=a(15),j=a(12),h=(a(37),a(10)),p=(a(38),a(0)),b=function(){return Object(p.jsx)("div",{className:"headerContainer",children:Object(p.jsxs)("header",{children:[Object(p.jsx)(h.b,{to:"/",activeClassName:"is_active",exact:!0,children:Object(p.jsx)("h1",{className:"header_title",children:"Plant Disease Classification"})}),Object(p.jsx)("nav",{children:Object(p.jsxs)("ul",{className:"nav_links",children:[Object(p.jsx)("li",{children:Object(p.jsxs)(h.b,{to:"/prediction_classes",activeClassName:"is_active",exact:!0,children:[Object(p.jsx)("i",{className:"fas fa-scroll"})," Prediction Labels"]})}),Object(p.jsx)("li",{children:Object(p.jsxs)("a",{href:"https://github.com/GauthamSree/Plant-Leaf-Disease-Classification",rel:"noreferrer",target:"_blank",children:[Object(p.jsx)("i",{className:"fab fa-github"})," GitHub"]})}),Object(p.jsx)("li",{children:Object(p.jsxs)("a",{href:"http://linkedin.com/in/gautham-sreekumar-5662b318b",rel:"noreferrer",target:"_blank",children:[Object(p.jsx)("i",{className:"fab fa-linkedin"})," LinkedIn"]})})]})})]})})},m=(a(45),function(){return Object(p.jsx)("div",{className:"footwrapper",children:Object(p.jsxs)("footer",{children:[Object(p.jsx)("div",{children:Object(p.jsx)("p",{children:'This website can be used to predict plant disease which uses a image classification model to predict the disease. User can click on "Try Out Sample" to test few random images pulled from backend and predicted on our trained Model. The result shows the prediction class to which the image uploaded belongs to and the confidence of the model prediction.'})}),Object(p.jsx)("div",{className:"byclass",children:"By Gautham Sreekumar"})]})})}),u=(a(46),function(e){var t=e.onPredict,a=e.onFileUpload,n=e.onCancelImage,s=e.onSample,i=Object(c.useRef)();return Object(p.jsx)("div",{children:Object(p.jsx)("div",{className:"wrapper",children:Object(p.jsxs)("div",{className:"formContainer",children:[Object(p.jsx)("div",{className:"imageContainer",children:Object(p.jsxs)("div",{className:"imageHolder",children:[Object(p.jsx)("button",{id:"cancel-btn",onClick:n,children:Object(p.jsx)("i",{className:"fas fa-times"})}),Object(p.jsx)("img",{id:"imageid",src:"",alt:"No file Uploaded"}),Object(p.jsxs)("span",{id:"imagespan",children:[Object(p.jsx)("i",{className:"fas fa-cloud-upload-alt"})," Image Preview"]})]})}),Object(p.jsxs)("div",{className:"buttonContainer",children:[Object(p.jsx)("input",{ref:i,type:"file",onChange:a,accept:"image/*",hidden:"hidden"}),Object(p.jsx)("button",{id:"custom-button",onClick:function(){i.current.click()},children:"Choose an Image"}),Object(p.jsx)("button",{onClick:s,children:"Try Out Sample"}),Object(p.jsx)("button",{onClick:t,children:"Predict"})]})]})})})}),f=(a(47),function(e){var t=e.Prediction,a=e.Confidence;return Object(p.jsx)("div",{children:Object(p.jsxs)("div",{className:"box",children:[Object(p.jsx)("h3",{children:"Result"}),Object(p.jsxs)("div",{className:"field",children:[Object(p.jsxs)("span",{children:["Prediction: ",Object(p.jsx)("span",{className:"resultText",children:t})]}),Object(p.jsxs)("span",{children:["Confidence: ",Object(p.jsx)("span",{className:"resultText",children:a})]})]})]})})}),O=["Apple -- Apple Scab","Apple -- Black Rot","Apple -- Cedar Apple Rust","Apple -- Healthy","Cherry -- Powdery Mildew","Cherry --  Healthy","Corn -- Gray Leaf Spot (Cercospora Leaf Spot)","Corn -- Common Rust","Corn -- Northern Leaf Blight","Corn -- Healthy","Grape -- Black Rot","Grape -- Esca (Black Measles)","Grape -- Leaf Blight (Isariopsis Leaf Spot)","Grape -- Healthy","Peach -- Bacterial_spot","Peach -- Healthy","Pepper Bell -- Bacterial Spot","Pepper Bell -- Healthy","Potato -- Early Blight","Potato -- Late Blight","Potato -- Healthy","Strawberry -- Leaf Scorch","Strawberry -- Healthy","Tomato -- Bacterial Spot","Tomato -- Early Blight","Tomato -- Late Blight","Tomato -- Leaf Mold","Tomato -- Septoria Leaf Spot","Tomato -- Two-spotted Spider Mites","Tomato -- Target Spot","Tomato -- Yellow Leaf Curl Virus","Tomato -- Mosaic Virus","Tomato -- Healthy"],x=(a(48),function(){return Object(p.jsxs)("div",{className:"Predwrapper",children:[Object(p.jsxs)("div",{className:"boxContainer",children:[Object(p.jsx)("h3",{children:"Description"}),Object(p.jsx)("div",{children:Object(p.jsx)("p",{children:"The model developed using EfficientNet B3 deep learning architecture helps to predict plant leaf diseases from leaf images. The accuracy of the model is 99.875%. PyTorch was used to train this model using the mixed precision functionality (torch.cuda.amp.GradScaler). Early Stopping callback was used to avoid overfitting of the model, which monitors performance of the loss value on validation split."})})]}),Object(p.jsxs)("div",{className:"boxContainer",children:[Object(p.jsx)("h3",{children:"Prediction Classes"}),Object(p.jsx)("div",{className:"classContainer",children:O.map((function(e,t){return Object(p.jsx)("div",{id:t,className:"fieldText",children:Object(p.jsxs)("span",{children:[t+1," : ",Object(p.jsx)("span",{className:"resultText",children:e})]})})}))})]})]})}),g=function(){return Object(p.jsx)("div",{children:Object(p.jsxs)("div",{className:"box",children:[Object(p.jsx)("h3",{children:"Result"}),Object(p.jsx)("div",{id:"progress",className:"field",children:"Predicting... Please Wait!"})]})})},y=a(29),v=a.n(y),C=a(2);var T=function(){var e=v.a.create({baseURL:Object({NODE_ENV:"production",PUBLIC_URL:"/Plant-Leaf-Disease-Classification",WDS_SOCKET_HOST:void 0,WDS_SOCKET_PATH:void 0,WDS_SOCKET_PORT:void 0,FAST_REFRESH:!0}).REACT_APP_API_URL||"https://plant-disease-fastapi.herokuapp.com/api"}),t=Object(c.useState)([]),a=Object(j.a)(t,2),n=a[0],s=a[1],i=Object(c.useState)([]),o=Object(j.a)(i,2),O=o[0],y=o[1],T=Object(c.useState)(!1),N=Object(j.a)(T,2),S=N[0],P=N[1],k=!n||n&&0===n.length,w=function(){var t=Object(d.a)(r.a.mark((function t(a){return r.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:P(!0),e.post("/predict/",O,{timeout:18e5}).then((function(e){P(!1),s(e.data),console.log(e.data)}),(function(e){document.getElementById("progress").innerHTML="Response Timeout. Please Try Again",console.log(e)}));case 2:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),B=function(){var t=Object(d.a)(r.a.mark((function t(){var a,c,n;return r.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:a=document.getElementById("imageid"),c=document.getElementById("imagespan"),n=document.getElementById("cancel-btn"),e.get("/sample_image/",{responseType:"blob",headers:{"Cache-Control":"no-store",Pragma:"no-cache"}}).then((function(e){var t=new File([e.data],"image.jpg"),c=new FormData;c.append("file",t),y(c),a.src=URL.createObjectURL(e.data),console.log(e.data)}),(function(e){console.log(e)})),a.alt="Backend not yet started",a.style.display="block",n.style.display="block",c.style.display="none";case 8:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}();return Object(p.jsx)(h.a,{children:Object(p.jsxs)("div",{className:"App",children:[Object(p.jsx)(b,{}),Object(p.jsxs)(C.c,{children:[Object(p.jsxs)(C.a,{exact:!0,path:"/",children:[Object(p.jsx)(u,{onPredict:w,onFileUpload:function(e){var t=new FormData,a=e.target.files[0];t.append("file",a),y(t),console.log(a);try{var c=new FileReader;c.onloadend=function(){var e=document.getElementById("imageid"),t=document.getElementById("imagespan"),a=document.getElementById("cancel-btn");e.src=c.result,e.style.display="block",a.style.display="block",t.style.display="none"},c.readAsDataURL(a)}catch(e){console.log(e)}},onCancelImage:function(){y([]),s([]),P(!1);var e=document.getElementById("imageid"),t=document.getElementById("imagespan"),a=document.getElementById("cancel-btn");e.src="",e.alt="No file Uploaded",e.style.display="none",a.style.display="none",t.style.display="block"},onSample:B}),S&&Object(p.jsx)(g,{}),!k&&Object(p.jsx)(f,Object(l.a)({},n))]}),Object(p.jsx)(C.a,{exact:!0,path:"/prediction_classes",children:Object(p.jsx)(x,{})})]}),Object(p.jsx)(m,{})]})})},N=function(e){e&&e instanceof Function&&a.e(3).then(a.bind(null,68)).then((function(t){var a=t.getCLS,c=t.getFID,n=t.getFCP,s=t.getLCP,i=t.getTTFB;a(e),c(e),n(e),s(e),i(e)}))};i.a.render(Object(p.jsx)(n.a.StrictMode,{children:Object(p.jsx)(T,{})}),document.getElementById("root")),N()}},[[67,1,2]]]);
//# sourceMappingURL=main.96f4c6de.chunk.js.map