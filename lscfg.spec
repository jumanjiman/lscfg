Name:		lscfg
Version:	1.2.0
Release:	0%{?dist}
Summary:	details the basic configuration of a Linux system

Group:		Admin
License:	GPLv2
URL:		http://github.com/jumanjiman/lscfg
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

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


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{_mandir}/man8
%{__mkdir_p} %{buildroot}/%{_sbindir}
%{__install} -m0755 lscfg %{buildroot}/%{_sbindir}
%{__gzip} -c src/lscfg.8 > %{buildroot}/%{_mandir}/man8/lscfg.8.gz



%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{_mandir}/man8/lscfg.8.gz
%doc src/COPYING.GPLv2
%{_sbindir}/lscfg



%changelog
* Sun Jul 25 2010 Paul Morgan <jumanjiman@gmail.com> 1.2.0-0
- new package built with tito


