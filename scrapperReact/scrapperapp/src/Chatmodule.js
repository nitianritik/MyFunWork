import React, { useState, useEffect, useRef } from 'react';
import { w3cwebsocket as WebSocket } from 'websocket';
import './Chatmodule.css';

const ws1 = new WebSocket('ws://localhost:8000/');
// const ws1 = new WebSocket('ws://localhost:8000/');
// const ws2 = new WebSocket('ws://localhost:8001/');

function Chatmodule() {
  const [messages, setMessages] = useState([]);
  const [messages2, setMessages2] = useState([]);
  const [newMessage, setNewMessage] = useState(false);
  const [newMessage2, setNewMessage2] = useState(false);
  const chatEndRef = useRef(null);
  const chatEndRef2 = useRef(null);
  const chatContainerRef = useRef(null);
  const chatContainerRef2 = useRef(null);
  const [shouldAutoScroll, setShouldAutoScroll] = useState(true);
  const [shouldAutoScroll2, setShouldAutoScroll2] = useState(true);

  useEffect(() => {
    ws1.onmessage = (event) => {

      const data = JSON.parse(event.data);
      setMessages((prevMessages) => {
        const newMessages = [...prevMessages, data];
        if (newMessages.length > 199) {
          newMessages.splice(0, newMessages.length - 199);
        }
        setNewMessage(true);
        setTimeout(() => setNewMessage(false), 5000); // Hide new message indicator after 5 seconds
        return newMessages;
      });

      if (data.important) {
        setMessages2((prevMessages2) => {
          // keep only the last 199 important messages and add the new one
          const newMessages2 = [...prevMessages2, data].slice(-199);
          setNewMessage2(true);
          setTimeout(() => setNewMessage2(false), 5000); // Hide new message indicator after 5 seconds
          return newMessages2;
        });
      }
    };
  }, []);

  useEffect(() => {
    if (shouldAutoScroll && chatContainerRef.current && chatContainerRef2.current) {
      chatContainerRef.current.scrollTo({ behavior: 'smooth', top: chatContainerRef.current.scrollHeight });
      chatContainerRef2.current.scrollTo({ behavior: 'smooth', top: chatContainerRef2.current.scrollHeight });
    } else if (chatContainerRef.current) {
      const messagesContainer = chatContainerRef.current;
      const lastMessageElement = messagesContainer.querySelector('.message-container:first-child');
      if (lastMessageElement) {
        const lastMessageHeight = lastMessageElement.getBoundingClientRect().height;
        messagesContainer.scrollTo({ top: messagesContainer.scrollTop -= lastMessageHeight });
      }
    }
  }, [messages, shouldAutoScroll]);

  useEffect(() => {
    if (shouldAutoScroll2 && chatContainerRef2.current) {
      chatEndRef2.current.scrollIntoView({ behavior: 'smooth' });
    } else if (chatContainerRef.current) {
    const messagesContainer2 = chatContainerRef2.current;
    const lastMessageElement2 = messagesContainer2.querySelector('.message-container2:first-child');
    if (lastMessageElement2) {
      const lastMessageHeight2 = lastMessageElement2.getBoundingClientRect().height;
      messagesContainer2.scrollTo({ top: messagesContainer2.scrollTop -= lastMessageHeight2 });
    }
  }
}, [messages2, shouldAutoScroll2]);

const toggleAutoScroll = () => {
  setShouldAutoScroll(!shouldAutoScroll);
};

const toggleAutoScroll2 = () => {
  setShouldAutoScroll2(!shouldAutoScroll2);
};

const getFormattedText = (text) => {
  const regex = /((https?:\/\/)|(www\.))[^\s]+/gi;
  const formattedText = text.replace(regex, (match) => {
    let url = match;
    if (!match.includes('://')) {
      url = 'http://' + match;
    }
    return `<a href="${url}" class="message-link" target="_blank" rel="noopener noreferrer">${match}</a>`;
  });
  return formattedText.replace(/\n/g, '<br/>');
};


return (
  <div>
    <div className='allcontainers'>
      <div className='chat01'>
        <div className="chat-container" ref={chatContainerRef}>
          {messages.map((message, i) => (
            <div
              key={i}
              className={`message-container ${i === messages.length - 1 && newMessage ? 'new-message' : ''}`}
            >
              <p className="message">
                <span className="sender">{message.senderName}:</span>
                <br />
                <span
                  className="text"
                  dangerouslySetInnerHTML={{ __html: getFormattedText(message.messageText) }}
                ></span>
                <br/>
                <hr className="horizontal-line" />
                
                <div className='message_bottom'>
                <span className="views">👁️‍🗨️{message.views}</span> {/* Add this line */}
                <span className="timee">🕗{message.timee}</span> {/* Add this line */}
                </div>
              </p>
            </div>
          ))}
          <div ref={chatEndRef}></div>
        </div>
        {messages.length > 18 ? (
          <div className="scroll-toggle">
            <button onClick={toggleAutoScroll}>
              {shouldAutoScroll ? 'Auto Scroll On' : 'Auto Scroll Off'}
            </button>
          </div>
        ) : null}
      </div>
      <div className='chat02'>
        <div className="chat-container" ref={chatContainerRef2}>
          {messages
            .filter((message2) => message2.important)
            .map((message2, i2) => (
              <div
                key={i2}
                className={`message-container ${i2 === messages2.length - 1 && newMessage2 ? 'new-message' : ''}`}
              >
                <p className="message">
                  <b><span className="sender">{message2.senderName}:</span></b>
                  <br />
                  <span
                    className="text"
                    dangerouslySetInnerHTML={{ __html: getFormattedText(message2.messageText) }}
                  ></span>
                   <br/>
                <hr className="horizontal-line" />
                
                <div className='message_bottom'>
                <span className="views">👁️‍🗨️{message2.views}</span> {/* Add this line */}
                <span className="timee">🕗{message2.timee}</span> {/* Add this line */}
                </div>
                </p>
              </div>
            ))}
          <div ref={chatEndRef2}></div>
        </div>
        {messages2.length > 18 ? (
          <div className="scroll-toggle">
            <button onClick={toggleAutoScroll2}>
              {shouldAutoScroll2 ? 'Auto Scroll On' : 'Auto Scroll Off'}
            </button>
          </div>
        ) : null}
      </div>
    </div>
  </div>
);
}

export default Chatmodule;



