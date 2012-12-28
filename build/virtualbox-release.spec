Name:   virtualbox-release
Version:  1.0
Release:  1%{?dist}
Summary:  VirtualBox repository configuration

Group:  System Environment/Base
License:  BSD
URL:    http://virtualbox.com
Source0:  %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch

%description
VirtualBox Linux repository configuration.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 virtualbox.repo $RPM_BUILD_ROOT/etc/yum.repos.d/

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 RPM-GPG-KEY-virtualbox $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/pki/rpm-gpg/RPM-GPG-KEY-virtualbox
/etc/yum.repos.d/virtualbox.repo

%changelog
* Sun May 20 2012 Chris Smart <chris@kororaa.org> - 1.0
- Initial package.
