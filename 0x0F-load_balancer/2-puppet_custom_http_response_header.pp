# Custom HTTP header response with Puppet

exec {'Update System':
  provider => shell,
  command  => 'sudo apt-get -y update',
}
-> exec {'Nginx Installation':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
}
-> file_line {'Adding Header':
  path   => '/etc/nginx/nginx.conf',
  match  => 'http {',
  line   => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec {'Restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
