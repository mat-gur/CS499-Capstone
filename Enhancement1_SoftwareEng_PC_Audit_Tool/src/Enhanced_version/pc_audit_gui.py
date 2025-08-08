# pc_audit_gui.py
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk  # For creating tabs
from pc_audit import list_all_usb_devices
from logger_utils import log_event, read_logs
import system_utils
from system_utils import get_antivirus_info

class PCAuditApp(tk.Tk):
    """Main GUI application for the PC Audit Tool."""

    def __init__(self):
        super().__init__()
        self.status_labels = None
        self.usb_output = None
        self.antivirus_output = None
        self.ping_entry = None
        self.networking_output = None
        self.logs_output = None
        self.title("PC Audit Tool")
        self.geometry("700x675")  # Set the window size
        self.icons = self.load_icons() # Loads icons
        self.create_tabs()

    def load_icons(self):
        """Loads icons used in the Welcome tab for visual enhancement"""
        icons = {}
        try:
            icons["control"] = tk.PhotoImage(file="icons/icons8-control-panel-48.png")
            icons["information"] = tk.PhotoImage(file="icons/icons8-information-40.png")
            icons["event"] = tk.PhotoImage(file="icons/icons8-event-log-48.png")
            icons["management"] = tk.PhotoImage(file="icons/icons8-management-48.png")
            icons["antivirus"] = tk.PhotoImage(file="icons/icons8-windows-defender-48.png")
        except Exception as e:
            print(f"Error loading icons: {e}")
        return icons


    def create_tabs(self):
        """Creates all the tabs in the main interface"""
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Welcome/Shortcuts tab
        welcome_tab = tk.Frame(notebook)
        notebook.add(welcome_tab, text="Welcome/Shortcuts")
        self.create_welcome_shortcuts_tab(welcome_tab)

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

        logs_tab = tk.Frame(notebook)
        notebook.add(logs_tab, text="Logs")
        self.create_logs_tab(logs_tab)

    def create_welcome_shortcuts_tab(self, tab):
        """Creates the Welcome tab with shortcuts and audit checklist"""
        tk.Label(tab, text="Welcome to the PC Audit Tool!", font=("Arial", 16, "bold")).pack(pady=20)
        tk.Label(tab, text="Explore your system or access useful tools below.", font=("Arial", 12)).pack(pady=10)

        # Checklist Status Section
        tk.Label(tab, text="System Audit Checklist", font=("Arial", 14, "bold")).pack(pady=10)

        self.status_labels = {
            "usb": tk.Label(tab, text="USB Info: ❌ Not Checked", font=("Arial", 11), fg="red"),
            "av": tk.Label(tab, text="Malwarebytes Info: ❌ Not Checked", font=("Arial", 11), fg="red"),
            "ping": tk.Label(tab, text="Ping: ❌ Not Run", font=("Arial", 11), fg="red")
        }

        self.status_labels["usb"].pack()
        self.status_labels["av"].pack()
        self.status_labels["ping"].pack()

        # Separator
        tk.Label(tab, text="---------------------------------", font=("Arial", 10)).pack(pady=10)

        # System shortcuts
        tk.Label(tab, text="System Shortcuts", font=("Arial", 14)).pack(pady=10)

        tk.Button(tab,image=self.icons["control"],text="Control Panel",compound="left",command=system_utils.open_control_panel).pack(pady=5)
        tk.Button(tab,image=self.icons["information"],text="System Info",compound="left",command=system_utils.open_system_info).pack(pady=5)
        tk.Button(tab, image=self.icons["management"], text="Computer Management", compound="left", command=system_utils.open_computer_management).pack(pady=5)
        tk.Button(tab,image=self.icons["event"],text="Event logs",compound="left",command=system_utils.open_event_logs).pack(pady=5)
        tk.Button(tab, image=self.icons["antivirus"], text="Open Malwarebytes", compound="left", command=system_utils.open_malwarebytes).pack(pady=5)

    def create_usb_tab(self, tab):
        """Creates the USB tab for listing connected USB storage devices"""
        # Add a button and output area for USB info
        btn_usb = tk.Button(tab, text="List USB Devices", command=self.on_list_usb_devices)
        btn_usb.pack(pady=10)

        self.usb_output = scrolledtext.ScrolledText(tab, wrap=tk.WORD, height=15)
        self.usb_output.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def create_antivirus_tab(self, tab):
        """Creates the Antivirus tab with a button to check AV info"""
        btn_antivirus = tk.Button(tab, text="Antivirus Info", command=self.on_check_antivirus)
        btn_antivirus.pack(pady=10)

        # Output box to display results
        self.antivirus_output = scrolledtext.ScrolledText(tab, wrap=tk.WORD, height=10)
        self.antivirus_output.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    def on_check_antivirus(self):
        """Fetch and display antivirus info from system_utils"""
        print("Antivirus button clicked")  # Debug

        try:
            info = get_antivirus_info()
            self.antivirus_output.delete('1.0', tk.END)
            self.antivirus_output.insert(tk.END, info)
            log_event("Antivirus Check", "Success")
        except Exception as e:
            messagebox.showerror("Antivirus Error", str(e))
            log_event("Antivirus Check Error", str(e))
        finally:
            self.refresh_logs()
            self.status_labels["av"].config(text="Antivirus Info: ✅ Checked", fg="green")

    def on_list_usb_devices(self):
        """List all USB storage devices and update log"""
        try:
            usb_devices = list_all_usb_devices()
            self.usb_output.delete('1.0', tk.END)
            self.usb_output.insert(tk.END, "Connected USB Devices:\n")

            if usb_devices:  # List has real devices
                for dev in usb_devices:
                    self.usb_output.insert(tk.END, f"- {dev}\n")
                log_event("USB Scan", f"{len(usb_devices)} device(s) found")
            else:  # Truly no devices
                self.usb_output.insert(tk.END, "No USB storage devices found.\n")
                log_event("USB Scan", "0 devices found")

        except Exception as e:
            messagebox.showerror("USB Scan Error", str(e))
            log_event("USB Scan Error", str(e))

        finally:
            self.refresh_logs()
            self.status_labels["usb"].config(text="USB Info: ✅ Checked", fg="green")

    def create_networking_tab(self, tab):
        """Creates the Networking tab with ping and ipconfig options."""
        tk.Label(tab, text="Enter the address or IP to ping (e.g., www.google.com or 127.0.0.1):").pack(pady=10)

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

    def create_logs_tab(self, tab):
        """Creates the logs tab to display and refresh event logs."""
        tk.Label(tab, text="Audit Log", font=("Arial", 14)).pack(pady=10)

        self.logs_output = scrolledtext.ScrolledText(tab, wrap=tk.WORD, height=20)
        self.logs_output.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        refresh_btn = tk.Button(tab, text="Refresh Logs", command=self.refresh_logs)
        refresh_btn.pack(pady=5)

        self.refresh_logs()  # Load logs on tab open

    def refresh_logs(self):
        """Refreshes the audit log text box."""
        logs = read_logs()
        self.logs_output.delete('1.0', tk.END)
        self.logs_output.insert(tk.END, logs)

    def run_ipconfig(self):
        """Runs ipconfig and displays results in the networking tab."""
        success, output = system_utils.run_ipconfig()

        # Show output in text area
        self.networking_output.delete('1.0', tk.END)
        self.networking_output.insert(tk.END, output)

        # Popup and log
        if success:
            log_event("IPConfig", "Success")
        else:
            messagebox.showerror("ipconfig error", output)
            log_event("IPConfig", f"Failure – {output}")

        self.refresh_logs()

    # Function to run ping with custom address
    def run_ping(self):
        """Runs ping on the user-entered address/IP and logs the result."""
        target = self.ping_entry.get().strip()
        if not target:
            messagebox.showerror("Error", "Please enter a valid address or IP to ping.")
            return

        success, output = system_utils.run_ping(target)

        self.networking_output.delete('1.0', tk.END)
        self.networking_output.insert(tk.END, output)

        status = "Success" if success else "Failure"
        if not success:
            messagebox.showerror("Ping Error", output)

        log_event("Ping", f"{status} – target: {target}")
        self.refresh_logs()
        self.status_labels["ping"].config(text="Ping: ✅ Completed", fg="green")

#Runs the app
if __name__ == "__main__":
    app = PCAuditApp()
    app.mainloop()
