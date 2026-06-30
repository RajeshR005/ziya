import { useState, useRef, useEffect } from 'react';
import { HiArrowUp } from 'react-icons/hi2';
import ReactMarkdown from 'react-markdown';
import styles from './Chat.module.css';

const SUGGESTIONS = [
  'Show me laptops under ₹80,000',
  'Find Samsung phones',
  'What are the top rated products?',
  'Compare gaming laptops',
  'Show Apple products',
];

export default function Chat({ messages, isLoading, onSendMessage }) {
  const [input, setInput] = useState('');
  const messagesEndRef = useRef(null);
  const textAreaRef = useRef(null);

  /* Auto-scroll to bottom */
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  /* Auto-resize textarea */
  useEffect(() => {
    if (textAreaRef.current) {
      textAreaRef.current.style.height = 'auto';
      textAreaRef.current.style.height = textAreaRef.current.scrollHeight + 'px';
    }
  }, [input]);

  const handleSend = () => {
    if (!input.trim() || isLoading) return;
    onSendMessage(input.trim());
    setInput('');
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleSuggestion = (text) => {
    onSendMessage(text);
  };

  const hasMessages = messages.length > 0;

  return (
    <div className={styles.chatContainer} id="chat-container">
      <div className={styles.messagesArea}>
        {!hasMessages && (
          <div className={styles.welcome}>
            <div className={styles.welcomeIcon}>Z</div>
            <h1 className={styles.welcomeTitle}>Ziya</h1>
            <p className={styles.welcomeSubtitle}>
              Your intelligent shopping assistant. Search products, compare options, read reviews, and manage your cart — all through conversation.
            </p>
            <p className={styles.welcomeGreeting}>Hi 👋 How can I help you today?</p>

            <div className={styles.suggestions}>
              {SUGGESTIONS.map((s) => (
                <button
                  key={s}
                  className={styles.suggestion}
                  onClick={() => handleSuggestion(s)}
                >
                  {s}
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`${styles.messageRow} ${
              msg.role === 'user' ? styles.messageRowUser : styles.messageRowAssistant
            }`}
          >
            {msg.role === 'assistant' && (
              <div className={`${styles.avatar} ${styles.avatarAssistant}`}>Z</div>
            )}
            <div
              className={`${styles.bubble} ${
                msg.role === 'user' ? styles.bubbleUser : styles.bubbleAssistant
              }`}
            >
              {msg.role === 'assistant' ? (
                <ReactMarkdown>{msg.content}</ReactMarkdown>
              ) : (
                msg.content
              )}
            </div>
            {msg.role === 'user' && (
              <div className={`${styles.avatar} ${styles.avatarUser}`}>
                <HiArrowUp size={14} />
              </div>
            )}
          </div>
        ))}

        {isLoading && (
          <div className={styles.thinking}>
            <div className={`${styles.avatar} ${styles.avatarAssistant}`}>Z</div>
            <div className={styles.thinkingBubble}>
              <div className={styles.dot} />
              <div className={styles.dot} />
              <div className={styles.dot} />
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <div className={styles.inputArea}>
        <div className={styles.inputWrapper}>
          <textarea
            ref={textAreaRef}
            className={styles.textInput}
            placeholder="Message Ziya..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            rows={1}
            id="chat-input"
          />
          <button
            className={styles.sendBtn}
            onClick={handleSend}
            disabled={!input.trim() || isLoading}
            id="send-button"
            aria-label="Send message"
          >
            <HiArrowUp />
          </button>
        </div>
      </div>
    </div>
  );
}
