Summary:	Lightweight and NETWM compliant desktop panel
Summary(pl):	Lekki i zgodny z NETWM panel
Name:		fbpanel
Version:	3.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/fbpanel/%{name}-%{version}.tgz
# Source0-md5:	f82a5b2ee50ee2a8cc19ddda1aa7009c
Patch0:		%{name}-build_fixes.patch
Patch1:		%{name}-include_menu.patch
Patch2:		%{name}-post_3.9_fixes.patch
URL:		http://fbpanel.sourceforge.net/
BuildRequires:	gtk+2-devel >= 1:2.4.0
BuildRequires:	pkgconfig
Requires:	gtk+2 >= 1:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fbpanel is a lightweight, NETWM compliant desktop panel.

%description -l pl
fbpanel to lekki i zgodny ze specyfikacj± NETWM panel.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2	-p1

%build
# no auto* tools here
./configure \
	--prefix=%{_prefix}

%{__make} \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/fbpanel*
