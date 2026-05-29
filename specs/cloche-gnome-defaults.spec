Name:           cloche-gnome-defaults
Version:        44.0
Release:        1%{?dist}
Summary:        GNOME defaults and dconf settings for Cloche
License:        Apache 2.0
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


%description
System-wide GNOME settings and GTK theme configuration for Cloche.

%prep
%setup -q

%install
# dconf profile and settings
install -Dm644 etc/dconf/profile/user \
    %{buildroot}/etc/dconf/profile/user
install -Dm644 etc/dconf/db/local.d/00-cloche-gnome \
    %{buildroot}/etc/dconf/db/local.d/00-cloche-gnome

# System logo
install -Dm644 usr/share/pixmaps/system-logo-white.png \
    %{buildroot}/usr/share/pixmaps/system-logo-white.png

# GTK skel configs
for f in etc/skel/.config/gtk-3.0 etc/skel/.config/gtk-4.0; do
    find %{_builddir}/%{name}-%{version}/$f -type f | while read FILE; do
        DEST="${FILE#%{_builddir}/%{name}-%{version}/}"
        install -Dm644 "$FILE" %{buildroot}/"$DEST"
    done
done

# Autostart
install -Dm644 etc/xdg/autostart/cloche-templates.desktop \
    %{buildroot}/etc/xdg/autostart/cloche-templates.desktop

%post
dconf update

%postun
dconf update

%files
/etc/dconf/profile/user
/etc/dconf/db/local.d/00-cloche-gnome
/usr/share/pixmaps/system-logo-white.png
/etc/skel/.config/gtk-3.0/
/etc/skel/.config/gtk-4.0/
/etc/xdg/autostart/cloche-templates.desktop