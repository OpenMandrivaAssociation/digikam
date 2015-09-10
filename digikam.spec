%bcond_with external_kvkontakte

Summary:	A KDE photo management utility
Name:		digikam
Epoch:		2
Version:	4.13.0
Release:	0.1
License:	GPLv2+
Group:		Graphics
Url:		http://www.digikam.org
Source0:	http://downloads.sourceforge.net/digikam/%{name}-%{version}.tar.bz2
Source2:	kipiplugin_expoblending_ru.po
Source3:	kipiplugin_panorama_ru.po
Source4:	kipiplugin_videoslideshow_ru.po
Source100:	%{name}.rpmlintrc
Patch1:		digikam-4.9.0-soversion.patch
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	eigen3
BuildRequires:	flex
BuildRequires:	imagemagick
BuildRequires:	qtsoap-devel
%if %{mdvver} >= 201400
BuildRequires:	mariadb-server
%else
BuildRequires:	mysql-core
BuildRequires:	mysql-common
%endif
BuildRequires:	baloo-devel
BuildRequires:	gomp-devel
BuildRequires:	hupnp-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	marble-devel
BuildRequires:	tiff-devel
BuildRequires:	kfilemetadata-devel
%if "%{disttag}" == "omv"
BuildRequires:	pkgconfig(qca2)
%endif
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libkexiv2)
BuildRequires:	pkgconfig(libksane)
BuildRequires:	pkgconfig(libkdcraw)
BuildRequires:	pkgconfig(libkipi)
BuildRequires:	pkgconfig(libpgf)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(lqr-1) >= 0.4.0
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(QtGStreamer-1.0)
BuildRequires:	pkgconfig(sqlite3)
%if %{with external_kvkontakte}
BuildRequires:	kvkontakte-devel
%endif
%if %{mdvver} >= 201400
Requires:	mariadb-common
%else
Requires:	mysql-core
Requires:	mysql-common
%endif
Requires:	kdebase4-runtime
Requires:	kipi-common
Requires:	kipi-plugins
Requires:	libkgeomap-common
Requires:	libkdcraw-common
Requires:	qt4-database-plugin-sqlite
Requires:	libgphoto-common

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

%files -f %{name}.lang
%doc core/AUTHORS core/ChangeLog core/COPYING core/COPYING.LIB core/NEWS core/README core/TODO
%{_kde_bindir}/digikam
%{_kde_bindir}/digitaglinktree
%{_kde_bindir}/cleanup_digikamdb
%{_kde_libdir}/kde4/digikam*.so
%{_kde_libdir}/kde4/kio_digikam*.so
%{_kde_appsdir}/digikam
%{_kde_appsdir}/kconf_update/adjustlevelstool.upd
%{_kde_appsdir}/solid/actions/digikam*.desktop
%{_kde_applicationsdir}/digikam.desktop
%{_kde_datadir}/appdata/digikam.appdata.xml
%{_kde_datadir}/appdata/digiKam-ImagePlugin_*.metainfo.xml
%{_kde_services}/digikam*.desktop
%{_kde_services}/digikam*.protocol
%{_kde_servicetypes}/digikam*.desktop
%{_kde_mandir}/man1/digitaglinktree.1*
%{_kde_mandir}/man1/cleanup_digikamdb.1*
%{_kde_iconsdir}/*/*/apps/digikam.*
%{_kde_libdir}/kde4/libexec/digikamdatabaseserver

#-----------------------------------------------------------------------

%package -n libkface-common
Summary:       Common files for libkface library
Group:         Graphics
Url:           https://projects.kde.org/projects/extragear/libs/libkface
BuildArch:     noarch
Conflicts:     %{name} < 1:2.0.0-0.rc1.2

%description -n libkface-common
Common files for libkface library.

Libkface is a Qt/C++ wrapper around LibFace library to perform face recognition
and detection over pictures.

%files -n libkface-common
%doc extra/libkface/README extra/libkface/AUTHORS extra/libkface/COPYING
%{_kde_appsdir}/libkface

#-----------------------------------------------------------------------

%package -n libkgeomap-common
Summary:	Common files for libkgeomap library
Group:		Graphics
Url:		https://projects.kde.org/projects/extragear/libs/libkgeomap
Conflicts:	%{name} < 1:2.0.0-0.rc1.2

%description -n libkgeomap-common
Common files for libkgeomap library

Libkgeomap is a wrapper around world map components as Marble,
OpenstreetMap and Google Maps, for browsing and arranging
photos on a map.

%files -n libkgeomap-common -f libkgeomap.lang
%doc extra/libkgeomap/README extra/libkgeomap/AUTHORS
%{_bindir}/libkgeomap_demo
%{_kde_appsdir}/libkgeomap

#-----------------------------------------------------------------------

%package -n showfoto
Summary:	Fast Image Editor
Group:		Graphics
Requires:	libkdcraw-common
# Otherwise it doesn't work properly
Requires:	%{name} = %{EVRD}

%description -n showfoto
Showfoto is a fast Image Editor with powerful image editing tools.
You can use it to view your photographs and improve them.

%files -n showfoto -f showfoto.lang
%{_kde_bindir}/showfoto
%{_kde_applicationsdir}/showfoto.desktop
%{_kde_appsdir}/showfoto
%{_kde_datadir}/appdata/showfoto.appdata.xml
%{_kde_iconsdir}/*/*/apps/showfoto.*

#-----------------------------------------------------------------------

%define libdigikamdatabase_major 4
%define libdigikamdatabase %mklibname digikamdatabase %{libdigikamdatabase_major}

%package -n %{libdigikamdatabase}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}digikamdatabase2 < 2:3.0.0
Obsoletes:	%{_lib}digikamdatabase3 < 2:4.0.0

%description -n %{libdigikamdatabase}
Librairie File needed by %{name}

%files -n %{libdigikamdatabase}
%{_kde_libdir}/libdigikamdatabase.so.%{libdigikamdatabase_major}*

#-----------------------------------------------------------------------

%define libdigikamcore_major 4
%define libdigikamcore %mklibname digikamcore %{libdigikamcore_major}

%package -n %{libdigikamcore}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}digikamcore2 < 2:3.0.0
Obsoletes:	%{_lib}digikamcore3 < 2:4.0.0

%description -n %{libdigikamcore}
Librairie File needed by %{name}

%files -n %{libdigikamcore}
%{_kde_libdir}/libdigikamcore.so.%{libdigikamcore_major}*

#-----------------------------------------------------------------------

%define libkface_major 3
%define libkface %mklibname kface %{libkface_major}

%package -n %{libkface}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/libs/libkface
Obsoletes:	%{_lib}kface1 < 2:3.3.0

%description -n %{libkface}
Librairie File needed by %{name}

Libkface is a Qt/C++ wrapper around LibFace library to perform face recognition
and detection over pictures.

%files -n %{libkface}
%{_kde_libdir}/libkface.so.%{libkface_major}*

#-----------------------------------------------------------------------

%define libkgeomap_major 2
%define libkgeomap %mklibname kgeomap %{libkgeomap_major}
%define libkmap %mklibname kmap 1

%package -n %{libkgeomap}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/libs/libkgeomap
Obsoletes:	%{libkmap} < 1:2.0.0-0.rc1.2

%description -n %{libkgeomap}
Librairie File needed by %{name}

Libkgeomap is a wrapper around world map components as Marble, OpenstreetMap
and Google Maps,for browsing and arranging photos on a map.

%files -n %{libkgeomap}
%{_kde_libdir}/libkgeomap.so.%{libkgeomap_major}*

#-----------------------------------------------------------------------

%define libmediawiki_major 1
%define libmediawiki %mklibname mediawiki %{libmediawiki_major}

%package -n %{libmediawiki}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/libs/libmediawiki

%description -n %{libmediawiki}
Librairie File needed by %{name}

libmediawiki is a KDE C++ interface for MediaWiki based
web service as wikipedia.org.

%files -n %{libmediawiki}
%{_kde_libdir}/libmediawiki.so.%{libmediawiki_major}*

#-----------------------------------------------------------------------

%define libkipiplugins_major 4
%define libkipiplugins %mklibname kipiplugins %{libkipiplugins_major}

%package -n %{libkipiplugins}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}kipiplugins2 < 2:3.0.0
Obsoletes:	%{_lib}kipiplugins3 < 2:4.0.0

%description -n %{libkipiplugins}
Librairie File needed by %{name}

%files -n %{libkipiplugins}
%{_kde_libdir}/libkipiplugins.so.%{libkipiplugins_major}*

#-----------------------------------------------------------------------

%define libkvkontakte_major 1
%define libkvkontakte %mklibname kvkontakte %libkvkontakte_major

%package -n %libkvkontakte
Summary: Runtime library for %{name}
Group: System/Libraries
URL: https://projects.kde.org/projects/extragear/libs/libkvkontakte

%description -n %libkvkontakte
Librairie File needed by %name

Libkvkontakte is a library for accessing the features of social networking
site vkontakte.ru.

%files -n %libkvkontakte
%_kde_libdir/libkvkontakte.so.%{libkvkontakte_major}*
%_kde_libdir/libkvkontakte.so.4*

#-----------------------------------------------------------------------

%package -n kipi-plugins
Summary:	KDE image Interface Plugins
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/graphics/kipi-plugins
BuildArch:	noarch
Suggests:	kipi-plugins-acquireimages
Suggests:	kipi-plugins-advancedslideshow
Suggests:	kipi-plugins-batchprocess
Suggests:	kipi-plugins-calendar
Suggests:	kipi-plugins-debianscreenshot
Suggests:	kipi-plugins-dlna
Suggests:	kipi-plugins-dngconverter
Suggests:	kipi-plugins-dropbox
Suggests:	kipi-plugins-expoblending
Suggests:	kipi-plugins-facebook
Suggests:	kipi-plugins-flashexport
Suggests:	kipi-plugins-flickr
Suggests:	kipi-plugins-galleryexport
Suggests:	kipi-plugins-googleservices
Suggests:	kipi-plugins-gpssync
Suggests:	kipi-plugins-htmlexport
Suggests:	kipi-plugins-imageshack
Suggests:	kipi-plugins-imageviewer
Suggests:	kipi-plugins-imgurexport
Suggests:	kipi-plugins-ipodexport
Suggests:	kipi-plugins-jalbumexport
Suggests:	kipi-plugins-jpeglossless
Suggests:	kipi-plugins-kioexportimport
Suggests:	kipi-plugins-kmlexport
Suggests:	kipi-plugins-kopete
Suggests:	kipi-plugins-metadataedit
Suggests:	kipi-plugins-panorama
Suggests:	kipi-plugins-piwigoexport
Suggests:	kipi-plugins-printimages
Suggests:	kipi-plugins-rajceexport
Suggests:	kipi-plugins-rawconverter
Suggests:	kipi-plugins-removeredeyes
Suggests:	kipi-plugins-sendimages
Suggests:	kipi-plugins-shwup
Suggests:	kipi-plugins-smug
Suggests:	kipi-plugins-timeadjust
Suggests:	kipi-plugins-videoslideshow
Suggests:	kipi-plugins-vkontakte
Suggests:	kipi-plugins-wikimedia
Suggests:	kipi-plugins-yandexfotki

%description -n kipi-plugins
The library of the KDE Image Plugin Interface.

Libkipi allows image applications to use a plugin architecture
for additional functionality such as: RawConverter, SlideShow, 
ImagesGallery, HTMLExport, PrintAssistant...

%files -n kipi-plugins -f kipi-plugins.lang
%{_datadir}/apps/kipi/tips
%doc extra/kipi-plugins/AUTHORS extra/kipi-plugins/COPYING extra/kipi-plugins/COPYING-ADOBE extra/kipi-plugins/ChangeLog extra/kipi-plugins/README extra/kipi-plugins/TODO extra/kipi-plugins/NEWS
%{_kde_applicationsdir}/kipiplugins.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-acquireimages
Summary:	Acquireimages
Group:		System/Libraries
Requires:	kipi-common
Conflicts:	kipi-plugins < 1:1.8.0-1

%description -n kipi-plugins-acquireimages
A tool to acquire images using flat scanner.

%files -n kipi-plugins-acquireimages -f kipiplugin_acquireimages.lang
%{_kde_appsdir}/kipi/kipiplugin_acquireimagesui.rc
%{_kde_bindir}/scangui
%{_kde_libdir}/kde4/kipiplugin_acquireimages.so
%{_kde_services}/kipiplugin_acquireimages.desktop
%{_kde_applicationsdir}/scangui.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-advancedslideshow
Summary:	Advanced Slideshow Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-advancedslideshow
A tool to slide images with 2D and 3D effects using OpenGL.

%files -n kipi-plugins-advancedslideshow -f kipiplugin_advancedslideshow.lang
%{_kde_appsdir}/kipi/kipiplugin_advancedslideshowui.rc
%{_kde_libdir}/kde4/kipiplugin_advancedslideshow.so
%{_kde_services}/kipiplugin_advancedslideshow.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-slideshow.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-batchprocess
Summary:	Batch Process Images Kipi Plugin
Group:		System/Libraries
# Resizing pictures need convert from imagemagick
Requires:	imagemagick
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-batchprocess
KIPI Batch Processing Images Plugin.

%files -n kipi-plugins-batchprocess -f kipiplugin_batchprocessimages.lang
%{_kde_appsdir}/kipi/kipiplugin_batchprocessimagesui.rc
%{_kde_libdir}/kde4/kipiplugin_batchprocessimages.so
%{_kde_services}/kipiplugin_batchprocessimages.desktop
%{_kde_iconsdir}/hicolor/*/actions/recompressimages.png
%{_kde_iconsdir}/hicolor/*/actions/renameimages.png
%{_kde_iconsdir}/hicolor/*/actions/resizeimages.png
%{_kde_iconsdir}/hicolor/*/actions/borderimages.png
%{_kde_iconsdir}/hicolor/*/actions/colorimages.png
%{_kde_iconsdir}/hicolor/*/actions/convertimages.png
%{_kde_iconsdir}/hicolor/*/actions/effectimages.png
%{_kde_iconsdir}/hicolor/*/actions/filterimages.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-calendar
Summary:	Calendar Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-calendar
A tool to create calendars.

%files -n kipi-plugins-calendar -f kipiplugin_calendar.lang
%{_kde_appsdir}/kipi/kipiplugin_calendarui.rc
%{_kde_libdir}/kde4/kipiplugin_calendar.so
%{_kde_services}/kipiplugin_calendar.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-debianscreenshot
Summary:	Debian Screenshot Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-debianscreenshot
A tool to export images to the Debian Screenshots site.

%files -n kipi-plugins-debianscreenshot -f kipiplugin_debianscreenshots.lang
%{_kde_appsdir}/kipi/kipiplugin_debianscreenshotsui.rc
%{_kde_libdir}/kde4/kipiplugin_debianscreenshots.so
%{_kde_services}/kipiplugin_debianscreenshots.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-debianscreenshots.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-dlna
Summary:	DLNA support
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-dlna
A tool to support DLNA.

%files -n kipi-plugins-dlna -f kipiplugin_dlnaexport.lang
%{_kde_appsdir}/kipi/kipiplugin_dlnaexportui.rc
%{_kde_appsdir}/kipiplugin_dlnaexport
%{_kde_libdir}/kde4/kipiplugin_dlnaexport.so
%{_kde_services}/kipiplugin_dlnaexport.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-dlna.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-dngconverter
Summary:	Dng converter Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-dngconverter
A tool to convert Raw Image to Digital NeGative.

%files -n kipi-plugins-dngconverter -f kipiplugin_dngconverter.lang
%{_kde_appsdir}/kipi/kipiplugin_dngconverterui.rc
%{_kde_bindir}/dngconverter
%{_kde_applicationsdir}/dngconverter.desktop
%{_kde_libdir}/kde4/kipiplugin_dngconverter.so
%{_kde_services}/kipiplugin_dngconverter.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-dngconverter.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-dropbox
Summary:	Dropbox export Kipi Plugin
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-dropbox
A tool to export images to a remote Dropbox web service.

%files -n kipi-plugins-dropbox -f kipiplugin_dropbox.lang
%{_kde_appsdir}/kipi/kipiplugin_dropboxui.rc
%{_kde_libdir}/kde4/kipiplugin_dropbox.so
%{_kde_services}/kipiplugin_dropbox.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-dropbox.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-expoblending
Summary:	Expoblending Kipi Plugin
Group:		System/Libraries
# need align_image_stack from Hugin project and enfuse from Enblend project (runtime dependency)
Requires:	hugin
Requires:	libkdcraw-common
Requires:	kipi-common
Conflicts:	kipi-plugins < 1:1.8.0-1

%description -n kipi-plugins-expoblending
A tool to blend bracketed images.

%files -n kipi-plugins-expoblending -f kipiplugin_expoblending.lang
%{_kde_appsdir}/kipi/kipiplugin_expoblendingui.rc
%{_kde_appsdir}/kipiplugin_expoblending
%{_kde_bindir}/expoblending
%{_kde_applicationsdir}/expoblending.desktop
%{_kde_libdir}/kde4/kipiplugin_expoblending.so
%{_kde_services}/kipiplugin_expoblending.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-expoblending.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-facebook
Summary:	Facebook Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-facebook
A tool to import/export images to/from a remote Facebook web service.

%files -n kipi-plugins-facebook -f kipiplugin_facebook.lang
%{_kde_appsdir}/kipi/kipiplugin_facebookui.rc
%{_kde_libdir}/kde4/kipiplugin_facebook.so
%{_kde_services}/kipiplugin_facebook.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-facebook.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-flashexport
Summary:	Flash export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-flashexport
A tool to export images to Flash.

%files -n kipi-plugins-flashexport -f kipiplugin_flashexport.lang
%{_kde_appsdir}/kipi/kipiplugin_flashexportui.rc
%{_kde_libdir}/kde4/kipiplugin_flashexport.so
%{_kde_appsdir}/kipiplugin_flashexport
%{_kde_services}/kipiplugin_flashexport.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-flash.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-flickr
Summary:	Flick Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-flickr
A tool to export images to a remote Flickr, 23 and Zoomr web services.

%files -n kipi-plugins-flickr -f kipiplugin_flickrexport.lang
%{_kde_appsdir}/kipi/kipiplugin_flickrexportui.rc
%{_kde_libdir}/kde4/kipiplugin_flickrexport.so
%{_kde_services}/kipiplugin_flickrexport.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-flickr.*
%{_kde_iconsdir}/hicolor/*/apps/kipi-hq.*
%{_kde_iconsdir}/hicolor/*/apps/kipi-zooomr.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-galleryexport
Summary:	Gallery Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-galleryexport
A tool to export images to a remote Gallery.

%files -n kipi-plugins-galleryexport -f kipiplugin_galleryexport.lang
%{_kde_appsdir}/kipi/kipiplugin_galleryexportui.rc
%{_kde_libdir}/kde4/kipiplugin_galleryexport.so
%{_kde_appsdir}/kipiplugin_galleryexport
%{_kde_services}/kipiplugin_galleryexport.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-gallery.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-googleservices
Summary:	Google services export Kipi Plugin
Group:		System/Libraries
Requires:	kipi-common
%rename kipi-plugins-gooledrive
%rename kipi-plugins-picasa

%description -n kipi-plugins-googleservices
A tool to export images to a remote services.

%files -n kipi-plugins-googledrive -f kipiplugin_googledrive.lang
%{_kde_appsdir}/kipi/kipiplugin_googleservicesui.rc
%{_kde_libdir}/kde4/kipiplugin_googleservices.so
%{_kde_services}/kipiplugin_googleservices.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-googledrive.*
%{_kde_iconsdir}/hicolor/*/apps/kipi-picasa.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-gpssync
Summary:	GPS Sync Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-gpssync
A tool to geolocalize pictures.

%files -n kipi-plugins-gpssync -f kipiplugin_gpssync.lang
%{_kde_appsdir}/kipi/kipiplugin_gpssyncui.rc
%{_kde_appsdir}/gpssync
%{_kde_libdir}/kde4/kipiplugin_gpssync.so
%{_kde_services}/kipiplugin_gpssync.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-gpsimagetag.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-htmlexport
Summary:	Html Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 2:3.2.0
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-htmlexport
A tool to export images collections into a static XHTML page.

%files -n kipi-plugins-htmlexport -f kipiplugin_htmlexport.lang
%{_kde_appsdir}/kipi/kipiplugin_htmlexportui.rc
%{_kde_appsdir}/kipiplugin_htmlexport
%{_kde_libdir}/kde4/kipiplugin_htmlexport.so
%{_kde_services}/kipiplugin_htmlexport.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-imageviewer
Summary:	Image Viewer Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-imageviewer
A tool to preview images using OpenGl.

%files -n kipi-plugins-imageviewer -f kipiplugin_imageviewer.lang
%{_kde_appsdir}/kipi/kipiplugin_imageviewerui.rc
%{_kde_libdir}/kde4/kipiplugin_imageviewer.so
%{_kde_appsdir}/kipiplugin_imageviewer
%{_kde_services}/kipiplugin_imageviewer.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-ogl.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-imageshack
Summary:	Imageshack Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-imageshack
A tool to export images to ImageShack.

%files -n kipi-plugins-imageshack -f kipiplugin_imageshackexport.lang
%{_kde_appsdir}/kipi/kipiplugin_imageshackexportui.rc
%{_kde_libdir}/kde4/kipiplugin_imageshackexport.so
%{_kde_services}/kipiplugin_imageshackexport.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-imageshack.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-imgurexport
Summary:	Imgur Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-imgurexport
A tool to export pictures to Imgur.

%files -n kipi-plugins-imgurexport -f kipiplugin_imgurexport.lang
%{_kde_appsdir}/kipi/kipiplugin_imgurexportui.rc
%{_kde_libdir}/kde4/kipiplugin_imgurexport.so
%{_kde_services}/kipiplugin_imgurexport.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-imgur.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-ipodexport
Summary:	Ipod Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-ipodexport
A tool to export pictures to an Ipod device.

%files -n kipi-plugins-ipodexport -f kipiplugin_ipodexport.lang
%{_kde_appsdir}/kipi/kipiplugin_ipodexportui.rc
%{_kde_libdir}/kde4/kipiplugin_ipodexport.so
%{_kde_services}/kipiplugin_ipodexport.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-jalbumexport
Summary:	JAlbum Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-jalbumexport
A tool to export images to a remote JAlbum.

%files -n kipi-plugins-jalbumexport -f kipiplugin_jalbumexport.lang
%{_kde_appsdir}/kipi/kipiplugin_jalbumexportui.rc
%{_kde_libdir}/kde4/kipiplugin_jalbumexport.so
%{_kde_services}/kipiplugin_jalbumexport.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-jalbum.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-jpeglossless
Summary:	Jpeg Lossless Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-jpeglossless
A tool to rotate/flip images without losing quality.

%files -n kipi-plugins-jpeglossless -f kipiplugin_jpeglossless.lang
%{_kde_appsdir}/kipi/kipiplugin_jpeglosslessui.rc
%{_kde_libdir}/kde4/kipiplugin_jpeglossless.so
%{_kde_services}/kipiplugin_jpeglossless.desktop
%{_kde_iconsdir}/hicolor/*/actions/flip-horizontal.png
%{_kde_iconsdir}/hicolor/*/actions/grayscaleconvert.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-kioexportimport
Summary:	Kio Export Import Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-kioexportimport
A tool to export pictures to or import from a remote directory that is
accessible via KIO.

%files -n kipi-plugins-kioexportimport -f kipiplugin_kioexportimport.lang
%{_kde_libdir}/kde4/kipiplugin_kioexportimport.so
%{_kde_services}/kipiplugin_kioexportimport.desktop
%{_kde_appsdir}/kipi/kipiplugin_kioexportimportui.rc

#-----------------------------------------------------------------------

%package -n kipi-plugins-kmlexport
Summary:	Create KML files to present images with coordinates
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-kmlexport
A plugin to create KML files to present images with coordinates.

%files -n kipi-plugins-kmlexport -f kipiplugin_kmlexport.lang
%{_kde_appsdir}/kipi/kipiplugin_kmlexportui.rc
%{_kde_libdir}/kde4/kipiplugin_kmlexport.so
%{_kde_services}/kipiplugin_kmlexport.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-kopete
Summary:	Kopete kipi plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-kopete
A tool to export images to an instant messaging contact.

%files -n kipi-plugins-kopete -f kipiplugin_kopete.lang
%{_kde_appsdir}/kipi/kipiplugin_kopeteui.rc
%{_kde_libdir}/kde4/kipiplugin_kopete.so
%{_kde_services}/kipiplugin_kopete.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-metadataedit
Summary:	Meta Data Edit kipi plugins
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-metadataedit
A tool to edit EXIF,IPTC and XMP metadata.

%files -n kipi-plugins-metadataedit -f kipiplugin_metadataedit.lang
%{_kde_appsdir}/kipi/kipiplugin_metadataeditui.rc
%{_kde_libdir}/kde4/kipiplugin_metadataedit.so
%{_kde_services}/kipiplugin_metadataedit.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-metadataedit.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-panorama
Summary:	Panorama tools
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common
Requires:	hugin

%description -n kipi-plugins-panorama
A tool to create panorama.

%files -n kipi-plugins-panorama -f kipiplugin_panorama.lang
%{_kde_appsdir}/kipi/kipiplugin_panoramaui.rc
%{_kde_bindir}/panoramagui
%{_kde_libdir}/kde4/kipiplugin_panorama.so
%{_kde_appsdir}/kipiplugin_panorama/
%{_kde_services}/kipiplugin_panorama.desktop
%{_kde_applicationsdir}/panoramagui.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-panorama.*

#-----------------------------------------------------------------------

%package -n kipiplugin-photolayouts-editor
Summary:	Photo Layouts Editor
Group:		System/Libraries
Requires:	kipi-common

%description -n kipiplugin-photolayouts-editor
Photo Layouts Editor.

%files -n kipiplugin-photolayouts-editor -f kipiplugin_photolayouteditor.lang
%{_kde_appsdir}/kipi/kipiplugin_photolayoutseditorui.rc
%{_kde_appsdir}/photolayoutseditor
%{_kde_applicationsdir}/photolayoutseditor.desktop
%{_kde_bindir}/photolayoutseditor
%{_kde_libdir}/kde4/kipiplugin_photolayoutseditor.so
%{_kde_services}/kipiplugin_photolayoutseditor.desktop
%{_kde_servicetypes}/photolayoutseditorborderplugin.desktop
%{_kde_servicetypes}/photolayoutseditoreffectplugin.desktop
%{_kde_datadir}/templates/kipiplugins_photolayoutseditor
%{_kde_datadir}/config.kcfg/photolayoutseditor.kcfg
%{_kde_iconsdir}/hicolor/*/apps/photolayoutseditor.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-piwigoexport
Summary:	Piwi Go Export
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-piwigoexport
A tool to export images to a remote Piwigo.

%files -n kipi-plugins-piwigoexport -f kipiplugin_piwigoexport.lang
%{_kde_appsdir}/kipi/kipiplugin_piwigoexportui.rc
%{_kde_libdir}/kde4/kipiplugin_piwigoexport.so
%{_kde_appsdir}/kipiplugin_piwigoexport
%{_kde_services}/kipiplugin_piwigoexport.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-piwigo.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-printimages
Summary:	Print Images Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-printimages
A tool to print images in various formats.

%files -n kipi-plugins-printimages -f kipiplugin_printimages.lang
%{_kde_appsdir}/kipi/kipiplugin_printimagesui.rc
%{_kde_libdir}/kde4/kipiplugin_printimages.so
%{_kde_services}/kipiplugin_printimages.desktop
%{_kde_appsdir}/kipiplugin_printimages/

#-----------------------------------------------------------------------

%package -n kipi-plugins-rajceexport
Summary:	Rajce.net Exporter
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-rajceexport
A tool to export images to a remote rajce.net service.

%files -n kipi-plugins-rajceexport -f kipiplugin_rajceexport.lang
%{_kde_appsdir}/kipi/kipiplugin_rajceexportui.rc
%{_kde_libdir}/kde4/kipiplugin_rajceexport.so
%{_kde_services}/kipiplugin_rajceexport.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-rajce.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-rawconverter
Summary:	Rawconverter kipi plugins
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-rawconverter
A tool to convert Raw Image to JPEG/PNG/TIFF.

%files -n kipi-plugins-rawconverter -f kipiplugin_rawconverter.lang
%{_kde_appsdir}/kipi/kipiplugin_rawconverterui.rc
%{_kde_libdir}/kde4/kipiplugin_rawconverter.so
%{_kde_iconsdir}/oxygen/*/apps/rawconverter.png
%{_kde_services}/kipiplugin_rawconverter.desktop
%{_kde_iconsdir}/oxygen/scalable/apps/rawconverter.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-removeredeyes
Summary:	Remove red eyes kipi-plugins
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-removeredeyes
A tool to remove red eyes automatically from images.

%files -n kipi-plugins-removeredeyes -f kipiplugin_removeredeyes.lang
%{_kde_appsdir}/kipi/kipiplugin_removeredeyesui.rc
%{_kde_libdir}/kde4/kipiplugin_removeredeyes.so
%{_kde_datadir}/apps/kipiplugin_removeredeyes
%{_kde_services}/kipiplugin_removeredeyes.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-sendimages
Summary:	Send Images kipi plugins
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-sendimages
A tool to send images by e-mail.

%files -n kipi-plugins-sendimages -f kipiplugin_sendimages.lang
%{_kde_appsdir}/kipi/kipiplugin_sendimagesui.rc
%{_kde_libdir}/kde4/kipiplugin_sendimages.so 
%{_kde_services}/kipiplugin_sendimages.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-shwup
Summary:	Shwup Kipi Plugins
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-shwup
A tool to export images to a remote Shwup web service.

%files -n kipi-plugins-shwup -f kipiplugin_shwup.lang
%{_kde_appsdir}/kipi/kipiplugin_shwupui.rc
%{_kde_libdir}/kde4/kipiplugin_shwup.so
%{_kde_services}/kipiplugin_shwup.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-shwup.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-smug
Summary:	Smug Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-smug
A tool to import/export images to/from SmugMug web service.

%files -n kipi-plugins-smug -f kipiplugin_smug.lang
%{_kde_appsdir}/kipi/kipiplugin_smugui.rc
%{_kde_libdir}/kde4/kipiplugin_smug.so
%{_kde_services}/kipiplugin_smug.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-smugmug.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-timeadjust
Summary:	Time Adjust kipi plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-timeadjust
A Tool to adjust time and date.

%files -n kipi-plugins-timeadjust -f kipiplugin_timeadjust.lang
%{_kde_appsdir}/kipi/kipiplugin_timeadjustui.rc
%{_kde_libdir}/kde4/kipiplugin_timeadjust.so
%{_kde_services}/kipiplugin_timeadjust.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-timeadjust.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-videoslideshow
Summary:	Video Slide Show export kipi plugin
Group:		System/Libraries
Requires:	kipi-common
Requires:	imagemagick

%description -n kipi-plugins-videoslideshow
A tool to export images as Video Slide Show.

%files -n kipi-plugins-videoslideshow -f kipiplugin_videoslideshow.lang
%{_kde_appsdir}/kipi/kipiplugin_videoslideshowui.rc
%{_kde_libdir}/kde4/kipiplugin_videoslideshow.so
%{_kde_services}/kipiplugin_videoslideshow.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-vkontakte
Summary:	VKontakte.ru Exporter
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-vkontakte
A tool to export on VKontakte.ru Web service

%files -n kipi-plugins-vkontakte -f kipiplugin_vkontakte.lang
%{_kde_appsdir}/kipi/kipiplugin_vkontakteui.rc
%{_kde_libdir}/kde4/kipiplugin_vkontakte.so
%{_kde_services}/kipiplugin_vkontakte.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-wikimedia
Summary:	Wikimedia Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-wikimedia
A tool to export images to a remote MediaWiki site

%files -n kipi-plugins-wikimedia -f kipiplugin_wikimedia.lang
%{_kde_appsdir}/kipi/kipiplugin_wikimediaui.rc
%{_kde_libdir}/kde4/kipiplugin_wikimedia.so
%{_kde_services}/kipiplugin_wikimedia.desktop
%{_kde_iconsdir}/hicolor/*/apps/kipi-wikimedia.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-yandexfotki
Summary:	Yandex.Fotki Exporter
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-yandexfotki
A tool to export images to a remote Yandex.Fotki web service.

%files -n kipi-plugins-yandexfotki -f kipiplugin_yandexfotki.lang
%{_kde_appsdir}/kipi/kipiplugin_yandexfotkiui.rc
%{_kde_libdir}/kde4/kipiplugin_yandexfotki.so
%{_kde_services}/kipiplugin_yandexfotki.desktop

#-----------------------------------------------------------------------

%define libnamedev %mklibname digikam -d
%define libmediawiki_devel %mklibname -d mediawiki

%package -n %{libmediawiki_devel}
Summary:	Headers to build packages against libmediawiki library
Group:		Development/C
Conflicts:	%{libnamedev} < 1:2.0.0-rc1.2
Requires:	%{libmediawiki} = %{EVRD}
Provides:	libmediawiki-devel = %{EVRD}

%description -n %{libmediawiki_devel}
This package contains the libraries and headers files needed to develop progams
which make use of libmediawiki library.

libmediawiki is a KDE C++ interface for MediaWiki based web service as 
wikipedia.org.

%files -n %{libmediawiki_devel}
%{_kde_libdir}/libmediawiki.so

#-----------------------------------------------------------------------

%define libkface_devel %mklibname -d kface

%package -n %{libkface_devel}
Summary:	Headers to build packages against libkface library
Group:		Development/C
Conflicts:	%{libnamedev} < 1:2.0.0-rc1.2
Requires:	%{libkface} = %{EVRD}
Requires:	libkface-common
Provides:	kface-devel = %{version}-%{release}
Provides:	libkface-devel = %{version}-%{release}

%description -n %{libkface_devel}
This package contains the libraries and headers files needed to develop progams
which make use of libkface library.

Libkface is a Qt/C++ wrapper around LibFace library to perform face recognition
and detection over pictures.

%files -n %{libkface_devel}
%{_kde_libdir}/libkface.so
%{_libdir}/cmake/Kface-3.5.0

#-----------------------------------------------------------------------

%define libkgeomap_devel %mklibname -d kgeomap

%package -n %{libkgeomap_devel}
Summary:	Headers to build packages against libkgeomap library
Group:		Development/C
Conflicts:	%{libnamedev} < 1:2.0.0-rc1.2
Requires:	libkgeomap-common
Requires:	%{libkgeomap} = %{EVRD}
Provides:	kgeomap-devel = %{version}-%{release}
Provides:	libkgeomap-devel = %{version}-%{release}

%description -n %{libkgeomap_devel}
This package contains the libraries and headers files needed to develop progams
which make use of libkgeomap (old libkmap) library.

Libkgeomap is a wrapper around world map components as Marble, OpenstreetMap
and Google Maps,for browsing and arranging photos on a map.

%files -n %{libkgeomap_devel}
%{_kde_libdir}/libkgeomap.so

#-----------------------------------------------------------------------

%define libkvkontakte_devel %mklibname -d kvkontakte
%package -n  %libkvkontakte_devel
Summary:     Headers to build packages against libkvkontakte library
Group:       Development/C
Requires:    %libkvkontakte = %epoch:%version-%release
Provides:    kvkontakte-devel = %version-%release
Provides:    libkvkontakte-devel = %version-%release

%description -n %libkvkontakte_devel
This package contains the libraries and headers files needed to develop progams
which make use of libkvkontakte library.

Libkvkontakte is a library for accessing the features of social networking
site vkontakte.ru.

%files -n %libkvkontakte_devel
#%_kde_includedir/libkvkontakte
%_kde_libdir/libkvkontakte.so
%_libdir/cmake/LibKVkontakte

#-----------------------------------------------------------------------

%package -n %{libnamedev}
Summary:	Static libraries and headers for %{name}
Group:		Development/C
Provides:	lib%{name}-devel = %{EVRD}
Provides:	kipi-plugins-devel = %{EVRD}
Obsoletes:	kipi-plugins-devel < 1:2.0.0
Requires:	%{libdigikamcore} = %{EVRD}
Requires:	%{libdigikamdatabase} = %{EVRD}
Requires:	%{libkgeomap_devel} = %{EVRD}
Requires:	%{libmediawiki_devel} = %{EVRD}
Requires:	%{libkface_devel} = %{EVRD}
Requires:	%{libkipiplugins} = %{EVRD}

%description -n %{libnamedev}
%{libnamedev} contains the libraries and header files needed to
develop programs which make use of %{name}.
The library documentation is available on header files.

%files -n %{libnamedev}
%{_kde_libdir}/libdigikamcore.so
%{_kde_libdir}/libdigikamdatabase.so
%{_kde_libdir}/libkipiplugins.so

#-----------------------------------------------------------------------

%prep
%setup -q
find . -name ox*-app-showfoto.* -exec rm -rf '{}' \;
find . -name ox*-app-digikam.* -exec rm -rf '{}' \;

# fix qtsoap find
sed -i s#/usr/include/qt4#%{_qt_includedir}# extra/kipi-plugins/cmake/modules/FindQtSoap.cmake

%patch1 -p1

pushd po
# Remove wallpaper po files (kipiplugin-wallpaper is not build )
find  . -name kipiplugin_wallpaper.po -exec rm -rf '{}' \;
cp -f %{SOURCE2} ru/kipiplugin_expoblending.po
cp -f %{SOURCE3} ru/kipiplugin_panorama.po
cp -f %{SOURCE4} ru/kipiplugin_videoslideshow.po
popd

%build
%if "%{disttag}" == "omv"
# to find qca2
export PKG_CONFIG_PATH=%{_libdir}/qt4/pkgconfig
%endif

%cmake_kde4 \
	-DDIGIKAMSC_USE_PRIVATE_KDEGRAPHICS=OFF \
	-DENABLE_BALOOSUPPORT=ON \
	-DENABLE_LCMS2=ON \
	-DENABLE_KDEPIMLIBSSUPPORT=ON \
	-DDIGIKAMSC_USE_PRIVATE_SHAREDLIBS=OFF \
	-DDIGIKAMSC_COMPILE_LIBKGEOMAP=ON \
	-DDIGIKAMSC_COMPILE_LIBMEDIAWIKI=ON \
	-DDIGIKAMSC_COMPILE_LIBKFACE=ON \
	-DENABLE_MYSQLSUPPORT=ON -DENABLE_INTERNALMYSQL=ON \
%if %{without external_kvkontakte}
	-DDIGIKAMSC_COMPILE_LIBKVKONTAKTE=ON
%endif

%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde_datadir}/locale/*/LC_MESSAGES/libkipi.mo

# photivo plugin not ready yet
rm -f %{buildroot}%{_kde_datadir}/locale/*/LC_MESSAGES/*photivo*.mo

%find_lang %{name} --with-html || touch %{name}.lang
%find_lang showfoto --with-html || touch showfoto.lang
%find_lang kipi-plugins kipiplugins kipi-plugins.lang --with-html || touch kipi-plugins.lang

%find_lang kipiplugin_acquireimages || touch kipiplugin_acquireimages.lang
%find_lang kipiplugin_advancedslideshow || touch kipiplugin_advancedslideshow.lang
%find_lang kipiplugin_batchprocessimages || touch kipiplugin_batchprocessimages.lang
%find_lang kipiplugin_calendar || touch kipiplugin_calendar.lang
%find_lang kipiplugin_dngconverter || touch kipiplugin_dngconverter.lang
%find_lang kipiplugin_expoblending || touch kipiplugin_expoblending.lang
%find_lang kipiplugin_facebook || touch kipiplugin_facebook.lang
%find_lang kipiplugin_flashexport || touch kipiplugin_flashexport.lang
%find_lang kipiplugin_flickrexport || touch kipiplugin_flickrexport.lang
%find_lang kipiplugin_galleryexport || touch kipiplugin_galleryexport.lang
%find_lang kipiplugin_gpssync || touch kipiplugin_gpssync.lang
%find_lang kipiplugin_htmlexport || touch kipiplugin_htmlexport.lang
%find_lang kipiplugin_imageviewer || touch kipiplugin_imageviewer.lang
%find_lang kipiplugin_ipodexport || touch kipiplugin_ipodexport.lang
%find_lang kipiplugin_jpeglossless || touch kipiplugin_jpeglossless.lang
%find_lang kipiplugin_kioexportimport || touch kipiplugin_kioexportimport.lang
%find_lang kipiplugin_metadataedit || touch kipiplugin_metadataedit.lang
%find_lang kipiplugin_panorama || touch kipiplugin_panorama.lang
%find_lang kipiplugin_picasawebexport || touch kipiplugin_picasawebexport.lang
%find_lang kipiplugin_piwigoexport || touch kipiplugin_piwigoexport.lang
%find_lang kipiplugin_printimages || touch kipiplugin_printimages.lang
%find_lang kipiplugin_rawconverter || touch kipiplugin_rawconverter.lang
%find_lang kipiplugin_removeredeyes || touch kipiplugin_removeredeyes.lang
%find_lang kipiplugin_sendimages || touch kipiplugin_sendimages.lang
%find_lang kipiplugin_shwup || touch kipiplugin_shwup.lang
%find_lang kipiplugin_smug || touch kipiplugin_smug.lang
%find_lang kipiplugin_timeadjust || touch kipiplugin_timeadjust.lang
%find_lang kipiplugin_videoslideshow || touch kipiplugin_videoslideshow.lang
%find_lang kipiplugin_debianscreenshots || touch kipiplugin_debianscreenshots.lang
%find_lang kipiplugin_dlnaexport || touch kipiplugin_dlnaexport.lang
%find_lang kipiplugin_dropbox || touch kipiplugin_dropbox.lang
%find_lang kipiplugin_googledrive || touch kipiplugin_googledrive.lang
%find_lang kipiplugin_imageshackexport || touch kipiplugin_imageshackexport.lang
%find_lang kipiplugin_imgurexport || touch kipiplugin_imgurexport.lang
%find_lang kipiplugin_jalbumexport || touch kipiplugin_jalbumexport.lang
%find_lang kipiplugin_kmlexport || touch kipiplugin_kmlexport.lang
%find_lang kipiplugin_kopete || touch kipiplugin_kopete.lang
#find_lang kipiplugin_photivointegration || touch kipiplugin_photivointegration.lang
%find_lang kipiplugin_photolayouteditor || touch kipiplugin_photolayouteditor.lang
%find_lang kipiplugin_rajceexport || touch kipiplugin_rajceexport.lang
%find_lang kipiplugin_vkontakte || touch kipiplugin_vkontakte.lang
%find_lang kipiplugin_wikimedia || touch kipiplugin_wikimedia.lang
%find_lang kipiplugin_yandexfotki || touch kipiplugin_yandexfotki.lang
%find_lang libkgeomap || touch libkgeomap.lang

