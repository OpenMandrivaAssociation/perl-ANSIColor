
%define realname   ANSIColor
%define version    2.00
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Color output using ANSI escape sequences
Source:     http://www.cpan.org/modules/by-module/Term/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

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


