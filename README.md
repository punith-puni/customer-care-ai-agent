# AI Customer Care Agent

## Overview

AI-powered customer support chatbot that combines Large Language Models, Retrieval-Augmented Generation (RAG), sentiment analysis, and order tracking capabilities.

The system can:

* Track customer orders from PostgreSQL
* Answer policy-related questions using RAG
* Detect customer sentiment
* Escalate frustrated customers into support tickets
* Monitor tickets through an Admin Dashboard

---

## Features

### Order Tracking

Customers can ask:

```text
Where is my order #1?
```

The chatbot retrieves order details from PostgreSQL and generates a natural response.

### Policy Q&A (RAG)

Customers can ask:

```text
What is your return policy?
```

The chatbot searches company policy documents using FAISS and LangChain.

### Sentiment Detection

Detects angry customer messages such as:

```text
This is ridiculous. I've been waiting for 2 weeks.
```

Creates escalation tickets automatically.

### Admin Dashboard

Monitor:

* Total Orders
* Total Tickets
* Open Tickets
* Escalated Tickets

---

## Tech Stack

### Backend

* FastAPI
* Python
* PostgreSQL
* SQLAlchemy

### AI

* Google Gemini API
* LangChain
* FAISS

### Frontend

* React
* Tailwind CSS
* Vite

---

## Project Structure

customer-care-ai-agent/

backend/

* database/
* routes/
* services/
* rag/
* main.py

frontend/

* src/
* public/
* package.json

README.md

---

## Installation

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Sample Questions

```text
Where is my order #1?

What is your return policy?

How long does shipping take?

This is ridiculous. I've been waiting for 2 weeks.
```

---

## Future Improvements

* Redis Conversation Memory
* Authentication System
* Real-time Ticket Monitoring
* Multi-user Support
* Deployment on Railway and Vercel

---

## Author

Punith
