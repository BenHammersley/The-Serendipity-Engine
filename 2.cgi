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
<body>
<link rel="stylesheet" type="text/css" href="styles.css"/>
<script type="text/javascript" src="webcam.js"></script>
<script language="JavaScript">
	webcam.set_api_url( "photosaver.php" );
	webcam.set_quality( 100 ); // JPEG quality (1 - 100)
	webcam.set_shutter_sound( true ); // play shutter click sound
</script>

<h1>Take a look at yourself, $name.</h1>
<p>Take the paper from The Serendipity Engine's Attendant. When you have followed the instructions, hold the picture up to the camera, and smile. You are being watched. Do not be alarmed.</p>
<script language="JavaScript">
	document.write( webcam.get_html(320, 240) );
</script>

<!-- Some buttons for controlling things -->
<br/>
<br/>
<br/>

<!--<form>
	<input type=button value="The Button" onClick="take_snapshot()">
</form>
//-->

<form>
<input type="hidden" name="name" value="$name">
<button type=submit formaction="3.cgi">Ready? Press me to continue</button>
</form>


<!-- Code to handle the server response (see test.php) -->
<script language="JavaScript">
	webcam.set_hook( 'onComplete', 'my_completion_handler' );
	
	function take_snapshot() {
		// take snapshot and upload to server
		document.getElementById('upload_results').innerHTML = '<h1>Uploading...</h1>';
		webcam.snap();
	}
	
	function my_completion_handler(msg) {
		// extract URL out of PHP output
		if (msg.match(/(http\:\/\/\S+)/)) {
			var image_url = RegExp.$1;
			// show JPEG image in page
			document.getElementById('upload_results').innerHTML = 
				'<h1>Upload Successful!</h1>' + 
				'<h3>JPEG URL: ' + image_url + '</h3>' + 
				'<img src="' + image_url + '">';
			
			// reset camera for another shot
			webcam.reset();
		}
		else alert("PHP Error: " + msg);
	}
</script>

<div id="upload_results" style="background-color:#eee;"></div>

</body>
</html>

EOM

exit;