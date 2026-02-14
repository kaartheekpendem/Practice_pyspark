from datetime import datetime

def log_request(endpoint: str, method: str, payload: dict):
    timestamp = datetime.utcnow().isoformat()
    print(f"[AUDIT] {timestamp} | {method} {endpoint} | Payload: {payload}")