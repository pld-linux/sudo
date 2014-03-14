# TODO: SSSD support?
#
# Conditional build:
%bcond_without	audit		# Linux audit support
%bcond_with	kerberos5	# enable Kerberos V support (conflicts with PAM)
%bcond_without	ldap		# disable LDAP support
%bcond_without	pam		# disable PAM support
%bcond_without	selinux		# build without SELinux support
%bcond_with	skey		# enable skey (onetime passwords) support (conflicts with PAM)
%bcond_without	tests		# do not perform "make check"

%if "%{pld_release}" == "ac"
%define		pam_ver	0.80.1
%else
%define		pam_ver	0.99.7.1
%endif

Summary:	Allows command execution as root for specified users
Summary(es.UTF-8):	Permite que usuarios específicos ejecuten comandos como se fueran el root
Summary(ja.UTF-8):	指定ユーザに制限付のroot権限を許可する
Summary(pl.UTF-8):	Umożliwia wykonywanie poleceń jako root dla konkretnych użytkowników
Summary(pt_BR.UTF-8):	Permite que usuários específicos executem comandos como se fossem o root
Summary(ru.UTF-8):	Позволяет определенным пользователям исполнять команды от имени root
Summary(uk.UTF-8):	Дозволяє вказаним користувачам виконувати команди від імені root
Name:		sudo
Version:	1.8.10p1
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.sudo.ws/pub/sudo/%{name}-%{version}.tar.gz
# Source0-md5:	1d9c2bc5aaf02608343d17b9a666e8e1
Source1:	%{name}.pamd
Source2:	%{name}-i.pamd
Source3:	%{name}.logrotate
Source4:	%{name}.tmpfiles
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-env.patch
Patch2:		config.patch
URL:		http://www.sudo.ws/sudo/
%{?with_audit:BuildRequires:	audit-libs-devel}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
%{?with_kerberos5:BuildRequires:	heimdal-devel}
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool >= 2:2.2.6b
%{?with_ldap:BuildRequires:	openldap-devel >= 2.3.0}
%{?with_pam:BuildRequires:	pam-devel}
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.595
%{?with_skey:BuildRequires:	skey-devel >= 2.2-11}
BuildRequires:	zlib-devel
Requires:	pam >= %{pam_ver}
Obsoletes:	cu-sudo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		schemadir	/usr/share/openldap/schema

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

%package devel
Summary:	Header file for sudo plugins development
Summary(pl.UTF-8):	Plik nagłówkowy do tworzenia wtyczek dla sudo
Group:		Development/Libraries

%description devel
Header file for sudo plugins development.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia wtyczek dla sudo.

%package -n openldap-schema-sudo
Summary:	Sudo LDAP schema
Summary(pl.UTF-8):	Schemat bazy sudo dla LDAP
Group:		Networking/Daemons
Requires(post,postun):	sed >= 4.0
Requires:	openldap-servers
Requires:	sed >= 4.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n openldap-schema-sudo
This package contains sudo.schema for openldap.

%description -n openldap-schema-sudo -l pl.UTF-8
Ten pakiet zawiera sudo.schema dla pakietu openldap.

%prep
%setup -q
# only local macros
mv aclocal.m4 acinclude.m4
# do not load libtool macros from acinclude
cp -p acinclude.m4 acinclude.m4.orig
%{__sed} -i -e '/Pull in libtool macros/,$d' acinclude.m4

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__mv} install-sh install-custom-sh
%{__libtoolize}
%{__mv} install-custom-sh install-sh
cp -f /usr/share/automake/config.sub .
%{__aclocal} -I m4
%{__autoconf}
%configure \
	NROFFPROG=nroff \
	--enable-zlib=system \
	--with-env-editor \
	--with-ignore-dot \
	--with-incpath=/usr/include/security \
	%{?with_kerberos5:--with-kerb5} \
	%{?with_ldap:--with-ldap} \
	%{?with_audit:--with-linux-audit} \
	--with-logfac=auth \
	--with-logging=both \
	--with-loglen=320 \
	--with-logpath=/var/log/sudo \
	--with-long-otp-prompt \
	--with-pam \
	--with-pam-login \
	--with-passprompt="[sudo] password for %%p: " \
	--with-secure-path="/bin:/sbin:/usr/bin:/usr/sbin" \
	%{?with_selinux:--with-selinux} \
	%{?with_skey:--with-skey}

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/{sudoers.d,pam.d,logrotate.d},/usr/lib/tmpfiles.d,/var/log/sudo-io,%{_mandir}/man8}

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	install_uid=$(id -u) \
	install_gid=$(id -g) \
	sudoers_uid=$(id -u) \
	sudoers_gid=$(id -g) \
	shlib_mode="0755"

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/sudo
cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/sudo-i
cp -p %{SOURCE3} $RPM_BUILD_ROOT/etc/logrotate.d/sudo
cp -p %{SOURCE4} $RPM_BUILD_ROOT/usr/lib/tmpfiles.d/%{name}.conf

touch $RPM_BUILD_ROOT/var/log/sudo

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%if %{with ldap}
install -d $RPM_BUILD_ROOT%{schemadir}
cp -p doc/schema.OpenLDAP $RPM_BUILD_ROOT%{schemadir}/sudo.schema
%endif

# sudo,sudoers domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post -n openldap-schema-sudo
%openldap_schema_register %{schemadir}/sudo.schema -d core
%service -q ldap restart
%banner -o -e openldap-schema-sudo <<'EOF'
NOTE:
In order for sudoRole LDAP queries to be efficient, the server must index
the attribute 'sudoUser', e.g.

    # Indices to maintain
    index   sudoUser    eq
EOF

%postun -n openldap-schema-sudo
if [ "$1" = "0" ]; then
	%openldap_schema_unregister %{schemadir}/sudo.schema
	%service -q ldap restart
fi

%triggerpostun -- %{name} < 1:1.7.8p2-5
mv -f /var/run/sudo/* /var/db/sudo 2>/dev/null
rmdir /var/run/sudo 2>/dev/null || :

%triggerpostun -- %{name} < 1:1.8.7-2
# add include statement to sudoers
if ! grep -q '#includedir %{_sysconfdir}/sudoers.d' /etc/sudoers; then
	echo 'Adding includedir %{_sysconfdir}/sudoers.d to /etc/sudoers'
	cat <<-EOF >> /etc/sudoers
		## Read drop-in files from %{_sysconfdir}/sudoers.d
		## (the '#' here does not indicate a comment)
		#includedir %{_sysconfdir}/sudoers.d
	EOF
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README doc/{CONTRIBUTORS,HISTORY,LICENSE,TROUBLESHOOTING,UPGRADE,sample.*}
%{?with_ldap:%doc README.LDAP plugins/sudoers/sudoers2ldif}
%attr(550,root,root) %dir %{_sysconfdir}/sudoers.d
%attr(440,root,root) %verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/sudoers
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/sudo
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/sudo-i
%attr(4755,root,root) %{_bindir}/sudo
%attr(4755,root,root) %{_bindir}/sudoedit
%attr(755,root,root) %{_bindir}/sudoreplay
%attr(755,root,root) %{_sbindir}/visudo
%dir %{_libdir}/sudo
%{?with_selinux:%attr(755,root,root) %{_libdir}/sudo/sesh}
%attr(755,root,root) %{_libdir}/sudo/group_file.so
%attr(755,root,root) %{_libdir}/sudo/sudo_noexec.so
%attr(755,root,root) %{_libdir}/sudo/sudoers.so
%attr(755,root,root) %{_libdir}/sudo/system_group.so
%{_mandir}/man5/sudoers.5*
%{_mandir}/man5/sudo.conf.5*
%{?with_ldap:%{_mandir}/man5/sudoers.ldap.5*}
%{_mandir}/man8/sudo.8*
%{_mandir}/man8/sudo_plugin.8*
%{_mandir}/man8/sudoedit.8*
%{_mandir}/man8/sudoreplay.8*
%{_mandir}/man8/visudo.8*
/usr/lib/tmpfiles.d/%{name}.conf
%attr(600,root,root) %ghost /var/log/sudo
%attr(700,root,root) /var/log/sudo-io
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/sudo
%attr(700,root,root) %dir /var/db/sudo

%files devel
%defattr(644,root,root,755)
%{_includedir}/sudo_plugin.h

%if %{with ldap}
%files -n openldap-schema-sudo
%defattr(644,root,root,755)
%{schemadir}/sudo.schema
%endif
