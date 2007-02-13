#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Data-Accessor
Summary:	Class::Data::Accessor - Inheritable, overridable class and instance data accessor creation
Summary(pl.UTF-8):	Class::Data::Accessor - tworzenie dziedzinych, przeciążalnych klas i dostępu do instancji danych
Name:		perl-Class-Data-Accessor
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	81d45455fa45f200c236bfdc38086e96
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Data::Accessor is the marriage of Class::Accessor and
Class::Data::Inheritable into a single module. It is used for creating
accessors to class data that overridable in subclasses as well as in
class instances.

%description -l pl.UTF-8
Class::Data::Accessor to połączenie Class::Accessor i
Class::Data::Inheritable w pojedynczy moduł. Służy do tworzenia metod
dostępu do danych klasy przeciążalnych w podklasach, a także w
instancjach klasy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/Data/*.pm
%{_mandir}/man3/*
