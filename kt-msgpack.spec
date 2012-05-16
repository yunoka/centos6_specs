Name:		kt-msgpack
Version:	0.0.1
Release:	1%{?dist}
Summary:	MessagePack-RPC Server Plugin for Kyoto Tycoon.
Requires:       kyotocabinet
Group:		Development/Libraries
License:	Apache 2.0
URL:		https://github.com/frsyuki/kt-msgpack
Source0:	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


BuildRequires:  pkgconfig, autoconf, automake,gcc >= 4.1
BuildRequires:  msgpack-devel >= 0.5.2
BuildRequires:  mpio-devel >= 0.3.5
BuildRequires:  kyototycoon-devel
Requires:       msgpack >= 0.5.2
Requires:       mpio    >= 0.3.5
Requires:       kyototycoon


%description
MessagePack-RPC Server Plugin for Kyoto Tycoon.


%prep
%setup -q -n %{name}-%{version}

%build
%configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm %{buildroot}%{_libexecdir}/libktmsgpack.a
rm %{buildroot}%{_libexecdir}/libktmsgpack.la


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
%doc AUTHORS COPYING NOTICE
%{_libexecdir}/*.so
%{_libexecdir}/*.so.*



%changelog
* Thu May 15 2012 Yunoka Minazuki <yuno@yuno.net>
- New Build