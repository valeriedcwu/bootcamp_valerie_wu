import os
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

load_dotenv()



