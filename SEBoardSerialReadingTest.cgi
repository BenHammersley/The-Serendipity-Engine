#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);


# This is to test the connection with the SE board, and the switches and sensors

# Set up the serial port
use Device::SerialPort;
my $port = Device::SerialPort->new("/dev/tty.usbserial");

# 19200, 81N on the USB ftdi driver
$port->baudrate(19200); # you may change this value
$port->databits(8); # but not this and the two following
$port->parity("none");
$port->stopbits(1);

# now catch gremlins at start
my $tEnd = time()+2; # 2 seconds in future
while (time()< $tEnd) { # end latest after 2 seconds
  my $c = $port->lookfor(); # char or nothing
  next if $c eq ""; # restart if noting
  # print $c; # uncomment if you want to see the gremlin
  last;
}


while (1) {
    # Poll to see if any data is coming in
    my $char = $port->lookfor();

    # If we get data, then print it
    # Send a number to the arduino
    if ($char) {
        print "Received character: $char \n";
    }
    # Uncomment the following lines, for slower reading, 
    # but lower CPU usage, and to avoid 
    # buffer overflow due to sleep function. 

    # $port->lookclear; 
    # sleep (1);
}