Name:		lscfg
Version:	1.2.0
Release:	3%{?dist}
Summary:	details the basic configuration of a Linux system

Group:		Applications/System
License:	GPLv2
URL:		http://github.com/jumanjiman/lscfg
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
buildarch:	noarch

buildrequires: asciidoc

Requires:	coreutils
Requires:	grep
Requires:	sed
Requires:	less
Requires:	chkconfig
Requires:	initscripts
Requires:	net-tools
Requires:	procps
Requires:	util-linux
Requires:	iproute

%description
Gives an overview of system configuration. 
Think of it as an anorexic version of sysreport.

%prep
%setup -q


%build
# convert manpage
a2x -d manpage -f manpage src/lscfg.8.asciidoc

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{_mandir}/man8
%{__mkdir_p} %{buildroot}/%{_sbindir}
%{__install} -m0755 src/lscfg %{buildroot}/%{_sbindir}
%{__gzip} -c src/lscfg.8 > %{buildroot}/%{_mandir}/man8/lscfg.8.gz



%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{_mandir}/man8/lscfg.8.gz
%doc src/COPYING.GPLv2
%{_sbindir}/lscfg



%changelog
* Sun Aug 29 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-3
- use asciidoc to generate manpage

* Sat Aug 28 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-2
- build noarch (jumanjiman@gmail.com)

* Sun Jul 25 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-1
- fixed typo in spec file

* Sun Jul 25 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-0
- new package built with tito


