---
cssclass: [monsters]
title1: Archon, Bastion Archon
desc_short: This massive, four-armed figure is protected by thick layers of rocky
  armor. Its face is a shimmering, pulsating globe of holy light.
title2: Bastion Archon
CR: 20
sources:
- name: Planar Adventures
  page: 226
  link: http://paizo.com/products/btpya1am
XP: 307200
alignment: LG
size: Huge
type: outsider
subtypes:
- archon
- extraplanar
- good
- lawful
initiative:
  bonus: 6
senses:
  darkvision: 60
  detect magic: true
  low-light vision: true
  true seeing: true
auras:
- name: aura of menace
  DC: 25
- name: aura of mending
  radius: 40
AC:
  AC: 36
  touch: 14
  flat_footed: 30
  components:
    dex: 6
    natural: 22
    size: -2
HP:
  HP: 350
  long: 20d10+240
  fast_healing: 5
saves:
  fort: 24
  ref: 14
  will: 19
  other: +4 vs. poison
defensive_abilities:
- all-around vision
- entrench
DR:
- amount: 15
  weakness: bludgeoning and evil
immunities:
- electricity
- blindness
- petrification
SR: 31
speeds:
  base: 40
  other_semicolon: air walk
attacks:
  melee:
  - - text: 4 slams +30 (4d6+12/19-20)
      entries:
      - - damage: 4d6+12
          crit_range: 19-20
      count: 4
      attack: slams
      bonus:
      - 30
  special:
  - holy beam
  - rending beam
  - smite evil
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: detect evil
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: daylight
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: sending
    source: default
    freq: At will
  - name: prismatic spray
    source: default
    freq: 3/day
    DC: 22
  - name: sunbeam
    source: default
    freq: 3/day
    DC: 22
  - name: meteor swarm
    source: default
    freq: 1/day
    DC: 24
  - name: polar ray
    source: default
    freq: 1/day
    DC: 23
  - name: sunburst
    source: default
    freq: 1/day
    DC: 23
  sources:
  - name: default
    CL: 20
    concentration: 25
spells:
  entries:
  - name: mass heal
    source: Cleric
    level: 9
  - name: holy aura
    source: Cleric
    level: 8
    DC: 25
  - name: mass cure critical wounds
    source: Cleric
    level: 8
  - name: greater restoration
    source: Cleric
    level: 7
  - name: holy word
    source: Cleric
    level: 7
    DC: 24
  - name: mass cure serious wounds
    source: Cleric
    level: 7
  - name: regenerate
    source: Cleric
    level: 7
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 23
  - name: greater dispel magic
    source: Cleric
    level: 6
  - name: heal
    source: Cleric
    level: 6
  - name: mass cure moderate wounds
    source: Cleric
    level: 6
    count: 2
  - name: break enchantment
    source: Cleric
    level: 5
  - name: breath of life
    source: Cleric
    level: 5
    count: 2
  - name: flame strike
    source: Cleric
    level: 5
    DC: 22
  - name: wall of stone
    source: Cleric
    level: 5
  - name: cure critical wounds
    source: Cleric
    level: 4
    count: 3
  - name: death ward
    source: Cleric
    level: 4
  - name: divine power
    source: Cleric
    level: 4
  - name: cure serious wounds
    source: Cleric
    level: 3
    count: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: searing light
    source: Cleric
    level: 3
  - name: cure moderate wounds
    source: Cleric
    level: 2
    count: 4
  - name: shield other
    source: Cleric
    level: 2
  - name: status
    source: Cleric
    level: 2
  - name: cure light wounds
    source: Cleric
    level: 1
    count: 4
  - name: divine favor
    source: Cleric
    level: 1
  - name: sanctuary
    source: Cleric
    level: 1
    DC: 18
  - name: guidance
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 17
    concentration: 24
ability_scores:
  STR: 34
  DEX: 23
  CON: 35
  INT: 22
  WIS: 25
  CHA: 20
BAB: 20
CMB: 34
CMD: 50
feats:
- name: Cleave
- name: Combat Casting
- name: Combat Expertise
- name: Combat Reflexes
- name: Critical Focus
- name: Improved Critical (slam)
- name: Lightning Reflexes
- name: Power Attack
- name: Staggering Critical
- name: Stand Still
skills:
  Diplomacy: 25
  Heal: 27
  Intimidate: 28
  Knowledge (arcana): 26
  Knowledge (engineering): 26
  Knowledge (geography): 29
  Knowledge (planes): 29
  Knowledge (religion): 26
  Perception: 30
  Sense Motive: 30
  Spellcraft: 29
  Survival: 30
languages:
- Celestial
- Draconic
- Infernal
- truespeech
special_qualities:
- ultimate sacrifice
ecology:
  environment: any (Heaven)
  organization: solitary
  treasure_type: standard
special_abilities:
  Aura of Mending (Su): Good-aligned creatures within 60 feet of a bastion archon
    are bathed in a rejuvenating holy light that grants them fast healing 5 while
    they remain in range. This includes the bastion archon itself.
  Entrench (Ex): If a bastion archon does not move from its location, it becomes entrenched
    until the start of its next turn. While entrenched, it can't be moved from its
    space by combat maneuvers or the push or pull universal monster rules, nor can
    it be tripped.
  Holy Beam (Su): Once every 1d4 rounds as a standard action, a bastion archon can
    unleash a concentrated beam of holy energy from the shining beacon that is its
    face. This beam of light creates a 120-foot line of holy radiance. Each creature
    within this area must succeed at a DC 25 Reflex save to avoid being blinded for
    1d4 rounds. Evil creatures in the area of effect also take 20d6 points of damage
    from the holy beam-this damage comes from sacred energies and cannot be reduced
    by energy resistance, but a creature that succeeds at its Reflex save negates
    the blindness and takes only half damage. The save DC is Charisma-based.
  Rending Beam (Su): A bastion archon that hits a single creature with two of its
    slam attacks can blast the target with a swift pulse of holy light that blinds
    the target for 1 round and deals 5d6 points of damage if the target is an evil
    creature. A target can attempt a DC 25 Reflex save to negate the blindness and
    take half damage. The save DC is Charisma-based.
  Spells: A bastion archon casts divine spells as a 17th-level cleric. It does not
    gain access to domains or other cleric abilities. Its beacon-like face serves
    as its divine focus.
  Ultimate Sacrifice (Su): When a bastion archon is slain by an evil creature, it
    erupts in a 40-foot-radius burst of positive energy that restores 100 hit points
    to good-aligned creatures and consecrates the ground in the area. The area is
    treated as the subject of a hallow spell (CL 20th) with an associated bless spell
    effect for 1 year thereafter.
desc_long: |-
  Though bastion archons are among Heaven's most powerful defenders, their formation results from the intertwining of lesser archons, starting with the least of them all, lantern archons. Rarely, when a group of at least nine lantern archons is turned back by an overwhelming invading force of fiends, the group can use their gestalt ability to form a whirling globe that stands its ground.

  This brave act of defiance usually lasts only half a minute, buying the lantern archons' allies time to escape before the gestalt is overcome. In such dire situations, a nearby shield archon-a combatant of Heaven more suited to serving as a bulwark against tides of evil-can transpose itself with the squad of lantern archons, using teleportation to take their place. But this interaction of abilities has unpredictable outcomes, and rarely, rather than swapping places, the two entities meld in a brilliant flash of light that sends nearby evil outsiders reeling, leaving a crater with a nascent bastion archon lodged in its center. The bastion archon is initially stuck in the ground where it formed, but it retains many of its component creatures' defensive and offensive abilities. If it survives, it eventually pulls together a huge, four-armed body from the surrounding terrain until it is clad in the stone of the Holy Mountain itself, in the process becoming infused with power greater than that of any other archon. A fully formed bastion archon stands 30 feet tall and weighs 15 tons.

  Even after a bastion archon has freed itself from its creation crater, it rarely moves far, preferring to defend the place that was once so nearly overcome by invading forces. Indeed, convincing a bastion archon to abandon its self-selected post is so futile that “trying to budge a bastion” is a common phrase in Heaven for attempting the impossible. However, there have been a few rare instances when a particularly large crusade into Abaddon, the Abyss, or Hell has prompted a bastion archon to serve as a forward base for the forces of Heaven, helping establish a formidable foothold that requires a truly terrible counteroffensive to uproot.

  In battle, a bastion archon is akin to the eye of the storm, standing firm and unmoved by the chaotic melee around it as its allies clash with invading fiends. It provides shelter to Heaven's servants, slamming enemies into dust or holding them aloft just long enough to rend them to shreds with its magnificent beam of holy light. Given the choice between pursuing a retreating evil army or tending to the wounded, a bastion archon almost always prefers the latter, following its indelible instincts to protect and heal.

  The one threat most likely to stir a bastion archon from its typically rigid methodology is a balor, the fiery winged demons that sometimes serve as generals during demonic invasions. Given the opportunity, a bastion archon wades through a vast army of demons in a single-minded effort to get to the strategic head and cut it off, leading to a confrontation that often ends explosively-either when the archon falls or the balor erupts into massive fireball during its death throes.

  Bastion archons hold in reserve an explosive last resort in the event they are felled in battle: an explosion of light that destroys the archon, heals its allies, and consecrates the ground around it. This final sacrifice gives its (likely overwhelmed) allies a last-ditch chance at victory, and the site of a bastion archon's death is often thereafter considered a sacred place of remembrance.

  A particularly unusual bastion archon by the name of Anvil Fist serves in the deepest caverns of the Forgeheart in Heaven, patrolling without end to keep invaders from the Abyss at bay. Anvil Fist is one of the longest-serving of its kind, and it has recently begun to act strangely, wandering into empty tunnels and staying there for days, speaking only in vague aphorisms when questioned. Some worry that Anvil Fist's millennia-long battle against chaotic abominations has begun to destabilize the archon, while others believe its uncharacteristic behaviors are the result of a qlippoth lord's vile machinations. Still others theorize that Anvil Fist may be nearing an apotheosis to something greater, perhaps becoming the first incarnation of an archon of power akin to the mightiest balor lords, infernal dukes, or veranallia azata elders.

---

# Archon, Bastion Archon
This massive, four-armed figure is protected by thick layers of rocky armor. Its face is a shimmering, pulsating globe of holy light.
**Source** _[[items/Weapon Magic Abilities/Planar|Planar]]_ Adventures pg. 226
**XP** 307,200

LG Huge outsider (archon, extraplanar, good, lawful)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +30
**Aura** aura of menace (DC 25), aura of _[[spells/Mending|mending]]_ (40 ft.)

##### Defense

**AC** 36, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+6 Dex, +22 natural, –2 size)
**hp** 350 (20d10+240); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +24, **Ref** +14, **Will** +19; +4 vs. poison
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, entrench; **DR** 15/bludgeoning and evil; **Immune** electricity, blindness, petrification; **SR** 31

##### Offense
**Speed** 40 ft.; _[[spells/Air Walk|air walk]]_
**Melee** 4 slams +30 (4d6+12/19–20)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** holy beam, rending beam, smite evil
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +25)
Constant—_air walk_, _[[spells/Detect Evil|detect evil]]_, _true seeing_
At will—aid, _[[spells/Daylight|daylight]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Sending|sending]]_
3/day—_[[spells/Prismatic Spray|prismatic spray]]_ (DC 22), _[[spells/Sunbeam|sunbeam]]_ (DC 22)
1/day—_[[spells/Meteor Swarm|meteor swarm]]_ (DC 24), _[[spells/Polar Ray|polar ray]]_ (DC 23), _[[spells/Sunburst|sunburst]]_ (DC 23)
**_[[classes/Cleric|Cleric]]_ Spells Prepared **(CL 17th; concentration +24)
9th—mass _[[spells/Heal|heal]]_
8th—_[[spells/Holy Aura|holy aura]]_ (DC 25), mass _[[spells/Cure Critical Wounds|cure critical wounds]]_
7th—greater _[[spells/Restoration|restoration]]_, _[[spells/Holy Word|holy word]]_ (DC 24), mass _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Regenerate|regenerate]]_
6th—_[[spells/Blade Barrier|blade barrier]]_ (DC 23), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Heal, Mass|heal, mass]]_ _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2)
5th—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Breath Of Life|breath of life]]_ (2), _[[spells/Flame Strike|flame strike]]_ (DC 22), _[[spells/Wall Of Stone|wall of stone]]_
4th—_cure critical wounds_ (3), _[[spells/Death Ward|death ward]]_, _[[spells/Divine Power|divine power]]_
3rd—_cure serious wounds_ (3), _dispel magic_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Searing Light|searing light]]_
2nd—_cure moderate wounds_ (4), _[[spells/Shield Other|shield other]]_, _[[spells/Status|status]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (4), _[[spells/Divine Favor|divine favor]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 18)
0—_[[spells/Guidance|guidance]]_, _mending_, _[[universal monster rules/Resistance|resistance]]_, stabilize

##### Statistics
**Str** 34, **Dex** 23, **Con** 35, **Int** 22, **Wis** 25, **Cha** 20
**Base Atk** +20; **CMB** +34; **CMD** 50
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stand Still|Stand Still]]_
**Skills** Diplomacy +25, _Heal_ +27, Intimidate +28, Knowledge (arcana) +26, Knowledge (engineering) +26, Knowledge (geography) +29, Knowledge (planes) +29, Knowledge (religion) +26, Perception +30, Sense Motive +30, Spellcraft +29, Survival +30
**Languages** Celestial, Draconic, Infernal; truespeech
**SQ** ultimate _[[spells/Sacrifice|sacrifice]]_

##### Ecology

**Environment** any (Heaven)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Aura of _Mending_ (Su)** Good-aligned creatures within 60 feet of a _[[items/Armor Magic Abilities/Bastion|bastion]]_ archon are bathed in a rejuvenating holy light that grants them _fast healing_ 5 while they remain in range. This includes the _bastion_ archon itself.

**Entrench (Ex)** If a _bastion_ archon does not move from its location, it becomes entrenched until the start of its next turn. While entrenched, it can’t be moved from its space by combat maneuvers or the push or _[[universal monster rules/Pull|pull]]_ universal monster rules, nor can it be tripped.

**Holy Beam (Su)** Once every 1d4 rounds as a standard action, a _bastion_ archon can unleash a concentrated beam of holy energy from the shining beacon that is its face. This beam of light creates a 120-foot line of holy _[[items/Weapon/Radiance|radiance]]_. Each creature within this area must succeed at a DC 25 Reflex save to avoid being _[[conditions/Blinded|blinded]]_ for 1d4 rounds. Evil creatures in the area of effect also take 20d6 points of damage from the holy beam—this damage comes from _[[items/Weapon Magic Abilities/Sacred|sacred]]_ energies and cannot be reduced by _[[items/Armor Magic Abilities/Energy Resistance|energy resistance]]_, but a creature that succeeds at its Reflex save negates the blindness and takes only half damage. The save DC is Charisma-based.

**Rending Beam (Su)** A _bastion_ archon that hits a single creature with two of its slam attacks can blast the target with a swift pulse of holy light that blinds the target for 1 round and deals 5d6 points of damage if the target is an evil creature. A target can attempt a DC 25 Reflex save to negate the blindness and take half damage. The save DC is Charisma-based.
**Spells** A _bastion_ archon casts divine spells as a 17th-level _cleric_. It does not gain access to domains or other _cleric_ abilities. Its beacon-like face serves as its divine focus.

**Ultimate _Sacrifice_ (Su)** When a _bastion_ archon is slain by an evil creature, it erupts in a 40-foot-radius burst of positive energy that restores 100 hit points to good-aligned creatures and consecrates the ground in the area. The area is treated as the subject of a _[[spells/Hallow|hallow]]_ spell (CL 20th) with an associated _[[spells/Bless|bless]]_ spell effect for 1 year thereafter.

##### Description

Though _bastion_ archons are among Heaven’s most powerful defenders, their formation results from the intertwining of lesser archons, starting with the least of them all, lantern archons. Rarely, when a group of at least nine lantern archons is turned back by an overwhelming invading force of fiends, the group can use their gestalt ability to form a whirling globe that stands its ground.

This brave act of defiance usually lasts only half a minute, buying the lantern archons’ allies time to escape before the gestalt is overcome. In such dire situations, a nearby _[[spells/Shield|shield]]_ archon—a combatant of Heaven more suited to serving as a bulwark against tides of evil—can transpose itself with the squad of lantern archons, using teleportation to take their place. But this interaction of abilities has unpredictable outcomes, and rarely, rather than swapping places, the two entities meld in a brilliant flash of light that sends nearby evil outsiders reeling, leaving a crater with a nascent _bastion_ archon lodged in its center. The _bastion_ archon is initially stuck in the ground where it formed, but it retains many of its component creatures’ defensive and offensive abilities. If it survives, it eventually pulls together a huge, four-armed body from the surrounding terrain until it is clad in the stone of the Holy Mountain itself, in the process becoming infused with power greater than that of any other archon. A fully formed _bastion_ archon stands 30 feet tall and weighs 15 tons.

Even after a _bastion_ archon has freed itself from its creation crater, it rarely moves far, preferring to defend the place that was once so nearly overcome by invading forces. Indeed, convincing a _bastion_ archon to abandon its self-selected post is so futile that “trying to budge a _bastion_” is a common phrase in Heaven for attempting the impossible. However, there have been a few rare instances when a particularly large crusade into Abaddon, the Abyss, or Hell has prompted a _bastion_ archon to serve as a forward base for the forces of Heaven, helping establish a formidable foothold that requires a truly terrible counteroffensive to uproot.

In battle, a _bastion_ archon is akin to the eye of the storm, standing firm and unmoved by the chaotic melee around it as its allies clash with invading fiends. It provides shelter to Heaven’s servants, slamming enemies into dust or holding them aloft just long enough to _[[universal monster rules/Rend|rend]]_ them to shreds with its magnificent beam of holy light. Given the choice between pursuing a retreating evil army or tending to the wounded, a _bastion_ archon almost always prefers the latter, following its indelible instincts to protect and _heal_.

The one threat most likely to stir a _bastion_ archon from its typically rigid methodology is a balor, the fiery winged demons that sometimes serve as generals during demonic invasions. Given the opportunity, a _bastion_ archon wades through a vast army of demons in a single-minded effort to get to the strategic head and cut it off, leading to a confrontation that often ends explosively—either when the archon falls or the balor erupts into massive _[[spells/Fireball|fireball]]_ during its death throes.

_Bastion_ archons hold in reserve an explosive last resort in the event they are felled in battle: an explosion of light that destroys the archon, heals its allies, and consecrates the ground around it. This _[[spells/Final Sacrifice|final sacrifice]]_ gives its (likely overwhelmed) allies a last-ditch chance at victory, and the site of a _bastion_ archon’s death is often thereafter considered a _sacred_ place of remembrance.

A particularly unusual _bastion_ archon by the name of _[[items/Mundane/Anvil|Anvil]]_ Fist serves in the deepest caverns of the Forgeheart in Heaven, patrolling without end to keep invaders from the Abyss at bay. _Anvil_ Fist is one of the longest-serving of its kind, and it has recently begun to act strangely, wandering into empty tunnels and staying there for days, speaking only in vague aphorisms when questioned. Some worry that _Anvil_ Fist’s millennia-long battle against chaotic abominations has begun to destabilize the archon, while others believe its uncharacteristic behaviors are the result of a qlippoth lord’s vile machinations. Still others theorize that _Anvil_ Fist may be nearing an _[[feats/Apotheosis|apotheosis]]_ to something greater, perhaps becoming the first incarnation of an archon of power akin to the mightiest balor lords, infernal dukes, or veranallia azata elders.