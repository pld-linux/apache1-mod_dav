Summary:	WebDAV module for the Apache Web server
Summary(pl):	Modu³ WebDAV dla webserwera Apache
%define		apache_version	1.3.6
%define		mod_name	dav
Name:		apache-mod_%{mod_name}
Version:	1.0.2
Release:	1
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
License:	OSI Approved
Source0:	http://www.webdav.org/mod_dav/mod_%{mod_name}-%{version}-%{apache_version}.tar.gz
URL:		http://www.webdav.org/mod_dav/
Prereq:		/usr/sbin/apxs
BuildRequires:	/usr/sbin/apxs
BuildRequires:	expat-devel
BuildRequires:	apache(EAPI)-devel	>= %{apache_version}
Requires:	apache(EAPI)		>= %{apache_version}
Requires:	expat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mod_dav

%define		_pkglibdir	%(%{_sbindir}/apxs -q LIBEXECDIR)

%description
mod_dav enables Apache to understand DAV protocol (extensions to
HTTP). DAV stands for "Distributed Authoring and Versioning", and is
defined by RFC 2518. DAV is intended to replace proprietary authoring
protocols such as those used by Frontpage or NetObjects' Fusion, but
is also a complete set of protocols for manipulating a webserver's
files and directories, and their properties.

%description -l pl
mod_dav w³±cza w Apache obs³ugê protoko³u DAV (rozszerzenie HTTP). DAV
oznacza "Dystrybuowane Oznaczanie i Wersjonowanie", i jest
zdefiniowany w RFC 2518. Podstawow± misj± DAV jest zast±piæ takie
protoko³y jak te u¿ywane w Frontpage czy NetObjects' Fusion. Lecz DAV
to tak¿e kompletny zestaw protoko³ów s³u¿±cych do manipulowania
plikami i katalogami serwera Web, oraz ich w³±¶ciwo¶ciami.

%prep 
%setup -q -n mod_%{mod_name}-%{version}-%{apache_version}

%build
CFLAGS="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O0 -g} %{?debug:-g -O0}"
%configure \
	--with-apxs=%{_sbindir}/apxs
%{__make} APXS=/usr/sbin/apxs

%install
install -d $RPM_BUILD_ROOT%{_pkglibdir}

install lib%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}/

gzip -9nf README CHANGES INSTALL

%post
%{_sbindir}/apxs -e -a -n %{mod_name} %{_pkglibdir}/lib%{mod_name}.so 1>&2
if [ -f /var/lock/subsys/httpd ]; then
	%{_sysconfdir}/rc.d/init.d/httpd restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	/usr/sbin/apxs -e -A -n %{mod_name} %{_pkglibdir}/lib%{mod_name}.so 1>&2
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz LICENSE.html
%attr(755,root,root) %{_pkglibdir}/*
