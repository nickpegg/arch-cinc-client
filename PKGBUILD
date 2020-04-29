# Maintainer: Nick Pegg <aur@nickpegg.com>

pkgname=cinc-client
pkgver=16.0.257
pkgrel=1
_ubuntuver=xenial
pkgdesc="A free-as-in-beer distribution of the open source software of Chef Software Inc."
arch=('x86_64')
url="https://downloads.cinc.sh/cinc/"
license=('Apache')
depends=()
conflicts=( chef chef-solo chef-client )
source=("http://packages.cinc.sh/files/stable/cinc/16.0.257/ubuntu/20.04/cinc_16.0.257-1_amd64.deb")
sha256sums=('73434ff3ca310066017f45b9fab4d06ea311dd2621f2badcb30fb4d6f1ebf5fb')

package() {
  cd "$srcdir"
  tar -xf data.tar.xz -C "$pkgdir"

  # link executables
  binaries="chef-apply chef-shell knife chef-client chef-solo ohai"
  binaries="$binaries cinc-apply cinc-shell cinc-client cinc-solo"

  mkdir -p $pkgdir/usr/bin

  for binary in $binaries; do
    ln -s /opt/cinc/bin/$binary $pkgdir/usr/bin/ || error_exit "Cannot link $binary to /usr/bin"
  done
  chown -Rh 0:0 $pkgdir
  chmod 755 $pkgdir/opt
}
