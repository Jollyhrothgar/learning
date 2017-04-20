use strict; # use - this is a perl pragma - it tells the perl compiler to do something.
use warnings;
use diagnostics;

# sigils: define type - $-> scalar, @->array, %->hash, these are our availble variable types
# scalars may contain: undef, number, string types, or a reference to another variable.
# it is impossible/irrelevant to determine if a scalar contains a number or string - the operator
# determines how it is used.

# Avoid problems with numbers and scalars, by separating number operators from scalar operators.
# Numerical operators:  <,  >, <=, >=, ==, !=, <=>
# String operators:    lt, gt, le, ge, eq, ne, cmp

# Columns are equivalent operators.

#No boolean operators. The following statements evaluate as "false" in if statements:
# A scalar evaluates, in if statement, to 'false' if it is:
# undef, number 0, string "", string "0". **remember, just numbers and strings.

# When perl returns "true" it is usually the number "1" and when it returns false, it is usually
# an empty string "".

# When a value is retrieved from an array, we use $, since that value is a scaler, rather than an
# array (precluding an array of arrays...)... and negative access numbers to write out values
# starting from the end...

my @array = ("Print", "these", "strings", "out", "for", "me",); # trailing comma is OK
print $array[0], "\n";
print $array[1], "\n";
print $array[2], "\n";
print $array[3], "\n";
print $array[4], "\n";
print $array[5], "\n";

print $array[-1 ], "\n";
print $array[-2], "\n";
print $array[-3], "\n";
print $array[-4], "\n";
print $array[-5], "\n";
print $array[-6], "\n";

# get an array's length:

print "This array has ", (scalar @array), " elements", "\n"; # Access number of array elements
print "The index populated was ", $#array, "\n"; # Get the last populated index

#concatination:
print $array[0].$array[1].$array[2], "\n";
# concatination via passing many arguments to print.
print @array,"\n";
# handle sigils within strings carefully. You can use a string literal, such as:
print 'michael.beaumier@gmail.com' , "\n";
# or by using the escape sigil \.
print "michael.beaumier\@gmail.com" , "\n";


# hash variables are similar to arrays, but different in the following way:
# this structure is also similar to php structures called "arrays".
# hash variables are indexed by string. Here is an example:
my %scientists = (
		"Newton"   => "Isaac",
		"Einstein" => "Albert",
		"Darwin"   => "Charles",
		);
# Notice how similar this declaration is to an array declaration. In fact, the double arrow 
# symbol => is called a "fat comma", because it is just a synonym for the comma separator. 
# A hash is merely a list with an even number of elements, where the even-numbered elements 
# (0, 2, ...) are all considered as strings.

# Remember, values retrieved are scalars, rather than hashes, in this case, so the access
# sigil is a $ rather than an % or @. A hash is an object that has a "key" and a "value".
# there is no 1-1 between a hash and an array, since an array would have twice as many
# entries to store both the key and value. There is no collision between an array, @hash
# and an actual hash, %hash.
