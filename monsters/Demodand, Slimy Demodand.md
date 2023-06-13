---
cssclass: [monsters]
title1: Demodand, Slimy Demodand
desc_short: This muscular, frog-headed humanoid has tattered flesh hanging from its
  batlike wings and is covered in a viscous slime.
title2: Slimy Demodand
CR: 16
sources:
- name: Bestiary 3
  page: 70
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 76800
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demodand
- evil
- extraplanar
initiative:
  bonus: 4
senses:
  darkvision: 120
  detect good: true
  detect magic: true
  see invisibility: true
auras:
- name: stench
  DC: 26
  duration: 1d6 rounds
AC:
  AC: 30
  touch: 13
  flat_footed: 27
  components:
    armor: 6
    dex: 3
    natural: 11
HP:
  HP: 241
  long: 21d10+126
saves:
  fort: 18
  ref: 13
  will: 14
  other: +4 vs. divine spells
DR:
- amount: 10
  weakness: good and magic
immunities:
- acid
- poison
resistances:
  cold: 10
  fire: 10
SR: 27
speeds:
  base: 20
  fly: 40
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +30 (1d10+9 plus 2d6 acid)
      entries:
      - - damage: 1d10+9
        - damage: 2d6
          type: acid
      attack: bite
      bonus:
      - 30
    - text: 2 claws +30 (2d6+13/19-20 plus 2d6 acid and grab)
      entries:
      - - damage: 2d6+13
          crit_range: 19-20
        - damage: 2d6
          type: acid
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 30
  special:
  - acid
  - dread claws
  - faith-stealing strike (DC 23)
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
  - name: detect thoughts
    source: default
    freq: At will
    DC: 15
  - name: fear
    source: default
    freq: At will
    DC: 17
  - name: acid fog
    source: default
    freq: 3/day
  - name: greater dispel magic
    source: default
    freq: 3/day
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: tarry demodands
      amount: 1d4
      chance: 50%
  sources:
  - name: default
    CL: 16
    concentration: 19
ability_scores:
  STR: 28
  DEX: 18
  CON: 23
  INT: 14
  WIS: 15
  CHA: 17
BAB: 21
CMB: 30
CMB_other: +34 grapple
CMD: 44
feats:
- name: Bleeding Critical
- name: Blind-Fight
- name: Critical Focus
- name: Flyby Attack
- name: Greater Vital Strike
- name: Improved Critical (claw)
- name: Improved Vital Strike
- name: Intimidating Prowess
- name: Lightning Reflexes
- name: Power Attack
- name: Vital Strike
skills:
  Acrobatics: 8
  Bluff: 27
  Climb: 16
  Fly: 25
  Intimidate: 36
  Knowledge (arcana): 13
  Knowledge (planes): 13
  Sense Motive: 26
  Spellcraft: 20
  Stealth: 25
  Survival: 20
  Perception: 2
languages:
- Abyssal
- Celestial
- Common
special_qualities:
- heretical soul
ecology:
  environment: any (Abyss)
  organization: solitary or slaving party (2 slimy demodands and 2-5 tarry demodands)
  treasure_type: standard
  treasure:
  - masterwork breastplate
  - other treasure
special_abilities:
  Acid (Su): A slimy demodand is coated in an ever-dripping layer of acid that deals
    an extra 2d6 points of acid damage on a successful natural attack. In addition,
    opponents that successfully strike a slimy demodand with an unarmed strike or
    natural attack take 2d6 points of acid damage.
  Dread Claws (Ex): A slimy demodand adds 1-1/2 times its strength bonus on all attack
    rolls made when using its claws.
desc_long: |-
  Slimy demodands are more muscular than shaggy demodands, but aren't as lithe or quick as their tarry brethren. They have froglike heads, similar to those of the shaggy demodands, but their constantly darting eyes give them a more feral look. A slimy demodand stands 6 feet tall and weighs 500 pounds.

  Slimy demodands often serve as shock troops in demodand armies, but they are also frequently put in charge of gathering and keeping slaves. Slimy demodands have no magical mind control powers, but prefer to rely upon intimidation and physical threats anyway to manage their slaves and keep them in line.

---

# Demodand, Slimy Demodand
This muscular, frog-headed humanoid has tattered flesh hanging from its batlike wings and is covered in a viscous slime.
**Source** Bestiary 3 pg. 70
**XP** 76,800
CE Medium outsider (chaotic, demodand, evil, extraplanar)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +2
**Aura** _[[universal monster rules/Stench|stench]]_ (DC 26, 1d6 rounds)

##### Defense

**AC** 30, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+6 armor, +3 Dex, +11 natural)
**hp** 241 (21d10+126)
**Fort** +18, **Ref** +13, **Will** +14; +4 vs. divine spells
**DR** 10/good and magic; **Immune** acid, poison; **Resist** cold 10, fire 10; **SR** 27

##### Offense
**Speed** 20 ft., fly 40 ft. (average)
**Melee** bite +30 (1d10+9 plus 2d6 acid), 2 claws +30 (2d6+13/19–20 plus 2d6 acid and _[[universal monster rules/Grab|grab]]_)
**Special Attacks** acid, dread claws, faith-stealing strike (DC 23)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 16th; concentration +19)
Constant—_detect good_, _detect magic_, _see invisibility_
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 15), _[[universal monster rules/Fear|fear]]_ (DC 17)
3/day—_[[spells/Acid Fog|acid fog]]_, greater _[[spells/Dispel Magic|dispel magic]]_
1/day—_[[universal monster rules/Summon|summon]]_ (level 6, 1d4 tarry demodands 50%)

##### Statistics
**Str** 28, **Dex** 18, **Con** 23, **Int** 14, **Wis** 15, **Cha** 17
**Base Atk** +21; **CMB** +30 (+34 grapple); **CMD** 44
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Intimidating Prowess|Intimidating Prowess]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +8, Bluff +27, _[[universal monster rules/Climb|Climb]]_ +16, Fly +25, Intimidate +36, Knowledge (arcana) +13, Knowledge (planes) +13, Sense Motive +26, Spellcraft +20, Stealth +25, Survival +20
**Languages** Abyssal, Celestial, Common
**SQ** _[[items/Weapon Magic Abilities/Heretical|heretical]]_ soul

##### Ecology

**Environment** any (Abyss)
**Organization** solitary or slaving party (2 slimy demodands and 2–5 tarry demodands)
**Treasure** standard (masterwork _[[items/Armor/Breastplate|breastplate]]_, other treasure)

### Special Abilities

**Acid (Su)** A slimy demodand is coated in an ever-dripping layer of acid that deals an extra 2d6 points of acid damage on a successful natural attack. In addition, opponents that successfully strike a slimy demodand with an unarmed strike or natural attack take 2d6 points of acid damage.

**Dread Claws (Ex)** A slimy demodand adds 1-1/2 times its strength bonus on all attack rolls made when using its claws.

##### Description

Slimy demodands are more muscular than shaggy demodands, but aren’t as lithe or quick as their tarry brethren. They have froglike heads, similar to those of the shaggy demodands, but their constantly darting eyes give them a more feral look. A slimy demodand stands 6 feet tall and weighs 500 pounds.

Slimy demodands often serve as _[[items/Weapon Magic Abilities/Shock|shock]]_ troops in demodand armies, but they are also frequently put in charge of gathering and keeping slaves. Slimy demodands have no magical mind control powers, but prefer to rely upon intimidation and physical threats anyway to manage their slaves and keep them in line.