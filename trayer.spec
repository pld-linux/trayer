Summary:	A lightweight GTK2-based systray for UNIX desktop
Summary(pl):	Lekki, bazuj±cy na GTK2 dok systemowy (systray)
Name:		trayer
Version:	1.0
Release:	1
License:	BSD
Group:		X11/Window Managers
Source0:	http://fvwm-crystal.berlios.de/files/files/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9acac948017bf1b5fc50bc1117c9b098
BuildRequires:	freetype-devel
BuildRequires:	atk-devel
BuildRequires:	pango-devel
URL:		http://fvwm-crystal.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trayer is small program designed to provide system tray similar to
these in GNOME/KDE desktop environments for window managers which
does not support that function.

%description -l pl
Trayer jest ma³ym programem zaprojektowanym by dostarczaæ funkcje 
doku systemowego znanego z GNOME/KDE dla ¶rodowisk okienkowych nie 
posiadaj±cych tej funkcjonalno¶ci. 

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        PREFIX=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install trayer $RPM_BUILD_ROOT%{_bindir}
install trayer.1.gz $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYING CREDITS README
%attr(755,root,root) %{_bindir}/trayer
%{_mandir}/man1/trayer.1.gz
