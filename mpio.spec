Name:		mpio
Version:	0.3.7
Release:	1%{?dist}
Summary:	Multipurpose concurrent I/O framework for C++.
Group:		Development/Libraries
License:	Apache 2.0
URL:		https://github.com/frsyuki/mpio/
Source0:	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Multipurpose parallel I/O framework for C++ with fully multithreaded event loop implementation 

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
%{_libdir}/libmpio.so.*

 
%files devel
%defattr(-, root, root, -)
%{_includedir}/mp/*.h
%{_libdir}/libmpio.so




%changelog
* Tue May 15 2012 Yunoka Minazuki <yuno@yuno.net>
- New Build