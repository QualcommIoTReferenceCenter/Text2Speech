#!/usr/bin/expect -f
# Conecta o bluetooth, precisa passar o MAC adress como parametro

set prompt '#'
set adress [lindex $argv 0]

spawn sudo bluetoothctl
sleep 1
send "trust $adress\r"
sleep 2
send "pair $adress\r"
sleep 3
send "connect $adress\r"
sleep 4
send "quit\r"
expect eof
