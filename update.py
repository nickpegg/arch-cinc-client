#!/usr/bin/env python3

"""
Updates the PKGBUILD from a template using the latest version of Cinc, as discovered
from their Omnitruck API.

Requires Python 3.
"""

from urllib.request import urlopen


# CPU architecture that we suport
ARCH = "x86_64"

# The Ubuntu version to track
UBUNTU_VER = "20.04"


def main():
    url = f"https://omnitruck.cinc.sh/stable/cinc/metadata?v=latest&p=ubuntu&pv={UBUNTU_VER}&m={ARCH}"

    print("Fetching attributes from omnitruck.cinc.sh")
    with urlopen(url) as f:
        response = f.read()

    # The response is a bunch of key-value pairs in a single line, alternating key then
    # value. Like: k v k v k v ...
    #
    # This builds a dictionary from these key-value pairs by zipping together the odd
    # indicies of the list with the even indicies.
    parts = response.split()
    attrs = dict(zip(parts[::2], parts[1::2]))

    tmpl = open("PKGBUILD.tmpl").read()

    print("Rendering PKGBUILD")
    with open("PKGBUILD", "w") as f:
        f.write(
            tmpl.format(
                arch=ARCH,
                download_url=attrs[b"url"].decode(),
                sha256sum=attrs[b"sha256"].decode(),
                version=attrs[b"version"].decode(),
            )
        )

    print("Done")

if __name__ == "__main__":
    main()
