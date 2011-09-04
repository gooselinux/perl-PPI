Name:           perl-PPI
Version:        1.206
Release:        4%{?dist}
Summary:        Parse, Analyze and Manipulate Perl

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/PPI/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/PPI-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Perl core modules
BuildRequires:  perl(List::Util) >= 1.20
BuildRequires:  perl(Storable) >= 2.17
BuildRequires:  perl(Test::More) >= 0.86
BuildRequires:  perl(Digest::MD5) >= 2.35
# CPAN modules
BuildRequires:  perl(Clone) >= 0.30
BuildRequires:  perl(File::Remove) >= 1.42
BuildRequires:  perl(IO::String) >= 1.07
BuildRequires:  perl(List::MoreUtils) >= 0.16
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(Test::ClassAPI) >= 1.04
BuildRequires:  perl(Test::NoWarnings) >= 0.084
BuildRequires:  perl(Test::Object) >= 0.07
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::SubCalls) >= 1.07
BuildRequires:  perl(Task::Weaken)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Parse, Analyze and Manipulate Perl (without perl).


%prep
%setup -q -n PPI-%{version}
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
sed -e '/^perl(PPI::.*)$/d'
EOF

%global __perl_provides %{_builddir}/PPI-%{version}/%{name}-prov
chmod +x %{__perl_provides}
iconv -f iso8859-1 -t utf-8 < Changes > Changes.1
mv Changes.1 Changes

chmod -c 644 lib/PPI/Document/File.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README inline2test.conf inline2test.tpl
%{perl_vendorlib}/PPI*
%{_mandir}/man3/*.3pm*


%changelog
* Wed Feb 10 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.206-4
- make rpmlint happy
- Resolves: rhbz#543948

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.206-2
- rebuild against perl 5.10.1

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 1.206-1
- new upstream version
- update build requires

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.203-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.203-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.203-1
- update to 1.203

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.201-3
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.201-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.201-1
- bump to 1.201

* Sat Sep 23 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.118-1
- Update to 1.118.

* Wed Sep  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.117-1
- Update to 1.117.

* Sun Jun  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.115-2
- Removed the perl(IO::Scalar) build requirement.

* Sun Jun  4 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.115-1
- Update to 1.115.

* Wed May 10 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.113-1
- Update to 1.113.

* Tue Apr 25 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.112-1
- Update to 1.112.

* Sat Apr 22 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.111-1
- First build.
