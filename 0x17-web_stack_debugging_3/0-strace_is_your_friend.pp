# using strace to determine Apache 500 error
# Bad "phpp" extension to "php" in "wp-settings.php"

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
