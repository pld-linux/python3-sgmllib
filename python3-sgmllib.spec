%define		module		sgmllib
%define		pypi_name	sgmllib3k

Summary:	Py3k port of sgmllib
Summary(pl.UTF-8):	Port py3k biblioteki sgmllib
Name:		python3-%{module}
Version:	1.0.0
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sgmllib3k/
Source0:	https://files.pythonhosted/packages/source/s/sgmllib3k/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	d70efde06e40797f37e867123aa080ec
URL:		https://pypi.org/project/sgmllib3k/
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Py3k port of sgmllib.

%description -l pl.UTF-8
Port py3k biblioteki sgmllib.

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
%{py3_sitescriptdir}/sgmllib.py
%{py3_sitescriptdir}/__pycache__/sgmllib.cpython-*.pyc
%{py3_sitescriptdir}/sgmllib3k-%{version}-py*.egg-info
