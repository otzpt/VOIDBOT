import os
from slack_bolt import App
from dotenv import load_dotenv

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNIN_SECRET")
)

@app.command("/ping")
def handle_ping(ack, say):
    ack()
    say("Conection succesfull! VOIDBOT is active.")

if __name__ == "__main__":
    app.start(port=3000)