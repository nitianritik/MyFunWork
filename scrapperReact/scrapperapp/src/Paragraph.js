// import React, { useState, useEffect, useRef } from 'react';
// // import { w3cwebsocket as WebSocket } from 'websocket';
// import './Paragraph.css';

// // const ws = new WebSocket('ws://localhost:8000/');
// import { ws } from './index.js';


// function Paragraph() {
//   const [messages, setMessages] = useState([]);
//   const [newMessage, setNewMessage] = useState(false);
//   const chatEndRef = useRef(null);
//   const chatContainerRef = useRef(null);
//   const [shouldAutoScroll, setShouldAutoScroll] = useState(true);

//   useEffect(() => {
//     ws.onmessage = (event) => {
//       const data = JSON.parse(event.data);
//       setMessages((prevMessages) => {
//         // keep only the last 99 messages and add the new one
//         const newMessages = [...prevMessages.slice(-199), data];
//         setNewMessage(true);
//         setTimeout(() => setNewMessage(false), 5000); // Hide new message indicator after 5 seconds
//         return newMessages;
//       });
//     };
//   }, []);

//   useEffect(() => {
//     if (shouldAutoScroll) {
//       chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
//     } else {
//       const messagesContainer = chatContainerRef.current;
//       const lastMessageElement = messagesContainer.querySelector('.message-container:first-child');
//       const lastMessageHeight = lastMessageElement.getBoundingClientRect().height;
//       messagesContainer.scrollTo({ top: messagesContainer.scrollTop -= lastMessageHeight });
//     }
//   }, [messages, shouldAutoScroll]);

//   const toggleAutoScroll = () => {
//     setShouldAutoScroll(!shouldAutoScroll);
//   };

//   const getFormattedText = (text) => {
//     // Find links in the text and replace them with HTML anchor tags
//     const regex = /((https?:\/\/)|(www\.))[^\s]+/gi;
//     return text.replace(regex, (match) => {
//       let url = match;
//       if (!match.includes('://')) {
//         url = 'http://' + match;
//       }
//       return `<a href="${url}" class="message-link" target="_blank" rel="noopener noreferrer">${match}</a>`;
//     });
//   };

//   return (
//     <div className='chat01'>
//     <div>
//     {messages.length > 18 ? (
//       <div className="scroll-toggle">
//         <button onClick={toggleAutoScroll}>
//           {shouldAutoScroll ? 'Auto Scroll On' : 'Auto Scroll Off'}
//         </button>
//       </div>
//     ) : null}
//       <div className="chat-container" ref={chatContainerRef}>
//         {messages.map((message, i) => (
//           <div
//             key={i}
//             className={`message-container ${
//               i === messages.length - 1 && newMessage ? 'new-message' : ''
//             }`}
//           >
//             <p className="message">
//               <span className="sender">{message.senderName}:</span>
//               <br />
//               <span
//                 className="text"
//                 dangerouslySetInnerHTML={{ __html: getFormattedText(message.messageText) }}
//               ></span>
//             </p>
//           </div>
//         ))}
//         <div ref={chatEndRef}></div>
//       </div>
//     </div>
//     </div>
//   );
// }

// export default Paragraph;
