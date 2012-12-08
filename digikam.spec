%bcond_without external_kvkontakte
#define _unpackaged_subdirs_terminate_build 0
%define beta %nil

Name:		digikam
Summary:	A KDE photo management utility
Group:		Graphics
Version:	2.9.0
%if "%{beta}" != ""
Release:	0.%{beta}.1
Source0:	http://downloads.sourceforge.net/digikam/%{name}-software-compilation-%{version}-%{beta}.tar.bz2
%else
Release:	2
Source0:	http://downloads.sourceforge.net/digikam/%{name}-%{version}.tar.bz2
%endif
Epoch:		2
License:	GPLv2+
URL:		http://www.digikam.org
Source1:	digikam-correct-pngfilesfor-apps.xz
%if %{with external_kvkontakte}
Patch0:		digikam-2.4.1-use-external-libvkontake.patch 
%endif

BuildRequires:	kdepimlibs4-devel
BuildRequires:	pkgconfig(libkexiv2)
BuildRequires:	pkgconfig(libksane)
BuildRequires:	pkgconfig(libkdcraw)
BuildRequires:	pkgconfig(libkipi)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(lqr-1) >= 0.4.0
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(libgpod-1.0)
#BuildRequires: pkgconfig(libpgf)
%if %{with external_kvkontakte}
BuildRequires:	libkvkontakte-devel
%endif 
BuildRequires:	libtiff-devel
BuildRequires:	libjasper-devel
BuildRequires:	marble-devel
BuildRequires:	libgomp-devel
BuildRequires:	doxygen
BuildRequires:	mysql-core
BuildRequires:	mysql-common

Requires:	mysql-core
Requires:	mysql-common
Requires:	kdebase4-runtime
Requires:	qt4-database-plugin-sqlite
Requires:	kipi-plugins
Requires:	libkface-common
Requires:	libkgeomap-common
Requires:	libkdcraw-common
Requires:	kipi-common

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
%doc core/AUTHORS core/ChangeLog core/COPYING core/COPYING.LIB core/NEWS core/README core/TODO  core/README.FACE core/TODO.FACE core/TODO.MYSQLPORT
%{_kde_bindir}/digikam
%{_kde_bindir}/digitaglinktree
%{_kde_bindir}/cleanup_digikamdb
%{_kde_libdir}/kde4/digikam*.so
%{_kde_libdir}/kde4/kio_digikam*.so
%{_kde_appsdir}/digikam
%{_kde_appsdir}/kconf_update/adjustlevelstool.upd
%{_kde_appsdir}/solid/actions/digikam*.desktop
%{_kde_applicationsdir}/digikam.desktop
%{_kde_services}/digikam*.desktop
%{_kde_services}/digikam*.protocol
%{_kde_servicetypes}/digikam*.desktop
%{_kde_mandir}/man1/digitaglinktree.1*
%{_kde_mandir}/man1/cleanup_digikamdb.1*
%{_kde_iconsdir}/*/*/apps/digikam.*
%{_kde_libdir}/kde4/libexec/digikamdatabaseserver

#-----------------------------------------------------------------------

%package -n libkface-common
Summary:	Common files for libkface library
Group:		Graphics
URL:		https://projects.kde.org/projects/extragear/libs/libkface
BuildArch:	noarch
Conflicts:	%{name} < 1:2.0.0-0.rc1.2

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
URL:		https://projects.kde.org/projects/extragear/libs/libkgeomap
BuildArch:	noarch
Conflicts:	%{name} < 1:2.0.0-0.rc1.2

%description -n libkgeomap-common
Common files for libkgeomap library

Libkgeomap is a wrapper around world map components as Marble,
OpenstreetMap and Google Maps, for browsing and arranging
photos on a map.

%files -n libkgeomap-common -f libkgeomap.lang
%doc extra/libkgeomap/README extra/libkgeomap/AUTHORS
%{_kde_appsdir}/libkgeomap

#-----------------------------------------------------------------------

%package -n showfoto
Summary:	Fast Image Editor
Group:		Graphics
Requires:	libkdcraw-common

%description -n showfoto
Showfoto is a fast Image Editor with powerful image editing tools.
You can use it to view your photographs and improve them.

%files -n showfoto -f showfoto.lang
%{_kde_bindir}/showfoto
%{_kde_datadir}/applications/kde4/showfoto.desktop
%{_kde_appsdir}/showfoto
%{_kde_iconsdir}/*/*/apps/showfoto.*

#-----------------------------------------------------------------------

%define libdigikamdatabase_major 2
%define libdigikamdatabase %mklibname digikamdatabase %{libdigikamdatabase_major}

%package -n %{libdigikamdatabase}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libdigikamdatabase}
Librairie File needed by %{name}

%files -n %{libdigikamdatabase}
%{_kde_libdir}/libdigikamdatabase.so.%{libdigikamdatabase_major}*

#-----------------------------------------------------------------------

%define libdigikamcore_major 2
%define libdigikamcore %mklibname digikamcore %{libdigikamcore_major}

%package -n %{libdigikamcore}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libdigikamcore}
Librairie File needed by %{name}

%files -n %{libdigikamcore}
%{_kde_libdir}/libdigikamcore.so.%{libdigikamcore_major}*

#-----------------------------------------------------------------------

%define libkface_major 1
%define libkface %mklibname kface %{libkface_major}

%package -n %{libkface}
Summary:	Runtime library for %{name}
Group:		System/Libraries
URL:		https://projects.kde.org/projects/extragear/libs/libkface

%description -n %{libkface}
Librairie File needed by %{name}

Libkface is a Qt/C++ wrapper around LibFace library to perform face recognition 
and detection over pictures.

%files -n %{libkface}
%{_kde_libdir}/libkface.so.%{libkface_major}*

#-----------------------------------------------------------------------

%define libkgeomap_major 1
%define libkgeomap %mklibname kgeomap %{libkgeomap_major}
%define libkmap %mklibname kmap 1

%package -n %{libkgeomap}
Summary:	Runtime library for %{name}
Group:		System/Libraries
URL:		https://projects.kde.org/projects/extragear/libs/libkgeomap
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
URL:		https://projects.kde.org/projects/extragear/libs/libmediawiki

%description -n %{libmediawiki}
Librairie File needed by %{name}

libmediawiki is a KDE C++ interface for MediaWiki based
web service as wikipedia.org.

%files -n %{libmediawiki}
%{_kde_libdir}/libmediawiki.so.%{libmediawiki_major}*

#-----------------------------------------------------------------------

%define libkipiplugins_major 2
%define libkipiplugins %mklibname kipiplugins %{libkipiplugins_major}

%package -n %{libkipiplugins}
Summary:	Runtime library for %{name}
Group:		System/Libraries

%description -n %{libkipiplugins}
Librairie File needed by %{name}

%files -n %{libkipiplugins}
%{_kde_libdir}/libkipiplugins.so.%{libkipiplugins_major}*

#-----------------------------------------------------------------------

%package -n kipi-plugins
Summary:	KDE image Interface Plugins
Group:		System/Libraries
URL:		https://projects.kde.org/projects/extragear/graphics/kipi-plugins
BuildArch:	noarch
Suggests:	kipi-plugins-timeadjust
Suggests:	kipi-plugins-smug
Suggests:	kipi-plugins-shwup
Suggests:	kipi-plugins-piwigoexport
Suggests:	kipi-plugins-picasa
Suggests:	kipi-plugins-metadataedit
Suggests:	kipi-plugins-kopete
Suggests:	kipi-plugins-kioexportimport
Suggests:	kipi-plugins-jpeglossless
Suggests:	kipi-plugins-ipodexport
Suggests:	kipi-plugins-imageviewer
Suggests:	kipi-plugins-htmlexport
Suggests:	kipi-plugins-debianscreenshot
Suggests:	kipi-plugins-gpssync
Suggests:	kipi-plugins-flickr
Suggests:	kipi-plugins-expoblending
Suggests:	kipi-plugins-calendar
Suggests:	kipi-plugins-batchprocess
Suggests:	kipi-plugins-advancedslideshow
Suggests:	kipi-plugins-printimages
Suggests:	kipi-plugins-dngconverter
Suggests:	kipi-plugins-galleryexport
Suggests:	kipi-plugins-flashexport
Suggests:	kipi-plugins-facebook
Suggests:	kipi-plugins-acquireimages
Suggests:	kipi-plugins-rawconverter
Suggests:	kipi-plugins-removeredeyes
Suggests:	kipi-plugins-sendimages
Suggests:	kipi-plugins-youtube
Suggests:	kipi-plugins-kmlexport
Suggests:	kipi-plugins-yandexfotki
Suggests:	kipi-plugins-rajceexport
Suggests:	kipi-plugins-panorama
Suggests:	kipi-plugins-vkontakte

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

%package -n kipi-plugins-timeadjust
Summary:	Time Adjust kipi plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-timeadjust
A Tool to adjust time and date.

%files -n kipi-plugins-timeadjust -f kipiplugin_timeadjust.lang
%{_kde_libdir}/kde4/kipiplugin_timeadjust.so
%{_kde_iconsdir}/hicolor/*/actions/timeadjust.png
%{_kde_services}/kipiplugin_timeadjust.desktop

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
%{_kde_libdir}/kde4/kipiplugin_smug.so
%{_kde_iconsdir}/hicolor/*/actions/smugmug.png
%{_kde_iconsdir}/hicolor/scalable/actions/smugmug.svgz
%{_kde_services}/kipiplugin_smug.desktop

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
%{_kde_libdir}/kde4/kipiplugin_shwup.so
%{_kde_iconsdir}/hicolor/*/actions/shwup.png
%{_kde_services}/kipiplugin_shwup.desktop

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
%{_kde_libdir}/kde4/kipiplugin_piwigoexport.so
%{_kde_appsdir}/kipiplugin_piwigoexport
%{_kde_services}/kipiplugin_piwigoexport.desktop
%{_kde_iconsdir}/hicolor/scalable/actions/piwigo.svgz
%{_kde_iconsdir}/hicolor/*/actions/piwigo.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-picasa
Summary:	Picasa Kipi Plugins
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-picasa
A tool to export images to a remote Picase Web Service

%files -n kipi-plugins-picasa -f kipiplugin_picasawebexport.lang
%{_kde_libdir}/kde4/kipiplugin_picasawebexport.so
%{_kde_services}/kipiplugin_picasawebexport.desktop
%{_kde_iconsdir}/hicolor/scalable/actions/picasa.svgz
%{_kde_iconsdir}/hicolor/*/actions/picasa.png

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
%{_kde_libdir}/kde4/kipiplugin_metadataedit.so
%{_kde_services}/kipiplugin_metadataedit.desktop
%{_kde_iconsdir}/hicolor/*/actions/metadataedit.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-kopete
Summary:	Kopete kipi plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-kopete
A tool to export images to an instant messaging contact.

%files -n kipi-plugins-kopete 
%{_kde_libdir}/kde4/kipiplugin_kopete.so
%{_kde_services}/kipiplugin_kopete.desktop

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
%{_kde_libdir}/kde4/kipiplugin_jpeglossless.so
%{_kde_services}/kipiplugin_jpeglossless.desktop
%{_kde_iconsdir}/hicolor/*/actions/flip-horizontal.png
%{_kde_iconsdir}/hicolor/*/actions/grayscaleconvert.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-ipodexport
Summary:	Ipod Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-ipodexport
A tool to export pictures to an Ipod device.

%files -n kipi-plugins-ipodexport -f kipiplugin_ipodexport.lang
%{_kde_libdir}/kde4/kipiplugin_ipodexport.so
%{_kde_services}/kipiplugin_ipodexport.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-imgurexport
Summary:	Imgur Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-imgurexport
A tool to export pictures to Imgur.

%files -n kipi-plugins-imgurexport 
%{_kde_libdir}/kde4/kipiplugin_imgurexport.so
%{_kde_iconsdir}/hicolor/*/actions/imgur.*
%{_kde_services}/kipiplugin_imgurexport.desktop

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
%{_kde_libdir}/kde4/kipiplugin_imageviewer.so
%{_kde_appsdir}/kipiplugin_imageviewer
%{_kde_services}/kipiplugin_imageviewer.desktop
%{_kde_iconsdir}/hicolor/*/actions/ogl.png 

#-----------------------------------------------------------------------

%package -n kipi-plugins-htmlexport
Summary:	Html Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-htmlexport
A tool to export images collections into a static XHTML page.

%files -n kipi-plugins-htmlexport -f kipiplugin_htmlexport.lang
%{_kde_libdir}/kde4/kipiplugin_htmlexport.so
%{_kde_services}/kipiplugin_htmlexport.desktop
%{_kde_appsdir}/kipiplugin_htmlexport

#-----------------------------------------------------------------------

%package -n kipi-plugins-debianscreenshot
Summary:	Debian Screenshot kipi plugins
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-debianscreenshot
A tool to export images to the Debian Screenshots site.

%files -n kipi-plugins-debianscreenshot 
%{_kde_libdir}/kde4/kipiplugin_debianscreenshots.so 
%{_kde_services}/kipiplugin_debianscreenshots.desktop
%{_kde_iconsdir}/hicolor/*/actions/debianscreenshots.png 
%{_kde_iconsdir}/hicolor/scalable/actions/debianscreenshots.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-gpssync
Summary:	GPS Sync Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-gpssync
A tool to geolocalize pictures.

%files -n kipi-plugins-gpssync -f kipiplugin_gpssync.lang
%{_kde_appsdir}/gpssync
%{_kde_libdir}/kde4/kipiplugin_gpssync.so
%{_kde_services}/kipiplugin_gpssync.desktop
%{_kde_iconsdir}/hicolor/*/actions/gpsimagetag.png

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
%{_kde_libdir}/kde4/kipiplugin_flickrexport.so
%{_kde_services}/kipiplugin_flickrexport.desktop
%{_kde_iconsdir}/hicolor/*/actions/flickr.png
%{_kde_iconsdir}/hicolor/*/actions/hq.png 
%{_kde_iconsdir}/hicolor/*/actions/zooomr.png
%{_kde_iconsdir}/hicolor/scalable/actions/flickr.svgz
%{_kde_iconsdir}/hicolor/scalable/actions/hq.svgz 
%{_kde_iconsdir}/hicolor/scalable/actions/zooomr.svgz 

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
%{_kde_bindir}/expoblending
%{_kde_applicationsdir}/expoblending.desktop
%{_kde_libdir}/kde4/kipiplugin_expoblending.so
%{_kde_appsdir}/kipiplugin_expoblending 
%{_kde_services}/kipiplugin_expoblending.desktop
%{_kde_iconsdir}/hicolor/*/actions/expoblending.png

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
%{_kde_libdir}/kde4/kipiplugin_calendar.so
%{_kde_services}/kipiplugin_calendar.desktop

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

%package -n kipi-plugins-advancedslideshow
Summary:	Advanced Slideshow Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-advancedslideshow
A tool to slide images with 2D and 3D effects using OpenGL.

%files -n kipi-plugins-advancedslideshow -f kipiplugin_advancedslideshow.lang
%{_kde_libdir}/kde4/kipiplugin_advancedslideshow.so
%{_kde_iconsdir}/hicolor/*/actions/slideshow.png
%{_kde_services}/kipiplugin_advancedslideshow.desktop

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
%{_kde_libdir}/kde4/kipiplugin_printimages.so
%{_kde_services}/kipiplugin_printimages.desktop
%{_kde_appsdir}/kipiplugin_printimages/

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
%{_kde_bindir}/dngconverter
%{_kde_bindir}/dnginfo
%{_kde_applicationsdir}/dngconverter.desktop
%{_kde_libdir}/kde4/kipiplugin_dngconverter.so
%{_kde_services}/kipiplugin_dngconverter.desktop
%{_kde_iconsdir}/*/*/*/dngconverter.*

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
%{_kde_libdir}/kde4/kipiplugin_galleryexport.so
%{_kde_appsdir}/kipiplugin_galleryexport
%{_kde_services}/kipiplugin_galleryexport.desktop
%{_kde_iconsdir}/hicolor/*/actions/gallery.png
%{_kde_iconsdir}/hicolor/scalable/actions/gallery.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-wikimedia
Summary:	Wikimedia Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-wikimedia
A tool to export images to a remote MediaWiki site

%files -n kipi-plugins-wikimedia
%{_kde_libdir}/kde4/kipiplugin_wikimedia.so
%{_kde_services}/kipiplugin_wikimedia.desktop
%{_kde_iconsdir}/*/*/*/wikimedia.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-imageshack
Summary:	Imageshack Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-imageshack
A tool to export images to ImageShack

%files -n kipi-plugins-imageshack
%{_kde_libdir}/kde4/kipiplugin_imageshackexport.so
%{_kde_services}/kipiplugin_imageshackexport.desktop
%{_kde_iconsdir}/*/*/*/imageshack.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-flashexport
Summary:	Flash export kipi-plugins
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-flashexport
A tool to export images to Flash.

%files -n kipi-plugins-flashexport -f kipiplugin_flashexport.lang
%{_kde_libdir}/kde4/kipiplugin_flashexport.so
%{_kde_appsdir}/kipiplugin_flashexport
%{_kde_services}/kipiplugin_flashexport.desktop
%{_kde_iconsdir}/hicolor/*/actions/flash.png
%{_kde_iconsdir}/hicolor/scalable/actions/flash.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-facebook
Summary:	Facebook kipi plugins
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-facebook
A tool to import/export images to/from a remote Facebook web service.

%files -n kipi-plugins-facebook -f kipiplugin_facebook.lang
%{_kde_libdir}/kde4/kipiplugin_facebook.so
%{_kde_services}/kipiplugin_facebook.desktop
%{_kde_iconsdir}/hicolor/*/actions/facebook.png
%{_kde_iconsdir}/hicolor/scalable/actions/facebook.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-acquireimages
Summary:	Acquireimages
Group:		System/Libraries
Requires:	kipi-common
Conflicts:	kipi-plugins < 1:1.8.0-1

%description -n kipi-plugins-acquireimages
A tool to acquire images using flat scanner.

%files -n kipi-plugins-acquireimages -f kipiplugin_acquireimages.lang
%{_kde_bindir}/scangui
%{_kde_libdir}/kde4/kipiplugin_acquireimages.so
%{_kde_services}/kipiplugin_acquireimages.desktop 
%{_kde_applicationsdir}/scangui.desktop 

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
%{_kde_libdir}/kde4/kipiplugin_sendimages.so 
%{_kde_services}/kipiplugin_sendimages.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-kmlexport
Summary:	Create KML files to present images with coordinates
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-kmlexport 
A plugin to create KML files to present images with coordinates.

%files -n kipi-plugins-kmlexport 
%{_kde_libdir}/kde4/kipiplugin_kmlexport.so
%{_kde_services}/kipiplugin_kmlexport.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-yandexfotki
Summary:	Yandex.Fotki Exporter
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-yandexfotki
A tool to export images to a remote Yandex.Fotki web service.

%files -n kipi-plugins-yandexfotki 
%{_kde_libdir}/kde4/kipiplugin_yandexfotki.so
%{_kde_services}/kipiplugin_yandexfotki.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-rajceexport
Summary:	Rajce.net Exporter
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-rajceexport
A tool to export images to a remote rajce.net service.

%files -n kipi-plugins-rajceexport 
%{_kde_libdir}/kde4/kipiplugin_rajceexport.so
%{_kde_services}/kipiplugin_rajceexport.desktop
%{_kde_iconsdir}/hicolor/*/actions/rajce.png


#-----------------------------------------------------------------------
%package -n kipiplugin-photolayouts-editor
Summary:	Photo Layouts Editor
Group:		System/Libraries
Requires:	kipi-common

%description -n kipiplugin-photolayouts-editor
Photo Layouts Editor.

%files -n kipiplugin-photolayouts-editor
%{_kde_bindir}/photolayoutseditor
%{_kde_iconsdir}/hicolor/*/apps/photolayoutseditor.png
%{_kde_services}/kipiplugin_photolayoutseditor.desktop
%{_kde_datadir}/kde4/servicetypes/photolayoutseditorborderplugin.desktop
%{_kde_datadir}/kde4/servicetypes/photolayoutseditoreffectplugin.desktop
%{_kde_datadir}/templates/kipiplugins_photolayoutseditor
%{_kde_libdir}/kde4/kipiplugin_photolayoutseditor.so
%{_kde_applicationsdir}/photolayoutseditor.desktop
%{_kde_appsdir}/photolayoutseditor
%{_kde_datadir}/config.kcfg/PLEConfigSkeleton.kcfgc

#-----------------------------------------------------------------------

%package -n kipi-plugins-panorama
Summary:	Panorama tools
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common
Requires:	hugin

%description -n kipi-plugins-panorama
A tool to create panorama.

%files -n kipi-plugins-panorama 
%{_kde_bindir}/panoramagui
%{_kde_libdir}/kde4/kipiplugin_panorama.so
%{_kde_appsdir}/kipiplugin_panorama/
%{_kde_services}/kipiplugin_panorama.desktop 
%{_kde_applicationsdir}/panoramagui.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-vkontakte
Summary:	VKontakte.ru Exporter
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-vkontakte
A tool to export on VKontakte.ru Web service

%files -n kipi-plugins-vkontakte 
%{_kde_libdir}/kde4/kipiplugin_vkontakte.so
%{_kde_services}/kipiplugin_vkontakte.desktop

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
%{_includedir}/libmediawiki
%{_kde_libdir}/libmediawiki.so
%{_kde_libdir}/pkgconfig/libmediawiki.pc
%{_kde_appsdir}/cmake/modules/FindMediawiki.cmake

#-----------------------------------------------------------------------

%define libkface_devel %mklibname -d kface

%package -n  %{libkface_devel}
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
%{_includedir}/libkface
%{_kde_libdir}/libkface.so
%{_kde_libdir}/pkgconfig/libkface.pc
%{_kde_appsdir}/cmake/modules/FindKface.cmake

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
%{_includedir}/libkgeomap
%{_kde_libdir}/libkgeomap.so
%{_kde_libdir}/pkgconfig/libkgeomap.pc
%{_kde_appsdir}/cmake/modules/FindKGeoMap.cmake

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
%{_kde_libdir}/libPropertyBrowser.a
#-----------------------------------------------------------------------

%prep
# Unpack correct files & reemove wrong png/svgz  (kde #286034) this part should be removed for next digikam version
%if "%{beta}" == ""
%setup -q -a 1
%else
%setup -q -n %{name}-software-compilation-%{version}-%{beta} -a 1
%endif
find . -name ox*-app-showfoto.* -exec rm -rf '{}' \;
find . -name ox*-app-digikam.* -exec rm -rf '{}' \;

%apply_patches

# Remove wallpaper po files (kipiplugin-wallpaper is not build )
pushd po
find  . -name kipiplugin_wallpaper.po -exec rm -rf '{}' \;

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html || touch %{name}.lang
%find_lang showfoto --with-html || touch showfoto.lang
%find_lang kipi-plugins kipiplugins kipi-plugins.lang --with-html || touch kipi-plugins.lang

%find_lang kipiplugin_rawconverter || touch kipiplugin_rawconverter.lang
%find_lang kipiplugin_sendimages || touch kipiplugin_sendimages.lang
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
%find_lang kipiplugin_picasawebexport || touch kipiplugin_picasawebexport.lang
%find_lang kipiplugin_piwigoexport || touch kipiplugin_piwigoexport.lang
%find_lang kipiplugin_printimages || touch kipiplugin_printimages.lang
%find_lang kipiplugin_rawconverter || touch kipiplugin_rawconverter.lang
%find_lang kipiplugin_removeredeyes || touch kipiplugin_removeredeyes.lang
%find_lang kipiplugin_sendimages || touch kipiplugin_sendimages.lang
%find_lang kipiplugin_shwup || touch kipiplugin_shwup.lang
%find_lang kipiplugin_timeadjust || touch kipiplugin_timeadjust.lang
%find_lang kipiplugin_acquireimages || touch kipiplugin_acquireimages.lang
%find_lang kipiplugin_advancedslideshow || touch kipiplugin_advancedslideshow.lang
%find_lang kipiplugin_batchprocessimages || touch kipiplugin_batchprocessimages.lang
%find_lang kipiplugin_smug || touch kipiplugin_smug.lang
%find_lang libkgeomap || touch libkgeomap.lang


%changelog
* Sat Aug 18 2012 Crispin Boylan <crisb@mandriva.org> 2:2.8.0-1
+ Revision: 815328
- New release

* Sun Jul 22 2012 Crispin Boylan <crisb@mandriva.org> 2:2.7.0-2
+ Revision: 810566
- Rebuild

* Mon Jul 09 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2:2.7.0-1
+ Revision: 808636
- Update to 2.7.0

* Thu Jun 07 2012 Crispin Boylan <crisb@mandriva.org> 2:2.6.0-2
+ Revision: 803171
- Rebuild for opencv

* Tue Jun 05 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:2.6.0-1
+ Revision: 802764
- 2.6.0 final
- Fix some rpmlint errors

* Sat May 19 2012 Crispin Boylan <crisb@mandriva.org> 1:2.6.0-0.rc.3
+ Revision: 799722
- Patch 2 to fix kde bug #295263 with editing metadata

* Fri May 11 2012 Andrey Bondrov <abondrov@mandriva.org> 1:2.6.0-0.rc.2
+ Revision: 798202
- Fix typo for kipi-plugins-metadataedit suggest and apply some spec cosmetics

* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 1:2.6.0-0.rc.1
+ Revision: 797799
- Update to rc

* Wed May 09 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:2.6.0-0.beta3.1
+ Revision: 797654
- Update to 2.6.0-beta3

* Fri Jan 06 2012 Crispin Boylan <crisb@mandriva.org> 1:2.5.0-2
+ Revision: 758021
- Use proper version of patch2 from digikam commit

* Thu Jan 05 2012 Crispin Boylan <crisb@mandriva.org> 1:2.5.0-1
+ Revision: 757943
- Package new lang files
- No kvkontakte lang files
- Patch2: Fix compile on kipi with kde 4.8
- New release, add patches for boost 1.4.8 and kipi used in kde 4.8

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against libtiff.so.5

  + Zé <ze@mandriva.org>
    - 2.4.1
    - use bcond
    - clean provides that already exist by default
    - update patch0
    - clean patch1 (fixed upstream)

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Enable external libvkontake
    - Do not build yet with external libkvkontakte
    - Start to update to digikam 2.3.0

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-2
+ Revision: 663777
- mass rebuild

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 1.9.0-1
+ Revision: 640705
- update to new version 1.9.0

* Mon Jan 24 2011 Funda Wang <fwang@mandriva.org> 1.8.0-1
+ Revision: 632473
- update to new version 1.8.0

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add warning about digikam 2

* Sun Dec 19 2010 Funda Wang <fwang@mandriva.org> 1.7.0-1mdv2011.0
+ Revision: 623157
- new version 1.7.0

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Use kde layout

* Tue Nov 23 2010 Buchan Milne <bgmilne@mandriva.org> 1.6.0-1mdv2011.0
+ Revision: 599940
- update to new version 1.6.0
- Tighten up library dependencies

* Mon Oct 11 2010 Funda Wang <fwang@mandriva.org> 1.5.0-1mdv2011.0
+ Revision: 584881
- new version 1.5.0

  + Buchan Milne <bgmilne@mandriva.org>
    - Use fix from svn that should not break other Canon cameras

* Tue Sep 21 2010 Buchan Milne <bgmilne@mandriva.org> 1.4.0-4mdv2011.0
+ Revision: 580395
- Fix lens auto-correction to use LensType tag on Canon, instead of Lens tag - KDE bug #251920

* Sat Sep 18 2010 Funda Wang <fwang@mandriva.org> 1.4.0-3mdv2011.0
+ Revision: 579317
- rebuild for new libkipi

* Thu Sep 02 2010 Funda Wang <fwang@mandriva.org> 1.4.0-2mdv2011.0
+ Revision: 575184
- rebuild for new kdeedu

* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 1.4.0-1mdv2011.0
+ Revision: 571990
- new version 1.4.0

* Sat Jul 31 2010 John Balcaen <mikala@mandriva.org> 1.3.0-2mdv2011.0
+ Revision: 563834
- Rebuild for kde 4.5 (new marble...)

* Sun Jun 27 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.3.0-1mdv2010.1
+ Revision: 549234
- Fix (Build)Requires
- Fix MySQL (Build)Requires
- Fix Requires/BuildRequires
- Add buildrequires
- Update to version 1.3.0

* Fri May 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.2.0-4mdv2010.1
+ Revision: 546514
- Update french translation

* Tue Apr 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.2.0-3mdv2010.1
+ Revision: 532010
- Rebuild against new libkdcraw

* Thu Apr 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.2.0-2mdv2010.1
+ Revision: 530657
- Fix a bug in the cmakefile ( BKO: 232875
- Add patch to fix crash

* Mon Mar 29 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.2.0-1mdv2010.1
+ Revision: 528657
- Update to 1.2.0

* Sun Jan 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 498784
- Update to digikam 1.1.0

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2010.1
+ Revision: 488745
- rebuilt against libjpeg v8

* Mon Dec 21 2009 Angelo Naselli <anaselli@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 480779
- removed old shofoto.desktop patch

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to digikam 1.0.0 final

* Mon Nov 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-0.7.1mdv2010.1
+ Revision: 471716
- Update to 1.0.0 Rc

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-0.6.2mdv2010.1
+ Revision: 465207
- Rebuild against new Qt

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 1.0.0-0.6.1mdv2010.1
+ Revision: 463499
- new version beta6

* Mon Nov 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-0.5.3mdv2010.1
+ Revision: 463383
- Rebuild against new kde 4

* Sun Oct 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-0.5.2mdv2010.0
+ Revision: 456686
- Add marble-common as a Requires in showfoto

* Tue Oct 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-0.5.1mdv2010.0
+ Revision: 454584
- Fix file list
- Update to beta5

* Mon Aug 31 2009 Helio Chissini de Castro <helio@mandriva.com> 1.0.0-0.4.1mdv2010.0
+ Revision: 423029
- Fix upgrade using numbers instead of letters
- New upstream version beta4

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-0.beta3.2mdv2010.0
+ Revision: 416610
- rebuilt against libjpeg v7

* Fri Jul 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-0.beta3.1mdv2010.0
+ Revision: 399526
- Remove merged patches
- Update to beta3

* Thu Jul 09 2009 Helio Chissini de Castro <helio@mandriva.com> 1.0.0-0.beta2.3mdv2010.0
+ Revision: 393960
- Fix mandriva bug 52073

* Thu Jul 09 2009 Helio Chissini de Castro <helio@mandriva.com> 1.0.0-0.beta2.2mdv2010.0
+ Revision: 393908
- Enable liquid rescale

* Mon Jul 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-0.beta2.1mdv2010.0
+ Revision: 392708
- Fix build
- Update to digikam 1.0.0-beta2

* Mon Jun 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-0.beta1.1mdv2010.0
+ Revision: 383855
- Update to 1.0.0 Beta1

* Wed Apr 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-6mdv2009.1
+ Revision: 367583
- Add a require on marble-common

* Tue Apr 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-5mdv2009.1
+ Revision: 367239
- Split showfoto on its own package to avoid useless on default install
- Remove old macros
- Digikam does not need marble, only marble libs

* Thu Apr 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-3mdv2009.1
+ Revision: 365357
- Add kipi-plugins as requires

* Mon Mar 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-2mdv2009.1
+ Revision: 356259
- New version 0.10 final

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-1.rc2.3mdv2009.1
+ Revision: 340820
- Update to Rc2

* Fri Jan 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-1.rc1.3mdv2009.1
+ Revision: 333096
- Update to Rc1
- Revert commit 331703, digikam requires kdebase4-runtime which Requires oxygen-icon-theme
  so this requires is useless.

  + Bruno Cornec <bcornec@mandriva.org>
    - Tag 3: Adds a dependency on oxygen-icon-theme as digikam 0.10 doesn't work correctly without it in KDE 4 (after upgrading from 0.9 and KDE 3.5)

* Tue Jan 13 2009 Funda Wang <fwang@mandriva.org> 0.10.0-1.beta8.2mdv2009.1
+ Revision: 328978
- digikam.desktop is already translated
- fix file list
- fix linkage

  + Emmanuel Blindauer <blindauer@mandriva.org>
    - rebuild for latest kdelibs

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to beta8

* Fri Dec 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-1.beta7.1mdv2009.1
+ Revision: 316353
- Update to beta7

* Sun Dec 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-1.beta6.4mdv2009.1
+ Revision: 314392
- Sync with trunk

* Fri Nov 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-1.beta6.3mdv2009.1
+ Revision: 307511
- Update to latest beta6
  Add new libdigikamcore libs
  Remove libdigikam lib

* Sun Nov 23 2008 Funda Wang <fwang@mandriva.org> 0.10.0-1.beta5.3mdv2009.1
+ Revision: 305980
- rebuild for new libkipi

* Sat Nov 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-1.beta5.2mdv2009.1
+ Revision: 303390
- Remove duplicate files

* Wed Nov 05 2008 Angelo Naselli <anaselli@mandriva.org> 0.10.0-1.beta5.1mdv2009.1
+ Revision: 299963
- new version 0.10.0 beta5

* Sun Oct 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-1.beta4.1mdv2009.1
+ Revision: 297477
- Update to digikam 0.10.0 beta4

* Mon Sep 29 2008 Helio Chissini de Castro <helio@mandriva.com> 0.10.0-1.beta3.2mdv2009.0
+ Revision: 289701
- Updated desktop file as requested by translation team

* Thu Sep 11 2008 Angelo Naselli <anaselli@mandriva.org> 0.10.0-1.beta3.1mdv2009.0
+ Revision: 283824
- new version 0.10.0 beta3

* Mon Aug 04 2008 Angelo Naselli <anaselli@mandriva.org> 0.10.0-1.beta2.1mdv2009.0
+ Revision: 263076
- new version 0.10.0 beta2

* Mon Jul 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-0.838532.1mdv2009.0
+ Revision: 251744
- New shapshot

* Tue Jun 24 2008 Helio Chissini de Castro <helio@mandriva.com> 0.10.0-0.824037.2mdv2009.0
+ Revision: 228792
- Update from svn
- Added requries for new liblens
- Up to date digikam form svn

  + Colin Guthrie <cguthrie@mandriva.org>
    - Update snapshot
    - Update BuildRequires now that kdcraw, kipi and kexiv2 are part of kdegraphics4
    - Fix the Require on qt4-sqlite plugin (update needed in qt4 to fix properly)
    - Tidy up %%post/%%postun scripts
    - Work around GCC 4.3.1 bug

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix Requires ( Reported on cooker Mailing List)

* Tue May 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-0.809821.4mdv2009.0
+ Revision: 209317
- Fix conflicts against oxygen-icon-theme

* Mon May 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-0.809821.3mdv2009.0
+ Revision: 209188
- Add kdeedu4-devel as BuildRequire

* Mon May 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-0.809821.2mdv2009.0
+ Revision: 209170
- Fix tarball
- Fix FileList
- New snapshot
- Fix spec file with new name
- Use kde4 apps by default
- Fix BuildRequires

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description

* Fri Dec 28 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-0.753592.1mdv2008.1
+ Revision: 138817
- Add buildrequire (liblcms-devel)
- Fix pkgconfig dir
- import kde4-digikam

