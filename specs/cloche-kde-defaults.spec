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
Requires:       cloche-wallpapers-1

%description
System-wide KDE Plasma settings and Konsole configuration for Cloche.

%prep
%setup -q

%install
install -Dm644 etc/skel/.config/kactivitymanagerdrc       %{buildroot}/etc/skel/.config/kactivitymanagerdrc
install -Dm644 etc/skel/.config/kdeglobals                %{buildroot}/etc/skel/.config/kdeglobals
install -Dm644 etc/skel/.config/kglobalshortcutsrc        %{buildroot}/etc/skel/.config/kglobalshortcutsrc
install -Dm644 etc/skel/.config/konsolerc                 %{buildroot}/etc/skel/.config/konsolerc
install -Dm644 etc/skel/.config/kscreenlockerrc           %{buildroot}/etc/skel/.config/kscreenlockerrc
install -Dm644 etc/skel/.config/kwinrc                    %{buildroot}/etc/skel/.config/kwinrc
install -Dm644 etc/skel/.config/plasma-org.kde.plasma.desktop-appletsrc \
    %{buildroot}/etc/skel/.config/plasma-org.kde.plasma.desktop-appletsrc
install -Dm644 etc/skel/.local/share/konsole/Main.profile \
    %{buildroot}/etc/skel/.local/share/konsole/Main.profile
install -Dm644 etc/skel/.local/share/konsole/WhiteOnBlack.colorscheme \
    %{buildroot}/etc/skel/.local/share/konsole/WhiteOnBlack.colorscheme

%files
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
/etc/skel/.local/share/konsole/WhiteOnBlack.colorscheme