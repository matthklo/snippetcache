#!/usr/bin/python
# -*- coding: UTF-8 -*-

############################################
# This script should be called by server watch
# dog script.
#
# It shall be called with 3 mandatory arguments
# follow by zero or more optional attachment files:
#   $1: 'To' (The recipient email list seperated by spaces)
#   $2: 'Subject' (The subject of the email)
#   $3: 'Body' (The content of the email)
#   [$4...]: File to be attached.

from __future__ import print_function
import smtplib
import sys

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if len(sys.argv) < 4:
  print('Error: Insufficient command line arguments.', file=sys.stderr)
  sys.exit(1)

fromaddr='{your gmail addr}'
smtppwd='{your gmail pwd}'
toaddrs=sys.argv[1].split()
subject=sys.argv[2]
body=sys.argv[3]

conn = smtplib.SMTP_SSL('smtp.gmail.com', 465)
conn.login(fromaddr, smtppwd)

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ', '.join(toaddrs)
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain', 'utf-8'))

for att in sys.argv[4:]:
  try:
    with open(att, 'rb') as rf:
      part = MIMEApplication(rf.read(), Name=basename(att))
      part['Content-Disposition'] = 'attachment; filename="%s"' % basename(att)
      msg.attach(part)
  except Exception as e:
    print('Warning: File "%s" is not readable. Skip it.' % att)

conn.sendmail(fromaddr, toaddrs, msg.as_string())
conn.quit()
