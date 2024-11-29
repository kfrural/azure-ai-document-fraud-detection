import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler("data/logs/system.log"), logging.StreamHandler()]
    )
    return logging.getLogger()

if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Sistema iniciado com sucesso.")
