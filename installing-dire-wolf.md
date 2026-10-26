# Installing Dire Wolf

Dire Wolf is ordinary open-source
software: C source, a public repository,
and packages in most Linux distributions.
This guide's lab installed the
distribution package on Ubuntu, which is
the route taught first — one command,
and the version your distribution's
maintainers tested together. Building
from source is the alternative when you
need a newer release, and on Windows and
macOS the project's releases page is the
front door. Any route ends at the same
five commands.

## The package install

On a Debian or Ubuntu machine:

```bash
sudo apt install direwolf
dpkg-query -W direwolf
which direwolf gen_packets atest decode_aprs kissutil
```

The lab's check — transcript
`dire-wolf-lab/transcripts/t00-version.txt` —
reads:

```text
$ dpkg-query -W direwolf
direwolf	1.7+dfsg-2build2
$ which direwolf gen_packets atest decode_aprs kissutil
/usr/bin/direwolf
/usr/bin/gen_packets
/usr/bin/atest
/usr/bin/decode_aprs
/usr/bin/kissutil
```

That is the whole verification. If
`which` names all five, the install is
complete: nothing else is needed before
chapter 8's file work, and nothing in
this guide needs a radio plugged in
until chapter 6 starts talking about
one. Fedora and Arch package it under
the same name; the Raspberry Pi OS
package likewise, which is why so many
digipeaters are Pis.

## What the install brings

The package is really a small workshop:

| Command | What it is |
|---|---|
| `direwolf` | The station itself: modem, digipeater, igate (chapter 5) |
| `gen_packets` | Written packets in, packet audio out (chapter 9) |
| `atest` | Packet audio in, decoded packets out — the test bench (chapter 8) |
| `decode_aprs` | One written packet in, a plain-language explanation out (chapter 3) |
| `kissutil` | A small tool for talking to a KISS port and exchanging frames with files (chapter 7) |

Two habits start here. Dire Wolf runs
happily as an **ordinary user** and says
so itself — run it as root and it
complains, repeatedly, that the
privileges are unnecessary risk; the lab
took the hint and ran everything as an
unprivileged account. And Dire Wolf
reads a **configuration file** (chapter
5): run bare, it looks for `direwolf.conf`
in the current directory and then in
your home; `-c` names the file explicitly,
which is what every command in this
guide does, so there is never a doubt
about which station you started.

## Building from source, in outline

The project's repository carries the
source and its build instructions; the
shape is the usual one — install the
compiler and the sound and USB libraries
it lists (`cmake`, ALSA and udev
development files on Debian-likes),
build, install. This route is documented
only here: the lab's package was current
enough, and chapter 5's parser does not
care how the binary arrived. Build only
if your distribution's package is old
enough to miss a feature you need —
versions matter when you read other
people's advice, exactly as the lab's
`t00` transcript exists to pin down:
this guide's outputs are all from
**1.7**, and an option named in a forum
post for 1.5 may have moved.

## The first run (and its honest stop)

Start it against the lab's configuration:

```bash
direwolf -t 0 -c direwolf.conf
```

(`-t 0` turns off the terminal colours,
which is why the lab's transcripts are
clean text.) On the lab machine the run
ends after a few lines — the
configuration is accepted, then the
sound device in it does not exist, and
Dire Wolf declines to continue:
"Pointless to continue without audio
device." That stop is chapter 5's whole
subject, and it is a *success* at this
stage: your install works, your file
parses, and the only missing piece is
hardware you have not connected yet.
