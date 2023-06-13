---
cssclass: [monsters]
title1: Nihiloi
desc_short: A mass of black, bramble-like tentacles writhes from the back of this
  vague, shifting humanoid. Inky skin covers the creature, and ebon claws curve long
  and thin from the tips of its fingers. Numerous tendrils of wispy shadow hold the
  creature aloft while others rise above its shoulders in strange, wriggling wings.
title2: Nihiloi
CR: 11
sources:
- name: 'Pathfinder #29: Mother of Flies'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/councilOfThieves/v5748btpy8bc1
XP: 12800
alignment: CN
size: Medium
type: outsider
subtypes:
- extraplanar
initiative:
  bonus: 11
senses:
  darkvision: 90
  see in darkness: true
auras:
- name: tendrils
AC:
  AC: 23
  touch: 18
  flat_footed: 15
  components:
    dex: 7
    dodge: 1
    natural: 5
HP:
  HP: 135
  long: 10d10+80
  fast_healing: 5
  fast_healing_weakness: only in shadows
saves:
  fort: 11
  ref: 16
  will: 12
defensive_abilities:
- malleable
immunities:
- cold
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 claws +13 (2d8+3)
      entries:
      - - damage: 2d8+3
      count: 2
      attack: claws
      bonus:
      - 13
    - text: 2 slams +13 (1d8+3 plus grab)
      entries:
      - - damage: 1d8+3
        - effect: grab
      count: 2
      attack: slams
      bonus:
      - 13
  special:
  - shadow crafting
space: 5
reach: 20
reach_other: with slam
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: At will
    DC: 16
  - name: deeper darkness
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 10
ability_scores:
  STR: 17
  DEX: 24
  CON: 27
  INT: 15
  WIS: 20
  CHA: 18
BAB: 10
CMB: 17
CMD: 31
feats:
- name: Agile Maneuvers
- name: Dodge
- name: Improved Initiative
- name: Lightning Reflexes
- name: Mobility
skills:
  Acrobatics: 20
    to jump: 24
  Bluff: 17
  Diplomacy: 17
    against Plane of Shadow natives: 21
  Escape Artist: 20
  Fly: 24
  Knowledge (planes): 15
  Perception: 18
  Stealth: 20
    in dim light: 30
  _racial_mods:
    Stealth:
      in areas of dim light: 10
    Diplomacy:
      when dealing with other Plane of Shadow natives: 4
languages:
- Abyssal
- Common
- Infernal
- broadcast
ecology:
  environment: any (Plane of Shadow)
  organization: solitary, cell (2-8), or cabal (9-26)
  treasure_type: standard
special_abilities:
  Broadcast (Su): Nihilois possess a selective type of long-distance telepathy. All
    nihilois can communicate telepathically with all other nihilois within 3 miles.
    An intermediary nihiloi can even pass messages between others of their race separated
    over long distances. They can also communicate telepathically with members of
    other races within 50 feet.
  Malleable (Su): Nihilois exists as shadow, congealed into tangible but ever-twisting
    forms. Anytime a nihiloi is aware of imminent attack, it receives the benefit
    of 20% concealment, as it can warp and shift its body to avoid the blow.
  See in Darkness (Su): Nihilois can see perfectly in darkness of any kind, even that
    created by a deeper darkness spell.
  Shadow Crafting (Sp): Five times per day, when in an area of dim light or darkness,
    a nihiloi can manipulate shadow to reproduce an effect identical to shadow evocation.
    Typically, these effects are DC 19 to resist, but if both the nihiloi and its
    target are within areas of dim light or darkness, the DC increases by +2. This
    is a shadow effect. The save DC is Charisma-based.
  Tendrils (Su): Once aware of enemies nearby, as a standard action, a nihiloi can
    unleash its tendrils in a haze of umbral whips that surrounds the area within
    10 feet of it. Any creature that enters this area takes 4d6+3 points of damage
    from dozens of deadly lashes (Reflex save DC 23 for half damage). A nihiloi must
    take an additional standard action to end this effect. The save DC is Constitution-based.
desc_long: |-
  Violent xenophobes, the creatures typically called nihilois, devashades, or shadow lords pose a rising threat to interlopers into their umbral realm. In ages immemorial, these creatures enjoyed vast empires upon the mysterious Plane of Shadow, but through the millennia incursion by immigrants and interlopers have eroded their way of life and scattered their numbers. In the face of spellcasters from the Material Plane striding across their homeland-using it as little more than a umbral thoroughfare-and whole terrible races like kytons migrating to their native reaches, the nihilois have long retreated into the deepest darknesses of their realm. Yet as alien encroachment continues, slowly the nihilois have revealed themselves, and found to their surprise that they are powerful and feared.

  Nihilois-as the first travelers from Golarion termed them, believing them to be members of an ancient mythical race-resemble gaunt, vaguely humanoid creatures shrouded in ever-writhing shadow stuff with fountains of dark tendrils jutting from their backs. They often hold these thin limbs in tight bunches that appear like strange, dense wings, but unfurl them easily and with shocking speed to lash out against their enemies. Unable to vocalize words, nihilois are widely distrusted by creatures foreign to the Plane of Shadow. Even a pair of the shadowy natives is unsettling to those encountering them for the first time as they silently gesture and nod, holding secret councils few others can understand. Creatures frequently interacting with them know the nihilois have a shared name for their race, though since these creatures speak only telepathically, the term sounds more like the passage of massive wings than a word pronounceable in most sentient tongues.

---

# Nihiloi
A mass of black, bramble-like tentacles writhes from the back of this vague, shifting humanoid. Inky skin covers the creature, and ebon claws curve long and thin from the tips of its fingers. Numerous tendrils of wispy _[[items/Armor Magic Abilities/Shadow|shadow]]_ hold the creature aloft while others rise above its shoulders in strange, wriggling wings.
**Source** Pathfinder #29: Mother of Flies pg. 86
**XP** 12,800

CN Medium outsider (extraplanar)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 90 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +18
**Aura** tendrils

##### Defense

**AC** 23, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+7 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural)
**hp** 135 (10d10+80); _[[universal monster rules/Fast Healing|fast healing]]_ 5 (only in shadows)
**Fort** +11, **Ref** +16, **Will** +12
**Defensive Abilities** malleable; **Immune** cold

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** 2 claws +13 (2d8+3), 2 slams +13 (1d8+3 plus _[[universal monster rules/Grab|grab]]_)
**Space** 5 ft., **Reach** 20 ft. (with slam)
**Special Attacks** _shadow_ crafting
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th)
At will - _[[spells/Detect Thoughts|detect thoughts]]_ (DC 16)
3/day - _[[spells/Deeper Darkness|deeper darkness]]_

##### Statistics
**Str** 17, **Dex** 24, **Con** 27, **Int** 15, **Wis** 20, **Cha** 18
**Base Atk** +10; **CMB** +17; **CMD** 31
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_
**Skills** Acrobatics +20 (+24 to _[[spells/Jump|jump]]_), Bluff +17, Diplomacy +17 (+21 against Plane of _Shadow_ natives), Escape Artist +20, Fly +24, Knowledge (planes) +15, Perception +18, Stealth +20 (+30 in dim light); **Racial Modifiers** +10 Stealth in areas of dim light, +4 Diplomacy when dealing with other Plane of _Shadow_ natives
**Languages** Abyssal, Common, Infernal; broadcast

##### Ecology

**Environment** any (Plane of _Shadow_)
**Organization** solitary, cell (2-8), or cabal (9-26)
**Treasure** standard

### Special Abilities

**Broadcast (Su)** Nihilois possess a selective type of long-distance _[[universal monster rules/Telepathy|telepathy]]_. All nihilois can communicate telepathically with all other nihilois within 3 miles. An intermediary _[[monsters/Nihiloi|nihiloi]]_ can even pass messages between others of their race separated over long distances. They can also communicate telepathically with members of other races within 50 feet.

**Malleable (Su)** Nihilois exists as _shadow_, congealed into tangible but ever-twisting forms. Anytime a _nihiloi_ is aware of imminent attack, it receives the benefit of 20% concealment, as it can warp and shift its body to avoid the blow.
**_See in Darkness_ (Su)** Nihilois can see perfectly in _[[spells/Darkness|darkness]]_ of any kind, even that created by a _deeper darkness_ spell.
**_Shadow_ Crafting (Sp)** Five times per day, when in an area of dim light or _darkness_, a _nihiloi_ can manipulate _shadow_ to reproduce an effect identical to _[[spells/Shadow Evocation|shadow evocation]]_. Typically, these effects are DC 19 to resist, but if both the _nihiloi_ and its target are within areas of dim light or _darkness_, the DC increases by +2. This is a _shadow_ effect. The save DC is Charisma-based.

**Tendrils (Su)** Once aware of enemies nearby, as a standard action, a _nihiloi_ can unleash its tendrils in a haze of _[[items/Weapon Magic Abilities/Umbral|umbral]]_ whips that surrounds the area within 10 feet of it. Any creature that enters this area takes 4d6+3 points of damage from dozens of _[[items/Weapon Magic Abilities/Deadly|deadly]]_ lashes (Reflex save DC 23 for half damage). A _nihiloi_ must take an additional standard action to end this effect. The save DC is Constitution-based.

##### Description

Violent xenophobes, the creatures typically _[[items/Weapon Magic Abilities/Called|called]]_ nihilois, devashades, or _shadow_ lords pose a rising threat to interlopers into their _umbral_ realm. In ages immemorial, these creatures enjoyed vast empires upon the mysterious Plane of _Shadow_, but through the millennia incursion by immigrants and interlopers have eroded their way of life and scattered their numbers. In the face of spellcasters from the Material Plane striding across their homeland—using it as little more than a _umbral_ thoroughfare—and whole terrible races like kytons migrating to their native reaches, the nihilois have long retreated into the deepest darknesses of their realm. Yet as alien encroachment continues, slowly the nihilois have revealed themselves, and found to their surprise that they are powerful and feared.

Nihilois—as the first travelers from Golarion termed them, believing them to be members of an ancient mythical race—resemble gaunt, vaguely humanoid creatures shrouded in ever-writhing _shadow_ stuff with fountains of dark tendrils jutting from their backs. They often hold these thin limbs in tight bunches that appear like strange, dense wings, but unfurl them easily and with shocking speed to lash out against their enemies. Unable to vocalize words, nihilois are widely distrusted by creatures foreign to the Plane of _Shadow_. Even a pair of the shadowy natives is unsettling to those encountering them for the first time as they silently gesture and nod, holding secret councils few others can understand. Creatures frequently interacting with them know the nihilois have a shared name for their race, though since these creatures speak only telepathically, the term sounds more like the passage of massive wings than a word pronounceable in most sentient _[[spells/Tongues|tongues]]_.