from fastapi import FastAPI, Request, HTTPException
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Alert Logger Service",
    description="A service to receive and log disaster alerts",
    version="1.0.0"
)

# Improvements:
# - use pydantic to validate the alert data
# - add health check endpoint
# - check alert sender is allowed to send alerts
# - configure logger

@app.post("/webhook")
async def webhook(request: Request):
    try:
        alert_data = await request.json()
        print(f"Alert received: {alert_data}")
        
        # Return 200 OK
        return { "status": "success" }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing the alert"
        )

if __name__ == "__main__":
    host = os.getenv("ALERT_LOGGER_WEBHOOK_HOST", "0.0.0.0")
    port = int(os.getenv("ALERT_LOGGER_WEBHOOK_PORT", "8000"))
    print(f"Starting Alert Logger Service on {host}:{port}")
    uvicorn.run(app, host=host, port=port)
