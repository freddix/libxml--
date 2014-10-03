Summary:	C++ interface for working with XML files
Name:		libxml++
Version:	2.36.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libxml++/2.36/%{name}-%{version}.tar.xz
# Source0-md5:	72838890c773f89ec701ba1a57cf0802
URL:		http://libxmlplusplus.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glibmm-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mm-common
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxml++ is a C++ interface for the libxml XML parser library.

%package devel
Summary:	Header files for libxml++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm-devel
Requires:	libxml2-devel

%description devel
Header files for libxml++.

%package apidocs
Summary:	libxml++ API documentation
Group:		Documentation

%description apidocs
libxml++ API documentation.

%prep
%setup -q

%{__sed} -i "s| examples||" Makefile.am

%build
mm-common-prepare
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT	\
	libdocdir=%{_gtkdocdir}/%{name}-%{apiver}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/libxml++-2.6
%{_includedir}/*
%{_pkgconfigdir}/*

%files apidocs
%defattr(644,root,root,755)
%doc %{_gtkdocdir}/%{name}-%{apiver}

