%define upstream_name	 CDDB
%define upstream_version 1.220

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	A high-level interface to cddb protocol servers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CDDB/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
CDDB is a high-level interface to databases based on the Compact Disc
Database protocol.

Starting with version 1.04, CDDB.pm will contact freedb.org servers by
default. cddb.com's developer license is for end-user applications; not
third-party libraries.  This makes CDDB.pm ineligible for access to
cddb.com servers.  This author will not pursue further cddb.com
access. Developers using CDDB.pm may continue to attempt connections to
cddb.com servers, but there are no guarantees.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README HISTORY
%{perl_vendorlib}/CDDB.pm
%{_mandir}/*/*

