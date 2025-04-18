import os
import logging


logs_filepath = os.path.join("logs", "running_logs.log")
os.makedirs(os.path.dirname(logs_filepath), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] : %(levelname)s : %(module)s : %(message)s",
    handlers=[logging.FileHandler(logs_filepath), logging.StreamHandler()],
)

logger = logging.getLogger(name="cnnClassifier")
