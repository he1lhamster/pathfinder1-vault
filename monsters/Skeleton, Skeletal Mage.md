---
cssclass: [monsters]
title1: Skeleton, Skeletal Mage
title2: Skeletal Mage
CR: 5
sources:
- name: 'Pathfinder #44: Trial of the Beast'
  page: 86
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/carrionCrown/v5748btpy8j5s
XP: 1600
race: Human
classes:
- skeletal mage necromancer 3
alignment: NE
size: Medium
type: undead
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 18
  touch: 12
  flat_footed: 16
  components:
    armor: 4
    dex: 2
    natural: 2
HP:
  HP: 38
  long: 2d8+3d6+18
  HD: 5
saves:
  fort: 2
  ref: 4
  will: 8
defensive_abilities:
- channel resistance +4
DR:
- amount: 5
  weakness: bludgeoning
immunities:
- cold
- undead traits
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk dagger +5 (1d4+1/19-20)
      entries:
      - - damage: 1d4+1
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 5
    - text: claw -1 (1d4)
      entries:
      - - damage: 1d4
      attack: claw
      bonus:
      - -1
  - - text: 2 claws +4 (1d4+1)
      entries:
      - - damage: 1d4+1
      count: 2
      attack: claws
      bonus:
      - 4
  - - text: spectral hand +6 touch (by touch spell)
      entries:
      - - effect: by touch spell
      attack: spectral hand
      bonus:
      - 6
      touch: true
  ranged:
  - - text: ray +4 ranged touch (by spell)
      entries:
      - - effect: by spell
      attack: ray
      bonus:
      - 4
      touch: true
  special:
  - channel negative energy (DC 13, 6/day, command undead only)
spell_like_abilities:
  entries:
  - name: grave touch
    source: default
    freq: 6/day
    other: 1 round
  sources:
  - name: default
    CL: 3
    concentration: 6
spells:
  entries:
  - name: ghoul touch
    source: Skeletal Mage Necromancer
    level: 2
    DC: 17
  - name: scorching ray
    source: Skeletal Mage Necromancer
    level: 2
  - name: spectral hand
    source: Skeletal Mage Necromancer
    level: 2
  - name: chill touch
    source: Skeletal Mage Necromancer
    level: 1
    DC: 16
  - name: mage armor
    source: Skeletal Mage Necromancer
    level: 1
  - name: magic missile
    source: Skeletal Mage Necromancer
    level: 1
  - name: ray of enfeeblement
    source: Skeletal Mage Necromancer
    level: 1
    DC: 16
  - name: detect magic
    source: Skeletal Mage Necromancer
    level: 0
  - name: mage hand
    source: Skeletal Mage Necromancer
    level: 0
  - name: ray of frost
    source: Skeletal Mage Necromancer
    level: 0
  - name: read magic
    source: Skeletal Mage Necromancer
    level: 0
  - name: touch of fatigue
    source: Skeletal Mage Necromancer
    level: 0
    DC: 15
  sources:
  - name: Skeletal Mage Necromancer
    type: prepared
    CL: 3
    concentration: 6
    slots:
      0: at-will
    opposition_schools:
    - enchantment
    - illusion
ability_scores:
  STR: 12
  DEX: 15
  CON:
  INT: 16
  WIS: 12
  CHA: 15
BAB: 2
CMB: 3
CMD: 15
feats:
- name: Combat Casting
- name: Command Undead
- is_bonus: true
  name: Improved Initiative
- name: Scribe Scroll
- is_bonus: true
  name: Silent Spell
- name: Spell Focus (necromancy)
- name: Toughness
- name: Weapon Finesse
skills:
  Intimidate: 8
  Knowledge (arcana): 11
  Knowledge (religion): 11
  Perception: 8
  Sense Motive: 9
  Spellcraft: 11
  Stealth: 10
languages:
- Abyssal
- Common
- Draconic
- Undercommon
special_qualities:
- arcane bond (skull)
ecology:
  environment: any
  organization: solitary or pair
  treasure_type: NPC Gear
  treasure:
  - masterwork dagger
  - cloak of resistance +1
  - skull
  - spell component pouch
  - spellbook
  - 348 gp
desc_long: Skeletal mages are minor spellcasters (typically 5th-level or less) who
  have retained both their intelligence and their spellcasting abilities. These variant
  skeletal champions gain Silent Spell as a bonus feat. Like skeletal champions, skeletal
  mages cannot be created with animate dead-they only arise under rare conditions
  or through ancient, esoteric rituals.

---

# Skeleton, Skeletal Mage

**Source** Pathfinder #44: Trial of the Beast pg. 86
**XP** 1,600
Human skeletal mage necromancer 3

NE Medium undead
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +8

##### Defense

**AC** 18, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 armor, +2 Dex, +2 natural)
**hp** 38 (5 HD; 2d8+3d6+18)
**Fort** +2, **Ref** +4, **Will** +8
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 5/bludgeoning; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +5 (1d4+1/19-20), claw -1 (1d4) or 2 claws +4 (1d4+1) or _[[spells/Spectral Hand|spectral hand]]_ +6 touch (by touch spell)
**Ranged** ray +4 ranged touch (by spell)
**Special Attacks** channel negative energy (DC 13, 6/day, _[[spells/Command Undead|command undead]]_ only)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +6)
6/day - grave touch (1 round)
**Spells Prepared** (CL 3rd; concentration +6)
2nd — _[[spells/Ghoul touch|ghoul touch]]_ (DC 17), _[[spells/Scorching Ray|scorching ray]]_, _spectral hand_
1st — _[[spells/Chill Touch|chill touch]]_ (DC 16), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 16)
0 (at will) — _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 15)
**Opposition Schools** Enchantment, Illusion

##### Statistics
**Str** 12, **Dex** 15, **Con** —, **Int** 16, **Wis** 12, **Cha** 15
**Base Atk** +2; **CMB** +3; **CMD** 15
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Command Undead_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (necromancy), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Intimidate +8, Knowledge (arcana) +11, Knowledge (religion) +11, Perception +8, Sense Motive +9, Spellcraft +11, Stealth +10
**Languages** Abyssal, Common, Draconic, Undercommon
**SQ** arcane bond (skull)

##### Ecology

**Environment** any
**Organization** solitary or pair
**Treasure** NPC Gear (masterwork _dagger_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, skull, _[[items/Mundane/Spell component pouch|spell component pouch]]_, _[[items/Mundane/Spellbook|spellbook]]_, 348 gp)

##### Description

Skeletal mages are minor spellcasters (typically 5th-level or less) who have retained both their intelligence and their spellcasting abilities. These variant skeletal champions gain _Silent Spell_ as a bonus feat. Like skeletal champions, skeletal mages cannot be created with _[[spells/Animate Dead|animate dead]]_—they only arise under rare conditions or through ancient, esoteric rituals.