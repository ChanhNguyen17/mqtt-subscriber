# MQTT subscriber

This project is a Python application that subscribes to an MQTT topic, logs the received messages, and stores them in a MongoDB database. It also provides a FastAPI-based REST API endpoint to retrieve these messages. The entire application is containerized using Docker for easy deployment.

## Project Structure

The project has the following directory structure:

```plaintext
mqtt_subscriber/
├── fastapi/
│   ├── Dockerfile
│   ├── fastapi_app.py
│   ├── mongo_client.py
│   └── requirements.txt
├── mqtt_sub/
│   ├── Dockerfile
│   ├── mqtt_subscriber.py
│   ├── mongo_client.py
│   └── requirements.txt
└── docker-compose.yml
```

## Setup

1. Clone this repository.
```bash
git clone https://github.com/ChanhNguyen17/mqtt-subscriber.git
```
2. Navigate to the project directory.
```bash
cd mqtt-subscriber/
```
3. Build and start the containers using Docker Compose.
```bash
docker-compose up -d
```

## MQTT Subscriber

The MQTT subscriber connects to an MQTT broker and subscribes to a specific topic. It logs received messages, including the payload and timestamp. Messages are then sent to the MongoDB database.

## FastAPI Application

The FastAPI application provides a REST API endpoint to retrieve messages stored in the MongoDB database. You can access the FastAPI application through its URL. API documentation is available at a specific URL.

## Dockerization

Both the MQTT subscriber and FastAPI application are containerized using Docker. The `docker-compose.yml` file defines the services, including an MQTT broker and a MongoDB database.

## Usage

- Access the FastAPI application at http://localhost:8008/
- Use the provided REST API endpoint to retrieve stored messages.

### Endpoints

- GET `/messages`: Retrieve all stored messages.

## Stopping the Containers

To stop and remove the containers, follow the provided instructions.

```bash
docker-compose down
```
