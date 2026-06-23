# VOIDBOT

A custom Slack bot built with Python using Socket Mode. Created during Hack Club Stardance as my first project in bot development and server automation.

Try it out in the [#voidbot-demo](https://hackclub.slack.com/archives/C0BCLB8NS12) channel on the Hack Club Slack.

## Commands

| Command | Description |
|---------|-------------|
| `/vt-ping` | Health check — confirms the bot is online |
| `/vt-about` | Info about VOIDBOT and its creator |
| `/vt-voidtune` | Displays the VOIDTUNE module status and planned CLI flags |

## How to run

```bash
git clone https://github.com/otzpt/VOIDBOT
cd VOIDBOT
pip install -r requirements.txt
```

Create a `.env` file:
SLACK_BOT_TOKEN=xoxb-...

SLACK_APP_TOKEN=xapp-...

Then run:
```bash
python main.py
```

## Tech stack

- Python 3
- [slack-bolt](https://github.com/slackapi/bolt-python) — Slack app framework
- Socket Mode — no public URL required
- Hosted on Hack Club Nest (24/7 Linux container)

## Challenges

The biggest challenge was hosting. VOIDBOT uses Socket Mode which doesn't expose an HTTP port, but Hugging Face Spaces (original host) expects a web server to be running. I solved this by running a lightweight HTTP health-check thread alongside the bot's WebSocket connection. Later migrated to Hack Club Nest for a permanent solution.

## What I learned

- How Slack bots work (Socket Mode vs HTTP)
- How to handle slash commands with slack-bolt
- How to keep a process running 24/7 on a Linux server using tmux
- SSH key generation and remote server setup
