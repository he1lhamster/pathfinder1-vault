---
cssclass: [monsters]
title1: Gambler
title2: Gambler
CR: 6
sources:
- name: NPC Codex
  page: 30
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 2400
race: Dwarf
classes:
- bard 7
alignment: N
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 1
AC:
  AC: 16
  touch: 11
  flat_footed: 15
  components:
    armor: 5
    dex: 1
HP:
  HP: 49
  long: 7d8+14
saves:
  fort: 3
  ref: 6
  will: 5
  other: +2 vs. poison, spells, and spell-like abilities, +4 vs. bardic performance,
    language-dependent, and sonic
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: unarmed strike +10 (1d3+4)
      entries:
      - - damage: 1d3+4
      attack: unarmed strike
      bonus:
      - 10
  - - text: mwk dagger +10 (1d4+4/19-20)
      entries:
      - - damage: 1d4+4
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 10
  ranged:
  - - text: dagger +6 (1d4+4/19-20)
      entries:
      - - damage: 1d4+4
          crit_range: 19-20
      attack: dagger
      bonus:
      - 6
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
  - bardic performance 20 rounds/day (move action; countersong, distraction, fascinate,
    inspire competence +3, inspire courage +2, suggestion)
spells:
  entries:
  - name: confusion
    source: Bard
    level: 3
    DC: 17
  - name: glibness
    source: Bard
    level: 3
  - name: cure moderate wounds
    source: Bard
    level: 2
    DC: 16
  - name: detect thoughts
    source: Bard
    level: 2
    DC: 16
  - name: eagle's splendor
    source: Bard
    level: 2
  - name: invisibility
    source: Bard
    level: 2
  - name: charm person
    source: Bard
    level: 1
    DC: 15
  - name: comprehend languages
    source: Bard
    level: 1
  - name: expeditious retreat
    source: Bard
    level: 1
  - name: unseen servant
    source: Bard
    level: 1
  - name: daze
    source: Bard
    level: 0
    DC: 14
  - name: detect magic
    source: Bard
    level: 0
  - name: mage hand
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 7
    concentration: 11
    slots:
      3: 1
      2: 4
      1: 5
      0: at-will
tactics:
  Before Combat: The bard casts eagle's splendor.
  During Combat: The bard brings his fists to any brawl that breaks out when he or
    someone else gets caught cheating. He alternates between making melee attacks
    and using confusion to reduce the number of effective combatants.
  Base Statistics: Without eagle's splendor, the bard's statistics are Bard Spells
    Known reduce spell DCs by 2; Cha 14; Skills Bluff +12, Diplomacy +4, Intimidate
    +14, Perform (comedy) +15, Perform (oratory) +12.
ability_scores:
  STR: 18
  DEX: 13
  CON: 12
  INT: 12
  WIS: 10
  CHA: 18
BAB: 5
CMB: 9
CMD: 20
CMD_other: 24 vs. bull rush or trip
feats:
- name: Improved Unarmed Strike
- name: Persuasive
- name: Skill Focus (Perform [comedy])
- name: Weapon Focus (unarmed strike)
skills:
  Bluff: 14
  Diplomacy: 6
  Intimidate: 16
  Knowledge (arcane): 8
  Knowledge (dungeoneering): 8
  Knowledge (geography): 8
  Knowledge (history): 8
  Knowledge (local): 8
  Knowledge (nature): 8
  Knowledge (religion): 8
  Perception: 10
    to notice unusual stonework: 12
  Perform (comedy): 17
  Perform (oratory): 14
  Sense Motive: 10
languages:
- Common
- Dwarven
special_qualities:
- bardic knowledge +3
- lore master 1/day
- versatile performance (comedy, oratory)
gear:
  combat:
  - elixir of vision
  other:
  - +1 chain shirt
  - masterwork dagger
  - belt of giant strength +2
  - 198 gp
desc_long: Gamblers lounge in dark corners of taverns and gambling dens, using their
  keen wits and talents to make a living.

---

# Gambler

**Source** NPC Codex pg. 30
**XP** 2,400
Dwarf _[[classes/Bard|bard]]_ 7

N Medium humanoid (dwarf)
**Init** +1; **Senses** Perception +10

##### Defense

**AC** 16, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 armor, +1 Dex)
**hp** 49 (7d8+14)
**Fort** +3, **Ref** +6, **Will** +5; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_, +4 vs. bardic performance, language-dependent, and sonic
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** unarmed strike +10 (1d3+4) or mwk _[[items/Weapon/Dagger|dagger]]_ +10 (1d4+4/19–20)
**Ranged** _dagger_ +6 (1d4+4/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids, bardic performance 20 rounds/day (move action; countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire competence +3, inspire courage +2, _[[spells/Suggestion|suggestion]]_)
**_Bard_ Spells Known **(CL 7th; concentration +11)
3rd (1/day)—_[[spells/Confusion|confusion]]_ (DC 17), _[[spells/Glibness|glibness]]_
2nd (4/day)—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (DC 16), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), _[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Invisibility|invisibility]]_
1st (5/day)—_[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Daze|daze]]_ (DC 14), _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Prestidigitation|prestidigitation]]_

### Tactics

**Before Combat **The _bard_ casts _eagle_’s splendor.
**During Combat **The _bard_ brings his fists to any brawl that breaks out when he or someone else gets caught cheating. He alternates between making melee attacks and using _confusion_ to reduce the number of effective combatants.
**Base Statistics **Without _eagle_’s splendor, the _bard_’s statistics are **_Bard_ Spells Known **reduce spell DCs by 2; **Cha **14; **Skills **Bluff +12, Diplomacy +4, Intimidate +14, Perform (comedy) +15, Perform (oratory) +12.

##### Statistics
**Str** 18, **Dex** 13, **Con** 12, **Int** 12, **Wis** 10, **Cha** 18
**Base Atk** +5; **CMB** +9; **CMD** 20 (24 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perform [comedy]), _[[feats/Weapon Focus|Weapon Focus]]_ (unarmed strike)
**Skills** Bluff +14, Diplomacy +6, Intimidate +16, Knowledge (arcane, dungeoneering, geography, history, local, nature, religion) +8, Perception +10 (+12 to notice unusual stonework), Perform (comedy) +17, Perform (oratory) +14, Sense Motive +10
**Languages** Common, Dwarven
**SQ** bardic knowledge +3, lore master 1/day, versatile performance (comedy, oratory)
**Combat Gear** _[[items/Wondrous Item/Elixir of Vision|elixir of vision]]_; **Other Gear** +1 _[[items/Armor/Chain shirt|chain shirt]]_, masterwork _dagger_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, 198 gp

Gamblers lounge in dark corners of taverns and gambling dens, using their _[[items/Weapon Magic Abilities/Keen|keen]]_ wits and talents to make a living.