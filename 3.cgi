#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

my $cgi = CGI->new();
my $name = $cgi->param("name");

print "Content-type: text/html\n\n";
print <<EOM;
<html>
<head>
<title>Serendipity Engine, Page 2: Portrait</title></head>
<link rel="stylesheet" type="text/css" href="styles.css"/>
<body>
<h1>$name! Please respond to the following questions.</h1>
<form id=answers>
	<fieldset id=aboutyou>
		<legend>About you</legend>
		<input type="hidden" name="name" value="$name">
		
		<label for=postcode>Postcode</label>
		<input id=postcode name=postcode type=text placeholder="Postcode" required autofocus>
		
		<label for=housenumber>House Number</label>
		<input id=postcode name=houseno type=text placeholder="Housenumber" required>
		
		<label for=age>How old were you at your last birthday?</label>
		<input id=age name=age type=text placeholder="45" required>
		
		<label for=agefeel>How old do you feel?</label>
		<input id=agefeel name=agefeel type=text placeholder="21" required>
		
		<label for=email>Email</label>
		<input id=email name=email type=email placeholder="email@example.com" required>
	</fieldset>
	
	<fieldset>
		<legend>Please list your usernames for the following social networks</legend>

		
		<label for=twitter>Twitter</label>
		<input id=twitter name=twitter type=text placeholder="Twitter">
		
		<label for=facebook>Facebook</label>
		<input id=facebook name=facebook type=text placeholder="Facebook">		
		
		<label for=googleplus>Google+</label>
		<input id=googleplus name=googleplus type=text placeholder="Google+">
		
	</fieldset>
	
	<fieldset id=influences>
		<legend>Your influences</legend>
		
		<label for=growup>When you were a child, what did you want to be when you grew up?</label>
		<input id=grownup name=grownup type=text placeholder="A fireman, or maybe a chef. No! An astronaut.">		
		
		<label for=film>What has been the most influential film in your life?</label>
		<input id=film name=film type=text placeholder="Breakin' 2: Electric Boogaloo">
		
		<label for=lastmeal>If you knew you had to die tomorrow, which three foods would be on your last menu?</label>
		<input id=lastmean name=lastmeal type=text placeholder="Ptarmigan Foiegras Twinkies">
		
		<label for=subject>What was your favourite subject at school?</label>
		<input id=subject name=subject type=text placeholder="Post-modernist sports">		
		
		<label for=song>Which one song would you take to a desert island?</label>
		<input id=song name=song type=text placeholder="Shadduppayaface">
		
		<label for=artist>And who sings that?</label>
		<input id=artist name=artist type=text placeholder="Joe Dolce">
	</fieldset>
	
	<fieldset id=parents>
		<legend>Parental Knowledge</legend>
		<label for=father>If your father had appeared on Mastermind, what would his specialist subject be?</label>
		<input id=father name=father type=text placeholder="Knitting">		
		
		<label for=mother>And your mother's?</label>
		<input id=mother name=mother type=text placeholder="Football">
	</fieldset>
	
	<fieldset>
		<legend>Please read this sentence</legend>
		<p>If the cake is from France, then it has more sugar if it is made with chocolate than if it is made with cream, but if the cake is from Spain, then it has more sugar if it is made with cream than if it is made with chocolate.</p>
	</fieldset>
	
	<button type=submit formaction="4.cgi">Now proceed to the suitcase. When you have set the switches, press me to continue</button>
	
	</form>
				
EOM

exit;