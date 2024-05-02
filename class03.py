#!/usr/bin/python3

# Script: Ops 401 Challenge 03
# Author: Rebecca Childs
# Date of last revision: 05/01/2024
# Purpose:
# Ask the user for an email address and password to use for sending notifications.
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

from email.message import EmailMessage
import ssl 
import smtplib

email_sender: 'potterpuff38@gmail.com'
email_password: ""
email_receiver: 'totallytech97840@outlook.com'

subject = 'Tentacula overtaking HP common room!!' 
body = """
Someone smuggled a vanomous tentacula into the hufflepuff common room! Please send Madam Pomfrey and Professor Sprout immediately!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set.content(body)

contect = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())