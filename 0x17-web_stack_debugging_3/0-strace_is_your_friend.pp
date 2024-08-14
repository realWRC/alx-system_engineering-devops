# Puppet script to replace and correct syntax errors.

# Correct all intances of phpp syntax error to php

$file = '/var/www/html/wp-settings.php'

exec { 'correct_syntax':
  command => "sed -i 's/phpp/php/g' ${file}",
  path    => ['/bin', '/usr/bin'],
  onlyif  => "grep 'phpp' ${file}",
}
