import { useState, useRef, useCallback, useEffect } from 'react';
import { sendChatMessage } from '../services/api';

/**
 * Generate a random thread ID for each browser session.
 */
function generateThreadId() {
  return 'thread_' + Math.random().toString(36).substring(2, 15) + Date.now().toString(36);
}

export function useChat(accessToken) {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const threadIdRef = useRef(generateThreadId());
  
  const tokenRef = useRef(accessToken);
  useEffect(() => {
    tokenRef.current = accessToken;
  }, [accessToken]);

  const addMessage = useCallback((role, content) => {
    setMessages((prev) => [...prev, { id: Date.now() + Math.random(), role, content, timestamp: new Date() }]);
  }, []);

  const sendMessage = useCallback(
    async (text) => {
      if (!text.trim() || isLoading) return null;

      addMessage('user', text);
      setIsLoading(true);

      try {
        const response = await sendChatMessage(text, threadIdRef.current, tokenRef.current);
        addMessage('assistant', response.reply);
        return response;
      } catch (error) {
        addMessage('assistant', `Sorry, something went wrong: ${error.message}`);
        return null;
      } finally {
        setIsLoading(false);
      }
    },
    [isLoading, addMessage],
  );

  return { messages, isLoading, sendMessage, addMessage };
}
