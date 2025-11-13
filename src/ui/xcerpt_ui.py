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

        self.login_button = ctk.CTkButton(master=self.frame, text="Login", command=self.handle_login)
        self.login_button.pack(pady=12, padx=10)

        self.root.mainloop()

    def handle_login(self):
        # TODO: Implement actual login logic and change text OpenAI API key and X API key
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"👤 Attempting login for user: {username}")
        # Here you would add authentication logic
        # For now, just open a web page as a placeholder
        webbrowser.open("https://example.com/login_success")