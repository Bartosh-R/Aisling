import subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

sendmessage("Simpla is started")