# Disable until libmediawiki gets individual tarball release
%bcond_with wikimedia
%bcond_with vkontakte

%define _disable_lto 1
%define _disable_ld_no_undefined 1

Summary:	A KDE photo management utility
Name:		digikam
Epoch:		2
Version:	5.5.0
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://www.digikam.org
Source0:	http://download.kde.org/stable/digikam/%{name}-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
## upstreamable patches
# doc-translated FTBFS, https://bugs.kde.org/show_bug.cgi?id=377597
Patch100:	digikam-5.5.0-doc_translated.patch
BuildRequires:	doxygen
BuildRequires:	eigen3
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	imagemagick
BuildRequires:	mariadb-server
BuildRequires:	mariadb-devel
BuildRequires:	gomp-devel
BuildRequires:	tiff-devel
BuildRequires:	boost-devel
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
%if %mdvver > 3000000
BuildRequires:	pkgconfig(opencv)
%endif
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(x11)
BuildRequires:	cmake(ECM)
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
BuildRequires:	cmake(Marble)

Requires:	mariadb-common
Requires:	kipi-common
Requires:	kipi-plugins
Requires:	libgphoto-common
Requires:	libkdcraw-common

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
%doc core/AUTHORS core/COPYING core/COPYING.LIB core/NEWS core/README
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
%{_iconsdir}/hicolor/*/apps/expoblending.png
%{_iconsdir}/hicolor/*/*/panorama.*
%{_iconsdir}/*/*/*/albumfolder*.*
%{_iconsdir}/*/*/*/overexposure.*
%{_iconsdir}/*/*/*/tag*.*
%{_iconsdir}/*/*/*/underexposure.*
%{_kde5_datadir}/knotifications5/digikam.notifyrc

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
%{_kde5_datadir}/applications/org.kde.showfoto.desktop
%{_kde5_datadir}/kxmlgui5/showfoto
%{_kde5_datadir}/showfoto
%{_kde5_datadir}/metainfo/org.kde.showfoto.appdata.xml
%{_kde5_iconsdir}/*/*/apps/showfoto.*

#-----------------------------------------------------------------------

%define libdigikamdatabase_major 5.3.0
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

%define libdigikamcore_major 5.3.0
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

%define libkipiplugins_major 5.3.0
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

%define libdigikamgui_major 5.3.0
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

%package -n %{libnamedev}
Summary:	Static libraries and headers for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Provides:	kipi-plugins-devel = %{EVRD}
Obsoletes:	kipi-plugins-devel < 1:2.0.0
Requires:	%libdigikamcore = %{EVRD}
Requires:	%libdigikamgui = %{EVRD}
Requires:	%libdigikamdatabase = %{EVRD}
Requires:	%libkipiplugins = %{EVRD}

%description -n %{libnamedev}
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
Suggests:	kipi-plugins-dlna
Suggests:	kipi-plugins-dropbox

Suggests:	kipi-plugins-facebook
Suggests:	kipi-plugins-flashexport
Suggests:	kipi-plugins-flickr
Suggests:	kipi-plugins-googleservices
Suggests:	kipi-plugins-imageshack
Suggests:	kipi-plugins-imgurexport
Suggests:	kipi-plugins-kmlexport
Suggests:	kipi-plugins-piwigoexport
Suggests:	kipi-plugins-printimages
Suggests:	kipi-plugins-rajceexport
Suggests:	kipi-plugins-remotestorage
Suggests:	kipi-plugins-sendimages
Suggests:	kipi-plugins-smug
%if %{with vkontakte}
Suggests:	kipi-plugins-vkontakte
%else
Obsoletes:	kipi-plugins-vkontakte < %{EVRD}
%endif
%if %{with wikimedia}
Suggests:	kipi-plugins-wikimedia
%else
Obsoletes:	kipi-plugins-wikimedia < %{EVRD}
%endif
Suggests:	kipi-plugins-yandexfotki
Obsoletes:	kipi-plugins-panorama < 5.0.0-0.beta4.2
Obsoletes:	kipi-plugins-expoblending < 5.0.0-0.beta4.2

%rename kipi-plugins-advancedslideshow
%rename kipi-plugins-picasa
%rename kipi-plugins-photivo
%rename kipi-plugins-gpssync
%rename kipi-plugins-acquireimages
%rename kipi-plugins-batchprocess
%rename kipi-plugins-calendar
%rename kipi-plugins-debianscreenshot
%rename kipi-plugins-dlna
%rename kipi-plugins-dngconverter
%rename kipi-plugins-galleryexport
%rename kipi-plugins-htmlexport
%rename kipi-plugins-imageviewer
%rename kipi-plugins-ipodexport
%rename kipi-plugins-jpeglossless
%rename kipi-plugins-kioexportimport
%rename kipi-plugins-metadataedit
%rename kipiplugin-photolayouts-editor
%rename kipi-plugins-rawconverter
%rename kipi-plugins-removeredeyes
%rename kipi-plugins-shwup
%rename kipi-plugins-timeadjust
%rename kipi-plugins-videoslideshow

%description -n kipi-plugins
The library of the KDE Image Plugin Interface.

Libkipi allows image applications to use a plugin architecture
for additional functionality such as: RawConverter, SlideShow, 
ImagesGallery, HTMLExport, PrintAssistant...

%files -n kipi-plugins -f kipi-plugins.lang
%doc extra/kipi-plugins/AUTHORS extra/kipi-plugins/COPYING  extra/kipi-plugins/README extra/kipi-plugins/TODO extra/kipi-plugins/NEWS
%{_kde5_applicationsdir}/kipiplugins.desktop

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
#%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_calendarui.rc
#%{_qt5_plugindir}/kipiplugin_calendar.so
#%{_kde5_services}/kipiplugin_calendar.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-dropbox
Summary:	Dropbox export Kipi Plugin
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-dropbox
A tool to export images to a remote Dropbox web service.

%files -n kipi-plugins-dropbox -f kipiplugin_dropbox.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_dropboxui.rc
%{_qt5_plugindir}/kipiplugin_dropbox.so
%{_kde5_services}/kipiplugin_dropbox.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-dropbox.*

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
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_facebookui.rc
%{_qt5_plugindir}/kipiplugin_facebook.so
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
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_flashexportui.rc
%{_kde5_datadir}/kipiplugin_flashexport
%{_qt5_plugindir}/kipiplugin_flashexport.so
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

%files -n kipi-plugins-flickr -f kipiplugin_flickr.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_flickrui.rc
%{_qt5_plugindir}/kipiplugin_flickr.so
%{_kde5_services}/kipiplugin_flickr.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-flickr.*
%{_kde5_iconsdir}/hicolor/*/apps/kipi-hq.*
%{_kde5_iconsdir}/hicolor/*/apps/kipi-zooomr.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-googleservices
Summary:	Google services export Kipi Plugin
Group:		System/Libraries
Requires:	kipi-common
%rename kipi-plugins-googledrive
%rename kipi-plugins-picasa

%description -n kipi-plugins-googleservices
A tool to export images to a remote services.

%files -n kipi-plugins-googleservices -f kipiplugin_googleservices.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_googleservicesui.rc
%{_qt5_plugindir}/kipiplugin_googleservices.so
%{_kde5_services}/kipiplugin_googleservices.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-googledrive.*
%{_kde5_iconsdir}/hicolor/*/apps/kipi-googlephoto.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-remotestorage
Summary:    Export pictures to or import from a remote directory that is accessible via KIO
Group:      System/Libraries
Requires:   kipi-common

%description -n kipi-plugins-remotestorage
A tool to export pictures to or import from a remote
directory that is accessible via KIO

%files -n kipi-plugins-remotestorage -f kipiplugin_remotestorage.lang
%{_qt5_plugindir}/kipiplugin_remotestorage.so
%{_kde5_datadir}/kservices5/kipiplugin_remotestorage.desktop
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_remotestorageui.rc

#-----------------------------------------------------------------------


%package -n kipi-plugins-imageshack
Summary:	Imageshack Export Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-imageshack
A tool to export images to ImageShack.

%files -n kipi-plugins-imageshack -f kipiplugin_imageshack.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_imageshackui.rc
%{_qt5_plugindir}/kipiplugin_imageshack.so
%{_kde5_services}/kipiplugin_imageshack.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-imageshack.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-imgurexport
Summary:	Imgur Kipi Plugin
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	kipi-common

%description -n kipi-plugins-imgurexport
A tool to export pictures to Imgur.

%files -n kipi-plugins-imgurexport -f kipiplugin_imgur.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_imgurui.rc
%{_qt5_plugindir}/kipiplugin_imgur.so
%{_kde5_services}/kipiplugin_imgur.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-imgur.*

#-----------------------------------------------------------------------

%package -n kipi-plugins-kmlexport
Summary:	Create KML files to present images with coordinates
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-kmlexport
A plugin to create KML files to present images with coordinates.

%files -n kipi-plugins-kmlexport -f kipiplugin_kmlexport.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_kmlexportui.rc
%{_qt5_plugindir}/kipiplugin_kmlexport.so
%{_kde5_services}/kipiplugin_kmlexport.desktop

#-----------------------------------------------------------------------

%package -n kipi-plugins-piwigoexport
Summary:	Piwi Go Export
Group:		System/Libraries
Conflicts:	kipi-plugins < 1:1.8.0-1
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-piwigoexport
A tool to export images to a remote Piwigo.

%files -n kipi-plugins-piwigoexport -f kipiplugin_piwigo.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_piwigoui.rc
%{_qt5_plugindir}/kipiplugin_piwigo.so
%{_kde5_datadir}/kipiplugin_piwigo
%{_kde5_services}/kipiplugin_piwigo.desktop
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
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_printimagesui.rc
%{_qt5_plugindir}/kipiplugin_printimages.so
%{_kde5_services}/kipiplugin_printimages.desktop
%{_kde5_datadir}/kipiplugin_printimages/

#-----------------------------------------------------------------------

%package -n kipi-plugins-rajceexport
Summary:	Rajce.net Exporter
Group:		System/Libraries
Requires:	libkdcraw-common
Requires:	kipi-common

%description -n kipi-plugins-rajceexport
A tool to export images to a remote rajce.net service.

%files -n kipi-plugins-rajceexport -f kipiplugin_rajce.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_rajceui.rc
%{_qt5_plugindir}/kipiplugin_rajce.so
%{_kde5_services}/kipiplugin_rajce.desktop
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
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_sendimagesui.rc
%{_qt5_plugindir}/kipiplugin_sendimages.so 
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
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_smugui.rc
%{_qt5_plugindir}/kipiplugin_smug.so
%{_kde5_services}/kipiplugin_smug.desktop
%{_kde5_iconsdir}/hicolor/*/apps/kipi-smugmug.*

#-----------------------------------------------------------------------
%if %{with vkontakte}
%package -n kipi-plugins-vkontakte
Summary:	VKontakte.ru Exporter
Group:		System/Libraries
Requires:	kipi-common

%description -n kipi-plugins-vkontakte
A tool to export on VKontakte.ru Web service

%files -n kipi-plugins-vkontakte -f kipiplugin_vkontakte.lang
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_vkontakteui.rc
%{_qt5_plugindir}/kipiplugin_vkontakte.so
%{_kde5_services}/kipiplugin_vkontakte.desktop
%endif

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
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_wikimediaui.rc
%{_qt5_plugindir}/kipiplugin_wikimedia.so
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
%{_kde5_datadir}/kxmlgui5/kipi/kipiplugin_yandexfotkiui.rc
%{_qt5_plugindir}/kipiplugin_yandexfotki.so
%{_kde5_services}/kipiplugin_yandexfotki.desktop

#-----------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde5 -G"Unix Makefiles" \
%if %mdvver > 3000000
	-DENABLE_OPENCV3:BOOL=ON \
%else
	-DENABLE_OPENCV3:BOOL=OFF \
%endif
	-DENABLE_MYSQLSUPPORT:BOOL=ON \
	-DENABLE_INTERNALMYSQL:BOOL=OFF \
	-DENABLE_AKONADICONTACTSUPPORT:BOOL=ON \
	-DENABLE_APPSTYLES:BOOL=ON \
	-DENABLE_KFILEMETADATASUPPORT:BOOL=ON \
	-DENABLE_MEDIAPLAYER:BOOL=ON

%make

%install
%makeinstall_std -C build

rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/libkipi.mo

# Plugin not ready for production yet, disabled upstream

rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/kipiplugin_photivointegration.mo
%if %{without wikimedia}
rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/kipiplugin_wikimedia.mo
%endif
%if %{without vkontakte}
rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/kipiplugin_vkontakte.mo
rm -f %{buildroot}%{_kde5_datadir}/locale/*/LC_MESSAGES/libkvkontakte.mo
%endif

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
%find_lang kipiplugin_facebook || touch kipiplugin_facebook.lang
%find_lang kipiplugin_flashexport || touch kipiplugin_flashexport.lang
%find_lang kipiplugin_flickr || touch kipiplugin_flickr.lang
%find_lang kipiplugin_galleryexport || touch kipiplugin_galleryexport.lang
%find_lang kipiplugin_googleservices || touch kipiplugin_googleservices.lang
%find_lang kipiplugin_gpssync || touch kipiplugin_gpssync.lang
%find_lang kipiplugin_htmlexport || touch kipiplugin_htmlexport.lang
%find_lang kipiplugin_imageshack || touch kipiplugin_imageshack.lang
%find_lang kipiplugin_imageviewer || touch kipiplugin_imageviewer.lang
%find_lang kipiplugin_imgur || touch kipiplugin_imgur.lang
%find_lang kipiplugin_ipodexport || touch kipiplugin_ipodexport.lang
%find_lang kipiplugin_jalbumexport || touch kipiplugin_jalbumexport.lang
%find_lang kipiplugin_jpeglossless || touch kipiplugin_jpeglossless.lang
%find_lang kipiplugin_kioexportimport || touch kipiplugin_kioexportimport.lang
%find_lang kipiplugin_kmlexport || touch kipiplugin_kmlexport.lang
%find_lang kipiplugin_kopete || touch kipiplugin_kopete.lang
%find_lang kipiplugin_metadataedit || touch kipiplugin_metadataedit.lang
%find_lang kipiplugin_photolayouteditor || touch kipiplugin_photolayouteditor.lang
%find_lang kipiplugin_piwigo || touch kipiplugin_piwigo.lang
%find_lang kipiplugin_printimages || touch kipiplugin_printimages.lang
%find_lang kipiplugin_rajce || touch kipiplugin_rajce.lang
%find_lang kipiplugin_rawconverter || touch kipiplugin_rawconverter.lang
%find_lang kipiplugin_removeredeyes || touch kipiplugin_removeredeyes.lang
%find_lang kipiplugin_remotestorage || touch kipiplugin_remotestorage.lang
%find_lang kipiplugin_sendimages || touch kipiplugin_sendimages.lang
%find_lang kipiplugin_shwup || touch kipiplugin_shwup.lang
%find_lang kipiplugin_smug || touch kipiplugin_smug.lang
%find_lang kipiplugin_timeadjust || touch kipiplugin_timeadjust.lang
%find_lang kipiplugin_videoslideshow || touch kipiplugin_videoslideshow.lang
%find_lang kipiplugin_vkontakte || touch kipiplugin_vkontakte.lang
%find_lang kipiplugin_wikimedia || touch kipiplugin_wikimedia.lang
%find_lang kipiplugin_yandexfotki || touch kipiplugin_yandexfotki.lang
%find_lang libkgeomap || touch libkgeomap.lang
%find_lang libkvkontakte || touch libkvkontakte.lang
