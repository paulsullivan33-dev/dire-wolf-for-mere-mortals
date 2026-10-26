# Connecting Applications

Dire Wolf by itself is a modem with a
terminal. The station most operators
picture — a live map, stations as icons,
messages in a window — is a **client
application** sitting on one of chapter
7's doors, and this short chapter is the
map of that layer: what clients do, how
they attach, and what to check when the
map is empty. It is an outline and is
labelled so: the lab attached ten lines
of Python, not a real client, and real
clients are described from their
documentation, not reviewed.

## What a client adds

- **The map.** Received positions,
  objects and tracks drawn as they
  arrive, with history — the single most
  common reason anyone installs any of
  this.
- **A messaging desk.** APRS messages
  (chapter 3) composed, acknowledged and
  filed, with the patience machinery —
  retries until `ack` — automated.
- **A station book.** What was heard,
  when, by what path: the client's log
  is the station's memory, far richer
  than the modem's scrolling terminal.
- **Composition.** Beacons, objects and
  telemetry shaped in forms instead of
  configuration lines.

## How clients attach

Two doors, two temperaments (chapter 7).
**AGW clients** register a call sign with
Dire Wolf and converse in structured
messages; much Windows and cross-platform
packet software speaks AGW because AGWPE
taught it to. **KISS clients** take the
frames raw and own the whole protocol;
most modern and mobile software speaks
KISS. Names you will meet, characterised
in one line each and not ranked:

- **Xastir** — the long-lived Linux APRS
  client: maps, messaging, decades of
  refinement, speaks both doors.
- **YAAC** — "Yet Another APRS Client":
  Java, cross-platform, map and message
  desk, AGW and KISS.
- **APRSIS32** — the Windows fixture of
  the APRS world, a client and an
  APRS-IS citizen in one.
- **PinPoint APRS** — a Windows tracker
  and map aimed at the moving station.
- **APRSdroid** — the phone in the
  picture: an Android APRS station that
  uses a KISS modem (Bluetooth or TCP)
  as its radio — very often Dire Wolf's
  cousin on a desk, or a small hardware
  modem in a pocket.

Every one of them expects the modem to
be *already right*: call sign set, audio
level honest, channel defined. A client
cannot fix chapter 6.

## The empty-map checklist

When a client shows nothing, the fault
lives at a layer boundary, and each
layer can be proved separately — the
habit this whole guide has practised:

1. **The modem hears.** Dire Wolf's own
   terminal prints packets (or `atest`
   decodes your recording — chapter 8).
   No prints, no client will save you:
   audio or configuration, chapters 5–6.
2. **The door is open.** The startup log
   announced the listeners (transcript
   t07), and the numbers in the client
   match the numbers in the file —
   including when, as in the lab, they
   are not the defaults.
3. **The client attached.** Dire Wolf
   logs attachments in plain words
   ("Attached to KISS TCP client
   application 0"). Silence here means
   the client is knocking elsewhere:
   wrong port, wrong machine, or the
   serial/TCP choice flipped.
4. **Then, and only then,** the client's
   own settings: its call sign, its
   filters, its map.

Check: step 3 is the lab's whole
chapter 7 in one line — if your client's
knock does not produce an "Attached"
line and, for KISS, a received frame in
the debug log, the modem has never met
it, whatever the client's own window
claims.
