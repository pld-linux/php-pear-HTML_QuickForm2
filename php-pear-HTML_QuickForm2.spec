%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	QuickForm2
%define		_status		alpha
%define		_pearname	HTML_QuickForm2
Summary:	%{_pearname} - PHP5 rewrite of HTML_QuickForm package
Summary(pl.UTF-8):	%{_pearname} - przepisany do PHP5 pakiet HTML_QuickForm
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	de91b8f00f732c8a7bc993e5d423abb1
URL:		http://pear.php.net/package/HTML_QuickForm2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTML_Common2 >= 0.3.0
Requires:	php-pear-PEAR >= 1.4.3
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
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%if 0
%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi
%endif

%files
%defattr(644,root,root,755)
%doc install.log docs/HTML_QuickForm2/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/QuickForm2
%{php_pear_dir}/HTML/QuickForm2.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/HTML_QuickForm2
