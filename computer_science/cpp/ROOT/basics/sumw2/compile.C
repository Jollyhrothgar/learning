// Root detects if changes have been made to the source file, and then compiles if so, but
// otherwise loads the library
{
	gROOT->ProcessLine(".L randomnoise.cc++");
	showmethenoise();
}
