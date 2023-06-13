---
cssclass: [monsters]
title1: Erlking
desc_short: Birdlike wings covered with autumnal leaves instead of feathers extend
  from the back of this regal, elf-like humanoid.
title2: Erlking
CR: 18
sources:
- name: Bestiary 4
  page: 94
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 153600
alignment: CN
size: Medium
type: fey
initiative:
  bonus: 7
senses:
  low-light vision: true
AC:
  AC: 34
  touch: 15
  flat_footed: 29
  components:
    armor: 7
    dex: 4
    dodge: 1
    natural: 12
    deflection vs. evil or law: 2
HP:
  HP: 270
  long: 20d6+200
  fast_healing: 10
saves:
  fort: 15
  ref: 20
  will: 17
defensive_abilities:
- blur
- protection from good and law
DR:
- amount: 10
  weakness: cold iron
immunities:
- poison
resistances:
  acid: 30
  cold: 30
  electricity: 30
speeds:
  base: 70
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: +3 cold iron keen longsword +20/+20/+15 (1d8+12/17-20 plus bleed)
      entries:
      - - damage: 1d8+12
          crit_range: 17-20
        - effect: bleed
      attack: +3 cold iron keen longsword
      bonus:
      - 20
      - 20
      - 15
  ranged:
  - - text: +3 ironwood longbow +20/+20/+15 (1d8+3/×3 plus bleed)
      entries:
      - - damage: 1d8+3
          crit_multiplier: 3
        - effect: bleed
      attack: +3 ironwood longbow
      bonus:
      - 20
      - 20
      - 15
  special:
  - bleed (1d6)
  - favored enemy (all humanoids +10)
  - ironwood mastery
spell_like_abilities:
  entries:
  - name: blur
    source: default
    freq: Constant
  - name: haste
    source: default
    freq: Constant
    other: self only
  - name: protection from evil
    source: default
    freq: Constant
  - name: protection from law
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
  - name: speak with plants
    source: default
    freq: Constant
  - name: whispering wind
    source: default
    freq: At will
  - name: animate plants
    source: default
    freq: 3/day
  - name: black tentacles
    source: default
    freq: 3/day
  - name: cure critical wounds
    source: default
    freq: 3/day
  - name: haste
    source: default
    freq: 3/day
  - name: ironwood
    source: default
    freq: 3/day
  - name: move earth
    source: default
    freq: 3/day
  - name: plant growth
    source: default
    freq: 3/day
  - name: summon nature's ally VI
    source: default
    freq: 3/day
  - name: summon
    source: default
    freq: 3/day
    level: 6
    summons:
    - name: 1d4+1 centaurs
    - name: treant
      amount: 1
      chance: 100%
  - name: tree stride
    source: default
    freq: 3/day
  - name: finger of death
    source: default
    freq: 1/day
    DC: 23
  - name: repel metal or stone
    source: default
    freq: 1/day
  - name: summon nature's ally IX
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 25
ability_scores:
  STR: 20
  DEX: 25
  CON: 28
  INT: 19
  WIS: 20
  CHA: 21
BAB: 10
CMB: 15
CMD: 33
feats:
- name: Critical Focus
- name: Disruptive
- name: Greater Weapon Focus (longsword)
- name: Greater Weapon Specialization (longsword)
- name: Power Attack
- name: Spellbreaker
- name: Toughness
- name: Vital Strike
- name: Weapon Focus (longsword)
- name: Weapon Specialization (longsword)
skills:
  Acrobatics: 19
    when jumping: 35
  Bluff: 18
  Climb: 12
  Diplomacy: 13
  Fly: 18
  Handle Animal: 15
  Heal: 10
  Intimidate: 25
  Knowledge (geography): 17
  Knowledge (nature): 27
  Knowledge (nobility): 9
  Perception: 28
  Perform (any one): 13
  Ride: 16
  Sense Motive: 18
  Spellcraft: 14
  Stealth: 29
  Survival: 15
  Swim: 17
  _racial_mods:
    Acrobatics:
      when jumping: 16
languages:
- Common
- Elven
- Sylvan
- speak with animals
- speak with plants
special_qualities:
- warrior fey
ecology:
  environment: temperate forests
  organization: solitary, squad (1 plus 2-12 centaurs, 2-12 satyrs, and 1-2 treants),
    or army (1 plus 4-24 centaurs, 4-24 satyrs, and 2-5 treants)
  treasure_type: double
  treasure:
  - ironwood chain shirt
  - ironwood longbow
  - ironwood longsword
  - other treasure
special_abilities:
  Ironwood Mastery (Su): Any ironwood armor an erlking wears gains a +3 enhancement
    bonus, and any ironwood weapon it wields is treated as a +3 cold iron keen weapon.
  Warrior Fey (Ex): An erlking counts as a 20th-level fighter for all abilities and
    effects requiring fighter levels.
desc_long: |-
  Erlkings guard the wildest, most pristine reaches of nature, and lead other fey to reclaim defiled lands. Most forest creatures acknowledge an erlking as king of the forest and arbiter in disputes between the people of the wilds. In most forests, an erlking is the brother or consort of a hamadryad, and represents the aggressive, dangerous, and vengeful aspect of the wilds.

  An erlking is a blur of motion on or off the battlefield, using his powers to coordinate attacks against despoilers, manipulate terrain to his side's advantage, and call in reinforcements when his forces would be overwhelmed. When his services are not needed, an erlking retires to the realm of the fey.

---

# Erlking
Birdlike wings covered with autumnal leaves instead of feathers extend from the back of this regal, elf-like humanoid.
**Source** Bestiary 4 pg. 94
**XP** 153,600

CN Medium fey
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +28

##### Defense

**AC** 34, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+7 armor, +4 Dex, +1 _[[feats/Dodge|dodge]]_, +12 natural; +2 _[[spells/Deflection|deflection]]_ vs. evil or law)
**hp** 270 (20d6+200); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +15, **Ref** +20, **Will** +17
**Defensive Abilities** _[[spells/Blur|blur]]_, _[[spells/Protection From Good|protection from good]]_ and law; **DR** 10/cold iron; **Immune** poison; **Resist** acid 30, cold 30, electricity 30

##### Offense
**Speed** 70 ft., fly 90 ft. (good)
**Melee** +3 cold iron _[[items/Weapon Magic Abilities/Keen|keen]]_ _[[items/Weapon/Longsword|longsword]]_ +20/+20/+15 (1d8+12/17–20 plus _[[universal monster rules/Bleed|bleed]]_)
**Ranged** +3 _[[spells/Ironwood|ironwood]]_ _[[items/Weapon/Longbow|longbow]]_ +20/+20/+15 (1d8+3/×3 plus _bleed_)
**Special Attacks** _bleed_ (1d6), favored enemy (all humanoids +10), _ironwood_ mastery
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +25)
Constant—_blur_, _[[spells/Haste|haste]]_ (self only), _[[spells/Protection From Evil|protection from evil]]_, _[[spells/Protection From Law|protection from law]]_, _[[spells/Speak with Animals|speak with animals]]_, _[[spells/Speak with Plants|speak with plants]]_
At will—_[[spells/Whispering Wind|whispering wind]]_
3/day—_[[spells/Animate Plants|animate plants]]_, _[[spells/Black Tentacles|black tentacles]]_, _[[spells/Cure Critical Wounds|cure critical wounds]]_, _haste_, _ironwood_, _[[spells/Move Earth|move earth]]_, _[[spells/Plant Growth|plant growth]]_, _[[universal monster rules/Summon|summon]]_ nature’s ally VI, _summon_ (level 6, 1d4+1 centaurs or 1 _[[monsters/Treant|treant]]_ 100%), _[[spells/Tree Stride|tree stride]]_
1/day—_[[spells/Finger Of Death|finger of death]]_ (DC 23), _[[spells/Repel Metal or Stone|repel metal or stone]]_, _summon_ nature’s ally IX

##### Statistics
**Str** 20, **Dex** 25, **Con** 28, **Int** 19, **Wis** 20, **Cha** 21
**Base Atk** +10; **CMB** +15; **CMD** 33
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Disruptive|Disruptive]]_, _[[feats/Greater Weapon Focus|Greater Weapon Focus]]_ (_longsword_), _[[feats/Greater Weapon Specialization|Greater Weapon Specialization]]_ (_longsword_), _[[feats/Power Attack|Power Attack]]_, _[[items/Weapon/Spellbreaker|Spellbreaker]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_longsword_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_longsword_)
**Skills** Acrobatics +19 (+35 when jumping), Bluff +18, _[[universal monster rules/Climb|Climb]]_ +12, Diplomacy +13, Fly +18, Handle Animal +15, _[[spells/Heal|Heal]]_ +10, Intimidate +25, Knowledge (geography) +17, Knowledge (nature) +27, Knowledge (nobility) +9, Perception +28, Perform (any one) +13, Ride +16, Sense Motive +18, Spellcraft +14, Stealth +29, Survival +15, Swim +17; **Racial Modifiers** +16 Acrobatics when jumping
**Languages** Common, Elven, Sylvan; _speak with animals_, _speak with plants_
**SQ** warrior fey

##### Ecology

**Environment** temperate forests
**Organization** solitary, squad (1 plus 2–12 centaurs, 2–12 satyrs, and 1–2 treants), or army (1 plus 4–24 centaurs, 4–24 satyrs, and 2–5 treants)
**Treasure** double (_ironwood_ _[[items/Armor/Chain shirt|chain shirt]]_, _ironwood_ _longbow_, _ironwood_ _longsword_, other treasure)

### Special Abilities

**_Ironwood_ Mastery (Su)** Any _ironwood_ armor an _[[monsters/Erlking|erlking]]_ wears gains a +3 enhancement bonus, and any _ironwood_ weapon it wields is treated as a +3 cold iron _keen_ weapon.

**Warrior Fey (Ex)** An _erlking_ counts as a 20th-level _[[classes/Fighter|fighter]]_ for all abilities and effects requiring _fighter_ levels.

##### Description

Erlkings _[[npcs/Guard|guard]]_ the wildest, most pristine reaches of nature, and lead other fey to reclaim defiled lands. Most forest creatures acknowledge an _erlking_ as _[[npcs/King|king]]_ of the forest and arbiter in disputes between the people of the wilds. In most forests, an _erlking_ is the brother or consort of a _[[monsters/Hamadryad|hamadryad]]_, and represents the aggressive, dangerous, and vengeful aspect of the wilds.

An _erlking_ is a _blur_ of motion on or off the battlefield, using his powers to coordinate attacks against despoilers, manipulate terrain to his side’s advantage, and call in reinforcements when his forces would be overwhelmed. When his services are not needed, an _erlking_ retires to the realm of the fey.