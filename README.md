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
![Docker Compose](https://github.com/inaadem/my-visit-counter-app/blob/main/project%20strujer.png?raw=true)

## Containerization with Docker
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
