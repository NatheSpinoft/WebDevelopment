Steps to Tie Apache Server to a Website Name:

    Configure DNS Records:
        Set up your domain name provider to point your domain to the IP address of your server.
        Use an A record to map the domain (e.g., example.com) to the server's IP address.
        Optionally, use a CNAME record to map www.example.com to example.com.

    Enable Apache Virtual Hosts:
        Apache uses Virtual Hosts to serve multiple websites from the same server. You need to configure a Virtual Host for your domain.

    Create the Virtual Host Configuration File:
        Navigate to the Apache sites directory:

        bash

cd /etc/apache2/sites-available/

Create a new configuration file for your domain, such as example.com.conf:

bash

    sudo nano /etc/apache2/sites-available/example.com.conf

Configure the Virtual Host: Inside the new configuration file, specify the domain, server name, and where the website's files are located. Here's a basic template:

apache

<VirtualHost *:80>
     ServerAdmin admin@example.com
     ServerName example.com
     ServerAlias www.example.com
     
     DocumentRoot /var/www/html/example.com/
     
     ErrorLog ${APACHE_LOG_DIR}/error.log
     CustomLog ${APACHE_LOG_DIR}/access.log combined
     
     # Optional: Proxy settings for back-end applications
     # ProxyPass / http://localhost:5000/
     # ProxyPassReverse / http://localhost:5000/
</VirtualHost>

    Replace example.com with your domain and /var/www/html/example.com/ with the actual path to your website files.

Enable the New Site: Enable your virtual host configuration using the a2ensite command:

bash

sudo a2ensite example.com.conf

Disable the Default Site (Optional): If Apache's default site is enabled, you may want to disable it to avoid conflicts:

bash

sudo a2dissite 000-default.conf

Reload Apache: After making these changes, reload or restart Apache to apply the new configuration:

bash

sudo systemctl reload apache2

Test the Setup: Visit your domain in a web browser (e.g., http://example.com). If DNS is configured correctly and Apache is properly set up, you should see your website.