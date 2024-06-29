# Install Flask from pip3

package { ['python3', 'python3-pip']:
  ensure => installed
}

package { 'werkzeug':
  ensure   => '2.1.1',
  require  => Package['python3-pip'],
  provider => 'pip3'
}

package { 'flask':
  ensure   => '2.1.0',
  require  => Package['python3-pip', 'werkzeug'],
  provider => 'pip3'
}
