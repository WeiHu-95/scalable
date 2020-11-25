import paramiko
import base64

hostname='macneill.scss.tcd.ie'
port=22
username='huwe'
password=base64.b64decode("SHc1NjYwNzM2Pw==").decode("utf-8")
conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect(hostname, port, username, password)
transport = conn.get_transport()
end =('rasp-019.berry.scss.tcd.ie',22)
start =('macneill.scss.tcd.ie' ,22)
channel = transport.open_channel("direct-tcpip",end,start)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('rasp-019.berry.scss.tcd.ie',username='huwe', password=base64.b64decode("SHc1NjYwNzM2Pw==").decode("utf-8"),sock = channel)
command = "sh automation.sh"
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)