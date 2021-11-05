#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-deldir
Version  : 1.0.6
Release  : 54
URL      : https://cran.r-project.org/src/contrib/deldir_1.0-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/deldir_1.0-6.tar.gz
Summary  : Delaunay Triangulation and Dirichlet (Voronoi) Tessellation
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-deldir-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
or Voronoi tessellation (with respect to the entire plane) of
	a planar point set. Plots triangulations and tessellations in
	various ways.  Clips tessellations to sub-windows. Calculates
	perimeters of tessellations.  Summarises information about
	the tiles of the tessellation.	Calculates the centroidal
	Voronoi (Dirichlet) tessellation using Lloyd's algorithm.

%package lib
Summary: lib components for the R-deldir package.
Group: Libraries

%description lib
lib components for the R-deldir package.


%prep
%setup -q -c -n deldir
cd %{_builddir}/deldir

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635118206

%install
export SOURCE_DATE_EPOCH=1635118206
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library deldir
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library deldir
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library deldir
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc deldir || :


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
/usr/lib64/R/library/deldir/SavedRatfor/acchk.r
/usr/lib64/R/library/deldir/SavedRatfor/addpt.r
/usr/lib64/R/library/deldir/SavedRatfor/adjchk.r
/usr/lib64/R/library/deldir/SavedRatfor/binsrt.r
/usr/lib64/R/library/deldir/SavedRatfor/circen.r
/usr/lib64/R/library/deldir/SavedRatfor/collincheck.r
/usr/lib64/R/library/deldir/SavedRatfor/cross.r
/usr/lib64/R/library/deldir/SavedRatfor/crossutil.r
/usr/lib64/R/library/deldir/SavedRatfor/delet.r
/usr/lib64/R/library/deldir/SavedRatfor/delet1.r
/usr/lib64/R/library/deldir/SavedRatfor/delout.r
/usr/lib64/R/library/deldir/SavedRatfor/delseg.r
/usr/lib64/R/library/deldir/SavedRatfor/dirout.r
/usr/lib64/R/library/deldir/SavedRatfor/dirseg.r
/usr/lib64/R/library/deldir/SavedRatfor/dldins.r
/usr/lib64/R/library/deldir/SavedRatfor/initad.r
/usr/lib64/R/library/deldir/SavedRatfor/insrt.r
/usr/lib64/R/library/deldir/SavedRatfor/insrt1.r
/usr/lib64/R/library/deldir/SavedRatfor/intri.r
/usr/lib64/R/library/deldir/SavedRatfor/locn.r
/usr/lib64/R/library/deldir/SavedRatfor/master.r
/usr/lib64/R/library/deldir/SavedRatfor/mnnd.r
/usr/lib64/R/library/deldir/SavedRatfor/pred.r
/usr/lib64/R/library/deldir/SavedRatfor/qtest.r
/usr/lib64/R/library/deldir/SavedRatfor/qtest1.r
/usr/lib64/R/library/deldir/SavedRatfor/stoke.r
/usr/lib64/R/library/deldir/SavedRatfor/succ.r
/usr/lib64/R/library/deldir/SavedRatfor/swap.r
/usr/lib64/R/library/deldir/SavedRatfor/testeq.r
/usr/lib64/R/library/deldir/SavedRatfor/triar.r
/usr/lib64/R/library/deldir/SavedRatfor/trifnd.r
/usr/lib64/R/library/deldir/code.discarded/collinChk.R
/usr/lib64/R/library/deldir/code.discarded/collincheck.f
/usr/lib64/R/library/deldir/code.discarded/collincheck.r
/usr/lib64/R/library/deldir/code.discarded/fexitc.c
/usr/lib64/R/library/deldir/code.discarded/fexitf.f
/usr/lib64/R/library/deldir/code.discarded/fexitf.r
/usr/lib64/R/library/deldir/code.discarded/ind.dup.R
/usr/lib64/R/library/deldir/code.discarded/inddup.r
/usr/lib64/R/library/deldir/code.discarded/init.c
/usr/lib64/R/library/deldir/code.discarded/intri.r.save
/usr/lib64/R/library/deldir/code.discarded/triang.list.R.save
/usr/lib64/R/library/deldir/code.discarded/trigraf.c
/usr/lib64/R/library/deldir/code.discarded/trigraf.r
/usr/lib64/R/library/deldir/code.discarded/trigraf1.r.save
/usr/lib64/R/library/deldir/code.discarded/xsucc.f
/usr/lib64/R/library/deldir/data/Rdata.rdb
/usr/lib64/R/library/deldir/data/Rdata.rds
/usr/lib64/R/library/deldir/data/Rdata.rdx
/usr/lib64/R/library/deldir/help/AnIndex
/usr/lib64/R/library/deldir/help/aliases.rds
/usr/lib64/R/library/deldir/help/deldir.rdb
/usr/lib64/R/library/deldir/help/deldir.rdx
/usr/lib64/R/library/deldir/help/macros/defns.Rd
/usr/lib64/R/library/deldir/help/paths.rds
/usr/lib64/R/library/deldir/html/00Index.html
/usr/lib64/R/library/deldir/html/R.css
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
