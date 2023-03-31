%global srcname pluginbase

Name:           python-%{srcname}
Version:        1.0.1
Release:        2
Summary:        Support library for building plugins systems
Group:          Development/Python

License:        BSD
URL:            https://github.com/mitsuhiko/pluginbase
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)

%description
PluginBase is a module for Python that enables the development of flexible\
plugin systems in Python.

%prep
%autosetup -n %{srcname}-%{version}

# Drop bundled egg-info
rm -rf *.egg-info

%build
%py_build

%install
%py_install

%files
%license LICENSE
%{python_sitelib}/%{srcname}-*.egg-info/
%{python_sitelib}/%{srcname}.py
%{python_sitelib}/__pycache__/%{srcname}.*
