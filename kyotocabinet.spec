Summary:        A straightforward implementation of DBM
Name:           kyotocabinet
Version:        1.2.75
Release:        1
License:        GPL/LGPL
Group:          Development/Libraries
URL:            http://fallabs.com/kyotocabinet/
Source:         http://fallabs.com/tokyocabinet/pkg/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  pkgconfig, zlib-devel, autoconf, automake

%description
Kyoto Cabinet is a library of routines for managing a database.
The database is a simple data file containing records,
each is a pair of a key and a value.
Every key and value is serial bytes with variable length.
Both binary data and character string can be used as a key and a value.
Each key must be unique within a database.
There is neither concept of data tables nor data types.
Records are organized in hash table or B+ tree.

%package devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
BuildRequires:  pkgconfig, zlib-devel, autoconf, automake

%description devel
This package contains the libraries and header files needed for
developing with %{name}.

%prep
%setup -q

%build
%configure
#%configure CFLAGS="$CFLAGS"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

rm -rf %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_libdir}/lib%{name}.a

%check
make check

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%{_bindir}/kc*
%{_libdir}/libkyotocabinet.so.*
%{_mandir}/man1/kc*.gz

%files devel
%defattr(-, root, root, -)
%{_docdir}/kyotocabinet/*
%{_includedir}/kc*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/kc*.gz


%changelog
* Tue May 08 2012 Keisuke Kawahara <kyohsuke@conafie.jp>
- bump up  1.2.75.

* Mon Apr 02 2012 Keisuke Kawahara <kyohsuke@conafie.jp>
- bump up  1.2.74.

* Wed Dec 21 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- bump up  1.2.72.

* Tue Sep 20 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- bump up  1.2.70.

* Thu Jun 02 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.2.58.

* Tue Apr 12 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.2.51.

* Fri Apr 08 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.2.50.

* Tue Feb 22 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.2.48.
- remove build failed patch.

* Tue Feb 22 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.2.45.
- fixed build failed in gcc 4.1.2.

* Mon Feb 14 2011 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.2.43.

* Wed Nov 10 2010 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.2.33.

* Wed Nov 10 2010 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.2.23.

* Thu Oct 21 2010 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.2.17.

* Wed Oct 06 2010 Keisuke Kawahara <kyohsuke@conafie.jp>
- convert from tokyocabinet.spec .

* Fri Sep 03 2010 Keisuke Kawahara <kyohsuke@conafie.jp>
- update to 1.4.46.

* Thu Jan 29 2009 myfinder <medianetworks@gmail.com> http://blog.myfinder.jp/2009/01/tokyo-tyrantrpm.html
- New Build
