#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-deldir
Version  : 0.1.15
Release  : 4
URL      : https://cran.r-project.org/src/contrib/deldir_0.1-15.tar.gz
Source0  : https://cran.r-project.org/src/contrib/deldir_0.1-15.tar.gz
Summary  : Delaunay Triangulation and Dirichlet (Voronoi) Tessellation
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-deldir-lib
BuildRequires : clr-R-helpers

%description
or Voronoi tessellation (with respect to the entire plane) of
	a planar point set. Plots triangulations and tessellations in
	various ways.  Clips tessellations to sub-windows. Calculates
	perimeters of tessellations.  Summarises information about the
	tiles of the tessellation.

%package lib
Summary: lib components for the R-deldir package.
Group: Libraries

%description lib
lib components for the R-deldir package.


%prep
%setup -q -c -n deldir

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523299131

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523299131
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library deldir
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library deldir
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library deldir
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library deldir|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/deldir/DESCRIPTION
/usr/lib64/R/library/deldir/INDEX
/usr/lib64/R/library/deldir/Meta/Rd.rds
/usr/lib64/R/library/deldir/Meta/data.rds
/usr/lib64/R/library/deldir/Meta/features.rds
/usr/lib64/R/library/deldir/Meta/hsearch.rds
/usr/lib64/R/library/deldir/Meta/links.rds
/usr/lib64/R/library/deldir/Meta/nsInfo.rds
/usr/lib64/R/library/deldir/Meta/package.rds
/usr/lib64/R/library/deldir/NAMESPACE
/usr/lib64/R/library/deldir/R/deldir
/usr/lib64/R/library/deldir/R/deldir.rdb
/usr/lib64/R/library/deldir/R/deldir.rdx
/usr/lib64/R/library/deldir/READ_ME
/usr/lib64/R/library/deldir/code.discarded/ind.dup.R
/usr/lib64/R/library/deldir/code.discarded/inddup.r
/usr/lib64/R/library/deldir/code.discarded/intri.r.save
/usr/lib64/R/library/deldir/code.discarded/triang.list.R.save
/usr/lib64/R/library/deldir/code.discarded/trigraf.c
/usr/lib64/R/library/deldir/code.discarded/trigraf.r
/usr/lib64/R/library/deldir/code.discarded/trigraf1.r.save
/usr/lib64/R/library/deldir/data/Rdata.rdb
/usr/lib64/R/library/deldir/data/Rdata.rds
/usr/lib64/R/library/deldir/data/Rdata.rdx
/usr/lib64/R/library/deldir/err.list
/usr/lib64/R/library/deldir/ex.out
/usr/lib64/R/library/deldir/help/AnIndex
/usr/lib64/R/library/deldir/help/aliases.rds
/usr/lib64/R/library/deldir/help/deldir.rdb
/usr/lib64/R/library/deldir/help/deldir.rdx
/usr/lib64/R/library/deldir/help/paths.rds
/usr/lib64/R/library/deldir/html/00Index.html
/usr/lib64/R/library/deldir/html/R.css
/usr/lib64/R/library/deldir/libs/symbols.rds
/usr/lib64/R/library/deldir/ratfor/acchk.r
/usr/lib64/R/library/deldir/ratfor/addpt.r
/usr/lib64/R/library/deldir/ratfor/adjchk.r
/usr/lib64/R/library/deldir/ratfor/binsrt.r
/usr/lib64/R/library/deldir/ratfor/circen.r
/usr/lib64/R/library/deldir/ratfor/cross.r
/usr/lib64/R/library/deldir/ratfor/delet.r
/usr/lib64/R/library/deldir/ratfor/delet1.r
/usr/lib64/R/library/deldir/ratfor/delout.r
/usr/lib64/R/library/deldir/ratfor/delseg.r
/usr/lib64/R/library/deldir/ratfor/dirout.r
/usr/lib64/R/library/deldir/ratfor/dirseg.r
/usr/lib64/R/library/deldir/ratfor/dldins.r
/usr/lib64/R/library/deldir/ratfor/initad.r
/usr/lib64/R/library/deldir/ratfor/insrt.r
/usr/lib64/R/library/deldir/ratfor/insrt1.r
/usr/lib64/R/library/deldir/ratfor/intri.r
/usr/lib64/R/library/deldir/ratfor/locn.r
/usr/lib64/R/library/deldir/ratfor/makefor
/usr/lib64/R/library/deldir/ratfor/master.r
/usr/lib64/R/library/deldir/ratfor/mnnd.r
/usr/lib64/R/library/deldir/ratfor/pred.r
/usr/lib64/R/library/deldir/ratfor/qtest.r
/usr/lib64/R/library/deldir/ratfor/qtest1.r
/usr/lib64/R/library/deldir/ratfor/stoke.r
/usr/lib64/R/library/deldir/ratfor/succ.r
/usr/lib64/R/library/deldir/ratfor/swap.r
/usr/lib64/R/library/deldir/ratfor/testeq.r
/usr/lib64/R/library/deldir/ratfor/triar.r
/usr/lib64/R/library/deldir/ratfor/trifnd.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/deldir/libs/deldir.so
/usr/lib64/R/library/deldir/libs/deldir.so.avx2
/usr/lib64/R/library/deldir/libs/deldir.so.avx512
