%define upstream_name    ANSIColor
%define upstream_version 3.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Color output using ANSI escape sequences
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module has two interfaces, one through color() and colored() and the
other through constants. It also offers the utility function uncolor(),
which has to be explicitly imported to be used (see the /SYNOPSIS manpage).

color() takes any number of strings as arguments and considers them to be
space-separated lists of attributes. It then forms and returns the escape
sequence to set those attributes. It doesn't print it out, just returns it,
so you'll have to print it yourself if you want to (this is so that you can
save it as a string, pass it to something else, send it to a file handle,
or do anything else with it that you might care to).

uncolor() performs the opposite translation, turning escape sequences into
a list of strings.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README ChangeLog README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 3.0.0-4mdv2011.0
+ Revision: 656880
- rebuild for updated spec-helper

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 3.0.0-3mdv2011.0
+ Revision: 597200
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 3.0.0-2mdv2011.0
+ Revision: 562436
- rebuild

* Mon Jan 25 2010 Jérôme Quelin <jquelin@mandriva.org> 3.0.0-1mdv2011.0
+ Revision: 495700
- update to 3.00

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 2.20.0-1mdv2010.0
+ Revision: 422879
- update to 2.02

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 2.10.0-2mdv2010.0
+ Revision: 420983
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.10.0-1mdv2010.0
+ Revision: 401788
- rebuild using %%perl_convert_version
- fixed license field

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2010.0
+ Revision: 392983
- update to new version 2.01

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 2.00-2mdv2010.0
+ Revision: 375972
- rebuild

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.00-1mdv2010.0
+ Revision: 372414
- import perl-ANSIColor


* Wed May 06 2009 cpan2dist 2.00-1mdv
- initial mdv release, generated with cpan2dist

