---
cssclass: [monsters]
title1: Aranea
desc_short: 'This bloated spider has a hunchbacked body and a gleam of intelligence
  in its multiple eyes. '
title2: Aranea
CR: 4
sources:
- name: Bestiary 2
  page: 30
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 1200
alignment: N
size: Medium
type: magical beast
subtypes:
- shapechanger
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 20
  touch: 13
  flat_footed: 17
  components:
    armor: 4
    dex: 3
    natural: 3
HP:
  HP: 37
  long: 5d10+10
saves:
  fort: 6
  ref: 7
  will: 4
speeds:
  base: 50
  climb: 30
attacks:
  melee:
  - - text: bite +8 (1d6 plus poison)
      entries:
      - - damage: 1d6
        - effect: poison
      attack: bite
      bonus:
      - 8
  special:
  - web (+8 ranged, DC 14, hp 5)
spells:
  entries:
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 14
  - name: mage armor
    source: Sorcerer
    level: 1
    other: 1 already cast
  - name: silent image
    source: Sorcerer
    level: 1
    DC: 14
  - name: sleep
    source: Sorcerer
    level: 1
    DC: 14
  - name: daze
    source: Sorcerer
    level: 0
    DC: 13
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 13
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 5
    concentration: 8
    slots:
      2: 5
      1: 7
      0: at-will
ability_scores:
  STR: 11
  DEX: 17
  CON: 14
  INT: 14
  WIS: 13
  CHA: 16
BAB: 5
CMB: 5
CMD: 18
feats:
- is_bonus: true
  name: Eschew Materials
- name: Improved Initiative
- name: Iron Will
- name: Weapon Finesse
skills:
  Acrobatics: 9
    jump: 17
  Climb: 14
  Escape Artist: 8
  Knowledge (arcana): 7
  Perception: 9
  Stealth: 9
  _racial_mods:
    Acrobatics:
      _: 2
    Perception:
      _: 2
languages:
- Common
- Sylvan
special_qualities:
- change shape (humanoid; alter self)
ecology:
  environment: tropical forests
  organization: solitary or colony (2-6)
  treasure_type: standard
special_abilities:
  Change Shape (Su): An aranea can take the form of a Small or Medium humanoid or
    spider-humanoid hybrid. In humanoid form, an aranea cannot use its bite, web,
    or poison. In spider-humanoid hybrid form, an aranea looks like a humanoid with
    spidery fangs and spinnerets, with the latter typically located at the small of
    its back. The aranea retains its bite attack, webs, and poison in this form, and
    can wield weapons and wear armor. When in humanoid or hybrid form, an aranea's
    speed is 30 feet and it has no climb speed.
  Poison (Ex): Bite-injury; save Fort DC 14; frequency 1/round for 6 rounds; effect
    1d3 Strength; cure 1 save.
  Spells: An aranea casts spells as a 5th-level sorcerer, but does not gain any additional
    abilities, such as a sorcerous bloodline.
desc_long: |-
  An aranea is an intelligent, shapechanging spider with sorcerous powers. In its natural form, an aranea resembles a humpbacked spider a little bigger than a human, and weighs about 150 pounds. The hump on its back houses the aranea's brain. All araneas have a single alternate form as well-this alternate form is that of a Small or Medium humanoid. Although an aranea can assume a spider-hybrid variant of this form, it cannot use its change shape ability to assume multiple humanoid forms-this additional shape is locked into one unique appearance. 

  Araneas typically gather in small colonies of two to six individuals, making webbed nests high in trees. These colonies work together to research magic, and may change membership many times over as individuals leave to pursue their own studies and are replaced by newer members. A single aranea may take on humanoid form and live for years in a humanoid community, never revealing its true nature. Though araneas generally prefer to be left alone, they often prove quite knowledgeable about the ways of magic, and if approached peacefully may be willing to share their expertise for the right price (typically a magic item or some service). 

  Skilled spellcasters, araneas try to avoid physical combat and use their webs and spells when they can. Rather than kill their enemies, araneas often subdue opponents and hold them for ransom.

---

# Aranea
This bloated spider has a hunchbacked body and a gleam of intelligence in its multiple eyes.

**Source** Bestiary 2 pg. 30
**XP** 1,200

N Medium magical beast (shapechanger)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9

##### Defense

**AC** 20, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +3 Dex, +3 natural)
**hp** 37 (5d10+10)
**Fort** +6, **Ref** +7, **Will** +4

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** bite +8 (1d6 plus poison)
**Special Attacks** web (+8 ranged, DC 14, hp 5)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 5th; concentration +8)
2nd (5/day)—_[[spells/Invisibility|invisibility]]_, _[[spells/Mirror Image|mirror image]]_
1st (7/day)—_[[spells/Charm Person|charm person]]_ (DC 14), _[[spells/Mage Armor|mage armor]]_ (1 already cast), _[[spells/Silent Image|silent image]]_ (DC 14), sleep (DC 14)
0 (at will)—_[[spells/Daze|daze]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 13), light, _[[spells/Mage Hand|mage hand]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 11, **Dex** 17, **Con** 14, **Int** 14, **Wis** 13, **Cha** 16
**Base Atk** +5; **CMB** +5; **CMD** 18
**Feats** _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +9 (+17 _[[spells/Jump|jump]]_), _Climb_ +14, Escape Artist +8, Knowledge (arcana) +7, Perception +9, Stealth +9; **Racial Modifiers** +2 Acrobatics, +2 Perception
**Languages** Common, Sylvan
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (humanoid; _[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** tropical forests
**Organization** solitary or colony (2–6)
**Treasure** standard

### Special Abilities

**_Change Shape_ (Su)** An _[[monsters/Aranea|aranea]]_ can take the form of a Small or _Medium_ humanoid or spider-humanoid hybrid. In humanoid form, an _aranea_ cannot use its bite, web, or poison. In spider-humanoid hybrid form, an _aranea_ looks like a humanoid with spidery fangs and spinnerets, with the latter typically located at the small of its back. The _aranea_ retains its bite attack, webs, and poison in this form, and can wield weapons and wear armor. When in humanoid or hybrid form, an _aranea_’s speed is 30 feet and it has no _climb_ speed.

**Poison (Ex)** Bite—injury; save Fort DC 14; frequency 1/round for 6 rounds; effect 1d3 Strength; cure 1 save.
**Spells** An _aranea_ casts spells as a 5th-level _sorcerer_, but does not gain any additional abilities, such as a sorcerous bloodline.

##### Description

An _aranea_ is an intelligent, shapechanging spider with sorcerous powers. In its natural form, an _aranea_ resembles a humpbacked spider a little bigger than a human, and weighs about 150 pounds. The hump on its back houses the _aranea_’s brain. All araneas have a single alternate form as well—this alternate form is that of a Small or _Medium_ humanoid. Although an _aranea_ can assume a spider-hybrid variant of this form, it cannot use its _change shape_ ability to assume multiple humanoid forms—this additional shape is locked into one unique appearance.

Araneas typically gather in small colonies of two to six individuals, making webbed nests high in trees. These colonies work together to research magic, and may change membership many times over as individuals leave to pursue their own studies and are replaced by newer members. A single _aranea_ may take on humanoid form and live for years in a humanoid community, never revealing its true nature. Though araneas generally prefer to be left alone, they often prove quite knowledgeable about the ways of magic, and if approached peacefully may be willing to share their expertise for the right price (typically a magic item or some service).

Skilled spellcasters, araneas try to avoid physical combat and use their webs and spells when they can. Rather than kill their enemies, araneas often subdue opponents and hold them for ransom.