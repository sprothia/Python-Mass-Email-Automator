import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load your spreadsheet data, this should contain Name and Email columns of the recipients
data = pd.read_csv('data.csv')

# Email credentials
my_email = "test@gmail.com"
my_password = "" # this is not your gmail password, but rather an app password you have to obtain. Refer to readme for instructions

# Set up the server
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login(my_email, my_password)

# Iterate over the rows of the spreadsheet
for index, row in data.iterrows():
    name = row['Name']
    email = row['Email']

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = email
    msg['Subject'] = f"Add subject line here"

    # Email body
    body = f"""
Hi {name},

 Add rest of body here

 Thanks so much,

 Siddharth
"""
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    server.send_message(msg)
    print(f"Email sent to {name}")

# Close the server
server.quit()
