Summary:	Allows command execution as root for specified users
Summary(pl):	Umo¿liwia wykonywaniew poleceñ jako root dla konkretnych u¿ytkowników
Name:		sudo
Version:	1.6.3p4
Release:	1
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://ftp.courtesan.com/pub/sudo/%{name}-%{version}.tar.gz
Source1:	sudo.pamd
Patch0:		sudo-DESTDIR.patch
URL:		http://www.courtesan.com/sudo/
BuildRequires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	cu-sudo

%define		_sysconfdir	/etc

%description
Sudo (superuser do) allows a permitted user to execute a command as
the superuser (real and effective uid and gid are set to 0 and root's
group as set in the passwd file respectively).

Sudo determines who is an authorized user by consulting the file
/etc/sudoers. By giving sudo the -v flag a user can update the time
stamp without running a command. The password prompt itself will also
time out if the password is not entered with N minutes (again, this is
defined at installation time and defaults to 5 minutes).

%description -l pl
Sudo (superuser do) umo¿liwia wykonywanie konkretnych poleceñ jako
root dla wyspecyfikowanych u¿ytkowników (rzeczywiste i efektywne
uid/gid podczas wykonywania tych programów jest 0). To kto mo¿e
wykonywaæ konkretne polecenia i w jaki sposób ma byæ autoryzowany jest
opisane w pliku /etc/sudoers.

%prep
%setup -q
%patch -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-timedir=/var/run/sudo \
	--with-C2 \
	--with-pam \
	--with-logging=both \
	--with-logfac=auth \
	--with-logpath=/var/log/sudo.log \
	--with-message=full \
	--with-ignore-dot \
	--with-env-editor \
	--with-insults \
	--with-all-insults \
	--with-classic-insults \
	--with-csops-insults \
	--with-hal-insults \
	--with-goons-insults \
	--with-secure-path="/bin:/sbin:%{_bindir}:%{_sbindir}" \
	--with-loglen=320 \

%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/pam.d,/var/{log,run/sudo}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	install_uid=`id -u` \
	install_gid=`id -g` \
	sudoers_uid=`id -u` \
	sudoers_gid=`id -g`

install %{SOURCE1}  $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/sudo
touch $RPM_BUILD_ROOT/var/log/sudo.log

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{5,8}/* \
	BUGS CHANGES HISTORY README TODO TROUBLESHOOTING

chmod -R +r $RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz sample.sudoers
%attr(0400,root,root) %verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/sudoers
%attr(0600,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/pam.d/sudo
%attr(4555,root,root) %{_bindir}/sudo
%attr(0555,root,root) %{_sbindir}/visudo
%{_mandir}/man*/*
%attr(0600,root,root) %ghost /var/log/sudo.log
%attr(0700,root,root) %dir /var/run/sudo
