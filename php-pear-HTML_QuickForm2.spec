%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	HTML_QuickForm2
Summary:	%{_pearname} - PHP5 rewrite of HTML_QuickForm package
Summary(pl.UTF-8):	%{_pearname} - przepisany do PHP5 pakiet HTML_QuickForm
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4060974d226f7024a7231079b6c124c5
URL:		http://pear.php.net/package/HTML_QuickForm2/
BuildRequires:	php-pear-PEAR
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTML_Common2 >= 2.0.0-0.beta1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package is expected to offer at least the same functionality as
HTML_QuickForm and work with PHP5 E_STRICT setting.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten w zamierzeniu ma dostarczyć taką samą funkcjonalność jak
pakiet HTML_QuickForm oraz działać z ustawieniem E_STRICT PHP5.

a klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

mv docs/HTML_QuickForm2/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/QuickForm2
%{php_pear_dir}/HTML/QuickForm2.php

%{php_pear_dir}/data/%{_pearname}

%{_examplesdir}/%{name}-%{version}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/HTML_QuickForm2
