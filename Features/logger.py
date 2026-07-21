import logging
from pathlib import Path

log_dir = Path("data/logs")
log_dir.mkdir(parents=True, exist_ok=True)

log_file = log_dir/"organiser.log"

logger = logging.getLogger("FileOrganiser")
logger.setLevel(logging.INFO)

if not logger.handlers:

    file_handler = logging.FileHandler(log_file, mode='a')

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    def log_move(file_name, source, destination, category):
        logger.info(
        f"MOVED | File: {file_name} | Category: {category} | "
        f"From: {source} | To: {destination}"
    )


def log_duplicate(file_name, source, path):
    logger.warning(
        f"DUPLICATE | File: {file_name} |" f"From: {source} | To: {path}"
    )


def log_error(file_name, source, error):
    logger.error(
        f"ERROR | File: {file_name} | Location: {source} | Reason: {error}"
    )
