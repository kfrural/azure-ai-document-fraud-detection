import os
from datetime import datetime

def log_alert(message):
    log_file = "data/logs/alerts.log"
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    with open(log_file, "a") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"{timestamp} - {message}\n")
        print(f"Alerta registrado: {message}")

if __name__ == "__main__":
    log_alert("Fraude detectada no documento ID 12345.")
