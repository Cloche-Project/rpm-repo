Name:           cloche-wallpapers-1
Version:        1.0
Release:        %{?build_timestamp}%{!?build_timestamp:1}%{?dist}
Summary:        Cloche Collection 1 wallpapers
License:        Apache-2.0 AND LicenseRef-Unsplash
URL:            https://github.com/cloche-project/rpm-repo
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Wallpapers for Cloche: the Cloche Default light/dark pair and Cloche Collection 1,
a curated set of Unsplash photographs. See Attribution.md for photo credits.

%prep
%setup -q

%install
install -Dm644 usr/share/backgrounds/cloche/towers-light.webp \
    %{buildroot}/usr/share/backgrounds/cloche/towers-light.webp
install -Dm644 usr/share/backgrounds/cloche/towers-dark.webp \
    %{buildroot}/usr/share/backgrounds/cloche/towers-dark.webp
install -Dm644 usr/share/wallpapers/Cloche-Default/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Default/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Default/contents/images/3840x2025.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Default/contents/images/3840x2025.webp
install -Dm644 usr/share/wallpapers/Cloche-Default/contents/images/3840x2025-dark.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Default/contents/images/3840x2025-dark.webp
install -Dm644 usr/share/gnome-background-properties/cloche-default.xml \
    %{buildroot}/usr/share/gnome-background-properties/cloche-default.xml
install -Dm644 usr/share/gnome-background-properties/cloche-collection-1.xml \
    %{buildroot}/usr/share/gnome-background-properties/cloche-collection-1.xml
install -Dm644 usr/share/licenses/cloche-wallpapers-1/Attribution.md \
    %{buildroot}/usr/share/licenses/cloche-wallpapers-1/Attribution.md
install -Dm644 usr/share/backgrounds/cloche/aaisha-muhammad-rTwJSWNPXZo-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/aaisha-muhammad-rTwJSWNPXZo-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-aaisha-muhammad-rTwJSWNPXZo-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-aaisha-muhammad-rTwJSWNPXZo-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-aaisha-muhammad-rTwJSWNPXZo-unsplash/contents/images/3840x2560.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-aaisha-muhammad-rTwJSWNPXZo-unsplash/contents/images/3840x2560.webp
install -Dm644 usr/share/backgrounds/cloche/andrew-clifton-zEnGSmjyIK4-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/andrew-clifton-zEnGSmjyIK4-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-andrew-clifton-zEnGSmjyIK4-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-andrew-clifton-zEnGSmjyIK4-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-andrew-clifton-zEnGSmjyIK4-unsplash/contents/images/3840x2560.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-andrew-clifton-zEnGSmjyIK4-unsplash/contents/images/3840x2560.webp
install -Dm644 usr/share/backgrounds/cloche/bence-balla-schottner-fdSJH2f7E8I-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/bence-balla-schottner-fdSJH2f7E8I-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-bence-balla-schottner-fdSJH2f7E8I-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-bence-balla-schottner-fdSJH2f7E8I-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-bence-balla-schottner-fdSJH2f7E8I-unsplash/contents/images/3840x2506.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-bence-balla-schottner-fdSJH2f7E8I-unsplash/contents/images/3840x2506.webp
install -Dm644 usr/share/backgrounds/cloche/gabriel-izgi-cfQEO_1S0Rs-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/gabriel-izgi-cfQEO_1S0Rs-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-gabriel-izgi-cfQEO_1S0Rs-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-gabriel-izgi-cfQEO_1S0Rs-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-gabriel-izgi-cfQEO_1S0Rs-unsplash/contents/images/3840x2553.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-gabriel-izgi-cfQEO_1S0Rs-unsplash/contents/images/3840x2553.webp
install -Dm644 usr/share/backgrounds/cloche/gauravdeep-singh-bansal-caC13DIDe9E-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/gauravdeep-singh-bansal-caC13DIDe9E-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-gauravdeep-singh-bansal-caC13DIDe9E-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-gauravdeep-singh-bansal-caC13DIDe9E-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-gauravdeep-singh-bansal-caC13DIDe9E-unsplash/contents/images/3840x2560.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-gauravdeep-singh-bansal-caC13DIDe9E-unsplash/contents/images/3840x2560.webp
install -Dm644 usr/share/backgrounds/cloche/guido-hofmann-DUiRJVNG_Tg-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/guido-hofmann-DUiRJVNG_Tg-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-guido-hofmann-DUiRJVNG_Tg-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-guido-hofmann-DUiRJVNG_Tg-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-guido-hofmann-DUiRJVNG_Tg-unsplash/contents/images/3840x2557.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-guido-hofmann-DUiRJVNG_Tg-unsplash/contents/images/3840x2557.webp
install -Dm644 usr/share/backgrounds/cloche/ishan-seefromthesky-qE1Y8GQKhEk-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/ishan-seefromthesky-qE1Y8GQKhEk-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-ishan-seefromthesky-qE1Y8GQKhEk-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-ishan-seefromthesky-qE1Y8GQKhEk-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-ishan-seefromthesky-qE1Y8GQKhEk-unsplash/contents/images/3840x2160.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-ishan-seefromthesky-qE1Y8GQKhEk-unsplash/contents/images/3840x2160.webp
install -Dm644 usr/share/backgrounds/cloche/jesse-van-vliet-fML2C3AMkeI-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/jesse-van-vliet-fML2C3AMkeI-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-jesse-van-vliet-fML2C3AMkeI-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-jesse-van-vliet-fML2C3AMkeI-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-jesse-van-vliet-fML2C3AMkeI-unsplash/contents/images/3840x2880.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-jesse-van-vliet-fML2C3AMkeI-unsplash/contents/images/3840x2880.webp
install -Dm644 usr/share/backgrounds/cloche/jez-timms-ikgmBELD7PQ-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/jez-timms-ikgmBELD7PQ-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-jez-timms-ikgmBELD7PQ-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-jez-timms-ikgmBELD7PQ-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-jez-timms-ikgmBELD7PQ-unsplash/contents/images/3840x2563.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-jez-timms-ikgmBELD7PQ-unsplash/contents/images/3840x2563.webp
install -Dm644 usr/share/backgrounds/cloche/josefin-WS5yjFjycNY-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/josefin-WS5yjFjycNY-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-josefin-WS5yjFjycNY-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-josefin-WS5yjFjycNY-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-josefin-WS5yjFjycNY-unsplash/contents/images/3840x2560.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-josefin-WS5yjFjycNY-unsplash/contents/images/3840x2560.webp
install -Dm644 usr/share/backgrounds/cloche/karl-hedin-A6mji45ETd4-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/karl-hedin-A6mji45ETd4-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-karl-hedin-A6mji45ETd4-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-karl-hedin-A6mji45ETd4-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-karl-hedin-A6mji45ETd4-unsplash/contents/images/3840x2159.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-karl-hedin-A6mji45ETd4-unsplash/contents/images/3840x2159.webp
install -Dm644 usr/share/backgrounds/cloche/marat-gilyadzinov-MYadhrkenNg-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/marat-gilyadzinov-MYadhrkenNg-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-marat-gilyadzinov-MYadhrkenNg-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-marat-gilyadzinov-MYadhrkenNg-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-marat-gilyadzinov-MYadhrkenNg-unsplash/contents/images/3800x2533.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-marat-gilyadzinov-MYadhrkenNg-unsplash/contents/images/3800x2533.webp
install -Dm644 usr/share/backgrounds/cloche/parrish-freeman-Z0d96glXlTI-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/parrish-freeman-Z0d96glXlTI-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-parrish-freeman-Z0d96glXlTI-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-parrish-freeman-Z0d96glXlTI-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-parrish-freeman-Z0d96glXlTI-unsplash/contents/images/3840x2560.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-parrish-freeman-Z0d96glXlTI-unsplash/contents/images/3840x2560.webp
install -Dm644 usr/share/backgrounds/cloche/phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash/contents/images/3840x2880.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash/contents/images/3840x2880.webp
install -Dm644 usr/share/backgrounds/cloche/simon-MxGPHq_UHaA-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/simon-MxGPHq_UHaA-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-simon-MxGPHq_UHaA-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-simon-MxGPHq_UHaA-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-simon-MxGPHq_UHaA-unsplash/contents/images/3840x2160.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-simon-MxGPHq_UHaA-unsplash/contents/images/3840x2160.webp
install -Dm644 usr/share/backgrounds/cloche/trinity-treft-TXWv_nkLNUQ-unsplash.webp \
    %{buildroot}/usr/share/backgrounds/cloche/trinity-treft-TXWv_nkLNUQ-unsplash.webp
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-trinity-treft-TXWv_nkLNUQ-unsplash/metadata.json \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-trinity-treft-TXWv_nkLNUQ-unsplash/metadata.json
install -Dm644 usr/share/wallpapers/Cloche-Collection-1-trinity-treft-TXWv_nkLNUQ-unsplash/contents/images/3840x2560.webp \
    %{buildroot}/usr/share/wallpapers/Cloche-Collection-1-trinity-treft-TXWv_nkLNUQ-unsplash/contents/images/3840x2560.webp

%files
%dir /usr/share/backgrounds/cloche
/usr/share/backgrounds/cloche/towers-light.webp
/usr/share/backgrounds/cloche/towers-dark.webp
%dir /usr/share/wallpapers/Cloche-Default
%dir /usr/share/wallpapers/Cloche-Default/contents
%dir /usr/share/wallpapers/Cloche-Default/contents/images
/usr/share/wallpapers/Cloche-Default/metadata.json
/usr/share/wallpapers/Cloche-Default/contents/images/3840x2025.webp
/usr/share/wallpapers/Cloche-Default/contents/images/3840x2025-dark.webp
/usr/share/gnome-background-properties/cloche-default.xml
/usr/share/gnome-background-properties/cloche-collection-1.xml
%license /usr/share/licenses/cloche-wallpapers-1/Attribution.md
/usr/share/backgrounds/cloche/aaisha-muhammad-rTwJSWNPXZo-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-aaisha-muhammad-rTwJSWNPXZo-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-aaisha-muhammad-rTwJSWNPXZo-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-aaisha-muhammad-rTwJSWNPXZo-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-aaisha-muhammad-rTwJSWNPXZo-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-aaisha-muhammad-rTwJSWNPXZo-unsplash/contents/images/3840x2560.webp
/usr/share/backgrounds/cloche/andrew-clifton-zEnGSmjyIK4-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-andrew-clifton-zEnGSmjyIK4-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-andrew-clifton-zEnGSmjyIK4-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-andrew-clifton-zEnGSmjyIK4-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-andrew-clifton-zEnGSmjyIK4-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-andrew-clifton-zEnGSmjyIK4-unsplash/contents/images/3840x2560.webp
/usr/share/backgrounds/cloche/bence-balla-schottner-fdSJH2f7E8I-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-bence-balla-schottner-fdSJH2f7E8I-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-bence-balla-schottner-fdSJH2f7E8I-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-bence-balla-schottner-fdSJH2f7E8I-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-bence-balla-schottner-fdSJH2f7E8I-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-bence-balla-schottner-fdSJH2f7E8I-unsplash/contents/images/3840x2506.webp
/usr/share/backgrounds/cloche/gabriel-izgi-cfQEO_1S0Rs-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-gabriel-izgi-cfQEO_1S0Rs-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-gabriel-izgi-cfQEO_1S0Rs-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-gabriel-izgi-cfQEO_1S0Rs-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-gabriel-izgi-cfQEO_1S0Rs-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-gabriel-izgi-cfQEO_1S0Rs-unsplash/contents/images/3840x2553.webp
/usr/share/backgrounds/cloche/gauravdeep-singh-bansal-caC13DIDe9E-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-gauravdeep-singh-bansal-caC13DIDe9E-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-gauravdeep-singh-bansal-caC13DIDe9E-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-gauravdeep-singh-bansal-caC13DIDe9E-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-gauravdeep-singh-bansal-caC13DIDe9E-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-gauravdeep-singh-bansal-caC13DIDe9E-unsplash/contents/images/3840x2560.webp
/usr/share/backgrounds/cloche/guido-hofmann-DUiRJVNG_Tg-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-guido-hofmann-DUiRJVNG_Tg-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-guido-hofmann-DUiRJVNG_Tg-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-guido-hofmann-DUiRJVNG_Tg-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-guido-hofmann-DUiRJVNG_Tg-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-guido-hofmann-DUiRJVNG_Tg-unsplash/contents/images/3840x2557.webp
/usr/share/backgrounds/cloche/ishan-seefromthesky-qE1Y8GQKhEk-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-ishan-seefromthesky-qE1Y8GQKhEk-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-ishan-seefromthesky-qE1Y8GQKhEk-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-ishan-seefromthesky-qE1Y8GQKhEk-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-ishan-seefromthesky-qE1Y8GQKhEk-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-ishan-seefromthesky-qE1Y8GQKhEk-unsplash/contents/images/3840x2160.webp
/usr/share/backgrounds/cloche/jesse-van-vliet-fML2C3AMkeI-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-jesse-van-vliet-fML2C3AMkeI-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-jesse-van-vliet-fML2C3AMkeI-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-jesse-van-vliet-fML2C3AMkeI-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-jesse-van-vliet-fML2C3AMkeI-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-jesse-van-vliet-fML2C3AMkeI-unsplash/contents/images/3840x2880.webp
/usr/share/backgrounds/cloche/jez-timms-ikgmBELD7PQ-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-jez-timms-ikgmBELD7PQ-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-jez-timms-ikgmBELD7PQ-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-jez-timms-ikgmBELD7PQ-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-jez-timms-ikgmBELD7PQ-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-jez-timms-ikgmBELD7PQ-unsplash/contents/images/3840x2563.webp
/usr/share/backgrounds/cloche/josefin-WS5yjFjycNY-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-josefin-WS5yjFjycNY-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-josefin-WS5yjFjycNY-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-josefin-WS5yjFjycNY-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-josefin-WS5yjFjycNY-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-josefin-WS5yjFjycNY-unsplash/contents/images/3840x2560.webp
/usr/share/backgrounds/cloche/karl-hedin-A6mji45ETd4-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-karl-hedin-A6mji45ETd4-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-karl-hedin-A6mji45ETd4-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-karl-hedin-A6mji45ETd4-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-karl-hedin-A6mji45ETd4-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-karl-hedin-A6mji45ETd4-unsplash/contents/images/3840x2159.webp
/usr/share/backgrounds/cloche/marat-gilyadzinov-MYadhrkenNg-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-marat-gilyadzinov-MYadhrkenNg-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-marat-gilyadzinov-MYadhrkenNg-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-marat-gilyadzinov-MYadhrkenNg-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-marat-gilyadzinov-MYadhrkenNg-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-marat-gilyadzinov-MYadhrkenNg-unsplash/contents/images/3800x2533.webp
/usr/share/backgrounds/cloche/parrish-freeman-Z0d96glXlTI-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-parrish-freeman-Z0d96glXlTI-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-parrish-freeman-Z0d96glXlTI-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-parrish-freeman-Z0d96glXlTI-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-parrish-freeman-Z0d96glXlTI-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-parrish-freeman-Z0d96glXlTI-unsplash/contents/images/3840x2560.webp
/usr/share/backgrounds/cloche/phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-phuong-uyen-vo-hoang-mBKmnETdk8M-unsplash/contents/images/3840x2880.webp
/usr/share/backgrounds/cloche/simon-MxGPHq_UHaA-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-simon-MxGPHq_UHaA-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-simon-MxGPHq_UHaA-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-simon-MxGPHq_UHaA-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-simon-MxGPHq_UHaA-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-simon-MxGPHq_UHaA-unsplash/contents/images/3840x2160.webp
/usr/share/backgrounds/cloche/trinity-treft-TXWv_nkLNUQ-unsplash.webp
%dir /usr/share/wallpapers/Cloche-Collection-1-trinity-treft-TXWv_nkLNUQ-unsplash
%dir /usr/share/wallpapers/Cloche-Collection-1-trinity-treft-TXWv_nkLNUQ-unsplash/contents
%dir /usr/share/wallpapers/Cloche-Collection-1-trinity-treft-TXWv_nkLNUQ-unsplash/contents/images
/usr/share/wallpapers/Cloche-Collection-1-trinity-treft-TXWv_nkLNUQ-unsplash/metadata.json
/usr/share/wallpapers/Cloche-Collection-1-trinity-treft-TXWv_nkLNUQ-unsplash/contents/images/3840x2560.webp