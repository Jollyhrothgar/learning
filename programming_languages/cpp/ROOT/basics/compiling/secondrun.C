// in ROOT:
// .L function.cc++
// function();
{
	gROOT->ProcessLine(".L function.cc+"); // forces recompile, if not compiled.
	function();
}
