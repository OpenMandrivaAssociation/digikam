# Disable until libmediawiki gets individual tarball release
%bcond_with wikimedia

%define pre beta2

Summary:	A KDE photo management utility
Name:		digikam
Epoch:		2
Version:	5.0.0
Release:	0.1
License:	GPLv2+
Group:		Graphics
Url:		http://www.digikam.org
Source0:	http://download.kde.org/stable/digikam/%{name}-%{version}-%pre.tar.bz2
Source100:	%{name}.rpmlintrc
Patch1:		digikam-5.0.0-beta2-clang.patch
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	eigen3
BuildRequires:	flex
BuildRequires:	imagemagick
BuildRequires:	mariadb-server
BuildRequires:	gomp-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(lensfun)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libgphoto2)
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libpgf)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(lqr-1) >= 0.4.0
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(exiv2)

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5WebKitWidgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5MultimediaWidgets)
BuildRequires:	cmake(Qt5XmlPatterns)
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
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	cmake(KF5Kipi)
BuildRequires:	cmake(KF5CalendarCore)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5Sane)
BuildRequires:	cmake(MarbleQt5)

Requires:	mariadb-common
Requires:	kipi-common
Requires:	kipi-plugins
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
%doc core/AUTHORS core/ChangeLog core/COPYING core/COPYING.LIB core/NEWS core/README
%{_kde5_bindir}/digikam
%{_kde5_bindir}/digitaglinktree
%{_kde5_bindir}/cleanup_digikamdb
%{_kde5_datadir}/digikam
%{_kde5_datadir}/kxmlgui5/digikam
%{_kde5_appsdir}/solid/actions/digikam*.desktop
%{_kde5_applicationsdir}/digikam.desktop
%{_kde5_datadir}/appdata/digikam.appdata.xml
%{_kde5_datadir}/appdata/digiKam-ImagePlugin_*.metainfo.xml
%{_kde5_services}/digikam*.desktop
%{_kde5_services}/digikam*.protocol
%{_kde5_servicetypes}/digikam*.desktop
%{_kde5_mandir}/man1/digitaglinktree.1*
%{_kde5_mandir}/man1/cleanup_digikamdb.1*
%{_kde5_iconsdir}/*/*/apps/digikam.*
%{_libdir}/libexec/digikamdatabaseserver
%{_qt5_plugindir}/digikamimageplugin_*
%_iconsdir/*/*/*/kipi-process-working.*

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
%{_kde5_bindir}/showfoto
%{_kde5_datadir}/showfoto.desktop
%{_kde5_datadir}/kxmlgui5/showfoto
%{_kde5_datadir}/showfoto
%{_kde5_datadir}/appdata/showfoto.appdata.xml
%{_kde5_iconsdir}/*/*/apps/showfoto.*

#-----------------------------------------------------------------------

%define libdigikamdatabase_major 5
%define libdigikamdatabase %mklibname digikamdatabase %{libdigikamdatabase_major}

%package -n %{libdigikamdatabase}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}digikamdatabase2 < 2:3.0.0
Obsoletes:	%{_lib}digikamdatabase3 < 2:4.0.0

%description -n %{libdigikamdatabase}
Librairie File needed by %{name}

%files -n %{libdigikamdatabase}
%{_kde5_libdir}/libdigikamdatabase.so.%{libdigikamdatabase_major}*

#-----------------------------------------------------------------------

%define libdigikamcore_major 5
%define libdigikamcore %mklibname digikamcore %{libdigikamcore_major}

%package -n %{libdigikamcore}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}digikamcore2 < 2:3.0.0
Obsoletes:	%{_lib}digikamcore3 < 2:4.0.0

%description -n %{libdigikamcore}
Librairie File needed by %{name}

%files -n %{libdigikamcore}
%{_kde5_libdir}/libdigikamcore.so.%{libdigikamcore_major}*

#-----------------------------------------------------------------------

%define libkipiplugins_major 5
%define libkipiplugins %mklibname KF5kipiplugins %{libkipiplugins_major}

%package -n %{libkipiplugins}
Summary:	Runtime library for %{name}
Group:		System/Libraries
Obsoletes:	%{_lib}kipiplugins2 < 2:3.0.0
Obsoletes:	%{_lib}kipiplugins3 < 2:4.0.0

%description -n %{libkipiplugins}
Librairie File needed by %{name}

%files -n %{libkipiplugins}
%{_kde5_libdir}/libKF5kipiplugins.so.%{libkipiplugins_major}*


#-----------------------------------------------------------------------

%define libdigikamgui_major 5
%define libdigikamgui %mklibname digikamgui %libdigikamgui_major

%package -n %libdigikamgui
Summary: Runtime library for %{name}
Group: System/Libraries

%description -n %libdigikamgui
Librairie File needed by %name

%files -n %libdigikamgui
%{_kde5_libdir}/libdigikamgui.so.%{libdigikamgui_major}*


#-----------------------------------------------------------------------

%define libnamedev %mklibname digikam -d

%package        -n     %libnamedev
Summary:        Static libraries and headers for %name
Group:          Development/C
Provides:       %name-devel = %epoch:%version-%release
Provides:       kipi-plugins-devel = %epoch:%version-%release
Obsoletes:      kipi-plugins-devel < 1:2.0.0
Requires:       %libdigikamcore = %epoch:%version-%release
Requires:       %libdigikamgui = %epoch:%version-%release
Requires:       %libdigikamdatabase = %epoch:%version-%release
Requires:       %libkipiplugins = %epoch:%version-%release

%description  -n     %libnamedev
%libnamedev contains the libraries and header files needed to
develop programs which make use of %name.
The library documentation is available on header files.

%files -n     %libnamedev
%{_kde5_libdir}/*.so

#-----------------------------------------------------------------------

%package -n kipi-plugins
Summary:	KDE image Interface Plugins
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/graphics/kipi-plugins
BuildArch:	noarch
Suggests:	kipi-plugins-advancedslideshow
Suggests:	kipi-plugins-dlna
Suggests:	kipi-plugins-dropbox
Suggests:	kipi-plugins-expoblending
Suggests:	kipi-plugins-facebook
Suggests:	kipi-plugins-flashexport
Suggests:	kipi-plugins-flickr
Suggests:	kipi-plugins-googleservices
Suggests:	kipi-plugins-imageshack
Suggests:	kipi-plugins-imageviewer
Suggests:	kipi-plugins-imgurexport
Suggests:	kipi-plugins-kmlexport
Suggests:	kipi-plugins-panorama
Suggests:	kipi-plugins-piwigoexport
Suggests:	kipi-plugins-printimages
Suggests:	kipi-plugins-rajceexport
Suggests:	kipi-plugins-sendimages
Suggests:	kipi-plugins-smug
Suggests:	kipi-plugins-videoslideshow
Suggests:	kipi-plugins-vkontakte
%if %{with wikimedia}
Suggests:	kipi-plugins-wikimedia
%else
Obsoletes:	kipi-plugins-wikimedia < %{EVRD}
%endif
Suggests:	kipi-plugins-yandexfotki

%description -n kipi-plugins
The library of the KDE Image Plugin Interface.

Libkipi allows image applications to use a plugin architecture
for additional functionality such as: RawConverter, SlideShow, 
ImagesGallery, HTMLExport, PrintAssistant...

%files -n kipi-plugins -f kipi-plugins.lang
%{_datadir}/apps/kipi/tips
%doc extra/kipi-plugins/AUTHORS extra/kipi-plugins/COPYING extra/kipi-plugins/COPYING-ADOBE extra/kipi-plugins/ChangeLog extra/kipi-plugins/README extra/kipi-plugins/TODO extra/kipi-plugins/NEWS
%{_kde5_applicationsdir}/kipiplugins.desktop

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
%{_kde5_appsdir}/kipi/kipiplugin_advancedslideshowui.rc
%{_kde5_libdir}/kde4/kipiplugin_advancedslideshow.so
%{_kde5_services}/kipiplugin_advancedslideshow.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-slideshow.*

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
%{_kde5_appsdir}/kipi/kipiplugin_batchprocessimagesui.rc
%{_kde5_libdir}/kde4/kipiplugin_batchprocessimages.so
%{_kde5_services}/kipiplugin_batchprocessimages.desktop
%{_kde5_iconsdir}/hicolor/*/actions/recompressimages.png
%{_kde5_iconsdir}/hicolor/*/actions/renameimages.png
%{_kde5_iconsdir}/hicolor/*/actions/resizeimages.png
%{_kde5_iconsdir}/hicolor/*/actions/borderimages.png
%{_kde5_iconsdir}/hicolor/*/actions/colorimages.png
%{_kde5_iconsdir}/hicolor/*/actions/convertimages.png
%{_kde5_iconsdir}/hicolor/*/actions/effectimages.png
%{_kde5_iconsdir}/hicolor/*/actions/filterimages.png

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
#%{_kde5_appsdir}/kipi/kipiplugin_calendarui.rc
#%{_kde5_libdir}/kde4/kipiplugin_calendar.so
#%{_kde5_services}/kipiplugin_calendar.desktop

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
%{_kde5_appsdir}/kipi/kipiplugin_debianscreenshotsui.rc
%{_kde5_libdir}/kde4/kipiplugin_debianscreenshots.so
%{_kde5_services}/kipiplugin_debianscreenshots.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-debianscreenshots.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-dlna
Summary:	DLNA support
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-dlna
A tool to support DLNA.

%files -n kipi-plugins-dlna -f kipiplugin_dlnaexport.lang
%{_kde5_appsdir}/kipi/kipiplugin_dlnaexportui.rc
%{_kde5_appsdir}/kipiplugin_dlnaexport
%{_kde5_libdir}/kde4/kipiplugin_dlnaexport.so
%{_kde5_services}/kipiplugin_dlnaexport.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-dlna.*

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
%{_kde5_appsdir}/kipi/kipiplugin_dngconverterui.rc
%{_kde5_bindir}/dngconverter
%{_kde5_applicationsdir}/dngconverter.desktop
%{_kde5_libdir}/kde4/kipiplugin_dngconverter.so
%{_kde5_services}/kipiplugin_dngconverter.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-dngconverter.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-dropbox
Summary:	Dropbox export Kipi Plugin
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-dropbox
A tool to export images to a remote Dropbox web service.

%files -n kipi-plugins-dropbox -f kipiplugin_dropbox.lang
%{_kde5_appsdir}/kipi/kipiplugin_dropboxui.rc
%{_kde5_libdir}/kde4/kipiplugin_dropbox.so
%{_kde5_services}/kipiplugin_dropbox.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-dropbox.*

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
%{_kde5_appsdir}/kipi/kipiplugin_expoblendingui.rc
%{_kde5_appsdir}/kipiplugin_expoblending
%{_kde5_bindir}/expoblending
%{_kde5_applicationsdir}/expoblending.desktop
%{_kde5_libdir}/kde4/kipiplugin_expoblending.so
%{_kde5_services}/kipiplugin_expoblending.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-expoblending.*

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
%{_kde5_appsdir}/kipi/kipiplugin_facebookui.rc
%{_kde5_libdir}/kde4/kipiplugin_facebook.so
%{_kde5_services}/kipiplugin_facebook.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-facebook.*

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
%{_kde5_appsdir}/kipi/kipiplugin_flashexportui.rc
%{_kde5_libdir}/kde4/kipiplugin_flashexport.so
%{_kde5_appsdir}/kipiplugin_flashexport
%{_kde5_services}/kipiplugin_flashexport.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-flash.*

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
%{_kde5_appsdir}/kipi/kipiplugin_flickrexportui.rc
%{_kde5_libdir}/kde4/kipiplugin_flickrexport.so
%{_kde5_services}/kipiplugin_flickrexport.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-flickr.*
%{_kde5_iconsdir}/hicolor/*/apps/kipi-hq.*
%{_kde5_iconsdir}/hicolor/*/apps/kipi-zooomr.*

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
%{_kde5_appsdir}/kipi/kipiplugin_galleryexportui.rc
%{_kde5_libdir}/kde4/kipiplugin_galleryexport.so
%{_kde5_appsdir}/kipiplugin_galleryexport
%{_kde5_services}/kipiplugin_galleryexport.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-gallery.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-googleservices
Summary:	Google services export Kipi Plugin
Group:		System/Libraries
Requires:	kipi-common
%rename kipi-plugins-googledrive
%rename kipi-plugins-picasa

%description -n kipi-plugins-googleservices
A tool to export images to a remote services.

%files -n kipi-plugins-googleservices -f kipiplugin_googledrive.lang
%{_kde5_appsdir}/kipi/kipiplugin_googleservicesui.rc
%{_kde5_libdir}/kde4/kipiplugin_googleservices.so
%{_kde5_services}/kipiplugin_googleservices.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-googledrive.*
%{_kde5_iconsdir}/hicolor/*/apps/kipi-picasa.*

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
%{_kde5_appsdir}/kipi/kipiplugin_imageviewerui.rc
%{_kde5_libdir}/kde4/kipiplugin_imageviewer.so
%{_kde5_appsdir}/kipiplugin_imageviewer
%{_kde5_services}/kipiplugin_imageviewer.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-ogl.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-imageshack
Summary:	Imageshack Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-imageshack
A tool to export images to ImageShack.

%files -n kipi-plugins-imageshack -f kipiplugin_imageshackexport.lang
%{_kde5_appsdir}/kipi/kipiplugin_imageshackexportui.rc
%{_kde5_libdir}/kde4/kipiplugin_imageshackexport.so
%{_kde5_services}/kipiplugin_imageshackexport.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-imageshack.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-imgurexport
Summary:	Imgur Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-imgurexport
A tool to export pictures to Imgur.

%files -n kipi-plugins-imgurexport -f kipiplugin_imgurexport.lang
%{_kde5_appsdir}/kipi/kipiplugin_imgurexportui.rc
%{_kde5_libdir}/kde4/kipiplugin_imgurexport.so
%{_kde5_services}/kipiplugin_imgurexport.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-imgur.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-kmlexport
Summary:	Create KML files to present images with coordinates
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-kmlexport
A plugin to create KML files to present images with coordinates.

%files -n kipi-plugins-kmlexport -f kipiplugin_kmlexport.lang
%{_kde5_appsdir}/kipi/kipiplugin_kmlexportui.rc
%{_kde5_libdir}/kde4/kipiplugin_kmlexport.so
%{_kde5_services}/kipiplugin_kmlexport.desktop

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
%{_kde5_appsdir}/kipi/kipiplugin_panoramaui.rc
%{_kde5_bindir}/panoramagui
%{_kde5_libdir}/kde4/kipiplugin_panorama.so
%{_kde5_appsdir}/kipiplugin_panorama/
%{_kde5_services}/kipiplugin_panorama.desktop
%{_kde5_applicationsdir}/panoramagui.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-panorama.*

#-----------------------------------------------------------------------

%package -n kipiplugin-photolayouts-editor
Summary:	Photo Layouts Editor
Group:		System/Libraries
Requires:	kipi-common

%description -n kipiplugin-photolayouts-editor
Photo Layouts Editor.

%files -n kipiplugin-photolayouts-editor -f kipiplugin_photolayouteditor.lang
%{_kde5_appsdir}/kipi/kipiplugin_photolayoutseditorui.rc
%{_kde5_appsdir}/photolayoutseditor
%{_kde5_applicationsdir}/photolayoutseditor.desktop
%{_kde5_bindir}/photolayoutseditor
%{_kde5_libdir}/kde4/kipiplugin_photolayoutseditor.so
%{_kde5_services}/kipiplugin_photolayoutseditor.desktop
%{_kde5_servicetypes}/photolayoutseditorborderplugin.desktop
%{_kde5_servicetypes}/photolayoutseditoreffectplugin.desktop
%{_kde5_datadir}/templates/kipiplugins_photolayoutseditor
%{_kde5_datadir}/config.kcfg/photolayoutseditor.kcfg
%{_kde5_iconsdir}/hicolor/*/apps/photolayoutseditor.png

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
%{_kde5_appsdir}/kipi/kipiplugin_piwigoexportui.rc
%{_kde5_libdir}/kde4/kipiplugin_piwigoexport.so
%{_kde5_appsdir}/kipiplugin_piwigoexport
%{_kde5_services}/kipiplugin_piwigoexport.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-piwigo.*

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
%{_kde5_appsdir}/kipi/kipiplugin_printimagesui.rc
%{_kde5_libdir}/kde4/kipiplugin_printimages.so
%{_kde5_services}/kipiplugin_printimages.desktop
%{_kde5_appsdir}/kipiplugin_printimages/

#-----------------------------------------------------------------------

%package -n kipi-plugins-rajceexport
Summary:	Rajce.net Exporter
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-rajceexport
A tool to export images to a remote rajce.net service.

%files -n kipi-plugins-rajceexport -f kipiplugin_rajceexport.lang
%{_kde5_appsdir}/kipi/kipiplugin_rajceexportui.rc
%{_kde5_libdir}/kde4/kipiplugin_rajceexport.so
%{_kde5_services}/kipiplugin_rajceexport.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-rajce.*

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
%{_kde5_appsdir}/kipi/kipiplugin_sendimagesui.rc
%{_kde5_libdir}/kde4/kipiplugin_sendimages.so 
%{_kde5_services}/kipiplugin_sendimages.desktop

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
%{_kde5_appsdir}/kipi/kipiplugin_smugui.rc
%{_kde5_libdir}/kde4/kipiplugin_smug.so
%{_kde5_services}/kipiplugin_smug.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-smugmug.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-videoslideshow
Summary:	Video Slide Show export kipi plugin
Group:		System/Libraries
Requires:	kipi-common
Requires:	imagemagick

%description -n kipi-plugins-videoslideshow
A tool to export images as Video Slide Show.

%files -n kipi-plugins-videoslideshow -f kipiplugin_videoslideshow.lang
%{_kde5_appsdir}/kipi/kipiplugin_videoslideshowui.rc
%{_kde5_libdir}/kde4/kipiplugin_videoslideshow.so
%{_kde5_services}/kipiplugin_videoslideshow.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-vkontakte
Summary:	VKontakte.ru Exporter
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-vkontakte
A tool to export on VKontakte.ru Web service

%files -n kipi-plugins-vkontakte -f kipiplugin_vkontakte.lang
%{_kde5_appsdir}/kipi/kipiplugin_vkontakteui.rc
%{_kde5_libdir}/kde4/kipiplugin_vkontakte.so
%{_kde5_services}/kipiplugin_vkontakte.desktop

#-----------------------------------------------------------------------

%if %{with wikimedia}
%package -n kipi-plugins-wikimedia
Summary:	Wikimedia Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-wikimedia
A tool to export images to a remote MediaWiki site

%files -n kipi-plugins-wikimedia -f kipiplugin_wikimedia.lang
%{_kde5_appsdir}/kipi/kipiplugin_wikimediaui.rc
%{_kde5_libdir}/kde4/kipiplugin_wikimedia.so
%{_kde5_services}/kipiplugin_wikimedia.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-wikimedia.*
%endif

#-----------------------------------------------------------------------

%package -n kipi-plugins-yandexfotki
Summary:	Yandex.Fotki Exporter
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-yandexfotki
A tool to export images to a remote Yandex.Fotki web service.

%files -n kipi-plugins-yandexfotki -f kipiplugin_yandexfotki.lang
%{_kde5_appsdir}/kipi/kipiplugin_yandexfotkiui.rc
%{_kde5_libdir}/kde4/kipiplugin_yandexfotki.so
%{_kde5_services}/kipiplugin_yandexfotki.desktop

#-----------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}-%{pre}
%apply_patches

%build
%cmake_kde5 -G"Unix Makefiles" \
	-DENABLE_BALOOSUPPORT=ON \
	-DENABLE_LCMS2=ON \
	-DENABLE_KDEPIMLIBSSUPPORT=ON \
	-DENABLE_MYSQLSUPPORT=ON \
	-DENABLE_INTERNALMYSQL=ON \

%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/libkipi.mo

# Plugin not ready for production yet, disabled upstream

rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/kipiplugin_photivointegration.mo
%if %{without wikimedia}
rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/kipiplugin_wikimedia.mo
%endif

# Seems to be useless
rm -f %{buildroot}%{_kde5_libdir}/libdigikamcore.so
rm -f %{buildroot}%{_kde5_libdir}/libdigikamdatabase.so
rm -f %{buildroot}%{_kde5_libdir}/libkipiplugins.so

%find_lang %{name} --with-html || touch %{name}.lang
%find_lang showfoto --with-html || touch showfoto.lang
%find_lang kipi-plugins kipiplugins kipi-plugins.lang --with-html || touch kipi-plugins.lang

%find_lang kipiplugin_acquireimages || touch kipiplugin_acquireimages.lang
%find_lang kipiplugin_advancedslideshow || touch kipiplugin_advancedslideshow.lang
%find_lang kipiplugin_batchprocessimages || touch kipiplugin_batchprocessimages.lang
%find_lang kipiplugin_calendar || touch kipiplugin_calendar.lang
%find_lang kipiplugin_debianscreenshots || touch kipiplugin_debianscreenshots.lang
%find_lang kipiplugin_dlnaexport || touch kipiplugin_dlnaexport.lang
%find_lang kipiplugin_dngconverter || touch kipiplugin_dngconverter.lang
%find_lang kipiplugin_dropbox || touch kipiplugin_dropbox.lang
%find_lang kipiplugin_expoblending || touch kipiplugin_expoblending.lang
%find_lang kipiplugin_facebook || touch kipiplugin_facebook.lang
%find_lang kipiplugin_flashexport || touch kipiplugin_flashexport.lang
%find_lang kipiplugin_flickrexport || touch kipiplugin_flickrexport.lang
%find_lang kipiplugin_galleryexport || touch kipiplugin_galleryexport.lang
%find_lang kipiplugin_googledrive || touch kipiplugin_googledrive.lang
%find_lang kipiplugin_gpssync || touch kipiplugin_gpssync.lang
%find_lang kipiplugin_htmlexport || touch kipiplugin_htmlexport.lang
%find_lang kipiplugin_imageshackexport || touch kipiplugin_imageshackexport.lang
%find_lang kipiplugin_imageviewer || touch kipiplugin_imageviewer.lang
%find_lang kipiplugin_imgurexport || touch kipiplugin_imgurexport.lang
%find_lang kipiplugin_ipodexport || touch kipiplugin_ipodexport.lang
%find_lang kipiplugin_jalbumexport || touch kipiplugin_jalbumexport.lang
%find_lang kipiplugin_jpeglossless || touch kipiplugin_jpeglossless.lang
%find_lang kipiplugin_kioexportimport || touch kipiplugin_kioexportimport.lang
%find_lang kipiplugin_kmlexport || touch kipiplugin_kmlexport.lang
%find_lang kipiplugin_kopete || touch kipiplugin_kopete.lang
%find_lang kipiplugin_metadataedit || touch kipiplugin_metadataedit.lang
%find_lang kipiplugin_panorama || touch kipiplugin_panorama.lang
%find_lang kipiplugin_photolayouteditor || touch kipiplugin_photolayouteditor.lang
%find_lang kipiplugin_piwigoexport || touch kipiplugin_piwigoexport.lang
%find_lang kipiplugin_printimages || touch kipiplugin_printimages.lang
%find_lang kipiplugin_rajceexport || touch kipiplugin_rajceexport.lang
%find_lang kipiplugin_rawconverter || touch kipiplugin_rawconverter.lang
%find_lang kipiplugin_removeredeyes || touch kipiplugin_removeredeyes.lang
%find_lang kipiplugin_sendimages || touch kipiplugin_sendimages.lang
%find_lang kipiplugin_shwup || touch kipiplugin_shwup.lang
%find_lang kipiplugin_smug || touch kipiplugin_smug.lang
%find_lang kipiplugin_timeadjust || touch kipiplugin_timeadjust.lang
%find_lang kipiplugin_videoslideshow || touch kipiplugin_videoslideshow.lang
%find_lang kipiplugin_vkontakte || touch kipiplugin_vkontakte.lang
%find_lang kipiplugin_wikimedia || touch kipiplugin_wikimedia.lang
%find_lang kipiplugin_yandexfotki || touch kipiplugin_yandexfotki.lang
%find_lang libkgeomap || touch libkgeomap.lang

