#
# Conditional build:
%bcond_without	selinux		# build without SELinux support
#
Summary:	Allows command execution as root for specified users
Summary(es):	Permite que usuarios especМficos ejecuten comandos como se fueran el root
Summary(ja):	╩ьдЙ╔Ф║╪╔╤╓кю╘╦биу╓нroot╦╒╦б╓Р╣Ж╡д╓╧╓К
Summary(pl):	Umo©liwia wykonywanie poleceЯ jako root dla konkretnych u©ytkownikСw
Summary(pt_BR):	Permite que usuАrios especМficos executem comandos como se fossem o root
Summary(ru):	Позволяет определенным пользователям исполнять команды от имени root
Summary(uk):	Дозволя╓ вказаним користувачам виконувати команди в╕д ╕мен╕ root
Name:		sudo
Version:	1.6.8p7
Release:	1
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.courtesan.com/pub/sudo/%{name}-%{version}.tar.gz
# Source0-md5:	ad65d24f20c736597360d242515e412c
Source1:	%{name}.pamd
Source2:	%{name}.logrotate
Patch0:		%{name}-selinux.patch
Patch1:		%{name}-ac.patch
URL:		http://www.courtesan.com/sudo/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
%{?with_selinux:BuildRequires:	libselinux-devel}
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
╓х╓о╔╥╔╧╔ф╔Ю╢имЩ╪т╓╛║╒©╝мя╓г╓╜╓К╔Ф║╪╔╤(╓ч╓©╓о╔╟╔К║╪╔в)╓кбп
╓╥╓ф║╒╓╓╓╞╓д╓╚(╓Б╓╥╓╞╓оа╢╓ф)╓н╔Ё╔ч╔С╔и╓Р root
╓х╓╥╓ф╪б╧т╓г╓╜╓К╓Х╓╕║╒╓╫╓н╔Ё╔ч╔С
╔и╓н╪б╧тмЗнР╓н╔М╔╟╓Р╓х╓Й╓д╓д╣Ж╡д╓╧╓К╩еах╓ъ╓г╓╧║ёsudo
╓о╔Ё╔ч╔С╔и╟Л╧тц╠╟л╓гф╟╨Н
╓╥╓ч╓╧║ё╔╥╔╖╔К╓нцж╓╜╢╧╓╗╓г╓о╓╒╓Й╓ч╓╩╓С║ё╟й╡╪╓н╣║г╫╓РфБб╒╓╥╓ф╓╓╓ч╓╧║ё╔ш╔╧╔хц╠╟л
╓г║╒╓╫╓н╔Ё╔ч╔С╔и╓Р╪б╧т╡дг╫╓й╔Ф║╪╔╤╓Рю╘╦б╓╧╓К╣║г╫║╒Ёф╔Ё╔ч╔С╔и╓к╓д╓╓╓ф╓н(ц╞╓╛╓й
╓к╓Р╪б╧т╓╥╓©╓╚╓н╨╞юв╓Р╩д╓╧╓©╓А╓н)к╜иы╓й╔М╔╝╔С╔╟╣║г╫║╒sudo
╔Ё╔ч╔С╔и╓н╔©╔╓╔Ю╔╒╔╕
╔х╩Ч╢ж╓РюъдЙ╡дг╫║╒йё©Т╓н╔ч╔╥╔С╓гф╠╟Л╓нюъдЙ╔у╔║╔╓╔К(sudoers)╓Р╤╕м╜╓╧╓К╣║г╫║╒╓╛
╓╒╓Й╓ч╓╧║ё

%description -l pl
Sudo (superuser do) umo©liwia wykonywanie konkretnych poleceЯ jako
root dla wyspecyfikowanych u©ytkownikСw (rzeczywiste i efektywne
uid/gid podczas wykonywania tych programСw jest 0). To kto mo©e
wykonywaФ konkretne polecenia i w jaki sposСb ma byФ autoryzowany jest
opisane w pliku /etc/sudoers.

%description -l pt_BR
Sudo (superuser do) permite que o administrador do sistema dЙ a certos
usuАrios (ou grupos de usuАrios) a habilidade para rodar alguns (ou
todos) comandos como root, registrando todos os comandos e argumentos.
Sudo opera numa base por comando, nЦo sendo um substituto para a
shell.

%description -l ru
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

%description -l uk
Sudo (superuser do) дозволя╓ системному адм╕н╕страторов╕ надати певним
користувачам (чи ╖х групам) можлив╕сть виконувати деяк╕ (чи вс╕)
команди з правами root, при цьому протоколюючи вс╕ команди та
аргументи. Sudo працю╓ з окремими командами, це не зам╕на командно╖
оболонки (shell). Деяк╕ з можливостей sudo: обмеження того, як╕
команди користувач може запускати в залежност╕ в╕д хоста; повне
протоколювання кожно╖ команди; настроюваний час, на протяз╕ якого sudo
пам'ята╓ пароль; використання одного конф╕гурац╕йного файлу (sudoers)
на багатьох машинах.

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
%configure \
	NROFFPROG=nroff \
	--with-timedir=/var/run/sudo \
	--with-pam \
	--with-logging=both \
	--with-logfac=auth \
	--with-logpath=/var/log/sudo \
	--with-ignore-dot \
	--with-env-editor \
	--with-insults \
	--with-all-insults \
	--with-classic-insults \
	--with-csops-insults \
	--with-hal-insults \
	--with-goons-insults \
	--with-secure-path="/bin:/sbin:/usr/bin:/usr/sbin" \
	--with-loglen=320 \
	--disable-saved-ids

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
