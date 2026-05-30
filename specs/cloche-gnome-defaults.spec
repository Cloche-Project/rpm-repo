Name:           cloche-gnome-defaults
Version:        44.0
Release:        1%{?dist}
Summary:        GNOME defaults and dconf settings for Cloche
License:        Apache-2.0
URL:            https://github.com/cloche-project/cloche-standard
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       dconf
Requires:       gnome-shell
Requires:       gtk3
Requires:       gtk4
Requires:       gnome-shell-extension-dash-to-panel
Requires:       gnome-shell-extension-dash-to-dock
Requires:       gnome-shell-extension-blur-my-shell
Requires:       gnome-shell-extension-caffeine

%description
System-wide GNOME settings and GTK theme configuration for Cloche.

%prep
%setup -q

%install
install -Dm644 etc/dconf/profile/user \
    %{buildroot}/etc/dconf/profile/user
install -Dm644 etc/dconf/db/local.d/00-cloche-gnome \
    %{buildroot}/etc/dconf/db/local.d/00-cloche-gnome
install -Dm644 usr/share/pixmaps/system-logo-white.png \
    %{buildroot}/usr/share/pixmaps/system-logo-white.png
install -Dm644 etc/xdg/autostart/cloche-templates.desktop \
    %{buildroot}/etc/xdg/autostart/cloche-templates.desktop
install -Dm644 usr/share/backgrounds/cloche/towers-light.png \
    %{buildroot}/usr/share/backgrounds/cloche/towers-light.png
install -Dm644 usr/share/backgrounds/cloche/towers-dark.png \
    %{buildroot}/usr/share/backgrounds/cloche/towers-dark.png
install -Dm644 usr/share/gnome-background-properties/cloche-default.xml \
    %{buildroot}/usr/share/gnome-background-properties/cloche-default.xml
mkdir -p %{buildroot}/etc/skel/.config
cp -r etc/skel/.config/gtk-3.0 %{buildroot}/etc/skel/.config/
cp -r etc/skel/.config/gtk-4.0 %{buildroot}/etc/skel/.config/

%post
dconf update

%postun
dconf update

%files
%config(noreplace) /etc/dconf/profile/user
/etc/dconf/db/local.d/00-cloche-gnome
/usr/share/pixmaps/system-logo-white.png
/etc/xdg/autostart/cloche-templates.desktop
/usr/share/backgrounds/cloche/
/usr/share/gnome-background-properties/cloche-default.xml
%dir /etc/skel/.config/gtk-3.0
/etc/skel/.config/gtk-3.0/
%dir /etc/skel/.config/gtk-4.0
/etc/skel/.config/gtk-4.0/