Name:     udisks
Summary:  Device management service, ver 2
Version:  2.1.2
Release:  1
License:  GPL-2.0+
Group:    Base/Device Management
URL:      http://www.freedesktop.org/wiki/Software/udisks
Source0:  %{name}-%{version}.tar.gz
Source1:  udisks.manifest

BuildRequires: pkgconfig(polkit-gobject-1) >= 0.112
BuildRequires: pkgconfig(polkit-agent-1) >= 0.112
BuildRequires: pkgconfig(libatasmart)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 0.6.2

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
udisks provides a daemon, udisksd, that implements well-defined D-Bus interfaces
that can be used to query and manipulate storage devices and a command-line
tool, udisksctl, that can be used to query and use the daemon. The actions that
a user can perform using udisks are restricted using polkit.


%package -n libudisks2-0
Summary:        UDisks Client Library, version 2
License:        LGPL-2.0+
Group:          System/Libraries
Recommends:     %{name} = %{version}


%description -n libudisks2-0
udisks provides a daemon, udisksd, that implements well-defined D-Bus interfaces
that can be used to query and manipulate storage devices and a command-line
tool, udisksctl, that can be used to query and use the daemon. The actions that
a user can perform using udisks are restricted using polkit.


%package -n typelib-UDisks-2_0
License:    LGPL-2.0+
Summary:    udisks Introspection bindings
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}


%description -n typelib-UDisks-2_0
udisks provides a daemon, udisksd, that implements well-defined D-Bus interfaces
that can be used to query and manipulate storage devices and a command-line
tool, udisksctl, that can be used to query and use the daemon. The actions that
a user can perform using udisks are restricted using polkit.    
This package provides the GObject Introspection bindings for UDisks client
library.
  

%package devel
License:    LGPL-2.0+
Summary:    udisks development package
Group:      Development/Libraries
Requires:   libudisks2-0 = %{version}-%{release}


%description devel
udisks provides a daemon, udisksd, that implements well-defined D-Bus interfaces
that can be used to query and manipulate storage devices and a command-line
tool, udisksctl, that can be used to query and use the daemon. The actions that
a user can perform using udisks are restricted using polkit.
This package provides development files for udisks.


%package locale
License:    GPL-2.0
Summary:    The udisks locale package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}


%description locale
udisks locale package


%prep
%setup -q


%build
%autogen \
  --disable-gtk-doc \
  --disable-gtk-doc-html \
  --disable-gtk-doc-pdf \
  --disable-man \
  --disable-nls

make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install
%install_service multi-user.target.wants udisks2.service
cp -a %{SOURCE1} %{buildroot}%{_datadir}/udisks.manifest


%clean


%post -n libudisks2-0 -p /sbin/ldconfig


%postun -n libudisks2-0 -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%manifest %{_datadir}/udisks.manifest
%{_unitdir}/udisks2.service
%{_unitdir}/multi-user.target.wants/udisks2.service
%{_udevrulesdir}/80-udisks2.rules
%{_bindir}/udisksctl
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.UDisks2.conf
%dir %{_libdir}/udisks2
%{_libdir}/udisks2/udisksd
%{_sbindir}/umount.udisks2
%{_datadir}/bash-completion/completions/udisksctl
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks2.service
%{_datadir}/polkit-1/actions/org.freedesktop.udisks2.policy


%files -n libudisks2-0
%defattr(-,root,root,-)
%{_libdir}/libudisks2.so.*


%files -n typelib-UDisks-2_0
%defattr(-,root,root,-)
%{_libdir}/girepository-1.0/UDisks-2.0.typelib


%files devel
%defattr(-,root,root,-)
%{_includedir}/udisks2/
%{_libdir}/libudisks2.so
%{_libdir}/pkgconfig/udisks2.pc
%{_datadir}/gir-1.0/UDisks-2.0.gir


%files locale
%lang(bg) %{_datadir}/locale/bg/LC_MESSAGES/udisks2.mo
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/udisks2.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/udisks2.mo
%lang(el) %{_datadir}/locale/el/LC_MESSAGES/udisks2.mo
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/udisks2.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/udisks2.mo
%lang(eu) %{_datadir}/locale/eu/LC_MESSAGES/udisks2.mo
%lang(fa) %{_datadir}/locale/fa/LC_MESSAGES/udisks2.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/udisks2.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/udisks2.mo
%lang(gl) %{_datadir}/locale/gl/LC_MESSAGES/udisks2.mo
%lang(hr) %{_datadir}/locale/hr/LC_MESSAGES/udisks2.mo
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/udisks2.mo
%lang(ia) %{_datadir}/locale/ia/LC_MESSAGES/udisks2.mo
%lang(id) %{_datadir}/locale/id/LC_MESSAGES/udisks2.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/udisks2.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/udisks2.mo
%lang(ka) %{_datadir}/locale/ka/LC_MESSAGES/udisks2.mo
%lang(kk) %{_datadir}/locale/kk/LC_MESSAGES/udisks2.mo
%lang(lv) %{_datadir}/locale/lv/LC_MESSAGES/udisks2.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/udisks2.mo
%lang(pa) %{_datadir}/locale/pa/LC_MESSAGES/udisks2.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/udisks2.mo
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/udisks2.mo
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/udisks2.mo
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/udisks2.mo
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/udisks2.mo
%lang(sq) %{_datadir}/locale/sq/LC_MESSAGES/udisks2.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/udisks2.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/udisks2.mo
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/udisks2.mo
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/udisks2.mo
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/udisks2.mo
%lang(zh_HK) %{_datadir}/locale/zh_HK/LC_MESSAGES/udisks2.mo
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/udisks2.mo
