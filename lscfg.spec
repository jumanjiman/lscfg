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
a2x -d manpage -f manpage src/doc/lscfg.8.asciidoc

%install
%{__rm} -rf %{buildroot}

# documentation
%{__mkdir_p} %{buildroot}/%{_mandir}/man8
%{__gzip} -c src/doc/lscfg.8 > %{buildroot}/%{_mandir}/man8/lscfg.8.gz

# the main script
%{__mkdir_p} %{buildroot}/%{_sbindir}
%{__install} -p -m0755 src/lscfg %{buildroot}/%{_sbindir}

# checkpoints
%{__mkdir_p} %{buildroot}/%{_datadir}/%{name}
%{__install} -p -m0755 src/checkpoints/* %{buildroot}/%{_datadir}/%{name}

# configs
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/%{name}
%{__install} -p -m0644 src/config/* %{buildroot}/%{_sysconfdir}/%{name}



%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{_mandir}/man8/lscfg.8.gz
%doc src/COPYING.GPLv2

# main script
%{_sbindir}/lscfg

# configs
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/lscfg.conf
%config %{_sysconfdir}/%{name}/functions

# checkpoints
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/arp-cache
%{_datadir}/%{name}/cpu_count
%{_datadir}/%{name}/cpu_type
%{_datadir}/%{name}/default_gateway
%{_datadir}/%{name}/disk_utilization
%{_datadir}/%{name}/duplex
%{_datadir}/%{name}/file
%{_datadir}/%{name}/free_memory
%{_datadir}/%{name}/ip-addr
%{_datadir}/%{name}/ip-rules
%{_datadir}/%{name}/ip-stats
%{_datadir}/%{name}/lspci
%{_datadir}/%{name}/mount
%{_datadir}/%{name}/nss-hosts
%{_datadir}/%{name}/numactl
%{_datadir}/%{name}/panic
%{_datadir}/%{name}/parted
%{_datadir}/%{name}/service


%changelog
* Sun Aug 29 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-3
- use asciidoc to generate manpage

* Sat Aug 28 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-2
- build noarch (jumanjiman@gmail.com)

* Sun Jul 25 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-1
- fixed typo in spec file

* Sun Jul 25 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-0
- new package built with tito


