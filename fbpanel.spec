Summary:	Lightweight and NETWM compliant desktop panel
Summary(pl.UTF-8):	Lekki i zgodny z NETWM panel
Name:		fbpanel
Version:	6.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/project/fbpanel/fbpanel/%{version}/%{name}-%{version}.tbz2
# Source0-md5:	80ca0c64195b30587cfcb8c2cd9887a0
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

%description -l pl.UTF-8
fbpanel to lekki i zgodny ze specyfikacją NETWM panel.

%prep
%setup -q
# %patch0 -p1
# %patch1 -p1
# %patch2 -p1

# sed -i -e 's|/lib/fbpanel|/%{_lib}/fbpanel|' plugin.c

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
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_datadir}/%{name}
