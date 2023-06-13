---
cssclass: [monsters]
title1: Storm Prophet
title2: Storm Prophet
CR: 8
sources:
- name: NPC Codex
  page: 212
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Dwarf
classes:
- sorcerer 7
- dragon disciple 2
alignment: CE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 5
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 12
  flat_footed: 18
  components:
    armor: 4
    deflection: 1
    dex: 1
    natural: 3
HP:
  HP: 80
  long: 7d6+2d12+40
saves:
  fort: 9
  ref: 5
  will: 7
  other: +2 vs. poison, spells, and spell-like abilities
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 warhammer +11 (1d8+7/×3)
      entries:
      - - damage: 1d8+7
          crit_multiplier: 3
      attack: +1 warhammer
      bonus:
      - 11
  - - text: 2 claws +11 (1d6+6)
      entries:
      - - damage: 1d6+6
      count: 2
      attack: claws
      bonus:
      - 11
    - text: bite +10 (1d6+9)
      entries:
      - - damage: 1d6+9
      attack: bite
      bonus:
      - 10
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
  - dragon bite
  - claws (2, 1d4+4, magic, 5 rounds/day)
spells:
  entries:
  - name: greater invisibility
    source: Sorcerer
    level: 4
  - name: fly
    source: Sorcerer
    level: 3
  - name: heroism
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 15
  - name: false life
    source: Sorcerer
    level: 2
  - name: protection from arrows
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: enlarge person
    source: Sorcerer
    level: 1
    DC: 13
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: magic weapon
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: shocking grasp
    source: Sorcerer
    level: 1
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: detect poison
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 12
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 8
    concentration: 10
    slots:
      4: 3
      3: 5
      2: 7
      1: 7
      0: at-will
    bloodline: draconic (blue)
tactics:
  Before Combat: The dragon disciple drinks his potion of bull's strength, and casts
    false life and mage armor.
  During Combat: At range, the dragon disciple casts lightning bolt and scorching
    ray. If forced into melee, he casts heroism and greater invisibility first.
  Base Statistics: Without bull's strength, false life, and mage armor, the dragon
    disciple's statistics are AC 15, touch 12, flat-footed 14; hp no temporary hit
    points; Melee +1 warhammer +9 (1d8+5/×3) or bite +8 (1d6+6), 2 claws +9 (1d6+4);
    Str 18; CMB +8; CMD 20 (24 vs. bull rush or trip); Skills Climb +4.
ability_scores:
  STR: 22
  DEX: 12
  CON: 16
  INT: 10
  WIS: 10
  CHA: 14
BAB: 4
CMB: 10
CMD: 22
CMD_other: 26 vs. bull rush or trip
feats:
- name: Arcane Armor Mastery
- name: Arcane Armor Training
- name: Combat Casting
- name: Eschew Materials
- name: Great Fortitude
- name: Improved Initiative
- name: Power Attack
- name: Weapon Focus (claws)
skills:
  Bluff: 7
  Climb: 6
  Diplomacy: 5
  Intimidate: 6
  Knowledge (arcana): 8
  Knowledge (geography): 1
  Knowledge (nature): 1
  Linguistics: 1
  Perception: 10
    to notice unusual stonework: 12
  Perform (oratory): 3
  Survival: 2
languages:
- Common
- Draconic
- Dwarven
special_qualities:
- blood of dragons
- bloodline arcana (electricity spells deal +1 damage per die)
gear:
  combat:
  - potion of bull's strength
  - potion of cure moderate wounds
  other:
  - +1 warhammer
  - amulet of natural armor +1
  - cloak of resistance +1
  - headband of alluring charisma +2
  - ring of protection +1
  - 138 gp
desc_long: Storm prophets are as terrible as thunderheads and as capricious as tornados.

---

# Storm Prophet

**Source** NPC Codex pg. 212
**XP** 4,800
Dwarf _[[classes/Sorcerer|sorcerer]]_ 7/dragon disciple 2
CE Medium humanoid (dwarf)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +3 natural)
**hp** 80 (7d6+2d12+40)
**Fort** +9, **Ref** +5, **Will** +7; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Warhammer|warhammer]]_ +11 (1d8+7/×3) or 2 claws +11 (1d6+6) and bite +10 (1d6+9)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids, dragon bite, claws (2, 1d4+4, magic, 5 rounds/day)
**_Sorcerer_ Spells Known **(CL 8th; concentration +10)
4th (3/day)—greater _[[spells/Invisibility|invisibility]]_
3rd (5/day)—fly, _[[spells/Heroism|heroism]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 15)
2nd (7/day)—_[[spells/False Life|false life]]_, _[[spells/Protection From Arrows|protection from arrows]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (7/day)—_[[spells/Enlarge Person|enlarge person]]_ (DC 13), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Shield|shield]]_, _[[spells/Shocking Grasp|shocking grasp]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 12), light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[universal monster rules/Resistance|resistance]]_
**Bloodline **draconic (blue)

### Tactics

**Before Combat **The dragon disciple drinks his potion of bull’s strength, and casts _false life_ and _mage armor_.
**During Combat **At range, the dragon disciple casts _lightning bolt_ and _scorching ray_. If forced into melee, he casts _heroism_ and greater _invisibility_ first.
**Base Statistics **Without bull’s strength, _false life_, and _mage armor_, the dragon disciple’s statistics are **AC **15, touch 12, _flat-footed_ 14; **hp **no temporary hit points; **Melee** +1 _warhammer_ +9 (1d8+5/×3) or bite +8 (1d6+6), 2 claws +9 (1d6+4); **Str **18; **CMB **+8; **CMD **20 (24 vs. bull rush or _[[universal monster rules/Trip|trip]]_); **Skills **_[[universal monster rules/Climb|Climb]]_ +4.

##### Statistics
**Str** 22, **Dex** 12, **Con** 16, **Int** 10, **Wis** 10, **Cha** 14
**Base Atk** +4; **CMB** +10; **CMD** 22 (26 vs. bull rush or _trip_)
**Feats** _[[feats/Arcane Armor Mastery|Arcane Armor Mastery]]_, _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claws)
**Skills** Bluff +7, _Climb_ +6, Diplomacy +5, Intimidate +6, Knowledge (arcana) +8, Knowledge (geography) +1, Knowledge (nature) +1, Linguistics +1, Perception +10 (+12 to notice unusual stonework), Perform (oratory) +3, Survival +2
**Languages** Common, Draconic, Dwarven
**SQ** blood of dragons, bloodline arcana (electricity spells deal +1 damage per die)
**Combat Gear** potion of bull’s strength, potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_; **Other Gear** +1 _warhammer_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 138 gp

Storm prophets are as terrible as thunderheads and as capricious as tornados.