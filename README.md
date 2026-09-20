# Cloche RPM Repository

Custom RPM package sources feeding the Cloche image family. Unlike the `cloche-*` image repos, this
repository does not produce an OCI image — it builds signed RPMs and publishes them as a plain
`createrepo_c` repository on GitHub Pages, which the image recipes `dnf install`/`rpm-ostree install`
from during their build.

---

## Packages

| Package | Summary | Consumed by |
|---------|---------|-------------|
| [`cloche-common`](specs/cloche-common.spec) | Core identity and configuration for Cloche, independent of desktop environment. | `cloche-standard`, `cloche-xe` |
| [`cloche-gnome-defaults`](specs/cloche-gnome-defaults.spec) | GNOME defaults and dconf settings for Cloche (extensions, theming, wallpapers, Red Hat fonts). | `cloche-standard`, `cloche-xe`, `cloche-pro-workstation` (GNOME) |
| [`cloche-kde-defaults`](specs/cloche-kde-defaults.spec) | KDE Plasma defaults and Konsole configuration for Cloche. | `cloche-standard`, `cloche-xe`, `cloche-pro-workstation` (Plasma) |
| [`cloche-wallpapers-1`](specs/cloche-wallpapers-1.spec) | Cloche Collection 1 wallpapers. Pulled in transitively by both defaults packages. | all desktop variants |
| [`bazaar`](specs/bazaar.spec) | Third-party GNOME app store with Flatpak/Flathub support, packaged for convenience. | opt-in |

Sources live under [`sources/<package>/`](sources), spec files under [`specs/`](specs).

---

## Build & Publish

RPMs are built in CI (`.github/workflows/`) whenever `sources/**` or `specs/**` change, matrixed
across `fedora-44` and `centos-stream-10` targets to match the two base images used across the
Cloche family. Built RPMs are GPG-signed, indexed with `createrepo_c`, and pushed to the `gh-pages`
branch, split by target:

* `cloche/<releasever>/<basearch>/` — Fedora-targeted packages (consumed by the rpm-ostree repos)
* `cloche-pro/<releasever>/<basearch>/` — CentOS Stream-targeted packages (consumed by `cloche-pro`/`cloche-pro-workstation`)

## Consuming this repo

Image recipes install the matching `.repo` file and `dnf`/`rpm-ostree install` the desired package.
The two `.repo` definitions are also published verbatim at the root of the `gh-pages` branch:

```bash
# Fedora / rpm-ostree images
curl -o /etc/yum.repos.d/cloche-rpm.repo https://cloche-project.github.io/rpm-repo/cloche-rpm.repo

# CentOS Stream / bootc images (cloche-pro, cloche-pro-workstation)
curl -o /etc/yum.repos.d/cloche-pro-rpm.repo https://cloche-project.github.io/rpm-repo/cloche-pro-rpm.repo
```

Both repos are GPG-verified against `RPM-GPG-KEY-cloche`, published alongside the packages at the
`gh-pages` root. See [`cloche-rpm.repo`](cloche-rpm.repo) / [`cloche-pro-rpm.repo`](cloche-pro-rpm.repo)
for the exact repo definitions, and [`scripts/setup-gpg.sh`](scripts/setup-gpg.sh) for how the signing
key itself is generated.

## License

Package definitions in this repo are licensed Apache-2.0. Individual packages may bundle
differently-licensed upstream sources — see each spec's `License:` field (e.g. `cloche-wallpapers-1`
includes `LicenseRef-Unsplash` assets, `bazaar` is GPL-3.0-or-later upstream).
