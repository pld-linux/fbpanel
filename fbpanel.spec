Summary:	Lightweight and NETWM compliant desktop panel
Summary(pl):	Lekki i zgodny z NETWM panel
Name:		fbpanel
Version:	4.3
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/fbpanel/%{name}-%{version}.tgz
# Source0-md5:	2d2f3713cf3c17b71997064f39d4c888
Source1:	%{name}.menu.readme
Patch0:		%{name}-build_fixes.patch
Patch1:		%{name}-file_watcher.patch
Patch2:		%{name}-client_list.patch
URL:		http://fbpanel.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	gtk+2 >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fbpanel is a lightweight, NETWM compliant desktop panel.

%description -l pl
fbpanel to lekki i zgodny ze specyfikacj± NETWM panel.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i -e 's|/lib/fbpanel|/%{_lib}/fbpanel|' plugin.c

%build
# no auto* tools here
./configure \
	--prefix=%{_prefix}

%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	DATADIR="%{_datadir}" \
	LIBDIR="%{_libdir}"

install %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README fbpanel.menu.readme
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/fbpanel
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/plugins
%{_datadir}/%{name}
%{_mandir}/man1/fbpanel*
