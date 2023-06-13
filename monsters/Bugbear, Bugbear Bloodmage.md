---
cssclass: [monsters]
title1: Bugbear, Bugbear Bloodmage
title2: Bugbear Bloodmage
CR: 11
sources:
- name: Monster Codex
  page: 26
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 12800
race: Bugbear
classes:
- sorcerer 10
alignment: CE
size: Medium
type: humanoid
subtypes:
- goblinoid
initiative:
  bonus: 6
senses:
  darkvision: 60
  scent: true
AC:
  AC: 18
  touch: 13
  flat_footed: 15
  components:
    dex: 2
    dodge: 1
    natural: 5
HP:
  HP: 97
  long: 3d8+10d6+49
  HD: 13
saves:
  fort: 8
  ref: 11
  will: 9
resistances:
  fire: 20
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 quarterstaff +12/+7 (1d6+7)
      entries:
      - - damage: 1d6+7
      attack: +1 quarterstaff
      bonus:
      - 12
      - 7
  ranged:
  - - text: mwk shortbow +10 (1d6/×3)
      entries:
      - - damage: 1d6
          crit_multiplier: 3
      attack: mwk shortbow
      bonus:
      - 10
spell_like_abilities:
  entries:
  - name: elemental ray
    source: default
    freq: 6/day
    other: 1d6+5 fire
  - name: elemental blast
    source: default
    freq: 1/day
    other: 10d6 fire
    DC: 18
  sources:
  - name: default
    CL: 10
    concentration: 12
spells:
  entries:
  - superscripts:
    - APG
    name: fire snake
    source: Sorcerer
    level: 5
    DC: 18
  - name: black tentacles
    source: Sorcerer
    level: 4
  - name: elemental body I
    source: Sorcerer
    level: 4
  - name: fire shield
    source: Sorcerer
    level: 4
  - name: fireball
    source: Sorcerer
    level: 3
    DC: 16
  - superscripts:
    - UM
    name: howling agony
    source: Sorcerer
    level: 3
    DC: 16
  - name: protection from energy
    source: Sorcerer
    level: 3
  - name: rage
    source: Sorcerer
    level: 3
  - name: stinking cloud
    source: Sorcerer
    level: 3
    DC: 16
  - name: alter self
    source: Sorcerer
    level: 2
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: levitate
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: see invisibility
    source: Sorcerer
    level: 2
  - name: touch of idiocy
    source: Sorcerer
    level: 2
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 14
  - name: color spray
    source: Sorcerer
    level: 1
    DC: 14
  - name: enlarge person
    source: Sorcerer
    level: 1
    DC: 14
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 14
  - name: shield
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 13
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: detect poison
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 13
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 13
  sources:
  - name: Sorcerer
    type: known
    CL: 10
    concentration: 13
    slots:
      5: 3
      4: 5
      3: 6
      2: 7
      1: 7
      0: at-will
    bloodline: elemental (fire)
tactics:
  Before Combat: The bloodmage casts invisibility and positions herself where she
    can hurl spells with impunity.
  During Combat: At the start of the battle, the bloodmage casts fire snake and fireball
    on her foes. She reserves spells such as fire shield and shield to protect herself
    when she becomes the target of attacks.
ability_scores:
  STR: 18
  DEX: 15
  CON: 16
  INT: 8
  WIS: 10
  CHA: 17
BAB: 7
CMB: 11
CMD: 24
feats:
- name: Combat Casting
- name: Dodge
- name: Empower Spell
- name: Enlarge Spell
- name: Eschew Materials
- name: Improved Initiative
- name: Lightning Reflexes
- name: Point-Blank Shot
- name: Precise Shot
skills:
  Intimidate: 6
  Spellcraft: 12
  Stealth: 9
  Perception: 0
languages:
- Common
- Goblin
special_qualities:
- bloodline arcana (change energy damage spells to fire)
- stalker
gear:
  combat:
  - potion of cure moderate wounds
  other:
  - +1 quarterstaff
  - mwk dagger
  - mwk shortbow with 20 arrows
  - amulet of natural armor +2
  - cloak of resistance +1
  - headband of alluring charisma +2
  - 117 gp
ecology:
  environment: temperate mountains
desc_long: Arcane spellcasters among bugbears are typically sorcerers-few bugbears
  have enough interest or patience to follow arcane paths such as wizardry that require
  study or control. Bugbears call those with natural magical talent bloodmages, and
  treat their spellcasting ability the same as any skill-if it's useful for hurting,
  it's worth knowing. A typical bloodmage is interested in only spells that cause
  destruction and pain, plus a few supplemental spells to help her defend herself.
  Almost no bloodmages learn to create magic items.

---

# Bugbear, Bugbear Bloodmage

**Source** Monster Codex pg. 26
**XP** 12,800
_[[monsters/Bugbear|Bugbear]]_ _[[classes/Sorcerer|sorcerer]]_ 10
CE Medium humanoid (goblinoid)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +0

##### Defense

**AC** 18, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural)
**hp** 97 (13 HD; 3d8+10d6+49)
**Fort** +8, **Ref** +11, **Will** +9
**Resist** fire 20

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Quarterstaff|quarterstaff]]_ +12/+7 (1d6+7)
**Ranged** mwk _[[items/Weapon/Shortbow|shortbow]]_ +10 (1d6/×3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +12)
6/day—elemental ray (1d6+5 fire)
1/day—elemental blast (10d6 fire, DC 18)
**_Sorcerer_ Spells Known **(CL 10th; concentration +13)
5th (3/day)—_[[spells/Fire Snake|fire snake]]_ (DC 18)
4th (5/day)—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Elemental Body I|elemental body I]]_, _[[spells/Fire Shield|fire shield]]_
3rd (6/day)—_[[spells/Fireball|fireball]]_ (DC 16), _[[spells/Howling Agony|howling agony]]_ (DC 16), _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Rage|rage]]_, _[[spells/Stinking Cloud|stinking cloud]]_ (DC 16)
2nd (7/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Levitate|levitate]]_, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/See Invisibility|see invisibility]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_
1st (7/day)—_[[spells/Burning Hands|burning hands]]_ (DC 14), _[[spells/Color Spray|color spray]]_ (DC 14), _[[spells/Enlarge Person|enlarge person]]_ (DC 14), _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 14), _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Daze|daze]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 13)
**Bloodline** elemental (fire)

### Tactics

**Before Combat** The bloodmage casts _invisibility_ and positions herself where she can hurl spells with impunity.
 **During Combat** At the start of the battle, the bloodmage casts _fire snake_ and _fireball_ on her foes. She reserves spells such as _fire shield_ and _shield_ to protect herself when she becomes the target of attacks.

##### Statistics
**Str** 18, **Dex** 15, **Con** 16, **Int** 8, **Wis** 10, **Cha** 17
**Base Atk** +7; **CMB** +11; **CMD** 24
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Enlarge Spell|Enlarge Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_
**Skills** Intimidate +6, Spellcraft +12, Stealth +9
**Languages** Common, _[[monsters/Goblin|Goblin]]_
**SQ** bloodline arcana (change energy damage spells to fire), stalker
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_; **Other Gear** +1 _quarterstaff_, mwk _[[items/Weapon/Dagger|dagger]]_, mwk _shortbow_ with 20 arrows, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, 117 gp

##### Ecology

**Environment** temperate mountains

##### Description

Arcane spellcasters among bugbears are typically sorcerers—few bugbears have enough interest or patience to follow arcane paths such as wizardry that require study or control. Bugbears call those with natural magical talent bloodmages, and treat their spellcasting ability the same as any skill—if it’s useful for hurting, it’s worth knowing. A typical bloodmage is interested in only spells that cause _[[spells/Destruction|destruction]]_ and pain, plus a few supplemental spells to help her defend herself. Almost no bloodmages learn to create magic items.