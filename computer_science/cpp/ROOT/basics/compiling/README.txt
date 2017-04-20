function.cc:

#include "function.h"

void function(void)
{
	  std::cout << "hello world\n";
}


function.h:

#ifndef function_h
#define function_h

#include <iostream>

#endif



in ROOT:
.L function.cc++
function();

or:

gROOT->ProcessLine(".L function.cc++"); // forces recompile, if not compiled.

You can also do
gROOT->ProcessLine(".L function.cc+"); // usefull if the code already compiled (in theory if not compiled, it'll compile anyway.)

which will only compile if the library doesn't already exist, but sometimes this does not work well for me.
