Name: qtcurve-gtk2
Summary: QtCurve Theme for GTK
Version: 0.68.0
Release: %mkrel 1
Source0: http://home.freeuk.com/cpdrummond/QtCurve-Gtk2-%version.tar.bz2
Patch0: QtCurve-Gtk2-0.59.5-fix-underlink.patch
URL: http://www.kde-look.org/content/show.php?content=40492
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2
BuildRequires: gtk+2-devel
BuildRequires: cmake

%description
QtCurve theme for GTK2.

%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog README TODO
%{_libdir}/gtk-2.0/*/engines/libqtcurve.so
%{_datadir}/themes/QtCurve

#--------------------------------------------------------------------
%prep 
%setup -q -n QtCurve-Gtk2-%version
%patch0 -p0

%build 
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
pushd build
%makeinstall_std
popd

%clean 
rm -rf $RPM_BUILD_ROOT
