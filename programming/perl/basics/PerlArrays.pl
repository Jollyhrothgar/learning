#!/usr/local/bin/perl

# Arrays are lists of scalars. We index arrays starting at 0. Arrays start with @.
@my_array = (2,5.3,99.272,1,0);
@mixed_array = ("A String", 'A Literal String', 42);

#Print to check filling
print @my_array[4],", ", @mixed_array[0],", ", @mixed_array[1],", ", @mixed_array[2], "\n";

#arrays also created 'on the fly' by using syntax to assign values to arrays.
@another_array[0] = "Look at Me!";

#arrays can be dynamically sized.
@another_array[1] = "1000";

print  @another_array[0], ", ", @another_array[1], ", ", "\n";
