Name:           cloche-kde-defaults
Version:        44.0
Release:        %{?build_timestamp}%{!?build_timestamp:1}%{?dist}
Summary:        KDE Plasma defaults and configuration for Cloche
License:        Apache-2.0
URL:            https://github.com/cloche-project/cloche-standard
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       plasma-desktop
Requires:       konsole
Requires:       cloche-common

%description
System-wide KDE Plasma settings and Konsole configuration for Cloche.

%prep
%setup -q

%install
mkdir -p %{buildroot}/etc/skel/.config
mkdir -p %{buildroot}/etc/skel/.local/share/konsole
install -Dm644 etc/xdg/kcm-about-distrorc \
    %{buildroot}/etc/xdg/kcm-about-distrorc
cp -r etc/skel/.config/. %{buildroot}/etc/skel/.config/
cp etc/skel/.local/share/konsole/Main.profile \
    %{buildroot}/etc/skel/.local/share/konsole/Main.profile

%files
/etc/xdg/kcm-about-distrorc
%dir /etc/skel/.config
/etc/skel/.config/kactivitymanagerdrc
/etc/skel/.config/kdeglobals
/etc/skel/.config/kglobalshortcutsrc
/etc/skel/.config/konsolerc
/etc/skel/.config/kscreenlockerrc
/etc/skel/.config/kwinrc
/etc/skel/.config/plasma-org.kde.plasma.desktop-appletsrc
%dir /etc/skel/.local/share/konsole
/etc/skel/.local/share/konsole/Main.profile