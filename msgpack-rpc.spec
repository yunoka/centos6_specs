Name:		msgpack-rpc
Version:	0.3.1
Release:	1%{?dist}
Summary:	RPC library using MessagePack.
Requires:       kyotocabinet
Group:		Development/Libraries
License:	Apache 2.0
URL:		http://www.msgpack.org
Source0:	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


BuildRequires:  pkgconfig, autoconf, automake,gcc >= 4.1
BuildRequires:  msgpack-devel >= 0.5.2
BuildRequires:  mpio-devel >= 0.3.5
Requires:       msgpack >= 0.5.2
Requires:       mpio    >= 0.3.5


%description
MessagePack-RPC is cross-language RPC library for client, server and cluster applications. Because it releases you from complicated network programming completely and provides well-designed API, you can easily implement advanced network applications with MessagePack-RPC.

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
%{_libdir}/libmsgpack-rpc.so.*
 
%files devel
%defattr(-, root, root, -)
%{_includedir}/msgpack/rpc/*.h
%{_includedir}/msgpack/rpc/transport/*.h
%{_libdir}/libmsgpack-rpc.so




%changelog
* Mon May 14 2012 Yunoka Minazuki <yuno@yuno.net>
- New Build