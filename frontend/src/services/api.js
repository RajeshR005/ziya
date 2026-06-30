const API_BASE = "https://ziya-backend.onrender.com/ziya";

/**
 * Generic fetch wrapper with error handling.
 */
async function request(endpoint, options = {}) {
  const url = `${API_BASE}${endpoint}`;
  try {
    const response = await fetch(url, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || `Request failed (${response.status})`);
    }

    return await response.json();
  } catch (error) {
    if (error.message === 'Failed to fetch') {
      throw new Error('Unable to connect to server. Please ensure the backend is running.');
    }
    throw error;
  }
}

/**
 * Authentication helpers (auth token header).
 */
function authHeaders(token) {
  return { Authorization: `Bearer ${token}` };
}

/* ─── Auth ─────────────────────────────────────────────── */

export async function loginUser(email, password) {
  const formData = new URLSearchParams();
  formData.append('username', email);
  formData.append('password', password);

  const response = await fetch(`${API_BASE}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: formData,
  });

  const data = await response.json();

  if (data.status === 0) {
    throw new Error(data.msg || 'Invalid credentials');
  }

  return data;
}

export async function registerUser(userData) {
  const data = await request('/user_registration', {
    method: 'POST',
    body: JSON.stringify(userData),
  });

  if (data.status === 0) {
    throw new Error(data.msg || 'Registration failed');
  }

  return data;
}

/* ─── Chat ─────────────────────────────────────────────── */

export async function sendChatMessage(message, threadId, accessToken = null) {
  return request('/chat', {
    method: 'POST',
    body: JSON.stringify({
      message,
      thread_id: threadId,
      access_token: accessToken,
    }),
  });
}

/* ─── Products ─────────────────────────────────────────── */

export async function getAllProducts() {
  return request('/get_all_products');
}

export async function getOneProduct(productId) {
  return request(`/get_one_product/${productId}`);
}

export async function filterProducts(params) {
  const query = new URLSearchParams();
  Object.entries(params).forEach(([key, val]) => {
    if (val != null && val !== '') query.append(key, val);
  });
  return request(`/filter_products/?${query.toString()}`);
}

export async function getCategories() {
  return request('/categories');
}

export async function getBrands() {
  return request('/brands');
}

export async function getTopRated() {
  return request('/top_rated');
}

export async function getReviews(productIds) {
  return request('/get_reviews', {
    method: 'POST',
    body: JSON.stringify(productIds),
  });
}

/* ─── Cart (Auth Required) ─────────────────────────────── */

export async function getCart(token) {
  return request('/get_cart', {
    headers: authHeaders(token),
  });
}

export async function addToCart(productId, quantity, token) {
  const query = new URLSearchParams({ product_id: productId, quantity: quantity || 1 });
  return request(`/cart?${query.toString()}`, {
    method: 'POST',
    headers: authHeaders(token),
  });
}

export async function updateCart(cartItemId, quantity, token) {
  const query = new URLSearchParams({ cart_item_id: cartItemId, quantity });
  return request(`/cart_update?${query.toString()}`, {
    method: 'POST',
    headers: authHeaders(token),
  });
}
