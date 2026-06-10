import os
import sys
from dotenv import load_dotenv

def init_environment():
    bot_token = os.environ.get("SLACK_BOT_TOKEN")
    signing_secret = os.environ.get("SLACK_SIGNING_SECRET")

    if bot_token and signing_secret and "---" not in bot_token and "---" not in signing_secret:
        return bot_token, signing_secret

    env_file = ".env"
    if not os.path.exists(env_file):
        with open(env_file, "w") as f:
            f.write("SLACK_BOT_TOKEN=---\n")
            f.write("SLACK_SIGNING_SECRET=---\n")
            f.write("SLACK_APP_TOKEN=---\n")
        sys.exit(0)

    load_dotenv()
    bot_token = os.environ.get("SLACK_BOT_TOKEN")
    signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
    
    if not bot_token or "---" in bot_token or not signing_secret or "---" in signing_secret:
        sys.exit(1)

    return bot_token, signing_secret
