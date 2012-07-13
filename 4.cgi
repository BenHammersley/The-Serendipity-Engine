#!/usr/bin/perl -w
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use IMDB::Film;
use Lyrics::Fetcher;
use WWW::Wikipedia;
use Lingua::Translate;
use Lingua::StopWords qw(getStopWords);
use List::Util qw/shuffle/;
use Device::SerialPort::Arduino;

my $cgi = CGI->new();
my $name = $cgi->param("name");

#Film lookup on IMDB
my $film = $cgi->param("film");
my $imdbobj = new IMDB::Film (crit => "$film", debug => 1);
my $filmplot = ($imdbobj->storyline());
my @plotwords = ($filmplot =~ /(\w+)/g);
my $tenplotwords = join ' ', @plotwords[0..10];


#Lyrics lookup from song
my $song = $cgi->param("song");
my $artist = $cgi->param("artist");
my $songlyrics = Lyrics::Fetcher->fetch("$artist", "$song");
my @songwords = ($songlyrics =~ /(\w+)/g);
my $tensongwords = join ' ', @songwords[0..5];

#Subject lookup on Wikipedia
my $subject = $cgi->param("subject");
my $wiki = WWW::Wikipedia->new();
my $wikiobj = $wiki->search("$subject");
my $subjectsummary = $wikiobj->text();
my @subjectwords = ($subjectsummary =~ /(\w+)/g);
my $tensubjectwords = join ' ', @subjectwords[60..65];
my $subjectrelated = $wikiobj->related();


#Father Subject lookup on Wikipedia
my $father = $cgi->param("father");
my $fwiki = WWW::Wikipedia->new();
my $fwikiobj = $wiki->search("$father");
my $fsubjectsummary = $fwikiobj->text();
my @fsubjectwords = ($fsubjectsummary =~ /(\w+)/g);
my $tenfsubjectwords = join ' ', @fsubjectwords[150..153];

#Mother Subject lookup on Wikipedia
my $mother = $cgi->param("mother");
my $mwiki = WWW::Wikipedia->new();
my $mwikiobj = $wiki->search("$mother");
my $msubjectsummary = $fwikiobj->text();
my @msubjectwords = ($msubjectsummary =~ /(\w+)/g);
my $tenmsubjectwords = join ' ', @msubjectwords[30..35];

my @locations = ('in the back of a cab', 'on a plane', 'at home');
my $location = $locations[int rand($#locations)];

my @context1s = ('with friends', 'alone', 'amongst strangers');
my $context1 = $context1s[int rand($#context1s)];

my @context2s = ('while drinking vodka', 'while smoking a cigar', 'while thinking about kissing');
my $context2 = $context2s[int rand($#context2s)];

my @lowhigh = ('LOW', 'HIGH', 'WANTING');
my $lowhigh1 = $lowhigh[int rand($#lowhigh)];
my $lowhigh2 = $lowhigh[int rand($#lowhigh)];
my $lowhigh3 = $lowhigh[int rand($#lowhigh)];
my $lowhigh4 = $lowhigh[int rand($#lowhigh)];


my $x18r = Lingua::Translate->new(src => "en", dest => "de");
my $english = $tenfsubjectwords.$tenplotwords.$tensongwords.$tensubjectwords.$subjectrelated.$tenmsubjectwords;
my $german = $x18r->translate($english);

my $x18r2 = Lingua::Translate->new(src => "de", dest => "en");
my $english2 = $x18r2->translate($german);

my $german2 = $x18r->translate($english2);
my $english3 = $x18r2->translate($german2);

my $stopwords = getStopWords('en');
my @words = ($english3 =~ /(\w+)/g);
my $chosenwords = 10;
my @chosen = (shuffle(@words))[0..$chosenwords-1];
my $displaytext = join ' ', grep { !$stopwords->{$_} } @chosen;

#      Reading of inputs from Engine board to go here

# Best tutorial found so far is at http://arduino.cc/playground/interfacing/PERL

# First initialise all the variables for the values from the switches
# The SE main arduino will be simply constantly sending theses values as a CSV block every few seconds
# This block should be topped and tailed
# Listen for this block of values, add it to a variable, split it along the commas, continue on



#     Logging to go in here



#     Printing to the Arduino driven printer to go here







print "Content-type: text/html\n\n";
print <<EOM;
<html>
<head>
<title>Serendipity Engine, The Prescription</title></head>
<link rel="stylesheet" type="text/css" href="styles.css"/>
<body>
<h1>Your Serendipity Recipe</h1>

<p>Hello, $name. Thank you for using the Serendipity Engine. Based on an analysis of your answers to the questions, plus your selections in the suitcase, the Serendipity Engine has determined that you are $lowhigh1 in social support, $lowhigh2 in creativity, $lowhigh3 in physical well being. You are $lowhigh3 in Head-RAM(tm), $lowhigh1 in attention and $lowhigh2 in access to knowledge. You are $lowhigh1 in Grit.</p>

<p>In addition, the Engine's Human Task Force has identified, based on your portrait and your drawings, your level of personal attractiveness and elegance. A more detailed breakdown of the ingredients of your personal Serendipity recipe can be retrieved at TheSerendipityEngine.com.</p><p>It prescribes the following tailor-made Serendipity Recipe to be considered $location, $context1 $context2:</p>
<h2></h2>

<div id="recipe">
<p>$displaytext</p>
</div>
EOM
exit;