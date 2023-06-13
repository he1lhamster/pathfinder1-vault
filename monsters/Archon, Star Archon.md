---
cssclass: [monsters]
title1: Archon, Star Archon
desc_short: 'This powerful humanoid floats in the air on a nimbus of pearly light.
  He grips a golden starknife in one hand. '
title2: Star Archon
CR: 19
sources:
- name: Bestiary 2
  page: 32
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 204800
alignment: LG
size: Large
type: outsider
subtypes:
- archon
- extraplanar
- good
- lawful
initiative:
  bonus: 8
senses:
  darkvision: 60
  low-light vision: true
  detect evil: true
  true seeing: true
auras:
- name: aura of courage
- name: aura of menace
  DC: 27
- name: magic circle against evil
AC:
  AC: 34
  touch: 11
  flat_footed: 32
  other: +2 deflection vs. evil
  components:
    armor: 9
    dex: 1
    dodge: 1
    natural: 12
    shield: 2
    size: -1
HP:
  HP: 294
  long: 19d10+190
  regeneration: 10
  regeneration_weakness: evil weapons and effects
saves:
  fort: 21
  ref: 17
  will: 15
  other: +4 vs. poison
defensive_abilities:
- explosive rebirth
DR:
- amount: 10
  weakness: evil
immunities:
- electricity
- fire
- charm
- compulsion
- fear
- petrification
SR: 30
speeds:
  base: 40
  other_semicolon: 30 ft. (fly 90 ft.) in armor
  fly: 120
  fly_maneuverability: good
attacks:
  melee:
  - - text: +5 holy starknife +29/+24/+19/+14 (1d6+12/×3)
      entries:
      - - damage: 1d6+12
          crit_multiplier: 3
      attack: +5 holy starknife
      bonus:
      - 29
      - 24
      - 19
      - 14
  special:
  - smite evil 1/day (+6 attack and AC, +29 damage)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: magic circle against evil
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At will
  - name: continual flame
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: message
    source: default
    freq: At will
  - name: sunbeam
    source: default
    freq: At will
    DC: 23
  - name: meteor swarm
    source: default
    freq: 1/day
    DC: 25
  - name: polar ray
    source: default
    freq: 1/day
    DC: 24
  - name: prismatic spray
    source: default
    freq: 1/day
    DC: 23
  - name: sunburst
    source: default
    freq: 1/day
    DC: 24
  sources:
  - name: default
    CL: 19
    concentration: 25
spells:
  entries:
  - name: implosion
    source: Cleric
    level: 9
    DC: 26
  - name: mass heal
    source: Cleric
    level: 9
  - name: miracle
    source: Cleric
    level: 9
  - name: dimensional lock
    source: Cleric
    level: 8
  - name: fire storm
    source: Cleric
    level: 8
    DC: 25
  - name: holy aura
    source: Cleric
    level: 8
    DC: 25
  - name: destruction
    source: Cleric
    level: 7
    count: 2
    DC: 24
  - name: holy word
    source: Cleric
    level: 7
    count: 2
    DC: 24
  - name: resurrection
    source: Cleric
    level: 7
  - name: greater dispel magic
    source: Cleric
    level: 6
  - name: heal
    source: Cleric
    level: 6
  - name: mass cure moderate wounds
    source: Cleric
    level: 6
    count: 3
  - name: break enchantment
    source: Cleric
    level: 5
    count: 2
  - name: breath of life
    source: Cleric
    level: 5
    count: 2
  - name: flame strike
    source: Cleric
    level: 5
    DC: 22
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
    count: 2
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: cure moderate wounds
    source: Cleric
    level: 2
    count: 4
  - name: eagle's splendor
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
  - name: resistance
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  - name: virtue
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 19
    concentration: 26
ability_scores:
  STR: 24
  DEX: 19
  CON: 31
  INT: 20
  WIS: 24
  CHA: 23
BAB: 19
CMB: 27
CMD: 42
feats:
- name: Blind-Fight
- name: Cleave
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Power Attack
- name: Stand Still
skills:
  Diplomacy: 28
  Fly: 20
  Heal: 16
  Intimidate: 28
  Knowledge (arcana): 14
  Knowledge (engineering): 14
  Knowledge (history): 18
  Knowledge (nature): 18
  Knowledge (religion): 24
  Perception: 29
  Sense Motive: 29
  Spellcraft: 24
  Stealth: 14
  Survival: 17
languages:
- Celestial
- Draconic
- Infernal
- truespeech
ecology:
  environment: any (Heaven)
  organization: solitary or pair
  treasure_type: double
  treasure:
  - full plate
  - heavy steel shield
  - +5 holy starknife
special_abilities:
  Explosive Rebirth (Su): When killed, a star archon explodes in a blinding flash
    of energy that deals 50 points of damage (half fire, half holy damage) to anything
    within 100 feet (Reflex DC 29 half). The save DC is Constitution-based. The slain
    archon reincarnates 1d4 rounds later as an advanced shield archon.
  Spells: Star archons cast divine spells as 19th-level clerics. They do not gain
    access to domains or other cleric abilities.
desc_long: Star archons are the tacticians and strategists of Heaven. Gifted with
  insight and powerful magic, they spend much of their time steering long-term plans
  for Heaven's armies and good folk in the world.

---

# Archon, Star Archon
This powerful humanoid floats in the air on a nimbus of pearly light. He grips a golden _[[items/Weapon/Starknife|starknife]]_ in one hand.

**Source** Bestiary 2 pg. 32
**XP** 204,800

LG Large outsider (archon, extraplanar, good, lawful)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/True Seeing|true seeing]]_; Perception +29
**Aura** aura of courage, aura of menace (DC 27), _[[spells/Magic Circle against Evil|magic circle against evil]]_

##### Defense

**AC** 34, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+9 armor, +1 Dex, +1 dodge, +12 natural, +2 _[[spells/Shield|shield]]_, –1 size) (+2 _[[spells/Deflection|deflection]]_ vs. evil)
**hp** 294 (19d10+190); _[[universal monster rules/Regeneration|regeneration]]_ 10 (evil weapons and effects)
**Fort** +21, **Ref** +17, **Will** +15; +4 vs. poison
**Defensive Abilities** explosive rebirth; **DR** 10/evil; **Immune** electricity, fire, charm, compulsion, _[[universal monster rules/Fear|fear]]_, petrification; **SR** 30

##### Offense
**Speed** 40 ft., fly 120 ft. (good); 30 ft. (fly 90 ft.) in armor
**Melee** +5 holy _starknife_ +29/+24/+19/+14 (1d6+12/×3)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** smite evil 1/day (+6 attack and AC, +29 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +25)
Constant—_detect evil_, _magic circle against evil_, _true seeing_
At will—aid, _[[spells/Continual Flame|continual flame]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Message|message]]_, _[[spells/Sunbeam|sunbeam]]_ (DC 23)
1/day—_[[spells/Meteor Swarm|meteor swarm]]_ (DC 25), _[[spells/Polar Ray|polar ray]]_ (DC 24), _[[spells/Prismatic Spray|prismatic spray]]_ (DC 23), _[[spells/Sunburst|sunburst]]_ (DC 24)
**_[[classes/Cleric|Cleric]]_ Spells Prepared **(CL 19th; concentration +26)
9th—_[[spells/Implosion|implosion]]_ (DC 26), mass _[[spells/Heal|heal]]_, _[[spells/Miracle|miracle]]_
8th—_[[spells/Dimensional Lock|dimensional lock]]_, _[[spells/Fire Storm|fire storm]]_ (DC 25), _[[spells/Holy Aura|holy aura]]_ (DC 25)
7th—_[[spells/Destruction|destruction]]_ (2, DC 24), _[[spells/Holy Word|holy word]]_ (2, DC 24), _[[spells/Resurrection|resurrection]]_
6th—greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Heal, Mass|heal, mass]]_ _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (3)
5th—_[[spells/Break Enchantment|break enchantment]]_ (2), _[[spells/Breath Of Life|breath of life]]_ (2), _[[spells/Flame Strike|flame strike]]_ (DC 22)
4th—_[[spells/Cure Critical Wounds|cure critical wounds]]_ (3), _[[spells/Death Ward|death ward]]_, _[[spells/Divine Power|divine power]]_
3rd—_[[spells/Cure Serious Wounds|cure serious wounds]]_ (3), _dispel magic_ (2), _[[spells/Invisibility Purge|invisibility purge]]_
2nd—_cure moderate wounds_ (4), _[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Status|status]]_
1st—_[[spells/Cure Light Wounds|cure light wounds]]_ (4), _[[spells/Divine Favor|divine favor]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 18)
0—_[[spells/Guidance|guidance]]_, _[[universal monster rules/Resistance|resistance]]_, stabilize, _[[spells/Virtue|virtue]]_

##### Statistics
**Str** 24, **Dex** 19, **Con** 31, **Int** 20, **Wis** 24, **Cha** 23
**Base Atk** +19; **CMB** +27; **CMD** 42
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Stand Still|Stand Still]]_
**Skills** Diplomacy +28, Fly +20, _Heal_ +16, Intimidate +28, Knowledge (arcana and engineering) +14, Knowledge (history and nature) +18, Knowledge (religion) +24, Perception +29, Sense Motive +29, Spellcraft +24, Stealth +14, Survival +17
**Languages** Celestial, Draconic, Infernal; truespeech

##### Ecology

**Environment** any (Heaven)
**Organization** solitary or pair
**Treasure** double (_[[items/Armor/Full plate|full plate]]_, _[[items/Shield/Heavy steel shield|heavy steel shield]]_, +5 holy _starknife_)

### Special Abilities

**Explosive Rebirth (Su)** When killed, a star archon explodes in a _[[feats/Blinding Flash|blinding flash]]_ of energy that deals 50 points of damage (half fire, half holy damage) to anything within 100 feet (Reflex DC 29 half). The save DC is Constitution-based. The slain archon reincarnates 1d4 rounds later as an advanced _shield_ archon.
**Spells **Star archons cast divine spells as 19th-level clerics. They do not gain access to domains or other _cleric_ abilities.

##### Description

Star archons are the tacticians and strategists of Heaven. Gifted with insight and powerful magic, they spend much of their time steering long-term plans for Heaven’s armies and good folk in the world.