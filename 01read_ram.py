import paramiko
import os

def capture_ram_remote(host, username, password, lime_path, output_path,local_save_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)

        cmd = f"sudo insmod {lime_path} path={output_path} format=lime && gzip {output_path}"
        stdin, stdout, stderr = ssh.exec_command(cmd)
        stdin.write(password + '\n')  # if sudo prompts for password
        stdin.flush()

        stdout_text = stdout.read().decode()
        stderr_text = stderr.read().decode()
        print("[✓] Remote RAM capture initiated")
        if stdout_text:
            print("STDOUT:", stdout_text)
        if stderr_text:
            print("STDERR:", stderr_text)


        ssh.close()

        print("⏳ Waiting for dump to finish...")
        import time; time.sleep(5)

        print("📥 Connecting for download...")
        transport = paramiko.Transport((host, 22))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        print(f"⬇️ Downloading dump to {local_save_path}...")
        sftp.get(output_path, local_save_path)

        sftp.close()
        transport.close()
        print("✅ RAM dump downloaded successfully!")

    except Exception as e:
        print(f"[✗] Error: {e}")

# Example
capture_ram_remote(
    host=input("Enter remote host IP: "),
    username=input("Enter remote username: "),
    password=input("Enter remote password: "),
    lime_path='/root/LiME/src/lime-5.14.0-570.12.1.el9_6.x86_64.ko',
    output_path='/root/memdump_remote.lime',
    local_save_path=os.path.expanduser('~/Downloads/memdump_remote.lime') 
)
