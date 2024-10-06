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
