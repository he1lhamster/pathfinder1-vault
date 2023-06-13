---
cssclass: [monsters]
title1: Demodand, Gristly Demodand
desc_short: This obese humanoid has a wide mouth, batlike wings, and pale fluid seeping
  from rolls of black, greasy skin.
title2: Gristly Demodand
CR: 17
sources:
- name: Bestiary 5
  page: 72
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 102400
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demodand
- evil
- extraplanar
initiative:
  bonus: 10
senses:
  darkvision: 120
  detect good: true
  detect magic: true
  see invisibility: true
AC:
  AC: 32
  touch: 16
  flat_footed: 26
  components:
    armor: 1
    dex: 6
    natural: 15
HP:
  HP: 264
  long: 23d10+138
  fast_healing: 10
saves:
  fort: 19
  ref: 15
  will: 15
  other: +4 vs. divine spells
defensive_abilities:
- fortification (50%)
DR:
- amount: 15
  weakness: good and slashing
immunities:
- acid
- poison
resistances:
  cold: 10
  fire: 10
SR: 28
speeds:
  base: 40
  fly: 50
  fly_maneuverability: average
attacks:
  melee:
  - - text: +1 vicious maul +34/+29/+24/+19 (2d6+16/19-20/×3 plus 2d6)
      entries:
      - - damage: 2d6+16
          crit_range: 19-20
          crit_multiplier: 3
        - damage: 2d6
      attack: +1 vicious maul
      bonus:
      - 34
      - 29
      - 24
      - 19
  - - text: 2 claws +33 (2d6+10)
      entries:
      - - damage: 2d6+10
      count: 2
      attack: claws
      bonus:
      - 33
  special:
  - faith-stealing strike (DC 25)
  - sacrilegious spittle
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: dimensional anchor
    source: default
    freq: At will
  - name: fear
    source: default
    freq: At will
    DC: 18
  - name: protection from good
    source: default
    freq: At will
  - name: seek thoughts
    source: default
    freq: At will
    DC: 17
  - name: quickened excruciating deformation
    source: default
    freq: 3/day
    DC: 17
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: quickened pain strike
    source: default
    freq: 3/day
    DC: 17
  - name: mass pain strike
    source: default
    freq: 1/day
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: tarry demodands
      amount: 1d4
    - name: stringy demodands
      amount: 1d2
      chance: 55%
  - name: waves of exhaustion
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 17
    concentration: 21
ability_scores:
  STR: 31
  DEX: 22
  CON: 23
  INT: 17
  WIS: 14
  CHA: 18
BAB: 23
CMB: 33
CMD: 49
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Improved Critical (maul)
- name: Improved Initiative
- name: Intimidating Prowess
- name: Lightning Reflexes
- name: Lunge
- name: Power Attack
- name: Quicken Spell-Like Ability (excruciating deformation)
- name: Quicken Spell-Like Ability (pain strike)
- name: Staggering Critical
- name: Stunning Critical
skills:
  Acrobatics: 21
  Bluff: 22
  Climb: 25
  Fly: 29
  Intimidate: 40
  Knowledge (arcana): 14
  Knowledge (planes): 14
  Knowledge (religion): 14
  Perception: 25
  Sense Motive: 20
  Spellcraft: 23
  Stealth: 29
  Survival: 25
languages:
- Abyssal
- Celestial
- Common
special_qualities:
- heretical soul
ecology:
  environment: any (Abyss)
  organization: solitary or hunting party (1 gristly demodand plus 2-5 tarry demodands)
  treasure_type: standard
  treasure:
  - mwk armored kilt
  - +1 vicious maul
  - other treasure
special_abilities:
  Sacrilegious Spittle (Ex): As a standard action once every 1d4 rounds, a gristly
    demodand can spit acidic mucus in a 30-foot cone. Creatures in the area take 15d6
    points of acid damage (DC 27 Reflex half), and are entangled on a failed save.
    Entangled creatures take 5d6 points of acid damage each round at the end of their
    turns. Creatures that take acid damage from sacrilegious spittle are also subject
    to the demodand's faith-stealing strike. Each round on its turn, an entangled
    creature may attempt a new saving throw to end the effect, as a full-round action
    that provokes attacks of opportunity. The save DC is Constitution-based.
desc_long: |-
  Gristly demodands delight in inflicting pain and suffering, eagerly fulfilling their roles in demodand culture as assassins, executioners, and torturers. These fiends conduct special missions of reconnaissance, disruption, and violent destruction, frequently leading crack units of tarry demodands into hostile lands, where they attack key demonic installations in order to subject their captives to brutal and insidious torture for the purpose of extracting information.

  A gristly demodand's skin is stretched so taut over rolls of fat and cartilaginous flesh that it continually rips and splits, though a yellow-white mucus that oozes out from within heals these superficial tears, keeping its body intact.

  A typical gristly demodand is 7 feet tall and weighs up to 600 pounds.

---

# Demodand, Gristly Demodand
This obese humanoid has a wide mouth, batlike wings, and pale fluid seeping from rolls of black, greasy skin.
**Source** Bestiary 5 pg. 72
**XP** 102,400
CE Medium outsider (chaotic, demodand, evil, extraplanar)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +25

##### Defense

**AC** 32, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+1 armor, +6 Dex, +15 natural)
**hp** 264 (23d10+138); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +19, **Ref** +15, **Will** +15; +4 vs. divine spells
**Defensive Abilities** _[[universal monster rules/Fortification|fortification]]_ (50%); **DR** 15/good and slashing; **Immune** acid, poison; **Resist** cold 10, fire 10; **SR** 28

##### Offense
**Speed** 40 ft., fly 50 ft. (average)
**Melee** +1 _[[items/Weapon Magic Abilities/Vicious|vicious]]_ maul +34/+29/+24/+19 (2d6+16/19-20/×3 plus 2d6) or 2 claws +33 (2d6+10)
**Special Attacks** faith-stealing strike (DC 25), sacrilegious spittle
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +21)
Constant—_detect good_, _detect magic_, _see invisibility_
At will—_[[spells/Dimensional Anchor|dimensional anchor]]_, _[[universal monster rules/Fear|fear]]_ (DC 18), _[[spells/Protection From Good|protection from good]]_, _[[spells/Seek Thoughts|seek thoughts]]_ (DC 17)
3/day—quickened _[[spells/Excruciating Deformation|excruciating deformation]]_ (DC 17), greater _[[spells/Dispel Magic|dispel magic]]_, quickened _[[spells/Pain Strike|pain strike]]_ (DC 17)
1/day—mass _pain strike_ (DC 19), _[[universal monster rules/Summon|summon]]_ (level 6, 1d4 tarry demodands or 1d2 stringy demodands 55%), _[[spells/Waves of Exhaustion|waves of exhaustion]]_

##### Statistics
**Str** 31, **Dex** 22, **Con** 23, **Int** 17, **Wis** 14, **Cha** 18
**Base Atk** +23; **CMB** +33; **CMD** 49
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (maul), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_excruciating deformation_), _Quicken Spell-Like Ability_ (_pain strike_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stunning Critical|Stunning Critical]]_
**Skills** Acrobatics +21, Bluff +22, _[[universal monster rules/Climb|Climb]]_ +25, Fly +29, Intimidate +40, Knowledge (arcana, planes, religion) +14, Perception +25, Sense Motive +20, Spellcraft +23, Stealth +29, Survival +25
**Languages** Abyssal, Celestial, Common
**SQ** _[[items/Weapon Magic Abilities/Heretical|heretical]]_ soul

##### Ecology

**Environment** any (Abyss)
**Organization** solitary or hunting party (1 gristly demodand plus 2-5 tarry demodands)
**Treasure** standard (mwk _[[items/Armor/Armored kilt|armored kilt]]_, +1 _vicious_ maul, other treasure)

### Special Abilities
**Sacrilegious Spittle (Ex)** As a standard action once every 1d4 rounds, a gristly demodand can spit acidic mucus in a 30-foot cone. Creatures in the area take 15d6 points of acid damage (DC 27 Reflex half), and are _[[conditions/Entangled|entangled]]_ on a failed save. _Entangled_ creatures take 5d6 points of acid damage each round at the end of their turns. Creatures that take acid damage from sacrilegious spittle are also subject to the demodand’s faith-stealing strike. Each round on its turn, an _entangled_ creature may attempt a new saving throw to end the effect, as a full-round action that provokes attacks of opportunity. The save DC is Constitution-based.

##### Description

Gristly demodands delight in inflicting pain and suffering, eagerly fulfilling their roles in demodand culture as assassins, executioners, and torturers. These fiends conduct special missions of reconnaissance, _[[items/Weapon Magic Abilities/Disruption|disruption]]_, and violent _[[spells/Destruction|destruction]]_, frequently leading crack units of tarry demodands into hostile lands, where they attack key demonic installations in order to subject their captives to brutal and insidious torture for the purpose of extracting information.

A gristly demodand’s skin is stretched so taut over rolls of fat and cartilaginous flesh that it continually rips and splits, though a yellow-white mucus that oozes out from within heals these superficial tears, keeping its body intact.

A typical gristly demodand is 7 feet tall and weighs up to 600 pounds.