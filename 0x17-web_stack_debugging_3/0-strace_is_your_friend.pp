# This Puppet manifest is intended to fix an issue in the WordPress configuration file
# `/var/www/html/wp-settings.php`. Specifically, it replaces all occurrences of
# `class-wp-locale.phpp` with `class-wp-locale.php`. This correction is necessary
# to address a typo that results in a 500 Internal Server Error due to incorrect file
# references.
#
# The manifest ensures the presence of the file and performs the replacement if the
# incorrect reference is found.
exec {'replace_phpp_with_php':
  command => '/bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
  onlyif  => '/bin/grep -q "phpp" /var/www/html/wp-settings.php'
}
