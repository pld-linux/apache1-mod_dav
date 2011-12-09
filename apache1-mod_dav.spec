%define		mod_name	dav
%define 	apxs	/usr/sbin/apxs1
%define		apache_version	1.3.6
Summary:	WebDAV module for the Apache Web server
Summary(cs.UTF-8):	DAV modul pro WWW server Apache
Summary(da.UTF-8):	En DAV-modul for Apache
Summary(de.UTF-8):	Ein DAV-Modul für Apache
Summary(es.UTF-8):	Módulo DAV para Apache
Summary(fr.UTF-8):	Module DAV pour Apache
Summary(it.UTF-8):	Modulo DAV per Apache
Summary(ja.UTF-8):	Apache 用の DAV モジュール
Summary(nb.UTF-8):	En DAV-modul for Apache
Summary(pl.UTF-8):	Moduł WebDAV dla webserwera Apache
Summary(pt.UTF-8):	Um módulo de DAV para o Apache
Summary(ru.UTF-8):	Модуль, реализующий протокол DAV в Apache
Summary(sv.UTF-8):	En DAV-modul till Apache
Summary(uk.UTF-8):	Модуль, що реалізує протокол DAV в Apache
Name:		apache1-mod_%{mod_name}
Version:	1.0.3
Release:	3
License:	OSI Approved
Group:		Networking/Daemons
Source0:	http://www.webdav.org/mod_dav/mod_%{mod_name}-%{version}-%{apache_version}.tar.gz
# Source0-md5:	ba83f2aa6e13b216a11d465b82aab484
Source1:	%{name}.conf
Patch0:		%{name}-format.patch
URL:		http://www.webdav.org/mod_dav/
BuildRequires:	apache1-devel >= 1.3.39
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(triggerpostun):	%{apxs}
Requires(triggerpostun):	grep
Requires(triggerpostun):	sed >= 4.0
Requires:	apache1(EAPI)
Obsoletes:	apache-mod_dav <= 1.0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)/conf.d

%description
mod_dav enables Apache to understand DAV protocol (extensions to
HTTP). DAV stands for "Distributed Authoring and Versioning", and is
defined by RFC 2518. DAV is intended to replace proprietary authoring
protocols such as those used by Frontpage or NetObjects' Fusion, but
is also a complete set of protocols for manipulating a webserver's
files and directories, and their properties.

%description -l cs.UTF-8
Modul mod_dav rozšiřuje WWW server Apache o podporu protokolu DAV
(Distributed Authoring a Versioning). Tento protokol rozšiřuje HTTP
protokol o možnosti vzdálené manipulace s obsahem WWW serveru. Je
zamýšlen jako náhrada za proprietální protokoly, které jsou používány
programy FrontPage nebo NetObjects' Fusion. Poskytuje kompletní sadu
protokolů pro manipulaci se soubory, adresáři a jejich vlastnostmi na
WWW serveru.

%description -l de.UTF-8
Das mod_dav Modul gibt dem Apche Webserver die Möglichkeit, das DAV
(Distributed Authoring and Versioning) Protokoll mit
HTTP-Erweiterungen zu verstehen. DAV ist ein komplettes Set von
Protokollen zur Bearbeitung der Dateien und Verzeichnisse sowie deren
Eigenschaften auf einem Webserver. Es soll die proprietären
Authoring-Protokolle, wie sie z.B. von FrontPage und NetObjects'
Fusion genutzt werden, ersetzen.

%description -l es.UTF-8
El módulo mod_dav da al servidor web Apache la capacidad de entender
que el protocolo DAV (Dristruted Authoring and Versioning) de
extensiones HTTP .DAV a completar un conjunto de protocolos para
manipular los ficheros de un servidor Web los ficheros y directorios y
sus características. Se piensa para substituir al propietario,
autorizando protocolos tales como ésos usados por FrontPage y la
fusión de NetObjets.

%description -l fr.UTF-8
Le module mod_dav donne au serveur Apache la possibilité de comprendre
le protocole DAV (Distributed Authoring and Versioning) des extensions
à HTTP. DAV est un ensemble complet de protocoles pour la manipulation
des fichiers et des répertoires d'un serveur Web et de leurs
propriétés. Il a pour but de remplacer les protocoles
d'authentification de propriétés comme ceux utilisés par FrontPage et
NetObject's Fusion.

%description -l it.UTF-8
Il modulo mod_dav permette al server web Apache di comprendere il
protocollo DAV (Distributed Authoring and Versioning) delle estensioni
per HTTP. DAV è una serie completa di protocolli per l'elaborazione di
file e di directory di un server Web e delle loro proprietà. E' stato
ideato per sostituire i protocolli di autenticazione proprietari come
quelli utilizzati da FrontPage e da NetObject's Fusion.

%description -l ja.UTF-8
mod_dav モジュールは、Apache Web サーバーに HTTP の拡張機能の DAV
(Distributed Authoring and Versioning) プロトコルを認識 させます。DAV
は、Web サーバーのファイルとディレクトリ、
そのプロパティを操作するためのプロトコルの完全なセット です。FrontPage
や NetObject の Fusion が使用するような
所有権のあるオーサリングプロトコルと置き換えることを目的とします。

%description -l pl.UTF-8
mod_dav włącza w Apache obsługę protokołu DAV (rozszerzenie HTTP). DAV
oznacza "Dystrybuowane Oznaczanie i Wersjonowanie", i jest
zdefiniowany w RFC 2518. Podstawową misją DAV jest zastąpić takie
protokoły jak te używane w Frontpage czy NetObjects' Fusion. Lecz DAV
to także kompletny zestaw protokołów służących do manipulowania
plikami i katalogami serwera Web, oraz ich właściwościami.

%description -l pt.UTF-8
O módulo mod_dav dá ao servidor Web Apache a possibilidade de aceitar
o protocolo de extensões de HTTP DAV (Distributed Authoring and
Versioning). O DAV é um conjunto completo de protocolos para manipular
os ficheiros e directorias dum servidor Web e as suas propriedades.
Pretende substituir os protocolos proprietários de 'authoring' tais
como os usados pelo FrontPage e pelo Fusion da NetObjects.

%description -l ru.UTF-8
Этот пакет содержит модуль, который позволяет Apache понимать протокол
DAV (расширение протокола HTTP). DAV означает "Distributed Authoring
and Versioning", этот протокол описан в RFC 2518. DAV предназначен для
замены собственных протоколов, таких как используемые в Frontpage, или
в Fusion от NetObjects.

%description -l sv.UTF-8
Modulen mod_dav ger webbervern Apache förmågan att förstå protokollet
DAV (Distributed Authoring and Versioning) som utvidgar HTTP. DAV är
en komplett uppsättning protokoll för att hantera en webbservers filer
och kataloger och deras egenskaper. Det är avsett att ersätta privata
författarptotokoll såsom de som används av FrontPage och NetObjects
Fusion.

%description -l uk.UTF-8
Цей пакет містить модуль, який дозволяє Apache розуміти протокол DAV
(розширення протоколу HTTP). DAV означає "Distributed Authoring and
Versioning", цей протокол описаний в RFC 2518. DAV призначений для
заміни власних протоколів, таких як використовувані в Frontpage, чи в
Fusion від NetObjects.

%prep
%setup -q -n mod_%{mod_name}-%{version}-%{apache_version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-apxs=%{apxs} \
	--with-expat=%{_prefix}
%{__make} APXS=%{apxs}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir},/var/lock/mod_dav}

install lib%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/90_mod_%{mod_name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q apache restart

%postun
if [ "$1" = "0" ]; then
	%service -q apache restart
fi

%triggerpostun -- %{name} < 1.0.3-1.1
if grep -q '^Include conf\.d/\*\.conf' /etc/apache/apache.conf; then
	%{apxs} -e -A -n %{mod_name} %{_pkglibdir}/libdav.so 1>&2
	sed -i -e '
		/^Include.*mod_%{mod_name}\.conf/d
	' /etc/apache/apache.conf
else
	# they're still using old apache.conf
	sed -i -e '
		s,^Include.*mod_%{mod_name}\.conf,Include %{_sysconfdir}/*_mod_%{mod_name}.conf,
	' /etc/apache/apache.conf
fi
if [ -f /var/lock/subsys/apache ]; then
	/etc/rc.d/init.d/apache restart 1>&2
fi

%files
%defattr(644,root,root,755)
%doc README CHANGES INSTALL LICENSE.html
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/*
%attr(750,http,http) /var/lock/mod_dav
