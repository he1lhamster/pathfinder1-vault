---
cssclass: [monsters]
title1: Graveknight
desc_short: Shadows veil what lurks within the dark, imposing armor of this figure,
  though two piercing eyes gaze from its closed visor.
title2: Graveknight
CR: 11
sources:
- name: Bestiary 3
  page: 138
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 12800
race: Human
classes:
- graveknight fighter 10
alignment: LE
size: Medium
type: undead
subtypes:
- augmented humanoid
initiative:
  bonus: 5
senses:
  darkvision: 60
auras:
- name: sacrilegious aura
  radius: 30
  DC: 19
AC:
  AC: 25
  touch: 11
  flat_footed: 24
  components:
    armor: 10
    dex: 1
    natural: 4
HP:
  HP: 139
  long: 10d10+80
saves:
  fort: 13
  ref: 6
  will: 6
  other: +3 vs. fear
defensive_abilities:
- bravery +3
- channel resistance +4
- rejuvenation
DR:
- amount: 10
  weakness: magic
immunities:
- acid
- cold
- electricity
- undead traits
SR: 22
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 greatsword +25/+20 (2d6+19 plus 2d6 acid)
      entries:
      - - damage: 2d6+19
        - damage: 2d6
          type: acid
      attack: +1 greatsword
      bonus:
      - 25
      - 20
  ranged:
  - - text: composite longbow +14/+9 (1d8+11/×3)
      entries:
      - - damage: 1d8+11
          crit_multiplier: 3
      attack: composite longbow
      bonus:
      - 14
      - 9
  special:
  - channel destruction
  - devastating blast (6d6 acid, DC 19)
  - undead mastery (DC 19)
  - weapon training (heavy blades +2, bows +1)
ability_scores:
  STR: 27
  DEX: 12
  CON: 10
  INT: 15
  WIS: 12
  CHA: 18
BAB: 10
CMB: 20
CMD: 29
feats:
- name: Cleave
- name: Critical Focus
- name: Dazzling Display
- name: Greater Weapon Focus (greatsword)
- is_bonus: true
  name: Improved Initiative
- is_bonus: true
  name: Mounted Combat
- name: Power Attack
- is_bonus: true
  name: Ride-By Attack
- name: Shatter Defenses
- name: Spirited Charge
- is_bonus: true
  name: Toughness
- name: Trample
- name: Unseat
- name: Vital Strike
- name: Weapon Focus (greatsword)
- name: Weapon Specialization (greatsword)
skills:
  Climb: 13
  Intimidate: 25
  Knowledge (nobility): 12
  Perception: 19
  Ride: 19
  Swim: 13
  _racial_mods:
    Intimidate:
      _: 8
    Perception:
      _: 8
    Ride:
      _: 8
languages:
- Common
- Dwarven
- Infernal
special_qualities:
- armor training 2
- phantom mount
- ruinous revivification
ecology:
  environment: any land
  organization: solitary or troop (graveknight plus 12-24 skeletal champions)
  treasure_type: NPC Gear
  treasure:
  - +1 full plate
  - +1 greatsword
  - composite longbow [+8 Str] with 20 arrows
  - belt of giant strength +2
  - other treasure
desc_long: Undying tyrants and eternal champions of the undead, graveknights arise
  from the corpses of the most nefarious warlords and disgraced heroes-villains too
  merciless to submit to the shackles of death. They bear the same weapons and regalia
  they did in life, though warped or empowered by their profane resurrection. The
  legions they once held also flock to them in death, ready to serve their wicked
  ambitions once more. A graveknight's essence is fundamentally tied to its armor,
  the bloodstained trappings of its battle lust. This armor becomes an icon of its
  perverse natures, transforming into a monstrous second skin over the husk of desiccated
  flesh and scarred bone locked within.

---

# Graveknight
Shadows _[[spells/Veil|veil]]_ what lurks within the dark, imposing armor of this figure, though two piercing eyes _[[universal monster rules/Gaze|gaze]]_ from its closed visor.
**Source** Bestiary 3 pg. 138
**XP** 12,800
Human _[[monsters/Graveknight|graveknight]]_ _[[classes/Fighter|fighter]]_ 10

LE Medium undead (augmented humanoid)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +19
**Aura** sacrilegious aura (30 ft., DC 19)

##### Defense

**AC** 25, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+10 armor, +1 Dex, +4 natural)
**hp** 139 (10d10+80)
**Fort** +13, **Ref** +6, **Will** +6; +3 vs. _[[universal monster rules/Fear|fear]]_
**Defensive Abilities** bravery +3, _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, rejuvenation; **DR** 10/magic; **Immune** acid, cold, electricity, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 22

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Greatsword|greatsword]]_ +25/+20 (2d6+19 plus 2d6 acid)
**Ranged** _[[items/Weapon/Composite longbow|composite longbow]]_ +14/+9 (1d8+11/×3)
**Special Attacks** channel _[[spells/Destruction|destruction]]_, devastating blast (6d6 acid, DC 19), undead mastery (DC 19), weapon _[[items/Weapon Magic Abilities/Training|training]]_ (heavy blades +2, bows +1)

##### Statistics
**Str** 27, **Dex** 12, **Con** 10, **Int** 15, **Wis** 12, **Cha** 18
**Base Atk** +10; **CMB** +20; **CMD** 29
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Dazzling Display|Dazzling Display]]_, _[[feats/Greater Weapon Focus|Greater Weapon Focus]]_ (_greatsword_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mounted Combat|Mounted Combat]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Ride-By Attack|Ride-By Attack]]_, _[[feats/Shatter Defenses|Shatter Defenses]]_, _[[feats/Spirited Charge|Spirited Charge]]_, _[[feats/Toughness|Toughness]]_, _[[universal monster rules/Trample|Trample]]_, _[[feats/Unseat|Unseat]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_greatsword_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_greatsword_)
**Skills** _[[universal monster rules/Climb|Climb]]_ +13, Intimidate +25, Knowledge (nobility) +12, Perception +19, Ride +19, Swim +13; **Racial Modifiers** +8 Intimidate, +8 Perception, +8 Ride
**Languages** Common, Dwarven, Infernal
**SQ** armor _training_ 2, phantom _[[spells/Mount|mount]]_, ruinous revivification

##### Ecology

**Environment** any land
**Organization** solitary or troop (_graveknight_ plus 12–24 skeletal champions)
**Treasure** NPC gear (+1 _[[items/Armor/Full plate|full plate]]_, +1 _greatsword_, _composite longbow_ [+8 Str] with 20 arrows, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, other treasure)

##### Description

Undying tyrants and eternal champions of the undead, graveknights arise from the corpses of the most nefarious warlords and disgraced heroes—villains too merciless to submit to the shackles of death. They bear the same weapons and regalia they did in life, though warped or empowered by their profane _[[spells/Resurrection|resurrection]]_. The legions they once held also flock to them in death, ready to serve their wicked ambitions once more. A _graveknight_’s essence is fundamentally tied to its armor, the bloodstained trappings of its battle lust. This armor becomes an icon of its perverse natures, transforming into a monstrous second skin over the husk of desiccated flesh and scarred bone locked within.