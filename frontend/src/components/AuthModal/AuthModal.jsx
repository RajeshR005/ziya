import { useState } from 'react';
import { HiXMark } from 'react-icons/hi2';
import { loginUser, registerUser } from '../../services/api';
import { useAuth } from '../../hooks/useAuth';
import styles from './AuthModal.module.css';

export default function AuthModal({ onClose }) {
  const [mode, setMode] = useState('login'); // 'login' | 'register'
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const { login, pendingAction, setPendingAction } = useAuth();

  /* ─── Login ──────────────────────────────────────────── */
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const data = await loginUser(email, password);
      login(data.access_token, email);
      onClose();

    } catch (err) {
      setError(err.message || 'Invalid credentials');
    } finally {
      setLoading(false);
    }
  };

  /* ─── Register ───────────────────────────────────────── */
  const [regData, setRegData] = useState({
    first_name: '',
    last_name: '',
    date_of_birth: '',
    email: '',
    password: '',
    confirm_password: '',
    phone_number: '',
  });

  const updateReg = (field, value) => {
    setRegData((prev) => ({ ...prev, [field]: value }));
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');
    setLoading(true);

    if (regData.password !== regData.confirm_password) {
      setError('Passwords do not match');
      setLoading(false);
      return;
    }

    try {
      await registerUser(regData);
      setSuccess('Account created successfully! Please sign in.');
      setTimeout(() => {
        setMode('login');
        setEmail(regData.email);
        setSuccess('');
      }, 1500);
    } catch (err) {
      setError(err.message || 'Registration failed');
    } finally {
      setLoading(false);
    }
  };

  const switchMode = (newMode) => {
    setMode(newMode);
    setError('');
    setSuccess('');
  };

  return (
    <div className={styles.overlay} onClick={onClose} id="auth-overlay">
      <div className={styles.modal} onClick={(e) => e.stopPropagation()} id="auth-modal">
        <button className={styles.closeBtn} onClick={onClose} aria-label="Close">
          <HiXMark />
        </button>

        {mode === 'login' ? (
          <>
            <h2 className={styles.title}>Welcome back</h2>
            <p className={styles.subtitle}>Sign in to manage your cart and orders</p>

            {error && <div className={styles.error}>{error}</div>}

            <form onSubmit={handleLogin}>
              <div className={styles.field}>
                <label className={styles.label}>Email</label>
                <input
                  className={styles.input}
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@example.com"
                  required
                  id="login-email"
                />
              </div>

              <div className={styles.field}>
                <label className={styles.label}>Password</label>
                <input
                  className={styles.input}
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Enter your password"
                  required
                  id="login-password"
                />
              </div>

              <button className={styles.submitBtn} type="submit" disabled={loading} id="login-submit">
                {loading ? 'Signing in...' : 'Sign in'}
              </button>
            </form>

            <p className={styles.switchText}>
              Don't have an account?{' '}
              <button className={styles.switchLink} onClick={() => switchMode('register')}>
                Create one
              </button>
            </p>
          </>
        ) : (
          <>
            <h2 className={styles.title}>Create account</h2>
            <p className={styles.subtitle}>Join Ziya to start shopping</p>

            {error && <div className={styles.error}>{error}</div>}
            {success && <div className={styles.success}>{success}</div>}

            <form onSubmit={handleRegister}>
              <div style={{ display: 'flex', gap: '12px' }}>
                <div className={styles.field} style={{ flex: 1 }}>
                  <label className={styles.label}>First Name</label>
                  <input
                    className={styles.input}
                    value={regData.first_name}
                    onChange={(e) => updateReg('first_name', e.target.value)}
                    placeholder="John"
                    required
                    id="reg-first-name"
                  />
                </div>
                <div className={styles.field} style={{ flex: 1 }}>
                  <label className={styles.label}>Last Name</label>
                  <input
                    className={styles.input}
                    value={regData.last_name}
                    onChange={(e) => updateReg('last_name', e.target.value)}
                    placeholder="Doe"
                    required
                    id="reg-last-name"
                  />
                </div>
              </div>

              <div className={styles.field}>
                <label className={styles.label}>Email</label>
                <input
                  className={styles.input}
                  type="email"
                  value={regData.email}
                  onChange={(e) => updateReg('email', e.target.value)}
                  placeholder="you@example.com"
                  required
                  id="reg-email"
                />
              </div>

              <div className={styles.field}>
                <label className={styles.label}>Phone Number</label>
                <input
                  className={styles.input}
                  type="tel"
                  value={regData.phone_number}
                  onChange={(e) => updateReg('phone_number', e.target.value)}
                  placeholder="10-digit phone number"
                  required
                  id="reg-phone"
                />
              </div>

              <div className={styles.field}>
                <label className={styles.label}>Date of Birth</label>
                <input
                  className={styles.input}
                  type="date"
                  value={regData.date_of_birth}
                  onChange={(e) => updateReg('date_of_birth', e.target.value)}
                  required
                  id="reg-dob"
                />
              </div>

              <div className={styles.field}>
                <label className={styles.label}>Password</label>
                <input
                  className={styles.input}
                  type="password"
                  value={regData.password}
                  onChange={(e) => updateReg('password', e.target.value)}
                  placeholder="Create a password"
                  required
                  id="reg-password"
                />
              </div>

              <div className={styles.field}>
                <label className={styles.label}>Confirm Password</label>
                <input
                  className={styles.input}
                  type="password"
                  value={regData.confirm_password}
                  onChange={(e) => updateReg('confirm_password', e.target.value)}
                  placeholder="Confirm your password"
                  required
                  id="reg-confirm-password"
                />
              </div>

              <button className={styles.submitBtn} type="submit" disabled={loading} id="reg-submit">
                {loading ? 'Creating account...' : 'Create account'}
              </button>
            </form>

            <p className={styles.switchText}>
              Already have an account?{' '}
              <button className={styles.switchLink} onClick={() => switchMode('login')}>
                Sign in
              </button>
            </p>
          </>
        )}
      </div>
    </div>
  );
}
