Name:           cloche-look-and-feel
Version:        1.0
Release:        %{?build_timestamp}%{!?build_timestamp:1}%{?dist}
Summary:        Cloche's KDE Plasma Look-and-Feel package
License:        Apache-2.0
URL:            https://github.com/cloche-project/rpm-repo
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       plasma-workspace
Requires:       cloche-wallpapers-1

%description
Plasma "Look and Feel" (org.cloche.desktop) package for Cloche. Sets Cloche-Default as the
wallpaper Plasma applies on first login and that plasmalogin/SDDM greeters resolve as the
system default, on top of the existing BreezeDark style/colors/icons/splash Cloche already
ships via cloche-kde-defaults.

%prep
%setup -q

%install
mkdir -p %{buildroot}/usr/share/plasma/look-and-feel/org.cloche.desktop/contents
install -Dm644 usr/share/plasma/look-and-feel/org.cloche.desktop/metadata.json \
    %{buildroot}/usr/share/plasma/look-and-feel/org.cloche.desktop/metadata.json
install -Dm644 usr/share/plasma/look-and-feel/org.cloche.desktop/contents/defaults \
    %{buildroot}/usr/share/plasma/look-and-feel/org.cloche.desktop/contents/defaults

%files
%dir /usr/share/plasma/look-and-feel/org.cloche.desktop
%dir /usr/share/plasma/look-and-feel/org.cloche.desktop/contents
/usr/share/plasma/look-and-feel/org.cloche.desktop/metadata.json
/usr/share/plasma/look-and-feel/org.cloche.desktop/contents/defaults
