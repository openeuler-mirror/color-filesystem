Name:           color-filesystem
Version:        1
Release:        14
Summary:        Color filesystem
License:        Public Domain
BuildArch:      noarch

Requires:       rpm filesystem

%description
This package provides some directories and macros that are required/used to store color management data.

%prep

%build

%install
install -d ${RPM_BUILD_ROOT}%{_datadir}/color/{icc,cmms,settings}
install -d ${RPM_BUILD_ROOT}%{_localstatedir}/lib/color/icc
install -d ${RPM_BUILD_ROOT}/etc/rpm/

cat >${RPM_BUILD_ROOT}%{_sysconfdir}/rpm/macros.color<<EOF
%%_colordir %%_datadir/color
%%_syscolordir %%_colordir
%%_icccolordir %%_colordir/icc
%%_cmmscolordir %%_colordir/cmms
%%_settingscolordir %%_colordir/settings
EOF

%check

%pre

%preun

%post

%postun

%files
%defattr(-,root,root,-)
%dir %{_datadir}/color/icc
%dir %{_datadir}/color/cmms
%dir %{_datadir}/color/settings
%dir %{_localstatedir}/lib/color/icc
%{_sysconfdir}/rpm/macros.color


%changelog
* Sat Sep 7 2019 guan yanjie <guanyanjie@huawei.com> - 1-14
- Package init
