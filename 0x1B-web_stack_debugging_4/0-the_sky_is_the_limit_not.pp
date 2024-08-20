# Increses the ULIMIT to 4096
exec { 'increase_ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin', '/usr/bin'],
  notify  => Exec['nginx-restart'],
}

# Restarts nginx
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  path        => ['/usr/sbin', '/sbin', '/usr/local/bin', '/bin', '/usr/bin'],
  refreshonly => true,
}
