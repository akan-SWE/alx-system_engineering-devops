# This Puppet manifest appends a configuration block to the global SSH configuration file.
# The configuration block sets up an alias "schoolserver" for the host with the IP address 100.26.173.36,
# specifies the identity file to use when connecting to the host, and disables password authentication.
exec {'ssh_config':
  command => "/bin/echo -e '
    Host schoolserver
        HostName 100.26.173.36
        user ubuntu
        IdentityFile ~/.ssh/school
        PasswordAuthentication no' >> /etc/ssh/ssh_config",
  path    => ['/bin/', '/usr/bin/'],
  unless  => '/bin/grep -q "Host schoolserver" /etc/ssh/ssh_config'
}
