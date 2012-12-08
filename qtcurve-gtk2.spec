%define libname %{_lib}%{name}

Name:		qtcurve-gtk2
Summary:	QtCurve Theme for GTK
Version:	1.8.15
Release:	2
Group:		Graphical desktop/GNOME
License:	GPLv2
URL:		http://www.kde-look.org/content/show.php?content=40492
Source0:	http://craigd.wikispaces.com/file/view/QtCurve-Gtk2-%{version}.tar.bz2
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	cmake
Requires:	%{libname} = %{version}-%{release}

%description
QtCurve theme for GTK2.

%package -n %{libname}
Summary:	libraries for %{name}
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

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


%changelog
* Tue May 08 2012 Andrey Bondrov <abondrov@mandriva.org> 1.8.15-1mdv2012.0
+ Revision: 797534
- New version 1.8.15

* Mon Apr 11 2011 Funda Wang <fwang@mandriva.org> 1.8.8-1
+ Revision: 652658
- update to new version 1.8.8

* Wed Mar 09 2011 Funda Wang <fwang@mandriva.org> 1.8.6-1
+ Revision: 643083
- update to new version 1.8.6

* Mon Feb 14 2011 Funda Wang <fwang@mandriva.org> 1.8.5-1
+ Revision: 637822
- New version 1.8.5

* Tue Dec 14 2010 Funda Wang <fwang@mandriva.org> 1.8.1-1mdv2011.0
+ Revision: 621741
- update to new version 1.8.1

* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 1.7.2-1mdv2011.0
+ Revision: 599605
- new version 1.7.2

* Sat Oct 02 2010 Funda Wang <fwang@mandriva.org> 1.6.3-1mdv2011.0
+ Revision: 582415
- update to new version 1.6.3

* Tue Jul 20 2010 Funda Wang <fwang@mandriva.org> 1.5.2-1mdv2011.0
+ Revision: 555649
- update to new version 1.5.2

* Fri Apr 16 2010 Frederik Himpe <fhimpe@mandriva.org> 1.3.0-1mdv2010.1
+ Revision: 535578
- update to new version 1.3.0

* Sat Apr 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 533538
- new upstream release 1.2.0
- clean spec

* Sun Feb 28 2010 Frederik Himpe <fhimpe@mandriva.org> 1.1.1-1mdv2010.1
+ Revision: 512678
- update to new version 1.1.1

* Thu Feb 11 2010 Funda Wang <fwang@mandriva.org> 1.0.2-1mdv2010.1
+ Revision: 504366
- New version 1.0.2

* Tue Jan 19 2010 Frederik Himpe <fhimpe@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 493841
- Update to new version 1.0.1
- Rediff underlink patch

* Sun Nov 15 2009 Frederik Himpe <fhimpe@mandriva.org> 0.69.2-2mdv2010.1
+ Revision: 466306
- Move so file to separate lib package, so that 64 bit and 32 bit GTK+
  engines can be installed together

* Tue Oct 20 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.69.2-1mdv2010.0
+ Revision: 458427
- Update to latest release to fix the arrow not displaying, bug #54560

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - update to new version 0.69.1 (fix bug #54640)

* Thu Sep 10 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.68.0-1mdv2010.0
+ Revision: 436906
- Update to new version 0.68

* Thu Aug 13 2009 Frederik Himpe <fhimpe@mandriva.org> 0.67.4-1mdv2010.0
+ Revision: 416099
- update to new version 0.67.4

* Sat Aug 08 2009 Frederik Himpe <fhimpe@mandriva.org> 0.67.3-1mdv2010.0
+ Revision: 411529
- update to new version 0.67.3

* Fri Jul 24 2009 Frederik Himpe <fhimpe@mandriva.org> 0.67.0-1mdv2010.0
+ Revision: 399419
- update to new version 0.67.0

* Tue Jun 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.65.1-1mdv2010.0
+ Revision: 391121
- update to new version 0.65.1

* Thu Jun 25 2009 Frederik Himpe <fhimpe@mandriva.org> 0.65.0-1mdv2010.0
+ Revision: 389182
- update to new version 0.65.0

* Sat May 16 2009 Jérôme Brenier <incubusss@mandriva.org> 0.62.8-1mdv2010.0
+ Revision: 376329
- update to new version 0.62.8

* Wed Mar 18 2009 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.62.4-1mdv2009.1
+ Revision: 357314
- Update to new version 0.62

* Sun Jan 11 2009 Frederik Himpe <fhimpe@mandriva.org> 0.60.0-1mdv2009.1
+ Revision: 328328
- Update to new version 0.60

* Fri Aug 01 2008 Funda Wang <fwang@mandriva.org> 0.59.7-1mdv2009.0
+ Revision: 259128
- New version 0.59.7

* Sat Jul 26 2008 Funda Wang <fwang@mandriva.org> 0.59.6-1mdv2009.0
+ Revision: 250052
- update to new version 0.59.6

* Mon Jul 14 2008 Funda Wang <fwang@mandriva.org> 0.59.5-1mdv2009.0
+ Revision: 234829
- import qtcurve-gtk2


