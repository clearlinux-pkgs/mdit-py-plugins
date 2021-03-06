#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mdit-py-plugins
Version  : 0.2.8
Release  : 1
URL      : https://files.pythonhosted.org/packages/10/a0/2d3df3cd0c55b4024d153b31b403e02a1af50d78df3a2fb22190100a7004/mdit-py-plugins-0.2.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/10/a0/2d3df3cd0c55b4024d153b31b403e02a1af50d78df3a2fb22190100a7004/mdit-py-plugins-0.2.8.tar.gz
Summary  : Collection of plugins for markdown-it-py
Group    : Development/Tools
License  : MIT
Requires: mdit-py-plugins-license = %{version}-%{release}
Requires: mdit-py-plugins-python = %{version}-%{release}
Requires: mdit-py-plugins-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(coverage)
BuildRequires : pypi(pre_commit)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
[![Github-CI][github-ci]][github-link]
        [![Coverage Status][codecov-badge]][codecov-link]
        [![PyPI][pypi-badge]][pypi-link]
        [![Conda][conda-badge]][conda-link]

%package license
Summary: license components for the mdit-py-plugins package.
Group: Default

%description license
license components for the mdit-py-plugins package.


%package python
Summary: python components for the mdit-py-plugins package.
Group: Default
Requires: mdit-py-plugins-python3 = %{version}-%{release}

%description python
python components for the mdit-py-plugins package.


%package python3
Summary: python3 components for the mdit-py-plugins package.
Group: Default
Requires: python3-core
Provides: pypi(mdit_py_plugins)
Requires: pypi(markdown_it_py)

%description python3
python3 components for the mdit-py-plugins package.


%prep
%setup -q -n mdit-py-plugins-0.2.8
cd %{_builddir}/mdit-py-plugins-0.2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637342206
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mdit-py-plugins
cp %{_builddir}/mdit-py-plugins-0.2.8/LICENSE %{buildroot}/usr/share/package-licenses/mdit-py-plugins/ab5a711cce75e49bdbd08bbcb728262e30580e5d
cp %{_builddir}/mdit-py-plugins-0.2.8/mdit_py_plugins/container/LICENSE %{buildroot}/usr/share/package-licenses/mdit-py-plugins/69fcf444c57897f60cc8189191798d32ace634f8
cp %{_builddir}/mdit-py-plugins-0.2.8/mdit_py_plugins/deflist/LICENSE %{buildroot}/usr/share/package-licenses/mdit-py-plugins/26e00dbad9e333aeec5c446047d7b5489e2d3c6b
cp %{_builddir}/mdit-py-plugins-0.2.8/mdit_py_plugins/footnote/LICENSE %{buildroot}/usr/share/package-licenses/mdit-py-plugins/26e00dbad9e333aeec5c446047d7b5489e2d3c6b
cp %{_builddir}/mdit-py-plugins-0.2.8/mdit_py_plugins/front_matter/LICENSE %{buildroot}/usr/share/package-licenses/mdit-py-plugins/752f88468d4c37d8f9d97b8e4031d92bdfe8e501
cp %{_builddir}/mdit-py-plugins-0.2.8/mdit_py_plugins/texmath/LICENSE %{buildroot}/usr/share/package-licenses/mdit-py-plugins/78a8778ee015c0603f4f0a9cd2cfe8c95ce791b0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mdit-py-plugins/26e00dbad9e333aeec5c446047d7b5489e2d3c6b
/usr/share/package-licenses/mdit-py-plugins/69fcf444c57897f60cc8189191798d32ace634f8
/usr/share/package-licenses/mdit-py-plugins/752f88468d4c37d8f9d97b8e4031d92bdfe8e501
/usr/share/package-licenses/mdit-py-plugins/78a8778ee015c0603f4f0a9cd2cfe8c95ce791b0
/usr/share/package-licenses/mdit-py-plugins/ab5a711cce75e49bdbd08bbcb728262e30580e5d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
