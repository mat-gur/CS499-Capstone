import win32com.client
print("Imports successful")

# Function to list all USB storage devices, if connected.
def list_all_usb_devices():
    try:
        wmi = win32com.client.GetObject("winmgmts:") # Connects to Windows Management Instrumentation
        logical_disks = wmi.ExecQuery("SELECT * FROM Win32_LogicalDisk")  # Get logical disks on the system

        usb_devices = []
        for disk in logical_disks:
            # Check if it's a removable or local disk (DriveType: 2 = Removable, 3 = Local)
            if disk.DriveType in [2, 3]:
                device_id = disk.DeviceID
                volume_name = disk.VolumeName or "Unknown Volume"
                file_system = disk.FileSystem or "Unknown FS"
                size = round(int(disk.Size) / (1024 ** 3), 2) if disk.Size else "N/A"
                free_space = round(int(disk.FreeSpace) / (1024 ** 3), 2) if disk.FreeSpace else "N/A"

                #Heuristic check for USB-like drives based on volume name or known drive letter.
                is_usb_like = (
                        "usb" in volume_name.lower()
                        or "extreme" in volume_name.lower()
                        or device_id == "E:" # Adjust as needed for known USB drive letters
                )

                if disk.DriveType == 2 or is_usb_like:
                    usb_devices.append(
                        f"Drive: {device_id}, Volume: {volume_name}, FS: {file_system}, "
                        f"Size: {size} GB, Free: {free_space} GB"
                    )

        return usb_devices
    except Exception as e:
        return [f"USB Scan Error: {e}"]

# --- Legacy function retained for reference (was used in pre-enhancement version of the app) ---
#def get_malwarebytes_version():
#    try:
#        file_path = r"C:\ProgramData\Malwarebytes\MBAMService\version.dat"
#        with open(file_path, "r") as file:
#            data = file.readlines()
#        return "\n".join(data).strip()  # Convert list to string
#    except Exception as e:
#       return f"Error: {e}"


# Standalone test: Run USB listing directly if file is executed on its own
if __name__ == "__main__":
    usb_devices = list_all_usb_devices()
    if usb_devices:
        print("Connected USB Devices:")
        for device in usb_devices:
            print(f"- {device}")
    else:
        print("No USB devices found.")
