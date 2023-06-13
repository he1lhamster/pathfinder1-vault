---
cssclass: [monsters]
title1: Camulatz
desc_short: Vibrant blue and yellow feathers adorn the body of this giant, parrot-like
  bird, but its curved beak and powerful talons are instead adorned with dried blood
  and gore.
title2: Camulatz
CR: 9
sources:
- name: 'Pathfinder #39: The City of Seven Spears'
  page: 80
  link: http://paizo.com/pathfinder/adventurePath/theSerpentsSkull/v5748btpy8ddd
XP: 6400
alignment: CE
size: Large
type: magical beast
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: frightful presence
  radius: 60
  DC: 18
AC:
  AC: 22
  touch: 12
  flat_footed: 19
  components:
    dex: 3
    natural: 10
    size: -1
HP:
  HP: 114
  long: 12d10+48
saves:
  fort: 12
  ref: 11
  will: 6
speeds:
  base: 10
  fly: 80
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +18 (2d6+6/19-20 plus 2d6 bleed)
      entries:
      - - damage: 2d6+6
          crit_range: 19-20
        - damage: 2d6
          type: bleed
      attack: bite
      bonus:
      - 18
    - text: 2 talons +17 (1d6+6)
      entries:
      - - damage: 1d6+6
      count: 2
      attack: talons
      bonus:
      - 17
  special:
  - decapitating strike
  - hypnotic display
  - rend (2 talons, 1d6+9)
space: 10
reach: 5
spell_like_abilities:
  entries:
  - name: entropic shield
    source: default
    freq: 3/day
  - name: ventriloquism
    source: default
    freq: 3/day
    DC: 13
  sources:
  - name: default
    CL: 12
    concentration: 14
ability_scores:
  STR: 23
  DEX: 17
  CON: 18
  INT: 8
  WIS: 15
  CHA: 14
BAB: 12
CMB: 19
CMD: 32
feats:
- name: Bleeding Critical
- name: Critical Focus
- name: Flyby Attack
- name: Improved Critical (bite)
- name: Improved Natural Attack (bite)
- name: Skill Focus (Perception)
skills:
  Bluff: 5
    to mimic sounds: 13
  Fly: 7
  Perception: 14
  _racial_mods:
    Bluff:
      to mimic sounds: 8
languages:
- Abyssal
- Auran
special_qualities:
- sound mimicry
ecology:
  environment: tropical jungles
  organization: solitary, flight (2-5), or aerie (6-12)
  treasure_type: none
special_abilities:
  Decapitating Strike (Ex): On an attack roll of a natural 20 (followed by a successful
    roll to confirm the critical hit) with its bite attack, a camulatz severs its
    opponent's head (if the opponent has one). Most creatures die when their heads
    are cut off. This ability functions as the vorpal weapon special ability.
  Hypnotic Display (Su): As a full-round action, a camulatz may cause its coat of
    feathers to change colors, shifting through a mesmerizing pattern that lures creatures
    to the camulatz's side. All creatures who can see the camulatz (even other camulatz)
    must succeed on a DC 18 Will saving throw or become captivated. A creature that
    successfully saves is not subject to the same camulatz's hypnotic display for
    24 hours. A victim under the effects of the hypnotic display moves toward the
    camulatz using the most direct means available. If this path leads the victim
    into a dangerous area, such as through fire or off a cliff, that creature receives
    a second saving throw to end the effect before moving into peril. Captivated creatures
    can take no actions other than to defend themselves. A victim that is within 5
    feet of the camulatz simply stands and offers no resistance to the camulatz's
    attacks. This effect lasts for 1d6 rounds. Sightless creatures are not affected.
    This is a mind-affecting pattern effect. The save DC is Charisma-based.
  Sound Mimicry (Ex): A camulatz can perfectly imitate certain sounds or the speech
    of any creature it has heard, though this ability does not allow it to speak or
    to understand languages it does not know. The listener must make a Sense Motive
    check opposed by the camulatz's Bluff check to recognize the mimicry, although
    if the listener isn't familiar with the person or the type of creatures mimicked,
    it takes a -8 penalty on its Sense Motive check. The camulatz has a +8 racial
    bonus on its Bluff check to mimic speech or sounds that it has listened to for
    at least 10 minutes. It cannot duplicate the effects of magical abilities (such
    as bardic performance or a harpy's captivating song), though it may be able to
    mimic the sound of those abilities.
desc_long: |-
  Hidden within the high canopy overlooking the jungle floor dwells a race of enormous, vicious, and vibrantly colored birds known as camulatz. Possessing a cruel intelligence, camulatz are vile headhunters and aggressive demon-worshipers, preying on all sentient creatures as sacrifices to their chosen demon lord: Pazuzu, King of the Wind Demons. Camulatz revel in trickery and bloodshed, luring victims into ambushes where the camulatz can indulge their bloodlust and take their victims' heads as grisly trophies.

  The iridescent coloration of a camulatz's feathers assists in mesmerizing unfortunate souls, luring them to the killing ground below the brightly colored bird's aerie. Camulatz also have a special affinity for sounds, naturally mimicking voices and animal noises, while perfecting the magical ability to displace such sounds, making them seem to emanate from other creatures or objects. Camulatz delight in using both their magical ventriloquism and their beautiful plumage to mislead and separate victims before surprising them with diving attacks from above.

  All camulatz possess sharp talons on their feet, capable of rending the most heavily armored foes, but they rely on their cruelly curved beaks to decapitate their victims. The vivid patterns of a camulatz's feathers also provide some protection to the birds, forming a magical field of clashing colors that can deflect ranged attacks.

  A mature camulatz is just over 14 feet in length from its beak to the ends of its tail feathers, but weighs only 300 pounds because of its lightweight bone structure. Each individual camulatz bears its own unique feather coloration, which it can consciously manipulate in set patterns to produce its hypnotic display.

---

# Camulatz
Vibrant blue and yellow feathers adorn the body of this giant, parrot-like bird, but its curved beak and powerful talons are instead adorned with dried blood and gore.
**Source** Pathfinder #39: The City of Seven Spears pg. 80
**XP** 6,400
CE Large magical beast
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (60 ft., DC 18)

##### Defense

**AC** 22, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+3 Dex, +10 natural, -1 size)
**hp** 114 (12d10+48)
**Fort** +12, **Ref** +11, **Will** +6

##### Offense
**Speed** 10 ft., fly 80 ft. (average)
**Melee** bite +18 (2d6+6/19-20 plus 2d6 _[[universal monster rules/Bleed|bleed]]_), 2 talons +17 (1d6+6)
**Space** 10 ft., **Reach** 5 ft.
**Special Attacks** decapitating strike, hypnotic display, _[[universal monster rules/Rend|rend]]_ (2 talons, 1d6+9)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +14)
3/day - _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 13)

##### Statistics
**Str** 23, **Dex** 17, **Con** 18, **Int** 8, **Wis** 15, **Cha** 14
**Base Atk** +12; **CMB** +19; **CMD** 32
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Natural Attack|Improved Natural Attack]]_ (bite), _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Bluff +5 (+13 to _[[monsters/Mimic|mimic]]_ sounds), Fly +7, Perception +14; **Racial Modifiers** +8 Bluff to _mimic_ sounds
**Languages** Abyssal, Auran
**SQ** _[[universal monster rules/Sound Mimicry|sound mimicry]]_

##### Ecology

**Environment** tropical jungles
**Organization** solitary, _[[universal monster rules/Flight|flight]]_ (2-5), or aerie (6-12)
**Treasure** none

### Special Abilities

**Decapitating Strike (Ex)** On an attack roll of a natural 20 (followed by a successful roll to confirm the critical hit) with its bite attack, a _[[monsters/Camulatz|camulatz]]_ severs its opponent’s head (if the opponent has one). Most creatures die when their heads are cut off. This ability functions as the _[[items/Weapon Magic Abilities/Vorpal|vorpal]]_ weapon special ability.

**Hypnotic Display (Su)** As a full-round action, a _camulatz_ may cause its coat of feathers to change colors, shifting through a mesmerizing pattern that lures creatures to the _camulatz_’s side. All creatures who can see the _camulatz_ (even other _camulatz_) must succeed on a DC 18 Will saving throw or become captivated. A creature that successfully saves is not subject to the same _camulatz_’s hypnotic display for 24 hours. A victim under the effects of the hypnotic display moves toward the _camulatz_ using the most direct means available. If this path leads the victim into a dangerous area, such as through fire or off a cliff, that creature receives a second saving throw to end the effect before moving into peril. Captivated creatures can take no actions other than to defend themselves. A victim that is within 5 feet of the _camulatz_ simply stands and offers no _[[universal monster rules/Resistance|resistance]]_ to the _camulatz_’s attacks. This effect lasts for 1d6 rounds. Sightless creatures are not affected. This is a mind-affecting pattern effect. The save DC is Charisma-based.
**_Sound Mimicry_ (Ex)** A _camulatz_ can perfectly imitate certain sounds or the speech of any creature it has heard, though this ability does not allow it to speak or to understand languages it does not know. The listener must make a Sense Motive check opposed by the _camulatz_’s Bluff check to recognize the mimicry, although if the listener isn’t familiar with the person or the type of creatures mimicked, it takes a –8 penalty on its Sense Motive check. The _camulatz_ has a +8 racial bonus on its Bluff check to _mimic_ speech or sounds that it has listened to for at least 10 minutes. It cannot duplicate the effects of magical abilities (such as bardic performance or a _[[monsters/Harpy|harpy]]_’s captivating song), though it may be able to _mimic_ the sound of those abilities.

##### Description

Hidden within the high canopy overlooking the jungle floor dwells a race of enormous, _[[items/Weapon Magic Abilities/Vicious|vicious]]_, and vibrantly colored birds known as _camulatz_. Possessing a _[[items/Weapon Magic Abilities/Cruel|cruel]]_ intelligence, _camulatz_ are vile headhunters and aggressive demon-worshipers, preying on all sentient creatures as sacrifices to their chosen demon lord: Pazuzu, _[[npcs/King|King]]_ of the Wind Demons. _Camulatz_ revel in trickery and bloodshed, luring victims into ambushes where the _camulatz_ can indulge their bloodlust and take their victims’ heads as grisly trophies.

The iridescent coloration of a _camulatz_’s feathers assists in mesmerizing unfortunate souls, luring them to the killing ground below the brightly colored bird’s aerie. _Camulatz_ also have a special affinity for sounds, naturally mimicking voices and animal noises, while perfecting the magical ability to displace such sounds, making them seem to emanate from other creatures or objects. _Camulatz_ delight in using both their magical _ventriloquism_ and their beautiful plumage to _[[spells/Mislead|mislead]]_ and separate victims before surprising them with diving attacks from above.

All _camulatz_ possess sharp talons on their feet, capable of rending the most heavily armored foes, but they rely on their cruelly curved beaks to _[[spells/Decapitate|decapitate]]_ their victims. The vivid patterns of a _camulatz_’s feathers also provide some protection to the birds, forming a magical field of clashing colors that can deflect ranged attacks.

A mature _camulatz_ is just over 14 feet in length from its beak to the ends of its tail feathers, but weighs only 300 pounds because of its lightweight bone structure. Each individual _camulatz_ bears its own unique feather coloration, which it can consciously manipulate in set patterns to produce its hypnotic display.