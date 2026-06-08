import os
from datetime import datetime

def log_activity(command_name, user_id=None):
    log_file = "activity.log"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #format the log line
    if user_id:
        log_line = f"[{current_time}] SUCESS: Command '{command_name}' triggered by user {user_id}\n"
    else:
        log_line = f"[{current_time}] SUCCESS: Command '{command_name}' triggered\n"
    
    try:
        #open the file in append mode
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_line)
        print(f"logged: {log_line.strip()}")
    except Exception as e:
        print(f"Failed to write log: {e}")
