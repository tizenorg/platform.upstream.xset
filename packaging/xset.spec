Name:           xset
Version:        1.2.2
Release:        1
License:        MIT
Summary:        User preference utility for X
Url:            http://xorg.freedesktop.org/
Group:          System/X11
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfontcache)
BuildRequires:  pkgconfig(xxf86misc)
BuildRequires:  pkgconfig(xmuu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17

%description
This program is used to set various user preference options of the
display.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/xset
%{_mandir}/man1/xset.1%{?ext_man}

