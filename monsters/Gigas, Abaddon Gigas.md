---
cssclass: [monsters]
title1: Gigas, Abaddon Gigas
desc_short: This lurching mass of spiked iron armor, rotting translucent flesh, and
  twisted black thorns resembles a dead giant with the head of an oversized boar.
title2: Abaddon Gigas
CR: 17
sources:
- name: 'Pathfinder #96: Shadow of the Storm Tyrant'
  page: 86
  link: http://paizo.com/products/btpy9et9?Pathfinder-Adventure-Path-96-Shadow-of-the-Storm-Tyrant
XP: 102400
alignment: NE
size: Gargantuan
type: humanoid
subtypes:
- evil
- extraplanar
- giant
initiative:
  bonus: 8
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 33
  touch: 9
  flat_footed: 30
  components:
    armor: 11
    dex: 3
    natural: 13
    size: -4
HP:
  HP: 241
  long: 21d8+147
saves:
  fort: 19
  ref: 11
  will: 15
defensive_abilities:
- rock catching
DR:
- amount: 10
  weakness: good
immunities:
- acid
- death effects
resistances:
  cold: 10
  electricity: 10
  fire: 10
  sonic: 10
speeds:
  base: 45
  base_other: 60 ft. without armor
attacks:
  melee:
  - - text: +3 wounding adamantine greatsword +30/+25/+20 (6d6+27 plus energy drain/19-20)
      entries:
      - - damage: 6d6+27
          crit_range: 19-20
        - effect: energy drain
      attack: +3 wounding adamantine greatsword
      bonus:
      - 30
      - 25
      - 20
  - - text: +5 nullifying adamantine spiked gauntlet +32/+27/+22 (2d6+21 plus energy
        drain)
      entries:
      - - damage: 2d6+21
        - effect: energy drain
      attack: +5 nullifying adamantine spiked gauntlet
      bonus:
      - 32
      - 27
      - 22
  - - text: +5 unholy adamantine quarterstaff +32/+27/+22 (3d6+29 plus energy drain)
      entries:
      - - damage: 3d6+29
        - effect: energy drain
      attack: +5 unholy adamantine quarterstaff
      bonus:
      - 32
      - 27
      - 22
  - - text: +3 cruel keen scythe +30/+25/+20 (4d6+27 plus energy drain/19-20/×4)
      entries:
      - - damage: 4d6+27
          crit_range: 19-20
          crit_multiplier: 4
        - effect: energy drain
      attack: +3 cruel keen scythe
      bonus:
      - 30
      - 25
      - 20
  ranged:
  - - text: rock +15 (4d6+24)
      entries:
      - - damage: 4d6+24
      attack: rock
      bonus:
      - 15
  special:
  - devour souls
  - energy drain (2 levels, DC 26)
  - rock throwing (160 ft.)
  - vile weapon
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: fear
    source: default
    freq: At will
    DC: 20
  - name: chain lightning
    source: default
    freq: 3/day
    DC: 22
  - name: cone of cold
    source: default
    freq: 3/day
    DC: 21
  - name: dimensional anchor
    source: default
    freq: 3/day
  - name: flame strike
    source: default
    freq: 3/day
    DC: 21
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: horrid wilting
    source: default
    freq: 3/day
    DC: 24
  - name: unholy blight
    source: default
    freq: 3/day
    DC: 20
  - name: destruction
    source: default
    freq: 1/day
    DC: 23
  - name: energy drain
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 17
    concentration: 23
ability_scores:
  STR: 42
  DEX: 19
  CON: 25
  INT: 15
  WIS: 22
  CHA: 22
BAB: 15
CMB: 35
CMB_other: +37 bull rush, +39 overrun
CMD: 49
CMD_other: 51 vs. bull rush and overrun
feats:
- name: Awesome Blow
- name: Cleave
- name: Combat Reflexes
- name: Great Cleave
- name: Greater Overrun
- name: Improved Bull Rush
- name: Improved Initiative
- name: Improved Overrun
- name: Iron Will
- name: Power Attack
- name: Stand Still
skills:
  Climb: 37
  Intimidate: 30
  Knowledge (planes): 12
  Perception: 30
  Sense Motive: 17
languages:
- Abyssal
- Giant
- Infernal
special_qualities:
- planar empowerment
ecology:
  environment: any (Abaddon)
  organization: solitary
  treasure_type: standard
  treasure:
  - +2 mithral full plate
  - other treasure
special_abilities:
  Devour Souls (Su): |-
    As a standard action once every 1d4 rounds, an Abaddon gigas can drain the souls from all living creatures within 60 feet that are not native to Abaddon. Such creatures must succeed at a DC 26 Fortitude save or gain 1d4 negative levels.

     If even one creature is affected, the Abaddon gigas gains fast healing 15 for 15 rounds. If a creature dies from an Abaddon gigas's energy drain special attack, energy drain spell, or devour souls attack, the Abaddon gigas devours that creature's soul, gaining the benefits of death knell at a caster level equal to the dead creature's HD. Such a creature cannot be raised or resurrected by any means until the Abaddon gigas is slain. The save DC is Charisma-based.
  Planar Empowerment (Su): 'While on the plane of Abaddon, an Abaddon gigas can cast
    each of the following as a spell-like ability once per day: blasphemy (DC 28),
    earthquake (DC 29), and unholy aura (DC 29) . If the gigas ventures onto another
    plane, it can't use these abilities (though its other spell-like abilities remain
    available). The save DCs for these spell-like abilities are Charisma-based and
    include a +5 racial bonus.'
  Vile Weapon (Su): As a swift action, an Abaddon gigas can transform its weapon into
    a +3 wounding adamantine greatsword, a +5 nullifyingUE adamantine spiked gauntlet,
    a +5 unholy adamantine quarterstaff, a +3 cruelUE keen scythe, or a +3 weapon
    of any other kind.
desc_long: |-
  Abaddon gigas are megalithic extraplanar giants that roam Abaddon and embody the same vile energies that permeate that plane. Their cruel forms and unusual powers give them nefarious reputations, and few giant hunters-even among those who traverse the Great Beyond-would willingly seek out one of these monstrosities.

  An Abaddon gigas stands over 50 feet tall and weighs 30 tons, not including the weight of its enormous armor.

---

# Gigas, Abaddon Gigas
This lurching mass of spiked iron armor, rotting translucent flesh, and twisted black thorns resembles a dead giant with the head of an oversized _[[monsters/Boar|boar]]_.
**Source** Pathfinder #96: _[[items/Armor Magic Abilities/Shadow|Shadow]]_ of the Storm Tyrant pg. 86
**XP** 102,400

NE Gargantuan humanoid (evil, extraplanar, giant)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +30

##### Defense

**AC** 33, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 30 (+11 armor, +3 Dex, +13 natural, –4 size)
**hp** 241 (21d8+147)
**Fort** +19, **Ref** +11, **Will** +15
**Defensive Abilities** _[[universal monster rules/Rock Catching|rock catching]]_; **DR** 10/good; **Immune** acid, death effects; **Resist** cold 10, electricity 10, fire 10, sonic 10

##### Offense
**Speed** 45 ft. (60 ft. without armor)
**Melee** +3 _[[items/Weapon Magic Abilities/Wounding|wounding]]_ adamantine _[[items/Weapon/Greatsword|greatsword]]_ +30/+25/+20 (6d6+27 plus energy drain/19–20) or +5 _[[items/Weapon Magic Abilities/Nullifying|nullifying]]_ adamantine _[[items/Weapon/Spiked gauntlet|spiked gauntlet]]_ +32/+27/+22 (2d6+21 plus _[[universal monster rules/Energy Drain|energy drain]]_) or +5 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ adamantine _[[items/Weapon/Quarterstaff|quarterstaff]]_ +32/+27/+22 (3d6+29 plus _energy drain_) or +3 _[[items/Weapon Magic Abilities/Cruel|cruel]]_ _[[items/Weapon Magic Abilities/Keen|keen]]_ _[[items/Weapon/Scythe|scythe]]_ +30/+25/+20 (4d6+27 plus energy drain/19–20/×4)
**Ranged** rock +15 (4d6+24)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** devour souls, _energy drain_ (2 levels, DC 26), _[[universal monster rules/Rock Throwing|rock throwing]]_ (160 ft.), vile weapon
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +23)
At will—_[[universal monster rules/Fear|fear]]_ (DC 20)
3/day—_[[spells/Chain Lightning|chain lightning]]_ (DC 22), _[[spells/Cone of Cold|cone of cold]]_ (DC 21), _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Flame Strike|flame strike]]_ (DC 21), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Horrid Wilting|horrid wilting]]_ (DC 24), _[[spells/Unholy Blight|unholy blight]]_ (DC 20)
1/day—_[[spells/Destruction|destruction]]_ (DC 23), _energy drain_ (DC 25)

##### Statistics
**Str** 42, **Dex** 19, **Con** 25, **Int** 15, **Wis** 22, **Cha** 22
**Base Atk** +15; **CMB** +35 (+37 bull rush, +39 overrun); **CMD** 49 (51 vs. bull rush and overrun)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Greater Overrun|Greater Overrun]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Stand Still|Stand Still]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +37, Intimidate +30, Knowledge (planes) +12, Perception +30, Sense Motive +17
**Languages** Abyssal, Giant, Infernal
**SQ** _[[items/Weapon Magic Abilities/Planar|planar]]_ empowerment

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary
**Treasure** standard (+2 mithral _[[items/Armor/Full plate|full plate]]_, other treasure)

### Special Abilities

**Devour Souls (Su)** As a standard action once every 1d4 rounds, an Abaddon gigas can drain the souls from all living creatures within 60 feet that are not native to Abaddon. Such creatures must succeed at a DC 26 Fortitude save or gain 1d4 negative levels.

If even one creature is affected, the Abaddon gigas gains _[[universal monster rules/Fast Healing|fast healing]]_ 15 for 15 rounds. If a creature dies from an Abaddon gigas’s _energy drain_ special attack, _energy drain_ spell, or devour souls attack, the Abaddon gigas devours that creature’s soul, gaining the benefits of _[[spells/Death Knell|death knell]]_ at a caster level equal to the dead creature’s HD. Such a creature cannot be raised or resurrected by any means until the Abaddon gigas is slain. The save DC is Charisma-based.

**_Planar_ Empowerment (Su)** While on the plane of Abaddon, an Abaddon gigas can cast each of the following as a spell-like ability once per day: _[[spells/Blasphemy|blasphemy]]_ (DC 28), _[[spells/Earthquake|earthquake]]_ (DC 29), and _[[spells/Unholy Aura|unholy aura]]_ (DC 29) . If the gigas ventures onto another plane, it can’t use these abilities (though its other _spell-like abilities_ remain available). The save DCs for these _spell-like abilities_ are Charisma-based and include a +5 racial bonus.

**Vile Weapon (Su)** As a swift action, an Abaddon gigas can transform its weapon into a +3 _wounding_ adamantine _greatsword_, a +5 _nullifying_ adamantine _spiked gauntlet_, a +5 _unholy_ adamantine _quarterstaff_, a +3 _cruel_ _keen_ _scythe_, or a +3 weapon of any other kind.

##### Description

Abaddon gigas are megalithic extraplanar giants that roam Abaddon and embody the same vile energies that permeate that plane. Their _cruel_ forms and unusual powers give them nefarious reputations, and few giant hunters—even among those who traverse the Great Beyond—would willingly seek out one of these monstrosities.

An Abaddon gigas stands over 50 feet tall and weighs 30 tons, not including the weight of its enormous armor.