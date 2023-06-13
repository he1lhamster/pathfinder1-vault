---
cssclass: [monsters]
title1: Ice Maiden
title2: Ice Maiden
CR: 19
sources:
- name: NPC Codex
  page: 215
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 204800
race: Elf
classes:
- sorcerer 10
- dragon disciple 10
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 7
senses:
  blindsense: 60
  low-light vision: true
AC:
  AC: 32
  touch: 18
  flat_footed: 28
  components:
    armor: 4
    deflection: 3
    dex: 3
    dodge: 1
    insight: 1
    natural: 10
HP:
  HP: 222
  long: 10d6+10d12+120
saves:
  fort: 18
  ref: 12
  will: 17
  other: +2 vs. enchantments
speeds:
  base: 30
  fly: 90
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 claws +15 (1d6+1 plus 1d6 cold)
      entries:
      - - damage: 1d6+1
        - damage: 1d6
          type: cold
      count: 2
      attack: claws
      bonus:
      - 15
    - text: bite +15 (1d6+1 plus 1d6 cold)
      entries:
      - - damage: 1d6+1
        - damage: 1d6
          type: cold
      attack: bite
      bonus:
      - 15
  ranged:
  - - text: +1 composite longbow +16/+11/+6 (1d8+2/×3)
      entries:
      - - damage: 1d8+2
          crit_multiplier: 3
      attack: +1 composite longbow
      bonus:
      - 16
      - 11
      - 6
  special:
  - breath weapon (30-foot cone, 20d6 cold, DC 27, 4/day)
  - claws (2, 1d6+1 plus 1d6 cold, magic, 10 rounds/day)
  - dragon bite
spell_like_abilities:
  entries:
  - name: form of the dragon II
    source: default
    freq: 2/day
    other: white dragon only
  sources:
  - name: default
    CL: 20
    concentration: 27
spells:
  entries:
  - name: form of the dragon III
    source: Sorcerer
    level: 8
  - name: polar ray
    source: Sorcerer
    level: 8
  - name: sunburst
    source: Sorcerer
    level: 8
    DC: 27
  - name: delayed blast fireball
    source: Sorcerer
    level: 7
    DC: 26
  - name: form of the dragon II
    source: Sorcerer
    level: 7
  - name: mass hold person
    source: Sorcerer
    level: 7
    DC: 24
  - name: prismatic spray
    source: Sorcerer
    level: 7
  - name: control water
    source: Sorcerer
    level: 6
  - name: disintegrate
    source: Sorcerer
    level: 6
    DC: 23
  - name: form of the dragon I
    source: Sorcerer
    level: 6
  - name: freezing sphere
    source: Sorcerer
    level: 6
    DC: 25
  - name: blight
    source: Sorcerer
    level: 5
    DC: 22
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 24
  - name: dream
    source: Sorcerer
    level: 5
  - name: spell resistance
    source: Sorcerer
    level: 5
  - name: wall of force
    source: Sorcerer
    level: 5
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: fear
    source: Sorcerer
    level: 4
    DC: 21
  - name: ice storm
    source: Sorcerer
    level: 4
  - name: stoneskin
    source: Sorcerer
    level: 4
  - name: wall of ice
    source: Sorcerer
    level: 4
    DC: 23
  - name: displacement
    source: Sorcerer
    level: 3
  - name: fly
    source: Sorcerer
    level: 3
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 22
  - name: sleet storm
    source: Sorcerer
    level: 3
  - name: vampiric touch
    source: Sorcerer
    level: 3
  - name: darkvision
    source: Sorcerer
    level: 2
  - name: gust of wind
    source: Sorcerer
    level: 2
    DC: 21
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: see invisibility
    source: Sorcerer
    level: 2
  - name: web
    source: Sorcerer
    level: 2
    DC: 19
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 18
  - name: expeditious retreat
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: silent image
    source: Sorcerer
    level: 1
    DC: 18
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: disrupt undead
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: ray of frost
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
    DC: 17
  sources:
  - name: Sorcerer
    type: known
    CL: 17
    concentration: 24
    slots:
      8: 4
      7: 7
      6: 7
      5: 7
      4: 7
      3: 8
      2: 8
      1: 8
      0: at-will
    bloodline: draconic (white)
tactics:
  Before Combat: The dragon disciple casts stoneskin.
  During Combat: The dragon disciple casts shield and spell resistance on herself,
    then takes flight and rains down destructive spells augmented with Empower Spell.
  Base Statistics: Without stoneskin, the dragon disciple's statistics are DR none.
ability_scores:
  STR: 12
  DEX: 16
  CON: 20
  INT: 16
  WIS: 10
  CHA: 25
BAB: 12
CMB: 13
CMD: 31
feats:
- name: Combat Casting
- name: Dodge
- name: Empower Spell
- name: Eschew Materials
- name: Great Fortitude
- name: Greater Spell Focus (evocation)
- name: Improved Initiative
- name: Iron Will
- name: Mobility
- name: Nimble Moves
- name: Quicken Spell
- name: Spell Focus (evocation)
- name: Spell Penetration
- name: Toughness
- name: Weapon Finesse
skills:
  Climb: 6
  Diplomacy: 12
  Fly: 11
  Heal: 5
  Intimidate: 15
  Knowledge (arcana): 11
  Knowledge (geography): 8
  Knowledge (local): 8
  Knowledge (nature): 8
  Knowledge (nobility): 8
  Knowledge (planes): 8
  Perception: 20
  Sense Motive: 5
  Spellcraft: 11
    to identify magic item properties: 13
  Stealth: 13
  Survival: 5
  Use Magic Device: 15
languages:
- Auran
- Common
- Draconic
- Elven
- Goblin
special_qualities:
- blood of dragons
- bloodline arcana (cold spells deal +1 damage per die)
- elven magic
- weapon familiarity
- wings
gear:
  combat:
  - wand of cure serious wounds (10 charges)
  - wand of lightning bolt (10 charges)
  other:
  - +1 composite longbow (+1 Str) with 20 arrows
  - amulet of natural armor +3
  - belt of mighty constitution +6
  - boots of the winterlands
  - bracers of armor +4
  - cloak of resistance +3
  - dusty rose prism ioun stone
  - headband of alluring charisma +6
  - ring of force shield
  - ring of protection +3
  - 3,099 gp
desc_long: With the patience of elves and the majesty of dragons, ice maidens are
  masters of subtle machinations-and of the battlefield.

---

# Ice Maiden

**Source** NPC Codex pg. 215
**XP** 204,800
Elf _[[classes/Sorcerer|sorcerer]]_ 10/dragon disciple 10

NE Medium humanoid (elf)
**Init** +7; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +20

##### Defense

**AC** 32, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+4 armor, +3 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +1 insight, +10 natural)
**hp** 222 (10d6+10d12+120)
**Fort** +18, **Ref** +12, **Will** +17; +2 vs. enchantments

##### Offense
**Speed** 30 ft., fly 90 ft. (average)
**Melee** 2 claws +15 (1d6+1 plus 1d6 cold), bite +15 (1d6+1 plus 1d6 cold)
**Ranged** +1 _[[items/Weapon/Composite longbow|composite longbow]]_ +16/+11/+6 (1d8+2/×3)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-foot cone, 20d6 cold, DC 27, 4/day), claws (2, 1d6+1 plus 1d6 cold, magic, 10 rounds/day), dragon bite
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
2/day—_[[spells/Form of the Dragon II|form of the dragon II]]_ (white dragon only)
**_Sorcerer_ Spells Known **(CL 17th; concentration +24)
8th (4/day)—_[[spells/Form of the Dragon III|form of the dragon III]]_, _[[spells/Polar Ray|polar ray]]_, _[[spells/Sunburst|sunburst]]_ (DC 27)
7th (7/day)—_[[spells/Delayed Blast Fireball|delayed blast fireball]]_ (DC 26), _form of the dragon II_, mass _[[spells/Hold Person|hold person]]_ (DC 24), _[[spells/Prismatic Spray|prismatic spray]]_
6th (7/day)—_[[spells/Control Water|control water]]_, _[[spells/Disintegrate|disintegrate]]_ (DC 23), _[[spells/Form of the Dragon I|form of the dragon I]]_, _[[spells/Freezing Sphere|freezing sphere]]_ (DC 25)
5th (7/day)—_[[spells/Blight|blight]]_ (DC 22), _[[spells/Cone of Cold|cone of cold]]_ (DC 24), _[[spells/Dream|dream]]_, _[[universal monster rules/Spell Resistance|spell resistance]]_, _[[spells/Wall Of Force|wall of force]]_
4th (7/day)—_[[spells/Dimension Door|dimension door]]_, _[[universal monster rules/Fear|fear]]_ (DC 21), _[[spells/Ice Storm|ice storm]]_, _[[spells/Stoneskin|stoneskin]]_, _[[spells/Wall Of Ice|wall of ice]]_ (DC 23)
3rd (8/day)—_[[spells/Displacement|displacement]]_, fly, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 22), _[[spells/Sleet Storm|sleet storm]]_, _[[spells/Vampiric Touch|vampiric touch]]_
2nd (8/day)—_[[spells/Darkvision|darkvision]]_, _[[spells/Gust Of Wind|gust of wind]]_ (DC 21), _[[spells/Invisibility|invisibility]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/See Invisibility|see invisibility]]_, web (DC 19)
1st (8/day)—_[[spells/Charm Person|charm person]]_ (DC 18), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/Silent Image|silent image]]_ (DC 18)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 17)
**Bloodline **draconic (white)

### Tactics

**Before Combat **The dragon disciple casts _stoneskin_.
**During Combat **The dragon disciple casts _shield_ and _spell resistance_ on herself, then takes _[[universal monster rules/Flight|flight]]_ and rains down destructive spells augmented with _[[feats/Empower Spell|Empower Spell]]_.
**Base Statistics **Without _stoneskin_, the dragon disciple’s statistics are DR none.

##### Statistics
**Str** 12, **Dex** 16, **Con** 20, **Int** 16, **Wis** 10, **Cha** 25
**Base Atk** +12; **CMB** +13; **CMD** 31
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _Empower Spell_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Nimble Moves|Nimble Moves]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +6, Diplomacy +12, Fly +11, _[[spells/Heal|Heal]]_ +5, Intimidate +15, Knowledge (arcana) +11, Knowledge (geography, local, nature, nobility, planes) +8, Perception +20, Sense Motive +5, Spellcraft +11 (+13 to _[[spells/Identify|identify]]_ magic item properties), Stealth +13, Survival +5, Use Magic Device +15
**Languages** Auran, Common, Draconic, Elven, _[[monsters/Goblin|Goblin]]_
**SQ** blood of dragons, bloodline arcana (cold spells deal +1 damage per die), elven magic, weapon familiarity, wings
**Combat Gear** wand of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (10 charges), wand of _lightning bolt_ (10 charges); **Other Gear** +1 _composite longbow_ (+1 Str) with 20 arrows, _[[items/Wondrous Item/Amulet of Natural Armor +3|amulet of natural armor +3]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +6|belt of mighty constitution +6]]_, _[[items/Wondrous Item/Boots of the Winterlands|boots of the winterlands]]_, _[[items/Wondrous Item/Bracers of Armor +4|bracers of armor +4]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Dusty Rose Prism Ioun Stone|dusty rose prism ioun stone]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +6|headband of alluring charisma +6]]_, _[[items/Ring/Ring of Force Shield|ring of force shield]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, 3,099 gp

With the patience of elves and the majesty of dragons, ice maidens are masters of subtle machinations—and of the battlefield.