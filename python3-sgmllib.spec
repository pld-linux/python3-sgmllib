%define		module		sgmllib
%define		pypi_name	sgmllib3k

Summary:	Py3k port of sgmllib
Name:		python3-%{module}
Version:	1.0.0
Release:	4
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	d70efde06e40797f37e867123aa080ec
URL:		https://pypi.org/project/sgmllib3k/
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Py3k port of sgmllib.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.cpython-*.pyc
%{py3_sitescriptdir}/%{pypi_name}-*.egg-info
