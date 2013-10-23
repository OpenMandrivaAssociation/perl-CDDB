%define upstream_name	 CDDB
%define upstream_version 1.222

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A high-level interface to cddb protocol servers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/CDDB/CDDB-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:  perl(Mail::Header)
BuildRequires:	perl(HTTP::Request)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc README HISTORY
%{perl_vendorlib}/CDDB.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.220.0-2mdv2011.0
+ Revision: 680660
- mass rebuild

* Mon Mar 08 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.220.0-1mdv2011.0
+ Revision: 515751
- update to 1.220

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.210.0-1mdv2010.0
+ Revision: 408831
- update to 1.21

* Mon Jul 27 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.0
+ Revision: 400633
- update to 1.20
- using %%perl_convert_version
- fixed license field

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.17-7mdv2009.0
+ Revision: 255594
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.17-5mdv2008.1
+ Revision: 136678
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-5mdv2008.0
+ Revision: 86063
- rebuild


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-4mdv2007.0
- Rebuild

* Thu May 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-3mdk
- drop explicit requires, they are optionals

* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.17-2mdk
- Fix SPEC Using perl Policies
	- BuildRequires
	- Source URL

* Mon Mar 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.17-1mdk
- New release 1.17
- drop test patch

* Wed Dec 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-2mdk
- fixed tests (patch 0)

* Tue Sep 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdk
- New release 1.16
- spec cleanup
- make test in %%check

* Thu Oct 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.15-1mdk
- 1.15.
- Trim description. Add test target.

* Tue May 11 2004 Michael Scherer <misc@mandrake.org> 1.12-1mdk
- New release 1.12
- repmbuildupdate aware



