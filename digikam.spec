%define major      1
%define libname    %mklibname digikam %major
%define libnamedev %mklibname digikam -d
%define oldlibnamedev %mklibname digikam %major -d

Name: digikam
Version: 1.4.0
Release: %mkrel 4
License: GPLv2+
Url: http://www.digikam.org
Group: Graphics
Source0: %{name}-%{version}.tar.bz2
Summary: A KDE photo management utility
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: kdegraphics4-devel
BuildRequires: kdeedu4-devel
BuildRequires: sqlite3-devel
BuildRequires: libjasper-devel
BuildRequires: libgphoto-devel
BuildRequires: libtiff-devel
BuildRequires: lcms-devel
BuildRequires: lensfun-devel
BuildRequires: liblqr-devel >= 0.4.0
BuildRequires: doxygen
BuildRequires: mysql-core
BuildRequires: mysql-common
Requires:      mysql-core
Requires:      mysql-common
Requires:      kdebase4-runtime
Requires:      qt4-database-plugin-sqlite
Requires:      kipi-plugins
Requires:      marble-common
Patch1:         digikam-1.4.0-canon-use-lenstype-tag.patch

%description
DigiKam is an advanced digital photo management application for KDE.
Photos can be collected into albums which can be sorted chronologically,
by directory layout or by custom collections.
DigiKam also provides tagging functionality. Images can be tagged despite of
their position and digiKam provides fast and intuitive ways to browse them.
User comments and customized meta-information added to images, are stored
into a database and retrieved to make them available into the user interface.
As soon as the camera is plugged in digikam allows you to preview, download,
upload and delete images.
Digikam also includes tools like Image Editor, to modify photos using plugins
such as red eye correction or Gamma correction, exif management,...
Light Table to make artistic photos and an external image editor such
as Showfoto.
Digikam also uses KIPI plugins (KDE Image Plugin Interface) to increase
its functionalities.


%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/digikam
%_kde_bindir/digitaglinktree
%_kde_bindir/cleanup_digikamdb
%_kde_libdir/kde4/libexec/digikamdatabaseserver
%_kde_libdir/kde4/*.so
%_kde_libdir/kde4/plugins/marble/ExternalDraw.so
%_kde_appsdir/digikam
%_kde_datadir/kde4/services/*
%_kde_datadir/kde4/servicetypes/digikamimageplugin.desktop
%_kde_mandir/*
%_kde_datadir/applications/kde4/digikam.desktop
%_kde_appsdir/solid/actions/digikam-opencamera.desktop
%_kde_iconsdir/hicolor/*/apps/digikam.*

#---------------------------------------------

%package -n     showfoto
Summary:        A KDE photo management utility
Group:          Graphics
Requires:       marble-common
Conflicts:      %name < 0.10.0-5

%description -n showfoto
A KDE photo management utility

%files -n showfoto
%defattr(-,root,root)
%_kde_bindir/showfoto
%_kde_datadir/applications/kde4/showfoto.desktop
%_kde_appsdir/showfoto
%_kde_iconsdir/hicolor/*/apps/showfoto.*

#---------------------------------------------

%define libdigikamdatabase %mklibname digikamdatabase 1

%package -n %libdigikamdatabase
Summary: KDE 4 library
Group: System/Libraries

%description -n %libdigikamdatabase
Librairie File needed by %name

%files -n %libdigikamdatabase
%defattr(-,root,root)
%_kde_libdir/libdigikamdatabase.so.*

#---------------------------------------------

%define libdigikamcore %mklibname digikamcore 1

%package -n %libdigikamcore
Summary: KDE 4 library
Group: System/Libraries
Obsoletes: %{_lib}digikam1 < 0.10.0-1.beta6.3

%description -n %libdigikamcore
Librairie File needed by %name

%files -n %libdigikamcore
%defattr(-,root,root)
%_kde_libdir/libdigikamcore.so.*

#---------------------------------------------

%package        -n     %{libnamedev}
Summary:        Static libraries and headers for %{name}
Group:          Development/C
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{oldlibnamedev} <  0.10.0-0.753592.2
Requires:       %libdigikamcore = %version-%release
Requires:       %libdigikamdatabase = %version-%release

%description  -n     %{libnamedev}
%{libnamedev} contains the libraries and header files needed to
develop programs which make use of %{name}.
The library documentation is available on header files.

%files -n     %{libnamedev}
%defattr(0644, root, root, 0755)
%dir %_kde_includedir/digikam
%_kde_includedir/digikam/*.h
%_kde_includedir/digikam_export.h
%_kde_libdir/libdigikamcore.so
%_kde_libdir/libdigikamdatabase.so

#------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .canonlenstype

%build
%cmake_kde4 
%make

%install
rm -rf %buildroot
%{makeinstall_std} -C build

%find_lang %{name}

%clean
rm -rf %buildroot
