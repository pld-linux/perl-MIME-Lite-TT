#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	MIME
%define		pnam	Lite-TT
Summary:	MIME::Lite::TT - TT enabled MIME::Lite wrapper
#Summary(pl.UTF-8):	
Name:		perl-MIME-Lite-TT
Version:	0.02
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82ac8e6dd4b0274ce552d5d2ace23eb4
URL:		http://search.cpan.org/dist/MIME-Lite-TT/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(MIME::Lite)
BuildRequires:	perl-Template-Toolkit
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::Lite::TT is the wrapper of MIME::Lite which enabled
Template::Toolkit as a template of email.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/MIME/Lite
%{perl_vendorlib}/MIME/Lite/*.pm
%{_mandir}/man3/*
