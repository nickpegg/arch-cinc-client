Arch package for [Cinc](https://cinc.sh)

This is based on the Ubuntu package of Cinc, much like the
[chef-client](https://aur.archlinux.org/packages/chef-client/) AUR package.

# Installation
```
git clone https://github.com/nickpegg/arch-cinc-client
cd arch-cinc-client
makepkg -si
```

# Updating the Cinc version
Included in this repo is a Python script, `update.py`, which will use Cinc's
Omnitruck API to determine the latest version and generate an appropriate
PKGBUILD.

To update this package to the latest upstream version:
```
python3 update.py
```
