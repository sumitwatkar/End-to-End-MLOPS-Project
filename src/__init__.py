import os
import sys
import logging

# Define a logging format for various information
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory where log files will be stored
log_dir = "logs"

# Create a file path for the log file within the specified directory
log_filepath = os.path.join(log_dir,"running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger instance with the name "fraud_logs"
logger = logging.getLogger("fraud_logs")