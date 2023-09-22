# Execute a command and create a manifest that kills a process named killmeno
exec { 'pkill killmenow':
  path => '/usr/bin:/usr/sbin:/bin'
}
