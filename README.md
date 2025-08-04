#  Flask + Redis Visit Counter App

## 📌 Project Overview
This project demonstrates a simple multi-container web application using **Flask**, **Redis**, **Docker**, and **Nginx**.  
It tracks the number of visits to a page and stores the count in Redis.

## Key Objectives
-  Containerize the app using Docker
-  Orchestrate services using Docker Compose
-  Reverse proxy with Nginx
-  Store visit count in Redis
-  Display count using Flask & HTML templates

## 📁 Project Structure
visit-counter/
│
├── app/
│ ├── app.py
│ └── templates/
│ ├── welcome.html
│ └── count.html
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
├── .gitignore
├── README.md
