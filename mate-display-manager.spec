%define	_build_pkgcheck_set	%{nil}
%define dm_user	mdm

Summary:	Displays login screen for MATE Desktop
Name:		mate-display-manager	
Version:	1.4.0
Release:	1
License:	GPLv2+ 
Group:		System/X11
URL:		https://mate-desktop.org	
Source0:	http://vicodan.fedorapeople.org/mate-display-manager-1.4.0.tar.gz
Patch0:		mate-display-manager-1.4.0_mateconf_min_ver.patch

BuildRequires:	intltool
BuildRequires:	icon-naming-utils
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libnm-gtk)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(libmatepanelapplet-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(popt)
Requires:	mate-conf
Requires:	mate-desktop
Requires:	mate-corba
Requires:	mate-session-manager
Requires:	mate-control-center
Requires:	mate-settings-daemon
Requires(pre,post,preun):	mate-conf
Requires(pre,post,preun):	rpm-helper

%description
Displays login screen for MATE Desktop

%prep
%setup -q
%autopatch -p1

%build
%configure2_5x \
	--disable-static \
	--disable-scrollkeeper \
	--disable-schemas-install \
	--disable-nls

%make

%install
export MATECONF_DISABLE_MAKE_FILE_SCHEMA INSTALL=1
%makeinstall_std

%find_lang mdm --with-gnome --all-name

%pre
%_pre_useradd %{dm_user} %{_var}/lib/%{name} /bin/false
%_pre_groupadd xgrp %{dm_user}

%postun
%_postun_userdel %{dm_user}
%_postun_groupdel xgrp %{dm_user}

%files -f mdm.lang
%doc AUTHORS COPYING README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/mdm.conf
%config(noreplace) %{_sysconfdir}/pam.d/mdm*
%config(noreplace) %{_sysconfdir}/mdm
%config(noreplace) %{_sysconfdir}/mateconf/schemas/mdm-simple-greeter.schemas
%{_bindir}/mdmflexiserver
%{_bindir}/mdm-screenshot
%{_sbindir}/mdm
%{_sbindir}/mdm-binary
%{_libexecdir}/mdm-*
%{_libexecdir}/matecomponent/servers/MATE_FastUserSwitchApplet.server
%{_datadir}/mate-2.0/ui/MATE_FastUserSwitchApplet.xml
%{_datadir}/mdm
%{_datadir}/pixmaps/faces/*
%{_datadir}/pixmaps/*.png
%{_iconsdir}/hicolor/*/*/*
%{_localstatedir}/lib/mdm

