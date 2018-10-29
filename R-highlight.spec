#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-highlight
Version  : 0.4.7.2
Release  : 1
URL      : https://cran.r-project.org/src/contrib/highlight_0.4.7.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/highlight_0.4.7.2.tar.gz
Summary  : Syntax Highlighter
Group    : Development/Tools
License  : GPL-3.0
Requires: R-highlight-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
on the results of the R parser. Rendering in HTML and latex 
	markup. Custom Sweave driver performing syntax highlighting 
	of R code chunks.

%package lib
Summary: lib components for the R-highlight package.
Group: Libraries

%description lib
lib components for the R-highlight package.


%prep
%setup -q -c -n highlight

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540824794

%install
export SOURCE_DATE_EPOCH=1540824794
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library highlight
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library highlight
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library highlight
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library highlight|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/highlight/DESCRIPTION
/usr/lib64/R/library/highlight/INDEX
/usr/lib64/R/library/highlight/Meta/Rd.rds
/usr/lib64/R/library/highlight/Meta/features.rds
/usr/lib64/R/library/highlight/Meta/hsearch.rds
/usr/lib64/R/library/highlight/Meta/links.rds
/usr/lib64/R/library/highlight/Meta/nsInfo.rds
/usr/lib64/R/library/highlight/Meta/package.rds
/usr/lib64/R/library/highlight/NAMESPACE
/usr/lib64/R/library/highlight/NEWS
/usr/lib64/R/library/highlight/R/highlight
/usr/lib64/R/library/highlight/R/highlight.rdb
/usr/lib64/R/library/highlight/R/highlight.rdx
/usr/lib64/R/library/highlight/help/AnIndex
/usr/lib64/R/library/highlight/help/aliases.rds
/usr/lib64/R/library/highlight/help/highlight.rdb
/usr/lib64/R/library/highlight/help/highlight.rdx
/usr/lib64/R/library/highlight/help/paths.rds
/usr/lib64/R/library/highlight/highlight/filetypes.conf
/usr/lib64/R/library/highlight/highlight/langDefs/4gl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/a4c.lang
/usr/lib64/R/library/highlight/highlight/langDefs/abnf.lang
/usr/lib64/R/library/highlight/highlight/langDefs/abp.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ada.lang
/usr/lib64/R/library/highlight/highlight/langDefs/agda.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ahk.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ampl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/amtrix.lang
/usr/lib64/R/library/highlight/highlight/langDefs/applescript.lang
/usr/lib64/R/library/highlight/highlight/langDefs/arc.lang
/usr/lib64/R/library/highlight/highlight/langDefs/arm.lang
/usr/lib64/R/library/highlight/highlight/langDefs/as.lang
/usr/lib64/R/library/highlight/highlight/langDefs/asm.lang
/usr/lib64/R/library/highlight/highlight/langDefs/asp.lang
/usr/lib64/R/library/highlight/highlight/langDefs/aspect.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ats.lang
/usr/lib64/R/library/highlight/highlight/langDefs/au3.lang
/usr/lib64/R/library/highlight/highlight/langDefs/avenue.lang
/usr/lib64/R/library/highlight/highlight/langDefs/awk.lang
/usr/lib64/R/library/highlight/highlight/langDefs/bat.lang
/usr/lib64/R/library/highlight/highlight/langDefs/bb.lang
/usr/lib64/R/library/highlight/highlight/langDefs/bbcode.lang
/usr/lib64/R/library/highlight/highlight/langDefs/bib.lang
/usr/lib64/R/library/highlight/highlight/langDefs/bms.lang
/usr/lib64/R/library/highlight/highlight/langDefs/bnf.lang
/usr/lib64/R/library/highlight/highlight/langDefs/boo.lang
/usr/lib64/R/library/highlight/highlight/langDefs/c.lang
/usr/lib64/R/library/highlight/highlight/langDefs/cb.lang
/usr/lib64/R/library/highlight/highlight/langDefs/cfc.lang
/usr/lib64/R/library/highlight/highlight/langDefs/chl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/clipper.lang
/usr/lib64/R/library/highlight/highlight/langDefs/clojure.lang
/usr/lib64/R/library/highlight/highlight/langDefs/clp.lang
/usr/lib64/R/library/highlight/highlight/langDefs/cob.lang
/usr/lib64/R/library/highlight/highlight/langDefs/cs.lang
/usr/lib64/R/library/highlight/highlight/langDefs/css.lang
/usr/lib64/R/library/highlight/highlight/langDefs/d.lang
/usr/lib64/R/library/highlight/highlight/langDefs/diff.lang
/usr/lib64/R/library/highlight/highlight/langDefs/dot.lang
/usr/lib64/R/library/highlight/highlight/langDefs/dylan.lang
/usr/lib64/R/library/highlight/highlight/langDefs/e.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ebnf.lang
/usr/lib64/R/library/highlight/highlight/langDefs/erl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/euphoria.lang
/usr/lib64/R/library/highlight/highlight/langDefs/exp.lang
/usr/lib64/R/library/highlight/highlight/langDefs/f77.lang
/usr/lib64/R/library/highlight/highlight/langDefs/f90.lang
/usr/lib64/R/library/highlight/highlight/langDefs/flx.lang
/usr/lib64/R/library/highlight/highlight/langDefs/frink.lang
/usr/lib64/R/library/highlight/highlight/langDefs/fs.lang
/usr/lib64/R/library/highlight/highlight/langDefs/go.lang
/usr/lib64/R/library/highlight/highlight/langDefs/haskell.lang
/usr/lib64/R/library/highlight/highlight/langDefs/hcl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/html.lang
/usr/lib64/R/library/highlight/highlight/langDefs/httpd.lang
/usr/lib64/R/library/highlight/highlight/langDefs/hx.lang
/usr/lib64/R/library/highlight/highlight/langDefs/icl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/icn.lang
/usr/lib64/R/library/highlight/highlight/langDefs/idl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/idlang.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ili.lang
/usr/lib64/R/library/highlight/highlight/langDefs/inc_luatex.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ini.lang
/usr/lib64/R/library/highlight/highlight/langDefs/inp.lang
/usr/lib64/R/library/highlight/highlight/langDefs/io.lang
/usr/lib64/R/library/highlight/highlight/langDefs/iss.lang
/usr/lib64/R/library/highlight/highlight/langDefs/j.lang
/usr/lib64/R/library/highlight/highlight/langDefs/java.lang
/usr/lib64/R/library/highlight/highlight/langDefs/js.lang
/usr/lib64/R/library/highlight/highlight/langDefs/jsp.lang
/usr/lib64/R/library/highlight/highlight/langDefs/lbn.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ldif.lang
/usr/lib64/R/library/highlight/highlight/langDefs/lgt.lang
/usr/lib64/R/library/highlight/highlight/langDefs/lhs.lang
/usr/lib64/R/library/highlight/highlight/langDefs/lisp.lang
/usr/lib64/R/library/highlight/highlight/langDefs/lotos.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ls.lang
/usr/lib64/R/library/highlight/highlight/langDefs/lsl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/lua.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ly.lang
/usr/lib64/R/library/highlight/highlight/langDefs/m.lang
/usr/lib64/R/library/highlight/highlight/langDefs/make.lang
/usr/lib64/R/library/highlight/highlight/langDefs/mel.lang
/usr/lib64/R/library/highlight/highlight/langDefs/mercury.lang
/usr/lib64/R/library/highlight/highlight/langDefs/mib.lang
/usr/lib64/R/library/highlight/highlight/langDefs/miranda.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ml.lang
/usr/lib64/R/library/highlight/highlight/langDefs/mo.lang
/usr/lib64/R/library/highlight/highlight/langDefs/mod2.lang
/usr/lib64/R/library/highlight/highlight/langDefs/mod3.lang
/usr/lib64/R/library/highlight/highlight/langDefs/mpl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ms.lang
/usr/lib64/R/library/highlight/highlight/langDefs/mssql.lang
/usr/lib64/R/library/highlight/highlight/langDefs/n.lang
/usr/lib64/R/library/highlight/highlight/langDefs/nas.lang
/usr/lib64/R/library/highlight/highlight/langDefs/nbc.lang
/usr/lib64/R/library/highlight/highlight/langDefs/nice.lang
/usr/lib64/R/library/highlight/highlight/langDefs/nrx.lang
/usr/lib64/R/library/highlight/highlight/langDefs/nsi.lang
/usr/lib64/R/library/highlight/highlight/langDefs/nut.lang
/usr/lib64/R/library/highlight/highlight/langDefs/nxc.lang
/usr/lib64/R/library/highlight/highlight/langDefs/oberon.lang
/usr/lib64/R/library/highlight/highlight/langDefs/objc.lang
/usr/lib64/R/library/highlight/highlight/langDefs/octave.lang
/usr/lib64/R/library/highlight/highlight/langDefs/oorexx.lang
/usr/lib64/R/library/highlight/highlight/langDefs/os.lang
/usr/lib64/R/library/highlight/highlight/langDefs/oz.lang
/usr/lib64/R/library/highlight/highlight/langDefs/pas.lang
/usr/lib64/R/library/highlight/highlight/langDefs/php.lang
/usr/lib64/R/library/highlight/highlight/langDefs/pike.lang
/usr/lib64/R/library/highlight/highlight/langDefs/pl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/pl1.lang
/usr/lib64/R/library/highlight/highlight/langDefs/pov.lang
/usr/lib64/R/library/highlight/highlight/langDefs/pro.lang
/usr/lib64/R/library/highlight/highlight/langDefs/progress.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ps.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ps1.lang
/usr/lib64/R/library/highlight/highlight/langDefs/psl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/pure.lang
/usr/lib64/R/library/highlight/highlight/langDefs/py.lang
/usr/lib64/R/library/highlight/highlight/langDefs/pyx.lang
/usr/lib64/R/library/highlight/highlight/langDefs/q.lang
/usr/lib64/R/library/highlight/highlight/langDefs/qmake.lang
/usr/lib64/R/library/highlight/highlight/langDefs/qu.lang
/usr/lib64/R/library/highlight/highlight/langDefs/r.lang
/usr/lib64/R/library/highlight/highlight/langDefs/rb.lang
/usr/lib64/R/library/highlight/highlight/langDefs/rebol.lang
/usr/lib64/R/library/highlight/highlight/langDefs/rexx.lang
/usr/lib64/R/library/highlight/highlight/langDefs/rnc.lang
/usr/lib64/R/library/highlight/highlight/langDefs/s.lang
/usr/lib64/R/library/highlight/highlight/langDefs/sas.lang
/usr/lib64/R/library/highlight/highlight/langDefs/sc.lang
/usr/lib64/R/library/highlight/highlight/langDefs/scala.lang
/usr/lib64/R/library/highlight/highlight/langDefs/scilab.lang
/usr/lib64/R/library/highlight/highlight/langDefs/sh.lang
/usr/lib64/R/library/highlight/highlight/langDefs/sma.lang
/usr/lib64/R/library/highlight/highlight/langDefs/smalltalk.lang
/usr/lib64/R/library/highlight/highlight/langDefs/sml.lang
/usr/lib64/R/library/highlight/highlight/langDefs/sno.lang
/usr/lib64/R/library/highlight/highlight/langDefs/spec.lang
/usr/lib64/R/library/highlight/highlight/langDefs/spn.lang
/usr/lib64/R/library/highlight/highlight/langDefs/sql.lang
/usr/lib64/R/library/highlight/highlight/langDefs/sybase.lang
/usr/lib64/R/library/highlight/highlight/langDefs/tcl.lang
/usr/lib64/R/library/highlight/highlight/langDefs/tcsh.lang
/usr/lib64/R/library/highlight/highlight/langDefs/test_re.lang
/usr/lib64/R/library/highlight/highlight/langDefs/tex.lang
/usr/lib64/R/library/highlight/highlight/langDefs/ttcn3.lang
/usr/lib64/R/library/highlight/highlight/langDefs/txt.lang
/usr/lib64/R/library/highlight/highlight/langDefs/vala.lang
/usr/lib64/R/library/highlight/highlight/langDefs/vb.lang
/usr/lib64/R/library/highlight/highlight/langDefs/verilog.lang
/usr/lib64/R/library/highlight/highlight/langDefs/vhd.lang
/usr/lib64/R/library/highlight/highlight/langDefs/xml.lang
/usr/lib64/R/library/highlight/highlight/langDefs/xpp.lang
/usr/lib64/R/library/highlight/highlight/langDefs/y.lang
/usr/lib64/R/library/highlight/highlight/langDefs/yaiff.lang
/usr/lib64/R/library/highlight/highlight/langDefs/znn.lang
/usr/lib64/R/library/highlight/highlight/themes/acid.style
/usr/lib64/R/library/highlight/highlight/themes/bipolar.style
/usr/lib64/R/library/highlight/highlight/themes/blacknblue.style
/usr/lib64/R/library/highlight/highlight/themes/bright.style
/usr/lib64/R/library/highlight/highlight/themes/contrast.style
/usr/lib64/R/library/highlight/highlight/themes/darkblue.style
/usr/lib64/R/library/highlight/highlight/themes/darkness.style
/usr/lib64/R/library/highlight/highlight/themes/desert.style
/usr/lib64/R/library/highlight/highlight/themes/easter.style
/usr/lib64/R/library/highlight/highlight/themes/emacs.style
/usr/lib64/R/library/highlight/highlight/themes/golden.style
/usr/lib64/R/library/highlight/highlight/themes/greenlcd.style
/usr/lib64/R/library/highlight/highlight/themes/ide-anjuta.style
/usr/lib64/R/library/highlight/highlight/themes/ide-codewarrior.style
/usr/lib64/R/library/highlight/highlight/themes/ide-eclipse.style
/usr/lib64/R/library/highlight/highlight/themes/ide-kdev.style
/usr/lib64/R/library/highlight/highlight/themes/ide-msvs2008.style
/usr/lib64/R/library/highlight/highlight/themes/ide-xcode.style
/usr/lib64/R/library/highlight/highlight/themes/jedit.style
/usr/lib64/R/library/highlight/highlight/themes/kwrite.style
/usr/lib64/R/library/highlight/highlight/themes/lucretia.style
/usr/lib64/R/library/highlight/highlight/themes/matlab.style
/usr/lib64/R/library/highlight/highlight/themes/moe.style
/usr/lib64/R/library/highlight/highlight/themes/navy.style
/usr/lib64/R/library/highlight/highlight/themes/nedit.style
/usr/lib64/R/library/highlight/highlight/themes/neon.style
/usr/lib64/R/library/highlight/highlight/themes/night.style
/usr/lib64/R/library/highlight/highlight/themes/orion.style
/usr/lib64/R/library/highlight/highlight/themes/pablo.style
/usr/lib64/R/library/highlight/highlight/themes/peachpuff.style
/usr/lib64/R/library/highlight/highlight/themes/print.style
/usr/lib64/R/library/highlight/highlight/themes/rand01.style
/usr/lib64/R/library/highlight/highlight/themes/seashell.style
/usr/lib64/R/library/highlight/highlight/themes/the.style
/usr/lib64/R/library/highlight/highlight/themes/typical.style
/usr/lib64/R/library/highlight/highlight/themes/vampire.style
/usr/lib64/R/library/highlight/highlight/themes/vim-dark.style
/usr/lib64/R/library/highlight/highlight/themes/vim.style
/usr/lib64/R/library/highlight/highlight/themes/whitengrey.style
/usr/lib64/R/library/highlight/highlight/themes/zellner.style
/usr/lib64/R/library/highlight/html/00Index.html
/usr/lib64/R/library/highlight/html/R.css
/usr/lib64/R/library/highlight/libs/symbols.rds
/usr/lib64/R/library/highlight/stylesheet/default.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/highlight/libs/highlight.so
/usr/lib64/R/library/highlight/libs/highlight.so.avx2
/usr/lib64/R/library/highlight/libs/highlight.so.avx512
