---
cssclass: [monsters]
title1: Master Storycrafter
title2: Master Storycrafter
CR: 16
sources:
- name: NPC Codex
  page: 234
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Half-elf
classes:
- sorcerer 10
- Pathfinder chronicler 7
alignment: N
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 22
  touch: 15
  flat_footed: 20
  components:
    armor: 5
    deflection: 3
    dex: 2
    natural: 2
HP:
  HP: 86
  long: 10d6+7d8+17
saves:
  fort: 10
  ref: 13
  will: 15
  other: +2 vs. enchantments
defensive_abilities:
- live to tell the tale (3/day)
DR:
- amount: 10
  weakness: magic
  max_absorb: 100
  other: ranged weapon attack only
immunities:
- sleep
speeds:
  base: 40
attacks:
  melee:
  - - text: quarterstaff +11/+6 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: quarterstaff
      bonus:
      - 11
      - 6
  ranged:
  - - text: dagger +14/+9 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 14
      - 9
  special:
  - bardic performance 23 rounds/day (countersong, distraction, epic tales, fascination,
    inspire action [move], inspire courage +2, inspire competence +2, whispering campaign)
spells:
  entries:
  - name: break enchantment
    source: Sorcerer
    level: 5
  - name: persistent image
    source: Sorcerer
    level: 5
    DC: 24
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: hallucinatory terrain
    source: Sorcerer
    level: 4
  - name: phantasmal killer
    source: Sorcerer
    level: 4
    DC: 23
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: heroism
    source: Sorcerer
    level: 3
  - name: invisibility sphere
    source: Sorcerer
    level: 3
  - name: major image
    source: Sorcerer
    level: 3
    DC: 22
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: protection from arrows
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: web
    source: Sorcerer
    level: 2
    DC: 19
  - name: animate rope
    source: Sorcerer
    level: 1
  - name: color spray
    source: Sorcerer
    level: 1
    DC: 20
  - name: disguise self
    source: Sorcerer
    level: 1
  - name: floating disk
    source: Sorcerer
    level: 1
  - name: identify
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 17
  - name: light
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 19
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 10
    concentration: 17
    slots:
      5: 4
      4: 6
      3: 8
      2: 8
      1: 8
      0: at-will
    bloodline: arcane
tactics:
  Before Combat: The Pathfinder chronicler casts heroism and protection from arrows.
  During Combat: The chronicler casts shield on herself, then supports allies with
    bardic performance and illusions.
  Base Statistics: Without heroism and protection from arrows, the Pathfinder chronicler's
    statistics are Fort +8, Ref +11, Will +13; DR none; Melee quarterstaff +9/+4 (1d6-1);
    Ranged dagger +12/+7 (1d4-1/19-20); Skills -2 on all skills.
ability_scores:
  STR: 8
  DEX: 14
  CON: 12
  INT: 14
  WIS: 10
  CHA: 24
BAB: 10
CMB: 9
CMD: 24
feats:
- name: Arcane Armor Training
- name: Combat Casting
- name: Enlarge Spell
- name: Eschew Materials
- name: Extend Spell
- name: Extra Performance
- name: Greater Spell Focus (illusion)
- name: Silent Spell
- name: Skill Focus (Perception)
- name: Spell Focus (illusion)
- name: Widen Spell
skills:
  Acrobatics: 9
    when jumping: 13
  Bluff: 17
  Diplomacy: 17
  Knowledge (arcana): 15
  Knowledge (dungeoneering): 15
  Knowledge (geography): 15
  Knowledge (history): 15
  Knowledge (local): 15
  Knowledge (nature): 15
  Knowledge (nobility): 15
  Knowledge (planes): 15
  Knowledge (religion): 15
  Linguistics: 10
  Perception: 23
  Perform (oratory): 17
  Perform (string): 17
  Profession (scribe): 10
  Sense Motive: 7
  Spellcraft: 12
  Stealth: 14
  Survival: 10
  Use Magic Device: 22
languages:
- Common
- Draconic
- Dwarven
- Elf
- Gnome
- Halfling
- Orc
special_qualities:
- arcane bond (staff of charming)
- bardic knowledge +3
- bloodline arcana (+1 DC for spells augmented by metamagic feats that increase spell
  level)
- call down the legends
- deep pockets (700 gp)
- elf blood
- improved aid
- master scribe
- metamagic adept (2/day)
- new arcana
- pathfinding
gear:
  combat:
  - potions of cure serious wounds (2)
  - potion of gaseous form
  - staff of charming
  other:
  - +3 leather armor
  - amulet of natural armor +2
  - boots of striding and springing
  - cloak of resistance +2
  - handy haversack
  - headband of alluring charisma +4
  - ring of protection +3
  - 1,290 gp
desc_long: These chroniclers travel with intrepid adventurers to record tales of their
  exploits.

---

# Master Storycrafter

**Source** NPC Codex pg. 234
**XP** 76,800
Half-elf _[[classes/Sorcerer|sorcerer]]_ 10/Pathfinder chronicler 7

N Medium humanoid (elf, human)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +23

##### Defense

**AC** 22, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+5 armor, +3 _[[spells/Deflection|deflection]]_, +2 Dex, +2 natural)
**hp** 86 (10d6+7d8+17)
**Fort** +10, **Ref** +13, **Will** +15; +2 vs. enchantments
**Defensive Abilities** live to tell the tale (3/day); **DR** 10/magic (ranged weapon attack only, 100 points); **Immune** sleep

##### Offense
**Speed** 40 ft.
**Melee** _[[items/Weapon/Quarterstaff|quarterstaff]]_ +11/+6 (1d6–1)
**Ranged** _[[items/Weapon/Dagger|dagger]]_ +14/+9 (1d4–1/19–20)
**Special Attacks** bardic performance 23 rounds/day (countersong, _[[universal monster rules/Distraction|distraction]]_, epic tales, fascination, inspire action [move], inspire courage +2, inspire competence +2, whispering campaign)
**_Sorcerer_ Spells Known **(CL 10th; concentration +17)
5th (4/day)—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Persistent Image|persistent image]]_ (DC 24)
4th (6/day)—_[[spells/Dimension Door|dimension door]]_, _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 23)
3rd (8/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Heroism|heroism]]_, _[[spells/Invisibility Sphere|invisibility sphere]]_, _[[spells/Major Image|major image]]_ (DC 22)
2nd (8/day)—_[[spells/Invisibility|invisibility]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Protection From Arrows|protection from arrows]]_, _[[spells/Scorching Ray|scorching ray]]_, web (DC 19)
1st (8/day)—_[[spells/Animate Rope|animate rope]]_, _[[spells/Color Spray|color spray]]_ (DC 20), _[[spells/Disguise Self|disguise self]]_, _[[spells/Floating Disk|floating disk]]_, _[[spells/Identify|identify]]_, _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 17), light, _[[spells/Ghost Sound|ghost sound]]_ (DC 19), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_
**Bloodline **arcane

### Tactics

**Before Combat **The _[[npcs/Pathfinder Chronicler|Pathfinder chronicler]]_ casts _heroism_ and _protection from arrows_.
**During Combat **The chronicler casts _shield_ on herself, then supports allies with bardic performance and illusions.
**Base Statistics **Without _heroism_ and _protection from arrows_, the _Pathfinder chronicler_’s statistics are **Fort **+8, **Ref **+11, **Will **+13; **DR **none; **Melee **_quarterstaff_ +9/+4 (1d6–1); **Ranged **_dagger_ +12/+7 (1d4–1/19–20); **Skills **–2 on all skills.

##### Statistics
**Str** 8, **Dex** 14, **Con** 12, **Int** 14, **Wis** 10, **Cha** 24
**Base Atk** +10; **CMB** +9; **CMD** 24
**Feats** _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Enlarge Spell|Enlarge Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Extra Performance|Extra Performance]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (illusion), _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Spell Focus|Spell Focus]]_ (illusion), _[[feats/Widen Spell|Widen Spell]]_
**Skills** Acrobatics +9 (+13 when jumping), Bluff +17, Diplomacy +17, Knowledge (arcana, dungeoneering, geography, history, local, nature, nobility, planes, religion) +15, Linguistics +10, Perception +23, Perform (oratory, string) +17, Profession (scribe) +10, Sense Motive +7, Spellcraft +12, Stealth +14, Survival +10, Use Magic Device +22
**Languages** Common, Draconic, Dwarven, Elf, Gnome, Halfling, _[[monsters/Orc|Orc]]_
**SQ** arcane bond (_[[items/Staff/Staff of Charming|staff of charming]]_), bardic knowledge +3, bloodline arcana (+1 DC for spells augmented by metamagic feats that increase spell level), call down the legends, deep pockets (700 gp), elf blood, improved aid, master scribe, metamagic adept (2/day), new arcana, pathfinding
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), potion of _[[spells/Gaseous Form|gaseous form]]_, _staff of charming_; **Other Gear** +3 _[[items/Armor/Leather armor|leather armor]]_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Boots of Striding and Springing|boots of striding and springing]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Handy Haversack|handy haversack]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, 1,290 gp

These chroniclers travel with intrepid adventurers to record tales of their exploits.