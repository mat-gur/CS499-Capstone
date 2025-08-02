# logger_utils.py

import datetime

def log_event(action_type, details=""):
    """
    Appends a timestamped log entry to the audit log file.

    Parameters:
        action_type (str): The type of action or event being logged.
        details (str): Optional additional details about the event.
    """


    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {action_type}: {details}\n"
    with open("audit_log.txt", "a") as log_file:
        log_file.write(log_entry)

def read_logs():
    """
    Reads the contents of the audit log file.

    returns:
        str: All log entries or a default if no logs are available.
    """

    try:
        with open("audit_log.txt", "r") as log_file:
            return log_file.read()
    except FileNotFoundError:
        return "No logs available yet."