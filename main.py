import paramiko
commandtoexecute = input("Enter the command to execute: ")
# Initializing 2 ssh connections
ssh1 = paramiko.SSHClient()
ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh1.connect("IP1", port=22, username="USERNAME", password="PASSWORD")

ssh2 = paramiko.SSHClient()
ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh2.connect("IP2", port=22, username="USERNAME", password="PASSWORD")

ssh1_stdin, ssh_stdout, ssh_stderr = ssh1.exec_command(commandtoexecute)
ssh2_stdin, ssh2_stdout, ssh2_stderr = ssh2.exec_command(commandtoexecute)

output1 = ssh_stdout.read().decode('ascii').strip("\n")
output2 = ssh2_stdout.read().decode('ascii').strip("\n")

print("Output of server 1")
print(output1)

print("Output of server 2")
print(output2)
