%define 	apxs	/usr/sbin/apxs
Summary:	WebDAV module for the Apache Web server
Summary(cs):	DAV modul pro WWW server Apache
Summary(da):	En DAV-modul for Apache
Summary(de):	Ein DAV-Modul für Apache
Summary(es):	Módulo DAV para Apache
Summary(fr):	Module DAV pour Apache
Summary(it):	Modulo DAV per Apache
Summary(ja):	Apache ÍÑ¤Î DAV ¥â¥¸¥å¡¼¥ë
Summary(no):	En DAV-modul for Apache
Summary(pl):	Modu³ WebDAV dla webserwera Apache
Summary(pt):	Um módulo de DAV para o Apache
Summary(ru):	íÏÄÕÌØ, ÒÅÁÌÉÚÕÀÝÉÊ ÐÒÏÔÏËÏÌ DAV × Apache
Summary(sv):	En DAV-modul till Apache
Summary(uk):	íÏÄÕÌØ, ÝÏ ÒÅÁÌ¦ÚÕ¤ ÐÒÏÔÏËÏÌ DAV × Apache
%define		apache_version	1.3.6
%define		mod_name	dav
Name:		apache-mod_%{mod_name}
Version:	1.0.3
Release:	5
License:	OSI Approved
Group:		Networking/Daemons
Source0:	http://www.webdav.org/mod_dav/mod_%{mod_name}-%{version}-%{apache_version}.tar.gz
Source1:	%{name}.conf
URL:		http://www.webdav.org/mod_dav/
Prereq:		%{_sbindir}/apxs
BuildRequires:	expat-devel
BuildRequires:	%{apxs}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	apache(EAPI)-devel	>= %{apache_version}
Requires:	apache(EAPI)		>= %{apache_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	mod_dav

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR)

%description
mod_dav enables Apache to understand DAV protocol (extensions to
HTTP). DAV stands for "Distributed Authoring and Versioning", and is
defined by RFC 2518. DAV is intended to replace proprietary authoring
protocols such as those used by Frontpage or NetObjects' Fusion, but
is also a complete set of protocols for manipulating a webserver's
files and directories, and their properties.

%description -l cs
Modul mod_dav roz¹iøuje WWW server Apache o podporu protokolu DAV
(Distributed Authoring a Versioning). Tento protokol roz¹iøuje HTTP
protokol o mo¾nosti vzdálené manipulace s obsahem WWW serveru. Je
zamý¹len jako náhrada za proprietální protokoly, které jsou pou¾ívány
programy FrontPage nebo NetObjects' Fusion. Poskytuje kompletní sadu
protokolù pro manipulaci se soubory, adresáøi a jejich vlastnostmi na
WWW serveru.

%description -l de
Das mod_dav Modul gibt dem Apche Webserver die Möglichkeit, das DAV
(Distributed Authoring and Versioning) Protokoll mit
HTTP-Erweiterungen zu verstehen. DAV ist ein komplettes Set von
Protokollen zur Bearbeitung der Dateien und Verzeichnisse sowie deren
Eigenschaften auf einem Webserver. Es soll die proprietären
Authoring-Protokolle, wie sie z.B. von FrontPage und NetObjects'
Fusion genutzt werden, ersetzen.

%description -l es
El módulo mod_dav da al servidor web Apache la capacidad de entender
que el protocolo DAV (Dristruted Authoring and Versioning) de
extensiones HTTP .DAV a completar un conjunto de protocolos para
manipular los ficheros de un servidor Web los ficheros y directorios y
sus características. Se piensa para substituir al propietario,
autorizando protocolos tales como ésos usados por FrontPage y la
fusión de NetObjets.

%description -l fr
Le module mod_dav donne au serveur Apache la possibilité de comprendre
le protocole DAV (Distributed Authoring and Versioning) des extensions
à HTTP. DAV est un ensemble complet de protocoles pour la manipulation
des fichiers et des répertoires d'un serveur Web et de leurs
propriétés. Il a pour but de remplacer les protocoles
d'authentification de propriétés comme ceux utilisés par FrontPage et
NetObject's Fusion.

%description -l it
Il modulo mod_dav permette al server web Apache di comprendere il
protocollo DAV (Distributed Authoring and Versioning) delle estensioni
per HTTP. DAV è una serie completa di protocolli per l'elaborazione di
file e di directory di un server Web e delle loro proprietà. E' stato
ideato per sostituire i protocolli di autenticazione proprietari come
quelli utilizzati da FrontPage e da NetObject's Fusion.

%description -l ja
mod_dav ¥â¥¸¥å¡¼¥ë¤Ï¡¢Apache Web ¥µ¡¼¥Ð¡¼¤Ë HTTP ¤Î³ÈÄ¥µ¡Ç½¤Î DAV
(Distributed Authoring and Versioning) ¥×¥í¥È¥³¥ë¤òÇ§¼± ¤µ¤»¤Þ¤¹¡£DAV
¤Ï¡¢Web ¥µ¡¼¥Ð¡¼¤Î¥Õ¥¡¥¤¥ë¤È¥Ç¥£¥ì¥¯¥È¥ê¡¢
¤½¤Î¥×¥í¥Ñ¥Æ¥£¤òÁàºî¤¹¤ë¤¿¤á¤Î¥×¥í¥È¥³¥ë¤Î´°Á´¤Ê¥»¥Ã¥È ¤Ç¤¹¡£FrontPage
¤ä NetObject ¤Î Fusion ¤¬»ÈÍÑ¤¹¤ë¤è¤¦¤Ê
½êÍ­¸¢¤Î¤¢¤ë¥ª¡¼¥µ¥ê¥ó¥°¥×¥í¥È¥³¥ë¤ÈÃÖ¤­´¹¤¨¤ë¤³¤È¤òÌÜÅª¤È¤·¤Þ¤¹¡£

%description -l pl
mod_dav w³±cza w Apache obs³ugê protoko³u DAV (rozszerzenie HTTP). DAV
oznacza "Dystrybuowane Oznaczanie i Wersjonowanie", i jest
zdefiniowany w RFC 2518. Podstawow± misj± DAV jest zast±piæ takie
protoko³y jak te u¿ywane w Frontpage czy NetObjects' Fusion. Lecz DAV
to tak¿e kompletny zestaw protoko³ów s³u¿±cych do manipulowania
plikami i katalogami serwera Web, oraz ich w³±¶ciwo¶ciami.

%description -l pt
O módulo mod_dav dá ao servidor Web Apache a possibilidade de aceitar
o protocolo de extensões de HTTP DAV (Distributed Authoring and
Versioning). O DAV é um conjunto completo de protocolos para manipular
os ficheiros e directorias dum servidor Web e as suas propriedades.
Pretende substituir os protocolos proprietários de 'authoring' tais
como os usados pelo FrontPage e pelo Fusion da NetObjects.

%description -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÍÏÄÕÌØ, ËÏÔÏÒÙÊ ÐÏÚ×ÏÌÑÅÔ Apache ÐÏÎÉÍÁÔØ ÐÒÏÔÏËÏÌ
DAV (ÒÁÓÛÉÒÅÎÉÅ ÐÒÏÔÏËÏÌÁ HTTP). DAV ÏÚÎÁÞÁÅÔ "Distributed Authoring
and Versioning", ÜÔÏÔ ÐÒÏÔÏËÏÌ ÏÐÉÓÁÎ × RFC 2518. DAV ÐÒÅÄÎÁÚÎÁÞÅÎ ÄÌÑ
ÚÁÍÅÎÙ ÓÏÂÓÔ×ÅÎÎÙÈ ÐÒÏÔÏËÏÌÏ×, ÔÁËÉÈ ËÁË ÉÓÐÏÌØÚÕÅÍÙÅ × Frontpage, ÉÌÉ
× Fusion ÏÔ NetObjects.

%description -l sv
Modulen mod_dav ger webbervern Apache förmågan att förstå protokollet
DAV (Distributed Authoring and Versioning) som utvidgar HTTP. DAV är
en komplett uppsättning protokoll för att hantera en webbservers filer
och kataloger och deras egenskaper. Det är avsett att ersätta privata
författarptotokoll såsom de som används av FrontPage och NetObjects
Fusion.

%description -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÍÏÄÕÌØ, ÑËÉÊ ÄÏÚ×ÏÌÑ¤ Apache ÒÏÚÕÍ¦ÔÉ ÐÒÏÔÏËÏÌ DAV
(ÒÏÚÛÉÒÅÎÎÑ ÐÒÏÔÏËÏÌÕ HTTP). DAV ÏÚÎÁÞÁ¤ "Distributed Authoring and
Versioning", ÃÅÊ ÐÒÏÔÏËÏÌ ÏÐÉÓÁÎÉÊ × RFC 2518. DAV ÐÒÉÚÎÁÞÅÎÉÊ ÄÌÑ
ÚÁÍ¦ÎÉ ×ÌÁÓÎÉÈ ÐÒÏÔÏËÏÌ¦×, ÔÁËÉÈ ÑË ×ÉËÏÒÉÓÔÏ×Õ×ÁÎ¦ × Frontpage, ÞÉ ×
Fusion ×¦Ä NetObjects.

%prep
%setup -q -n mod_%{mod_name}-%{version}-%{apache_version}

%build
%{__aclocal}
%{__autoconf}
%configure \
	--with-apxs=%{apxs} \
	--with-expat=%{_prefix}
%{__make} APXS=%{apxs}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},/etc/httpd,/var/lock/mod_dav}

install lib%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}/
install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/mod_dav.conf

%post
%{apxs} -e -a -n %{mod_name} %{_pkglibdir}/lib%{mod_name}.so 1>&2
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*mod_dav.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/mod_dav.conf" >> /etc/httpd/httpd.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	%{_sysconfdir}/rc.d/init.d/httpd restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	%{apxs} -e -A -n %{mod_name} %{_pkglibdir}/lib%{mod_name}.so 1>&2
	grep -v "^Include.*mod_dav.conf" /etc/httpd/httpd.conf > \
		/etc/httpd/httpd.conf.tmp
	mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
	if [ -f /var/lock/subsys/httpd ]; then
		/etc/rc.d/init.d/httpd restart 1>&2
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES INSTALL LICENSE.html
%config(noreplace) /etc/httpd/mod_dav.conf
%attr(755,root,root) %{_pkglibdir}/*
%attr(750,http,http) /var/lock/mod_dav
