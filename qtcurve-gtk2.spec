%define libname %{_lib}%{name}

Name:		qtcurve-gtk2
Summary:	QtCurve Theme for GTK
Version:	1.8.16
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2
URL:		https://www.kde-look.org/content/show.php?content=40492
Source0:	http://craigd.wikispaces.com/file/view/QtCurve-Gtk2-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	cmake
Requires:	%{libname} = %{EVRD}

%description
QtCurve theme for GTK2.

%package -n %{libname}
Summary:	libraries for %{name}
Group:		System/Libraries
Provides:	lib%{name} = %{EVRD}

%description -n %{libname}
Libraries for %{name}.

%prep
%setup -q -n QtCurve-Gtk2-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%doc AUTHORS ChangeLog README TODO
%{_datadir}/themes/QtCurve

%files -n %{libname}
%{_libdir}/gtk-2.0/*/engines/libqtcurve.so
