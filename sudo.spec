#
%bcond_without  selinux   # do not compile selinux support
#
Summary:	Allows command execution as root for specified users
Summary(es):	Permite que usuarios espec�ficos ejecuten comandos como se fueran el root
Summary(ja):	����桼���������դ�root���¤���Ĥ���
Summary(pl):	Umo�liwia wykonywaniew polece� jako root dla konkretnych u�ytkownik�w
Summary(pt_BR):	Permite que usu�rios espec�ficos executem comandos como se fossem o root
Summary(ru):	��������� ������������ ������������� ��������� ������� �� ����� root
Summary(uk):	������Ѥ �������� ������������ ���������� ������� צ� ���Φ root
Name:		sudo
Version:	1.6.7p5
Release:	6
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.courtesan.com/pub/sudo/%{name}-%{version}.tar.gz
# Source0-md5:	55d503e5c35bf1ea83d38244e0242aaf
Source1:	%{name}.pamd
Source2:	%{name}.logrotate
Patch0:		%{name}-selinux.patch
URL:		http://www.courtesan.com/sudo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pam-devel
%{?with_selinux:BuildRequires:	libselinux-devel}
Requires:	pam >= 0.77.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	cu-sudo

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
�Ȥϥ����ƥ�����Ԥ������ѤǤ���桼��(�ޤ��ϥ��롼��)����
���ơ������Ĥ�(�⤷��������)�Υ��ޥ�ɤ� root
�Ȥ��Ƽ¹ԤǤ���褦�����Υ��ޥ�
�ɤμ¹�����Υ���Ȥ�Ĥĵ��Ĥ�����ȤߤǤ���sudo
�ϥ��ޥ�ɰ��ñ�̤�ư��
���ޤ�����������֤������ǤϤ���ޤ��󡣰ʲ��ε�ǽ����¢���Ƥ��ޤ����ۥ���ñ��
�ǡ����Υ��ޥ�ɤ�¹Բ�ǽ�ʥ桼�������¤��뵡ǽ���ƥ��ޥ�ɤˤĤ��Ƥ�(ï����
�ˤ�¹Ԥ������κ��פ�Ĥ������)˭�٤ʥ��󥰵�ǽ��sudo
���ޥ�ɤΥ����ॢ��
�Ȼ��֤������ǽ��ʣ���Υޥ����Ʊ�������ե�����(sudoers)��ͭ���뵡ǽ����
����ޤ���

%description -l pl
Sudo (superuser do) umo�liwia wykonywanie konkretnych polece� jako
root dla wyspecyfikowanych u�ytkownik�w (rzeczywiste i efektywne
uid/gid podczas wykonywania tych program�w jest 0). To kto mo�e
wykonywa� konkretne polecenia i w jaki spos�b ma by� autoryzowany jest
opisane w pliku /etc/sudoers.

%description -l pt_BR
Sudo (superuser do) permite que o administrador do sistema d� a certos
usu�rios (ou grupos de usu�rios) a habilidade para rodar alguns (ou
todos) comandos como root, registrando todos os comandos e argumentos.
Sudo opera numa base por comando, n�o sendo um substituto para a
shell.

%description -l ru
Sudo (superuser do) ��������� ���������� �������������� �������������
������������ ������������� (��� �� �������) ����������� ���������
��������� (��� ���) ������� � ������� root, ��� ���� ������������ ���
������� � ���������. Sudo �������� � ���������� ���������, ��� ��
������ ��������� �������� (shell). ��������� �� ������������ sudo:
����������� ����, ����� ������� ������������ ����� ��������� �
����������� �� �����; ������ ���������������� ������ �������;
������������� �����, �� ���������� �������� sudo ������ ������;
������������� ������ ����������������� ����� (sudoers) �� ������
�������.

%description -l uk
Sudo (superuser do) ������Ѥ ���������� ��ͦΦ��������צ ������ ������
������������ (�� �� ������) �����צ��� ���������� ���˦ (�� �Ӧ)
������� � ������� root, ��� ����� ������������ �Ӧ ������� ��
���������. Sudo ������ � �������� ���������, �� �� ��ͦ�� �������ϧ
�������� (shell). ���˦ � ����������� sudo: ��������� ����, �˦
������� ���������� ���� ��������� � ��������Ԧ צ� �����; �����
�������������� ����ϧ �������; ������������ ���, �� �����ڦ ����� sudo
���'���� ������; ������������ ������ ���Ʀ����æ����� ����� (sudoers)
�� �������� �������.

%prep
%setup -q
%{?with_selinux:%patch0 -p1}

%build
cp /usr/share/automake/config.sub .
%configure \
	--with-timedir=/var/run/sudo \
	--with-C2 \
	--with-pam \
	--with-logging=both \
	--with-logfac=auth \
	--with-logpath=/var/log/sudo \
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
	--disable-saved-ids \
	NROFFPROG=nroff

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES HISTORY README TODO TROUBLESHOOTING sample.sudoers
%attr(0440,root,root) %verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/sudoers
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/sudo
%attr(4555,root,root) %{_bindir}/sudo
%attr(0555,root,root) %{_sbindir}/visudo
%{_mandir}/man*/*
%attr(0600,root,root) %ghost /var/log/sudo
%attr(0640,root,root) /etc/logrotate.d/*
%attr(0700,root,root) %dir /var/run/sudo
