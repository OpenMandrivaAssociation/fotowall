%define debug_package %{nil}

Name:		fotowall
Version:	1.0
Release:	1
Summary:	Wallpaper generator
License:	GPLv2
Source0:	https://github.com/enricoros/fotowall/releases/download/v%{version}/Fotowall-%{version}-RETRO.tar.bz2
Group:		Graphical desktop/KDE
URL:		https://github.com/enricoros/fotowall
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  libv4l-devel
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qttools
BuildRequires:  qmake5

%description
FotoWall is a wallpaper generator rendering some of your favorite pictures
in a nice and smooth high resolution composition.

%prep
%setup -q -n Fotowall-%{version}-RETRO

sed -i -e "/scripts/d" -e "s@man\ \\\@man@" %{name}.pro
# for v4l1 compatibility
sed -i -e 's/linux\/videodev2.h/libv4l1-videodev.h/' 3rdparty/videocapture/VideoDevice.h

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

desktop-file-install --vendor="" \
  --mode 644 \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%doc GPL_V2 README.markdown
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/man/man?/%{name}.?.*

%changelog
* Fri Mar 02 2012 Andrey Bondrov <abondrov@mandriva.org> 0.9-1mdv2011.0
+ Revision: 781698
- imported package fotowall

