exec { 'kill_process':
  command     => 'pkill -9 killmenow',
  path        => '/bin:/usr/bin',
  onlyif      => 'pgrep killmenow',
  refreshonly => 'true',
}
