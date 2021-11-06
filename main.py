import paramiko

shells_number = int(input("Enter the number of shells you are going to create: "))
commandtoexecute = input("Enter the command to execute: ")

for i in range(shells_number):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    shellip = input("Enter the shell IP: ")
    shellport = input("Enter the shell port: ")
    username = input(f"Enter the username of the shell with IP {shellip}: ")
    password = input(f"Enter the password of the shell with IP {shellip}: ")
    ssh.connect(shellip, port=shellport, username=username, password=password)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(commandtoexecute)
    ssh_output = ssh_stdout.read().decode("ascii").strip("\n")
    print(f"Received output from {shellip}: {ssh_output}")