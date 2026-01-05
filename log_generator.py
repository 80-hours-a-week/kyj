from datetime import datetime
from typing import Iterable

def log_stream(events: Iterable[str]):
    for e in events:
        timestamp = datetime.now().strftime("%H:%M:%S")
        yield f"[{timestamp}] {e}"