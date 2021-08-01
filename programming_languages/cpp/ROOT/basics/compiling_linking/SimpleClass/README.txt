This tutorial demonstrates compiling a project using autotools in order to
create a shared-object library which can be loaded in ROOT. Objects in a shared
object library can be instantiated interactively, and run at the speed of
compiled code.

This code is setup to build in the standard PHENIX way, using "autogen.sh" to
run the configure.ac file, check for dependancies, and create a custom Makefile.

To install, cd to build/ and run:

../src/autogen.sh --prefix=$MYINSTALL (if you have $MYINSTALL defined)

or

../src/autogen.sh --prefix=$PWD/../lib/

To build your code into a library, then run:

make install

And load the library normally.
