%define		status		stable
%define		pearname	HTML_QuickForm2
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - PHP5 rewrite of HTML_QuickForm package
Summary(pl.UTF-8):	%{pearname} - przepisany do PHP5 pakiet HTML_QuickForm
Name:		php-pear-%{pearname}
Version:	2.0.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	a2c0e3dd45559e8527618515440cde93
URL:		http://pear.php.net/package/HTML_QuickForm2/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-HTML_Common2 >= 2.0.0-0.beta1
Obsoletes:	php-pear-HTML_QuickForm2-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package is expected to offer at least the same functionality as
HTML_QuickForm and work with PHP5 E_STRICT setting.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Pakiet ten w zamierzeniu ma dostarczyć taką samą funkcjonalność jak
pakiet HTML_QuickForm oraz działać z ustawieniem E_STRICT PHP5.

a klasa ma w PEAR status: %{status}.

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

%{php_pear_dir}/data/%{pearname}

%{_examplesdir}/%{name}-%{version}
