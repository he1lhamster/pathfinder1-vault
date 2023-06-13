---
cssclass: [monsters]
title1: Demon, Glabrezu
desc_short: Four arms grace the torso of this towering monstrosity. The monster's
  eyes shine with a mix of intelligence and cruelty.
title2: Glabrezu
CR: 13
sources:
- name: Pathfinder RPG Bestiary
  page: 61
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 25600
alignment: CE
size: Huge
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 0
senses:
  darkvision: 60
  true seeing: true
AC:
  AC: 28
  touch: 8
  flat_footed: 28
  components:
    natural: 20
    size: -2
HP:
  HP: 186
  long: 12d10+120
saves:
  fort: 18
  ref: 4
  will: 11
DR:
- amount: 10
  weakness: good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 24
speeds:
  base: 40
attacks:
  melee:
  - - text: 2 pincers +20 (2d8+10/19-20)
      entries:
      - - damage: 2d8+10
          crit_range: 19-20
      count: 2
      attack: pincers
      bonus:
      - 20
    - text: 2 claws +20 (1d6+10)
      entries:
      - - damage: 1d6+10
      count: 2
      attack: claws
      bonus:
      - 20
    - text: bite +20 (1d8+10)
      entries:
      - - damage: 1d8+10
      attack: bite
      bonus:
      - 20
  special:
  - rend (2 pincers, 2d8+15)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: chaos hammer
    source: default
    freq: At will
    DC: 19
  - name: confusion
    source: default
    freq: At will
    DC: 19
  - name: dispel magic
    source: default
    freq: At will
  - name: mirror image
    source: default
    freq: At will
  - name: reverse gravity
    source: default
    freq: At will
    DC: 22
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: veil
    source: default
    freq: At will
    other: self only
  - name: unholy blight
    source: default
    freq: At will
  - name: power word stun
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: glabrezu
      amount: 1
      chance: 20%
    - name: vrocks
      amount: 1d2
      chance: 50%
  - name: wish
    source: default
    freq: 1/month
    other: granted to a mortal humanoid only
  sources:
  - name: default
    CL: 14
ability_scores:
  STR: 31
  DEX: 11
  CON: 31
  INT: 16
  WIS: 16
  CHA: 20
BAB: 12
CMB: 24
CMD: 34
feats:
- name: Cleave
- name: Great Cleave
- name: Improved Critical (pincer)
- name: Persuasive
- name: Power Attack
- name: Vital Strike
skills:
  Bluff: 28
  Diplomacy: 22
  Intimidate: 22
  Knowledge (history): 18
  Knowledge (local): 18
  Perception: 26
  Sense Motive: 18
  Stealth: 7
  Use Magic Device: 17
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
ecology:
  environment: any (Abyss)
  organization: solitary or troop (1 glabrezu, 1 succubus, and 2-5 vrocks)
  treasure_type: standard
desc_long: |-
  Whereas the succubus is a demon that works her wiles by exploiting the physical lusts and needs of her prey, the glabrezu is a tempter of a different sort. Ferocious and bestial in form, the glabrezu is in fact a master of trickery and lies. With its ability to cloak its true form in pleasant illusions, the glabrezu uses its magic to grant wishes to mortal humanoids as a method of rewarding those who succumb to its guile and deceit. A wish granted by a glabrezu always fulfills the wisher's need in the most destructive way possible-although such methods might not be immediately apparent. A struggling weaponsmith might wish for fame and skill at his craft, only to find that his best patron is a cruel and sadistic murderer who uses the weapons to further his destructive desires. A lonely man who wishes for a companion might have his wish granted in the form of a lost love returned to “life” as a vampire, and so on-the glabrezu is nothing if not creative in addressing a mortal's desires.

  A glabrezu stands 18 feet tall and weighs just over 6,000 pounds. These treacherous demons form from the souls of the treasonous, the false, and the subversive-souls of mortals who, in life, bore false witness or used treachery and deceit to ruin the lives of others.

---

# Demon, Glabrezu
Four arms _[[spells/Grace|grace]]_ the torso of this towering monstrosity. The monster’s eyes shine with a mix of intelligence and _[[feats/Cruelty|cruelty]]_.
**Source** Pathfinder RPG Bestiary pg. 61
**XP** 25,600
CE Huge outsider (chaotic, demon, evil, extraplanar)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +26

##### Defense

**AC** 28, touch 8, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+20 natural, –2 size)
**hp** 186 (12d10+120)
**Fort** +18, **Ref** +4, **Will** +11
**DR** 10/good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 24

##### Offense
**Speed** 40 ft.
**Melee** 2 pincers +20 (2d8+10/19–20), 2 claws +20 (1d6+10), bite +20 (1d8+10)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Rend|rend]]_ (2 pincers, 2d8+15)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th)
Constant—_true seeing_
At will—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 19), _[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Reverse Gravity|reverse gravity]]_ (DC 22), greater teleport (self plus 50 lbs. of objects only), _[[spells/Veil|veil]]_ (self only), _[[spells/Unholy Blight|unholy blight]]_
1/day—_[[spells/Power Word Stun|power word stun]]_, _[[universal monster rules/Summon|summon]]_ (level 4, 1 glabrezu 20% or 1d2 vrocks 50%)
1/month—_[[spells/Wish|wish]]_ (granted to a mortal humanoid only)

##### Statistics
**Str** 31, **Dex** 11, **Con** 31, **Int** 16, **Wis** 16, **Cha** 20
**Base Atk** +12; **CMB** +24; **CMD** 34
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (pincer), _[[feats/Persuasive|Persuasive]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +28, Diplomacy +22, Intimidate +22, Knowledge (history) +18, Knowledge (local) +18, Perception +26, Sense Motive +18, Stealth +7, Use Magic Device +17; **Racial Modifiers** +8 Bluff, +8 Perception
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary or troop (1 glabrezu, 1 succubus, and 2–5 vrocks)
**Treasure** standard

##### Description

Whereas the succubus is a demon that works her wiles by exploiting the physical lusts and needs of her prey, the glabrezu is a tempter of a different sort. Ferocious and bestial in form, the glabrezu is in fact a master of trickery and lies. With its ability to cloak its _[[spells/True Form|true form]]_ in pleasant illusions, the glabrezu uses its magic to grant wishes to mortal humanoids as a method of rewarding those who succumb to its guile and deceit. A _wish_ granted by a glabrezu always fulfills the wisher’s need in the most destructive way possible—although such methods might not be immediately apparent. A struggling weaponsmith might _wish_ for fame and skill at his craft, only to find that his best patron is a _[[items/Weapon Magic Abilities/Cruel|cruel]]_ and sadistic murderer who uses the weapons to further his destructive desires. A lonely man who wishes for a companion might have his _wish_ granted in the form of a lost love returned to “life” as a _[[monsters/Vampire|vampire]]_, and so on—the glabrezu is nothing if not creative in addressing a mortal’s desires.

A glabrezu stands 18 feet tall and weighs just over 6,000 pounds. These treacherous demons form from the souls of the _[[items/Weapon Magic Abilities/Treasonous|treasonous]]_, the false, and the subversive—souls of mortals who, in life, bore false _[[spells/Witness|witness]]_ or used treachery and deceit to ruin the lives of others.