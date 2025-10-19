# HGN-track-0-backend
A simple RESTful API endpoint that returns your profile information along with a dynamic cat fact fetched from an external API. This task validates my ability to consume third-party APIs, format JSON responses, and return dynamic data.


## Features

*   **GET /me Endpoint**: Returns a JSON response containing user details and a random cat fact.
*   **Dynamic Cat Fact**: Integrates with the [Cat Facts API](https://catfact.ninja/) to fetch a new cat fact on each request.
*   **Real-time Timestamp**: Provides the current UTC time in ISO 8601 format.
*   **Environment Variable Configuration**: Allows easy customization of user details and API settings.
*   **Basic Error Handling**: Gracefully handles failures when fetching cat facts from the external API.

## Requirements

To run this application, you will need:

*   Python 3.8+
*   `pip` (Python package installer)

## Local Setup Instructions

Follow these steps to set up and run the application locally:

1.  **Clone the repository** (if applicable, or create the files):

    ```bash
    # If you have a git repository
    git clone <your-repo-link>
    cd <your-repo-name>
    ```

    Otherwise, ensure you have `app.py` and `requirements.txt` in the same directory.

2.  **Create a virtual environment** (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set environment variables**:

    The application uses environment variables for user details and API configuration. You can set them directly in your terminal or create a `.env` file (and use a library like `python-dotenv` if you prefer, though not included in this basic setup).

    ```bash
    export USER_EMAIL="emmanuelbinen@outlook.com"
    export USER_NAME="Emmanuel Binen"
    export USER_STACK="Python/Flask"
    export CAT_FACT_API_URL="https://catfact.ninja/fact" # Optional, default is provided
    export CAT_FACT_API_TIMEOUT="5" # Optional, default is 5 seconds
    ```

    **Note**: Replace `your.email@example.com`, `Your Full Name`, and `Python/Flask` with your actual information.

5.  **Run the Flask application**:

    ```bash
    python app.py
    ```

    The API will start running on `http://127.0.0.1:5000` (or `http://localhost:5000`).

## API Endpoint

### `GET /me`

Returns your profile information and a random cat fact.

**URL**: `/me`
on my sie it is:

http://127.0.0.1:5000/me.

**Method**: `GET`

**Response (JSON)**:

```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Full Name",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-20T10:30:00.123Z",
  "fact": "Cats can jump up to six times their height."
}
```

## Error Handling

If the Cat Facts API is unreachable or returns an error, the `fact` field in the response will indicate "Failed to fetch cat fact." The API will still return a `200 OK` status for the `/me` endpoint, as the profile information is still valid.

## Dependencies

*   **Flask**: A micro web framework for Python.
*   **Requests**: An elegant and simple HTTP library for Python.

These are listed in `requirements.txt`.

## Testing the Endpoint

You can test the endpoint using `curl` or by visiting it in your web browser:

```bash
curl http://localhost:5000/me
```

Each request should return a new cat fact and an updated timestamp.

## Deployment Notes

This basic setup is suitable for local development.