Name:           bazaar
Version:        0.8.1
Release:        1%{?dist}
Summary:        App store for GNOME with Flatpak support
License:        GPL-3.0-or-later
URL:            https://github.com/bazaar-org/bazaar
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# glycin, libdex, and blueprint-compiler are GNOME 47+ era packages.
# They ship in Fedora 44 but are absent from EPEL 10 at the time of writing.
# The build will fail on CentOS Stream 10 until those land in EPEL.
BuildRequires:  meson >= 0.60.0
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  pkgconf-pkg-config
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  glib2-devel
BuildRequires:  blueprint-compiler
BuildRequires:  gtk4-devel >= 4.22.1
BuildRequires:  libadwaita-devel >= 1.7.0
BuildRequires:  libdex-devel >= 1.0
BuildRequires:  flatpak-devel >= 1.9
BuildRequires:  appstream-devel >= 1.0
BuildRequires:  libxmlb-devel >= 0.3.4
BuildRequires:  glycin-devel >= 2.0
BuildRequires:  glycin-gtk4-devel >= 2.0
BuildRequires:  libyaml-devel >= 0.2.5
BuildRequires:  libsoup3-devel >= 3.6.0
BuildRequires:  json-glib-devel >= 1.10.0
BuildRequires:  md4c-devel >= 0.5.1
BuildRequires:  gtksourceview5-devel
BuildRequires:  webkitgtk6.0-devel
BuildRequires:  libsecret-devel

Requires:       flatpak
Requires:       hicolor-icon-theme

%description
Bazaar is a modern app store for GNOME focused on discovering and installing
applications from Flatpak remotes, particularly Flathub. It provides rich
application metadata browsing, developer support links, and fast search.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.kolunmi.bazaar.desktop
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/io.github.kolunmi.bazaar.metainfo.xml

%post
/usr/bin/update-desktop-database %{_datadir}/applications &>/dev/null || :
[ -d %{_datadir}/glib-2.0/schemas ] && \
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%postun
/usr/bin/update-desktop-database %{_datadir}/applications &>/dev/null || :
[ -d %{_datadir}/glib-2.0/schemas ] && \
  /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &>/dev/null || :

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/bazaar
%{_datadir}/applications/io.github.kolunmi.bazaar.desktop
%{_datadir}/metainfo/io.github.kolunmi.bazaar.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/io.github.kolunmi.bazaar*
%{?_datadir}/glib-2.0/schemas/io.github.kolunmi.bazaar.gschema.xml
%{?_datadir}/dbus-1/services/io.github.kolunmi.bazaar*.service

%changelog
* %(date "+%a %b %d %Y") Cloche Maintainers <packages@cloche.example> - %{version}-1
- Update to %{version}