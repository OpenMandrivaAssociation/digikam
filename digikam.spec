%define revision beta7

%define major      1
%define libname    %mklibname digikam %major
%define libnamedev %mklibname digikam -d
%define oldlibnamedev %mklibname digikam %major -d

Name: digikam
Version: 0.10.0
Release: %mkrel 1.%revision.1
License: GPLv2+
Url: http://www.digikam.org
Group: Graphics
Source0: %{name}-%{version}-%revision.tar.bz2
Source1: digikam.desktop
Source2: showfoto.desktop
Summary:       A KDE photo management utility
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
Requires: kdebase4-runtime
Requires: marble
Requires: qt4-database-plugin-sqlite

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


%if %mdkversion < 200900
%post
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f build/%name.lang
%defattr(-,root,root)
%_kde_bindir/digikam
%_kde_bindir/digikam-camera
%_kde_bindir/digikamthemedesigner
%_kde_bindir/digitaglinktree
%_kde_bindir/showfoto
%_kde_libdir/kde4/*.so
%_kde_appsdir/digikam
%_kde_datadir/kde4/services/*
%_kde_datadir/kde4/servicetypes/digikamimageplugin.desktop
%_kde_mandir/*
%_kde_datadir/applications/kde4/digikam.desktop
%_kde_datadir/applications/kde4/showfoto.desktop
%_kde_appsdir/showfoto
%_kde_datadir/kde4/services/ServiceMenus/*.desktop
%_kde_iconsdir/*/*/*/*
# Conflicts with oxygen-icon-theme which already contains those files 
%exclude %_kde_iconsdir/oxygen/*/*/digikam.*
%exclude %_kde_iconsdir/oxygen/16x16/actions/transform-crop-and-resize.png
%exclude %_kde_iconsdir/oxygen/16x16/actions/view-object-histogram-logarithmic.png
%exclude %_kde_iconsdir/oxygen/22x22/actions/transform-crop-and-resize.png
%exclude %_kde_iconsdir/oxygen/22x22/actions/view-object-histogram-linear.png
%exclude %_kde_iconsdir/oxygen/22x22/actions/view-object-histogram-logarithmic.png
%exclude %_kde_iconsdir/oxygen/32x32/actions/transform-crop-and-resize.png
%exclude %_kde_iconsdir/oxygen/32x32/actions/view-object-histogram-linear.png
%exclude %_kde_iconsdir/oxygen/32x32/actions/view-object-histogram-logarithmic.png
%exclude %_kde_iconsdir/oxygen/48x48/actions/transform-crop-and-resize.png
%exclude %_kde_iconsdir/oxygen/scalable/actions/transform-crop-and-resize.svgz
%exclude %_kde_iconsdir/oxygen/scalable/actions/view-object-histogram-linear.svgz
%exclude %_kde_iconsdir/oxygen/scalable/actions/view-object-histogram-logarithmic.svgz
%exclude %_kde_iconsdir/oxygen/22x22/actions/view-object-histogram-linear.png
%exclude %_kde_iconsdir/oxygen/32x32/actions/view-object-histogram-linear.png
%exclude %_kde_iconsdir/oxygen/scalable/actions/transform-crop-and-resize.svgz
%exclude %_kde_iconsdir/oxygen/scalable/actions/view-object-histogram-linear.svgz
%exclude %_kde_iconsdir/oxygen/scalable/actions/view-object-histogram-logarithmic.svgz


#---------------------------------------------

%define libdigikamdatabase %mklibname digikamdatabase 1

%package -n %libdigikamdatabase
Summary: KDE 4 library
Group: System/Libraries

%description -n %libdigikamdatabase
Librairie File needed by %name

%if %mdkversion < 200900
%post -n %libdigikamdatabase -p /sbin/ldconfig

%postun -n %libdigikamdatabase -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %libdigikamcore -p /sbin/ldconfig

%postun -n %libdigikamcore -p /sbin/ldconfig
%endif

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
%setup -q -n %{name}-%{version}-%{revision}

%build
# (cg) Work around GCC 4.3.1 bug:
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=36439
# Can be removed once this is fixed.
export CXXFLAGS="%optflags -fno-tree-pre"
%cmake_kde4 
%make

%install
cd build
rm -rf %buildroot
%{makeinstall_std}

%find_lang %{name}

# Translation the modified desktop file
cp -f %SOURCE1 %SOURCE2  %buildroot/%_kde_datadir/applications/kde4/

%clean
rm -rf %buildroot
