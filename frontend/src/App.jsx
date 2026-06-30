import { useState, useCallback, useEffect } from 'react';
import { AuthProvider, useAuth } from './hooks/useAuth';
import { useChat } from './hooks/useChat';
import Header from './components/Header/Header';
import Chat from './components/Chat/Chat';
import AuthModal from './components/AuthModal/AuthModal';
import CartDrawer from './components/CartDrawer/CartDrawer';
import './App.css';

function AppContent() {
  const { token, isAuthenticated, pendingAction, setPendingAction } = useAuth();
  const { messages, isLoading, sendMessage } = useChat(token);

  const [showAuth, setShowAuth] = useState(false);
  const [showCart, setShowCart] = useState(false);
  const [cartCount, setCartCount] = useState(0);

  /**
   * Intercept cart-related messages when user is not authenticated.
   * Store the message as a pending action, show login modal,
   * and replay it after successful login.
   */
  const handleSendMessage = useCallback(
    (text) => {
      const cartKeywords = ['add to cart', 'cart', 'add this', 'buy', 'purchase', 'remove from cart', 'update cart', 'show my cart', 'view cart', 'my orders'];
      const isCartAction = cartKeywords.some((kw) => text.toLowerCase().includes(kw));

      if (isCartAction && !isAuthenticated) {
        // Save the message text to replay after login
        setPendingAction(text);
        setShowAuth(true);
        return;
      }

      sendMessage(text);
    },
    [isAuthenticated, sendMessage, setPendingAction],
  );

  useEffect(() => {
    if (isAuthenticated && pendingAction) {
      sendMessage(pendingAction);
      setPendingAction(null);
    }
  }, [isAuthenticated, pendingAction, sendMessage, setPendingAction]);

  return (
    <div className="app">
      <Header
        onCartClick={() => setShowCart(true)}
        onLoginClick={() => setShowAuth(true)}
        cartCount={cartCount}
      />

      <main className="main">
        <Chat
          messages={messages}
          isLoading={isLoading}
          onSendMessage={handleSendMessage}
        />
      </main>

      {showAuth && <AuthModal onClose={() => setShowAuth(false)} />}

      {showCart && isAuthenticated && (
        <CartDrawer
          onClose={() => setShowCart(false)}
          onCartCountChange={setCartCount}
        />
      )}
    </div>
  );
}

export default function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
}
