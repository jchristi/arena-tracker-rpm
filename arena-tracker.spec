## The upstream versioning is not semantically correct (ie. 4.4 == 4.40)
%global   rpm_version 6.0
%global   zip_version 6.0

## Disable debug subpackage
## https://fedoraproject.org/wiki/Packaging:Debuginfo#Useless_or_incomplete_debuginfo_packages_due_to_other_reasons
%global   debug_package %{nil}

## Do not repack JARs
%define   __jar_repack %{nil}

Name:     arena-tracker
Version:  %{rpm_version}
Release:  1%{?dist}
Summary:  Tracks your Hearthstone Arena matches and cards

Group:    Amusements/Games
License:  GPL
URL:      https://github.com/supertriodo/Arena-Tracker
Source0:  %{url}/releases/download/v%{zip_version}/Arena.Tracker.v%{zip_version}.Linux.zip

Source1:  arena-tracker.desktop
Source2:  ArenaTracker.ico

##BuildRequires:
Requires: libjpeg-turbo
Requires: libjpeg-turbo-utils
Requires: libpng
Requires: xcb-util-renderutil
Requires: jpgalleg
## Need to build old libjpeg8
Requires: libjpeg8

%description
Tracks your Hearthstone Arena matches and cards. Arena Tracker reads the Hearthstone log
to give your all the info you need. Arena Tracker works in arena, constructed, adventures
and tavern-brawl.


%prep
%setup -qn "Arena Tracker v%{zip_version} Linux"


%build
# Source is pre-compiled so no build required


%install
mkdir -p %{buildroot}{%{_bindir},%{_datadir}/icons,%{_datadir}/applications}
cp -p ArenaTracker %{buildroot}%{_bindir}/%{name}
cp -p %{SOURCE1} %{buildroot}%{_datadir}/applications/
cp -p %{SOURCE2} %{buildroot}%{_datadir}/icons/


%files
%defattr(-,root,root,-)
%{_bindir}/arena-tracker
%{_datadir}/icons/ArenaTracker.ico
%{_datadir}/applications/arena-tracker.desktop


%changelog
* Thu Aug 31 2017 <jchristi@github.com> - 6.0-1
- Update to version 6.0
* Thu Aug 24 2017 <jchristi@github.com> - 5.3-1
- Update to version 5.3
* Mon Jul 17 2017 <jchristi@github.com> - 5.2-1
- Update to latest version
* Sun Jan 01 2017 <jchristi@github.com> - 4.41-1
- Initial build
