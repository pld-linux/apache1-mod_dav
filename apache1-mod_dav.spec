%define		apache_version	1.3.6
%define		mod_name	dav
Summary:	WebDAV module for the Apache Web server
Summary(pl):	Modu³ WebDAV dla webserwera Apache
Name:		apache-mod_%{mod_name}
Version:	1.0.2
Release:	1
License:	OSI Approved
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://www.webdav.org/mod_%{mod_name}/mod_%{mod_name}-%{version}-%{apache_version}.tar.gz
URL:		http://www.webdav.org/mod_%{mod_name}
Prereq:		/usr/sbin/apxs
BuildRequires:	expat-devel
BuildRequires:	apache(EAPI)-devel	>= %{apache_version}
Requires:	apache(EAPI)		>= %{apache_version}
Requires:	expat
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%configure \
	--with-apxs=%{_sbindir}/apxs
%{__make} APXS=%{_sbindir}/apxs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkglibdir}

install *.so $RPM_BUILD_ROOT%{_pkglibdir}

gzip -9nf README CHANGES INSTALL LICENSE.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_pkglibdir}/*
