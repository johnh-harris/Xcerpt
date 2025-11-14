import customtkinter as ctk
import webbrowser
import src.api.callback_server as callback_server
from src.api.oauth_flow import build_login_url, exchange_code_for_token

class XcerptUI:
    def __init__(self):
        print("Initializing Xcerpt UI...")


    def launch_login_screen(self):
        print("Launching login screen...")
        self.root = ctk.CTk()
        self.root.title("Xcerpt Login")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text="Welcome to Xcerpt! Please log in.")
        self.label.pack(pady=12, padx=10)

        self.username_entry = ctk.CTkEntry(master=self.frame, placeholder_text="OpenAI API Key")
        self.username_entry.pack(pady=12, padx=10)

        self.x_button = ctk.CTkButton(master=self.frame, text="Signin with X", command=self.handle_login)
        self.x_button.pack(pady=12, padx=10)

        self.login_button = ctk.CTkButton(master=self.frame, text="Enter Dashboard", command=self.handle_login)
        self.login_button.pack(pady=12, padx=10)

        self.root.mainloop()

    def handle_login(self):
        self.callback_server = callback_server.OAuthCallbackServer(port=5000)
        self.callback_server.start()

        login_url = build_login_url()

        webbrowser.open(login_url)

        code = self.callback_server.wait_for_code()
        print("Authorization Code:", code)

        access_token = exchange_code_for_token(code)