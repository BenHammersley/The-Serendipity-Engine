#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);


# This is to test the connection with the SE board, and the switches and sensors

# Set up the serial port
use Device::SerialPort;
my $port = Device::SerialPort->new("/dev/tty.usbmodem1a21");

# 9600, 81N on the USB ftdi driver
$port->baudrate(9600); # you may change this value
$port->databits(8); # but not this and the two following
$port->parity("none");
$port->stopbits(1);

$port->write("abcdef 123456\n\n\n\n\n\n\n");