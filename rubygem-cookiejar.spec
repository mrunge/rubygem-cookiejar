%global gem_name cookiejar

Name: rubygem-%{gem_name}
Version: 0.3.3
Release: 1%{?dist}
Summary: Parsing and returning cookies in Ruby
Group: Development/Languages
License: BSD
URL: https://github.com/dwaite/cookiejar
Source0: https://rubygems.org/gems/cookiejar-%{version}.gem
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rspec-core)
BuildRequires: rubygem(rspec-mocks)
BuildRequires: rubygem(rspec-expectations)
BuildRequires: rubygem(rspec-collection_matchers)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildArch: noarch
%if 0%{?fc19} || 0%{?fc20} || 0%{?rhel} <= 7
Requires: ruby(release)
Requires: rubygems
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
The Ruby CookieJar is a library to help manage client-side cookies in pure
Ruby. It enables parsing and setting of cookie headers, alternating between
multiple 'jars' of cookies at one time (such as having a set of cookies for
each browser or thread), and supports persistence of the cookies in a JSON
string.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install


%check
pushd ./%{gem_instdir}
rspec -Ilib spec
popd

%install

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/contributors.json
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/cookiejar.gemspec
%{gem_spec}
%doc %{gem_instdir}/spec/*
%doc %{gem_instdir}/LICENSE

%files doc
%{gem_docdir}
%{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile

%changelog
* Mon Jan 30 2017 Martin Mágr <mmagr@redhat.com> - 0.3.3-1
- Updated to latest upstream
- Add missing rspec dependency for unit tests

* Mon Feb 08 2016 Greg Hellings <greg.hellings@gmail.com> - 0.3.2-8
- Updates for EPEL7

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild


* Tue Jun 24 2014 Nitesh Narayan Lal <niteshnarayan@fedoraproject.org> - 0.3.2-5
- Updated to latest upstream release

* Wed May 28 2014 Nitesh Narayan Lal <niteshnarayan@fedoraproject.org> - 0.3.2-4
- Added conditional for F19/F20

* Sat Mar 15 2014 Nitesh Narayan Lal <niteshnarayan@fedoraproject.org> - 0.3.2-3
- Updated to comply with Fedora guidelines

* Thu Mar 6 2014 Nitesh Narayan Lal <niteshnarayan@fedoraproject.org> - 0.3.2-2
- Updated as per the Fedora guidelines

* Sat Jan 11 2014 Nitesh Narayan Lal <niteshnarayan@fedoraproject.org> - 0.3.2-1
- Initial package
