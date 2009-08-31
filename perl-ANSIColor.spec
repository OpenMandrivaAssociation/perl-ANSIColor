%define upstream_name    ANSIColor
%define upstream_version 2.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Color output using ANSI escape sequences
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README ChangeLog README
%{_mandir}/man3/*
%perl_vendorlib/*
