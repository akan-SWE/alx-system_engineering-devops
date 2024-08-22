# Increase Nginx file descriptor limit to 65535
# This ensures Nginx can handle a large number of simultaneous requests by setting a higher ulimit.


file {'increase_nginx_ulimit':
  ensure  => file,
  path    => '/etc/default/nginx',
  content =>
'
# Note: You may want to look at the following page before setting the ULIMIT.
#  http://wiki.nginx.org/CoreModule#worker_rlimit_nofile
# Set the ulimit variable if you need defaults to change.
#  Example: ULIMIT="-n 4096"
ULIMIT="-n 65535"

'
}
# Restart nginx automatically if the file '/etc/default/nginx' changes
service {'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['increase_nginx_ulimit']
}
