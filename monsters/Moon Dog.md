---
cssclass: [monsters]
title1: Moon Dog
desc_short: This sleek, white-furred hound stands three feet tall at the shoulder.
  It paws resemble hands and its face seems preternaturally wise.
title2: Moon Dog
CR: 9
sources:
- name: Bestiary 5
  page: 174
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 6400
alignment: NG
size: Medium
type: outsider
subtypes:
- extraplanar
- good
initiative:
  bonus: 2
senses:
  darkvision: 120
  detect evil: true
  detect magic: true
  keen senses: true
  scent: true
  see invisibility: true
AC:
  AC: 23
  touch: 13
  flat_footed: 20
  components:
    dex: 2
    dodge: 1
    natural: 10
HP:
  HP: 114
  long: 12d10+48
saves:
  fort: 12
  ref: 10
  will: 9
DR:
- amount: 10
  weakness: evil
immunities:
- fear
SR: 20
speeds:
  base: 50
  or: 30
  or_other: while on two legs
attacks:
  melee:
  - - text: bite +17 (1d6+6 plus trip)
      entries:
      - - damage: 1d6+6
        - effect: trip
      attack: bite
      bonus:
      - 17
  special:
  - bay (DC 19)
  - lunar light
  - sneak attack +6d6
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: dancing lights
    source: default
    freq: At will
  - name: alter self
    source: default
    freq: 3/day
  - name: mirror image
    source: default
    freq: 3/day
  - name: darkness
    source: default
    freq: 1/day
  - name: dispel magic
    source: default
    freq: 1/day
  - name: greater invisibility
    source: default
    freq: 1/day
  - name: greater shadow conjuration
    source: default
    freq: 1/day
    DC: 20
  - name: nondetection
    source: default
    freq: 1/day
  - name: obscuring mist
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 12
    concentration: 15
ability_scores:
  STR: 18
  DEX: 15
  CON: 19
  INT: 15
  WIS: 16
  CHA: 16
BAB: 12
CMB: 16
CMD: 29
CMD_other: 33 vs. trip
feats:
- name: Alertness
- name: Dodge
- name: Iron Will
- name: Mobility
- name: Spring Attack
- name: Weapon Focus (bite)
skills:
  Acrobatics: 17
  Bluff: 17
  Diplomacy: 18
  Knowledge (arcana): 13
  Knowledge (planes): 10
  Perception: 26
  Sense Motive: 22
  Stealth: 17
  Survival: 18
    when tracking by scent: 22
  _racial_mods:
    Perception:
      _: 4
    Survival:
      when tracking by scent: 4
languages:
- Celestial (can't speak)
- telepathy 100 ft.
special_qualities:
- lick
- plane shift
ecology:
  environment: any (Nirvana)
  organization: solitary, pair, or pack (3-11)
  treasure_type: standard
special_abilities:
  Bay (Su): |-
    A moon dog can produce one of the following effects when it howls or barks. Each bay is a sonic effect that functions as the spell of the same name (caster level 12th) except as noted below. The save DCs are Charisma-based. A creature that successfully saves against one of these effects is immune to that bay effect, created by that moon dog, for 24 hours.
    Dismissal: This effect works as per the spell dismissal, except it targets one evil extraplanar creature.
    Fear: As per the spell fear, except this fear affects all evil creatures within 80 feet.
  Keen Senses (Ex): Moon dogs can see twice as far as humans in low-light and normal
    light conditions, and can see without impairment through mist and fog.
  Lick (Sp): 'The lick of a moon dog provides one of the following spell effects (caster
    level 12th) to the target: cure light wounds, neutralize poison, or remove disease.
    Each is usable at will by the moon dog, but can affect a given recipient only
    once per day.'
  Lunar Light (Su): When in dim light, a moon dog can create dappled shadows and pale
    luminous patterns in a 60-foot-radius emanation. This effect causes evil creatures
    to become fascinated (Will DC 19 negates). Good-aligned creatures in this area
    gain the benefits of protection from evil (caster level 12th). Creating this lunar
    light is a full-round action, and the moon dog must concentrate to maintain it.
    The shadow weave remains centered on the moon dog as it moves. Evil creatures
    saving against lunar light cannot be affected again by that moon dog's lunar light
    for 24 hours.
  Plane Shift (Sp): A moon dog can enter the Astral Plane, Ethereal Plane, or Material
    Plane as a standard action, as if using plane shift (caster level 12th).
desc_long: |-
  Moon dogs are extraplanar hounds that live in nomadic packs on Elysium, traveling and hunting planar menaces where they please. Often their hunts will take them to the Astral Plane or the Ethereal Plane, and sometimes to the remote wildernesses of the Material Plane. More often than not, they enter the Material Plane to combat irruptions of evil outsiders plaguing innocent mortals. When they do so, they often ally with powerful celestials, serving amid their forays as scouts and wise council.

  Moon dogs can stand erect and wield weapons if desired, but they prefer the speed and mobility of traveling on all fours. Most moon dogs stand approximately 5 feet tall and weigh about 125 pounds.

---

# Moon Dog
This sleek, white-furred hound stands three feet tall at the shoulder. It paws resemble hands and its face seems preternaturally wise.
**Source** Bestiary 5 pg. 174
**XP** 6,400

NG Medium outsider (extraplanar, good)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Keen Senses|keen senses]]_, _[[universal monster rules/Scent|scent]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +26

##### Defense

**AC** 23, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+2 Dex, +1 _[[feats/Dodge|dodge]]_, +10 natural)
**hp** 114 (12d10+48)
**Fort** +12, **Ref** +10, **Will** +9
**DR** 10/evil; **Immune** _[[universal monster rules/Fear|fear]]_; **SR** 20

##### Offense
**Speed** 50 ft., or 30 ft. (while on two legs)
**Melee** bite +17 (1d6+6 plus _[[universal monster rules/Trip|trip]]_)
**Special Attacks** bay (DC 19), lunar light, sneak attack +6d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +15)
Constant—_detect evil_, _detect magic_, _see invisibility_
At will—_[[spells/Dancing Lights|dancing lights]]_
3/day—_[[spells/Alter Self|alter self]]_, _[[spells/Mirror Image|mirror image]]_
1/day—_[[spells/Darkness|darkness]]_, _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ _[[spells/Invisibility, Greater|invisibility, greater]]_ _[[spells/Shadow Conjuration|shadow conjuration]]_ (DC 20), _[[spells/Nondetection|nondetection]]_, _[[spells/Obscuring Mist|obscuring mist]]_

##### Statistics
**Str** 18, **Dex** 15, **Con** 19, **Int** 15, **Wis** 16, **Cha** 16
**Base Atk** +12; **CMB** +16; **CMD** 29 (33 vs. _trip_)
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Acrobatics +17, Bluff +17, Diplomacy +18, Knowledge (arcana) +13, Knowledge (planes) +10, Perception +26, Sense Motive +22, Stealth +17, Survival +18 (+22 when tracking by _scent_); **Racial Modifiers** +4 Perception, +4 Survival when tracking by _scent_
**Languages** Celestial (can’t speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** lick, _[[spells/Plane Shift|plane shift]]_

##### Ecology

**Environment** any (Nirvana)
**Organization** solitary, pair, or pack (3–11)
**Treasure** standard

### Special Abilities

**Bay (Su)** A _[[monsters/Moon Dog|moon dog]]_ can produce one of the following effects when it howls or barks. Each bay is a sonic effect that functions as the spell of the same name (caster level 12th) except as noted below. The save DCs are Charisma-based. A creature that successfully saves against one of these effects is immune to that bay effect, created by that _moon dog_, for 24 hours.

_[[spells/Dismissal|Dismissal]]_: This effect works as per the spell _dismissal_, except it targets one evil extraplanar creature.

_Fear_: As per the spell _fear_, except this _fear_ affects all evil creatures within 80 feet.

**_Keen Senses_ (Ex)** Moon dogs can see twice as far as humans in low-light and normal light conditions, and can see without impairment through mist and fog.

**Lick (Sp)** The lick of a _moon dog_ provides one of the following spell effects (caster level 12th) to the target: _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Neutralize Poison|neutralize poison]]_, or _[[spells/Remove Disease|remove disease]]_. Each is usable at will by the _moon dog_, but can affect a given recipient only once per day.

**Lunar Light (Su)** When in dim light, a _moon dog_ can create dappled shadows and pale luminous patterns in a 60-foot-radius emanation. This effect causes evil creatures to become _[[conditions/Fascinated|fascinated]]_ (Will DC 19 negates). Good-aligned creatures in this area gain the benefits of _[[spells/Protection From Evil|protection from evil]]_ (caster level 12th). Creating this lunar light is a full-round action, and the _moon dog_ must concentrate to maintain it. The _[[items/Armor Magic Abilities/Shadow|shadow]]_ weave remains centered on the _moon dog_ as it moves. Evil creatures saving against lunar light cannot be affected again by that _moon dog_’s lunar light for 24 hours.

**_Plane Shift_ (Sp)** A _moon dog_ can enter the Astral Plane, Ethereal Plane, or Material Plane as a standard action, as if using _plane shift_ (caster level 12th).

##### Description

Moon dogs are extraplanar hounds that live in nomadic packs on Elysium, traveling and hunting _[[items/Weapon Magic Abilities/Planar|planar]]_ menaces where they please. Often their hunts will take them to the Astral Plane or the Ethereal Plane, and sometimes to the remote wildernesses of the Material Plane. More often than not, they enter the Material Plane to combat irruptions of evil outsiders plaguing innocent mortals. When they do so, they often ally with powerful celestials, serving amid their forays as scouts and wise council.

Moon dogs can stand erect and wield weapons if desired, but they prefer the speed and _mobility_ of traveling on all fours. Most moon dogs stand approximately 5 feet tall and weigh about 125 pounds.