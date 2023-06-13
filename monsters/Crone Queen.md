---
cssclass: [monsters]
title1: Crone Queen
desc_short: A cold, hateful light burns in the eye sockets of this corpse-like creature,
  whose withered skin is stretched over its icy bones.
title2: Crone Queen
CR: 15
sources:
- name: Bestiary 5
  page: 61
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: "Pathfinder #72: The Witch Queen's Revenge"
  page: 84
  link: http://paizo.com/products/btpy8yv7?Pathfinder-Adventure-Path-72-The-Witch-Queen-s-Revenge
XP: 51200
alignment: NE
size: Medium
type: undead
subtypes:
- cold
initiative:
  bonus: 9
senses:
  darkvision: 60
  lifesense: true
auras:
- name: fear aura
  radius: 30
  DC: 25
AC:
  AC: 30
  touch: 16
  flat_footed: 24
  components:
    armor: 4
    dex: 5
    dodge: 1
    natural: 10
HP:
  HP: 209
  long: 22d8+110
  fast_healing: 10
saves:
  fort: 13
  ref: 14
  will: 18
defensive_abilities:
- channel resistance +4
DR:
- amount: 10
  weakness: cold iron and slashing
immunities:
- cold
- undead traits
SR: 26
weaknesses:
- vulnerable to fire
speeds:
  base: 30
attacks:
  melee:
  - - text: ice staff +27/+22/+17/+12 (1d6+14 plus 1d6 cold and energy drain)
      entries:
      - - damage: 1d6+14
        - damage: 1d6
          type: cold
        - effect: energy drain
      attack: ice staff
      bonus:
      - 27
      - 22
      - 17
      - 12
  - - text: 2 claws +22 (1d6+6 plus 1d6 cold and energy drain)
      entries:
      - - damage: 1d6+6
        - damage: 1d6
          type: cold
        - effect: energy drain
      count: 2
      attack: claws
      bonus:
      - 22
  special:
  - cold
  - energy drain (2 levels, DC 25)
  - hexes (blight, evil eye, hoarfrost, ice tomb, misfortune)
  - ice staff
  - unearthly cold
spell_like_abilities:
  entries:
  - name: mage armor
    source: default
    freq: Constant
  - name: frost fall
    source: default
    freq: At will
    DC: 16
  - name: ice missile
    source: default
    freq: At will
    paren_text: as magic missile, but deals cold damage
  - name: obscuring mist
    source: default
    freq: At will
  - name: screech
    source: default
    freq: At will
    DC: 17
  - name: bestow curse
    source: default
    freq: 3/day
    DC: 17
  - name: crushing despair
    source: default
    freq: 3/day
    DC: 18
  - name: ice storm
    source: default
    freq: 3/day
  - name: unshakable chill
    source: default
    freq: 3/day
    DC: 16
  - name: wall of ice
    source: default
    freq: 3/day
    DC: 18
  - name: cone of cold
    source: default
    freq: 1/day
    DC: 19
  - name: freezing sphere
    source: default
    freq: 1/day
    DC: 20
  - name: polar ray
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 19
    concentration: 23
ability_scores:
  STR: 23
  DEX: 20
  CON:
  INT: 19
  WIS: 17
  CHA: 18
BAB: 16
CMB: 22
CMD: 38
feats:
- name: Alertness
- name: Combat Casting
- name: Dodge
- name: Great Fortitude
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Lunge
- name: Mobility
- name: Power Attack
- name: Toughness
skills:
  Intimidate: 29
  Knowledge (arcana): 27
  Knowledge (history): 27
  Knowledge (nobility): 27
  Perception: 32
  Sense Motive: 32
  Spellcraft: 29
  Stealth: 30
languages:
- Aklo
- Common
- Draconic
- Giant
- Sylvan
ecology:
  environment: cold ruins
  organization: solitary, coven (3-6), or court (12-14)
  treasure_type: double
special_abilities:
  Cold (Ex): A crone queen's body generates intense cold, dealing 1d6 points of cold
    damage with its touch or when creatures attack it with unarmed strikes and natural
    attacks.
  Hexes (Su): A crone queen can use the hexes listed in its special attacks entry
    as a 20th-level witch . The save DC to resist a crone queen's hex is 24.
  Ice Staff (Su): As a free action, a crone queen can create a magic staff out of
    supernaturally hard ice that functions as a +5 frost quarterstaff. The crone queen
    can use her energy drain attack with this staff. The ice staff melts away instantly
    if it leaves the crone queen's hands.
  Unearthly Cold (Su): Half the cold damage caused by cold spells and spell-like abilities
    cast by the crone queen is not subject to cold resistance or immunity.
desc_long: Crone queens are unique and deadly creatures formed from the frozen remains
  of Baba Yaga's daughters.

---

# Crone Queen
A cold, hateful light burns in the eye sockets of this corpse-like creature, whose withered skin is stretched over its icy bones.
**Source** Bestiary 5 pg. 61, Pathfinder #72: The _[[classes/Witch|Witch]]_ Queen's Revenge pg. 84
**XP** 51,200

NE Medium undead (cold)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Lifesense|lifesense]]_; Perception +32
**Aura** _[[universal monster rules/Fear|fear]]_ aura (30 ft., DC 25)

##### Defense

**AC** 30, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+4 armor, +5 Dex, +1 _[[feats/Dodge|Dodge]]_, +10 natural)
**hp** 209 (22d8+110); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +13, **Ref** +14, **Will** +18
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 10/cold iron and slashing; **Immune** cold, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 26
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 30 ft.
**Melee** ice staff +27/+22/+17/+12 (1d6+14 plus 1d6 cold and _[[universal monster rules/Energy Drain|energy drain]]_) or 2 claws +22 (1d6+6 plus 1d6 cold and _energy drain_)
**Special Attacks** cold, _energy drain_ (2 levels, DC 25), hexes (_[[spells/Blight|blight]]_, evil eye, hoarfrost, ice tomb, misfortune), ice staff, unearthly cold
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +23)
Constant—_[[spells/Mage Armor|mage armor]]_
At will—_[[spells/Frost Fall|frost fall]]_(DC 16), ice missile (as _[[spells/Magic Missile|magic missile]]_, but deals cold damage), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Screech|screech]]_(DC 17)
3/day—_[[spells/Bestow Curse|bestow curse]]_ (DC 17), _[[spells/Crushing Despair|crushing despair]]_ (DC 18), _[[spells/Ice Storm|ice storm]]_, _[[spells/Unshakable Chill|unshakable chill]]_ (DC 16), _[[spells/Wall Of Ice|wall of ice]]_ (DC 18)
1/day—_[[spells/Cone of Cold|cone of cold]]_ (DC 19), _[[spells/Freezing Sphere|freezing sphere]]_ (DC 20), _[[spells/Polar Ray|polar ray]]_

##### Statistics
**Str** 23, **Dex** 20, **Con** —, **Int** 19, **Wis** 17, **Cha** 18
**Base Atk** +16; **CMB** +22; **CMD** 38
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Intimidate +29, Knowledge (arcana, history, nobility) +27, Perception +32, Sense Motive +32, Spellcraft +29, Stealth +30
**Languages** Aklo, Common, Draconic, Giant, Sylvan

##### Ecology

**Environment** cold ruins
**Organization** solitary, coven (3-6), or court (12-14)
**Treasure** double

### Special Abilities

**Cold (Ex)** A _[[monsters/Crone Queen|crone queen]]_’s body generates intense cold, dealing 1d6 points of cold damage with its touch or when creatures attack it with unarmed strikes and _[[universal monster rules/Natural Attacks|natural attacks]]_.

**Hexes (Su)** A _crone queen_ can use the hexes listed in its special attacks entry as a 20th-level _witch_ . The save DC to resist a _crone queen_’s hex is 24.

**Ice Staff (Su)** As a free action, a _crone queen_ can create a magic staff out of supernaturally hard ice that functions as a +5 frost _[[items/Weapon/Quarterstaff|quarterstaff]]_. The _crone queen_ can use her _energy drain_ attack with this staff. The ice staff melts away instantly if it leaves the _crone queen_’s hands.

**Unearthly Cold (Su)** Half the cold damage caused by cold spells and _spell-like abilities_ cast by the _crone queen_ is not subject to cold _[[universal monster rules/Resistance|resistance]]_ or _[[universal monster rules/Immunity|immunity]]_.

##### Description

Crone queens are unique and _[[items/Weapon Magic Abilities/Deadly|deadly]]_ creatures formed from the frozen remains of Baba Yaga’s daughters.