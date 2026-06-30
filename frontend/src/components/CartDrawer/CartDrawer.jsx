import { useState, useEffect, useCallback } from 'react';
import { HiXMark, HiPlus, HiMinus, HiOutlineShoppingCart } from 'react-icons/hi2';
import { getCart, updateCart } from '../../services/api';
import { useAuth } from '../../hooks/useAuth';
import styles from './CartDrawer.module.css';

export default function CartDrawer({ onClose, onCartCountChange }) {
  const { token } = useAuth();
  const [cartData, setCartData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchCart = useCallback(async () => {
    setLoading(true);
    setError('');
    try {
      const data = await getCart(token);
      if (data.status === 0) {
        setCartData({ products: [], total_cart_value: 0 });
        onCartCountChange?.(0);
      } else {
        setCartData(data);
        onCartCountChange?.(data.products?.length || 0);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [token, onCartCountChange]);

  useEffect(() => {
    fetchCart();
  }, [fetchCart]);

  const handleUpdateQty = async (cartItemId, newQty) => {
    try {
      await updateCart(cartItemId, newQty, token);
      fetchCart();
    } catch (err) {
      setError(err.message);
    }
  };

  const handleRemove = async (cartItemId) => {
    try {
      await updateCart(cartItemId, 0, token);
      fetchCart();
    } catch (err) {
      setError(err.message);
    }
  };

  const products = cartData?.products || [];
  const total = cartData?.total_cart_value || 0;

  return (
    <>
      <div className={styles.overlay} onClick={onClose} />
      <div className={styles.drawer} id="cart-drawer">
        <div className={styles.header}>
          <h2 className={styles.title}>Your Cart</h2>
          <button className={styles.closeBtn} onClick={onClose} aria-label="Close cart">
            <HiXMark />
          </button>
        </div>

        <div className={styles.body}>
          {loading && <div className={styles.loading}>Loading cart...</div>}

          {error && <div className={styles.error}>{error}</div>}

          {!loading && !error && products.length === 0 && (
            <div className={styles.empty}>
              <HiOutlineShoppingCart className={styles.emptyIcon} />
              <p className={styles.emptyText}>Your cart is empty</p>
            </div>
          )}

          {!loading &&
            products.map((item) => (
              <div key={item.cart_item_id} className={styles.cartItem}>
                <div className={styles.itemInfo}>
                  <div className={styles.itemName}>{item.product_name}</div>
                  <div className={styles.itemBrand}>{item.brand}</div>
                  <div className={styles.itemPrice}>₹{item.price?.toLocaleString('en-IN')}</div>
                </div>
                <div className={styles.itemActions}>
                  <div className={styles.qtyControls}>
                    <button
                      className={styles.qtyBtn}
                      onClick={() => handleUpdateQty(item.cart_item_id, (item.quantity || 1) - 1)}
                      aria-label="Decrease quantity"
                    >
                      <HiMinus size={12} />
                    </button>
                    <span className={styles.qtyValue}>{item.quantity || 1}</span>
                    <button
                      className={styles.qtyBtn}
                      onClick={() => handleUpdateQty(item.cart_item_id, (item.quantity || 1) + 1)}
                      aria-label="Increase quantity"
                    >
                      <HiPlus size={12} />
                    </button>
                  </div>
                  <button className={styles.removeBtn} onClick={() => handleRemove(item.cart_item_id)}>
                    Remove
                  </button>
                </div>
              </div>
            ))}
        </div>

        {products.length > 0 && (
          <div className={styles.footer}>
            <div className={styles.totalRow}>
              <span className={styles.totalLabel}>Total</span>
              <span className={styles.totalValue}>₹{total.toLocaleString('en-IN')}</span>
            </div>
          </div>
        )}
      </div>
    </>
  );
}
