Summary:	Allows command execution as root for specified users
Summary(pl):	Umo¿liwia wykonywaniew poleceñ jako root dla konkretnych u¿ytkowników
Name:		sudo
Version:	1.5.9p2
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/Systemowe
Source:		ftp://ftp.cs.colorado.edu/pub/sudo/cu-sudo.v%{version}.tar.gz
URL:		http://www.courtesan.com/courtesan/products/sudo/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Sudo (superuser do) allows a permitted user to execute a command as the
superuser (real and effective uid and gid are set to 0 and root's group as
set in the passwd file respectively).
                                                                                                              
Sudo determines who is an authorized user by consulting the file
/etc/sudoers.  By giving sudo the -v flag a user can update the time stamp
without running a command.  The password prompt itself will also time out if
the password is not entered with N minutes (again, this is defined at
installation time and defaults to 5 minutes).

%description -l pl
Sudo (superuser do) umo¿liwia wykonywanie konkretnych poleceñ jako root dla
wyspecyfikowanych u¿ytkowników (rzeczywiste i efektywne uid/gid podczas
wykonywania tych programów jest 0).

To kto mo¿e wykonywaæ konkretne polecenia i w jaki sposób ma byæ
autoryzowany jest opisane w pliku /etc/sudoers.

%prep
%setup -q -n %{name}.v%{version}

%build
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=/usr \
	--sbindir=%{_sbindir} \
	--with-timedir=/var/run \
	--with-C2 \
	--with-pam \
	--with-logging=both \
	--with-logfac=LOG_AUTH \
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
	--with-secure-path="/bin:/sbin:/usr/bin:/usr/sbin" \
	--with-loglen=320 \

make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/pam.d,var/log}

make install \
	prefix=$RPM_BUILD_ROOT/usr \
	visudodir=$RPM_BUILD_ROOT%{_sbindir} \
	sysconfdir=$RPM_BUILD_ROOT/etc \
	install_uid=`id -u` \
	install_gid=`id -g` \
	sudoers_uid=`id -u` \
	sudoers_gid=`id -g`

install sample.pam $RPM_BUILD_ROOT/etc/pam.d/sudo
touch $RPM_BUILD_ROOT/var/log/sudo.log

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{5,8}/* \
	BUGS CHANGES HISTORY README TODO TROUBLESHOOTING

chmod -R +r $RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz sample.sudoers
%attr(0400,root,root) %verify(not md5 size mtime) %config(noreplace) /etc/sudoers
%attr(0600,root,root) %config /etc/pam.d/sudo
%attr(4555,root,root) %{_bindir}/sudo
%attr(0555,root,root) %{_sbindir}/visudo
%{_mandir}/man*/*
%attr(0600,root,root) %ghost /var/log/sudo.log

%changelog
* Sun May 30 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.9p2-1]
- added more rpm macros.

* Wed Apr  7 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.9p1-1]
- added gzipping %doc
- removed man group from man pages.

* Sun Nov 29 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.7p2-1]
- added gzipping man pages,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added "not size mtime" to %verify rule for /etc/sudoers,
- changed way passing $RPM_OPT_FLAGS,
- rewrited %description,
- rewrited %build and %install using new autoconf sheme,
- added pl translation.

* Tue Sep 21 1998 Ian Macdonald <ianmacd@xs4all.nl>
- upgraded to 1.5.6p2
- built with PAM support
- removed SUDO_LDFLAGS="-static" from make: would no longer build with it

* Wed May  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added using %%{name} macro in Buildroot.

* Mon Apr 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5.4-3]
- Buildroot changed to /tmp/sudo-%%{PACKAGE_VERSION}-root,
- added %%{PACKAGE_VERSION} to Source url and %setup macro,
- removed sudo-1.5.4-buildroot.patch and instead this added few parameters
  to "make install",
- SUDO_LDFLAGS="-static" and CFLAGS="$RPM_OPT_FLAGS" is passed as make 
  arguments,
- removed COPYING from %doc (Copyright statement is in Copyright field),
- removed from %doc *.pod and options.h and added sample.sudoers,
- added /var/log/sudo.log as %ghost file,
- added %verify(not md5) for /etc/sudoers (allow modify this file without
  display warning on verify with using rpm),
- added noreplace parameter for /etc/sudoers %config file,
- removed sudo.v1.5.4-glibc.diff because sudo compiles on glibc 2.0.7,
- added %defattr and %attr macros in %files (allows building package from
  non-root account); %defattr requires rpm >= 2.4.99.

* Fri Jan 23 1998 Ian Macdonald <ianmacd@xs4all.nl>
  [1.5.4-2]
- glibc build was broken; added patch to fix it

* Tue Nov 18 1997 Otto Hammersmith <otto@redhat.com>
- built for glibc, no problems

* Fri Apr 25 1997 Michael Fulbright <msf@redhat.com>
- Fixed for 4.2 PowerTools 
- Still need to be pamified
- Still need to move stmp file to /var/log

* Mon Feb 17 1997 Michael Fulbright <msf@redhat.com>
- First version for PowerCD.
