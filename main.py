import os
from slack_bolt import App
from dotenv import load_dotenv
from config import init_environment
from logger import log_activity

# Automatically run the automation check
BOT_TOKEN, SIGNING_SECRET = init_environment()

app = App(
    token=BOT_TOKEN,
    signing_secret=SIGNING_SECRET
)

@app.command("/ping")
def handle_ping(ack, body, say): 
    ack()
    user = body.get("user_id")    
    log_activity("/ping", user)   
    say("Connection successful! VOIDBOT is active.")

@app.command("/about")
def handle_about(ack, body, say): 
    ack()
    user = body.get("user_id")
    log_activity("/about", user)
    say(
        "Hello, Im VOIDBOT\n"
        "I was created by @otzpt/otzpt_dev, I'm his first slackbot project\n"
        "I'm being programmed in Python!!"
    )

@app.command("/voidtune")
def handle_voidtune(ack, body, say):
    user = body.get("user_id")
    log_activity("/voidtune", user)
    say(
        "Advanced VOIDTUNE Module\n"
        "Current Status: Listening for OS diagnostic flags.\n"
        "Planned actions:\n"
        "'--debloat` : Strips telemetry and stops unnecessary background processes.\n"
        "`--ram` : Triggers real-time memory cleanup routines.\n"
        "`--fps` : Toggles gaming performance profile tweaks.\n"
        "Run with caution inside your Linux/Windows environment!"
    )

if __name__ == "__main__":
    app.start(port=3000)
