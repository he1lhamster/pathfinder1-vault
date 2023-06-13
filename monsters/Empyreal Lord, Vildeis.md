---
cssclass: [monsters]
title1: Empyreal Lord, Vildeis
desc_short: This red-winged angel is blindfolded and wrapped with bloody bandages.
  What shows of her flesh is scarred with celestial runes.
title2: Vildeis
CR: 28
sources:
- name: Bestiary 4
  page: 92
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 4915200
alignment: LG
size: Large
type: outsider
subtypes:
- angel
- extraplanar
- good
- lawful
initiative:
  bonus: 13
senses:
  blindsense: 120
  darkvision: 60
  detect evil: true
  true seeing: true
  zealous vision: true
auras:
- name: primal
  radius: 30
- name: protective
AC:
  AC: 44
  touch: 19
  flat_footed: 34
  components:
    dex: 9
    dodge: 1
    natural: 25
    size: -1
    deflection vs. evil: 4
HP:
  HP: 610
  long: 33d10+429
  regeneration: 10
  regeneration_weakness: evil artifacts, effects, and spells
saves:
  fort: 31
  ref: 20
  will: 26
  other: +4 vs. poison, +4 resistance vs. evil
DR:
- amount: 15
  weakness: epic and evil
immunities:
- ability damage
- ability drain
- acid
- bleed
- charm effects
- compulsion effects
- cold
- death effects
- energy drain
- petrification
resistances:
  electricity: 30
  fire: 30
speeds:
  base: 40
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: Cicatrix +50/+45/+40/+35 (1d6+17/17-20 plus 1 bleed and 2d6 vicious)
      entries:
      - - damage: 1d6+17
          crit_range: 17-20
        - damage: '1'
          type: bleed
        - damage: 2d6
          type: vicious
      attack: Cicatrix
      bonus:
      - 50
      - 45
      - 40
      - 35
  ranged:
  - - text: Cicatrix +47 (1d6+17/17-20 plus 1 bleed)
      entries:
      - - damage: 1d6+17
          crit_range: 17-20
        - damage: '1'
          type: bleed
      attack: Cicatrix
      bonus:
      - 47
  special:
  - smite evil 7/day (+5 attack and AC, +20 damage, disintegrate evil outsiders)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: command
    source: default
    freq: At will
    DC: 16
  - name: greater teleport
    source: default
    freq: At will
  - name: haste
    source: default
    freq: At will
  - superscripts:
    - APG
    name: paladin's sacrifice
    source: default
    freq: At will
  - superscripts:
    - APG
    name: pain strike
    source: default
    freq: At will
    DC: 18
  - name: discern location
    source: default
    freq: 3/day
  - name: geas/quest
    source: default
    freq: 3/day
    DC: 21
  - name: heal
    source: default
    freq: 3/day
  - name: holy word
    source: default
    freq: 3/day
    DC: 22
  - name: mark of justice
    source: default
    freq: 3/day
    DC: 20
  - superscripts:
    - APG
    name: mass pain strike
    source: default
    freq: 3/day
    DC: 20
  - name: searing light
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 20
    concentration: 25
spells:
  entries:
  - superscripts:
    - APG
    name: blaze of glory
    source: Paladin
    level: 4
    DC: 19
  - name: break enchantment
    source: Paladin
    level: 4
  - name: death ward
    source: Paladin
    level: 4
  - superscripts:
    - APG
    name: king's castle
    source: Paladin
    level: 4
  - name: dispel magic
    source: Paladin
    level: 3
  - superscripts:
    - APG
    name: fires of judgment
    source: Paladin
    level: 3
    DC: 18
  - name: prayer
    source: Paladin
    level: 3
  - superscripts:
    - APG
    name: righteous vigor
    source: Paladin
    level: 3
  - name: bull's strength
    source: Paladin
    level: 2
  - superscripts:
    - APG
    name: corruption resistance
    source: Paladin
    level: 2
  - superscripts:
    - UC
    name: litany of warding
    source: Paladin
    level: 2
  - name: remove paralysis
    source: Paladin
    level: 2
  - name: shield other
    source: Paladin
    level: 2
  - name: divine favor
    source: Paladin
    level: 1
    count: 3
  - superscripts:
    - APG
    name: hero's defiance
    source: Paladin
    level: 1
  - name: lesser restoration
    source: Paladin
    level: 1
    count: 2
  sources:
  - name: Paladin
    type: prepared
    CL: 20
    concentration: 25
ability_scores:
  STR: 35
  DEX: 29
  CON: 37
  INT: 18
  WIS: 22
  CHA: 21
BAB: 33
CMB: 46
CMD: 66
feats:
- name: Blinding Critical
- name: Combat Casting
- name: Combat Reflexes
- name: Critical Focus
- name: Deadly Aim
- name: Dodge
- name: Flyby Attack
- name: Improved Critical (dagger)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Spell Penetration
- name: Step Up
- name: Vital Strike
- name: Weapon Focus (dagger)
skills:
  Acrobatics: 45
  Bluff: 41
  Fly: 26
  Heal: 23
  Intimidate: 41
  Knowledge (planes): 40
  Knowledge (religion): 40
  Perception: 42
  Sense Motive: 42
  Sleight of Hand: 45
  Stealth: 41
languages:
- Celestial
- Draconic
- truespeech
special_qualities:
- lay on hands (16d6, 25/day)
- seed of life
ecology:
  environment: any (Heaven)
  organization: unique
  treasure_type: standard
  treasure:
  - Cicatrix
  - other treasure
special_abilities:
  Primal Aura (Su): Whenever Vildeis would be affected by a bleed effect, all enemies
    within 30 feet gain that bleeding condition instead, as though they were the effect's
    original targets (no saving throw, creatures immune to bleeding are immune to
    this effect). The Heal DC to stop this bleeding is 25.
  Smite Evil (Su): Vildeis can smite evil as a 20th-level paladin. Whenever she uses
    smite evil and successfully strikes an evil outsider, the outsider is also subject
    to disintegrate, using Vildeis's paladin level as the caster level. After the
    disintegrate effect and the damage from the attack are resolved, the smite effect
    immediately ends.
  Spells: Vildeis casts spells as a 20th-level paladin.
  Zealous Vision (Su): Vildeis automatically pinpoints the location of any evil creature
    within 1,000 feet of her.
desc_long: |-
  Also known as the Cardinal Martyr, Vildeis endlessly sacrifices herself in penitence for the sins of the multiverse, every battle against evil giving her body one more wound with which she might shed bloody tears for existence. When Vildeis emerged from the Heavens, she was a being of sublime beauty, but of a majesty so delicate that she couldn't suffer the sight or even the thought of evil. Within an hour of her birth, she had put out her own eyes, refusing to even gaze upon a reality tainted by sin. Since the first self-inflicted wound marred her once-perfect body, she has struggled against evil in all its forms. Denying herself home or rest, Vildeis harrows the wildest reaches of the multiverse, driving back the expansions of foul realms and slaying those who would do wicked deeds.

  Vildeis has no home among the planes, and forgoes any comforts-even those as basic as shelter or company-so long as there is evil afoot in the multiverse. Such makes her one of the most aloof empyreal lords, but also one of the most storied. Across the planes, legends tell of pitched battles, desperate last stands, and near massacres turned in the favor of the innocent by the sudden appearance of Vildeis herself, bloody-winged and avenging. While such miraculous rescues have more to do with happenstance then omniscience, they nonetheless inf lame the passions of the righteous across countless worlds. Those who seek to encounter the empyreal lord of devotion, sacrifice, and scars must follow rumors of her passing, usually spoken by awed beings and crippled fiends along the fringes of reality's darkest outlands.

  Nearly as well known as the Cardinal Martyr herself are her morbid trappings-miles of stained bandages, scars etched and re-etched in the shapes of celestial runes, and a dagger that drips with her blood as often as that of her enemies. Of these, her dagger Cicatrix is the most infamous, a black blade like a thorn dropped from some gigantic iron rose, which the empyreal lord used to blind herself. Tales tell that she uses her blade not just to slay the wicked and share her blindness, but to carve the runes that crisscross her body upon others, infusing them with the compulsion to battle evil even if previously there was no such desire.

---

# Empyreal Lord, Vildeis
This red-winged angel is blindfolded and wrapped with bloody bandages. What shows of her flesh is scarred with celestial runes.
**Source** Bestiary 4 pg. 92
**XP** 4,915,200

LG Large outsider (angel, extraplanar, good, lawful)
**Init** +13; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 120 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_, _[[spells/True Seeing|true seeing]]_, zealous _[[spells/Vision|vision]]_; Perception +42
**Aura** primal (30 ft.), protective

##### Defense

**AC** 44, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 34 (+9 Dex, +1 dodge, +25 natural, –1 size; +4 _[[spells/Deflection|deflection]]_ vs. evil)
**hp** 610 (33d10+429); _[[universal monster rules/Regeneration|regeneration]]_ 10 (evil artifacts, effects, and spells)
**Fort** +31, **Ref** +20, **Will** +26; +4 vs. poison, +4 _[[universal monster rules/Resistance|resistance]]_ vs. evil
**DR** 15/epic and evil; **Immune** ability damage, ability drain, acid, _[[universal monster rules/Bleed|bleed]]_, charm effects, compulsion effects, cold, death effects, _[[universal monster rules/Energy Drain|energy drain]]_, petrification; **Resist** electricity 30, fire 30

##### Offense
**Speed** 40 ft., fly 60 ft. (average)
**Melee** _[[items/Weapon/Cicatrix|Cicatrix]]_ +50/+45/+40/+35 (1d6+17/17–20 plus 1 _bleed_ and 2d6 _[[items/Weapon Magic Abilities/Vicious|vicious]]_)
**Ranged** _Cicatrix_ +47 (1d6+17/17–20 plus 1 _bleed_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** smite evil 7/day (+5 attack and AC, +20 damage, _[[spells/Disintegrate|disintegrate]]_ evil outsiders)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +25)
Constant—_detect evil_, _true seeing_
At will—_[[spells/Command|command]]_* (DC 16), greater teleport, _[[spells/Haste|haste]]_*, _[[classes/Paladin|paladin]]_’s _[[spells/Sacrifice|sacrifice]]_, _[[spells/Pain Strike|pain strike]]_ (DC 18)
3/day—_[[spells/Discern Location|discern location]]_, geas/quest (DC 21), _[[spells/Heal|heal]]_, _[[spells/Holy Word|holy word]]_* (DC 22), _[[spells/Mark of Justice|mark of justice]]_ (DC 20), mass _pain strike_ (DC 20), _[[spells/Searing Light|searing light]]_*
* Vildeis can use the mythic version of this ability in her realm.
**_Paladin_ Spells Prepared **(CL 20th; concentration +25)
4th—_[[spells/Blaze of Glory|blaze of glory]]_ (DC 19), _[[spells/Break Enchantment|break enchantment]]_, _[[spells/Death Ward|death ward]]_, _[[npcs/King|king]]_’s castle
3rd—_[[spells/Dispel Magic|dispel magic]]_, fires of judgment (DC 18), _[[spells/Prayer|prayer]]_, _[[spells/Righteous Vigor|righteous vigor]]_
2nd—bull’s strength, _[[spells/Corruption Resistance|corruption resistance]]_, _[[spells/Litany of Warding|litany of warding]]_, _[[spells/Remove Paralysis|remove paralysis]]_, _[[spells/Shield Other|shield other]]_
1st—_[[spells/Divine Favor|divine favor]]_ (3), hero’s defiance, lesser _[[spells/Restoration|restoration]]_ (2)

##### Statistics
**Str** 35, **Dex** 29, **Con** 37, **Int** 18, **Wis** 22, **Cha** 21
**Base Atk** +33; **CMB** +46; **CMD** 66
**Feats** _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (_[[items/Weapon/Dagger|dagger]]_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Step Up|Step Up]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_dagger_)
**Skills** Acrobatics +45, Bluff +41, Fly +26, _Heal_ +23, Intimidate +41, Knowledge (planes) +40, Knowledge (religion) +40, Perception +42, Sense Motive +42, Sleight of Hand +45, Stealth +41
**Languages** Celestial, Draconic; truespeech
**SQ** lay on hands (16d6, 25/day), seed of life

##### Ecology

**Environment** any (Heaven)
**Organization** unique
**Treasure** standard (_Cicatrix_, other treasure)

### Special Abilities

**Primal Aura (Su)** Whenever Vildeis would be affected by a _bleed_ effect, all enemies within 30 feet gain that bleeding condition instead, as though they were the effect’s original targets (no saving throw, creatures immune to bleeding are immune to this effect). The _Heal_ DC to stop this bleeding is 25.
**Smite Evil (Su)** Vildeis can smite evil as a 20th-level _paladin_. Whenever she uses smite evil and successfully strikes an evil outsider, the outsider is also subject to _disintegrate_, using Vildeis’s _paladin_ level as the caster level. After the _disintegrate_ effect and the damage from the attack are resolved, the smite effect immediately ends.
**Spells** Vildeis casts spells as a 20th-level _paladin_.

**Zealous _Vision_ (Su)** Vildeis automatically pinpoints the location of any evil creature within 1,000 feet of her.

##### Description

Also known as the Cardinal Martyr, Vildeis endlessly sacrifices herself in penitence for the sins of the multiverse, every battle against evil giving her body one more wound with which she might shed bloody tears for existence. When Vildeis emerged from the Heavens, she was a being of sublime beauty, but of a majesty so delicate that she couldn’t suffer the sight or even the thought of evil. Within an hour of her birth, she had put out her own eyes, refusing to even _[[universal monster rules/Gaze|gaze]]_ upon a reality tainted by sin. Since the first self-inflicted wound marred her once-perfect body, she has struggled against evil in all its forms. _[[items/Armor Magic Abilities/Denying|Denying]]_ herself home or rest, Vildeis harrows the wildest reaches of the multiverse, driving back the expansions of foul realms and slaying those who would do wicked deeds.

Vildeis has no home among the planes, and forgoes any comforts—even those as basic as shelter or company—so long as there is evil afoot in the multiverse. Such makes her one of the most aloof empyreal lords, but also one of the most storied. Across the planes, legends tell of pitched battles, desperate last stands, and near massacres turned in the favor of the innocent by the sudden appearance of Vildeis herself, bloody-winged and avenging. While such miraculous rescues have more to do with happenstance then omniscience, they nonetheless inf lame the passions of the _[[items/Armor Magic Abilities/Righteous|righteous]]_ across countless worlds. Those who seek to encounter the empyreal lord of devotion, _sacrifice_, and scars must follow rumors of her passing, usually spoken by awed beings and crippled fiends along the fringes of reality’s darkest outlands.

Nearly as well known as the Cardinal Martyr herself are her morbid trappings—miles of stained bandages, scars etched and re-etched in the shapes of celestial runes, and a _dagger_ that drips with her blood as often as that of her enemies. Of these, her _dagger_ _Cicatrix_ is the most infamous, a black blade like a thorn dropped from some gigantic iron rose, which the empyreal lord used to blind herself. Tales tell that she uses her blade not just to slay the wicked and share her blindness, but to carve the runes that crisscross her body upon others, infusing them with the compulsion to battle evil even if previously there was no such desire.