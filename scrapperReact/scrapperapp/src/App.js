import React from 'react';
import './App.css';

// import  { useState, useEffect } from 'react';
// import axios from 'axios';


function App() {
  // const [message, setMessage] = useState('');


  // useEffect(() => {
  //   const interval = setInterval(() => {
  //     axios.get('/api/messages').then(response => {
  //       setMessage(response.data.message);
  //     });
  //   }, 1000);

  //   return () => clearInterval(interval);
  // }, []);

  return (
    <div>
      <div className='upper_message' >
        <h1 style={{ color: '#8bc8f7' }}> All loot deals: (AI Powered) </h1>
        <u><p style={{ color: 'yellow' }}> ▷ NOTE: </p> </u>
        <p style={{ color: 'white' }}>These messages represent the most recent deals extracted from various Telegram channels that offer the best deals. All duplicate deals have been effectively removed. The chat container on the right side applies an AI algorithm to filter and display only the most relevant messages. Although the model is currently in the training phase, it is already producing good 👍 results. Enjoy!</p>
      </div>
    </div>
  );
}

export default App;
