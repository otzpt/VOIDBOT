import os
import sys
from dotenv import load_dotenv

def init_environment():
    """
    Automates the environment setup by creating a template .env
    file if it doesn't exist, and loads the secure tokens.
    """
    env_file = ".env"

    # If env doesn't exist, create a baseline template automatically
    if not os.path.exists(env_file):
        print(f"{env_file} not found. Creating a clean template for you...")
        with open(env_file, "w") as f:
            f.write("SLACK_BOT_TOKEN=---\n")
            f.write("SLACK_SIGNING_SECRET=---\n")
        print(f"Template created. Please add your real tokens inside {env_file}.")
        sys.exit(0)

    # Load the variables from the file
    load_dotenv()

    bot_token = os.environ.get("SLACK_BOT_TOKEN")
    signing_secret = os.environ.get("SLACK_SIGNING_SECRET")

    # Fail-safe check
    if not bot_token or "---" in bot_token or not signing_secret or "---" in signing_secret:
        print("Error: Missing or invalid Slack tokens inside your .env file!")
        print("Please replace the template strings with your real keys from api.slack.com")
        sys.exit(1)

    return bot_token, signing_secret
  