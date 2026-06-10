import os
import sys
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from config import init_environment
from logger import log_activity

BOT_TOKEN, SIGNING_SECRET = init_environment()

app = App(
    token=BOT_TOKEN,
    signing_secret=SIGNING_SECRET
)

@app.command("/vt-ping")
def handle_ping(ack, body, say): 
    ack()
    user = body.get("user_id")    
    log_activity("/vt-ping", user)   
    say("Connection successful! VOIDBOT is active.")

@app.command("/vt-about")
def handle_about(ack, body, say): 
    ack()
    user = body.get("user_id")
    log_activity("/vt-about", user)  
    say(
        "Hello, Im VOIDBOT\n"
        "I was created by @otzpt/otzpt_dev, I'm his first slackbot project\n"
        "I'm being programmed in Python!!"
    )

@app.command("/vt-voidtune")
def handle_voidtune(ack, body, say):
    ack()  
    user = body.get("user_id")
    log_activity("/vt-voidtune", user) 
    say(
        "Advanced VOIDTUNE Module\n"
        "Current Status: Listening for OS diagnostic flags.\n"
        "Planned actions:\n"
        "'--debloat` : Strips telemetry and stops unnecessary background processes.\n"
        "`--ram` : Triggers real-time memory cleanup routines.\n"
        "`--fps` : Toggles gaming performance profile tweaks.\n"
        "Run with caution inside your Linux/Windows environment!"
    )

def run_health_check_server():
    port = int(os.environ.get("PORT", 7860))
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Health check server online on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    try:
        print("VOIDBOT backend engine is starting in Socket Mode...")
        
        health_thread = threading.Thread(target=run_health_check_server, daemon=True)
        health_thread.start()
        
        handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
        handler.start()
    except KeyboardInterrupt:
        print("\n👋 VOIDBOT server shut down gracefully. See you soon!")
        sys.exit(0)
