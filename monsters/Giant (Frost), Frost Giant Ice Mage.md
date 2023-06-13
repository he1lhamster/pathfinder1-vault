---
cssclass: [monsters]
title1: Giant (Frost), Frost Giant Ice Mage
title2: Frost Giant Ice Mage
CR: 12
sources:
- name: Monster Codex
  page: 72
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 19200
race: Frost
classes:
- giant sorcerer 6
alignment: CE
size: Large
type: humanoid
subtypes:
- cold
- giant
initiative:
  bonus: 4
senses:
  low-light vision: true
AC:
  AC: 26
  touch: 10
  flat_footed: 26
  components:
    armor: 2
    deflection: 1
    natural: 10
    shield: 4
    size: -1
HP:
  HP: 204
  long: 14d8+6d6+120
  HD: 20
saves:
  fort: 17
  ref: 8
  will: 11
defensive_abilities:
- rock catching
immunities:
- cold
weaknesses:
- vulnerable to fire
speeds:
  base: 40
attacks:
  melee:
  - - text: mwk morningstar +21/+16/+11 (2d6+12)
      entries:
      - - damage: 2d6+12
      attack: mwk morningstar
      bonus:
      - 21
      - 16
      - 11
  - - text: 2 slams +20 (1d8+8 plus 1d6 cold)
      entries:
      - - damage: 1d8+8
        - damage: 1d6
          type: cold
      count: 2
      attack: slams
      bonus:
      - 20
  ranged:
  - - text: rock +12 (1d8+12 plus 1d6 cold)
      entries:
      - - damage: 1d8+12
        - damage: 1d6
          type: cold
      attack: rock
      bonus:
      - 12
  special:
  - rock throwing (120 ft.)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: cold steel
    source: default
    freq: 7/day
    other: grant weapon or 50 ammunition frost weapon special ability for 3 rounds
  sources:
  - name: default
    CL: 6
    concentration: 9
spells:
  entries:
  - name: dispel magic
    source: Sorcerer
    level: 3
  - superscripts:
    - UM
    name: frigid touch
    source: Sorcerer
    level: 2
  - name: ice slick
    source: Sorcerer
    level: 2
  - name: rage
    source: Sorcerer
    level: 2
    DC: 16
  - name: enlarge person
    source: Sorcerer
    level: 1
  - name: expeditious retreat
    source: Sorcerer
    level: 1
  - name: obscuring mist
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: true strike
    source: Sorcerer
    level: 1
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 13
  - name: flare
    source: Sorcerer
    level: 0
    DC: 13
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 13
  sources:
  - name: Sorcerer
    type: known
    CL: 6
    concentration: 9
    slots:
      3: 4
      2: 6
      1: 7
      0: at-will
    bloodline: boreal
tactics:
  Before Combat: A frost giant ice mage casts shield and expeditious retreat.
  During Combat: A frost giant ice mage uses his wand of solid fog to trap opponents,
    then blasts them at range with his wand of ice storm or wand of lightning bolt.
    He casts ice slick and uses his icewalker bloodline ability to outmaneuver his
    opponents in icy and snowy areas.
ability_scores:
  STR: 26
  DEX: 11
  CON: 22
  INT: 14
  WIS: 14
  CHA: 16
BAB: 13
CMB: 22
CMD: 33
feats:
- name: Arcane Strike
- name: Born of Frost
- name: Chilled Rock
- name: Combat Casting
- name: Eschew Materials
- name: Extend Spell
- name: Improved Initiative
- name: Improved Lightning Reflexes
- name: Lightning Reflexes
- name: Power Attack
- name: Skill Focus (Stealth)
skills:
  Bluff: 12
  Climb: 21
  Craft (alchemy): 15
  Intimidate: 16
  Knowledge (arcana): 15
  Perception: 25
  Spellcraft: 15
  Stealth: 12
    in snow: 16
  _racial_mods:
    Stealth:
      in snow: 4
languages:
- Abyssal
- Auran
- Common
- Giant
special_qualities:
- icewalker
gear:
  combat:
  - potions of cure serious wounds (2)
  - potion of invisibility
  - potion of protection from energy (fire)
  - wand of ice storm (10 charges)
  - wand of lightning bolt (10 charges)
  - wand of solid fog (5 charges)
  - alchemist's fire (4)
  other:
  - mwk morningstar
  - amulet of natural armor +1
  - bracers of armor +2
  - ring of protection +1
  - 362 gp
ecology:
  environment: cold mountains
desc_long: Ice mages inherit the magic of the icy north. While some are tricksters
  and manipulators-perhaps using enlarge person to grow to Huge size and trick travelers
  into thinking they're cloud giants-many act as support and artillery for their tribe's
  raiders, killing at a distance with the power of a storm or increasing their allies'
  size and ferocity. As powerful as sorcerers may be, frost giant society still places
  more value in physical strength and melee prowess, meaning sorcerers are usually
  advisors rather than leaders.

---

# Giant (Frost), Frost Giant Ice Mage

**Source** Monster Codex pg. 72
**XP** 19,200
Frost giant _[[classes/Sorcerer|sorcerer]]_ 6
CE Large humanoid (cold, giant)
**Init** +4; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +25

##### Defense

**AC** 26, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+2 armor, +1 deflection, +10 natural, +4 _[[spells/Shield|shield]]_, –1 size)
**hp** 204 (20 HD; 14d8+6d6+120)
**Fort** +17, **Ref** +8, **Will** +11
**Defensive Abilities** _[[universal monster rules/Rock Catching|rock catching]]_; **Immune** cold
**Weaknesses** vulnerable to fire

##### Offense
**Speed** 40 ft.
**Melee** mwk _[[items/Weapon/Morningstar|morningstar]]_ +21/+16/+11 (2d6+12) or 2 slams +20 (1d8+8 plus 1d6 cold)
**Ranged** rock +12 (1d8+12 plus 1d6 cold)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +9)
7/day—cold steel (grant weapon or 50 ammunition frost weapon special ability for 3 rounds)
**_Sorcerer_ Spells Known **(CL 6th; concentration +9)
3rd (4/day)—_[[spells/Dispel Magic|dispel magic]]_
2nd (6/day)—_[[spells/Frigid Touch|frigid touch]]_, _[[spells/Ice Slick|ice slick]]_, _[[spells/Rage|rage]]_ (DC 16)
1st (7/day)—_[[spells/Enlarge Person|enlarge person]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _shield_, _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Flare|flare]]_ (DC 13), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 13)
**Bloodline** boreal

### Tactics

**Before Combat** A frost giant _[[npcs/Ice Mage|ice mage]]_ casts _shield_ and _expeditious retreat_.
 **During Combat** A frost giant _ice mage_ uses his wand of _[[spells/Solid Fog|solid fog]]_ to trap opponents, then blasts them at range with his wand of _[[spells/Ice Storm|ice storm]]_ or wand of _[[spells/Lightning Bolt|lightning bolt]]_. He casts _ice slick_ and uses his icewalker bloodline ability to outmaneuver his opponents in icy and snowy areas.

##### Statistics
**Str** 26, **Dex** 11, **Con** 22, **Int** 14, **Wis** 14, **Cha** 16
**Base Atk** +13; **CMB** +22; **CMD** 33
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Born Of Frost|Born of Frost]]_, _[[feats/Chilled Rock|Chilled Rock]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** Bluff +12, _[[universal monster rules/Climb|Climb]]_ +21, Craft (alchemy) +15, Intimidate +16, Knowledge (arcana) +15, Perception +25, Spellcraft +15, Stealth +12 (+16 in snow); **Racial Modifiers** +4 Stealth in snow
**Languages** Abyssal, Auran, Common, Giant
**SQ** icewalker
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), potion of _[[spells/Invisibility|invisibility]]_, potion of _[[spells/Protection from Energy|protection from energy]]_ (fire), wand of _ice storm_ (10 charges), wand of _lightning bolt_ (10 charges), wand of _solid fog_ (5 charges), _[[classes/Alchemist|alchemist]]_’s fire (4); **Other Gear** mwk _morningstar_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Bracers of Armor +2|bracers of armor +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 362 gp

##### Ecology

**Environment** cold mountains

##### Description

Ice mages inherit the magic of the icy north. While some are tricksters and manipulators—perhaps using _enlarge person_ to grow to Huge size and trick travelers into thinking they’re cloud giants—many act as support and artillery for their tribe’s raiders, killing at a distance with the power of a storm or increasing their allies’ size and _[[universal monster rules/Ferocity|ferocity]]_. As powerful as sorcerers may be, frost giant society still places more value in physical strength and melee prowess, meaning sorcerers are usually advisors rather than leaders.