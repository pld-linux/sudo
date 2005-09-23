#
# Conditional build:
%bcond_without	selinux		# build without SELinux support
%bcond_without	skey		# disable skey (onetime passwords) support
%bcond_without	heimdal		# disable Kerberos support
%bcond_without	ldap		# disable LDAP support
#
Summary:	Allows command execution as root for specified users
Summary(es):	Permite que usuarios específicos ejecuten comandos como se fueran el root
Summary(ja):	»ØÄê¥æ¡¼¥¶¤ËÀ©¸ÂÉÕ¤Îroot¸¢¸Â¤òµö²Ä¤¹¤ë
Summary(pl):	Umo¿liwia wykonywanie poleceñ jako root dla konkretnych u¿ytkowników
Summary(pt_BR):	Permite que usuários específicos executem comandos como se fossem o root
Summary(ru):	ðÏÚ×ÏÌÑÅÔ ÏÐÒÅÄÅÌÅÎÎÙÍ ÐÏÌØÚÏ×ÁÔÅÌÑÍ ÉÓÐÏÌÎÑÔØ ËÏÍÁÎÄÙ ÏÔ ÉÍÅÎÉ root
Summary(uk):	äÏÚ×ÏÌÑ¤ ×ËÁÚÁÎÉÍ ËÏÒÉÓÔÕ×ÁÞÁÍ ×ÉËÏÎÕ×ÁÔÉ ËÏÍÁÎÄÉ ×¦Ä ¦ÍÅÎ¦ root
Name:		sudo
Version:	1.6.8p9
Release:	2
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.courtesan.com/pub/sudo/%{name}-%{version}.tar.gz
# Source0-md5:	6d0346abd16914956bc7ea4f17fc85fb
Source1:	%{name}.pamd
Source2:	%{name}.logrotate
Patch0:		%{name}-selinux.patch
Patch1:		%{name}-ac.patch
URL:		http://www.courtesan.com/sudo/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
%{?with_selinux:BuildRequires:	libselinux-devel}
%{?with_heimdal:BuildRequires:	heimdal-devel >= 0.7}
%{?with_ldap:BuildRequires:	openldap-devel}
%{?with_skey:BuildRequires:	skey-devel >= 2.2-11}
BuildRequires:	libtool
BuildRequires:	pam-devel
Requires:	pam >= 0.77.3
Obsoletes:	cu-sudo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sudo (superuser do) allows a permitted user to execute a command as
the superuser (real and effective uid and gid are set to 0 and root's
group as set in the passwd file respectively).

Sudo determines who is an authorized user by consulting the file
/etc/sudoers. By giving sudo the -v flag a user can update the time
stamp without running a command. The password prompt itself will also
time out if the password is not entered with N minutes (again, this is
defined at installation time and defaults to 5 minutes).

%description -l es
Sudo (superuser do) permite que el administrador del sistema otorga a
ciertos usuarios (o grupos de usuarios) la habilidad para ejecutar
algunos (o todos) comandos como root, registrando todos los comandos y
argumentos. Sudo opera en una base por comando, no siendo un
substituto para la shell.

%description -l ja
sudo (superuser do)
¤È¤Ï¥·¥¹¥Æ¥à´ÉÍý¼Ô¤¬¡¢¿®ÍÑ¤Ç¤­¤ë¥æ¡¼¥¶(¤Þ¤¿¤Ï¥°¥ë¡¼¥×)¤ËÂÐ
¤·¤Æ¡¢¤¤¤¯¤Ä¤«(¤â¤·¤¯¤ÏÁ´¤Æ)¤Î¥³¥Þ¥ó¥É¤ò root
¤È¤·¤Æ¼Â¹Ô¤Ç¤­¤ë¤è¤¦¡¢¤½¤Î¥³¥Þ¥ó
¥É¤Î¼Â¹ÔÍúÎò¤Î¥í¥°¤ò¤È¤ê¤Ä¤Äµö²Ä¤¹¤ë»ÅÁÈ¤ß¤Ç¤¹¡£sudo
¤Ï¥³¥Þ¥ó¥É°ì¹ÔÃ±°Ì¤ÇÆ°ºî
¤·¤Þ¤¹¡£¥·¥§¥ë¤ÎÃÖ¤­´¹¤¨¤Ç¤Ï¤¢¤ê¤Þ¤»¤ó¡£°Ê²¼¤Îµ¡Ç½¤òÆâÂ¢¤·¤Æ¤¤¤Þ¤¹¡£¥Û¥¹¥ÈÃ±°Ì
¤Ç¡¢¤½¤Î¥³¥Þ¥ó¥É¤ò¼Â¹Ô²ÄÇ½¤Ê¥æ¡¼¥¶¤òÀ©¸Â¤¹¤ëµ¡Ç½¡¢³Æ¥³¥Þ¥ó¥É¤Ë¤Ä¤¤¤Æ¤Î(Ã¯¤¬¤Ê
¤Ë¤ò¼Â¹Ô¤·¤¿¤«¤Îº¯À×¤ò»Ä¤¹¤¿¤á¤Î)Ë­ÉÙ¤Ê¥í¥®¥ó¥°µ¡Ç½¡¢sudo
¥³¥Þ¥ó¥É¤Î¥¿¥¤¥à¥¢¥¦
¥È»þ´Ö¤òÀßÄê²ÄÇ½¡¢Ê£¿ô¤Î¥Þ¥·¥ó¤ÇÆ±°ì¤ÎÀßÄê¥Õ¥¡¥¤¥ë(sudoers)¤ò¶¦Í­¤¹¤ëµ¡Ç½¡¢¤¬
¤¢¤ê¤Þ¤¹¡£

%description -l pl
Sudo (superuser do) umo¿liwia wykonywanie konkretnych poleceñ jako
root dla wyspecyfikowanych u¿ytkowników (rzeczywiste i efektywne
uid/gid podczas wykonywania tych programów jest 0). To kto mo¿e
wykonywaæ konkretne polecenia i w jaki sposób ma byæ autoryzowany jest
opisane w pliku /etc/sudoers.

%description -l pt_BR
Sudo (superuser do) permite que o administrador do sistema dê a certos
usuários (ou grupos de usuários) a habilidade para rodar alguns (ou
todos) comandos como root, registrando todos os comandos e argumentos.
Sudo opera numa base por comando, não sendo um substituto para a
shell.

%description -l ru
Sudo (superuser do) ÐÏÚ×ÏÌÑÅÔ ÓÉÓÔÅÍÎÏÍÕ ÁÄÍÉÎÉÓÔÒÁÔÏÒÕ ÐÒÅÄÏÓÔÁ×ÌÑÔØ
ÏÐÒÅÄÅÌÅÎÎÙÍ ÐÏÌØÚÏ×ÁÔÅÌÑÍ (ÉÌÉ ÉÈ ÇÒÕÐÐÁÍ) ×ÏÚÍÏÖÎÏÓÔØ ÉÓÐÏÌÎÑÔØ
ÎÅËÏÔÏÒÙÅ (ÉÌÉ ×ÓÅ) ËÏÍÁÎÄÙ Ó ÐÒÁ×ÁÍÉ root, ÐÒÉ ÜÔÏÍ ÐÒÏÔÏËÏÌÉÒÕÑ ×ÓÅ
ËÏÍÁÎÄÙ É ÁÒÇÕÍÅÎÔÙ. Sudo ÒÁÂÏÔÁÅÔ Ó ÏÔÄÅÌØÎÙÍÉ ËÏÍÁÎÄÁÍÉ, ÜÔÏ ÎÅ
ÚÁÍÅÎÁ ËÏÍÁÎÄÎÏÊ ÏÂÏÌÏÞËÉ (shell). îÅËÏÔÏÒÙÅ ÉÚ ×ÏÚÍÏÖÎÏÓÔÅÊ sudo:
ÏÇÒÁÎÉÞÅÎÉÅ ÔÏÇÏ, ËÁËÉÅ ËÏÍÁÎÄÙ ÐÏÌØÚÏ×ÁÔÅÌØ ÍÏÖÅÔ ÚÁÐÕÓËÁÔØ ×
ÚÁ×ÉÓÉÍÏÓÔÉ ÏÔ ÈÏÓÔÁ; ÐÏÌÎÏÅ ÐÒÏÔÏËÏÌÉÒÏ×ÁÎÉÅ ËÁÖÄÏÊ ËÏÍÁÎÄÙ;
ÎÁÓÔÒÁÉ×ÁÅÍÏÅ ×ÒÅÍÑ, ÎÁ ÐÒÏÔÑÖÅÎÉÉ ËÏÔÏÒÏÇÏ sudo ÐÏÍÎÉÔ ÐÁÒÏÌØ;
ÉÓÐÏÌØÚÏ×ÁÎÉÅ ÏÄÎÏÇÏ ËÏÎÆÉÇÕÒÁÃÉÏÎÎÏÇÏ ÆÁÊÌÁ (sudoers) ÎÁ ÍÎÏÇÉÈ
ÍÁÛÉÎÁÈ.

%description -l uk
Sudo (superuser do) ÄÏÚ×ÏÌÑ¤ ÓÉÓÔÅÍÎÏÍÕ ÁÄÍ¦Î¦ÓÔÒÁÔÏÒÏ×¦ ÎÁÄÁÔÉ ÐÅ×ÎÉÍ
ËÏÒÉÓÔÕ×ÁÞÁÍ (ÞÉ §È ÇÒÕÐÁÍ) ÍÏÖÌÉ×¦ÓÔØ ×ÉËÏÎÕ×ÁÔÉ ÄÅÑË¦ (ÞÉ ×Ó¦)
ËÏÍÁÎÄÉ Ú ÐÒÁ×ÁÍÉ root, ÐÒÉ ÃØÏÍÕ ÐÒÏÔÏËÏÌÀÀÞÉ ×Ó¦ ËÏÍÁÎÄÉ ÔÁ
ÁÒÇÕÍÅÎÔÉ. Sudo ÐÒÁÃÀ¤ Ú ÏËÒÅÍÉÍÉ ËÏÍÁÎÄÁÍÉ, ÃÅ ÎÅ ÚÁÍ¦ÎÁ ËÏÍÁÎÄÎÏ§
ÏÂÏÌÏÎËÉ (shell). äÅÑË¦ Ú ÍÏÖÌÉ×ÏÓÔÅÊ sudo: ÏÂÍÅÖÅÎÎÑ ÔÏÇÏ, ÑË¦
ËÏÍÁÎÄÉ ËÏÒÉÓÔÕ×ÁÞ ÍÏÖÅ ÚÁÐÕÓËÁÔÉ × ÚÁÌÅÖÎÏÓÔ¦ ×¦Ä ÈÏÓÔÁ; ÐÏ×ÎÅ
ÐÒÏÔÏËÏÌÀ×ÁÎÎÑ ËÏÖÎÏ§ ËÏÍÁÎÄÉ; ÎÁÓÔÒÏÀ×ÁÎÉÊ ÞÁÓ, ÎÁ ÐÒÏÔÑÚ¦ ÑËÏÇÏ sudo
ÐÁÍ'ÑÔÁ¤ ÐÁÒÏÌØ; ×ÉËÏÒÉÓÔÁÎÎÑ ÏÄÎÏÇÏ ËÏÎÆ¦ÇÕÒÁÃ¦ÊÎÏÇÏ ÆÁÊÌÕ (sudoers)
ÎÁ ÂÁÇÁÔØÏÈ ÍÁÛÉÎÁÈ.

%prep
%setup -q
%{?with_selinux:%patch0 -p1}

# only local macros
mv -f aclocal.m4 acinclude.m4
# kill libtool.m4 copy
rm -f acsite.m4

%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
# sparc64 2.4.x kernels have buggy sys32_utimes(somefile, NULL) syscall
# it's fixed in >= 2.4.31-0.3, but keep workaround not to require very
# fresh kernel
%ifarch sparc sparcv9
export ac_cv_func_utimes=no
%endif
%configure \
	NROFFPROG=nroff \
	--with-incpath=/usr/include/security \
	--with-timedir=/var/run/sudo \
	--with-pam \
	--with-logging=both \
	--with-logfac=auth \
	--with-logpath=/var/log/sudo \
	--with-ignore-dot \
	--with-env-editor \
	--with-secure-path="/bin:/sbin:/usr/bin:/usr/sbin" \
	--with-loglen=320 \
	--disable-saved-ids \
	--with%{?with_heimdal:out}-kerb5 \
	--with%{?with_ldap:out}-ldap \
	--with%{?with_skey:out}-skey \
	--with-long-otp-prompt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{pam.d,logrotate.d},/var/{log,run/sudo}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	install_uid=`id -u` \
	install_gid=`id -g` \
	sudoers_uid=`id -u` \
	sudoers_gid=`id -g`

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/sudo
touch $RPM_BUILD_ROOT/var/log/sudo
install %{SOURCE2} $RPM_BUILD_ROOT/etc/logrotate.d/sudo

chmod -R +r $RPM_BUILD_ROOT%{_prefix}

rm -f $RPM_BUILD_ROOT%{_libdir}/sudo_noexec.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HISTORY README TODO TROUBLESHOOTING sample.sudoers
%attr(440,root,root) %verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/sudoers
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/sudo
%attr(4755,root,root) %{_bindir}/sudo
%attr(4755,root,root) %{_bindir}/sudoedit
%{?with_selinux:%attr(755,root,root) %{_sbindir}/sesh}
%attr(755,root,root) %{_sbindir}/visudo
%attr(755,root,root) %{_libdir}/sudo_noexec.so
%{_mandir}/man*/*
%attr(600,root,root) %ghost /var/log/sudo
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%attr(700,root,root) %dir /var/run/sudo
