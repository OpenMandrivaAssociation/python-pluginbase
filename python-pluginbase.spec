%global srcname pluginbase

Name:           python-%{srcname}
Version:        1.0.0
Release:        %mkrel 2
Summary:        Support library for building plugins systems
Group:          Development/Python

License:        BSD
URL:            https://github.com/mitsuhiko/pluginbase
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%global _description \
PluginBase is a module for Python that enables the development of flexible\
plugin systems in Python.

%description %{_description}

%package -n python3-%{srcname}
Summary:        Support library for building plugins systems
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}

# Drop bundled egg-info
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%check
pushd tests
  PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v
popd

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*
