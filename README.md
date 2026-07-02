<div align="center">

# 🛍️ Ziya — Agentic AI Shopping Assistant

### Conversational Commerce powered by Agentic AI

Build smarter shopping experiences using **FastAPI**, **LangGraph**, **LangChain**, **Groq**, and **MySQL**.

<br>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/LangChain-Agentic_AI-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LangGraph-Workflow-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Groq-Qwen3--27B-orange?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Alembic-Migrations-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Production_Ready-success?style=for-the-badge" />
</p>

<br>

---

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Vercel-000000?style=for-the-badge)](https://ziya-ecru.vercel.app)     [![Backend API](https://img.shields.io/badge/⚡_Backend-Render-46E3B7?style=for-the-badge)](https://ziya-backend.onrender.com)     [![Swagger Docs](https://img.shields.io/badge/📚_Swagger_API-Documentation-85EA2D?style=for-the-badge)](https://ziya-backend.onrender.com/docs) 

</div>

---

## 📖 Table of Contents

<details>
<summary>Click to expand</summary>

- [📖 Overview](#-overview)
- [✨ Key Highlights](#-key-highlights)
- [🏆 Skills Demonstrated](#-skills-demonstrated)
- [📸 Demo & Screenshots](#-demo--screenshots)
- [⚙️ Technology Stack](#️-technology-stack)
- [🏛 System Architecture](#-system-architecture)
- [🏗 Backend Architecture](#-backend-architecture)
- [🗄 Database Design](#-database-design)
- [🤖 Agentic AI & Tools](#-agentic-ai--tools)
- [🛍 AI Shopping Workflow](#-ai-shopping-workflow)
- [🔐 Authentication & Security](#-authentication--security)
- [🌐 REST API Reference](#-rest-api-reference)
- [🚀 Installation & Setup](#-installation--setup)
- [🔑 Environment Variables](#-environment-variables)
- [☁️ Deployment Guide](#️-deployment-guide)
- [🗺 Project Roadmap](#-project-roadmap)
- [❓ Troubleshooting](#-troubleshooting)
- [💬 FAQ](#-faq)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)
- [👨‍💻 Author](#-author)

</details>

---

## 📖 Overview

**Ziya** is an **Agentic AI-powered shopping assistant** built with **FastAPI**, **LangGraph**, **LangChain**, **Groq LLM**, and **MySQL**, delivering an intelligent conversational shopping experience.

Instead of relying on prompt engineering alone, Ziya follows an **Agentic AI architecture** — the language model reasons about intent, selects the appropriate backend tool, retrieves live application data through REST APIs, and generates responses grounded in real product information. Users explore products naturally through conversation, with authentication, cart management, and product discovery unified into a single AI workflow.

> Developed to demonstrate production-grade backend engineering combined with Agentic AI application development — showing how modern LLMs can safely interact with real business systems through structured tools.

---

## ✨ Key Highlights

| Feature | Description |
|---------|-------------|
| 🤖 **Agentic AI** | Tool-driven reasoning using LangGraph + LangChain |
| ⚡ **FastAPI Backend** | Modular, production-oriented REST API architecture |
| 🛍 **Conversational Shopping** | Natural language product discovery, filtering & comparison |
| 🔍 **Smart Filtering** | Filter by brand, category, price range, and ratings |
| ⭐ **Review Aggregation** | Customer review retrieval and AI-powered summaries |
| 🔐 **JWT Authentication** | Secure authentication for protected shopping operations |
| 🛒 **Cart Management** | Add, update, and view cart through conversation |
| 💬 **Conversation Memory** | Thread-based context for multi-turn interactions |
| 🗄 **MySQL + SQLAlchemy** | Relational database with ORM and Alembic migrations |
| 🚀 **Production Deployed** | Backend on Render, Frontend on Vercel |

---

## 🏆 Skills Demonstrated

<table>
<tr>
<td width="50%" valign="top">

### 🔧 Backend Engineering
- FastAPI REST API Design
- SQLAlchemy ORM
- Alembic Database Migrations
- MySQL Database Design
- JWT Authentication
- Pydantic Data Validation
- Dependency Injection
- Environment-Based Configuration

</td>
<td width="50%" valign="top">

### 🧠 Agentic AI
- LangChain Tool Calling
- LangGraph Agent Orchestration
- Groq LLM Integration (Qwen3-27B)
- Prompt Engineering
- Conversational Memory
- Multi-Step Reasoning
- Grounded AI Responses
- Authentication-Aware AI

</td>
</tr>
</table>

---

## 📸 Demo & Screenshots

<div align="center">

![Ziya Chat Interface](https://github.com/user-attachments/assets/c3d507a3-53eb-49fc-b0f7-c662bfc46f31)

<i>AI-powered conversational shopping in action</i>

</div>

<details>
<summary><b>🖼 View more screenshots</b></summary>
<br/>
  
| Screenshot | Description |
|:---:|:---|
| ![Product Search](https://github.com/user-attachments/assets/2f3e4fff-5fe4-4d6d-a440-c981e5b58476) | **Product Discovery** — AI-powered product search and filtering |
| ![Cart Management](https://github.com/user-attachments/assets/acf6bc70-e399-405c-8527-f121df794f85) | **Shopping Cart** — Add, update, and manage cart through conversation |
| ![Register](https://github.com/user-attachments/assets/e9d68fa4-6309-4904-a30e-542308293cec) | **Register** — Create a new account |
| ![Login](https://github.com/user-attachments/assets/5a51b49d-1bdc-4f44-9a9d-3741eb09f122) | **Login** — JWT-based secure authentication |
| ![Swagger UI](https://github.com/user-attachments/assets/6c2cfe52-0f03-49eb-969c-d86547f7db03) | **Swagger Documentation** — Interactive API explorer |

</details>

---

## ⚙️ Technology Stack

| Category | Technology | Purpose |
|----------|------------|---------|
| **Backend Framework** | FastAPI | High-performance REST API development |
| **Language** | Python 3.12 | Core application development |
| **Database** | MySQL | Relational data storage |
| **ORM** | SQLAlchemy | Database abstraction & object-relational mapping |
| **Migrations** | Alembic | Version-controlled schema evolution |
| **Validation** | Pydantic | Request/response data validation |
| **Authentication** | JWT (python-jose) | Stateless user authentication |
| **Password Hashing** | Passlib | Secure credential storage |
| **AI Framework** | LangChain | Tool integration & LLM orchestration |
| **Agent Framework** | LangGraph | Stateful agent workflow execution |
| **LLM Provider** | Groq | High-speed LLM inference |
| **Language Model** | Qwen 3 27B | Conversational reasoning |
| **Frontend** | React + Vite | Client-side chat interface |
| **Backend Deployment** | Render | FastAPI hosting |
| **Frontend Deployment** | Vercel | React app hosting |

---

## 🏛 System Architecture

Ziya follows a layered architecture where the **React frontend**, **FastAPI backend**, **Agentic AI workflow**, and **MySQL database** work together through clearly defined responsibilities.

```text
                                   User
                                     │
                                     ▼
                        React + Vite Frontend (Vercel)
                                     │
                          HTTP / REST Requests
                                     │
                                     ▼
                            FastAPI Backend (Render)
                                     │
               ┌─────────────────────┴─────────────────────┐
               │                                           │
               ▼                                           ▼
      Product & User APIs                         AI Chat Endpoint
               │                                           │
               │                                   LangGraph Agent
               │                                           │
               │                                   Groq (Qwen 3 27B)
               │                                           │
               │                               LangChain Tool Selection
               │                                           │
               └─────────────────────┬─────────────────────┘
                                     │
                                     ▼
                           SQLAlchemy ORM Layer
                                     │
                                     ▼
                                MySQL Database
```

### 🎯 Architectural Principles

| Principle | Implementation |
|-----------|----------------|
| **Separation of Concerns** | Frontend, Backend, AI, and Database are independently organized |
| **Modular Design** | Every major responsibility resides in its own module |
| **REST-first** | All business operations are exposed through REST APIs |
| **Tool-based AI** | The LLM interacts only through LangChain tools |
| **Database Abstraction** | SQLAlchemy isolates application logic from SQL |
| **Stateless APIs** | Authentication via JWT tokens — no server-side sessions |
| **Layered Design** | Presentation → API → AI → Business Logic → Database |

---

## 🏗 Backend Architecture

The backend uses a **modular, production-oriented architecture** that separates API routing, business logic, database access, authentication, and AI integration into independent components.

### 📂 Project Structure

```text
ziya/
│
├── app/                               # FastAPI application
│   ├── api/                           # REST API endpoints
│   │   ├── routers.py                 #   Central API router
│   │   ├── login.py                   #   User authentication
│   │   ├── register_user.py           #   User registration
│   │   ├── chat.py                    #   AI chat endpoint
│   │   ├── all_products.py            #   Full product catalog
│   │   ├── one_product.py             #   Single product details
│   │   ├── filter_products.py         #   Dynamic product filtering
│   │   ├── category_api.py            #   Product categories
│   │   ├── brands_api.py              #   Available brands
│   │   ├── top_rated.py               #   Top-rated products
│   │   ├── get_reviews.py             #   Customer reviews
│   │   ├── add_cart.py                #   Add to cart
│   │   ├── cart_update.py             #   Update cart
│   │   └── show_orders.py             #   View cart/orders
│   │
│   ├── db/                            # Database configuration
│   │   ├── base.py                    #   ORM base model
│   │   ├── session.py                 #   Session management
│   │   └── create_db.py               #   DB initialization
│   │
│   ├── models/                        # SQLAlchemy ORM models
│   │   ├── user.py                    #   User entity
│   │   ├── product.py                 #   Product entity
│   │   ├── review.py                  #   Review entity
│   │   └── cart.py                    #   Cart entity
│   │
│   ├── schemas/                       # Pydantic validation schemas
│   │   └── register_user_schema.py
│   │
│   ├── seed_data/                     # Initial datasets
│   │   ├── products_dump.py           #   Product catalog seed
│   │   └── review_dump.py             #   Reviews seed
│   │
│   ├── deps.py                        # Shared dependencies
│   └── utils.py                       # Utility helpers
│
├── ziya/                              # Agentic AI Layer
│   ├── agent.py                       #   LangGraph workflow
│   ├── prompts.py                     #   System prompt
│   └── tools/                         #   LangChain tools
│       ├── all_products_tool.py
│       ├── filter_products_tool.py
│       ├── one_product_tool.py
│       ├── auth_tool.py
│       ├── manage_cart.py
│       └── view_cart_tool.py
│
├── alembic/                           # Database migrations
│   ├── env.py
│   ├── versions/
│   └── script.py.mako
│
├── frontend/                          # React + Vite frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chat/                  #   Chat interface
│   │   │   ├── AuthModal/             #   Login/Register modal
│   │   │   ├── CartDrawer/            #   Shopping cart drawer
│   │   │   └── Header/                #   Navigation header
│   │   ├── hooks/
│   │   │   ├── useAuth.jsx            #   Authentication hook
│   │   │   └── useChat.js             #   Chat logic hook
│   │   └── services/
│   │       └── api.js                 #   API client
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── main.py                            # Application entry point
├── requirements.txt                   # Python dependencies
├── render.yaml                        # Render deployment config
├── alembic.ini                        # Alembic configuration
└── .env                               # Environment variables
```

### 📦 Module Responsibilities

| Directory | Responsibility |
|-----------|----------------|
| `app/api/` | REST API endpoints for authentication, products, reviews, cart, and AI chat |
| `app/models/` | SQLAlchemy ORM models — Users, Products, Reviews, Cart |
| `app/schemas/` | Pydantic models for request validation and response serialization |
| `app/db/` | Database engine, session management, and base model configuration |
| `app/seed_data/` | Seed scripts to populate the database with sample products and reviews |
| `ziya/` | Complete Agentic AI implementation — LangGraph agent, tools, and prompts |
| `ziya/tools/` | Custom LangChain tools bridging the AI agent to FastAPI endpoints |
| `alembic/` | Version-controlled database migration scripts |
| `frontend/` | React + Vite conversational shopping interface |

---

## 🗄 Database Design

A **normalized relational schema** designed around the core shopping workflow with four primary entities.

### 🏛 Entity Relationship Diagram

```text
                    ┌─────────────────────┐
                    │       Users         │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
               1:N  ▼                     ▼  1:N
          ┌─────────────┐          ┌─────────────┐
          │    Cart     │          │   Reviews   │
          └──────┬──────┘          └──────┬──────┘
                 │                        │
            N:1  ▼                        ▼  N:1
          ┌──────────────────────────────────────┐
          │              Products                │
          └──────────────────────────────────────┘
```

### 📋 Database Tables

<details>
<summary><b>👤 Users</b></summary>

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer (PK) | Auto-increment primary key |
| `first_name` | String(100) | Customer first name |
| `last_name` | String(100) | Customer last name |
| `date_of_birth` | Date | Date of birth |
| `email` | String(100) | Unique login email (indexed) |
| `password` | String(300) | Hashed password |
| `phone_number` | String(50) | Contact number |
| `role` | String(50) | User role (default: `user`) |
| `status` | Integer | Account status (1 = active) |
| `created_at` | DateTime | Record creation timestamp |
| `created_by` | Integer (FK) | Creator reference |
| `modified_at` | DateTime | Last modification timestamp |
| `modified_by` | Integer (FK) | Modifier reference |

</details>

<details>
<summary><b>🛍 Products</b></summary>

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer (PK) | Auto-increment primary key |
| `product_name` | String(255) | Product title (indexed) |
| `brand` | String(100) | Brand name |
| `category` | String(100) | Product category |
| `description` | Text | Product description |
| `price` | Float | Selling price |
| `stock_quantity` | Integer | Available inventory |
| `average_rating` | Float | Aggregated customer rating |
| `status` | Integer | Product availability |

</details>

<details>
<summary><b>⭐ Reviews</b></summary>

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer (PK) | Auto-increment primary key |
| `product_id` | Integer (FK) | Associated product |
| `user_id` | Integer (FK) | Review author |
| `rating` | Float | Numeric rating |
| `review_text` | Text | Customer review content |

</details>

<details>
<summary><b>🛒 Cart</b></summary>

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer (PK) | Auto-increment primary key |
| `user_id` | Integer (FK) | Cart owner |
| `product_id` | Integer (FK) | Selected product |
| `quantity` | Integer | Number of items (default: 1) |

</details>

### 🔗 Entity Relationships

| Relationship | Type | Description |
|--------------|------|-------------|
| User → Cart | One-to-Many | A user owns multiple cart items |
| User → Reviews | One-to-Many | A user writes multiple reviews |
| Product → Cart | One-to-Many | A product appears in many carts |
| Product → Reviews | One-to-Many | A product receives multiple reviews |

---

## 🤖 Agentic AI & Tools

Ziya is built on an **Agentic AI architecture** where the language model actively reasons, selects tools, retrieves live application data, and generates grounded responses. All interactions between the agent and the platform happen through **custom LangChain tools**, each mapped to a FastAPI endpoint.

### 🧠 How the Agent Thinks

```text
                    User Query
                         │
                         ▼
              LangGraph Agent Starts
                         │
                         ▼
              Understand User Intent
                         │
                         ▼
          Decide Whether Tools Are Needed
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
  Tool Required                 General Conversation
          │                             │
          ▼                             ▼
  Select Tool → Execute API      Generate Response
          │
          ▼
  Receive Live Data → Generate Grounded Response
          │
          ▼
      Return to User
```

### 📦 Tools, Endpoints & Access

| Tool | Backend Endpoint | Responsibility | Auth |
|------|-----------------|----------------|:---:|
| `all_products_tool` | `GET /ziya/get_all_products` | Retrieve complete product catalog | ❌ |
| `filter_products_tool` | `GET /ziya/filter_products` | Filter by brand, category, price, rating | ❌ |
| `one_product_tool` | `GET /ziya/get_one_product/{id}` | Product details + customer reviews | ❌ |
| `auth_tool` | `POST /ziya/login` | Authenticate user & store JWT | ❌ |
| `manage_cart` | `POST /ziya/cart` · `POST /ziya/cart_update` | Add/update cart items | ✅ |
| `view_cart_tool` | `GET /ziya/get_cart` | Retrieve authenticated user's cart | ✅ |

### 💬 Conversation Memory

Thread-based memory enables natural multi-turn conversations. The agent maintains context across the session — no need to repeat previous information:

```
User: Show Apple laptops.
  ↓
User: Only show ones below ₹80,000.
  ↓
User: Tell me more about the first one.
  ↓
User: Add it to my cart.
```

### 🔒 Grounded Responses

The model is explicitly instructed to:

- ❌ Never invent products, prices, ratings, stock, or reviews
- ✅ Always retrieve data from backend APIs

### ⚡ Why LangGraph? (vs a Traditional Chatbot)

| Traditional Chatbot | Ziya (Agentic AI) |
|---------------------|-------------------|
| Prompt-only reasoning | Tool-driven reasoning |
| Static/pretrained knowledge | Live backend data |
| Higher hallucination risk | Grounded responses |
| Cannot perform actions | Executes backend operations |
| Limited business awareness | Integrated with shopping workflow |

---

## 🛍 AI Shopping Workflow

Every user interaction follows a deterministic pipeline combining the frontend, backend, Agentic AI, and database:

```text
User → React Chat UI → POST /ziya/chat → FastAPI → LangGraph Agent
  → LLM Reasoning → Tool Selection → FastAPI REST API
  → SQLAlchemy → MySQL → JSON Response
  → LLM Generates Reply → React Renders Response → User
```

### 🧠 Example Workflows

<details>
<summary><b>🔍 Product Discovery</b></summary>

```
User: "Show me laptops under ₹80,000"
  → Intent: product filtering
  → filter_products_tool(category="laptop", max_price=80000)
  → GET /ziya/filter_products?category=laptop&max_price=80000
  → MySQL returns matching products
  → LLM formats results as a conversational response
```
</details>

<details>
<summary><b>📦 Product Details</b></summary>

```
User: "Tell me about MacBook Air"
  → Intent: product details
  → one_product_tool(product_id=...)
  → GET /ziya/get_one_product/{id}
  → Returns product info + customer reviews
  → LLM summarizes specifications, price, and reviews
```
</details>

<details>
<summary><b>🛒 Cart Management</b></summary>

```
User: "Add HP Victus to my cart"
  → Intent: cart operation (protected)
  → Verifies JWT authentication
  → manage_cart(product_id=..., quantity=1)
  → POST /ziya/cart (Authorization: Bearer <JWT>)
  → Database updated
  → LLM confirms: "HP Victus has been added to your cart!"
```
</details>

---

## 🔐 Authentication & Security

JWT-based authentication secures protected operations while allowing anonymous browsing of the product catalog.

### 🏛 Authentication Flow

```text
User Login (Email + Password)
  → POST /ziya/login → Verify Credentials → Generate JWT Token
  → Frontend Stores Token → Authorization: Bearer <JWT>
  → Protected API Access
```

### 🛡 Access Control

| Operation | Auth Required |
|-----------|:---:|
| Browse Products | ❌ |
| Filter Products | ❌ |
| View Product Details | ❌ |
| Read Reviews | ❌ |
| Chat with AI | ❌ |
| Add to Cart | ✅ |
| Update Cart | ✅ |
| View Cart | ✅ |

### 🔑 Security Practices

- Passwords hashed before storage (never stored in plain text)
- JWT-based stateless authentication
- Protected endpoints validate the `Authorization: Bearer <token>` header
- AI agent never handles passwords directly
- User-specific cart isolation through token validation
- Secrets stored in environment variables

---

## 🌐 REST API Reference

Full interactive documentation is available at [`/docs`](https://ziya-backend.onrender.com/docs) (Swagger UI) and [`/redoc`](https://ziya-backend.onrender.com/redoc) (ReDoc).

### 🔐 Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/ziya/user_registration` | Register a new user |
| `POST` | `/ziya/login` | Authenticate & receive JWT |

### 🛍 Products

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/ziya/get_all_products` | Retrieve full product catalog |
| `GET` | `/ziya/get_one_product/{id}` | Get single product details |
| `GET` | `/ziya/filter_products` | Filter by brand, category, price, rating |
| `GET` | `/ziya/top_rated` | Get highest-rated products |
| `GET` | `/ziya/categories` | List available categories |
| `GET` | `/ziya/brands` | List available brands |

### ⭐ Reviews

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/ziya/get_reviews` | Retrieve reviews for products |

### 🛒 Cart `🔒 Protected`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/ziya/cart` | Add product to cart |
| `POST` | `/ziya/cart_update` | Update cart item quantity |
| `GET` | `/ziya/get_cart` | Retrieve current user's cart |

### 🤖 AI Chat

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/ziya/chat` | Conversational AI shopping endpoint |

**Chat Request Body:**
```json
{
  "message": "Show me laptops under ₹80,000",
  "thread_id": "unique-session-id",
  "token": "jwt-access-token (optional)"
}
```

---

## 🚀 Installation & Setup

### Prerequisites

- **Python** 3.12+
- **Node.js** 18+
- **MySQL** 8.0+
- **Git**
- **Groq API Key** — [Get one here](https://console.groq.com)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/RajeshR005/ziya.git
cd ziya
```

### 2️⃣ Backend Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root — see the [Environment Variables](#-environment-variables) section for the full list.

### 4️⃣ Database Setup

```bash
# Create the database
mysql -u root -p -e "CREATE DATABASE ziya_db;"

# Run Alembic migrations
alembic upgrade head

# (Optional) Seed sample data
python -c "from app.seed_data.products_dump import seed_products; seed_products()"
python -c "from app.seed_data.review_dump import seed_reviews; seed_reviews()"
```

### 5️⃣ Start the Backend

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend: `http://localhost:8000` · Swagger docs: `http://localhost:8000/docs`

### 6️⃣ Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create frontend .env
echo "VITE_API_URL=http://localhost:8000" > .env

# Start development server
npm run dev
```

Frontend: `http://localhost:5173`

---

## 🔑 Environment Variables

### Backend (`.env`)

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | MySQL connection string | `mysql+pymysql://user:pass@host:3306/ziya_db` |
| `SECRET_KEY` | JWT signing secret | `your-super-secret-key` |
| `GROQ_API_KEY` | Groq API key for LLM inference | `gsk_...` |
| `BASE_API_URL` | Backend base URL (used by AI tools) | `http://localhost:8000` |
| `FRONTEND_URL` | Frontend URL (for CORS) | `http://localhost:5173` |

### Frontend (`.env`)

| Variable | Description | Example |
|----------|-------------|---------|
| `VITE_API_URL` | Backend API base URL | `http://localhost:8000` |

> ⚠️ **Never commit `.env` files to version control.** The `.gitignore` already excludes them.

---

## ☁️ Deployment Guide

Ziya uses a split deployment: **Render** for the backend, **Vercel** for the frontend, and a managed **MySQL** cloud database.

```text
        User
         │
         ▼
  Vercel (React) ──── CDN
         │
    REST APIs
         │
         ▼
  Render (FastAPI) ──── Groq API (LLM)
         │
   SQLAlchemy
         │
         ▼
  MySQL (Cloud)
```

### 🟢 Backend — Render

1. Connect your GitHub repository to [Render](https://render.com)
2. Build command: `pip install -r requirements.txt`
3. Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Add all backend environment variables in Render's dashboard
5. The `render.yaml` file can automate this setup

### 🔵 Frontend — Vercel

1. Connect the `frontend/` directory to [Vercel](https://vercel.com)
2. Set root directory to `frontend`
3. Framework preset: **Vite**
4. Add `VITE_API_URL` pointing to your Render backend URL
5. Deploy

### 🗄 Database — Managed MySQL

Use any managed provider: [PlanetScale](https://planetscale.com) · [Railway](https://railway.app) · [AWS RDS](https://aws.amazon.com/rds/) · [Aiven](https://aiven.io)

---

## 🗺 Project Roadmap

- [x] 🤖 Agentic AI shopping assistant with LangGraph
- [x] 🛍 Natural language product discovery
- [x] 🔍 Multi-criteria product filtering
- [x] ⭐ Customer review retrieval
- [x] 🔐 JWT authentication
- [x] 🛒 Shopping cart management
- [x] 💬 Thread-based conversation memory
- [x] 🚀 Production deployment (Render + Vercel)
- [ ] ❤️ Wishlist functionality
- [ ] 📦 Order history & tracking
- [ ] 🖼 Image-based product search
- [ ] 🎯 Personalized product recommendations

---

## ❓ Troubleshooting

<details>
<summary><b>🔴 Backend fails to start</b></summary>

- Verify all environment variables are set in `.env`
- Check MySQL is running and `DATABASE_URL` is correct
- Ensure `alembic upgrade head` was run successfully
- Confirm Python 3.12+ is being used

</details>

<details>
<summary><b>🔴 Database connection error</b></summary>

- Verify MySQL service is running
- Check the `DATABASE_URL` format: `mysql+pymysql://user:pass@host:3306/db_name`
- Ensure the database exists: `mysql -e "SHOW DATABASES;"`
- For cloud databases, verify the host is whitelisted

</details>

<details>
<summary><b>🔴 Groq API errors</b></summary>

- Verify your `GROQ_API_KEY` is valid at [console.groq.com](https://console.groq.com)
- Check API rate limits — Groq has usage tiers
- Ensure the `Qwen3-27B` model is available in your Groq account

</details>

<details>
<summary><b>🔴 Frontend can't connect to backend</b></summary>

- Verify `VITE_API_URL` in the frontend `.env` matches the backend URL
- Check CORS settings — `FRONTEND_URL` in backend `.env` must match the frontend origin
- Ensure the backend is running before starting the frontend

</details>

<details>
<summary><b>🔴 JWT authentication issues</b></summary>

- Clear the browser's local storage and re-login
- Verify `SECRET_KEY` hasn't changed between sessions
- Check that `Authorization: Bearer <token>` header is being sent

</details>

---

## 💬 FAQ

<details>
<summary><b>Is this a real e-commerce platform?</b></summary>

No. Ziya is a **portfolio project** designed to demonstrate backend engineering and Agentic AI integration. It uses sample product data to showcase the technical implementation.

</details>

<details>
<summary><b>Why Groq instead of OpenAI?</b></summary>

Groq provides significantly faster inference with its custom LPU hardware, making conversations feel more responsive. The Qwen3-27B model offers strong reasoning suitable for tool-calling workflows.

</details>

<details>
<summary><b>Can I use a different LLM?</b></summary>

Yes. The AI layer is modular. Swap Groq for OpenAI, Anthropic, or any LangChain-compatible LLM by updating the model configuration in `ziya/agent.py`.

</details>

<details>
<summary><b>Why LangGraph instead of a simple LangChain agent?</b></summary>

LangGraph provides stateful execution, conversation memory, and deterministic workflow control — essential for a production-grade assistant that must handle multi-turn conversations reliably.

</details>

<details>
<summary><b>Can I add more products?</b></summary>

Yes. Add products directly to the MySQL database or modify the seed scripts in `app/seed_data/`. The AI agent will automatically discover and recommend new products.

</details>

---

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### 📌 Guidelines

- Follow existing code style and project structure
- Write descriptive commit messages
- Update documentation for new features
- Test your changes thoroughly before submitting
- One feature per pull request

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

---

## Acknowledgments

- [**FastAPI**](https://fastapi.tiangolo.com/) — Modern, fast web framework for building APIs
- [**LangChain**](https://www.langchain.com/) — Framework for LLM-powered applications
- [**LangGraph**](https://langchain-ai.github.io/langgraph/) — Stateful agent orchestration
- [**Groq**](https://groq.com/) — High-speed LLM inference
- [**SQLAlchemy**](https://www.sqlalchemy.org/) — Python SQL toolkit and ORM
- [**React**](https://react.dev/) — UI component library
- [**Render**](https://render.com/) — Cloud application hosting
- [**Vercel**](https://vercel.com/) — Frontend deployment platform

---

## 👨‍💻 Author

<div align="center">

**Rajesh R** — Backend Developer · AI Engineer

[![GitHub](https://img.shields.io/badge/GitHub-RajeshR005-181717?style=for-the-badge&logo=github)](https://github.com/RajeshR005)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/rajeshradha)

⭐ **If you found this project useful, please consider giving it a star!**

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:3B82F6,100:06B6D4&height=120&section=footer" width="100%" />
