import logging

def setup_logger():
    # Create a custom logger
    logger = logging.getLogger('weatherAppLogger')

    # Set the lowest-severity log message to be handled (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('weather_app.log')

    # Set logging level for handlers
    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.ERROR)

    # Create formatters and add it to handlers
    console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger