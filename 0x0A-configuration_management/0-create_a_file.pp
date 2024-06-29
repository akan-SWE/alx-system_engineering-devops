# create a file school in /tmp, set it metadata and inserts a text

file { '/tmp/school':
  ensure  => 'present',
    owner => 'www-data',
    group => 'www-data',
    mode  => '0744',
  content => 'I love Puppet'
}
