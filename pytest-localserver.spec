#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-localserver
Version  : tip
Release  : 3
URL      : https://bitbucket.org/pytest-dev/pytest-localserver/get/tip.tar.gz
Source0  : https://bitbucket.org/pytest-dev/pytest-localserver/get/tip.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: pytest-localserver-license = %{version}-%{release}
Requires: pytest-localserver-python = %{version}-%{release}
Requires: pytest-localserver-python3 = %{version}-%{release}
BuildRequires : Werkzeug
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
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

%description python3
python3 components for the pytest-localserver package.


%prep
%setup -q -n pytest-dev-pytest-localserver-25bcc0df2252

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549036374
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-localserver
cp LICENSE %{buildroot}/usr/share/package-licenses/pytest-localserver/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-localserver/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
