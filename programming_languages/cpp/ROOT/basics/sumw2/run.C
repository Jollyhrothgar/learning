// Root compiles the code into a library, and loads it for use.
{
	gROOT->ProcessLine(".L randomnoise.cc+");
	showmethenoise();
}
