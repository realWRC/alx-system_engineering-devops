exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton hard/s/.*/holberton hard nofile 50000/" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep "^holberton hard" /etc/security/limits.conf',
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/.*/holberton soft nofile 50000/" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep "^holberton soft" /etc/security/limits.conf',
}
