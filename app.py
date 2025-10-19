import os
import requests
from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration from environment variables
USER_EMAIL = os.getenv('USER_EMAIL', 'your_email@example.com')
USER_NAME = os.getenv('USER_NAME', 'Your Name')
USER_STACK = os.getenv('USER_STACK', 'Python/Flask')
CAT_FACT_API_URL = os.getenv('CAT_FACT_API_URL', 'https://catfact.ninja/fact')
CAT_FACT_API_TIMEOUT = int(os.getenv('CAT_FACT_API_TIMEOUT', '5')) # seconds

@app.route('/me', methods=['GET'])
def get_my_profile():
    cat_fact = "Failed to fetch cat fact."
    try:
        response = requests.get(CAT_FACT_API_URL, timeout=CAT_FACT_API_TIMEOUT)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        cat_fact = response.json().get('fact', cat_fact)
    except requests.exceptions.Timeout:
        print(f"Timeout occurred while fetching cat fact from {CAT_FACT_API_URL}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cat fact from {CAT_FACT_API_URL}: {e}")
    except ValueError as e:
        print(f"Error parsing cat fact JSON: {e}")

    response_data = {
        "status": "success",
        "user": {
            "email": USER_EMAIL,
            "name": USER_NAME,
            "stack": USER_STACK
        },
        "timestamp": datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z'),
        "fact": cat_fact
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)