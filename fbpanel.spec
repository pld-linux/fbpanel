Summary:	Lightweight and NETWM compliant desktop panel
Summary(pl):	Lekki i zgodny z NETWM panel
Name:		fbpanel
Version:	3.17
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/fbpanel/%{name}-%{version}.tgz
# Source0-md5:	7d8de58756e9d7797fc959d44dcd8260
Source1:	%{name}.menu.readme
Patch0:		%{name}-build_fixes.patch
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

install %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS README fbpanel.menu.readme
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/fbpanel*
