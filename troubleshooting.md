# Troubleshooting

The failures this guide's lab actually
met, and the ones the documentation
warns of, each in the form *symptom →
what it meant → the check that proves
it*. Worked from the top: every entry
here is cheaper than the ones below it.

## The program stops at the sound card

**Symptom.** A new configuration, run,
ends with:

```text
Could not open audio device plughw:1,0 for input
Pointless to continue without audio device.
```

**What it meant.** The file parsed —
everything above that line in the output
had already been accepted — and then the
named audio device did not exist. In
the lab, honestly: the machine had no
sound card at all (transcript t05). On
a real station it is the wrong card
number in **ADEVICE**, an interface
unplugged, or another program holding
the device.

**The check.** The messages *above* the
failure: if the parser's sentences are
about your lines, fix lines; if the
first complaint is the device, list the
machine's sound devices by the method
in the project documentation and make
ADEVICE match one that exists.

## Four warnings about the call sign

**Symptom.** A station starts, but its
digipeater never repeats and its beacon
never fires. The banner said:

```text
Config file: MYCALL must be set for channel 0 before beaconing is allowed.
Config file: MYCALL must be set for receive channel 0 before digipeating is allowed.
Config file: MYCALL must be set for transmit channel 0 before digipeating is allowed.
Config file: Beaconing should be configured for channel 0 when digipeating is enabled.
```

**What it meant.** `MYCALL` is unset or
still the placeholder `N0CALL`, and
Dire Wolf has disarmed — deliberately,
in writing — every feature that would
originate or repeat traffic as nobody
(chapters 1 and 5). **The check** is the
line itself: a real call sign in the
file, and the four sentences gone on the
next start. If they persist with a real
call sign present, the file being read
is not the file you edited — `-c` names
the file (chapter 4), and certainty is
cheap.

## It names a word and a line number

**Symptom.**

```text
Config file: Unrecognized command 'MYCAL' on line 10.
```

**What it meant.** Exactly that (the
lab made this one on purpose, with
`sed`, in transcript t06).
Configuration words are a fixed
vocabulary and the parser is literal.
**The check.** Open the file at the
line; compare the word against the
manual's list for that section. Resist
"fixing" it by deleting the line until
you know what the line was for —
chapter 5 exists so that you do.

## A door's port is already taken

**Symptom.** At startup:

```text
Bind failed with error: 98
Address already in use
Some other application is probably already using port 8000.
```

**What it meant.** Something else on
the machine owns the AGW (or KISS) port —
the lab met this when its shared build
machine had another program on 8000,
and moved its doors rather than fight
(transcript t07's configuration,
`null.conf`). **The check.** `ss -tlnp`
(or your platform's equivalent) names
the owner. Either it is a Dire Wolf you
forgot was running — the common case —
or the port is genuinely spoken for, in
which case **AGWPORT/KISSPORT** take new
numbers and every client must be told.

## Heard, but nothing decodes

**Symptom.** The terminal shows audio
activity (or a recording exists) and no
packets — or a fraction of what other
stations report. **What it meant**, in
the order to check: the **level** —
decode lines report it (chapter 6);
near-zero is a whisper, three figures
is a shout or a noise floor like
transcript t04's; the **speed** — a
9600 recording into a 1200 modem (or
the 9600 discriminator pin feeding a
1200 channel) decodes *nothing*, which
looks like silence and is arithmetic;
the **source** — a radio whose squelch
or CTCSS gate never opens on data, or a
speaker output so processed the tones
are porridge. **The check.** `atest`
on a recording (chapter 8): if the file
decodes on the bench, your decoder is
innocent and the wire is guilty; if it
does not, the file's header and the
summary are the confession.

## The client connects and nothing flows

**Symptom.** The map is empty; the
client claims a connection. **What it
meant.** Usually one of chapter 13's
layer boundaries: the client knocked on
a door the file did not open, at a
number the station moved, or it
connected and spoke no protocol — the
lab's bare AGW knock earned the pure
form:

```text
Error getting message header from AGW client application 0.
Tried to read 36 bytes but got only 0.
Closing connection.
```

**The check.** Dire Wolf's log is the
witness: an "Attached" line (chapter 7)
means the knock landed; frames in the
debug log mean the client talks; their
absence, with an attachment, means the
client is set to the wrong door — KISS
framing into the AGW port draws exactly
this blank.

## It transmits nothing, politely

**Symptom.** Beacons configured, frames
queued, the radio never keys. **What it
meant.** The startup said so, once, in
passing: "Note: PTT not configured for
channel 0. (Ignore this if using VOX.)"
— and VOX, if that was the plan, is
asleep, or eats the first syllable of
every transmission (chapter 6). **The
check.** The PTT line in the channel
block (chapter 5), the interface's own
indicators, and a dummy load: never
debug keying into an antenna on a live
frequency when a load and a second
receiver will tell you more.
