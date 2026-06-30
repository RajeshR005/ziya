
import { createContext, useContext, useState, useCallback, useEffect } from 'react';
const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [token, setToken] = useState(null);
  const [user, setUser] = useState(null);

  // Stores the pending action to retry after login
  const [pendingAction, setPendingAction] = useState(null);

  const login = useCallback((accessToken, email) => {
    setToken(accessToken);
    setUser({ email });
  }, []);

  const logout = useCallback(() => {
    setToken(null);
    setUser(null);
  }, []);

  const isAuthenticated = !!token;
  return (
    <AuthContext.Provider
      value={{
        token,
        user,
        isAuthenticated,
        login,
        logout,
        pendingAction,
        setPendingAction,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}
