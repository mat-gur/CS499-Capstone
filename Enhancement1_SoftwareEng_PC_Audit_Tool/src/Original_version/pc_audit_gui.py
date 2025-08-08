# pc_audit_gui.py
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk  # For creating tabs
from pc_audit import list_all_usb_devices, get_malwarebytes_version
import subprocess

def open_control_panel():
    subprocess.run("control", shell=True)

def open_system_info():
    subprocess.run("msinfo32", shell=True)

def open_computer_management():
    subprocess.run("compmgmt.msc", shell=True)

def open_event_logs():
    subprocess.run("eventvwr", shell=True)

def open_malwarebytes():
    try:
        subprocess.run(r'"C:\Program Files\Malwarebytes\Anti-Malware\Malwarebytes.exe"', shell=True)
    except FileNotFoundError:
        messagebox.showerror("Error", "Malwarebytes.exe not found! Please check the installation path.")



class PCAuditApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.on_check_antivirus = None
        self.title("PC Audit Tool")
        self.geometry("600x600")  # Set the window size
        self.create_tabs()

    def create_tabs(self):
        # Create a Notebook widget for tabs
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Welcome/Shortcuts tab
        welcome_tab = tk.Frame(notebook)
        notebook.add(welcome_tab, text="Welcome/Shortcuts")
        self.create_welcome_shortcuts_tab(welcome_tab, notebook)

        # Create USB tab
        usb_tab = tk.Frame(notebook)
        notebook.add(usb_tab, text="USB Info")
        self.create_usb_tab(usb_tab)

        # Create Antivirus tab
        antivirus_tab = tk.Frame(notebook)
        notebook.add(antivirus_tab, text="Antivirus Info")
        self.create_antivirus_tab(antivirus_tab)

        # Create Networking tab
        networking_tab = ttk.Frame(notebook)
        notebook.add(networking_tab, text="Networking")
        self.create_networking_tab(networking_tab)

    def create_welcome_shortcuts_tab(self, tab, notebook):
        # Welcome message
        tk.Label(tab, text="Welcome to the PC Audit Tool!", font=("Arial", 16, "bold")).pack(pady=20)
        tk.Label(tab, text="Explore your system or access useful tools below.", font=("Arial", 12)).pack(pady=10)

        # Navigation buttons to other tabs
        tk.Button(tab, text="Go to USB Info", command=lambda: notebook.select(1)).pack(pady=5)
        tk.Button(tab, text="Go to Antivirus Info", command=lambda: notebook.select(2)).pack(pady=5)

        # Separator
        tk.Label(tab, text="---------------------------------", font=("Arial", 10)).pack(pady=10)

        # System shortcuts
        tk.Label(tab, text="System Shortcuts", font=("Arial", 14)).pack(pady=10)

        tk.Button(tab, text="Control Panel", command=open_control_panel).pack(pady=5)
        tk.Button(tab, text="System Information", command=open_system_info).pack(pady=5)
        tk.Button(tab, text="Computer Management", command=open_computer_management).pack(pady=5)
        tk.Button(tab, text="Event Logs", command=open_event_logs).pack(pady=5)
        tk.Button(tab, text="Open Malwarebytes", command=open_malwarebytes).pack(pady=5)


    def create_usb_tab(self, tab):
        # Add a button and output area for USB info
        btn_usb = tk.Button(tab, text="List USB Devices", command=self.on_list_usb_devices)
        btn_usb.pack(pady=10)

        self.usb_output = scrolledtext.ScrolledText(tab, wrap=tk.WORD, height=15)
        self.usb_output.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def create_antivirus_tab(self, tab):
        # Button to check Malwarebytes version
        btn_antivirus = tk.Button(tab, text="Check Malwarebytes Info", command=self.on_check_malwarebytes)
        btn_antivirus.pack(pady=10)

        # Output box to display results
        self.antivirus_output = scrolledtext.ScrolledText(tab, wrap=tk.WORD, height=10)
        self.antivirus_output.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def on_check_malwarebytes(self):
        raw_data = get_malwarebytes_version().strip()  # Get and clean data
        print(f"Raw Data from File:\n{raw_data}")  # Debugging Step

        result = [line for line in raw_data.split("\n") if line.strip()]  # Remove empty lines
        print(f"Filtered Data: {result}")  # Debugging Step

        # Ensure all values are captured, defaulting to "N/A" if missing
        version = result[0] if len(result) > 0 else "N/A"
        update_date = result[1] if len(result) > 1 else "N/A"
        last_update_time = result[2] if len(result) > 2 else "N/A"

        formatted_output = (
            f"Malwarebytes Version: {version}\n"
            f"Update Date: {update_date}\n"
            f"Last Update Time: {last_update_time}"
        )

        self.antivirus_output.delete('1.0', tk.END)
        self.antivirus_output.insert(tk.END, formatted_output)

    def on_list_usb_devices(self):
        usb_devices = list_all_usb_devices()
        self.usb_output.delete('1.0', tk.END)  # Clear existing text
        self.usb_output.insert(tk.END, "Connected USB Devices:\n")
        for device in usb_devices:
            self.usb_output.insert(tk.END, f"- {device}\n")


    def create_networking_tab(self, tab):
        # Label for the input field
        tk.Label(tab, text="Enter the address or IP to ping (e.g., www.google.com or 127.0.0.1):").pack(pady=10)

        # Entry widget for IP address or URL
        self.ping_entry = tk.Entry(tab, width=30)
        self.ping_entry.pack(pady=10)

        # Buttons to run networking commands
        btn_ipconfig = tk.Button(tab, text="Run ipconfig", command=self.run_ipconfig)
        btn_ipconfig.pack(pady=10)

        btn_ping = tk.Button(tab, text="Run Ping", command=self.run_ping)
        btn_ping.pack(pady=10)

        # Output text area
        self.networking_output = scrolledtext.ScrolledText(tab, wrap=tk.WORD, height=15)
        self.networking_output.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Function to run ipconfig
    def run_ipconfig(self):
        output = subprocess.run("ipconfig", capture_output=True, text=True, shell=True)
        self.networking_output.delete('1.0', tk.END)  # Clear existing text
        self.networking_output.insert(tk.END, output.stdout)

        # Function to run ping

        # Function to run ping with custom address

    def run_ping(self):
        target = self.ping_entry.get()  # Get the address from the entry widget
        if not target:
            messagebox.showerror("Error", "Please enter a valid address or IP to ping.")
            return
        output = subprocess.run(f"ping {target}", capture_output=True, text=True, shell=True)
        self.networking_output.delete('1.0', tk.END)  # Clear existing text
        self.networking_output.insert(tk.END, output.stdout)

if __name__ == "__main__":
    app = PCAuditApp()
    app.mainloop()
