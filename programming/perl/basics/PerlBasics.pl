#!/usr/local/bin/perl
use strict;
use warnings;
use diagnostics;

#### FirstProgram.pl ####
# Execute this script by typing "perl FirstProgram.pl" in the console.

### Examples - Strings, Print Statents, Lists of Aruments to Prints, Syntax. ###

## Passing an argument to the perl function "print"
print "\n";
print "Hi There!\n";

## Parsing Example - feeding arguments as a list to print, and otherwise odd behavior. ##

# Perl has a large library of functions, which often accept parameters as a list separated by
# commas and terminated with semicolons. Below is an example of feeding parameters to the pring
# function. Also introduced below are the two basic data types supported in perl - numbers,
# literal strings, and intepreted strings.

print "We can output" , " lists",
" of stuff";
print " on multple lines of our text"; print " file\n";
print "In Perl, string are handled as literal, or interpreted.\n";
print "This string is interpreted, special characters like newline:\n and tab:\t affect the format of the stream\n";
print 'This string is literal, no special characters like \n or \t do anything to the stream',"\n";
print "Perl can handle numbers: " , 10000, " ", 45.2293, " etc.\n";

### Variables ###

# Think of functions as verbs, and variables as nouns, within the perl syntax structure.
# perl supports three types of variables:
#	arrays: think of this like a 'list'
#	hashes: think of this like a 'dictionary'
#	scalars: think of this like a 'thing'
# All variable names are a punctuation character, a letter or underscore, and one or 
# more alphanumeric characters or underscores.

## Scalar Examples ##

my $myNumeral = 52;
my $_aString = "Look at me, I'm a String!!!";
my $apple_count = 5;
my $shopping_center = "Ralph's Canyon Crest";

## Using Scalar Variables in print streams

print "The shopping center: $shopping_center currently has $apple_count apples.\n";
# Perl supports multiple levels of this type of behavior.

my $count_report_stores = "$shopping_center has $apple_count apples.";
print "The shopping center: $count_report_stores\n";
print "See? We intepreted with an interpreted string. Note that single quotes break it:\n";
print 'The shopping center: $count_report_stores\n', "\n";

# ++, --, +=, -=, /= and *= are supported for number-style scalars. Careful, though, because
# we can make scalars that look like numbers, but are actually strings. The operations below show
# perl converting all strings to numbers on the fly, and perfomring operations. (Basic math operators
# for multiplication are * and / respectively.

my $mynum1 = 2;
my $mynum2 = '2';
my $mynum3 = "2";
print "Here are some numbers: ", $mynum1, " ", $mynum2, " ", $mynum3, "\n";
print "Here are those numbers, added: ", $mynum1+$mynum2+$mynum3, "\n";

# Concatination - "." puts strings together, "+" adds them.

print "Here are  the three scalars again, concatinated: ";
print $mynum1.$mynum2.$mynum3, "\n";

# string + scalar
print "Here, we attempt a number like string added to a string-like string: ",$_aString+$mynum1, "\n";
# Produced behavior where string-like string was ignored, and only the number results

# string + string literal
print "Here, we attempt a number like string added to a string-like string: ",$_aString+$mynum2, "\n";
# Produced behavior where string-like string was ignored, and only the number results

# string + string
print "Here, we attempt a number like string added to a string-like string: ",$_aString+$mynum3, "\n";
# Produced behavior where string-like string was ignored, and only the number results

# scalar + string
print "Here, we attempt a number like string added to a string-like string: ",$mynum1+$_aString, "\n";
# Produced behavior where string-like string was ignored, and only the number results

# string literal + scalar
print "Here, we attempt a number like string added to a string-like string: ",$mynum2+$_aString, "\n";
# Produced behavior where string-like string was ignored, and only the number results

# string + string
print "Here, we attempt a number like string added to a string-like string: ",$mynum3+$_aString, "\n";
# Produced behavior where string-like string was ignored, and only the number results
