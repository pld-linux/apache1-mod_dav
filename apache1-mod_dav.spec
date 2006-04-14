%define		mod_name	dav
%define 	apxs	/usr/sbin/apxs1
%define		apache_version	1.3.6
Summary:	WebDAV module for the Apache Web server
Summary(cs):	DAV modul pro WWW server Apache
Summary(da):	En DAV-modul for Apache
Summary(de):	Ein DAV-Modul fЭr Apache
Summary(es):	MСdulo DAV para Apache
Summary(fr):	Module DAV pour Apache
Summary(it):	Modulo DAV per Apache
Summary(ja):	Apache мя╓н DAV ╔Б╔╦╔Е║╪╔К
Summary(nb):	En DAV-modul for Apache
Summary(pl):	ModuЁ WebDAV dla webserwera Apache
Summary(pt):	Um mСdulo de DAV para o Apache
Summary(ru):	Модуль, реализующий протокол DAV в Apache
Summary(sv):	En DAV-modul till Apache
Summary(uk):	Модуль, що реал╕зу╓ протокол DAV в Apache
Name:		apache1-mod_%{mod_name}
Version:	1.0.3
Release:	2
License:	OSI Approved
Group:		Networking/Daemons
Source0:	http://www.webdav.org/mod_dav/mod_%{mod_name}-%{version}-%{apache_version}.tar.gz
# Source0-md5:	ba83f2aa6e13b216a11d465b82aab484
Source1:	%{name}.conf
Patch0:		%{name}-format.patch
URL:		http://www.webdav.org/mod_dav/
BuildRequires:	%{apxs}
BuildRequires:	apache1-devel >= 1.3.33-2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(triggerpostun):	%{apxs}
Requires(triggerpostun):	grep
Requires(triggerpostun):	sed >= 4.0
Requires:	apache1 >= 1.3.33-2
Obsoletes:	apache-mod_dav <= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

%description
mod_dav enables Apache to understand DAV protocol (extensions to
HTTP). DAV stands for "Distributed Authoring and Versioning", and is
defined by RFC 2518. DAV is intended to replace proprietary authoring
protocols such as those used by Frontpage or NetObjects' Fusion, but
is also a complete set of protocols for manipulating a webserver's
files and directories, and their properties.

%description -l cs
Modul mod_dav roz╧iЬuje WWW server Apache o podporu protokolu DAV
(Distributed Authoring a Versioning). Tento protokol roz╧iЬuje HTTP
protokol o mo╬nosti vzdАlenИ manipulace s obsahem WWW serveru. Je
zamЩ╧len jako nАhrada za proprietАlnМ protokoly, kterИ jsou pou╬МvАny
programy FrontPage nebo NetObjects' Fusion. Poskytuje kompletnМ sadu
protokolЫ pro manipulaci se soubory, adresАЬi a jejich vlastnostmi na
WWW serveru.

%description -l de
Das mod_dav Modul gibt dem Apche Webserver die MЖglichkeit, das DAV
(Distributed Authoring and Versioning) Protokoll mit
HTTP-Erweiterungen zu verstehen. DAV ist ein komplettes Set von
Protokollen zur Bearbeitung der Dateien und Verzeichnisse sowie deren
Eigenschaften auf einem Webserver. Es soll die proprietДren
Authoring-Protokolle, wie sie z.B. von FrontPage und NetObjects'
Fusion genutzt werden, ersetzen.

%description -l es
El mСdulo mod_dav da al servidor web Apache la capacidad de entender
que el protocolo DAV (Dristruted Authoring and Versioning) de
extensiones HTTP .DAV a completar un conjunto de protocolos para
manipular los ficheros de un servidor Web los ficheros y directorios y
sus caracterМsticas. Se piensa para substituir al propietario,
autorizando protocolos tales como Иsos usados por FrontPage y la
fusiСn de NetObjets.

%description -l fr
Le module mod_dav donne au serveur Apache la possibilitИ de comprendre
le protocole DAV (Distributed Authoring and Versioning) des extensions
Ю HTTP. DAV est un ensemble complet de protocoles pour la manipulation
des fichiers et des rИpertoires d'un serveur Web et de leurs
propriИtИs. Il a pour but de remplacer les protocoles
d'authentification de propriИtИs comme ceux utilisИs par FrontPage et
NetObject's Fusion.

%description -l it
Il modulo mod_dav permette al server web Apache di comprendere il
protocollo DAV (Distributed Authoring and Versioning) delle estensioni
per HTTP. DAV Х una serie completa di protocolli per l'elaborazione di
file e di directory di un server Web e delle loro proprietЮ. E' stato
ideato per sostituire i protocolli di autenticazione proprietari come
quelli utilizzati da FrontPage e da NetObject's Fusion.

%description -l ja
mod_dav ╔Б╔╦╔Е║╪╔К╓о║╒Apache Web ╔╣║╪╔п║╪╓к HTTP ╓нЁхд╔╣║г╫╓н DAV
(Distributed Authoring and Versioning) ╔в╔М╔х╔Ё╔К╓Рг╖╪╠ ╓╣╓╩╓ч╓╧║ёDAV
╓о║╒Web ╔╣║╪╔п║╪╓н╔у╔║╔╓╔К╓х╔г╔ё╔Л╔╞╔х╔Й║╒
╓╫╓н╔в╔М╔я╔ф╔ё╓РаЮ╨Н╓╧╓К╓©╓А╓н╔в╔М╔х╔Ё╔К╓н╢╟а╢╓й╔╩╔ц╔х ╓г╓╧║ёFrontPage
╓Д NetObject ╓н Fusion ╓╛╩хмя╓╧╓К╓Х╓╕╓й
╫Йм╜╦╒╓н╓╒╓К╔╙║╪╔╣╔Й╔С╔╟╔в╔М╔х╔Ё╔К╓хцж╓╜╢╧╓╗╓К╓Ё╓х╓Рлэе╙╓х╓╥╓ч╓╧║ё

%description -l pl
mod_dav wЁ╠cza w Apache obsЁugЙ protokoЁu DAV (rozszerzenie HTTP). DAV
oznacza "Dystrybuowane Oznaczanie i Wersjonowanie", i jest
zdefiniowany w RFC 2518. Podstawow╠ misj╠ DAV jest zast╠piФ takie
protokoЁy jak te u©ywane w Frontpage czy NetObjects' Fusion. Lecz DAV
to tak©e kompletny zestaw protokoЁСw sЁu©╠cych do manipulowania
plikami i katalogami serwera Web, oraz ich wЁa╤ciwo╤ciami.

%description -l pt
O mСdulo mod_dav dА ao servidor Web Apache a possibilidade de aceitar
o protocolo de extensУes de HTTP DAV (Distributed Authoring and
Versioning). O DAV И um conjunto completo de protocolos para manipular
os ficheiros e directorias dum servidor Web e as suas propriedades.
Pretende substituir os protocolos proprietАrios de 'authoring' tais
como os usados pelo FrontPage e pelo Fusion da NetObjects.

%description -l ru
Этот пакет содержит модуль, который позволяет Apache понимать протокол
DAV (расширение протокола HTTP). DAV означает "Distributed Authoring
and Versioning", этот протокол описан в RFC 2518. DAV предназначен для
замены собственных протоколов, таких как используемые в Frontpage, или
в Fusion от NetObjects.

%description -l sv
Modulen mod_dav ger webbervern Apache fЖrmЕgan att fЖrstЕ protokollet
DAV (Distributed Authoring and Versioning) som utvidgar HTTP. DAV Дr
en komplett uppsДttning protokoll fЖr att hantera en webbservers filer
och kataloger och deras egenskaper. Det Дr avsett att ersДtta privata
fЖrfattarptotokoll sЕsom de som anvДnds av FrontPage och NetObjects
Fusion.

%description -l uk
Цей пакет м╕стить модуль, який дозволя╓ Apache розум╕ти протокол DAV
(розширення протоколу HTTP). DAV означа╓ "Distributed Authoring and
Versioning", цей протокол описаний в RFC 2518. DAV призначений для
зам╕ни власних протокол╕в, таких як використовуван╕ в Frontpage, чи в
Fusion в╕д NetObjects.

%prep
%setup -q -n mod_%{mod_name}-%{version}-%{apache_version}
%patch -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-apxs=%{apxs} \
	--with-expat=%{_prefix}
%{__make} APXS=%{apxs}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir}/conf.d,/var/lock/mod_dav}

install lib%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/90_mod_%{mod_name}.conf

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
		s,^Include.*mod_%{mod_name}\.conf,Include %{_sysconfdir}/conf.d/*_mod_%{mod_name}.conf,
	' /etc/apache/apache.conf
fi
if [ -f /var/lock/subsys/apache ]; then
	/etc/rc.d/init.d/apache restart 1>&2
fi

%files
%defattr(644,root,root,755)
%doc README CHANGES INSTALL LICENSE.html
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/*
%attr(750,http,http) /var/lock/mod_dav
