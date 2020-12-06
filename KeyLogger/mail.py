#!/usr/bin/env python3

import smtplib
import ssl

# Email and password for SMTP server (gmail account)
from_email = 'smtplib.sav@gmail.com'
from_password = 'XDSkPwtDU8erDJy'

# Send log to this address
to_email = from_email  # 'saveriomattolisurvey@gmail.com'

# Body of email
message = 'testing'

# Set up a secure SMTP server connection
print('Connecting...')
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        print('Connected!')
        try:
            # log in to gmail account
            print('Logging in...')
            server.login(from_email, from_password)
            print('Logged in!')
            try:
                # Send message
                print('Sending mail...')
                server.sendmail(from_email, to_email, message)
                print('Mail sent!')
            except Exception as send_ex: # Full exception list - https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail
                print('sendmail failed - try again')
                # print(send_ex)
        except Exception as login_ex: # Full exception list - https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.login
            print('login failed - try again')
            # print(login_ex)
except Exception as connect_ex:
    print('connection failed - try again')
    # print(connect_ex)


""" context = ssl.create_default_context()
    server = smtplib.SMTP("smtp.gmail.com", 587)

    try:
      # server.ehlo()
      server.starttls(context=context)
      # server.ehlo()
      server.login(email,password)
      server.sendmail(email,email,message)
      # From our email to our email
    except Exception as e:
      print(e)
    finally:
      server.quit() """