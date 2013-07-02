Name:		fotowall
Version:	0.9
Release:	2
Summary:	Wallpaper generator
License:	GPLv2
Source0:	Fotowall-%{version}.tar.bz2
Group:		Graphical desktop/KDE
URL:		http://www.kde-apps.org/content/show.php/FotoWall?content=71320
BuildRequires:	qt4-devel >= 4.5.2
BuildRequires:	libv4l-devel
BuildRequires:	desktop-file-utils

%description
FotoWall is a wallpaper generator rendering some of your favorite pictures
in a nice and smooth high resolution composition.

%prep
%setup -q -n Fotowall-%{version}
# for hidden-file-or-dir warning
sed -i -e "s/\.build/build/" %{name}.pro
# Unused file
sed -i -e "/scripts/d" -e "s@man\ \\\@man@" %{name}.pro
# for v4l1 compatibility
sed -i -e 's/linux\/videodev.h/libv4l1-videodev.h/' 3rdparty/videocapture/VideoDevice.h

%build
%qmake_qt4
%make

%install
make install INSTALL_ROOT=%{buildroot}
desktop-file-install --vendor="" \
    --mode 644 \
    --dir %{buildroot}%{_datadir}/applications/ \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean

%files
%doc README.markdown GPL_V2
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*



%changelog
* Fri Mar 02 2012 Andrey Bondrov <abondrov@mandriva.org> 0.9-1mdv2011.0
+ Revision: 781698
- imported package fotowall

