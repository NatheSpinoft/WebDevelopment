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

