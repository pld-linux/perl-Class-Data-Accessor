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
Version:	0.04004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b5ea49ad12041ac8a7c1c0e111ed67d1
URL:		http://search.cpan.org/dist/Class-Data-Accessor/
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
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Class::Data::Accessor")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/Data/*.pm
%{_mandir}/man3/*
