import React from 'react';

function ChatMessages({ chatHistory, isTyping, clearChat, chatEndRef }) {
  return (
    <div className="chat-history">
      <div className="chat-header">
        <h3>Conversation</h3>
        <button className="clear-btn" onClick={clearChat}>
          🗑️ Clear Chat
        </button>
      </div>

      <div className="messages">
        {chatHistory.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <div className="message-avatar">
              {msg.role === 'user' ? '👤' : '🤖'}
            </div>
            <div className="message-content">
              <div className="message-role">
                {msg.role === 'user' ? 'You' : 'AI Coach'}
              </div>
              <div className="message-text">
                {msg.content.split('\n').map((line, j) => (
                  <div key={j}>{line}</div>
                ))}
              </div>
            </div>
          </div>
        ))}

        {isTyping && (
          <div className="message assistant typing">
            <div className="message-avatar">🤖</div>
            <div className="message-content">
              <div className="message-role">AI Coach</div>
              <div className="message-text typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        )}

        <div ref={chatEndRef} />
      </div>
    </div>
  );
}

export default ChatMessages;