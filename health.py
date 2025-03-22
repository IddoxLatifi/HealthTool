# This script was created to execute CMD commands for system security and system information queries. 
# It contains no hidden scripts or anything similar and works 99% of the time with CMD. Python is used only for the display and interface.
# Please note that I cannot assume any liability for any damage caused. The program was tested on Windows 10 22H2 Build 19045.5608 and is only 
# applicable to the Windows operating system. 
# Creator: @apt_start_latifi
# Contact: https://iddox.tech/
# Enjoy the Programm

import os
import subprocess
from colorama import init, Fore, Back, Style

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu(options, title):
    clear_screen()
    print(Fore.LIGHTMAGENTA_EX + r"""
__          ___           _                         
\ \        / (_)         | |                        
 \ \  /\  / / _ _ __   __| | _____      _____       
  \ \/  \/ / | | '_ \ / _` |/ _ \ \ /\ / / __|      
   \  /\  /  | | | | | (_| | (_) \ V  V /\__ \      
    \/  \/   |_|_| |_|\__,_|\___/ \_/\_/ |___/      
 _    _            _ _   _       _______          _ 
| |  | |          | | | | |     |__   __|        | |
| |__| | ___  __ _| | |_| |__      | | ___   ___ | |
|  __  |/ _ \/ _` | | __| '_ \     | |/ _ \ / _ \| |
| |  | |  __/ (_| | | |_| | | |    | | (_) | (_) | |
|_|  |_|\___|\__,_|_|\__|_| |_|    |_|\___/ \___/|_|
    """)
    print(Fore.BLUE + f"{title}")
    print(Fore.BLUE + "If you have any problems or suggestions, Contact me : https://iddox.tech/")
    print(Fore.BLUE + "Select an option (1-9):")
    
    for i in range(0, len(options), 2):
        row = options[i:i+2]
        print(" | ".join(f"{Fore.LIGHTMAGENTA_EX}{i+j+1}. {option}" for j, option in enumerate(row)))
    print(Fore.BLUE + "(b) go back to menu" + Fore.RED + " | (q) quit")

def get_user_input():
    return input(Fore.GREEN + "Your choice: ").strip().lower()

def run_as_admin(command, wait=True):
    if os.name == 'nt':  
        try:
            switch = "/c" if wait else "/k"
            wait_flag = " -Wait" if wait else ""
            full_command = f"Start-Process cmd -Verb RunAs -ArgumentList '{switch} {command}'{wait_flag}"
            subprocess.run(["powershell", "-Command", full_command])
        except Exception as e:
            print(Fore.RED + f"Error executing '{command}': {e}")
    else:
        print(Fore.RED + "This script is only suitable for Windows.")

def network_info():
    commands = {
        1: ("Local IP Address", "ipconfig | findstr IPv4"),
        2: ("Public IP Address", "curl ifconfig.me"),
        3: ("MAC Address", "getmac"),
        4: ("Open Ports", "netstat -an"),
        5: ("Route", "route print"),
        6: ("DNS Cache", "ipconfig /displaydns"),
        7: ("ARP Table", "arp -a"),
        8: ("Network Adapters", "ipconfig /all")
    }
    while True:
        display_menu([cmd[0] for cmd in commands.values()], "Network Infos")
        choice = get_user_input()
        if choice == 'b':
            break
        elif choice == 'q':
            exit()
        elif choice.isdigit():
            option = int(choice)
            if option in commands:
                name, cmd = commands[option]
                print(Fore.LIGHTMAGENTA_EX + f"{name}:")
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, errors='replace')
                if option == 1:  
                    ips = [line.strip() for line in result.stdout.splitlines() if line.strip()]
                    for ip in ips:
                        print(Fore.BLUE + ip)
                    input(Fore.YELLOW + "Press Enter to continue... ")
                elif option == 2:  
                    print(Fore.BLUE + result.stdout.strip(), end=" ")
                    input(Fore.YELLOW + "Press Enter to continue...")
                elif option in (6, 8):
                    print(result.stdout)
                    input(Fore.YELLOW + "Press Enter to continue...")
                else:
                    print(Fore.BLUE + result.stdout)
                    input(Fore.YELLOW + "Press Enter to continue...")
            else:
                print(Fore.RED + "Invalid input!")
        else:
            print(Fore.RED + "Invalid input!")

def parse_wmic_output(output):
    lines = output.strip().splitlines()
    if len(lines) < 2:
        return []
    headers = lines[0].strip().split()
    data = []
    for line in lines[1:]:
        values = line.strip().split(None, len(headers) - 1)
        if len(values) == len(headers):
            data.append(dict(zip(headers, values)))
    return data

def hardware_info():
    commands = {
        1: ("GPU Info", "wmic path win32_videocontroller get name,pnpdeviceid"),
        2: ("Disk Info", "wmic diskdrive get model,serialnumber"),
        3: ("Motherboard Info", "wmic baseboard get product,serialnumber"),
        4: ("CPU Info", "wmic cpu get name,numberofcores")
    }
    while True:
        display_menu([cmd[0] for cmd in commands.values()], "Hardware Infos")
        choice = get_user_input()
        if choice == 'b':
            break
        elif choice == 'q':
            exit()
        elif choice.isdigit():
            option = int(choice)
            if option in commands:
                name, cmd = commands[option]
                print(Fore.LIGHTMAGENTA_EX + f"{name}:")
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                data = parse_wmic_output(result.stdout)
                if not data:
                    print(Fore.RED + "Error: No data found.")
                else:
                    if option == 1:  
                        for item in data:
                            print(Fore.LIGHTMAGENTA_EX + f"Name: {Fore.GREEN}{item.get('Name', 'N/A')}")
                            print(Fore.LIGHTMAGENTA_EX + f"Graphic-Card-ID: {Fore.GREEN}{item.get('PNPDeviceID', 'N/A')}")
                    elif option == 2: 
                        drives = ["C:/", "D:/", "E:/", "F:/", "G:/", "H:/", "I:/", "J:/"]
                        for i, item in enumerate(data):
                            print(Fore.LIGHTMAGENTA_EX + f"Drive: {Fore.GREEN}{drives[i]} {item.get('Model', 'N/A')}")
                            print(Fore.LIGHTMAGENTA_EX + f"ID: {Fore.GREEN}{item.get('SerialNumber', 'N/A')}")
                    elif option == 3: 
                        for item in data:
                            print(Fore.LIGHTMAGENTA_EX + f"Motherboard-Name: {Fore.GREEN}{item.get('Product', 'N/A')}")
                            print(Fore.LIGHTMAGENTA_EX + f"Motherboard-ID: {Fore.GREEN}{item.get('SerialNumber', 'N/A')}")
                    elif option == 4: 
                        for item in data:
                            print(Fore.LIGHTMAGENTA_EX + f"Name: {Fore.GREEN}{item.get('Name', 'N/A')}")
                            print(Fore.LIGHTMAGENTA_EX + f"Memory: {Fore.GREEN}{item.get('NumberOfCores', 'N/A')}")
                input(Fore.YELLOW + "Press Enter to continue...")
            else:
                print(Fore.RED + "Invalid input!")
        else:
            print(Fore.RED + "Invalid input!")

def network_hardware_check():
    commands = {
        1: ("Ping", "ping"),
        2: ("Disk Check", "chkdsk /f & chkdsk /r"),
        3: ("System Check", "sfc /scannow"),
        4: ("Windows Check", "DISM /Online /Cleanup-Image /CheckHealth"),
        5: ("Restore Windows", "DISM /Online /Cleanup-Image /RestoreHealth"),
        6: ("Restore Network", "netsh winsock reset & netsh int ip reset & ipconfig /release & ipconfig /flushdns & ipconfig /renew"),
        7: ("Star Wars", "pkgmgr /iu:TelnetClient && telnet towel.blinkenlights.nl")
    }
    while True:
        display_menu([cmd[0] for cmd in commands.values()], "Network/Hardware Check")
        choice = get_user_input()
        if choice == 'b':
            break
        elif choice == 'q':
            exit()
        elif choice.isdigit():
            option = int(choice)
            if option in commands:
                name, cmd = commands[option]
                print(Fore.LIGHTMAGENTA_EX + f"{name}:")
                if option == 1: 
                    ip = input(Fore.GREEN + "Enter the IP address you want to ping: ")
                    run_as_admin(f"ping {ip}")
                else:
                    run_as_admin(cmd)
                input(Fore.YELLOW + "Press Enter to continue...")
            else:
                print(Fore.RED + "Invalid input!")
        else:
            print(Fore.RED + "Invalid input!")

def bitlocker_decrypt():
    """Function to disable BitLocker (decrypt)."""
    print(Fore.YELLOW + "To disable BitLocker, please enter the BitLocker password you previously set.")
    password = input(Fore.GREEN + "BitLocker-Password: ")
    unlock_cmd = f'manage-bde -unlock C: -Password {password}'
    print(Fore.BLUE + "Unlocking drive...")
    run_as_admin(unlock_cmd, wait=True)
    off_cmd = 'manage-bde -off C:'
    print(Fore.BLUE + "BitLocker is being disabled. Please wait until the process is complete.")
    run_as_admin(off_cmd, wait=True)

def tpm_instructions():
    """Shows instructions on how to use BitLocker without a compatible TPM or how to enable a TPM."""
    print(Fore.YELLOW + "TPM/BitLocker Guide:")
    print(Fore.BLUE + "To use BitLocker without a compatible TPM, open the Group Policy Editor (gpedit.msc). Navigate to:")
    print(Fore.GREEN + "Administrative Templates → Windows Components → BitLocker Drive Encryption → Operating System Drives")
    print(Fore.BLUE + "Double-click 'Require additional authentication at system startup',")
    print(Fore.BLUE + "Enable the policy and check 'Allow BitLocker without a compatible TPM'.")
    print(Fore.BLUE + "Apply the changes and restart your computer.")
    print(Fore.RED + "If you want to use a TPM, make sure that a compatible TPM is enabled and installed in the BIOS.")
    input(Fore.YELLOW + "Press Enter to return to the menu...")

def basic_security():
    security_options = {
        1: ("Antivirus (Windows Defender)", "sc query WinDefend", "sc start WinDefend"),
        2: ("Firewall", "netsh advfirewall show allprofiles", "netsh advfirewall set allprofiles state on"),
        3: ("BitLocker activate", "manage-bde -status", "bitlocker_encrypt"),
        4: ("BitLocker deactivate", "manage-bde -status", "bitlocker_decrypt"),
        5: ("Remote Desktop", 'reg query "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections', 'reg add "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f'),
        6: ("UAC", 'reg query "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v EnableLUA', 'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v EnableLUA /t REG_DWORD /d 1 /f'),
        7: ("Accounts", "net user", None),
        8: ("Security protocols", "wevtutil qe Security /c:5 /f:text", None),
        9: ("TPM/BitLocker Instructions", None, None)
    }
    while True:
        options_list = [val[0] for key, val in sorted(security_options.items())]
        display_menu(options_list, "Basic Security Checks")
        choice = get_user_input()
        if choice == 'b':
            break
        elif choice == 'q':
            exit()
        elif choice.isdigit():
            option = int(choice)
            if option in security_options:
                name, check_cmd, remediate_cmd = security_options[option]
                print(Fore.LIGHTMAGENTA_EX + f"{name} Check:")
                result = subprocess.run(check_cmd, shell=True, capture_output=True, text=True, errors='replace') if check_cmd else None
                output = result.stdout if result else ""
                if output:
                    print(Fore.BLUE + output)
                
                if option == 1:  
                    if "RUNNING" in output:
                        print(Fore.GREEN + "Antivirus is already active. No remediation necessary.")
                    elif remediate_cmd:
                        r = input(Fore.GREEN + "Press (r) to fix the problem, or Enter to continue: ").strip().lower()
                        if r == 'r':
                            run_as_admin(remediate_cmd, wait=True)
                elif option == 2: 
                    if "State" in output and ("OFF" in output or "off" in output):
                        r = input(Fore.GREEN + "Firewall appears to be disabled. Press (r) to enable it, or Enter to continue: ").strip().lower()
                        if r == 'r' and remediate_cmd:
                            run_as_admin(remediate_cmd, wait=True)
                    else:
                        print(Fore.GREEN + "Firewall is already enabled.")
                elif option == 3:  
                    if "Protection Status:" in output and "On" in output:
                        print(Fore.GREEN + "BitLocker is already enabled.")
                    elif remediate_cmd:
                        r = input(Fore.GREEN + "Press (r) to enable BitLocker, or Enter to continue: ").strip().lower()
                        if r == 'r':
                            print(Fore.RED + "IMPORTANT: The password entered in the following window MUST be kept safe, as without it you will no longer have access to your data! Additionally, you must enable TPM (Trusted Platform Module) mode in the BIOS to encrypt your hard drives.")
                            print(Fore.YELLOW + "A terminal window will open. Please enter the desired password interactively and confirm it.")
                            run_as_admin("manage-bde -protectors -add C: -Password", wait=False)
                            input(Fore.YELLOW + "After adding password protection (manually close the window), press Enter to start encryption...")
                            run_as_admin("manage-bde -on C:", wait=True)
                elif option == 4: 
                    if remediate_cmd:
                        r = input(Fore.GREEN + "Press (r) to disable BitLocker, or Enter to continue: ").strip().lower()
                        if r == 'r':
                            bitlocker_decrypt()
                elif option == 5: 
                    if "0x1" in output:
                        print(Fore.GREEN + "Remote Desktop is already disabled.")
                    elif remediate_cmd:
                        r = input(Fore.GREEN + "Press (r) to disable Remote Desktop, or Enter to continue: ").strip().lower()
                        if r == 'r':
                            run_as_admin(remediate_cmd, wait=True)
                elif option == 6: 
                    if "0x1" in output:
                        print(Fore.GREEN + "UAC is already enabled.")
                    elif remediate_cmd:
                        r = input(Fore.GREEN + "Press (r) to enable UAC, or Enter to continue: ").strip().lower()
                        if r == 'r':
                            run_as_admin(remediate_cmd, wait=True)
                elif option == 7: 
                    r = input(Fore.GREEN + "Do you want to deactivate a user account? (j/n): ").strip().lower()
                    if r == 'j':
                        username = input(Fore.GREEN + "Enter the username you want to deactivate: ")
                        cmd = f"net user {username} /active:no"
                        run_as_admin(cmd, wait=True)
                elif option == 8: 
                    print(Fore.YELLOW + "Automatic remediation is not available for this option.")
                elif option == 9:
                    tpm_instructions()
                
                input(Fore.YELLOW + "Press Enter to continue...")
            else:
                print(Fore.RED + "Invalid input!")
        else:
            print(Fore.RED + "Invalid input!")

def main():
    while True:
        clear_screen()
        print(Fore.LIGHTMAGENTA_EX + r"""
__          ___           _                         
\ \        / (_)         | |                        
 \ \  /\  / / _ _ __   __| | _____      _____       
  \ \/  \/ / | | '_ \ / _` |/ _ \ \ /\ / / __|      
   \  /\  /  | | | | | (_| | (_) \ V  V /\__ \      
    \/  \/   |_|_| |_|\__,_|\___/ \_/\_/ |___/      
 _    _            _ _   _       _______          _ 
| |  | |          | | | | |     |__   __|        | |
| |__| | ___  __ _| | |_| |__      | | ___   ___ | |
|  __  |/ _ \/ _` | | __| '_ \     | |/ _ \ / _ \| |
| |  | |  __/ (_| | | |_| | | |    | | (_) | (_) | |
|_|  |_|\___|\__,_|_|\__|_| |_|    |_|\___/ \___/|_|
        """)
        print(Fore.BLUE + "If you have any problems or suggestions, Contact me : https://iddox.tech/")
        print(Fore.BLUE + "Select an option:")
        print(Fore.LIGHTMAGENTA_EX + "1. Network Infos")
        print(Fore.LIGHTMAGENTA_EX + "2. Hardware Infos")
        print(Fore.LIGHTMAGENTA_EX + "3. Network/Hardware Check")
        print(Fore.LIGHTMAGENTA_EX + "4. Basic Security")
        print(Fore.RED + "(q) quit")
        choice = get_user_input()
        if choice == '1':
            network_info()
        elif choice == '2':
            hardware_info()
        elif choice == '3':
            network_hardware_check()
        elif choice == '4':
            basic_security()
        elif choice == 'q':
            break
        else:
            print(Fore.RED + "Invalid input!")

if __name__ == "__main__":
    main()
