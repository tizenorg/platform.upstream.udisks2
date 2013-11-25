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
%{_prefix}/lib/
%{_libdir}/systemd/
%{_libdir}/udev/
%{_prefix}/bin/
%{_prefix}/etc/
%{_prefix}/sbin/
%{_prefix}/share/
%exclude %{_prefix}/share/locale/
%exclude %{_prefix}/lib/pkgconfig/udisks2.pc
%exclude %{_prefix}/lib/debug
%license COPYING

%files devel
%{_prefix}/include/
%{_prefix}/lib/libudisks2.so
%{_prefix}/lib/pkgconfig/udisks2.pc

%files locale
%{_prefix}/share/locale/

