---
cssclass: [monsters]
title1: Stage Magician
title2: Stage Magician
CR: 8
sources:
- name: NPC Codex
  page: 204
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 4800
race: Half-orc
classes:
- bard 4
- rogue 3
- arcane trickster 2
alignment: N
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 9
senses:
  darkvision: 60
AC:
  AC: 21
  touch: 17
  flat_footed: 15
  components:
    armor: 3
    deflection: 1
    dex: 5
    dodge: 1
    natural: 1
HP:
  HP: 51
  long: 4d8+3d8+2d6+9
saves:
  fort: 6
  ref: 15
  will: 7
  other: +4 vs. bardic performance, language-dependent, and sonic
defensive_abilities:
- evasion
- orc ferocity
- trap sense +1
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 light mace +9/+4 (1d6+1)
      entries:
      - - damage: 1d6+1
      attack: +1 light mace
      bonus:
      - 9
      - 4
  ranged:
  - - text: dagger +13 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: dagger
      bonus:
      - 13
  - - text: light mace +13 (1d6)
      entries:
      - - damage: 1d6
      attack: light mace
      bonus:
      - 13
  special:
  - bardic performance 12 rounds/day (countersong, distraction, fascinate, inspire
    competence +2, inspire courage +1)
  - sneak attack +3d6
spells:
  entries:
  - name: cat's grace
    source: Bard
    level: 2
  - name: cure moderate wounds
    source: Bard
    level: 2
    DC: 14
  - name: eagle's splendor
    source: Bard
    level: 2
  - name: suggestion
    source: Bard
    level: 2
    DC: 14
  - name: animate rope
    source: Bard
    level: 1
  - name: charm person
    source: Bard
    level: 1
    DC: 13
  - name: silent image
    source: Bard
    level: 1
    DC: 13
  - name: sleep
    source: Bard
    level: 1
    DC: 13
  - name: dancing lights
    source: Bard
    level: 0
  - name: detect magic
    source: Bard
    level: 0
  - name: lullaby
    source: Bard
    level: 0
    DC: 12
  - name: mage hand
    source: Bard
    level: 0
  - name: mending
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 6
    concentration: 8
    slots:
      2: 4
      1: 5
      0: at-will
tactics:
  Before Combat: The arcane trickster drinks his potion of heroism and casts cat's
    grace on himself.
  During Combat: The trickster starts by throwing the light maces he uses for his
    juggling act, then casts charm person and suggestion to help even the odds.
  Base Statistics: Without heroism, the arcane trickster's statistics are Init +7;
    Fort +4, Ref +11, Will +5; Melee +1 light mace +7/+2 (1d6+1); Ranged dagger +9
    (1d4/19-20) or light mace +9 (1d6); Dex 17; CMD 21; Skills Acrobatics +15, Disable
    Device +15, Escape Artist +15, Handle Animal +3, Intimidate +4, Knowledge (arcana)
    +11, Perception +11, Perform (comedy) +9, Ride +4, Sense Motive +6, Sleight of
    Hand +15, Stealth +15, Swim +4, Use Magic Device +14.
ability_scores:
  STR: 10
  DEX: 21
  CON: 13
  INT: 14
  WIS: 8
  CHA: 14
BAB: 6
CMB: 6
CMD: 23
feats:
- name: Catch Off-Guard
- name: Combat Casting
- name: Dodge
- name: Improved Initiative
- name: Throw Anything
skills:
  Acrobatics: 19
  Disable Device: 19
  Escape Artist: 19
  Handle Animal: 5
  Intimidate: 6
  Knowledge (arcana): 13
  Perception: 13
  Perform (comedy): 11
  Ride: 8
  Sense Motive: 8
  Sleight of Hand: 19
  Stealth: 19
  Swim: 6
  Use Magic Device: 16
languages:
- Celestial
- Common
- Goblin
special_qualities:
- bardic knowledge +2
- orc blood
- ranged legerdemain
- rogue talents (ledge walker)
- trapfinding +1
- versatile performance (comedy)
- weapon familiarity
gear:
  combat:
  - potion of delay poison
  - potion of heroism
  - potions of invisibility (2)
  - potion of pass without trace
  - scrolls of summon monster I (3)
  - acid (4)
  - holy water (4)
  - smokesticks (4)
  - tanglefoot bags (4)
  - thunderstones (4)
  other:
  - +1 leather armor
  - +1 light mace
  - dagger (6)
  - light mace (6)
  - amulet of natural armor +1
  - ring of protection +1
  - everburning torches (4)
  - masterwork thieves' tools
  - spell component pouch
  - 53 gp
desc_long: Stage magicians use their skills to entertain nobles in theaters and crowds
  of commoners on street corners.

---

# Stage Magician

**Source** NPC Codex pg. 204
**XP** 4,800
Half-orc _[[classes/Bard|bard]]_ 4/rogue 3/arcane trickster 2

N Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +13

##### Defense

**AC** 21, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+3 armor, +1 _[[spells/Deflection|deflection]]_, +5 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural)
**hp** 51 (4d8+3d8+2d6+9)
**Fort** +6, **Ref** +15, **Will** +7; +4 vs. bardic performance, language-dependent, and sonic
**Defensive Abilities** evasion, _orc_ _[[universal monster rules/Ferocity|ferocity]]_, trap sense +1

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Light mace|light mace]]_ +9/+4 (1d6+1)
**Ranged** _[[items/Weapon/Dagger|dagger]]_ +13 (1d4/19–20) or _light mace_ +13 (1d6)
**Special Attacks** bardic performance 12 rounds/day (countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire competence +2, inspire courage +1), sneak attack +3d6
**_Bard_ Spells Known **(CL 6th; concentration +8)
2nd (4/day)—cat’s _[[spells/Grace|grace]]_, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (DC 14), _[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Suggestion|suggestion]]_ (DC 14)
1st (5/day)—_[[spells/Animate Rope|animate rope]]_, _[[spells/Charm Person|charm person]]_ (DC 13), _[[spells/Silent Image|silent image]]_ (DC 13), sleep (DC 13)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Lullaby|lullaby]]_ (DC 12), _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Prestidigitation|prestidigitation]]_

### Tactics

**Before Combat **The arcane trickster drinks his potion of _[[spells/Heroism|heroism]]_ and casts cat’s _grace_ on himself.
**During Combat **The trickster starts by _[[items/Weapon Magic Abilities/Throwing|throwing]]_ the light maces he uses for his juggling act, then casts _charm person_ and _suggestion_ to help even the odds.
**Base Statistics **Without _heroism_, the arcane trickster’s statistics are **Init **+7; **Fort **+4, **Ref **+11, **Will **+5; **Melee** +1 _light mace_ +7/+2 (1d6+1); **Ranged **_dagger_ +9 (1d4/19–20) or _light mace_ +9 (1d6); **Dex **17; **CMD **21; **Skills **Acrobatics +15, Disable Device +15, Escape Artist +15, Handle Animal +3, Intimidate +4, Knowledge (arcana) +11, Perception +11, Perform (comedy) +9, Ride +4, Sense Motive +6, Sleight of Hand +15, Stealth +15, Swim +4, Use Magic Device +14.

##### Statistics
**Str** 10, **Dex** 21, **Con** 13, **Int** 14, **Wis** 8, **Cha** 14
**Base Atk** +6; **CMB** +6; **CMD** 23
**Feats** _[[feats/Catch Off-Guard|Catch Off-Guard]]_, _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Throw Anything|Throw Anything]]_
**Skills** Acrobatics +19, Disable Device +19, Escape Artist +19, Handle Animal +5, Intimidate +6, Knowledge (arcana) +13, Perception +13, Perform (comedy) +11, Ride +8, Sense Motive +8, Sleight of Hand +19, Stealth +19, Swim +6, Use Magic Device +16
**Languages** Celestial, Common, _[[monsters/Goblin|Goblin]]_
**SQ** bardic knowledge +2, _orc_ blood, ranged legerdemain, _[[classes/Rogue|rogue]]_ talents (_[[feats/Ledge Walker|ledge walker]]_), trapfinding +1, versatile performance (comedy), weapon familiarity
**Combat Gear** potion of _[[spells/Delay Poison|delay poison]]_, potion of _heroism_, potions of _[[spells/Invisibility|invisibility]]_ (2), potion of _[[spells/Pass without Trace|pass without trace]]_, scrolls of _[[spells/Summon Monster I|summon monster I]]_ (3), acid (4), _[[items/Mundane/Holy water|holy water]]_ (4), smokesticks (4), tanglefoot bags (4), thunderstones (4); **Other Gear** +1 _[[items/Armor/Leather armor|leather armor]]_, +1 _light mace_, _dagger_ (6), _light mace_ (6), _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, everburning torches (4), masterwork thieves’ tools, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 53 gp

Stage magicians use their skills to entertain nobles in theaters and crowds of commoners on street corners.