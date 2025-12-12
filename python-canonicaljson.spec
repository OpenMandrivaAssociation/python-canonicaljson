Name:		python-canonicaljson
Version:	2.0.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/c/canonicaljson/canonicaljson-%{version}.tar.gz
Summary:	Canonical JSON
URL:		https://pypi.org/project/canonicaljson/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Canonical JSON

%prep
%autosetup -p1 -n canonicaljson-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/canonicaljson
%{py_sitedir}/canonicaljson-*.*-info
