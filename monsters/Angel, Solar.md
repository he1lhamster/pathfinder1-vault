---
cssclass: [monsters]
title1: Angel, Solar
desc_short: This towering humanoid creature has shining topaz eyes, metallic skin,
  and three pairs of white wings.
title2: Solar
CR: 23
sources:
- name: Pathfinder RPG Bestiary
  page: 12
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 819200
alignment: NG
size: Large
type: outsider
subtypes:
- angel
- extraplanar
- good
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
  detect evil: true
  detect snares and pits: true
  true seeing: true
auras:
- name: protective aura
AC:
  AC: 44
  touch: 11
  flat_footed: 42
  components:
    armor: 14
    dex: 1
    dodge: 1
    natural: 19
    size: -1
    deflection vs. evil: 4
HP:
  HP: 363
  long: 22d10+242
  regeneration: 15
  regeneration_weakness: evil artifacts, effects, and spells
saves:
  fort: 25
  ref: 14
  will: 23
  other: +4 vs. poison, +4 resistance vs. evil
DR:
- amount: 15
  weakness: epic and evil
immunities:
- acid
- cold
- petrification
resistances:
  electricity: 10
  fire: 10
SR: 34
speeds:
  base: 50
  other_semicolon: 35 ft., fly 100 ft. (good) in armor
  fly: 150
  fly_maneuverability: good
attacks:
  melee:
  - - text: +5 dancing greatsword +35/+30/+25/+20 (3d6+18)
      entries:
      - - damage: 3d6+18
      attack: +5 dancing greatsword
      bonus:
      - 35
      - 30
      - 25
      - 20
  - - text: slam +30 (2d8+13)
      entries:
      - - damage: 2d8+13
      attack: slam
      bonus:
      - 30
  ranged:
  - - text: +5 composite longbow (+9 Str bonus) +31/+26/+21/+16 (2d6+14 plus slaying
        arrow)
      entries:
      - - damage: 2d6+14
        - effect: slaying arrow
      attack: +5 composite longbow (+9 Str bonus)
      bonus:
      - 31
      - 26
      - 21
      - 16
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: detect snares and pits
    source: default
    freq: Constant
  - name: discern lies
    source: default
    freq: Constant
    DC: 21
  - name: true seeing
    source: default
    freq: Constant
  - name: aid
    source: default
    freq: At Will
  - name: animate objects
    source: default
    freq: At Will
  - name: commune
    source: default
    freq: At Will
  - name: continual flame
    source: default
    freq: At Will
  - name: dimensional anchor
    source: default
    freq: At Will
  - name: greater dispel magic
    source: default
    freq: At Will
  - name: holy smite
    source: default
    freq: At Will
    DC: 21
  - name: imprisonment
    source: default
    freq: At Will
    DC: 26
  - name: invisibility
    source: default
    freq: At Will
    other: self only
  - name: lesser restoration
    source: default
    freq: At Will
  - name: remove curse
    source: default
    freq: At Will
  - name: remove disease
    source: default
    freq: At Will
  - name: remove fear
    source: default
    freq: At Will
  - name: resist energy
    source: default
    freq: At Will
  - name: summon monster VII
    source: default
    freq: At Will
  - name: speak with dead
    source: default
    freq: At Will
    DC: 20
  - name: waves of fatigue
    source: default
    freq: At Will
  - name: blade barrier
    source: default
    freq: 3/day
    DC: 23
  - name: earthquake
    source: default
    freq: 3/day
    DC: 25
  - name: heal
    source: default
    freq: 3/day
  - name: mass charm monster
    source: default
    freq: 3/day
    DC: 25
  - name: permanency
    source: default
    freq: 3/day
  - name: resurrection
    source: default
    freq: 3/day
  - name: waves of exhaustion
    source: default
    freq: 3/day
  - name: greater restoration
    source: default
    freq: 1/day
  - name: power word blind
    source: default
    freq: 1/day
  - name: power word kill
    source: default
    freq: 1/day
  - name: power word stun
    source: default
    freq: 1/day
  - name: prismatic spray
    source: default
    freq: 1/day
    DC: 24
  - name: wish
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
spells:
  entries:
  - name: etherealness
    source: '?'
    level: 9
  - name: mass heal
    source: '?'
    level: 9
  - name: miracle
    source: '?'
    level: 9
  - name: storm of vengeance
    source: '?'
    level: 9
    DC: 27
  - name: fire storm
    source: '?'
    level: 8
    DC: 26
  - name: holy aura
    source: '?'
    level: 8
    count: 2
    DC: 26
  - name: mass cure critical wounds
    source: '?'
    level: 8
    count: 2
  - name: destruction
    source: '?'
    level: 7
    DC: 25
  - name: dictum
    source: '?'
    level: 7
    DC: 25
  - name: ethereal jaunt
    source: '?'
    level: 7
  - name: holy word
    source: '?'
    level: 7
    DC: 25
  - name: regenerate
    source: '?'
    level: 7
  - name: banishment
    source: '?'
    level: 6
    DC: 24
  - name: heroes' feast
    source: '?'
    level: 6
  - name: mass cure moderate wounds
    source: '?'
    level: 6
  - name: undeath to death
    source: '?'
    level: 6
    DC: 24
  - name: word of recall
    source: '?'
    level: 6
  - name: break enchantment
    source: '?'
    level: 5
  - name: breath of life
    source: '?'
    level: 5
  - name: dispel evil
    source: '?'
    level: 5
    DC: 23
  - name: plane shift
    source: '?'
    level: 5
    DC: 23
  - name: righteous might
    source: '?'
    level: 5
  - name: symbol of sleep
    source: '?'
    level: 5
    DC: 23
  - name: cure critical wounds
    source: '?'
    level: 4
    count: 3
  - name: death ward
    source: '?'
    level: 4
  - name: dismissal
    source: '?'
    level: 4
    DC: 22
  - name: neutralize poison
    source: '?'
    level: 4
    count: 2
    DC: 22
  - name: cure serious wounds
    source: '?'
    level: 3
  - name: daylight
    source: '?'
    level: 3
  - name: invisibility purge
    source: '?'
    level: 3
  - name: magic circle against evil
    source: '?'
    level: 3
  - name: prayer
    source: '?'
    level: 3
  - name: protection from energy
    source: '?'
    level: 3
  - name: wind wall
    source: '?'
    level: 3
  - name: align weapon
    source: '?'
    level: 2
  - name: bear's endurance
    source: '?'
    level: 2
  - name: bull's strength
    source: '?'
    level: 2
  - name: consecrate
    source: '?'
    level: 2
  - name: cure moderate wounds
    source: '?'
    level: 2
    count: 2
  - name: eagle's splendor
    source: '?'
    level: 2
  - name: bless
    source: '?'
    level: 1
  - name: cure light wounds
    source: '?'
    level: 1
    count: 3
  - name: divine favor
    source: '?'
    level: 1
  - name: entropic shield
    source: '?'
    level: 1
  - name: shield of faith
    source: '?'
    level: 1
  - name: detect magic
    source: '?'
    level: 0
  - name: purify food and drink
    source: '?'
    level: 0
  - name: stabilize
    source: '?'
    level: 0
  - name: virtue
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: prepared
    CL: 20
    slots:
      0: at-will
ability_scores:
  STR: 28
  DEX: 20
  CON: 30
  INT: 23
  WIS: 27
  CHA: 25
BAB: 22
CMB: 32
CMD: 47
feats:
- name: Cleave
- name: Deadly Aim
- name: Dodge
- name: Great Fortitude
- name: Improved Initiative
- name: Improved Sunder
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Power Attack
- name: Toughness
skills:
  Craft (any one): 31
  Diplomacy: 32
  Fly: 32
  Knowledge (history): 31
  Knowledge (nature): 31
  Knowledge (planes): 31
  Knowledge (religion): 31
  Perception: 33
  Sense Motive: 33
  Spellcraft: 31
  Stealth: 21
  Survival: 31
languages:
- Celestial
- Draconic
- Infernal
- truespeech
special_qualities:
- change shape (alter self)
ecology:
  environment: any good-aligned plane
  organization: solitary or pair
  treasure_type: double
  treasure:
  - +5 full plate
  - +5 dancing greatsword
  - +5 composite longbow [+9 Str bonus]
special_abilities:
  Spells: Solars can cast divine spells as 20th-level clerics. They do not gain access
    to domains or other cleric abilities.
  Slaying Arrow (Su): A solar's bow needs no ammunition, and automatically creates
    a slaying arrow of the solar's choice when drawn.
desc_long: |-
  Solars are the greatest type of angel, usually serving at the right hand of a deity or championing a cause that benefits an entire world or plane. A typical solar looks roughly human, though some physically resemble other humanoid races and a rare few have even more unusual forms. A solar stands about 9 feet tall and weighs about 500 pounds, with a strong, commanding voice that is impossible to ignore. Most have silvery or golden skin.

  Blessed with an array of magical powers and the spellcasting abilities of the most powerful clerics, solars are powerful opponents capable of single-handedly slaying mighty evils. They are the greatest trackers among the celestials, the most masterful of which are said to be able to track the days-old wake of a pit fiend flying through the Astral Plane. Some take on the mantle of monster-slayers and hunt powerful fiends and undead such as devourers, night hags, night shades, and pit fiends, even making forays into the evil planes and the Negative Energy Plane to destroy these creatures at their source before they can bring harm to mortals. A few very old solars have succeeded at this task and bear slayer-names of dread creatures that are now extinct by the solar's hand.

  Solars accept roles as guardians, usually of fundamental supernatural concepts, or objects or creatures of great importance. On one world, a group of solars patrols the energy conduits of the sun, alert for any attempts by evil races such as drow to snuff out the light and bring eternal darkness. On another, seven solars stand watch over seven mystical chains keeping evil gods bound within a prison demiplane. On yet another, a solar with a flaming sword stands watch over the original mortal paradise so that no creature may enter.

  In worlds where the gods cannot take physical form, they send solars to be their prophets and gurus (often pretending to be mortals), laying the foundation for cults that grow to become great religions. Likewise, in worlds oppressed by evil, solars are the secret priests who bring hope to the downtrodden, or in some cases allow themselves to be martyred so that their holy essence can explode outward to land and grow in the hearts of great heroes-to-be.

  Though they are not gods, the solars' power approaches that of demigods, and they often have an advisory role for younger or weaker deities. In some polytheistic faiths, mortals worship one or more solars as aspects or near-equal servants of the true deities-never without the deity's approval-or consider notable solars to be offspring, consorts, lovers, or spouses of true deities (which they may be, depending on the deity).

  Unlike other angels, most solars are created from an amalgam of good souls and raw divine energy to directly serve the gods, but an increasing number of these powerful angels have been “promoted” to their existence as solars from lesser creatures like planetars or devas. A few rare and powerful good souls ascend directly to the status of solar. The oldest solars predate mortality and are among the gods' first creations. These strange solars are paragons of their kind and have little direct interaction with mortals, focusing on the protection or destruction of abstract concepts such as gravity, dark matter, entropy, and primordial evil.

  Solars who spend a long time in the Material Plane, especially those in the guise of mortals, are sometimes the source of half-celestial or aasimar bloodlines in mortal families, due either to romantic dalliances or simply the mortals' proximity to celestial energy. Actual offspring are rare, and when they occur, it is always a mortal mother that bears the child-while solars can appear as either sex, the gods have not granted them the capacity for pregnancy or motherhood. Indeed, this fundamental truth is often what drives a solar to seek out a mortal lover. Since begetting a child upon a mortal is generally frowned upon by other solars, a solar father rarely interacts directly with the fate of his lover or child, so as to avoid bringing shame upon himself or his responsibilities. Yet such solars still watch over their progeny from afar, and in times of peril, they might even be moved to intercede to aid one of their endangered children, albiet in subtle and mysterious ways.

  All angels respect the power and wisdom of solars, and though these mightiest of angels usually work alone, they sometimes command multiple armies led by planetars, acting as great field marshals for massive incursions against the legions of Hell or the hordes of the Abyss.

---

# Angel, Solar
This towering humanoid creature has shining topaz eyes, metallic skin, and three pairs of white wings.
**Source** Pathfinder RPG Bestiary pg. 12
**XP** 819,200

NG Large outsider (angel, extraplanar, good)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Snares and Pits|detect snares and pits]]_, _[[spells/True Seeing|true seeing]]_; Perception +33
**Aura** protective aura

##### Defense

**AC** 44, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 42 (+14 armor, +1 Dex, +1 dodge, +19 natural, –1 size; +4 _[[spells/Deflection|deflection]]_ vs. evil)
**hp** 363 (22d10+242); _[[universal monster rules/Regeneration|regeneration]]_ 15 (evil artifacts, effects, and spells)
**Fort** +25, **Ref** +14, **Will** +23; +4 vs. poison, +4 _[[universal monster rules/Resistance|resistance]]_ vs. evil
**DR** 15/epic and evil; **Immune** acid, cold, petrification; **Resist** electricity 10, fire 10; **SR** 34

##### Offense
**Speed** 50 ft., fly 150 ft. (good); 35 ft., fly 100 ft. (good) in armor
**Melee** +5 _[[items/Weapon Magic Abilities/Dancing|dancing]]_ _[[items/Weapon/Greatsword|greatsword]]_ +35/+30/+25/+20 (3d6+18) or slam +30 (2d8+13)
**Ranged** +5 _[[items/Weapon/Composite longbow|composite longbow]]_ (+9 Str bonus) +31/+26/+21/+16 (2d6+14 plus slaying arrow)
**Space** 10 ft., **Reach** 10 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th)
Constant—_detect evil_, _detect snares and pits_, _[[spells/Discern Lies|discern lies]]_ (DC 21), _true seeing_
At Will—aid, _[[spells/Animate Objects|animate objects]]_, _[[spells/Commune|commune]]_, _[[spells/Continual Flame|continual flame]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Holy Smite|holy smite]]_ (DC 21), _[[spells/Imprisonment|imprisonment]]_ (DC 26), _[[spells/Invisibility|invisibility]]_ (self only), lesser _[[spells/Restoration|restoration]]_, _[[spells/Remove Curse|remove curse]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Summon Monster VII|summon monster VII]]_, _[[spells/Speak with Dead|speak with dead]]_ (DC 20), _[[spells/Waves of Fatigue|waves of fatigue]]_
3/day—_[[spells/Blade Barrier|blade barrier]]_ (DC 23), _[[spells/Earthquake|earthquake]]_ (DC 25), _[[spells/Heal, Mass|heal, mass]]_ _[[spells/Charm Monster|charm monster]]_ (DC 25), _[[spells/Permanency|permanency]]_, _[[spells/Resurrection|resurrection]]_, _[[spells/Waves of Exhaustion|waves of exhaustion]]_
1/day—greater _restoration_, _[[spells/Power Word Blind|power word blind]]_, _[[spells/Power Word Kill|power word kill]]_, _[[spells/Power Word Stun|power word stun]]_, _[[spells/Prismatic Spray|prismatic spray]]_ (DC 24), _[[spells/Wish|wish]]_
**Spells Prepared **(CL 20th)
9th—_[[spells/Etherealness|etherealness]]_, mass _[[spells/Heal|heal]]_, _[[spells/Miracle|miracle]]_, _[[spells/Storm Of Vengeance|storm of vengeance]]_ (DC 27)
8th—_[[spells/Fire Storm|fire storm]]_ (DC 26), _[[spells/Holy Aura|holy aura]]_ (2) (DC 26), mass _[[spells/Cure Critical Wounds|cure critical wounds]]_ (2)
7th—_[[spells/Destruction|destruction]]_ (DC 25), _[[spells/Dictum|dictum]]_ (DC 25), _[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Holy Word|holy word]]_ (DC 25), _[[spells/Regenerate|regenerate]]_
6th—_[[spells/Banishment|banishment]]_ (DC 24), heroes’ feast, mass _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Undeath to Death|undeath to death]]_ (DC 24), _[[spells/Word of Recall|word of recall]]_
5th—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Breath Of Life|breath of life]]_, _[[spells/Dispel Evil|dispel evil]]_ (DC 23), _[[spells/Plane Shift|plane shift]]_ (DC 23), _[[spells/Righteous Might|righteous might]]_, _[[spells/Symbol of Sleep|symbol of sleep]]_ (DC 23)
4th—_cure critical wounds_ (3), _[[spells/Death Ward|death ward]]_, _[[spells/Dismissal|dismissal]]_ (DC 22), _[[spells/Neutralize Poison|neutralize poison]]_ (2) (DC 22)
3rd—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Daylight|daylight]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Circle against Evil|magic circle against evil]]_, _[[spells/Prayer|prayer]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Wind Wall|wind wall]]_
2nd—_[[spells/Align Weapon|align weapon]]_, bear’s _[[feats/Endurance|endurance]]_, bull’s strength, _[[spells/Consecrate|consecrate]]_, _cure moderate wounds_ (2), _[[monsters/Eagle|eagle]]_’s splendor
1st—_[[spells/Bless|bless]]_, _[[spells/Cure Light Wounds|cure light wounds]]_ (3), _[[spells/Divine Favor|divine favor]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, stabilize, _[[spells/Virtue|virtue]]_

##### Statistics
**Str** 28, **Dex** 20, **Con** 30, **Int** 23, **Wis** 27, **Cha** 25
**Base Atk** +22; **CMB** +32; **CMD** 47
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Craft (any one) +31, Diplomacy +32, Fly +32, Knowledge (history) +31, Knowledge (nature) +31, Knowledge (planes) +31, Knowledge (religion) +31, Perception +33, Sense Motive +33, Spellcraft +31, Stealth +21, Survival +31
**Languages** Celestial, Draconic, Infernal; truespeech
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any good-aligned plane
**Organization** solitary or pair
**Treasure** double (+5 _[[items/Armor/Full plate|full plate]]_, +5 _dancing_ _greatsword_, +5 _composite longbow_ [+9 Str bonus])

### Special Abilities
**Spells **Solars can cast divine spells as 20th-level clerics. They do not gain access to domains or other _[[classes/Cleric|cleric]]_ abilities.
**Slaying Arrow (Su)** A solar’s bow needs no ammunition, and automatically creates a slaying arrow of the solar’s choice when drawn.

##### Description

Solars are the greatest type of angel, usually serving at the right hand of a deity or championing a cause that benefits an entire world or plane. A typical solar looks roughly human, though some physically resemble other humanoid races and a rare few have even more unusual forms. A solar stands about 9 feet tall and weighs about 500 pounds, with a strong, commanding voice that is impossible to ignore. Most have silvery or golden skin.

_[[feats/Blessed|Blessed]]_ with an array of magical powers and the spellcasting abilities of the most powerful clerics, solars are powerful opponents capable of single-handedly slaying mighty evils. They are the greatest trackers among the celestials, the most masterful of which are said to be able to track the days-old wake of a pit fiend flying through the Astral Plane. Some take on the mantle of monster-slayers and hunt powerful fiends and undead such as devourers, night hags, night _[[spells/Shades|shades]]_, and pit fiends, even making forays into the evil planes and the Negative Energy Plane to destroy these creatures at their source before they can bring _[[spells/Harm|harm]]_ to mortals. A few very old solars have succeeded at this task and bear slayer-names of dread creatures that are now extinct by the solar’s hand.

Solars accept roles as guardians, usually of fundamental supernatural concepts, or objects or creatures of great importance. On one world, a group of solars patrols the energy conduits of the sun, alert for any attempts by evil races such as _[[monsters/Drow|drow]]_ to snuff out the light and bring eternal _[[spells/Darkness|darkness]]_. On another, seven solars stand watch over seven mystical chains keeping evil gods bound within a prison demiplane. On yet another, a solar with a _[[items/Weapon Magic Abilities/Flaming|flaming]]_ sword stands watch over the original mortal paradise so that no creature may enter.

In worlds where the gods cannot take physical form, they send solars to be their prophets and gurus (often pretending to be mortals), laying the foundation for cults that grow to become great religions. Likewise, in worlds oppressed by evil, solars are the secret priests who bring hope to the downtrodden, or in some cases allow themselves to be martyred so that their holy essence can explode outward to land and grow in the hearts of great heroes-to-be.

Though they are not gods, the solars’ power approaches that of demigods, and they often have an advisory role for younger or weaker deities. In some polytheistic faiths, mortals worship one or more solars as aspects or near-equal servants of the true deities—never without the deity’s approval—or consider notable solars to be offspring, consorts, lovers, or spouses of true deities (which they may be, depending on the deity).

Unlike other angels, most solars are created from an amalgam of good souls and raw divine energy to directly serve the gods, but an increasing number of these powerful angels have been “promoted” to their existence as solars from lesser creatures like planetars or devas. A few rare and powerful good souls ascend directly to the _[[spells/Status|status]]_ of solar. The oldest solars predate mortality and are among the gods’ first creations. These strange solars are paragons of their kind and have little direct interaction with mortals, focusing on the protection or _destruction_ of abstract concepts such as gravity, dark matter, entropy, and primordial evil.

Solars who spend a long time in the Material Plane, especially those in the guise of mortals, are sometimes the source of half-celestial or _[[monsters/Aasimar|aasimar]]_ bloodlines in mortal families, due either to romantic dalliances or simply the mortals’ proximity to celestial energy. Actual offspring are rare, and when they occur, it is always a mortal mother that bears the child—while solars can appear as either sex, the gods have not granted them the capacity for pregnancy or motherhood. Indeed, this fundamental truth is often what drives a solar to seek out a mortal lover. Since begetting a child upon a mortal is generally frowned upon by other solars, a solar father rarely interacts directly with the fate of his lover or child, so as to avoid bringing shame upon himself or his responsibilities. Yet such solars still watch over their progeny from afar, and in times of peril, they might even be moved to intercede to aid one of their endangered children, albiet in subtle and mysterious ways.

All angels respect the power and wisdom of solars, and though these mightiest of angels usually work alone, they sometimes _[[spells/Command|command]]_ multiple armies led by planetars, acting as great field marshals for massive incursions against the legions of Hell or the hordes of the Abyss.