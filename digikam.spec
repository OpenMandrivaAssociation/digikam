%bcond_without external_kvkontakte

Name:          digikam
Summary:       A KDE photo management utility
Group:         Graphics
Version:       2.5.0
Release:       1
Epoch:         1
License:       GPLv2+ 
URL:           http://www.digikam.org
Source0:       http://downloads.sourceforge.net/digikam/%{name}-%{version}.tar.bz2
Source1:       digikam-correct-pngfilesfor-apps.xz
%if %{with external_kvkontakte}
Patch0:        digikam-2.4.1-use-external-libvkontake.patch 
%endif
Patch1:	       digikam-2.5.0-boost-1.48.patch
Patch2:	       digikam-2.5.0-kipi-4.7.patch

BuildRequires: kdepimlibs4-devel
BuildRequires: pkgconfig(libkexiv2)
BuildRequires: pkgconfig(libksane)
BuildRequires: pkgconfig(libkdcraw)
BuildRequires: pkgconfig(libkipi)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libgphoto2)
BuildRequires: pkgconfig(opencv)
BuildRequires: pkgconfig(lcms)
BuildRequires: pkgconfig(lensfun)
BuildRequires: pkgconfig(lqr-1) >= 0.4.0
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(libgpod-1.0)
#BuildRequires: pkgconfig(libpgf)
%if %{with external_kvkontakte}
BuildRequires: libkvkontakte-devel
%endif 
BuildRequires: libtiff-devel
BuildRequires: libjasper-devel
BuildRequires: marble-devel
BuildRequires: libgomp-devel
BuildRequires: doxygen
BuildRequires: mysql-core
BuildRequires: mysql-common

Requires:      mysql-core
Requires:      mysql-common
Requires:      kdebase4-runtime
Requires:      qt4-database-plugin-sqlite
Requires:      kipi-plugins
Requires:      libkface-common
Requires:      libkgeomap-common
Requires:      libkdcraw-common
Requires:      kipi-common

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
%doc core/AUTHORS core/ChangeLog core/COPYING core/COPYING.LIB core/COPYING.DOC core/NEWS core/README core/TODO  core/README.FACE core/TODO.FACE core/TODO.MYSQLPORT
%_kde_bindir/digikam
%_kde_bindir/digitaglinktree
%_kde_bindir/cleanup_digikamdb
%_kde_bindir/libkgeomap_demo
%_kde_libdir/kde4/digikam*.so
%_kde_libdir/kde4/kio_digikam*.so
%_kde_appsdir/digikam
%_kde_appsdir/solid/actions/digikam*.desktop
%_kde_applicationsdir/digikam.desktop
%_kde_services/digikam*.desktop
%_kde_services/digikam*.protocol
%_kde_servicetypes/digikam*.desktop
%_kde_mandir/man1/digitaglinktree.1*
%_kde_mandir/man1/cleanup_digikamdb.1*
%_kde_iconsdir/*/*/apps/digikam.*
%_kde_libdir/kde4/libexec/digikamdatabaseserver

#-----------------------------------------------------------------------

%package -n libkface-common
Summary:     Common files for libkface library
Group:       Graphics
URL:         https://projects.kde.org/projects/extragear/libs/libkface
BuildArch:   noarch
Conflicts:   %name < 1:2.0.0-0.rc1.2
%description -n libkface-common
Common files for libkface library.

Libkface is a Qt/C++ wrapper around LibFace library to perform face recognition 
and detection over pictures.


%files -n libkface-common
%doc extra/libkface/README extra/libkface/NEWS extra/libkface/AUTHORS extra/libkface/COPYING
%_kde_appsdir/libkface

#-----------------------------------------------------------------------

%package -n libkgeomap-common
Summary:    Common files for libkgeomap library
Group:      Graphics
URL:        https://projects.kde.org/projects/extragear/libs/libkgeomap
BuildArch:  noarch
Conflicts: %name < 1:2.0.0-0.rc1.2

%description -n libkgeomap-common
Common files for libkgeomap library

Libkgeomap is a wrapper around world map components as Marble, OpenstreetMap and
GoogleMap,for browsing and arranging photos on a map.

%files -n libkgeomap-common -f libkgeomap.lang
%doc extra/libkgeomap/README extra/libkgeomap/AUTHORS
%_kde_appsdir/libkgeomap

#-----------------------------------------------------------------------

%package -n     showfoto
Summary:        Fast Image Editor
Group:          Graphics
Requires:       libkdcraw-common

%description -n showfoto
Showfoto is a fast Image Editor with powerful image editing tools.
You can use it to view your photographs and improve them.

%files -n showfoto -f showfoto.lang
%_kde_bindir/showfoto
%_kde_datadir/applications/kde4/showfoto.desktop
%_kde_appsdir/showfoto
%_kde_iconsdir/*/*/apps/showfoto.*

#-----------------------------------------------------------------------

%define libdigikamdatabase_major 2
%define libdigikamdatabase %mklibname digikamdatabase %libdigikamdatabase_major

%package -n %libdigikamdatabase
Summary: Runtime library for %{name}
Group: System/Libraries

%description -n %libdigikamdatabase
Librairie File needed by %name

%files -n %libdigikamdatabase
%_kde_libdir/libdigikamdatabase.so.%{libdigikamdatabase_major}*

#-----------------------------------------------------------------------

%define libdigikamcore_major 2
%define libdigikamcore %mklibname digikamcore %libdigikamcore_major

%package -n %libdigikamcore
Summary: Runtime library for %{name}
Group: System/Libraries

%description -n %libdigikamcore
Librairie File needed by %name

%files -n %libdigikamcore
%_kde_libdir/libdigikamcore.so.%{libdigikamcore_major}*

#-----------------------------------------------------------------------

%define libkface_major 1
%define libkface %mklibname kface %libkface_major

%package -n %libkface
Summary: Runtime library for %{name}
Group: System/Libraries
URL:   https://projects.kde.org/projects/extragear/libs/libkface
%description -n %libkface
Librairie File needed by %name

Libkface is a Qt/C++ wrapper around LibFace library to perform face recognition 
and detection over pictures.

%files -n %libkface
%_kde_libdir/libkface.so.%{libkface_major}*

#-----------------------------------------------------------------------

%define libkgeomap_major 1
%define libkgeomap %mklibname kgeomap %libkgeomap_major
%define libkmap %mklibname kmap 1

%package -n %libkgeomap
Summary: Runtime library for %{name}
Group: System/Libraries
URL:   https://projects.kde.org/projects/extragear/libs/libkgeomap
Obsoletes: %libkmap < 1:2.0.0-0.rc1.2

%description -n %libkgeomap
Librairie File needed by %name

Libkgeomap is a wrapper around world map components as Marble, OpenstreetMap and
GoogleMap,for browsing and arranging photos on a map.

%files -n %libkgeomap
%_kde_libdir/libkgeomap.so.%{libkgeomap_major}*

#-----------------------------------------------------------------------

%define libmediawiki_major 1
%define libmediawiki %mklibname mediawiki %libmediawiki_major

%package -n %libmediawiki
Summary:    Runtime library for %{name}
Group:      System/Libraries
URL:        https://projects.kde.org/projects/extragear/libs/libmediawiki

%description -n %libmediawiki
Librairie File needed by %name

libmediawiki is a KDE C++ interface for MediaWiki based web service as wikipedia.org.

%files -n %libmediawiki
%_kde_libdir/libmediawiki.so.%{libmediawiki_major}*

#-----------------------------------------------------------------------

%define libkipiplugins_major 2
%define libkipiplugins %mklibname kipiplugins %libkipiplugins_major

%package -n %libkipiplugins
Summary:    Runtime library for %{name}
Group:      System/Libraries

%description -n %libkipiplugins
Librairie File needed by %name

%files -n %libkipiplugins
%_kde_libdir/libkipiplugins.so.%{libkipiplugins_major}*

#-----------------------------------------------------------------------

%package -n kipi-plugins
Summary:    KDE image Interface Plugins
Group:      System/Libraries
URL:        https://projects.kde.org/projects/extragear/graphics/kipi-plugins
BuildArch:  noarch
Suggests:   kipi-plugins-timeadjust
Suggests:   kipi-plugins-smug
Suggests:   kipi-plugins-shwup
Suggests:   kipi-plugins-piwigoexport
Suggests:   kipi-plugins-picasa
Suggests:   kipi-plugins-metadaedit
Suggests:   kipi-plugins-kopete
Suggests:   kipi-plugins-kioexportimport
Suggests:   kipi-plugins-jpeglossless
Suggests:   kipi-plugins-ipodexport
Suggests:   kipi-plugins-imageviewer
Suggests:   kipi-plugins-htmlexport
Suggests:   kipi-plugins-debianscreenshot
Suggests:   kipi-plugins-gpssync
Suggests:   kipi-plugins-flickr
Suggests:   kipi-plugins-expoblending
Suggests:   kipi-plugins-calendar
Suggests:   kipi-plugins-batchprocess
Suggests:   kipi-plugins-advancedslideshow
Suggests:   kipi-plugins-printimages
Suggests:   kipi-plugins-dngconverter
Suggests:   kipi-plugins-galleryexport
Suggests:   kipi-plugins-flashexport
Suggests:   kipi-plugins-facebook
Suggests:   kipi-plugins-acquireimages
Suggests:   kipi-plugins-rawconverter
Suggests:   kipi-plugins-removeredeyes
Suggests:   kipi-plugins-sendimages
Suggests:   kipi-plugins-youtube
Suggests:   kipi-plugins-kmlexport
Suggests:   kipi-plugins-yandexfotki
Suggests:   kipi-plugins-rajceexport
Suggests:   kipi-plugins-panorama
Suggests:   kipi-plugins-vkontakte

%description -n kipi-plugins
The library of the KDE Image Plugin Interface.

Libkipi allows image applications to use a plugin architecture
for additional functionality such as: RawConverter, SlideShow, 
ImagesGallery, HTMLExport, PrintAssistant...

%files -n kipi-plugins -f kipi-plugins.lang

%doc extra/kipi-plugins/AUTHORS extra/kipi-plugins/COPYING extra/kipi-plugins/COPYING-ADOBE extra/kipi-plugins/ChangeLog extra/kipi-plugins/README extra/kipi-plugins/TODO extra/kipi-plugins/NEWS
%_kde_applicationsdir/kipiplugins.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-timeadjust
Summary:    Time Adjust kipi plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-timeadjust
A Tool to adjust time and date.

%files -n kipi-plugins-timeadjust -f kipiplugin_timeadjust.lang
%_kde_libdir/kde4/kipiplugin_timeadjust.so
%_kde_iconsdir/hicolor/*/actions/timeadjust.png
%_kde_services/kipiplugin_timeadjust.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-smug
Summary:    Smug Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-smug
A tool to import/export images to/from SmugMug web service.

%files -n kipi-plugins-smug -f kipiplugin_smug.lang
%_kde_libdir/kde4/kipiplugin_smug.so
%_kde_iconsdir/hicolor/*/actions/smugmug.png
%_kde_iconsdir/hicolor/scalable/actions/smugmug.svgz
%_kde_services/kipiplugin_smug.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-shwup
Summary:    Shwup Kipi Plugins
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-shwup
A tool to export images to a remote Shwup web service.

%files -n kipi-plugins-shwup -f kipiplugin_shwup.lang
%_kde_libdir/kde4/kipiplugin_shwup.so
%_kde_iconsdir/hicolor/*/actions/shwup.png
%_kde_services/kipiplugin_shwup.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-piwigoexport
Summary:    Piwi Go Export
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-piwigoexport
A tool to export images to a remote Piwigo.

%files -n kipi-plugins-piwigoexport -f kipiplugin_piwigoexport.lang
%_kde_libdir/kde4/kipiplugin_piwigoexport.so
%_kde_appsdir/kipiplugin_piwigoexport
%_kde_services/kipiplugin_piwigoexport.desktop
%_kde_iconsdir/hicolor/scalable/actions/piwigo.svgz
%_kde_iconsdir/hicolor/*/actions/piwigo.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-picasa
Summary:    Picasa Kipi Plugins
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-picasa
A tool to export images to a remote Picase Web Service

%files -n kipi-plugins-picasa -f kipiplugin_picasawebexport.lang
%_kde_libdir/kde4/kipiplugin_picasawebexport.so
%_kde_services/kipiplugin_picasawebexport.desktop
%_kde_iconsdir/hicolor/scalable/actions/picasa.svgz
%_kde_iconsdir/hicolor/*/actions/picasa.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-metadataedit
Summary:    Meta Data Edit kipi plugins
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-metadataedit
A tool to edit EXIF,IPTC and XMP metadata.

%files -n kipi-plugins-metadataedit -f kipiplugin_metadataedit.lang
%_kde_libdir/kde4/kipiplugin_metadataedit.so
%_kde_services/kipiplugin_metadataedit.desktop
%_kde_iconsdir/hicolor/*/actions/metadataedit.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-kopete
Summary:    Kopete kipi plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   kipi-common

%description -n kipi-plugins-kopete 
A tool to export images to an instant messaging contact.

%files -n kipi-plugins-kopete 
%{_kde_libdir}/kde4/kipiplugin_kopete.so
%_kde_services/kipiplugin_kopete.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-kioexportimport
Summary:    Kio Export Import Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   kipi-common

%description -n kipi-plugins-kioexportimport
A tool to export pictures to or import from a remote directory that is
accessible via KIO.

%files -n kipi-plugins-kioexportimport -f kipiplugin_kioexportimport.lang
%_kde_libdir/kde4/kipiplugin_kioexportimport.so
%_kde_services/kipiplugin_kioexportimport.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-jpeglossless
Summary:    Jpeg Lossless Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-jpeglossless
A tool to rotate/flip images without losing quality.

%files -n kipi-plugins-jpeglossless -f kipiplugin_jpeglossless.lang
%_kde_libdir/kde4/kipiplugin_jpeglossless.so
%_kde_services/kipiplugin_jpeglossless.desktop
%_kde_iconsdir/hicolor/*/actions/flip-horizontal.png
%_kde_iconsdir/hicolor/*/actions/grayscaleconvert.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-ipodexport
Summary:    Ipod Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   kipi-common

%description -n kipi-plugins-ipodexport
A tool to export pictures to an Ipod device.

%files -n kipi-plugins-ipodexport -f kipiplugin_ipodexport.lang
%_kde_libdir/kde4/kipiplugin_ipodexport.so
%_kde_services/kipiplugin_ipodexport.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-imageviewer
Summary:    Image Viewer Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-imageviewer 
A tool to preview images using OpenGl.

%files -n kipi-plugins-imageviewer -f kipiplugin_imageviewer.lang
%_kde_libdir/kde4/kipiplugin_imageviewer.so
%_kde_appsdir/kipiplugin_imageviewer
%_kde_services/kipiplugin_imageviewer.desktop
%_kde_iconsdir/hicolor/*/actions/ogl.png 

#-----------------------------------------------------------------------

%package -n kipi-plugins-htmlexport
Summary:    Html Export Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-htmlexport
A tool to export images collections into a static XHTML page.

%files -n kipi-plugins-htmlexport -f kipiplugin_htmlexport.lang
%_kde_libdir/kde4/kipiplugin_htmlexport.so
%_kde_services/kipiplugin_htmlexport.desktop
%_kde_appsdir/kipiplugin_htmlexport

#-----------------------------------------------------------------------

%package -n kipi-plugins-debianscreenshot
Summary:    Debian Screenshot kipi plugins
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-debianscreenshot
A tool to export images to the Debian Screenshots site.

%files -n kipi-plugins-debianscreenshot 
%_kde_libdir/kde4/kipiplugin_debianscreenshots.so 
%_kde_services/kipiplugin_debianscreenshots.desktop
%_kde_iconsdir/hicolor/*/actions/debianscreenshots.png 
%_kde_iconsdir/hicolor/scalable/actions/debianscreenshots.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-gpssync
Summary:    GPS Sync Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   kipi-common

%description -n kipi-plugins-gpssync
A tool to geolocalize pictures.

%files -n kipi-plugins-gpssync -f kipiplugin_gpssync.lang
%_kde_appsdir/gpssync
%_kde_libdir/kde4/kipiplugin_gpssync.so
%_kde_services/kipiplugin_gpssync.desktop
%_kde_iconsdir/hicolor/*/actions/gpsimagetag.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-flickr
Summary:    Flick Export Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-flickr
A tool to export images to a remote Flickr, 23 and Zoomr web services.

%files -n kipi-plugins-flickr -f kipiplugin_flickrexport.lang
%_kde_libdir/kde4/kipiplugin_flickrexport.so
%_kde_services/kipiplugin_flickrexport.desktop
%_kde_iconsdir/hicolor/*/actions/flickr.png
%_kde_iconsdir/hicolor/*/actions/hq.png 
%_kde_iconsdir/hicolor/*/actions/zooomr.png
%_kde_iconsdir/hicolor/scalable/actions/flickr.svgz
%_kde_iconsdir/hicolor/scalable/actions/hq.svgz 
%_kde_iconsdir/hicolor/scalable/actions/zooomr.svgz 

#-----------------------------------------------------------------------

%package -n kipi-plugins-expoblending
Summary:    Expoblending Kipi Plugin
Group:      System/Libraries
# need align_image_stack from Hugin project and enfuse from Enblend project (runtime dependency)
Requires:   hugin
Requires:   libkdcraw-common
Requires:   kipi-common
Conflicts:  kipi-plugins < 1:1.8.0-1


%description -n kipi-plugins-expoblending
A tool to blend bracketed images.

%files -n kipi-plugins-expoblending -f kipiplugin_expoblending.lang
%_kde_bindir/expoblending
%_kde_applicationsdir/expoblending.desktop
%_kde_libdir/kde4/kipiplugin_expoblending.so
%_kde_appsdir/kipiplugin_expoblending 
%_kde_services/kipiplugin_expoblending.desktop
%_kde_iconsdir/hicolor/*/actions/expoblending.png

#-----------------------------------------------------------------------

%package -n kipi-plugins-calendar 
Summary:    Calendar Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-calendar
A tool to create calendars.

%files -n kipi-plugins-calendar -f kipiplugin_calendar.lang
%_kde_libdir/kde4/kipiplugin_calendar.so
%_kde_services/kipiplugin_calendar.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-batchprocess
Summary:    Batch Process Images Kipi Plugin
Group:      System/Libraries
# Resizing pictures need convert from imagemagick
Requires:   imagemagick
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   kipi-common

%description -n kipi-plugins-batchprocess
KIPI Batch Processing Images Plugin.

%files -n kipi-plugins-batchprocess -f kipiplugin_batchprocessimages.lang

%_kde_libdir/kde4/kipiplugin_batchprocessimages.so
%_kde_services/kipiplugin_batchprocessimages.desktop
%_kde_iconsdir/hicolor/*/actions/recompressimages.png
%_kde_iconsdir/hicolor/*/actions/renameimages.png
%_kde_iconsdir/hicolor/*/actions/resizeimages.png
%_kde_iconsdir/hicolor/*/actions/borderimages.png
%_kde_iconsdir/hicolor/*/actions/colorimages.png
%_kde_iconsdir/hicolor/*/actions/convertimages.png
%_kde_iconsdir/hicolor/*/actions/effectimages.png 
%_kde_iconsdir/hicolor/*/actions/filterimages.png 

#-----------------------------------------------------------------------

%package -n kipi-plugins-advancedslideshow
Summary:    Advanced Slideshow Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-advancedslideshow
A tool to slide images with 2D and 3D effects using OpenGL.

%files -n kipi-plugins-advancedslideshow -f kipiplugin_advancedslideshow.lang
%_kde_libdir/kde4/kipiplugin_advancedslideshow.so
%_kde_iconsdir/hicolor/*/actions/slideshow.png
%_kde_services/kipiplugin_advancedslideshow.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-printimages
Summary:    Print Images Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-printimages
A tool to print images in various formats.

%files -n kipi-plugins-printimages -f kipiplugin_printimages.lang
%_kde_libdir/kde4/kipiplugin_printimages.so
%_kde_services/kipiplugin_printimages.desktop
%_kde_appsdir/kipiplugin_printimages/

#-----------------------------------------------------------------------

%package -n kipi-plugins-dngconverter
Summary:    Dng converter Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-dngconverter
A tool to convert Raw Image to Digital NeGative.

%files -n kipi-plugins-dngconverter -f kipiplugin_dngconverter.lang
%_kde_bindir/dngconverter
%_kde_bindir/dnginfo
%_kde_applicationsdir/dngconverter.desktop
%_kde_libdir/kde4/kipiplugin_dngconverter.so
%_kde_services/kipiplugin_dngconverter.desktop
%_kde_iconsdir/oxygen/*/apps/dngconverter.png
%_kde_iconsdir/oxygen/scalable/apps/dngconverter.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-galleryexport
Summary:    Gallery Export Kipi Plugin
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-galleryexport
A tool to export images to a remote Gallery.

%files -n kipi-plugins-galleryexport -f kipiplugin_galleryexport.lang
%_kde_libdir/kde4/kipiplugin_galleryexport.so
%_kde_appsdir/kipiplugin_galleryexport
%_kde_services/kipiplugin_galleryexport.desktop
%_kde_iconsdir/hicolor/*/actions/gallery.png
%_kde_iconsdir/hicolor/scalable/actions/gallery.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-flashexport
Summary:    Flash export kipi-plugins
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-flashexport
A tool to export images to Flash.

%files -n kipi-plugins-flashexport -f kipiplugin_flashexport.lang
%_kde_libdir/kde4/kipiplugin_flashexport.so
%_kde_appsdir/kipiplugin_flashexport
%_kde_services/kipiplugin_flashexport.desktop
%_kde_iconsdir/hicolor/*/actions/flash.png
%_kde_iconsdir/hicolor/scalable/actions/flash.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-facebook
Summary:    Facebook kipi plugins
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-facebook
A tool to import/export images to/from a remote Facebook web service.

%files -n kipi-plugins-facebook -f kipiplugin_facebook.lang
%_kde_libdir/kde4/kipiplugin_facebook.so
%_kde_services/kipiplugin_facebook.desktop
%_kde_iconsdir/hicolor/*/actions/facebook.png
%_kde_iconsdir/hicolor/scalable/actions/facebook.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-acquireimages
Summary:    Acquireimages
Group:      System/Libraries
Requires:   kipi-common
Conflicts:  kipi-plugins < 1:1.8.0-1

%description -n kipi-plugins-acquireimages
A tool to acquire images using flat scanner.

%files -n kipi-plugins-acquireimages -f kipiplugin_acquireimages.lang
%_kde_bindir/scangui
%_kde_libdir/kde4/kipiplugin_acquireimages.so
%_kde_services/kipiplugin_acquireimages.desktop 
%_kde_applicationsdir/scangui.desktop 

#-----------------------------------------------------------------------

%package -n kipi-plugins-rawconverter
Summary:    Rawconverter kipi plugins
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-rawconverter
A tool to convert Raw Image to JPEG/PNG/TIFF.

%files -n kipi-plugins-rawconverter -f kipiplugin_rawconverter.lang
%_kde_libdir/kde4/kipiplugin_rawconverter.so
%_kde_iconsdir/oxygen/*/apps/rawconverter.png
%_kde_services/kipiplugin_rawconverter.desktop
%_kde_iconsdir/oxygen/scalable/apps/rawconverter.svgz

#-----------------------------------------------------------------------

%package -n kipi-plugins-removeredeyes
Summary:    Remove red eyes kipi-plugins
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   kipi-common

%description -n kipi-plugins-removeredeyes
A tool to remove red eyes automatically from images.

%files -n kipi-plugins-removeredeyes -f kipiplugin_removeredeyes.lang
%_kde_libdir/kde4/kipiplugin_removeredeyes.so
%_kde_datadir/apps/kipiplugin_removeredeyes
%_kde_services/kipiplugin_removeredeyes.desktop 

#-----------------------------------------------------------------------

%package -n kipi-plugins-sendimages
Summary:    Send Images kipi plugins
Group:      System/Libraries
Conflicts:  kipi-plugins < 1:1.8.0-1
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-sendimages
A tool to send images by e-mail.

%files -n kipi-plugins-sendimages -f kipiplugin_sendimages.lang
%_kde_libdir/kde4/kipiplugin_sendimages.so 
%_kde_services/kipiplugin_sendimages.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-kmlexport
Summary:    Create KML files to present images with coordinates
Group:      System/Libraries
Requires:   kipi-common

%description -n kipi-plugins-kmlexport 
A plugin to create KML files to present images with coordinates.

%files -n kipi-plugins-kmlexport 
%_kde_libdir/kde4/kipiplugin_kmlexport.so
%_kde_services/kipiplugin_kmlexport.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-yandexfotki
Summary:    Yandex.Fotki Exporter
Group:      System/Libraries
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-yandexfotki
A tool to export images to a remote Yandex.Fotki web service.

%files -n kipi-plugins-yandexfotki 
%_kde_libdir/kde4/kipiplugin_yandexfotki.so
%_kde_services/kipiplugin_yandexfotki.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-rajceexport
Summary:    Rajce.net Exporter
Group:      System/Libraries
Requires:   libkdcraw-common
Requires:   kipi-common

%description -n kipi-plugins-rajceexport
A tool to export images to a remote rajce.net service.

%files -n kipi-plugins-rajceexport 
%_kde_libdir/kde4/kipiplugin_rajceexport.so
%_kde_services/kipiplugin_rajceexport.desktop
%_kde_iconsdir/hicolor/*/actions/rajce.png


#-----------------------------------------------------------------------
%package -n kipiplugin-photolayouts-editor
Summary: Photo Layouts Editor
Group:  System/Libraries
Requires: kipi-common
%description -n kipiplugin-photolayouts-editor
Photo Layouts Editor.

%files -n kipiplugin-photolayouts-editor
%_kde_bindir/photolayoutseditor
%_kde_iconsdir/hicolor/*/apps/photolayoutseditor.png
%_kde_services/kipiplugin_photolayoutseditor.desktop
%_kde_datadir/kde4/servicetypes/photolayoutseditorborderplugin.desktop
%_kde_datadir/kde4/servicetypes/photolayoutseditoreffectplugin.desktop
%_kde_libdir/kde4/kipiplugin_photolayoutseditor.so
%_kde_applicationsdir/photolayoutseditor.desktop
%_kde_appsdir/photolayoutseditor/photolayoutseditorui.rc
%_kde_datadir/config.kcfg/PLEConfigSkeleton.kcfgc

#-----------------------------------------------------------------------

%package -n kipi-plugins-panorama
Summary:    Panorama tools
Group:      System/Libraries
Requires:   libkdcraw-common
Requires:   kipi-common
Requires:   hugin

%description -n kipi-plugins-panorama
A tool to create panorama.

%files -n kipi-plugins-panorama 
%_kde_bindir/panoramagui
%_kde_libdir/kde4/kipiplugin_panorama.so
%_kde_appsdir/kipiplugin_panorama/
%_kde_services/kipiplugin_panorama.desktop 
%_kde_applicationsdir/panoramagui.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-vkontakte
Summary:    VKontakte.ru Exporter
Group:      System/Libraries
Requires:   kipi-common


%description -n kipi-plugins-vkontakte
A tool to export on VKontakte.ru Web service

%files -n kipi-plugins-vkontakte 
%_kde_libdir/kde4/kipiplugin_vkontakte.so
%_kde_services/kipiplugin_vkontakte.desktop

#-----------------------------------------------------------------------

%define libnamedev %mklibname digikam -d

%define libmediawiki_devel %mklibname -d mediawiki
%package -n %libmediawiki_devel
Summary:     Headers to build packages against libmediawiki library
Group:       Development/C
Conflicts:   %libnamedev < 1:2.0.0-rc1.2
Requires:    %libmediawiki = %epoch:%version-%release
Provides:    libmediawiki-devel = %epoch:%version-%release

%description -n %libmediawiki_devel
This package contains the libraries and headers files needed to develop progams
which make use of libmediawiki library.

libmediawiki is a KDE C++ interface for MediaWiki based web service as 
wikipedia.org.


%files -n %libmediawiki_devel
%_includedir/libmediawiki
%_kde_libdir/libmediawiki.so
%_kde_libdir/pkgconfig/libmediawiki.pc
%_kde_appsdir/cmake/modules/FindMediawiki.cmake

#-----------------------------------------------------------------------

%define libkface_devel %mklibname -d kface
%package -n  %libkface_devel
Summary:     Headers to build packages against libkface library
Group:       Development/C
Conflicts:   %libnamedev < 1:2.0.0-rc1.2
Requires:    %libkface = %epoch:%version-%release
Requires:    libkface-common
Provides:    kface-devel = %version-%release
Provides:    libkface-devel = %version-%release

%description -n %libkface_devel
This package contains the libraries and headers files needed to develop progams
which make use of libkface library.

Libkface is a Qt/C++ wrapper around LibFace library to perform face recognition 
and detection over pictures.

%files -n %libkface_devel
%_includedir/libkface
%_kde_libdir/libkface.so
%_kde_libdir/pkgconfig/libkface.pc
%_kde_appsdir/cmake/modules/FindKface.cmake

#-----------------------------------------------------------------------

%define libkgeomap_devel %mklibname -d kgeomap
%package -n %libkgeomap_devel
Summary:     Headers to build packages against libkgeomap library
Group:       Development/C
Conflicts:   %libnamedev < 1:2.0.0-rc1.2
Requires:    libkgeomap-common
Requires:    %libkgeomap = %epoch:%version-%release
Provides:    kgeomap-devel = %version-%release
Provides:    libkgeomap-devel = %version-%release

%description -n %libkgeomap_devel
This package contains the libraries and headers files needed to develop progams
which make use of libkgeomap (old libkmap) library.

Libkgeomap is a wrapper around world map components as Marble, OpenstreetMap and
GoogleMap,for browsing and arranging photos on a map.

%files -n %libkgeomap_devel
%_includedir/libkgeomap
%_kde_libdir/libkgeomap.so
%_kde_libdir/pkgconfig/libkgeomap.pc
%_kde_appsdir/cmake/modules/FindKGeoMap.cmake

#-----------------------------------------------------------------------

%package -n %libnamedev
Summary:        Static libraries and headers for %name
Group:          Development/C
Provides:       lib%name-devel = %epoch:%version-%release
Provides:       kipi-plugins-devel = %epoch:%version-%release
Obsoletes:      kipi-plugins-devel < 1:2.0.0
Requires:       %libdigikamcore = %epoch:%version-%release
Requires:       %libdigikamdatabase = %epoch:%version-%release
Requires:       %libkgeomap_devel = %epoch:%version-%release
Requires:       %libmediawiki_devel = %epoch:%version-%release
Requires:       %libkface_devel = %epoch:%version-%release
Requires:       %libkipiplugins = %epoch:%version-%release

%description -n %libnamedev
%libnamedev contains the libraries and header files needed to
develop programs which make use of %name.
The library documentation is available on header files.

%files -n %libnamedev
%_kde_libdir/libdigikamcore.so
%_kde_libdir/libdigikamdatabase.so
%_kde_libdir/libkipiplugins.so
%_kde_libdir/libPropertyBrowser.a
#-----------------------------------------------------------------------

%prep
# Unpack correct files & reemove wrong png/svgz  (kde #286034) this part should be removed for next digikam version
%setup -q -a 1
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

%find_lang %name --with-html
%find_lang showfoto --with-html
%find_lang kipi-plugins kipiplugins kipi-plugins.lang --with-html

%find_lang kipiplugin_rawconverter
%find_lang kipiplugin_sendimages
%find_lang kipiplugin_calendar
%find_lang kipiplugin_dngconverter
%find_lang kipiplugin_expoblending
%find_lang kipiplugin_facebook
%find_lang kipiplugin_flashexport
%find_lang kipiplugin_flickrexport
%find_lang kipiplugin_galleryexport
%find_lang kipiplugin_gpssync
%find_lang kipiplugin_htmlexport
%find_lang kipiplugin_imageviewer
%find_lang kipiplugin_ipodexport
%find_lang kipiplugin_jpeglossless
%find_lang kipiplugin_kioexportimport
%find_lang kipiplugin_metadataedit
%find_lang kipiplugin_picasawebexport
%find_lang kipiplugin_piwigoexport
%find_lang kipiplugin_printimages
%find_lang kipiplugin_rawconverter
%find_lang kipiplugin_removeredeyes
%find_lang kipiplugin_sendimages
%find_lang kipiplugin_shwup
%find_lang kipiplugin_timeadjust
%find_lang kipiplugin_acquireimages
%find_lang kipiplugin_advancedslideshow
%find_lang kipiplugin_batchprocessimages
%find_lang kipiplugin_smug
%find_lang libkgeomap
