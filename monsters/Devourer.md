---
cssclass: [monsters]
title1: Devourer
desc_short: This dry, hovering corpse's chest is a prison of jagged ribs, within which
  is trapped a small tormented ghostly form.
title2: Devourer
CR: 11
sources:
- name: Pathfinder RPG Bestiary
  page: 82
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 12800
alignment: NE
size: Large
type: undead
subtypes:
- extraplanar
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 25
  touch: 12
  flat_footed: 22
  components:
    dex: 3
    natural: 13
    size: -1
HP:
  HP: 133
  long: 14d8+70
saves:
  fort: 9
  ref: 7
  will: 12
defensive_abilities:
- spell deflection
- undead traits
SR: 22
speeds:
  base: 30
  fly: 20
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +18 (1d8+9 plus energy drain)
      entries:
      - - damage: 1d8+9
        - effect: energy drain
      count: 2
      attack: claws
      bonus:
      - 18
  special:
  - devour soul
  - energy drain (1 level, DC 20)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - superscripts:
    - 4th
    name: animate dead
    source: default
    freq: At will
  - superscripts:
    - 4th
    name: bestow curse
    source: default
    freq: At will
    DC: 19
  - superscripts:
    - 4th
    name: confusion
    source: default
    freq: At will
    DC: 19
  - superscripts:
    - 7th
    name: control undead
    source: default
    freq: At will
    DC: 22
  - superscripts:
    - 2nd
    name: death knell
    source: default
    freq: At will
    DC: 17
  - superscripts:
    - 2nd
    name: ghoul touch
    source: default
    freq: At will
    DC: 17
  - superscripts:
    - 3rd
    name: inflict serious wounds
    source: default
    freq: At will
    DC: 18
  - superscripts:
    - 4th
    name: lesser planar ally
    source: default
    freq: At will
  - superscripts:
    - 1st
    name: ray of enfeeblement
    source: default
    freq: At will
  - superscripts:
    - 2nd
    name: spectral hand
    source: default
    freq: At will
  - superscripts:
    - 3rd
    name: suggestion
    source: default
    freq: At will
    DC: 18
  - superscripts:
    - 6th
    name: true seeing
    source: default
    freq: At will
  - superscripts:
    - 3rd
    name: vampiric touch
    source: default
    freq: At will
    DC: 18
  sources:
  - name: default
    CL: 18
ability_scores:
  STR: 28
  DEX: 16
  CON:
  INT: 19
  WIS: 16
  CHA: 21
BAB: 10
CMB: 20
CMD: 33
feats:
- name: Blind-Fight
- name: Cleave
- name: Combat Casting
- name: Combat Expertise
- name: Improved Initiative
- name: Improved Sunder
- name: Power Attack
skills:
  Bluff: 19
  Diplomacy: 14
  Fly: 19
  Intimidate: 19
  Knowledge (arcana): 21
  Knowledge (planes): 18
  Perception: 20
  Sense Motive: 17
  Spellcraft: 21
  Stealth: 6
languages:
- Abyssal
- Celestial
- Common
- Infernal
- telepathy 100 ft.
ecology:
  environment: any
  organization: solitary
  treasure_type: standard
special_abilities:
  Devour Soul (Su): By making a touch attack as a standard action, a devourer can
    deal 12d6+18 points of damage as if using a slay living spell. A DC 22 Fortitude
    save reduces this damage to 3d6+18. The soul of a creature slain by this attack
    becomes trapped within the devourer's chest. The creature cannot be brought back
    to life until the devourer's destruction (or a spell deflection-see below) releases
    its soul. A devourer can hold only one soul at a time. The trapped essence provides
    a devourer with 5 essence points for each Hit Die possessed by the soul. A devourer
    must expend essence points when it uses a spell-like ability equal to the spell's
    level (for sake of ease, spell levels for its spell-like abilities are included
    in its stats in superscript). At the start of an encounter, a devourer generally
    has 3d4+3 essence points available. The trapped essence gains one permanent negative
    level for every 5 points of essence drained-these negative levels remain if the
    creature is brought back to life (but they do not stack with any negative levels
    imparted by being brought back to life). A soul that is completely consumed may
    only be restored to life by a miracle or wish. The save DC is Charisma-based.
  Spell Deflection (Su): 'If any of the following spells are cast at the devourer
    and overcome its spell resistance, they instead affect a devoured soul: banishment,
    chaos hammer, confusion, crushing despair, detect thoughts, dispel evil, dominate
    person, fear, geas/quest, holy word, hypnotism, imprisonment, magic jar, maze,
    suggestion, trap the soul, or any form of charm or compulsion. While none of these
    effects harms the soul, the caster makes a DC 25 caster level check when a spell
    is deflected-success indicates that the trapped soul is released from its prison
    and the creature whose body it belonged to can now be restored to life as normal.'
desc_long: Devourers are the undead remnants of fiends and evil spellcasters who became
  lost beyond the farthest reaches of the multiverse. Returning with warped bodies,
  alien sentience, and a hunger for life, devourers threaten all souls with a terrifying,
  tormented annihilation. These withered corpses stand 10 feet tall but weigh a mere
  200 pounds.

---

# Devourer
This dry, hovering corpse’s chest is a prison of jagged ribs, within which is trapped a small tormented ghostly form.
**Source** Pathfinder RPG Bestiary pg. 82
**XP** 12,800

NE Large undead (extraplanar)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +20

##### Defense

**AC** 25, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+3 Dex, +13 natural, –1 size)
**hp** 133 (14d8+70)
**Fort** +9, **Ref** +7, **Will** +12
**Defensive Abilities** spell deflection, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 22

##### Offense
**Speed** 30 ft., fly 20 ft. (perfect)
**Melee** 2 claws +18 (1d8+9 plus _[[universal monster rules/Energy Drain|energy drain]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** devour soul, _energy drain_ (1 level, DC 20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th)
At will—_[[spells/Animate Dead|animate dead]]_, _[[spells/Bestow Curse|bestow curse]]_ (DC 19), _[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Control Undead|control undead]]_ (DC 22), _[[spells/Death Knell|death knell]]_ (DC 17), _[[spells/Ghoul touch|ghoul touch]]_ (DC 17), _[[spells/Inflict Serious Wounds|inflict serious wounds]]_ (DC 18), lesser _[[spells/Planar Ally|planar ally]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_, _[[spells/Spectral Hand|spectral hand]]_, _[[spells/Suggestion|suggestion]]_ (DC 18), _[[spells/True Seeing|true seeing]]_, _[[spells/Vampiric Touch|vampiric touch]]_ (DC 18)

##### Statistics
**Str** 28, **Dex** 16, **Con** —, **Int** 19, **Wis** 16, **Cha** 21
**Base Atk** +10; **CMB** +20; **CMD** 33
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Bluff +19, Diplomacy +14, Fly +19, Intimidate +19, Knowledge (arcana) +21, Knowledge (planes) +18, Perception +20, Sense Motive +17, Spellcraft +21, Stealth +6
**Languages** Abyssal, Celestial, Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** standard

### Special Abilities

**Devour Soul (Su)** By making a touch attack as a standard action, a _[[monsters/Devourer|devourer]]_ can deal 12d6+18 points of damage as if using a _[[spells/Slay Living|slay living]]_ spell. A DC 22 Fortitude save reduces this damage to 3d6+18. The soul of a creature slain by this attack becomes trapped within the _devourer_’s chest. The creature cannot be brought back to life until the _devourer_’s _[[spells/Destruction|destruction]]_ (or a spell _deflection_—see below) releases its soul. A _devourer_ can hold only one soul at a time. The trapped essence provides a _devourer_ with 5 essence points for each Hit Die possessed by the soul. A _devourer_ must _[[spells/Expend|expend]]_ essence points when it uses a spell-like ability equal to the spell’s level (for sake of ease, spell levels for its _spell-like abilities_ are included in its stats in superscript). At the start of an encounter, a _devourer_ generally has 3d4+3 essence points available. The trapped essence gains one permanent negative level for every 5 points of essence drained—these negative levels remain if the creature is brought back to life (but they do not stack with any negative levels imparted by being brought back to life). A soul that is completely consumed may only be restored to life by a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_. The save DC is Charisma-based.
**Spell _Deflection_ (Su) **If any of the following spells are cast at the _devourer_ and overcome its _[[universal monster rules/Spell Resistance|spell resistance]]_, they instead affect a devoured soul: _[[spells/Banishment|banishment]]_, _[[spells/Chaos Hammer|chaos hammer]]_, _confusion_, _[[spells/Crushing Despair|crushing despair]]_, _[[spells/Detect Thoughts|detect thoughts]]_, _[[spells/Dispel Evil|dispel evil]]_, _[[spells/Dominate Person|dominate person]]_, _[[universal monster rules/Fear|fear]]_, geas/quest, _[[spells/Holy Word|holy word]]_, _[[spells/Hypnotism|hypnotism]]_, _[[spells/Imprisonment|imprisonment]]_, _[[spells/Magic Jar|magic jar]]_, _[[spells/Maze|maze]]_, _suggestion_, _[[spells/Trap the Soul|trap the soul]]_, or any form of charm or compulsion. While none of these effects harms the soul, the caster makes a DC 25 caster level check when a spell is deflected—success indicates that the trapped soul is released from its prison and the creature whose body it belonged to can now be restored to life as normal.

##### Description

Devourers are the undead remnants of fiends and evil spellcasters who became lost beyond the farthest reaches of the multiverse. Returning with warped bodies, alien sentience, and a hunger for life, devourers threaten all souls with a terrifying, tormented annihilation. These withered corpses stand 10 feet tall but weigh a mere 200 pounds.