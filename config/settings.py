import os
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.getenv("BASE_URL", "https://demowebshop.tricentis.com").rstrip("/")
HEADLESS = os.getenv("HEADLESS", "false").lower() in {"1", "true", "yes"}
EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "12"))
