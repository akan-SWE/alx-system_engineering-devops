# Install and configure Nginx server

package { 'nginx':
  ensure => latest,
}


service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Service['nginx']
}


$url = 'https://www.google.com'

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
                try_files \$uri \$uri/ =404;
        }

        location /redirect_me {
            return 301 ${url};
        }
    }",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
