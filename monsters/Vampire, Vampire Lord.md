---
cssclass: [monsters]
title1: Vampire, Vampire Lord
title2: Vampire Lord
CR: 15
sources:
- name: Monster Codex
  page: 243
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 51200
race: Half-elf
classes:
- vampire magus 14 (Pathfinder RPG Ultimate Magic 9)
alignment: NE
size: Medium
type: undead
subtypes:
- augmented humanoid
- elf
- human
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 28
  touch: 14
  flat_footed: 25
  components:
    armor: 7
    deflection: 1
    dex: 2
    dodge: 1
    natural: 7
HP:
  HP: 150
  long: 14d8+84
  fast_healing: 5
saves:
  fort: 16
  ref: 10
  will: 13
  other: +2 vs. enchantments
defensive_abilities:
- channel resistance +4
DR:
- amount: 10
  weakness: magic and silver
immunities:
- sleep
- undead traits
resistances:
  cold: 10
  electricity: 10
weaknesses:
- vampire weaknesses
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 frost longsword +20/+15 (1d8+11/17-20 plus 2d6)
      entries:
      - - damage: 1d8+11
          crit_range: 17-20
        - damage: 2d6
      attack: +1 frost longsword
      bonus:
      - 20
      - 15
    - text: slam +13 (1d4+8 plus energy drain)
      entries:
      - - damage: 1d4+8
        - effect: energy drain
      attack: slam
      bonus:
      - 13
  special:
  - blood drain
  - children of the night
  - create spawn
  - dominate (DC 22)
  - energy drain (2 levels, DC 22)
  - greater spell combat
  - improved spell combat
  - spell combat (-2 attack, +2 concentration, double bonus)
  - spellstrike
spells:
  entries:
  - name: baleful polymorph
    source: Magus
    level: 5
    DC: 19
  - superscripts:
    - UM
    name: monstrous physique III
    source: Magus
    level: 5
  - name: fire shield
    source: Magus
    level: 4
  - name: greater invisibility
    source: Magus
    level: 4
  - name: ice storm
    source: Magus
    level: 4
  - name: shout
    source: Magus
    level: 4
    DC: 18
  - name: stoneskin
    source: Magus
    level: 4
  - superscripts:
    - APG
    name: cloak of winds
    source: Magus
    level: 3
  - name: dispel magic
    source: Magus
    level: 3
  - name: fireball
    source: Magus
    level: 3
    DC: 17
  - name: haste
    source: Magus
    level: 3
  - name: slow
    source: Magus
    level: 3
    DC: 17
  - name: darkness
    source: Magus
    level: 2
  - superscripts:
    - UM
    name: frigid touch
    source: Magus
    level: 2
  - name: mirror image
    source: Magus
    level: 2
  - name: scorching ray
    source: Magus
    level: 2
    count: 2
  - name: web
    source: Magus
    level: 2
    DC: 16
  - name: expeditious retreat
    source: Magus
    level: 1
  - superscripts:
    - UM
    name: frostbite
    source: Magus
    level: 1
  - name: shield
    source: Magus
    level: 1
  - name: shocking grasp
    source: Magus
    level: 1
    count: 2
  - name: true strike
    source: Magus
    level: 1
  - name: arcane mark
    source: Magus
    level: 0
  - name: dancing lights
    source: Magus
    level: 0
  - name: detect magic
    source: Magus
    level: 0
  - name: ghost sound
    source: Magus
    level: 0
    DC: 14
  - name: ray of frost
    source: Magus
    level: 0
  sources:
  - name: Magus
    type: prepared
    CL: 14
    concentration: 18
    slots:
      0: at-will
tactics:
  Before Combat: The vampire lord casts stoneskin on herself.
  During Combat: The vampire casts cloak of winds, expeditious retreat, greater invisibility,
    and shield on herself. She uses accurate strike against better-defended opponents,
    Mobility to avoid flanking, and Flanking Foil to negate sneak attacks.
ability_scores:
  STR: 26
  DEX: 14
  CON:
  INT: 18
  WIS: 15
  CHA: 20
BAB: 10
CMB: 18
CMD: 32
feats:
- is_bonus: true
  name: Alertness
- name: Combat Casting
- name: Critical Focus
- name: Disruptive
- is_bonus: true
  name: Dodge
- superscripts:
  - UC
  name: Flanking Foil
- name: Improved Critical (longsword)
- is_bonus: true
  name: Improved Initiative
- is_bonus: true
  name: Lightning Reflexes
- name: Mobility
- name: Power Attack
- name: Skill Focus (Perception)
- name: SpellbreakerB
- name: ToughnessB
- name: Weapon Focus (longsword)
- name: Weapon Specialization (longsword)
skills:
  Diplomacy: 12
  Intimidate: 22
  Knowledge (arcana): 21
  Knowledge (dungeoneering): 21
  Knowledge (local): 11
  Knowledge (nobility): 11
  Perception: 35
  Sense Motive: 12
  Spellcraft: 21
  Use Magic Device: 15
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
    Sense Motive:
      _: 8
    Stealth:
      _: 8
languages:
- Common
- Dwarven
- Elven
- Giant
- Sylvan
- Undercommon
special_qualities:
- arcane pool (11 points, +4)
- change shape (dire bat or wolf, beast shape II)
- elf blood
- fighter training (fighter level 7)
- gaseous form
- heavy armor proficiency
- improved spell recall
- knowledge pool
- magus arcana (accurate strike, concentrate, spell shield, spellbreaker) medium armor
  proficiency
- shadowless
- spider climb
gear:
  gear:
  - +1 breastplate
  - +1 frost longsword
  - amulet of natural armor +1
  - belt of physical might +2 (Str, Dex)
  - cloak of resistance +2
  - headband of alluring charisma +4
  - ring of protection +1
  - granite and diamond dust (worth 500 gp)
  - 835 gp
ecology:
  environment: any
desc_long: A vampire lord is a ruthless, calculating noble or other figure of authority
  that dominates her political landscape.

---

# Vampire, Vampire Lord

**Source** Monster Codex pg. 243
**XP** 51,200
Half-elf _[[monsters/Vampire|vampire]]_ _[[classes/Magus|magus]]_ 14 (Pathfinder RPG Ultimate Magic 9)

NE Medium undead (augmented humanoid, elf, human)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +35

##### Defense

**AC** 28, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+7 armor, +1 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +7 natural)
**hp** 150 (14d8+84); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +16, **Ref** +10, **Will** +13; +2 vs. enchantments
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 10/magic and silver; **Immune** sleep, _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** cold 10, electricity 10
**Weaknesses** _vampire_ weaknesses

##### Offense
**Speed** 20 ft.
**Melee** +1 frost _[[items/Weapon/Longsword|longsword]]_ +20/+15 (1d8+11/17–20 plus 2d6), slam +13 (1d4+8 plus _[[universal monster rules/Energy Drain|energy drain]]_)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_, children of the night, create spawn, dominate (DC 22), _energy drain_ (2 levels, DC 22), greater spell combat, improved spell combat, spell combat (–2 attack, +2 concentration, double bonus), spellstrike
**_Magus_ Spells Prepared **(CL 14th; concentration +18)
5th—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 19), _[[spells/Monstrous Physique III|monstrous physique III]]_
4th—_[[spells/Fire Shield|fire shield]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Ice Storm|ice storm]]_, _[[spells/Shout|shout]]_ (DC 18), _[[spells/Stoneskin|stoneskin]]_
3rd—_[[spells/Cloak of Winds|cloak of winds]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 17), _[[spells/Haste|haste]]_, _[[spells/Slow|slow]]_ (DC 17)
2nd—_[[spells/Darkness|darkness]]_, _[[spells/Frigid Touch|frigid touch]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Scorching Ray|scorching ray]]_ (2), web (DC 16)
1st—_[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Frostbite|frostbite]]_, _[[spells/Shield|shield]]_, _[[spells/Shocking Grasp|shocking grasp]]_ (2), _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 14), _[[spells/Ray of Frost|ray of frost]]_

### Tactics

**Before Combat** The _vampire_ lord casts _stoneskin_ on herself.
 **During Combat** The _vampire_ casts _cloak of winds_, _expeditious retreat_, greater _invisibility_, and _shield_ on herself. She uses accurate strike against better-defended opponents, _[[feats/Mobility|Mobility]]_ to avoid flanking, and _[[feats/Flanking Foil|Flanking Foil]]_ to negate sneak attacks.

##### Statistics
**Str** 26, **Dex** 14, **Con** —, **Int** 18, **Wis** 15, **Cha** 20
**Base Atk** +10; **CMB** +18; **CMD** 32
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Disruptive|Disruptive]]_, _Dodge_, _Flanking Foil_, _[[feats/Improved Critical|Improved Critical]]_ (_longsword_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _Mobility_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), SpellbreakerB, ToughnessB, _[[feats/Weapon Focus|Weapon Focus]]_ (_longsword_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_longsword_)
**Skills** Diplomacy +12, Intimidate +22, Knowledge (arcana) +21, Knowledge (dungeoneering) +21, Knowledge (local) +11, Knowledge (nobility) +11, Perception +35, Sense Motive +12, Spellcraft +21, Use Magic Device +15; **Racial Modifiers** +8 Bluff, +8 Perception, +8 Sense Motive, +8 Stealth
**Languages** Common, Dwarven, Elven, Giant, Sylvan, Undercommon
**SQ** arcane pool (11 points, +4), _[[universal monster rules/Change Shape|change shape]]_ (dire bat or _[[monsters/Wolf|wolf]]_, _[[spells/Beast Shape II|beast shape II]]_), elf blood, _[[classes/Fighter|fighter]]_ _[[items/Weapon Magic Abilities/Training|training]]_ (_fighter_ level 7), _[[spells/Gaseous Form|gaseous form]]_, _[[feats/Heavy Armor Proficiency|heavy armor proficiency]]_, improved spell recall, knowledge pool, _magus_ arcana (accurate strike, concentrate, spell _shield_, _[[items/Weapon/Spellbreaker|spellbreaker]]_) _[[feats/Medium Armor Proficiency|medium armor proficiency]]_, shadowless, _[[spells/Spider Climb|spider climb]]_
**Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 frost _longsword_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Physical Might +2|belt of physical might +2]]_ (Str, Dex), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, granite and diamond dust (worth 500 gp), 835 gp

##### Ecology

**Environment** any

##### Description

A _vampire_ lord is a ruthless, calculating noble or other figure of authority that dominates her political landscape.