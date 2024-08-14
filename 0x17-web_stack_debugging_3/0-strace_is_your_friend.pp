# Correct all intances of phpp syntax error to php
exec { 'correct_syntax':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin', '/usr/bin'],
  onlyif  => "grep 'phpp' ${file}",
}
