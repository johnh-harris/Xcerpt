import customtkinter as ctk
import webbrowser


class XcerptUI:
    def __init__(self):
        print("🎨 Initializing Xcerpt UI...")


    def launch_login_screen(self):
        print("🔐 Launching login screen...")
        self.root = ctk.CTk()
        self.root.title("Xcerpt Login")

        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label = ctk.CTkLabel(master=self.frame, text="Welcome to Xcerpt! Please log in.")
        self.label.pack(pady=12, padx=10)

        self.username_entry = ctk.CTkEntry(master=self.frame, placeholder_text="OpenAI API Key")
        self.username_entry.pack(pady=12, padx=10)

        self.password_entry = ctk.CTkEntry(master=self.frame, placeholder_text="X API Key", show="*")
        self.password_entry.pack(pady=12, padx=10)
        
        self.x_button = ctk.CTkButton(master=self.frame, text="Signin with X", command=self.handle_login)
        self.x_button.pack(pady=12, padx=10)

        self.login_button = ctk.CTkButton(master=self.frame, text="Enter Dashboard", command=self.handle_login)
        self.login_button.pack(pady=12, padx=10)

        self.root.mainloop()

    def handle_login(self):
        # TODO: Implement actual login logic and change text OpenAI API key and X API key
        # username = self.username_entry.get()
        # password = self.password_entry.get()
        print(f"👤 Attempting login for user: {username}")
        # Here you would add authentication logic
        # For now, just open a web page as a placeholder
        ''' 
        goes to this URL 
        
        https://twitter.com/i/oauth2/authorize
    ?response_type=code
    &client_id=YOUR_CLIENT_ID
    &redirect_uri=YOUR_REDIRECT_URI
    &scope=tweet.read%20users.read%20offline.access
    &state=RANDOM_STRING
    &code_challenge=CHALLENGE_VALUE
    &code_challenge_method=S256

        '''
        webbrowser.open("https://example.com/login_success")