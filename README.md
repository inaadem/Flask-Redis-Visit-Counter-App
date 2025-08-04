#  Flask + Redis Visit Counter App

## 📌 Project Overview
This project demonstrates a simple multi-container web application using **Flask**, **Redis**, **Docker**, and **Nginx**.  
It tracks the number of visits to a page and stores the count in Redis.

## Key Objectives
- 🐳 Containerize the app using Docker
- 🔄 Orchestrate services using Docker Compose
- 🌐 Reverse proxy with Nginx
- 🔢 Store visit count in Redis
- 👨‍💻 Display count using Flask & HTML templates

## 📁 Project Structure
```
visit-counter/
├── app/
│   ├── app.py
│   └── templates/
│       ├── welcome.html
│       └── count.html
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
├── .gitignore
├── README.md
```

## Containerization with Docker
Containerize the application using Docker
![Docker Compose](https://github.com/inaadem/my-visit-counter-app/blob/main/dockerfile.png?raw=true) 


## Containerization with Docker

```services:
  web:
    build: .
    expose:
      - "5002"
    depends_on:
      - redis
    environment:
      - REDIS_HOST=my-redis
      - REDIS_PORT=6379
  
  redis:
    image: redis
    hostname: my-redis
    volumes: 
      - redis-data:/data
  
  nginx:
    image: nginx:latest
    ports:
      - "5002:5002"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web

volumes:
  redis-data:
```

##  Browser – Count Page
This page displays the current visit count.
Every time the user refreshes or revisits this page, the counter increases.
Flask communicates with Redis, increments the visits key, and renders the count using count.html.

![Docker Compose](https://github.com/inaadem/my-visit-counter-app/blob/main/browser-welcome.png.png?raw=true) 

![Docker Compose](https://github.com/inaadem/my-visit-counter-app/blob/main/browser-welcome.png%20(2).png?raw=true) 

## Technologies Used:
Flask – Lightweight web server for Python

Redis – Fast key-value store to track visits

Docker – For containerizing the app

Docker Compose – For orchestrating services together

Nginx – To proxy traffic to the Flask app

HTML + Jinja2 – For dynamic UI rendering

# How to Run

### 1.Clone the repo
git clone https://github.com/yourusername/visit-counter-app.git
cd visit-counter-app

### 2.Build and run containers
```bash
docker compose up --build
```

### 3.Visit the app
Go to: http://localhost:8080
Click through to the Count Page to test Redis counter




