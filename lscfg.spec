Name:		lscfg
Version:	1.3.1
Release:	1%{?dist}
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
Requires:	logrotate
Requires:	crontabs

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

# logdir
%{__mkdir_p} %{buildroot}/%{_var}/log/%{name}

# logrotate
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/logrotate.d
%{__install} -p -m0644 src/config/logrotate.d/lscfg %{buildroot}/%{_sysconfdir}/logrotate.d

# documentation
%{__mkdir_p} %{buildroot}/%{_mandir}/man8
%{__gzip} -c src/doc/lscfg.8 > %{buildroot}/%{_mandir}/man8/lscfg.8.gz

# the main script
%{__mkdir_p} %{buildroot}/%{_sbindir}
%{__install} -p -m0755 src/lscfg %{buildroot}/%{_sbindir}
%{__install} -p -m0755 src/lscfg.basic %{buildroot}/%{_sbindir}
%{__install} -p -m0755 src/lscfg.disk %{buildroot}/%{_sbindir}
%{__install} -p -m0755 src/lscfg.hardware %{buildroot}/%{_sbindir}
%{__install} -p -m0755 src/lscfg.kernel %{buildroot}/%{_sbindir}
%{__install} -p -m0755 src/lscfg.network %{buildroot}/%{_sbindir}
%{__install} -p -m0755 src/lscfg.services %{buildroot}/%{_sbindir}
%{__install} -p -m0755 src/lscfg.virt %{buildroot}/%{_sbindir}

# checkpoints
%{__mkdir_p} %{buildroot}/%{_datadir}/%{name}
%{__install} -p -m0755 src/checkpoints/* %{buildroot}/%{_datadir}/%{name}

# configs
%{__mkdir_p} %{buildroot}/%{_sysconfdir}/%{name}
%{__install} -p -m0644 src/config/functions %{buildroot}/%{_sysconfdir}/%{name}
%{__install} -p -m0644 src/config/lscfg.conf %{buildroot}/%{_sysconfdir}/%{name}

# cronjobs
%{__mkdir_p} %{buildroot}%{_sysconfdir}/cron.daily
%{__install} -p -m0755 src/config/cron.daily/lscfg %{buildroot}%{_sysconfdir}/cron.daily



%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{_mandir}/man8/lscfg.8.gz
%doc LICENSE

# main script
%{_sbindir}/lscfg
%{_sbindir}/lscfg.basic
%{_sbindir}/lscfg.disk
%{_sbindir}/lscfg.hardware
%{_sbindir}/lscfg.kernel
%{_sbindir}/lscfg.network
%{_sbindir}/lscfg.services
%{_sbindir}/lscfg.virt

# configs
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/lscfg.conf
%config %{_sysconfdir}/%{name}/functions
%config %{_sysconfdir}/cron.daily/lscfg
%config %{_sysconfdir}/logrotate.d/lscfg

# logdir
%dir %{_var}/log/%{name}

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
%{_datadir}/%{name}/lvdisplay
%{_datadir}/%{name}/lvm-filter
%{_datadir}/%{name}/mount
%{_datadir}/%{name}/multipath
%{_datadir}/%{name}/nss-hosts
%{_datadir}/%{name}/numactl
%{_datadir}/%{name}/panic
%{_datadir}/%{name}/parted
%{_datadir}/%{name}/pvdisplay
%{_datadir}/%{name}/service
%{_datadir}/%{name}/vgdisplay
%{_datadir}/%{name}/virsh-capabilities
%{_datadir}/%{name}/virsh-dominfo
%{_datadir}/%{name}/virsh-list
%{_datadir}/%{name}/virsh-net-list
%{_datadir}/%{name}/xm-list


# NOTE:
# see http://fedoraproject.org/wiki/Packaging/ScriptletSnippets

%post
# always reload crond to pick up add/delete/change
/sbin/service crond reload || :

%postun
if [ $1 -eq 0 ]; then
  /sbin/service crond reload || :
fi


%changelog
* Fri Sep 17 2010 Paul Morgan <jumanjiman@gmail.com> 1.3.1-1
- Add: daily cron job and logrotate config (jumanjiman@gmail.com)

* Tue Aug 31 2010 Paul Morgan <jumanjiman@gmail.com> 1.3.0-7
- lvm commands have different path between fedora and rhel

* Tue Aug 31 2010 Paul Morgan <jumanjiman@gmail.com> 1.3.0-6
- make new checkpoints executable
- protect output from asciidoc interpretation

* Tue Aug 31 2010 Paul Morgan <jumanjiman@gmail.com> 1.3.0-5
- add lscfg.virt to files

* Tue Aug 31 2010 Paul Morgan <jumanjiman@gmail.com> 1.3.0-4
- new checkpoints for virt
- checkpoints for lvm, multipath
- better return code for checkpoint parted

* Mon Aug 30 2010 Paul Morgan <jumanjiman@gmail.com> 1.3.0-3
- better formatting in basic info
- added intro and checkpoint-code sections
- only output doc title section if running checkpoints
- explanatory note in README for github

* Mon Aug 30 2010 Paul Morgan <jumanjiman@gmail.com> 1.3.0-2
- add missing scripts to spec

* Mon Aug 30 2010 Paul Morgan <jumanjiman@gmail.com> 1.3.0-1
- version bump
- output in asciidoc for conversion to other formats
- fix up path for sudo invocation
- modular checkpoints in /usr/share/lscfg
- do checkpoints at nice +19
- moved variables into config file
- use parted instead of fdisk
- add numa checkpoints
- new net checkpoints
- remove release from script version
- GPLv2 is now in LICENSE instead of COPYING.GPLv2

* Sun Aug 29 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-3
- use asciidoc to generate manpage

* Sat Aug 28 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-2
- build noarch (jumanjiman@gmail.com)

* Sun Jul 25 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-1
- fixed typo in spec file

* Sun Jul 25 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-0
- new package built with tito


