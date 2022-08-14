#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pydot_ng
Version  : 2.0.0
Release  : 46
URL      : https://files.pythonhosted.org/packages/60/7a/d4022ba8b47d8f5e4c58b285e66eb233745f46f07bd7e6569a695fc91e7f/pydot_ng-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/60/7a/d4022ba8b47d8f5e4c58b285e66eb233745f46f07bd7e6569a695fc91e7f/pydot_ng-2.0.0.tar.gz
Summary  : Python interface to Graphviz's Dot
Group    : Development/Tools
License  : MIT
Requires: pypi-pydot_ng-license = %{version}-%{release}
Requires: pypi-pydot_ng-python = %{version}-%{release}
Requires: pypi-pydot_ng-python3 = %{version}-%{release}
Requires: graphviz
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(pyparsing)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
---------------------------------------------------
        Ero Carrera (c) 2004-2007
        
        ero@dkbza.org
        
        This code is distributed under the MIT license.

%package license
Summary: license components for the pypi-pydot_ng package.
Group: Default

%description license
license components for the pypi-pydot_ng package.


%package python
Summary: python components for the pypi-pydot_ng package.
Group: Default
Requires: pypi-pydot_ng-python3 = %{version}-%{release}

%description python
python components for the pypi-pydot_ng package.


%package python3
Summary: python3 components for the pypi-pydot_ng package.
Group: Default
Requires: python3-core
Provides: pypi(pydot_ng)
Requires: pypi(pyparsing)

%description python3
python3 components for the pypi-pydot_ng package.


%prep
%setup -q -n pydot_ng-2.0.0
cd %{_builddir}/pydot_ng-2.0.0
pushd ..
cp -a pydot_ng-2.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656397696
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pydot_ng
cp %{_builddir}/pydot_ng-2.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pydot_ng/e38c1f7359ea268ce9ecd751f3fd9787fb2d40db
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pydot_ng/e38c1f7359ea268ce9ecd751f3fd9787fb2d40db

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
