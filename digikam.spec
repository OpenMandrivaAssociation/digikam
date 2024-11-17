#define beta %{nil}

Summary:	A KDE photo management utility
Name:		digikam
Version:	8.5.0
License:	GPLv2+
Group:		Graphics
Url:		https://www.digikam.org
Source0:	https://download.kde.org/%{?beta:un}stable/digikam/%{version}/digiKam-%{version}%{?beta:-%{beta}}.tar.xz
%if 0%{?beta:1}
# Generated by tarring up po/ after running
# cmake -DDIGIKAMSC_CHECKOUT_PO:BOOL=ON
Source1:	digikam-7.2-l10n.tar.xz
%endif
Release:	1
Source100:	%{name}.rpmlintrc

BuildRequires:	doxygen
BuildRequires:  gettext
BuildRequires:	graphviz
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
# FIXME - qtav is abandoned in upstream, and does not compile with ffmpeg6. Drop it for now, forever or fix it someday.
#BuildRequires:	cmake(QtAV)
#BuildRequires:	cmake(QtAVWidgets)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6NetworkAuth)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6MultimediaWidgets)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6StateMachine)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6SvgWidgets)
BuildRequires:	cmake(Qt6WebView)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Solid)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KPim6AkonadiContactCore)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KF6FileMetaData)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KF6ThreadWeaver)
BuildRequires:	cmake(KSaneCore6)
BuildRequires:	cmake(KSaneWidgets6)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	plasma6-marble-devel
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	git-core

Requires:	mariadb-common
Requires:	libgphoto-common
Requires:	libkdcraw-common

# For assembling panorama photos
Suggests:	hugin
# For displaying geolocation data on a map
Suggests:	marble

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
%{_bindir}/digikam
%{_bindir}/digitaglinktree
%{_bindir}/cleanup_digikamdb
%{_datadir}/digikam
%{_datadir}/solid/actions/digikam*.desktop
%{_datadir}/kxmlgui5/digikam
%{_datadir}/applications/org.kde.digikam.desktop
%{_datadir}/metainfo/org.kde.digikam.appdata.xml
%{_mandir}/man1/digitaglinktree.1*
%{_mandir}/man1/cleanup_digikamdb.1*
%{_iconsdir}/*/*/apps/digikam.*
%{_iconsdir}/hicolor/*/*/dk-*.*
%{_iconsdir}/hicolor/*/apps/expoblending.png
%{_iconsdir}/hicolor/*/*/panorama.*
%{_iconsdir}/*/*/*/albumfolder*.*
%{_iconsdir}/*/*/*/overexposure.*
%{_iconsdir}/*/*/*/tag*.*
%{_iconsdir}/*/*/*/underexposure.*
%{_datadir}/knotifications6/digikam.notifyrc
%{_qtdir}/plugins/digikam

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

%files -n showfoto
%{_bindir}/showfoto
%{_datadir}/applications/org.kde.showfoto.desktop
%{_datadir}/kxmlgui5/showfoto
%{_datadir}/showfoto
%{_datadir}/metainfo/org.kde.showfoto.appdata.xml
%{_iconsdir}/*/*/apps/showfoto.*

#-----------------------------------------------------------------------

%define libdigikamdatabase_major 8.4.0
%define libdigikamdatabase %mklibname digikamdatabase

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
Obsoletes:	%{_lib}digikamdatabase7.0.0 < 7.1.0
Obsoletes:	%{_lib}digikamdatabase7.1.0 < 7.2.0
Obsoletes:	%{_lib}digikamdatabase7.2.0 < 7.3.0
Obsoletes:	%{_lib}digikamdatabase7.3.0 < 7.4.0
Obsoletes:	%{_lib}digikamdatabase7.4.0 < 7.5.0
Obsoletes:	%{_lib}digikamdatabase7.5.0 < 7.6.0
Obsoletes:	%{_lib}digikamdatabase7.6.0 < 7.7.0
Obsoletes:	%{_lib}digikamdatabase7.7.0 < 7.8.0
Obsoletes:	%{_lib}digikamdatabase7.8.0 < 7.9.0
Obsoletes:	%{_lib}digikamdatabase7.9.0 < 7.10.0

%description -n %{libdigikamdatabase}
Librairie File needed by %{name}

%files -n %{libdigikamdatabase}
%{_libdir}/libdigikamdatabase.so.%{libdigikamdatabase_major}*

#-----------------------------------------------------------------------

%define libdigikamcore_major 8.4.0
%define libdigikamcore %mklibname digikamcore

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
Obsoletes:	%{_lib}digikamcore7.0.0 < 7.1.0
Obsoletes:	%{_lib}digikamcore7.1.0 < 7.2.0
Obsoletes:	%{_lib}digikamcore7.2.0 < 7.3.0
Obsoletes:	%{_lib}digikamcore7.3.0 < 7.4.0
Obsoletes:	%{_lib}digikamcore7.4.0 < 7.5.0
Obsoletes:	%{_lib}digikamcore7.5.0 < 7.6.0
Obsoletes:	%{_lib}digikamcore7.6.0 < 7.7.0
Obsoletes:	%{_lib}digikamcore7.7.0 < 7.8.0
Obsoletes:	%{_lib}digikamcore7.8.0 < 7.9.0
Obsoletes:	%{_lib}digikamcore7.9.0 < 7.10.0

%description -n %{libdigikamcore}
Library File needed by %{name}

%files -n %{libdigikamcore}
%{_libdir}/libdigikamcore.so.%{libdigikamcore_major}*

#-----------------------------------------------------------------------

%define libdigikamgui_major 8.4.0
%define libdigikamgui %mklibname digikamgui

%package -n %{libdigikamgui}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}digikamgui5.9.0 < 6.0.0
Obsoletes:	%{_lib}digikamgui6.0.0 < 6.1.0
Obsoletes:	%{_lib}digikamgui6.1.0 < 6.2.0
Obsoletes:	%{_lib}digikamgui6.2.0 < 6.3.0
Obsoletes:	%{_lib}digikamgui6.3.0 < 6.4.0
Obsoletes:	%{_lib}digikamgui6.4.0 < 6.5.0
Obsoletes:	%{_lib}digikamgui7.0.0 < 7.1.0
Obsoletes:	%{_lib}digikamgui7.1.0 < 7.2.0
Obsoletes:	%{_lib}digikamgui7.2.0 < 7.3.0
Obsoletes:	%{_lib}digikamgui7.3.0 < 7.4.0
Obsoletes:	%{_lib}digikamgui7.4.0 < 7.5.0
Obsoletes:	%{_lib}digikamgui7.5.0 < 7.6.0
Obsoletes:	%{_lib}digikamgui7.6.0 < 7.7.0
Obsoletes:	%{_lib}digikamgui7.7.0 < 7.8.0
Obsoletes:	%{_lib}digikamgui7.8.0 < 7.9.0
Obsoletes:	%{_lib}digikamgui7.9.0 < 7.10.0

%description -n %{libdigikamgui}
Librairie File needed by %name.

%files -n %{libdigikamgui}
%{_libdir}/libdigikamgui.so.%{libdigikamgui_major}*

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
%{_libdir}/*.so
%{_libdir}/cmake/DigikamCore*
%{_libdir}/cmake/DigikamDatabase*
%{_libdir}/cmake/DigikamGui*
%{_libdir}/cmake/DigikamPlugin

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}%{?beta:-%{beta}}
%if 0%{?beta:1}
tar xf %{S:1}
%endif
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-DENABLE_OPENCV3:BOOL=ON \
	-DENABLE_MYSQLSUPPORT:BOOL=ON \
	-DENABLE_INTERNALMYSQL:BOOL=OFF \
	-DENABLE_AKONADICONTACTSUPPORT:BOOL=ON \
	-DENABLE_APPSTYLES:BOOL=ON \
	-DENABLE_KFILEMETADATASUPPORT:BOOL=ON \
	-DENABLE_MEDIAPLAYER:BOOL=ON \
	-DBUILD_TESTING:BOOL=OFF \
	-DBUILD_WITH_QT6:BOOL=ON \
	-Wno-dev

%build
export LD_LIBRARY_PATH=$(pwd)/build/bin
%ninja_build -C build

%install
export LD_LIBRARY_PATH=$(pwd)/build/bin
%ninja_install -C build

%find_lang %{name} --with-html || echo '%%optional /not/yet/there' >%{name}.lang
