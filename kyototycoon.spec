# Enable Lua extention.
%define ENABLE_LUA 1

# Disable system-specific event.
%define DISABLE_EVENT 0

Summary:        A persistent cache server
Name:           kyototycoon
Version:        0.9.55
Release:        1
License:        GPL/LGPL
Group:          Development/Libraries
URL:            http://fallabs.com/kyototycoon/
Source:         http://fallabs.com/kyototycoon/pkg/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       kyotocabinet
Requires:       lua
BuildRequires:  kernel-devel >= 2.6.17
BuildRequires:  kernel >= 2.6.17
BuildRequires:  kyotocabinet-devel,lua-devel
BuildRequires:  pkgconfig, zlib-devel, autoconf, automake

%description
Kyoto Tycoon is a lightweight database server with auto expiration mechanism,
which is useful to handle cache data of various applications.
Kyoto Tycoon is also a package of network interface to the DBM called Kyoto Cabinet.
Though the DBM has high performance and high concurrency,
you might bother in case that multiple processes share the same database,
or remote processes access the database.
Thus, Kyoto Tycoon is provided for concurrent and remote connections to Kyoto Cabinet.
Kyoto Tycoon is composed of the server process managing multiple databases and its access library for client applications.

%package devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package contains the libraries and header files needed for
developing with %{name}.

%prep
%setup -q

%build
autoconf
%configure \
 %if %{ENABLE_LUA}
    --enable-lua \
 %endif
 %if %{DISABLE_EVENT}
    --disable-event \
 %endif
    CFLAGS="$CFLAGS"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

rm -rf %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_libdir}/lib%{name}.a
rm -rf %{buildroot}%{_defaultdocdir}/%{name}

# Install And Setup Scripts.
%{__cat} > ./ktservctl.head << 'EOF'
#! /bin/sh
#
# ktservctl	This shell script takes care of starting and stopping
#		    the KyotoTycoon subsystem (ktserver).
#
# chkconfig: - 64 36
# description: KyotoTycoon: A persistent cache server
# processname: ktserver
# pidfile: /var/ktserver/pid

# Source function library.
. /etc/rc.d/init.d/functions

EOF
%{__cat} ./ktservctl.head ./lab/ktservctl > %{buildroot}%{_bindir}/ktservctl

%{__install} -Dp -m0755 %{buildroot}%{_bindir}/ktservctl %{buildroot}%{_sysconfdir}/rc.d/init.d/ktservctl

%check
make check

%clean
rm -rf %{buildroot}

%post 
/sbin/ldconfig
/sbin/chkconfig --add ktservctl
/sbin/chkconfig ktservctl on
/sbin/service ktservctl start > /dev/null 2>&1

%preun
/sbin/service ktservctl stop > /dev/null 2>&1
/sbin/chkconfig --del ktservctl

%postun
/sbin/service ktservctl stop > /dev/null 2>&1
/sbin/chkconfig --del ktservctl > /dev/null 2>&1
/sbin/ldconfig

%files
%defattr(-, root, root, -)
%config(noreplace) %{_initrddir}/ktservctl
%{_libexecdir}/*.so
%doc COPYING ChangeLog kyototycoon.idl
%{_bindir}/kt*
%{_libdir}/libkyototycoon.so.*
%{_mandir}/man1/kt*.gz


%files devel
%defattr(-, root, root, -)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/kt*.gz


%changelog
* Sun May 13 2012 Yunoka Minazuki <yuno@yuno.net>
- For CentOS/RHEL 6 fix
- Add docs.
- Add Lua-extension
- Add lib-event

* Tue May 08 2012 Keisuke Kawahara <kyohsuke@conafie.jp>
- bump up  0.9.55.

* Mon Apr 02 2012 Keisuke Kawahara <kyohsuke@conafie.jp>
- bump up  0.9.54.

* Wed Dec 21 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- bump up  0.9.52.

* Tue Sep 20 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- bump up  0.9.51.

* Fri Apr 08 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 0.9.38.
- add init script

* Mon Feb 14 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 0.9.33.

* Wed Jan 08 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 0.9.22.

* Wed Nov 10 2010 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 0.9.6.

* Thu Oct 21 2010 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 0.9.3.

* Wed Oct 06 2010 Keisuke Kawahara <kyohsuke@conafie.jp>
- convert from tokyotyrant.spec .

* Fri Sep 03 2010 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.1.41.

* Thu Jan 29 2009 myfinder <medianetworks@gmail.com> http://blog.myfinder.jp/2009/01/tokyo-tyrantrpm.html
- New Build
