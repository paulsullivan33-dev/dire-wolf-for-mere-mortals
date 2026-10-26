# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's packets are the lab talking to itself, off the air.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 15 names what the tool
   cannot do: it is not a radio and cannot fix bad audio, a
   general-purpose computer is not an appliance, the doors
   accept whatever a local program hands them, and running a
   digipeater or igate for strangers carries duties software
   cannot discharge for you.
8. **The licence rule is in the text, early.** Chapter 1 and
   the README state it plainly — *transmit only with a
   licence, under your own call sign* — before any procedure
   depends on it, and chapter 11 adds the igate half: what
   your station forwards to the internet is yours, in every
   sense that matters.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox with
no radio, no sound card and no amateur licence exercised in it.
Dire Wolf **1.7** (distribution package 1.7+dfsg-2build2) was
installed with the system package manager. Every run was made
as an unprivileged user, off the air: the audio is generated
files, and the one full program start used ALSA's **null**
device — a software sound card that discards what it is given
and hears only silence. All files live in `dire-wolf-lab/`;
transcripts are in `dire-wolf-lab/transcripts/`.

Run for real, with transcripts as evidence:

- Install and inventory: the package version and the five
  companion tools on the path — `direwolf`, `gen_packets`,
  `atest`, `decode_aprs`, `kissutil` (t00).
- Six written APRS packets (position, second position, object,
  message, status, telemetry — all fictional, all under the
  placeholder N0CALL) turned into 4.7 seconds of 1200-baud
  audio by `gen_packets` (t01), and the WAV kept in the lab.
- That audio decoded by `atest`: 6 of 6 packets, audio level
  reported as 50 on each (t02).
- The same six lines explained field by field by
  `decode_aprs` (t03).
- Twelve packets generated with rising noise by
  `gen_packets -n`: 9 decoded, 3 lost — the decoder's honest
  limit, in numbers (t04).
- The real program run against the lab configuration: the
  file read and checked, four configuration messages (the
  placeholder call sign disables beaconing and digipeating,
  in the program's own words), then the stop at the missing
  audio device (t05). A one-letter typo variant shows the
  parser naming the offending line (t06).
- A full start against the null device: channel summary,
  both doors announced, a KISS frame sent by the lab's
  `knock.py` and shown in Dire Wolf's own hex dump as it is
  queued for transmission, and an AGW connection attached —
  then closed by Dire Wolf when no AGW header followed,
  the 36-byte header named in its error (t07).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- Everything involving a radio: cables and interfaces, PTT
  wiring and methods, real audio levels on real signals, and
  all transmitting. The level readings in chapter 6 are from
  generated files, and the chapter says so.
- The digipeater in operation. Its rule in the lab
  configuration was accepted by the parser (t05), and Dire
  Wolf refused to arm it under the placeholder call sign —
  but no packet was ever repeated: there was no radio and
  nothing to repeat.
- The igate in operation. Chapter 11's configuration lines
  follow the project's examples; no connection to the
  APRS-IS was made, no passcode was used, and nothing was
  forwarded in either direction.
- The application programs of chapter 13 and the neighbours
  of chapter 14 are characterised, not benchmarked; the
  lab drove Dire Wolf's doors with ten lines of Python, not
  with a real client.
- FX.25 and IL2P, smart beaconing, GPS input and APRStt are
  described in outline from the documentation; the lab
  worked at plain AX.25, 1200 baud.

Fixtures are this guide's own and deliberately generic: an
invented hilltop called Bramble Hill, an invented rover, a
position over open farmland that is nobody's station and
nobody's home, and the placeholder call sign N0CALL, which
the guide explains must be replaced by the reader's own
before any of this touches a radio. No example is modelled
on any real person, station, network or organisation, and
nothing was transmitted at any point: the lab's loudest
moment was a WAV file.
