#!/usr/bin/perl

# This is a script that a user will input a word of which they only know a portion of the characters.
# Output will be a list of the words matching the requirements input by the user.
#
# Usage: crosswordHelper.pl [input]
#   where input consists of . when a user does not know the character and the known characters are input
#
# Example: crosswordHelper.pl m.n will match man and men.
#
# Author: Andrew Bennett
# Date: 9/25/2014

use strict;
use warnings;

use Path::Class;

# Variables and setup
my $word;

# Read in some user input
# If no input was given ask the user, otherwise roll with it
my $num_args = $#ARGV + 1;
if ($num_args != 1) {
	print "No input given.  Please give a word template that you would like to search for. \n";
	$word = <STDIN>;
} else { 
	$word = $ARGV[0]."\n";
}

# Provide some feedback
print "Searching for words that look like $word";

# Definition of the dictionary file (should be okay on most versions of *nix)
my $dir = dir("/usr/share/dict");
my $file = $dir->file("words");

# Get all the words
my $wordList = $file->slurp();
$word = "\n".$word; # Fixing for the regex to make life easier

# Match the pattern to $wordList and print the results
while ($wordList =~ m/$word/gi) {
	my $match = substr $&, 1;
	print $match;
}
