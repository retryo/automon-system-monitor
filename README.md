# AutoMon - System Performance Dashboard

AutoMon is a lightweight Flask web app that monitors system performance (CPU, memory, and disk)
in real time. It’s containerized with Docker and ready for deployment on AWS or any cloud platform.

## Features
- Real-time system monitoring via Flask and Chart.js
- Dockerized for simple deployment
- AWS EC2/ECS ready

## Run Locally
```bash
docker build -t automon .
docker run -p 8080:5000 automon
