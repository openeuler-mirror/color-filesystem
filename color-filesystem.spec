%global apiver %(v=2.1.0; echo ${v%.${v#[0-9].[0-9].}})

Name:			color-filesystem
Version:		1
Release:		15
Summary:		Color filesystem layout
Group:			System Environment/Base
License:		Public Domain
BuildArch:		noarch
URL:			https://src.fedoraproject.org/rpms/color-filesystem
Source0:		color-filesystem.tar.gz

ExclusiveArch:	%{arm} %{ix86} x86_64 %{mips} aarch64

Requires:		filesystem
Requires:		rpm

%description
This package provides some directories that are required/used to store color.

%prep
# Nothing to prep

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/icc
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/cmms
mkdir -p $RPM_BUILD_ROOT%{_datadir}/color/settings
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/color/icc

# rpm macros
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm/
cat >$RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.color<<EOF
%%_colordir %%_datadir/color
%%_syscolordir %%_colordir
%%_icccolordir %%_colordir/icc
%%_cmmscolordir %%_colordir/cmms
%%_settingscolordir %%_colordir/settings
EOF


%files
%defattr(-,root,root,-)
%dir %{_datadir}/color
%dir %{_datadir}/color/icc
%dir %{_datadir}/color/cmms
%dir %{_datadir}/color/settings
%dir %{_localstatedir}/lib/color
%dir %{_localstatedir}/lib/color/icc
%{_sysconfdir}/rpm/macros.color

%changelog
* Tue May 25 2021 zhangyao <zhangyao05@outlook.com> - 1-15
- Import Color Filesystem

* Sat Sep 7 2019 guan yanjie <guanyanjie@huawei.com> - 1-14
- Package init
