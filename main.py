import multiprocessing
from mqtt_subscriber import run_mqtt_subscriber
from fastapi_app import create_app
from uvicorn import run


if __name__ == "__main__":
    # Create a separate proces for MQTT subscriber
    mqtt_process = multiprocessing.Process(target=run_mqtt_subscriber)

    # Start the MQTT process
    mqtt_process.start()

    # Create the FastAPI app
    app = create_app()

    # Run the FastAPI app using Uvicorn
    run(app)
