---
cssclass: [monsters]
title1: Rabisu
desc_short: This hollow-eyed, blue-skinned woman has a vulture's wings, birdlike talons
  for hands and feet, and a fang-filled mouth.
title2: Rabisu
CR: 11
sources:
- name: Qadira, Jewel of the East
  page: 62
  link: http://paizo.com/products/btpy9nd2?Pathfinder-Campaign-Setting-Qadira-Jewel-of-the-East
XP: 12800
alignment: CE
size: Medium
type: fey
initiative:
  bonus: 7
senses:
  low-light vision: true
  scent: true
  see in darkness: true
AC:
  AC: 25
  touch: 18
  flat_footed: 17
  components:
    dex: 8
    dodge: 1
    natural: 7
HP:
  HP: 147
  long: 14d6+98
saves:
  fort: 11
  ref: 16
  will: 14
DR:
- amount: 10
  weakness: cold iron and magic
immunities:
- fire
- bleed
- fear
resistances:
  cold: 10
  electricity: 10
weaknesses:
- suceptible to salt
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +17 (1d6+8 plus blood drain)
      entries:
      - - damage: 1d6+8
        - effect: blood drain
      attack: bite
      bonus:
      - 17
    - text: 4 claws +18 (1d4+8 plus grab)
      entries:
      - - damage: 1d4+8
        - effect: grab
      count: 4
      attack: claws
      bonus:
      - 18
  special:
  - blood drain (1d2 Constitution)
spell_like_abilities:
  entries:
  - name: greater magic fang
    source: default
    freq: Constant
    other: self only
  - name: command undead
    source: default
    freq: At will
    DC: 18
  - name: invisibility
    source: default
    freq: At will
  - name: ray of enfeeblement
    source: default
    freq: At will
    DC: 19
  - name: charm monster
    source: default
    freq: 3/day
    DC: 20
  - name: quickened invisibility
    source: default
    freq: 3/day
  - name: quickened ray of enfeeblement
    source: default
    freq: 3/day
    DC: 19
  - name: ray of exhaustion
    source: default
    freq: 3/day
  - name: vampiric touch
    source: default
    freq: 3/day
  - name: mirage arcana
    source: default
    freq: 1/day
    DC: 21
  - name: veil
    source: default
    freq: 1/day
    other: self only
  - name: waves of fatigue
    source: default
    freq: 1/day
  - name: wind walk
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 12
    concentration: 18
ability_scores:
  STR: 21
  DEX: 24
  CON: 24
  INT: 19
  WIS: 21
  CHA: 22
BAB: 7
CMB: 12
CMB_other: +16 grapple
CMD: 30
CMD_other: 34 vs. grapple
feats:
- name: Ability Focus (ray of enfeeblement)
- name: Combat Casting
- name: Dodge
- name: Quicken Spell-Like Ability (invisibility)
- name: Quicken Spell-Like Ability (ray of enfeeblement)
- name: Skill Focus (Stealth)
- name: Weapon Finesse
- name: Weapon Focus (claw)
skills:
  Acrobatics: 24
  Disguise: 23
  Escape Artist: 24
  Fly: 28
  Intimidate: 20
  Knowledge (nature): 21
  Perception: 22
  Sense Motive: 22
  Stealth: 38
  Survival: 19
  _racial_mods:
    Stealth:
      _: 8
languages:
- Aklo
- Auran
- Common
special_qualities:
- blood frenzy
ecology:
  environment: warm deserts, hills, and mountains
  organization: solitary, pair, or gang (3-6)
  treasure_type: standard
special_abilities:
  Blood Frenzy (Ex): When a rabisu successfully drains blood from a creature, it becomes
    frenzied. For 1d4 rounds after it drains blood, it acts as if affected by haste
    and gains fast healing 5.
  Susceptible to Salt (Ex): A handful of salt burns a rabisu as a flask of acid would,
    causing 1d6 points of damage per use. Ground sprinkled with salt functions as
    difficult terrain for a rabisu. A line of salt placed across a doorway, window,
    or other aperture can largely prevent a rabisu from passing through that opening.
    It can attempt to go through the opening as a move action, but unless it succeeds
    at a DC 20 Fortitude save, the salt prevents it from completing the movement,
    and it becomes nauseated for 1 round.
desc_long: |-
  Despite their ghoulish appearance, rabisus are living creatures, not undead. While they can manipulate objects with their talons, they cannot wield weapons. Rabisus take great delight in the taste of blood. To these fey, this flavor can vary greatly, even between two similar creatures. Rabisus might keep particularly delicious victims prisoner for months to prolong the pleasure of savoring their blood.

   A rabisu stands 6 feet tall and weighs 160 pounds.

---

# Rabisu
This hollow-eyed, blue-skinned woman has a _[[monsters/Vulture|vulture]]_’s wings, birdlike talons for hands and feet, and a fang-filled mouth.
**Source** Qadira, Jewel of the East pg. 62
**XP** 12,800
CE Medium fey
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +22

##### Defense

**AC** 25, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+8 Dex, +1 _[[feats/Dodge|Dodge]]_, +7 natural)
**hp** 147 (14d6+98)
**Fort** +11, **Ref** +16, **Will** +14
**DR** 10/cold iron and magic; **Immune** fire, _[[universal monster rules/Bleed|bleed]]_, _[[universal monster rules/Fear|fear]]_; **Resist** cold 10, electricity 10
**Weaknesses** suceptible to salt

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** bite +17 (1d6+8 plus _[[universal monster rules/Blood Drain|blood drain]]_), 4 claws +18 (1d4+8 plus _[[universal monster rules/Grab|grab]]_)
**Special Attacks** _blood drain_ (1d2 Constitution)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +18)
Constant—greater _[[spells/Magic Fang|magic fang]]_ (self only)
 At will—_[[spells/Command Undead|command undead]]_ (DC 18), _[[spells/Invisibility|invisibility]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 19)
 3/day—_[[spells/Charm Monster|charm monster]]_ (DC 20), quickened _invisibility_, quickened _ray of enfeeblement_ (DC 19), _[[spells/Ray of Exhaustion|ray of exhaustion]]_, _[[spells/Vampiric Touch|vampiric touch]]_
 1/day—_[[spells/Mirage Arcana|mirage arcana]]_ (DC 21), _[[spells/Veil|veil]]_ (self only), _[[spells/Waves of Fatigue|waves of fatigue]]_, _[[spells/Wind Walk|wind walk]]_

##### Statistics
**Str** 21, **Dex** 24, **Con** 24, **Int** 19, **Wis** 21, **Cha** 22
**Base Atk** +7; **CMB** +12 (+16 grapple); **CMD** 30 (34 vs. grapple)
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_ray of enfeeblement_), _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_invisibility_, _ray of enfeeblement_), _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Acrobatics +24, Disguise +23, Escape Artist +24, Fly +28, Intimidate +20, Knowledge (nature) +21, Perception +22, Sense Motive +22, Stealth +38, Survival +19; **Racial Modifiers** +8 Stealth
**Languages** Aklo, Auran, Common
**SQ** blood frenzy

##### Ecology

**Environment** warm deserts, hills, and mountains
**Organization** solitary, pair, or gang (3-6)
**Treasure** standard

### Special Abilities

**Blood Frenzy (Ex)** When a _[[monsters/Rabisu|rabisu]]_ successfully drains blood from a creature, it becomes frenzied. For 1d4 rounds after it drains blood, it acts as if affected by _[[spells/Haste|haste]]_ and gains _[[universal monster rules/Fast Healing|fast healing]]_ 5.
**Susceptible to Salt (Ex)** A handful of salt burns a _rabisu_ as a _[[items/Mundane/Flask|flask]]_ of acid would, causing 1d6 points of damage per use. Ground sprinkled with salt functions as difficult terrain for a _rabisu_. A line of salt placed across a doorway, window, or other aperture can largely prevent a _rabisu_ from passing through that opening. It can attempt to go through the opening as a move action, but unless it succeeds at a DC 20 Fortitude save, the salt prevents it from completing the movement, and it becomes _[[conditions/Nauseated|nauseated]]_ for 1 round.

##### Description

Despite their ghoulish appearance, rabisus are living creatures, not undead. While they can manipulate objects with their talons, they cannot wield weapons. Rabisus take great delight in the taste of blood. To these fey, this flavor can vary greatly, even between two similar creatures. Rabisus might keep particularly delicious victims prisoner for months to prolong the pleasure of savoring their blood.

A _rabisu_ stands 6 feet tall and weighs 160 pounds.