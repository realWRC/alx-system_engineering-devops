exec { 'flask_install':
  command => '/usr/bin/pip3 install flask=2.1.0',
  path    => ['/usr/bin', '/bin'],
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
