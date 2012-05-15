Name:		msgpack
Version:	0.5.7
Release:	1%{?dist}
Summary:	MessagePack is a binary-based efficient object serialization library.

Group:		Development/Libraries
License:	Apache 2.0
URL:		http://www.msgpack.org
Source0:	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
MessagePack is a binary-based efficient object serialization library. It enables to exchange structured objects between many languages like JSON. But unlike JSON, it is very fast and small.

%package devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
 
%description devel
This package contains the libraries and header files needed for developing with %{name}.
%prep
%setup -q -n %{name}-%{version}


%build
%configure --prefix=/usr
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm %{buildroot}%{_libdir}/lib%{name}.a
rm %{buildroot}%{_libdir}/lib%{name}.la
rm %{buildroot}%{_libdir}/lib%{name}c.a
rm %{buildroot}%{_libdir}/lib%{name}c.la

%clean
rm -rf %{buildroot}
 
%post
/sbin/ldconfig
 
%preun
 
%postun
/sbin/ldconfig
exit 0
 
%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/libmsgpack.so.*
%{_libdir}/libmsgpackc.so.*
 
%files devel
%defattr(-, root, root, -)
%{_includedir}/msgpack.h
%{_includedir}/msgpack.hpp
%{_includedir}/msgpack/*
%{_libdir}/libmsgpack.so
%{_libdir}/libmsgpackc.so



%changelog
* Mon May 14 2012 Yunoka Minazuki <yuno@yuno.net>
- New Build