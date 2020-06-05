%define beta beta3

# Workaround for
# Cannot handle 8-byte build ID
%define debug_package %{nil}

Summary:	A KDE photo management utility
Name:		digikam
Version:	7.0.0
License:	GPLv2+
Group:		Graphics
Url:		http://www.digikam.org
%if "%{beta}" != ""
Source0:	http://download.kde.org/unstable/digikam/%{name}-%{version}-%{beta}.tar.xz
# Generated by tarring up po/ after running
# cmake -DDIGIKAMSC_CHECKOUT_PO:BOOL=ON
Source1:	digikam-7.0-l10n.tar.xz
Release:	0.%{beta}.1
%else
Source0:	http://download.kde.org/stable/digikam/%{version}/%{name}-%{version}.tar.xz
Release:	1
%endif
Source100:	%{name}.rpmlintrc
## upstreamable patches
Patch0:		digikam-7.0.0-qt-5.15.patch
BuildRequires:	doxygen
BuildRequires:	eigen3
BuildRequires:	flex
BuildRequires:	lld
BuildRequires:	bison
BuildRequires:	imagemagick
BuildRequires:	mariadb-server
BuildRequires:	mariadb-devel
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libpgf)
BuildRequires:  pkgconfig(libpng)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(lqr-1) >= 0.4.0
BuildRequires:	pkgconfig(opencv4) >= 4.3.0
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(expat)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(QtAV)
BuildRequires:	cmake(QtAVWidgets)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5MultimediaWidgets)
BuildRequires:	cmake(Qt5XmlPatterns)
BuildRequires:	cmake(Qt5X11Extras)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5WebView)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5AkonadiContact)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	cmake(KF5Kipi)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5Sane)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(Marble)

Requires:	mariadb-common
Requires:	libgphoto-common
Requires:	libkdcraw-common

# FIXME why doesn't the dependency generator see this?
# https://issues.openmandriva.org/show_bug.cgi?id=2391
Requires:	%mklibname sane 1

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

%files -f %{name}.lang
%{_kde5_bindir}/digikam
%{_kde5_bindir}/digitaglinktree
%{_kde5_bindir}/cleanup_digikamdb
%{_kde5_datadir}/digikam
%{_kde5_datadir}/solid/actions/digikam*.desktop
%{_kde5_datadir}/kxmlgui5/digikam
%{_kde5_applicationsdir}/org.kde.digikam.desktop
%{_kde5_datadir}/metainfo/org.kde.digikam.appdata.xml
%{_kde5_mandir}/man1/digitaglinktree.1*
%{_kde5_mandir}/man1/cleanup_digikamdb.1*
%{_kde5_iconsdir}/*/*/apps/digikam.*
%{_iconsdir}/hicolor/*/*/dk-*.*
%{_iconsdir}/hicolor/*/apps/expoblending.png
%{_iconsdir}/hicolor/*/*/panorama.*
%{_iconsdir}/*/*/*/albumfolder*.*
%{_iconsdir}/*/*/*/overexposure.*
%{_iconsdir}/*/*/*/tag*.*
%{_iconsdir}/*/*/*/underexposure.*
%{_kde5_datadir}/knotifications5/digikam.notifyrc
%{_libdir}/qt5/plugins/digikam

#-----------------------------------------------------------------------

%package -n showfoto
Summary:	Fast Image Editor
Group:		Graphics
Requires:	libkdcraw
# Otherwise it doesn't work properly
Requires:	%{name} = %{EVRD}

%description -n showfoto
Showfoto is a fast Image Editor with powerful image editing tools.
You can use it to view your photographs and improve them.

%files -n showfoto -f showfoto.lang
%{_kde5_bindir}/showfoto
%{_kde5_datadir}/applications/org.kde.showfoto.desktop
%{_kde5_datadir}/kxmlgui5/showfoto
%{_kde5_datadir}/showfoto
%{_kde5_datadir}/metainfo/org.kde.showfoto.appdata.xml
%{_kde5_iconsdir}/*/*/apps/showfoto.*

#-----------------------------------------------------------------------

%define libdigikamdatabase_major %{version}
%define libdigikamdatabase %mklibname digikamdatabase %{libdigikamdatabase_major}

%package -n %{libdigikamdatabase}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}digikamdatabase2 < 3.0.0
Obsoletes:	%{_lib}digikamdatabase3 < 4.0.0
Obsoletes:	%{_lib}digikamdatabase5.9.0 < 6.0.0
Obsoletes:	%{_lib}digikamdatabase6.0.0 < 6.1.0
Obsoletes:	%{_lib}digikamdatabase6.1.0 < 6.2.0
Obsoletes:	%{_lib}digikamdatabase6.2.0 < 6.3.0
Obsoletes:	%{_lib}digikamdatabase6.3.0 < 6.4.0
Obsoletes:	%{_lib}digikamdatabase6.4.0 < 6.5.0

%description -n %{libdigikamdatabase}
Librairie File needed by %{name}

%files -n %{libdigikamdatabase}
%{_kde5_libdir}/libdigikamdatabase.so.%{libdigikamdatabase_major}*

#-----------------------------------------------------------------------

%define libdigikamcore_major %{version}
%define libdigikamcore %mklibname digikamcore %{libdigikamcore_major}

%package -n %{libdigikamcore}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}digikamcore2 < 3.0.0
Obsoletes:	%{_lib}digikamcore3 < 4.0.0
Obsoletes:	%{_lib}digikamcore5.9.0 < 6.0.0
Obsoletes:	%{_lib}digikamcore6.0.0 < 6.1.0
Obsoletes:	%{_lib}digikamcore6.1.0 < 6.2.0
Obsoletes:	%{_lib}digikamcore6.2.0 < 6.3.0
Obsoletes:	%{_lib}digikamcore6.3.0 < 6.4.0
Obsoletes:	%{_lib}digikamcore6.4.0 < 6.5.0

%description -n %{libdigikamcore}
Librairie File needed by %{name}

%files -n %{libdigikamcore}
%{_kde5_libdir}/libdigikamcore.so.%{libdigikamcore_major}*

#-----------------------------------------------------------------------

%define libdigikamgui_major %{version}
%define libdigikamgui %mklibname digikamgui %libdigikamgui_major

%package -n %{libdigikamgui}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}digikamgui5.9.0 < 6.0.0
Obsoletes:	%{_lib}digikamgui6.0.0 < 6.1.0
Obsoletes:	%{_lib}digikamgui6.1.0 < 6.2.0
Obsoletes:	%{_lib}digikamgui6.2.0 < 6.3.0
Obsoletes:	%{_lib}digikamgui6.3.0 < 6.4.0
Obsoletes:	%{_lib}digikamgui6.4.0 < 6.5.0

%description -n %{libdigikamgui}
Librairie File needed by %name.

%files -n %{libdigikamgui}
%{_kde5_libdir}/libdigikamgui.so.%{libdigikamgui_major}*

#-----------------------------------------------------------------------

%define libnamedev %mklibname digikam -d

%package -n %{libnamedev}
Summary:	Static libraries and headers for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%libdigikamcore = %{EVRD}
Requires:	%libdigikamgui = %{EVRD}
Requires:	%libdigikamdatabase = %{EVRD}

%description -n %{libnamedev}
%libnamedev contains the libraries and header files needed to
develop programs which make use of %name.
The library documentation is available on header files.

%files -n %{libnamedev}
%{_includedir}/digikam
%{_kde5_libdir}/*.so
%{_libdir}/cmake/DigikamCore*
%{_libdir}/cmake/DigikamDatabase*
%{_libdir}/cmake/DigikamGui*

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}%{?beta:-%{beta}}
%if "%{beta}" != ""
tar xf %{S:1}
%endif

%build
# (tpg) upstream ships own libraw library instead of using system-wide libraw
# make[2]: Leaving directory '/builddir/build/BUILD/digikam-5.5.0/build'
# /usr/bin/ld: warning: ../libs/rawengine/libraw/liblibraw.a(demosaic_packs.cpp.o): multiple common of '.gomp_critical_user_.var'
# /usr/bin/ld: ../libs/rawengine/libraw/liblibraw.a(libraw_cxx.cpp.o): previous definition here
# /builddir/build/BUILD/digikam-5.5.0/core/libs/rawengine/libraw/src/libraw_xtrans_compressed.cpp:130: error: undefined reference to '__kmpc_global_thread_num'
# try to build with GCC because of above issue

%cmake_kde5 -G Ninja \
	-DENABLE_OPENCV3:BOOL=ON \
	-DENABLE_MYSQLSUPPORT:BOOL=ON \
	-DENABLE_INTERNALMYSQL:BOOL=OFF \
	-DENABLE_AKONADICONTACTSUPPORT:BOOL=ON \
	-DENABLE_APPSTYLES:BOOL=ON \
	-DENABLE_KFILEMETADATASUPPORT:BOOL=ON \
	-DENABLE_MEDIAPLAYER:BOOL=ON \
	-Wno-dev

%ninja_build

%install
%ninja_install -C build

%find_lang %{name} --with-html || echo '%%optional /not/yet/there' >%{name}.lang
%find_lang showfoto --with-html || echo '%%optional /not/yet/there' >showfoto.lang
