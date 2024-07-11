##
#   This script performs the following tasks on a server running Ubuntu:
#
#   1. Installs Nginx.
#   2. Configures the server to redirect any requests coming in at /redirect_me to another page.
#   3. Sets up a custom 404 error page.
#   4. Adds a custom Nginx response header.
##

# Install nginx
package { 'nginx':
  ensure => latest
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}

# Backup the original configuration file
file { '/etc/nginx/sites-available/default.bak':
  ensure => file,
  source => '/etc/nginx/sites-available/default'
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Service['nginx']
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
  require => Service['nginx']
}


$url = 'https://www.google.com'

# Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    # Add index.php to the list if you are using PHP
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        add_header X-Served-By \"${::hostname}\";
        try_files \$uri \$uri/ =404;
    }

    # Configure redirection
    location /redirect_me {
        return 301 ${url};
    }

    # Define custom 404 page
    error_page 404 /404.html;
}
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
