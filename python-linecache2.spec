# NOTE: linecache already in standard libraries since 2.?/3.?;
#       linecache 1.0.0 is equivalent of version from cpython 3.5.0 .. 3.7.0 (no changes in this range)
#       so the only point of providing linecache2 1.0.0 for python>=3.5.0 are external dependencies
#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# test target

Summary:	Backport of linecache to older supported Pythons
Summary(pl.UTF-8):	Backport modułu linecache do starszych wersji Pythona
Name:		python-linecache2
Version:	1.0.0
Release:	1
License:	MIT
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/pypi/linecache2/
Source0:	https://files.pythonhosted.org/packages/source/l/linecache2/linecache2-%{version}.tar.gz
# Source0-md5:	7b25d0289ec36bff1f9e63c4329ce65c
URL:		https://github.com/testing-cabal/linecache2
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
%if %{with tests}
BuildRequires:	python-fixtures
BuildRequires:	python-unittest2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
%if %{with tests}
BuildRequires:	python3-fixtures
BuildRequires:	python3-unittest2
%endif
%endif
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backport of linecache to older supported Pythons.

linecache module provides random access to text lines.

%description -l pl.UTF-8
Backport modułu linecache do starszych wersji Pythona.

Moduł linecache pozwala na swobodny dostęp do linii tekstu.

%package -n python3-linecache2
Summary:	Backport of linecache to older supported Pythons
Summary(pl.UTF-8):	Backport modułu linecache do starszych wersji Pythona
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-linecache2
Backport of linecache to older supported Pythons.

linecache module provides random access to text lines.

%description -n python3-linecache2 -l pl.UTF-8
Backport modułu linecache do starszych wersji Pythona.

Moduł linecache pozwala na swobodny dostęp do linii tekstu.

%prep
%setup -q -n linecache2-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/linecache2/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/linecache2/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%dir %{py_sitescriptdir}/linecache2
%{py_sitescriptdir}/linecache2/*.py[co]
%{py_sitescriptdir}/linecache2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-linecache2
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%dir %{py3_sitescriptdir}/linecache2
%{py3_sitescriptdir}/linecache2/*.py
%{py3_sitescriptdir}/linecache2/__pycache__
%{py3_sitescriptdir}/linecache2-%{version}-py*.egg-info
%endif
