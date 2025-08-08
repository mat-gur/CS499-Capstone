# system_utils.py

from tkinter import messagebox
import subprocess
import os

def open_control_panel():
    """Opens the control panel"""
    subprocess.Popen("control", shell=True)

def open_system_info():
    """Opens Windows System Information window"""
    subprocess.Popen("msinfo32", shell=True)

def open_computer_management():
    """Opens the Computer Management console"""
    subprocess.Popen("compmgmt.msc", shell=True)

def open_event_logs():
    """Opens the Event Viewer"""
    subprocess.Popen("eventvwr", shell=True)

def run_ipconfig():
    """
    Runs 'ipconfig /all' and returns the result

    returns:
        str: Output of the ipconfig command or error message.
    """
    try:
        output = subprocess.check_output("ipconfig", shell=True, text=True)
        return True, output
    except subprocess.CalledProcessError as e:
        return False, str(e)

def run_ping(target: str, count: int = 4):
    """
       Pings a specified target and returns the result.

       Parameters:
           target (str): Hostname or IP address to ping.
           count (int): Number of ping attempts.

       Returns:
           tuple: (bool success, str output)
       """
    try:
        command = f"ping -n {count} {target}"
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=True,
            timeout=10
        )
        output = completed.stdout or completed.stderr
        success = completed.returncode == 0
        return success, output
    except Exception as e:
        return False, f"Ping error: {e}"

def open_malwarebytes():
    """
        Attempts to open Malwarebytes if it is installed.

        Displays an error message if the executable is not found.
        """
    try:
        subprocess.run(r'"C:\Program Files\Malwarebytes\Anti-Malware\Malwarebytes.exe"', shell=True)
    except FileNotFoundError:
        messagebox.showerror("Error", "Malwarebytes.exe not found! Please check the installation path.")

def get_antivirus_info():
    """
        Attempts to detect Malwarebytes and return its version details.

        Returns:
            str: Malwarebytes info or fallback message if not found.
        """
    try:
        # Check for Malwarebytes version file
        malwarebytes_path = r"C:\ProgramData\Malwarebytes\MBAMService\version.dat"
        if os.path.exists(malwarebytes_path):
            with open(malwarebytes_path, "r") as file:
                data = file.readlines()
            return "Malwarebytes Detected:\n" + "".join(data).strip()
        else:
            return "Malwarebytes not found.\nChecking built-in Windows Defender..."

        # Optional: Add Windows Defender fallback parsing from registry or security center
    except Exception as e:
        return f"Error retrieving antivirus info: {e}"