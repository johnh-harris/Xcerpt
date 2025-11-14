# src/api/callback_server.py

from flask import Flask, request
import threading

class OAuthCallbackServer:
    """
    A lightweight Flask server that listens for the OAuth2 callback
    and captures the authorization code from X (Twitter).
    """

    def __init__(self, port=8000):
        self.port = port
        self.app = Flask(__name__)
        self.auth_code = None
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route("/callback")
        def callback():
            """
            Handles: http://127.0.0.1:5000/callback?code=XYZ&state=123
            """
            self.auth_code = request.args.get("code")

            return (
                "<h2>Login Successful!</h2>"
                "<p>You can close this window and return to Xcerpt.</p>"
            )

    def start(self):
        """
        Start the Flask server in a background thread.
        """
        server_thread = threading.Thread(
            target=self.app.run,
            kwargs={"port": self.port, "debug": False, "use_reloader": False},
        )
        server_thread.daemon = True
        server_thread.start()

    def wait_for_code(self):
        """
        Poll until the code is received.
        """
        print("Waiting for OAuth callback from X...")

        while self.auth_code is None:
            pass  # simple blocking loop — GUI remains responsive because Flask is in another thread

        print("Authorization code received!")
        return self.auth_code