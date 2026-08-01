from loguru import logger

# Save logs to a file: a new file is created every time it reaches 10 MB,
# and logs older than 5 days are automatically removed (compressed as .zip)
logger.add("logs.log", rotation="10 MB", retention="5 days", compression="zip")


def start_system():
    logger.info("Starting system... socket check complete.")

    try:
        # Example check: simulated RAM speed reading
        ram_speed = 3200

        logger.debug(f"Detected RAM speed: {ram_speed} MHz")

        if ram_speed <= 3200:
            logger.warning("RAM speed is at or below the expected threshold!")

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    logger.success("System active!")
    start_system()
