#!/usr/bin/env python3

import shutil
import psutil
import socket
import email
import smtplib


## stress --cpu 8: stress cpu
## crontab -e: exucete file each 60 minutes



#Warning if CPU usage is over 80%
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = (du.free / du.total) * 100
    return free > 20

#Report an error if available disk space is lower than 20%
def check_cpu_usage():
    usage_cpu = psutil.cpu_percent(1)
    return usage_cpu < 80

#Report an error if available memory is less than 500MB
def available_memory():
    m = psutil.virtual_memory()
    return m.available/1024 ** 2 > 500

#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
def hostname_check():
    local_host_ip = socket.gethostbyname('localhost')
    return local_host_ip == "127.0.0.1"

def email_warning(error):
    # sender = "automation@example.com"
    # receiver = "student-02-dde78dd51971@example.com"
    # subject = error
    # body = "Please check your system and resolve the issue as soon as possible."
    
    # message = email.message.EmailMessage()
    # message["From"] = sender
    # message["To"] = receiver
    # message["Subject"] = subject
    # message.set_content(body)
    
    # ## Send Message
    # mail_server = smtplib.SMTP('localhost')
    # mail_server.send_message(message)
    # mail_server.quit()
    print(error)

def principal():
    if not check_cpu_usage():
      subject = "Error - CPU usage is over 80%"
      email_warning(subject)
    
    if not check_disk_usage("/"):
      subject = "Error - Available disk space is less than 20%"
      email_warning(subject)
    
    if not available_memory():
      subject = "Error - Available memory is less than 500MB"
      email_warning(subject)
    
    if not hostname_check():
      subject = "Error - localhost cannot be resolved to 127.0.0.1"
      email_warning(subject)

if __name__ == "__main__":
    principal()
