Summary:	Inter-toolkit configuration settings library
Summary(pl.UTF-8):	Biblioteka ustawień dzielonych między toolkitami
Name:		libxsettings-client
Version:	0.17
Release:	7
License:	MIT
Group:		X11/Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	2c052bbe613d2d83abad391824b217ad
Patch0:		%{name}-opt.patch
URL:		http://freedesktop.org/wiki/Software/xsettings
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	gtk-doc-automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xorg-lib-libX11-devel
Provides:	Xsettings-client = %{version}-%{release}
Obsoletes:	Xsettings-client < 0.17-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The intent of XSETTINGS protocol is to provide a mechanism to allow
the configuration of settings such as double click timeout,
drag-and-drop threshold, and default foreground and background colors
for all applications running within a desktop.

This package contains XSETTINGS client library.

%description -l pl.UTF-8
Celem protokołu XSETTINGS jest dostarczenie mechanizmu pozwalającego
na konfigurację ustawień takich jak czas podwójnego kliknięcia, próg
przeciągania i upuszczania czy domyślne kolory obrazu i tła dla
wszystkich aplikacji działających na pulpicie.

Ten pakiet zawiera bibliotekę kliencką XSETTINGS.

%package devel
Summary:	Header files for libXsettings-client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXsettings-client
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Provides:	Xsettings-client-devel = %{version}-%{release}
Obsoletes:	Xsettings-client-devel < 0.17-1

%description devel
Header files for libXsettings-client library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libXsettings-client.

%package static
Summary:	Static libXsettings-client library
Summary(pl.UTF-8):	Statyczna biblioteka libXsettings-client
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	Xsettings-static = %{version}-%{release}
Obsoletes:	Xsettings-static

%description static
Static libXsettings-client library.

%description static -l pl.UTF-8
Statyczna biblioteka libXsettings-client.

%package apidocs
Summary:	libXsettings-client API documentation
Summary(pl.UTF-8):	Dokumentacja API libXsettings-client
License:	LGPL v2.1+
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
libXsettings-client API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libXsettings-client.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXsettings-client.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXsettings-client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXsettings-client.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXsettings-client.so
%{_includedir}/xsettings-*.h
%{_pkgconfigdir}/libxsettings-client.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXsettings-client.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libXsettings-client
