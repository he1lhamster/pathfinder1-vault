---
cssclass: [monsters]
title1: Encantado
desc_short: This graceful creature combines the features of a human and a river dolphin.
title2: Encantado
CR: 8
sources:
- name: Bestiary 5
  page: 110
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 4800
alignment: CN
size: Medium
type: fey
subtypes:
- shapechanger
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 21
  touch: 20
  flat_footed: 16
  components:
    deflection: 5
    dex: 5
    natural: 1
HP:
  HP: 95
  long: 10d6+60
saves:
  fort: 13
  ref: 17
  will: 16
DR:
- amount: 10
  weakness: cold iron
speeds:
  base: 30
  swim: 80
attacks:
  melee:
  - - text: slam +10 (1d4+4 plus intoxication)
      entries:
      - - damage: 1d4+4
        - effect: intoxication
      attack: slam
      bonus:
      - 10
  - - text: spear +8 (1d8+4/×3)
      entries:
      - - damage: 1d8+4
          crit_multiplier: 3
      attack: spear
      bonus:
      - 8
  ranged:
  - - text: spear +10 (1d8+3/×3)
      entries:
      - - damage: 1d8+3
          crit_multiplier: 3
      attack: spear
      bonus:
      - 10
spell_like_abilities:
  entries:
  - name: charm person
    source: default
    freq: At will
    DC: 16
  - name: suggestion
    source: default
    freq: At will
    DC: 18
  - name: unnatural lust
    source: default
    freq: At will
    DC: 17
  - name: charm monster
    source: default
    freq: 3/day
    DC: 18
  - name: confusion
    source: default
    freq: 3/day
    DC: 19
  - name: daze monster
    source: default
    freq: 3/day
    DC: 17
  - name: control weather
    source: default
    freq: 1/week
  sources:
  - name: default
    CL: 10
    concentration: 15
ability_scores:
  STR: 16
  DEX: 21
  CON: 20
  INT: 13
  WIS: 18
  CHA: 21
BAB: 5
CMB: 10
CMD: 28
CMD_other: can't be tripped
feats:
- name: Agile Maneuvers
- name: Deceitful
- name: Improved Initiative
- name: Toughness
- name: Weapon Finesse
skills:
  Bluff: 22
  Diplomacy: 18
  Disguise: 7
  Escape Artist: 18
  Knowledge (local): 9
  Perception: 17
  Perform (dance): 13
  Perform (sing): 13
  Sense Motive: 11
  Stealth: 18
  Swim: 15
languages:
- Common
- Sylvan
- speak with animals
special_qualities:
- change shape (dolphin or Medium humanoid; alter self or beast shape I)
- enchanting grace
- hold breath
ecology:
  environment: warm rivers
  organization: solitary
  treasure_type: standard
  treasure:
  - spear
  - other treasure
special_abilities:
  Enchanting Grace (Su): An encantado adds its Charisma bonus as a racial bonus on
    all of its saving throws, and as a deflection bonus to its Armor Class.
  Intoxication (Su): An encantado's slam attack affects its target as if the target
    had overindulged, causing the target to gain the sickened condition for 1 hour.
    A target already sickened by an encantado's intoxication instead becomes nauseated
    for 1d4 rounds.
desc_long: |-
  When warm, humid nights in the jungle turn into jubilant celebrations, one can be sure that an encantado can be found nearby. These fey live on the fringes of humanoid societies. They are attracted to parties, and change form into attractive humanoids to infiltrate celebrations. Skilled musicians and dancers, encantados blend in to the festivities seamlessly. When encantados shapeshift, their blowholes are still present, so they usually wear hats or wigs, or arrange their hair into elaborate coiffures, to conceal this feature. When in dolphin form, encantados can still manipulate objects with their flippers as if the flippers were hands.

   Many encantados are kind creatures who want only to celebrate joy, but others take their inclinations to influence others to an extreme, kidnapping the objects of their obsession and taking them away to their river dens. Some suffer from extreme narcissism.

   Encantados often take levels in bard or druid, while some cruel encantados become enchanters or mesmerists.

---

# Encantado
This graceful creature combines the features of a human and a river _[[monsters/Dolphin|dolphin]]_.
**Source** Bestiary 5 pg. 110
**XP** 4,800

CN Medium fey (shapechanger)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17

##### Defense

**AC** 21, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+5 _[[spells/Deflection|deflection]]_, +5 Dex, +1 natural)
**hp** 95 (10d6+60)
**Fort** +13, **Ref** +17, **Will** +16
**DR** 10/cold iron

##### Offense
**Speed** 30 ft., swim 80 ft.
**Melee** slam +10 (1d4+4 plus intoxication) or _[[items/Weapon/Spear|spear]]_ +8 (1d8+4/×3)
**Ranged** _spear_ +10 (1d8+3/×3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +15)
At will—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Suggestion|suggestion]]_ (DC 18), _[[spells/Unnatural Lust|unnatural lust]]_ (DC 17)
 3/day—_[[spells/Charm Monster|charm monster]]_ (DC 18), _[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Daze Monster|daze monster]]_ (DC 17)
 1/week—_[[spells/Control Weather|control weather]]_

##### Statistics
**Str** 16, **Dex** 21, **Con** 20, **Int** 13, **Wis** 18, **Cha** 21
**Base Atk** +5; **CMB** +10; **CMD** 28 (can’t be tripped)
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Deceitful|Deceitful]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +22, Diplomacy +18, Disguise +7, Escape Artist +18, Knowledge (local) +9, Perception +17, Perform (dance) +13, Perform (sing) +13, Sense Motive +11, Stealth +18, Swim +15
**Languages** Common, Sylvan; _[[spells/Speak with Animals|speak with animals]]_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_dolphin_ or _Medium_ humanoid; _[[spells/Alter Self|alter self]]_ or _[[spells/Beast Shape I|beast shape I]]_), enchanting _[[spells/Grace|grace]]_, _[[universal monster rules/Hold Breath|hold breath]]_

##### Ecology

**Environment** warm rivers
**Organization** solitary
**Treasure** standard (_spear_, other treasure)

### Special Abilities

**Enchanting _Grace_ (Su)** An _[[monsters/Encantado|encantado]]_ adds its Charisma bonus as a racial bonus on all of its saving throws, and as a _deflection_ bonus to its Armor Class.

**Intoxication (Su)** An _encantado_’s slam attack affects its target as if the target had overindulged, causing the target to gain the _[[conditions/Sickened|sickened]]_ condition for 1 hour. A target already _sickened_ by an _encantado_’s intoxication instead becomes _[[conditions/Nauseated|nauseated]]_ for 1d4 rounds.

##### Description

When warm, humid nights in the jungle turn into jubilant celebrations, one can be sure that an _encantado_ can be found nearby. These fey live on the fringes of humanoid societies. They are attracted to parties, and change form into attractive humanoids to infiltrate celebrations. Skilled musicians and dancers, encantados _[[spells/Blend|blend]]_ in to the festivities seamlessly. When encantados shapeshift, their blowholes are still present, so they usually wear hats or wigs, or arrange their hair into elaborate coiffures, to conceal this feature. When in _dolphin_ form, encantados can still manipulate objects with their flippers as if the flippers were hands.

Many encantados are kind creatures who want only to celebrate joy, but others take their inclinations to influence others to an extreme, kidnapping the objects of their obsession and taking them away to their river dens. Some suffer from extreme narcissism.

Encantados often take levels in _[[classes/Bard|bard]]_ or _[[classes/Druid|druid]]_, while some _[[items/Weapon Magic Abilities/Cruel|cruel]]_ encantados become enchanters or mesmerists.