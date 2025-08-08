import win32com.client
print("Imports successful")

def list_all_usb_devices():
    usb_devices = []
    wmi = win32com.client.GetObject("winmgmts:")

    # Get all USB hubs (for port info)
    usb_hubs = wmi.InstancesOf("Win32_USBHub")
    logical_disks = wmi.InstancesOf("Win32_LogicalDisk")  # For getting drive letter

    # Iterate over all PnP devices
    for device in wmi.InstancesOf("Win32_PnPEntity"):
        if device.Name and "USB" in device.Name:
            description = device.Description if device.Description else "Unknown Description"
            location = device.PNPDeviceID if device.PNPDeviceID else "Unknown Location"

            # Try to match device location to hub/port
            port = "Unknown Port"
            for hub in usb_hubs:
                if hub.PNPDeviceID in location:
                    port = hub.DeviceID  # Hub's DeviceID can help us identify the port

            # Check if the device is a storage device and assign drive letter if available
            drive_letter = "No Drive Letter"
            for disk in logical_disks:
                if disk.PNPDeviceID and device.PNPDeviceID in disk.PNPDeviceID:
                    drive_letter = disk.DeviceID  # This provides the drive letter (e.g., C:, D:)

            usb_devices.append(f"Device: {description}, Location: {location}, Port: {port}, Drive: {drive_letter}")

    return usb_devices

import os
def get_malwarebytes_version():
    try:
        file_path = r"C:\ProgramData\Malwarebytes\MBAMService\version.dat"
        with open(file_path, "r") as file:
            data = file.readlines()
        return "\n".join(data).strip()  # Convert list to string
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    # Get USB devices
    usb_devices = list_all_usb_devices()
    if usb_devices:
        print("Connected USB Devices:")
        for device in usb_devices:
            print(f"- {device}")
    else:
        print("No USB devices found.")
