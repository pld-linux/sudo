#
# Conditional build:
%bcond_with	kerberos5	# enable Kerberos V support (conflicts with PAM)
%bcond_without	ldap		# disable LDAP support
%bcond_without	pam		# disable PAM support
%bcond_without	selinux		# build without SELinux support
%bcond_with	skey		# enable skey (onetime passwords) support (conflicts with PAM)
#
Summary:	Allows command execution as root for specified users
Summary(es.UTF-8):	Permite que usuarios específicos ejecuten comandos como se fueran el root
Summary(ja.UTF-8):	指定ユーザに制限付のroot権限を許可する
Summary(pl.UTF-8):	Umożliwia wykonywanie poleceń jako root dla konkretnych użytkowników
Summary(pt_BR.UTF-8):	Permite que usuários específicos executem comandos como se fossem o root
Summary(ru.UTF-8):	Позволяет определенным пользователям исполнять команды от имени root
Summary(uk.UTF-8):	Дозволяє вказаним користувачам виконувати команди від імені root
Name:		sudo
Version:	1.7.2p6
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.sudo.ws/pub/sudo/%{name}-%{version}.tar.gz
# Source0-md5:	c4f1a43e8ba94f6bf06d2211442148c4
Source1:	%{name}.pamd
Source2:	%{name}-i.pamd
Source3:	%{name}.logrotate
Patch0:		%{name}-pam-login.patch
Patch1:		%{name}-libtool.patch
Patch2:		%{name}-env.patch
URL:		http://www.sudo.ws/sudo/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
%{?with_kerberos5:BuildRequires:	heimdal-devel}
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_pam:BuildRequires:	pam-devel}
%{?with_skey:BuildRequires:	skey-devel >= 2.2-11}
Requires:	pam >= 0.99.7.1
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

%description -l es.UTF-8
Sudo (superuser do) permite que el administrador del sistema otorga a
ciertos usuarios (o grupos de usuarios) la habilidad para ejecutar
algunos (o todos) comandos como root, registrando todos los comandos y
argumentos. Sudo opera en una base por comando, no siendo un
substituto para la shell.

%description -l ja.UTF-8
sudo (superuser do)
とはシステム管理者が、信用できるユーザ(またはグループ)に対
して、いくつか(もしくは全て)のコマンドを root
として実行できるよう、そのコマン
ドの実行履歴のログをとりつつ許可する仕組みです。sudo
はコマンド一行単位で動作
します。シェルの置き換えではありません。以下の機能を内蔵しています。ホスト単位
で、そのコマンドを実行可能なユーザを制限する機能、各コマンドについての(誰がな
にを実行したかの痕跡を残すための)豊富なロギング機能、sudo
コマンドのタイムアウ
ト時間を設定可能、複数のマシンで同一の設定ファイル(sudoers)を共有する機能、が
あります。

%description -l pl.UTF-8
Sudo (superuser do) umożliwia wykonywanie konkretnych poleceń jako
root dla wyspecyfikowanych użytkowników (rzeczywiste i efektywne
uid/gid podczas wykonywania tych programów jest 0). To kto może
wykonywać konkretne polecenia i w jaki sposób ma być autoryzowany jest
opisane w pliku /etc/sudoers.

%description -l pt_BR.UTF-8
Sudo (superuser do) permite que o administrador do sistema dê a certos
usuários (ou grupos de usuários) a habilidade para rodar alguns (ou
todos) comandos como root, registrando todos os comandos e argumentos.
Sudo opera numa base por comando, não sendo um substituto para a
shell.

%description -l ru.UTF-8
Sudo (superuser do) позволяет системному администратору предоставлять
определенным пользователям (или их группам) возможность исполнять
некоторые (или все) команды с правами root, при этом протоколируя все
команды и аргументы. Sudo работает с отдельными командами, это не
замена командной оболочки (shell). Некоторые из возможностей sudo:
ограничение того, какие команды пользователь может запускать в
зависимости от хоста; полное протоколирование каждой команды;
настраиваемое время, на протяжении которого sudo помнит пароль;
использование одного конфигурационного файла (sudoers) на многих
машинах.

%description -l uk.UTF-8
Sudo (superuser do) дозволяє системному адміністраторові надати певним
користувачам (чи їх групам) можливість виконувати деякі (чи всі)
команди з правами root, при цьому протоколюючи всі команди та
аргументи. Sudo працює з окремими командами, це не заміна командної
оболонки (shell). Деякі з можливостей sudo: обмеження того, які
команди користувач може запускати в залежності від хоста; повне
протоколювання кожної команди; настроюваний час, на протязі якого sudo
пам'ятає пароль; використання одного конфігураційного файлу (sudoers)
на багатьох машинах.

%prep
%setup -q
# only local macros
mv -f aclocal.m4 acinclude.m4
# kill libtool.m4 copy
rm -f acsite.m4

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__mv} install-sh install-custom-sh
%{__libtoolize}
%{__mv} install-custom-sh install-sh
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure \
	NROFFPROG=nroff \
	--with-incpath=/usr/include/security \
	--with-timedir=/var/run/sudo \
	--with-pam \
	--with-pam-login \
	--with-logging=both \
	--with-logfac=auth \
	--with-logpath=/var/log/sudo \
	--with-ignore-dot \
	--with-env-editor \
	--with-secure-path="/bin:/sbin:/usr/bin:/usr/sbin" \
	--with-loglen=320 \
	--with%{!?with_kerberos5:out}-kerb5 \
	--with%{!?with_ldap:out}-ldap \
	--with%{!?with_skey:out}-skey \
	--with%{!?with_selinux:out}-selinux \
	--with-long-otp-prompt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{pam.d,logrotate.d},/var/{log,run/sudo},%{_mandir}/man8}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	install_uid=`id -u` \
	install_gid=`id -g` \
	sudoers_uid=`id -u` \
	sudoers_gid=`id -g`

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/sudo
install %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/sudo-i
touch $RPM_BUILD_ROOT/var/log/sudo
install %{SOURCE3} $RPM_BUILD_ROOT/etc/logrotate.d/sudo

chmod -R +r $RPM_BUILD_ROOT%{_prefix}

rm -f $RPM_BUILD_ROOT%{_libdir}/sudo_noexec.la

# replace hardlinks with symlinks
ln -sf %{_bindir}/sudo $RPM_BUILD_ROOT%{_bindir}/sudoedit
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/sudoedit.8
echo '.so sudo.8' > $RPM_BUILD_ROOT%{_mandir}/man8/sudoedit.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README TROUBLESHOOTING sample.sudoers
%attr(440,root,root) %verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/sudoers
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/sudo
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/sudo-i
%attr(4755,root,root) %{_bindir}/sudo
%attr(4755,root,root) %{_bindir}/sudoedit
%attr(755,root,root) %{_sbindir}/visudo
%{?with_selinux:%attr(755,root,root) %{_libdir}/sesh}
%attr(755,root,root) %{_libdir}/sudo_noexec.so
%{_mandir}/man5/sudoers.5*
%{_mandir}/man5/sudoers.ldap.5*
%{_mandir}/man8/sudo.8*
%{_mandir}/man8/sudoedit.8*
%{_mandir}/man8/visudo.8*
%attr(600,root,root) %ghost /var/log/sudo
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/sudo
%attr(700,root,root) %dir /var/run/sudo
