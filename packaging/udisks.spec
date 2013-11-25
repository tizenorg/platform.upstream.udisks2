Name:     udisks
Summary:  The udisks
Version:  2.1.2
Release:  1
License:  GPL-2.0
Group:    Base/Device Management
URL:      http://code.google.com/p/cryptsetup/
Source0:  %{name}-%{version}.tar.gz
Source1:  udisks.manifest

BuildRequires: pkgconfig(polkit-gobject-1) >= 0.112
BuildRequires: pkgconfig(polkit-agent-1) >= 0.112
BuildRequires: pkgconfig(libatasmart)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(expat)

BuildRequires: gobject-introspection
BuildRequires: device-mapper-devel
BuildRequires: perl-XML-Parser
BuildRequires: libgudev-devel
BuildRequires: kernel-headers
BuildRequires: systemd-devel
BuildRequires: gnome-common
BuildRequires: libacl-devel
BuildRequires: python-xml
BuildRequires: intltool
BuildRequires: gtk-doc

Requires:      glib2
Requires:      libxslt
Requires:      polkit
Requires:      expat

%description
The udisks project provides:
    - daemon, udisksd, that implements well-defined D-Bus interfaces that can be used to query and 
      manipulate storage devices
    - command-line tool, udisksctl, that can be used to query and use the daemon The actions that 
      a user can perform using udisks are restricted using polkit

%package devel
License:    LGPL-2.1
Summary:    The udisks development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%package locale
License:    GPL-2.0
Summary:    The udisks locale package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
udisk development package

%description locale
udisk development package

%prep
%setup -q

%build
./autogen.sh --disable-gtk-doc --disable-gtk-doc-html --disable-gtk-doc-pdf --disable-man --disable-nls --prefix=/usr

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../udisks2.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/udisks2.service
cp -a %{SOURCE1} %{buildroot}%{_datadir}/udisks.manifest

%clean

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%manifest %{_datadir}/udisks.manifest
%{_libdir}/systemd/system/udisks2.service
%{_libdir}/systemd/system/multi-user.target.wants/udisks2.service
%{_libdir}/udev/rules.d/80-udisks2.rules
%{_prefix}/bin/udisksctl
%{_prefix}/etc/dbus-1/system.d/org.freedesktop.UDisks2.conf
%{_prefix}/include/udisks2/udisks/udisks-generated.h
%{_prefix}/lib/libudisks2.so
%{_prefix}/lib/libudisks2.so.0
%{_prefix}/lib/libudisks2.so.0.0.0
%{_prefix}/lib/udisks2/udisksd
%{_prefix}/sbin/umount.udisks2
%{_prefix}/share/bash-completion/completions/udisksctl
%{_prefix}/share/dbus-1/system-services/org.freedesktop.UDisks2.service
%{_prefix}/share/polkit-1/actions/org.freedesktop.udisks2.policy


%files devel
%{_prefix}/include/udisks2/udisks/udisks-generated.h
%{_prefix}/include/udisks2/udisks/udisks.h
%{_prefix}/include/udisks2/udisks/udisksclient.h
%{_prefix}/include/udisks2/udisks/udisksenums.h
%{_prefix}/include/udisks2/udisks/udisksenumtypes.h
%{_prefix}/include/udisks2/udisks/udiskserror.h
%{_prefix}/include/udisks2/udisks/udisksobjectinfo.h
%{_prefix}/include/udisks2/udisks/udiskstypes.h
%{_prefix}/include/udisks2/udisks/udisksversion.h
%{_prefix}/lib/libudisks2.so
%{_prefix}/lib/pkgconfig/udisks2.pc

%files locale
%{_prefix}/share/locale/bg/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/cs/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/de/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/el/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/en_GB/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/es/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/eu/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/fa/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/fi/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/fr/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/gl/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/hr/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/hu/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/ia/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/id/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/it/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/ja/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/ka/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/kk/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/lv/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/nl/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/pa/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/pl/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/pt_BR/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/ru/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/sk/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/sl/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/sq/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/sr/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/sv/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/tr/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/uk/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/zh_CN/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/zh_HK/LC_MESSAGES/udisks2.mo
%{_prefix}/share/locale/zh_TW/LC_MESSAGES/udisks2.mo

