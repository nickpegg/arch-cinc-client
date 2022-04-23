# Maintainer: Nick Pegg <aur@nickpegg.com>

pkgname=cinc-client
pkgver=17.10.0
pkgrel=1
_ubuntuver=xenial
pkgdesc="A free-as-in-beer distribution of the open source software of Chef Software Inc."
arch=('x86_64')
url="https://downloads.cinc.sh/cinc/"
license=('Apache')
depends=()
conflicts=( chef chef-solo chef-client )
source=("http://packages.cinc.sh/files/stable/cinc/17.10.0/ubuntu/20.04/cinc_17.10.0-1_amd64.deb")
sha256sums=('79f3b62e1768f1deb0c505fc44fa5c180b0298605fcf3f6baafa0bb962924d12')

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
