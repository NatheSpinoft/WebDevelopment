# March 9 2024 
Saved a few changes to scripts and learned a few python material

# March 10 2024
Corrected postgresql clusters

## Given
There was an issue with the reinstallation of postgresql as the main postgresql folder was deleted

## Required
The main folder in /var/lib/postgresql/14/main to be reinstated and to fix the error

## Analysis
Going through the pg_lsclusters no instance was recorded, so looking onling found the function to use /etc/init.d/postgresql

## Solution
The solution was to use the /etc/init.d/postrgresql restart function 

## Statement
If there is an issue with missing files in the postrgresql directory restarting services under init.d would help

# October 10 2024

## Understand the Current Setup
The current setup was the Ubuntu 22.04 Desktop amd64 was currently lagging behind and the website for stefannstuff.com could use
some more current changes if ubuntu was upgraded to 24.05. 

## Prepare for the update
backed up the app.py script along with the subprocess with the smtp.py in a file called stefannstuff-2024-10-06.py

## Gather Resources
N/A resources were installed via terminal

## Review Update Process

## Apply Updates
Sudo apt-update, sudo apt-upgrade

## Document Changes
Batch files were updated and removed 721 obsolete libraries

## Evaluate and test
Issue noted when entering into boot mode there was a MOKLIST error Volume Full. 
Steps to resolve:
    Disable secure boot
    Use custom keys opposed to HP keys
    System restore security settings

Evaluation: grub now works and can enter Ubuntu

Documentation of Changes
Project Overview

This document outlines the changes implemented in the app.py and smtp.py files for the Flask application, as well as configurations related to the website stefannstuff.com.
1. Flask Application (app.py)
General Overview

    Framework: Flask
    Purpose: Handle web requests, manage user sessions, and facilitate email sending through SMTP.

Key Changes
1.1. Environment Variable Loading

    Utilized the python-dotenv package to load environment variables.

python

from dotenv import load_dotenv
load_dotenv()

1.2. Email Configuration

    Introduced environment variables for SMTP configurations, including EMAIL, PASSWORD, SMTP_SERVER, and SMTP_PORT.

1.3. Contact Route

    Implemented a contact form that allows users to send emails.
    Validated form fields to ensure all inputs are filled.

python

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        sender_email = request.form.get('email')
        subject = request.form.get('subject')
        message_body = request.form.get('message')

1.4. Subprocess Management

    Integrated subprocess handling to manage external scripts related to SMTP, though later modified to use function calls directly instead.

1.5. Error Handling

    Added flash messages for user feedback during email sending and form submission processes.

python

if not sender_email or not subject or not message_body:
    flash("All fields are required.", 'error')

2. SMTP Script (smtp.py)
General Overview

    Purpose: Handle email sending using SMTP.

Key Changes
2.1. Environment Variable Usage

    Used dotenv to load email credentials and SMTP server details.

2.2. Email Sending Functionality

    Created a function send_email to manage the email composition and sending process.

python

def send_email(sender_email, subject, message_body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = EMAIL
    msg['Subject'] = subject

2.3. SMTP Connection Handling

    Established an SMTP connection, started TLS encryption, and handled authentication for sending emails.

python

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.ehlo()
    server.starttls()
    server.login(EMAIL, PASSWORD)

2.4. Error Management

    Implemented try-except blocks to capture and report errors during the email sending process.

python

except Exception as e:
    print(f'Failed to send message: {str(e)}')

3. Website Configuration (stefannstuff.com)
General Overview

    Purpose: Host the Flask application and serve user-facing web pages.

Key Changes
3.1. Fully Qualified Domain Name (FQDN)

    Set the FQDN as stefannstuff.com and hostname as stefanpinto-ubuntu.

3.2. SPF Records

    Implemented Sender Policy Framework (SPF) records to authorize sending emails from stefannstuff.com.

Example SPF Record:

less

v=spf1 a mx include:_spf.your-email-provider.com ~all

Additional Notes

    Ensure that your DNS settings reflect the correct SPF records for proper email authentication.

This report summarizes the changes made to enhance your Flask application and email sending capabilities, along with website configurations. Let me know if you need any more details or further modifications!