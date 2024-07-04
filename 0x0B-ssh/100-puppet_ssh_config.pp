# This Puppet manifest appends a configuration block to the global SSH configuration file.
# The configuration block sets up an alias "schoolserver" for the host with the IP address 100.26.173.36,
# specifies the identity file to use when connecting to the host, and disables password authentication.

# Include the stdlib module
include stdlib

# Ensure the SSH client configuration directory exists
file { '~/.ssh':
  ensure => directory,
}

# Ensure the SSH client configuration file exists
file { '~/.ssh/school':
  ensure => file,
}

# Configure SSH client to use the private key
file_line { 'Declare identity file':
  path  => '~/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
}

# Configure SSH client to refuse password authentication
file_line { 'Turn off passwd auth':
  path  => '~/.ssh/config',
  line  => 'PasswordAuthentication no',
}
