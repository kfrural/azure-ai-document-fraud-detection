import logging
from datetime import datetime

logging.basicConfig(
    filename="data/logs/alerts.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_alert(message):
    logging.info(f"Alerta: {message}")

if __name__ == "__main__":
    log_alert("Fraude detectada no documento ID 12345.")
