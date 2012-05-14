# $Id$
# Authority: dag

Summary: FUSE filesystem using Amazon Simple Storage Service as storage
Name: fuse-s3fs
Version: 1.61
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://code.google.com/p/s3fs/

Source: http://s3fs.googlecode.com/files/s3fs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: fuse-devel > 2.8.4
BuildRequires: libcurl-devel > 7.0
BuildRequires: libxml2-devel > 2.6 
BuildRequires: openssl-devel
Requires: fuse > 2.8.4
Requires: libcurl > 7.0
Requires: libxml2 > 2.6
Requires: openssl


%description
This package provides a FUSE (Filesystem in User Space) application allowing
for the mounting of Amazon Web Services' S3 storage facilities on a local
system.
WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING
This package has undergone some minimal testing and is deemed to be
safe to store data on.  However, this is the first instance in which this
project has been placed into wide circulation.  As such, until this package
develops some extra maturity from more widespread use, it is recommended that
data stored on fuse-s3fs be backed up on other media as well.

%prep
%setup -q -n s3fs-%{version}

%build
%configure
make
%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 -p src/s3fs %{buildroot}%{_bindir}/s3fs
%{__install} -Dp -m0644 -p doc/man/s3fs.1 %{buildroot}%{_mandir}/man1/s3fs.1
#make install PREFIX=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING 
%doc %{_mandir}/man1/s3fs.1*
%{_bindir}/s3fs

%changelog
* Sun May 13 2012 Yunoka Minazuki <yuno@yuno.net>
- Initial package.
