from datetime import datetime
from typing import Optional, Dict, Any
import requests
import os

def check_alert_webhook_credentials():
    webhook_host = os.getenv("ALERT_LOGGER_WEBHOOK_HOST", "localhost")
    if not webhook_host:
        raise ValueError("ALERT_LOGGER_WEBHOOK_HOST is not set")

    webhook_port = os.getenv("ALERT_LOGGER_WEBHOOK_PORT", "8000")
    if not webhook_port:
        raise ValueError("ALERT_LOGGER_WEBHOOK_PORT is not set")

def notify_alert(
    alert_id: str,
    alert_timestamp: datetime,
    alert_type: str,
    message: str,
    severity: str,
    status: str,
) -> bool:
    """
    Send an alert to the webhook endpoint.
    
    Args:
        alert_id: Unique identifier for the alert
        alert_timestamp: When the alert was generated
        alert_type: Type of alert (e.g. "Flood Warning")
        message: Alert message
        severity: Alert severity level
        status: Alert status
        
    Returns:
        bool: True if alert was sent successfully, False otherwise
    """
    # Get webhook URL from environment or use default
    webhook_host = os.getenv("ALERT_LOGGER_WEBHOOK_HOST", "localhost")
    webhook_port = os.getenv("ALERT_LOGGER_WEBHOOK_PORT", "8000")
    webhook_url = f"http://{webhook_host}:{webhook_port}/webhook"
    
    # Prepare alert data
    alert_data = {
        "alert_id": alert_id,
        "timestamp": alert_timestamp.isoformat(),
        "type": alert_type,
        "message": message,
        "severity": severity,
        "status": status
    }
    
    # Send POST request to webhook
    response = requests.post(webhook_url, json=alert_data)
    
    # Check if request was successful
    if response.status_code == 200:
        print(f"Alert sent successfully: {alert_id}")
        return True
    else:
        print(f"Failed to send alert. Status code: {response.status_code}")
        return False
        
