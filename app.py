import src.ui.xcerpt_ui as xcerpt_ui

def main():
    print("🚀 Starting Xcerpt...")

    ui = xcerpt_ui.XcerptUI()
    ui.launch_login_screen()
    # This will eventually initialize your app:
    # - Load config
    # - Launch UI (login screen)
    # - Connect to APIs

if __name__ == "__main__":
    main()