import { HiOutlineShoppingCart, HiOutlineUser } from 'react-icons/hi2';
import { useAuth } from '../../hooks/useAuth';
import styles from './Header.module.css';

export default function Header({ onCartClick, onLoginClick, cartCount }) {
  const { isAuthenticated, user, logout } = useAuth();

  return (
    <header className={styles.header} id="app-header">
      <div className={styles.logo}>
        <div className={styles.logoIcon}>Z</div>
        <span className={styles.logoText}>Ziya</span>
      </div>

      <div className={styles.actions}>
        {isAuthenticated && (
          <button
            className={styles.iconBtn}
            onClick={onCartClick}
            id="cart-button"
            aria-label="View cart"
          >
            <HiOutlineShoppingCart />
            {cartCount > 0 && (
              <span className={styles.cartBadge}>{cartCount}</span>
            )}
          </button>
        )}

        {isAuthenticated ? (
          <button className={styles.userBtn} onClick={logout} id="user-button">
            <span className={styles.userAvatar}>
              {user?.email?.charAt(0).toUpperCase()}
            </span>
            <span>Logout</span>
          </button>
        ) : (
          <button
            className={styles.loginBtn}
            onClick={onLoginClick}
            id="login-button"
          >
            Sign in
          </button>
        )}
      </div>
    </header>
  );
}
