AUTOMAKE_OPTIONS = foreign

AM_CXXFLAGS = -Wall -Werror

BUILT_SOURCES = \
  testexternals.C

AM_CPPFLAGS = \
  -I$(includedir) \
  -I$(OFFLINE_MAIN)/include \
  -I$(ROOTSYS)/include

lib_LTLIBRARIES = \
  libSimpleClass.la

noinst_HEADERS = \
	dontIncludeMe.h

# this can be replaced with a shell command which invokes and captures root-config --libs
libSimpleClass_la_LDFLAGS = \
  -L$(ROOTSYS)/lib `root-config --evelibs` -lRooFitCore -lMinuit -lFoam 

AM_LDFLAGS = \
  -L$(OFFLINE_MAIN)/lib \
  -L$(ROOTSYS)/lib \
  -L$(libdir) 

libSimpleClass_la_SOURCES = \
  SimpleClass.C \
  DictOutput.cxx

noinst_PROGRAMS = \
  testexternals

testexternals_LDADD = \
  libSimpleClass.la

testexternals.C:
	echo "//*** this is a generated file. Do not commit, do not edit" > $@
	echo "int main()" >> $@
	echo "{" >> $@
	echo "  return 0;" >> $@
	echo "}" >> $@

DictOutput.cxx: SimpleClass.h SimpleClassLinkDef.h
	rootcint -f $@ -c $(DEFAULT_INCLUDES) $(AM_CPPFLAGS) $^

clean-local:
	rm -f *Dict.*
