Name:           cloche-common
Version:        44.0
Release:        %{?build_timestamp}%{!?build_timestamp:1}%{?dist}
Summary:        Core identity and configuration for Cloche
License:        Apache-2.0
URL:            https://github.com/cloche-project/cloche-standard
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       fastfetch
Requires:       distrobox

%description
Base configuration and branding for Cloche, independent of desktop environment.

%prep
%setup -q

%install
install -Dm644 etc/fastfetch/config.jsonc \
    %{buildroot}/etc/fastfetch/config.jsonc
install -Dm755 etc/profile.d/cloche-fetch.sh \
    %{buildroot}/etc/profile.d/cloche-fetch.sh
install -Dm755 etc/profile.d/toolbox.sh \
    %{buildroot}/etc/profile.d/toolbox.sh
install -Dm644 usr/share/cloche/logo.txt \
    %{buildroot}/usr/share/cloche/logo.txt

%post
# 
if [ ! -f /etc/distrobox/distrobox.ini ]; then
    mkdir -p /etc/distrobox
    cp /dev/stdin /etc/distrobox/distrobox.ini << 'EOF'
EOF
fi

%files
/etc/fastfetch/config.jsonc
/etc/profile.d/cloche-fetch.sh
/etc/profile.d/toolbox.sh
/usr/share/cloche/logo.txt