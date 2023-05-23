import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import App from './App';
// import Paragraph from './Paragraph'
import ChatModule from './Chatmodule'
import reportWebVitals from './reportWebVitals';
import App from './App';

// import { w3cwebsocket as WebSocket } from 'websocket';
// const ws = new WebSocket('ws://localhost:8000/');


const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <div>
    <App />
    {/* <Paragraph /> */}
    <ChatModule />
    </div>
  </React.StrictMode>
); 

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();


// export { WebSocket, ws };
