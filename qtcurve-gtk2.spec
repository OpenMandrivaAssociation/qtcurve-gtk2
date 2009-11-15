%define libname %{_lib}%{name}

Name: qtcurve-gtk2
Summary: QtCurve Theme for GTK
Version: 0.69.2
Release: %mkrel 2
Source0: http://home.freeuk.com/cpdrummond/QtCurve-Gtk2-%version.tar.bz2
Patch0: QtCurve-Gtk2-0.59.5-fix-underlink.patch
URL: http://www.kde-look.org/content/show.php?content=40492
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2
BuildRequires: gtk+2-devel
BuildRequires: cmake
Requires: %{libname} = %{version}

%description
QtCurve theme for GTK2.

%package -n %{libname}
Summary: libraries for %{name}
Group: System/Libraries 
Provides: lib%{name} = %{version}-%{release} 
Conflicts: %{name} < 0.69.2-2

%description -n %{libname}
Libraries for %{name}.

%prep 
%setup -q -n QtCurve-Gtk2-%{version}
%patch0 -p0

%build 
%cmake
%make

%install
rm -rf %{buildroot}
pushd build
%makeinstall_std
popd

%clean 
rm -rf %{buildroot}a

%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog README TODO
%{_datadir}/themes/QtCurve

%files -n %{libname}
%{_libdir}/gtk-2.0/*/engines/libqtcurve.so
