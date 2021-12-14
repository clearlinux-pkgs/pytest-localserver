#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-localserver
Version  : 0.5.1.post0
Release  : 23
URL      : https://files.pythonhosted.org/packages/c3/c8/bd84dba7f73dfd9ff9eff2bbd9037707001ab97c14e78c3af9384c15aa74/pytest-localserver-0.5.1.post0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c3/c8/bd84dba7f73dfd9ff9eff2bbd9037707001ab97c14e78c3af9384c15aa74/pytest-localserver-0.5.1.post0.tar.gz
Summary  : py.test plugin to test server connections locally.
Group    : Development/Tools
License  : MIT
Requires: pytest-localserver-license = %{version}-%{release}
Requires: pytest-localserver-python = %{version}-%{release}
Requires: pytest-localserver-python3 = %{version}-%{release}
Requires: Werkzeug
BuildRequires : Werkzeug
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pypi(werkzeug)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
==================
pytest-localserver
==================
pytest-localserver is a plugin for the `pytest`_ testing framework which enables
you to test server connections locally.

%package license
Summary: license components for the pytest-localserver package.
Group: Default

%description license
license components for the pytest-localserver package.


%package python
Summary: python components for the pytest-localserver package.
Group: Default
Requires: pytest-localserver-python3 = %{version}-%{release}

%description python
python components for the pytest-localserver package.


%package python3
Summary: python3 components for the pytest-localserver package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_localserver)
Requires: pypi(werkzeug)

%description python3
python3 components for the pytest-localserver package.


%prep
%setup -q -n pytest-localserver-0.5.1.post0
cd %{_builddir}/pytest-localserver-0.5.1.post0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639502060
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-localserver
cp %{_builddir}/pytest-localserver-0.5.1.post0/LICENSE %{buildroot}/usr/share/package-licenses/pytest-localserver/6ac85a70f686f54f65aaa4a188eb74e358fa5727
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-localserver/6ac85a70f686f54f65aaa4a188eb74e358fa5727

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
