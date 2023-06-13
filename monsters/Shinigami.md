---
cssclass: [monsters]
title1: Shinigami
desc_short: This emaciated, robed humanoid wields a scythe made of bone to match the
  skeletal wings that protrude from its shoulders.
title2: Shinigami
CR: 17
sources:
- name: Bestiary 3
  page: 244
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 102400
alignment: LN
size: Large
type: outsider
subtypes:
- extraplanar
- lawful
initiative:
  bonus: 9
senses:
  darkvision: 60
  detect chaos: true
  detect law: true
  true seeing: true
auras:
- name: fear aura
  radius: 60
  DC: 30
AC:
  AC: 31
  touch: 15
  flat_footed: 25
  components:
    dex: 5
    dodge: 1
    natural: 16
    size: -1
HP:
  HP: 275
  long: 22d10+154
  fast_healing: 10
saves:
  fort: 20
  ref: 12
  will: 19
DR:
- amount: 10
  weakness: chaotic and silver
immunities:
- ability damage
- ability drain
- cold
- death effects
- disease
- energy drain
- negative energy
- poison
resistances:
  acid: 10
  fire: 10
SR: 28
speeds:
  base: 30
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +3 axiomatic scythe +30/+25/+20/+15 (2d6+10/×4)
      entries:
      - - damage: 2d6+10
          crit_multiplier: 4
      attack: +3 axiomatic scythe
      bonus:
      - 30
      - 25
      - 20
      - 15
    - text: 2 wings +21 (1d8+2)
      entries:
      - - damage: 1d8+2
      count: 2
      attack: wings
      bonus:
      - 21
  special:
  - destroy soul
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: destruction
    source: default
    freq: 3/day
    DC: 26
  - name: energy drain
    source: default
    freq: 3/day
  - name: greater scrying
    source: default
    freq: 3/day
    DC: 26
  - name: soul bind
    source: default
    freq: 3/day
    DC: 28
  sources:
  - name: default
    CL: 20
    concentration: 29
ability_scores:
  STR: 21
  DEX: 20
  CON: 24
  INT: 17
  WIS: 22
  CHA: 29
BAB: 22
CMB: 28
CMD: 44
feats:
- name: Cleave
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Power Attack
- name: Spring Attack
- name: Stand Still
- name: Weapon Focus (scythe)
- name: Whirlwind Attack
skills:
  Acrobatics: 30
  Diplomacy: 34
  Fly: 36
  Intimidate: 34
  Knowledge (planes): 28
  Perception: 31
  Sense Motive: 31
  Spellcraft: 28
  Stealth: 26
languages:
- Celestial
- Common
- Draconic
- Infernal
- tongues
ecology:
  environment: any
  organization: solitary
  treasure_type: double
  treasure:
  - +3 axiomatic scythe
  - other treasure
special_abilities:
  Destroy Soul (Su): A shinigami possesses six gems in which it encapsulates souls
    with its soul bind spell-like ability. These gems are only useful to the shinigami
    that owns them, and if the shinigami dies, the gems are destroyed as well. As
    a standard action once per day, a shinigami can hold up a gem that currently contains
    a soul and crush it, permanently destroying the soul within and releasing a 30-foot-radius
    burst of negative energy that inflicts 1d6 negative levels on all creatures in
    the area of effect. A successful DC 30 Fortitude save reduces this to 1 negative
    level. The soul destroyed in the process of using this ability can only be brought
    back to life by means of a miracle or wish spell. This is a death effect. The
    save DC is Charisma-based.
desc_long: Feared as truly impartial and merciless harbingers of death, shinigamis
  are relentless in their pursuit of dispensing quick and just deaths upon those who
  would seek to disrupt the delicate balance of life. Unlike other, more sinister
  bringers of doom, shinigamis do not take pleasure in their work and do not seek
  to impose suffering-although there are exceptions. Some individuals, aptly described
  by their kin as “rogue shinigamis,” subscribe to either more merciful or more despicable
  forms of execution, and are either lawful good or lawful evil. Victims who have
  had their lives spared by kind shinigamis praise the angels of death for their clemency
  and willingness to listen to the victims' plight, while other dastardly survivors
  have successfully cheated or bribed their way out of death by manipulating credulous
  or less honorable shinigami. A shinigami is 9 feet tall and weighs 130 pounds.

---

# Shinigami
This emaciated, robed humanoid wields a _[[items/Weapon/Scythe|scythe]]_ made of bone to match the skeletal wings that protrude from its shoulders.
**Source** Bestiary 3 pg. 244
**XP** 102,400

LN Large outsider (extraplanar, lawful)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Law|detect law]]_, _[[spells/True Seeing|true seeing]]_; Perception +31
**Aura** _[[universal monster rules/Fear|fear]]_ aura (60 ft., DC 30)

##### Defense

**AC** 31, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+5 Dex, +1 dodge, +16 natural, –1 size)
**hp** 275 (22d10+154); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +20, **Ref** +12, **Will** +19
**DR** 10/chaotic and silver; **Immune** ability damage, ability drain, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, negative energy, poison; **Resist** acid 10, fire 10; **SR** 28

##### Offense
**Speed** 30 ft., fly 40 ft. (perfect)
**Melee** +3 _[[items/Weapon Magic Abilities/Axiomatic|axiomatic]]_ _scythe_ +30/+25/+20/+15 (2d6+10/×4), 2 wings +21 (1d8+2)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** destroy soul
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +29)
Constant—_detect chaos_, _detect law_, _[[spells/Tongues|tongues]]_, _true seeing_
3/day—_[[spells/Destruction|destruction]]_ (DC 26), _energy drain_, greater _[[spells/Scrying|scrying]]_ (DC 26), _[[spells/Soul Bind|soul bind]]_ (DC 28)

##### Statistics
**Str** 21, **Dex** 20, **Con** 24, **Int** 17, **Wis** 22, **Cha** 29
**Base Atk** +22; **CMB** +28; **CMD** 44
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Stand Still|Stand Still]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scythe_), _[[feats/Whirlwind Attack|Whirlwind Attack]]_
**Skills** Acrobatics +30, Diplomacy +34, Fly +36, Intimidate +34, Knowledge (planes) +28, Perception +31, Sense Motive +31, Spellcraft +28, Stealth +26
**Languages** Celestial, Common, Draconic, Infernal; _tongues_

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** double (+3 _axiomatic_ _scythe_, other treasure)

### Special Abilities

**Destroy Soul (Su)** A _[[monsters/Shinigami|shinigami]]_ possesses six gems in which it encapsulates souls with its _soul bind_ spell-like ability. These gems are only useful to the _shinigami_ that owns them, and if the _shinigami_ dies, the gems are destroyed as well. As a standard action once per day, a _shinigami_ can hold up a gem that currently contains a soul and crush it, permanently destroying the soul within and releasing a 30-foot-radius burst of negative energy that inflicts 1d6 negative levels on all creatures in the area of effect. A successful DC 30 Fortitude save reduces this to 1 negative level. The soul destroyed in the process of using this ability can only be brought back to life by means of a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_ spell. This is a death effect. The save DC is Charisma-based.

##### Description

Feared as truly impartial and merciless harbingers of death, shinigamis are relentless in their pursuit of dispensing quick and just deaths upon those who would seek to disrupt the delicate balance of life. Unlike other, more sinister bringers of _[[spells/Doom|doom]]_, shinigamis do not take pleasure in their work and do not seek to impose suffering—although there are exceptions. Some individuals, aptly described by their kin as “_[[classes/Rogue|rogue]]_ shinigamis,” subscribe to either more _[[items/Weapon Magic Abilities/Merciful|merciful]]_ or more despicable forms of execution, and are either lawful good or lawful evil. Victims who have had their lives spared by kind shinigamis praise the angels of death for their clemency and willingness to listen to the victims’ plight, while other dastardly survivors have successfully cheated or bribed their way out of death by manipulating credulous or less honorable _shinigami_. A _shinigami_ is 9 feet tall and weighs 130 pounds.