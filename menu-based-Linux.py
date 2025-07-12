import threading
import speech_recognition as sr
import paramiko

# Remote SSH Configuration
ip_address = input("Enter the remote IP address: ")
username = input("Enter the SSH username: ")
password = input("Enter the SSH password: ")

# Initialize SSH client globally
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(ip_address, username=username, password=password)
except Exception as e:
    print(f"[!] Failed to connect: {e}")
    exit(1)

def run_remote_command(command):
    print(f"\n[+] Running: {command}\n")
    try:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print(output)
        else:
            print("[!] No output.")

        if error:
            print(f"[!] Error:\n{error}")
    except Exception as e:
        print(f"[!] Exception occurred: {e}")

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎤 Listening... (say a command name)\n")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"[Voice Input]: {command}")
            return command
        except sr.UnknownValueError:
            print("[!] Could not understand audio.")
        except sr.RequestError as e:
            print(f"[!] Recognition error: {e}")
    return None

def main():
    print("\nRemote Linux Command Executor via SSH")
    print("-------------------------------------")

    menu = {
        "1": ("Show date", "date"),
        "2": ("Show time", "date +%T"),
        "3": ("List directory", "ls -l"),
        "4": ("Current user", "whoami"),
        "5": ("System info", "uname -a"),
        "6": ("Running tasks", "top -b -n 1 | head -15"),
        "7": ("IP config", "ip a"),
        "8": ("Active connections", "ss -tuln"),
        "9": ("ARP table", "ip neigh"),
        "10": ("All users", "cut -d: -f1 /etc/passwd"),
        "11": ("Logged in users", "who"),
        "12": ("Environment variables", "printenv"),
        "13": ("List services", "systemctl list-units --type=service --state=running"),
        "14": ("Running processes", "ps aux --sort=-%mem | head -10"),
        "15": ("Installed packages", "dpkg -l | head -20 || rpm -qa | head -20"),
        "16": ("Battery status", "acpi -b || echo 'No battery info'"),
        "17": ("Disk usage", "df -h"),
        "18": ("Startup programs", "ls /etc/init.d/"),
        "19": ("BIOS info", "dmidecode -t bios"),
        "20": ("CPU info", "lscpu"),
        "21": ("Memory info", "free -h"),
        "22": ("Motherboard info", "dmidecode -t baseboard"),
        "23": ("Network adapters", "lshw -class network"),
        "24": ("Uptime", "uptime"),
        "25": ("Routing table", "ip route")
    }

    def display_menu():
        for key, (desc, _) in menu.items():
            print(f"{key}. {desc}")
        print("v. Voice command")
        print("q. Quit")

    display_menu()

    while True:
        choice = input("\nEnter your choice (or 'v' for voice): ").strip().lower()
        matched = False

        # Match by number
        if choice in menu:
            _, cmd = menu[choice]
            thread = threading.Thread(target=run_remote_command, args=(cmd,))
            thread.start()
            matched = True

        # Match by description
        else:
            for _, (desc, cmd) in menu.items():
                if choice == desc.lower():
                    thread = threading.Thread(target=run_remote_command, args=(cmd,))
                    thread.start()
                    matched = True
                    break

        # Voice input
        if choice == "v":
            voice_input = listen_for_command()
            if voice_input:
                found = False
                for _, (desc, cmd) in menu.items():
                    if voice_input in desc.lower():
                        thread = threading.Thread(target=run_remote_command, args=(cmd,))
                        thread.start()
                        found = True
                        break
                if not found:
                    print("[!] Voice command not recognized. Try again.")
            matched = True

        # Quit
        elif choice == "q":
            print("Exiting.")
            break

        # Invalid
        if not matched and choice not in ("v", "q"):
            print("Invalid choice. Try again.")

    ssh_client.close()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Exiting.")
        ssh_client.close()
