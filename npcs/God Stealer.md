---
cssclass: [monsters]
title1: God Stealer
title2: God Stealer
CR: 19
sources:
- name: NPC Codex
  page: 207
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 204800
race: Elf
classes:
- rogue 3
- enchanter 7
- arcane trickster 10
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 8
senses:
  low-light vision: true
AC:
  AC: 23
  touch: 17
  flat_footed: 19
  components:
    armor: 5
    deflection: 3
    dex: 4
    natural: 1
HP:
  HP: 163
  long: 3d8+7d6+10d6+87
saves:
  fort: 13
  ref: 19
  will: 16
  other: +2 vs. enchantments
defensive_abilities:
- evasion
- trap sense +1
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 unholy rapier +15/+10 (1d6/18-20)
      entries:
      - - damage: 1d6
          crit_range: 18-20
      attack: +1 unholy rapier
      bonus:
      - 15
      - 10
  ranged:
  - - text: ray +15 (by spell)
      entries:
      - - effect: by spell
      attack: ray
      bonus:
      - 15
  special:
  - impromptu sneak attack 2/day
  - sneak attack +7d6
  - surprise spells
spell_like_abilities:
  entries:
  - name: dazing touch
    source: default
    freq: 11/day
  sources:
  - name: default
    CL: 17
    concentration: 25
spells:
  entries:
  - name: dominate monster
    source: Enchanter
    level: 9
    DC: 29
  - name: energy drain
    source: Enchanter
    level: 9
    DC: 27
  - name: irresistible dance
    source: Enchanter
    level: 8
    DC: 28
  - name: mass charm monster
    source: Enchanter
    level: 8
    DC: 28
  - name: polar ray
    source: Enchanter
    level: 8
  - name: power word stun
    source: Enchanter
    level: 8
  - name: insanity
    source: Enchanter
    level: 7
    DC: 27
  - name: mass hold person
    source: Enchanter
    level: 7
    DC: 27
  - name: phase door
    source: Enchanter
    level: 7
  - name: power word blind
    source: Enchanter
    level: 7
  - name: project image
    source: Enchanter
    level: 7
    DC: 25
  - name: acid fog
    source: Enchanter
    level: 6
  - name: chain lightning
    source: Enchanter
    level: 6
    DC: 24
  - name: circle of death
    source: Enchanter
    level: 6
    DC: 24
  - name: disintegrate
    source: Enchanter
    level: 6
    DC: 24
  - name: eyebite
    source: Enchanter
    level: 6
    DC: 24
  - name: mass suggestion
    source: Enchanter
    level: 6
    DC: 26
  - name: cloudkill
    source: Enchanter
    level: 5
    DC: 23
  - name: dominate person
    source: Enchanter
    level: 5
    DC: 25
  - name: feeblemind
    source: Enchanter
    level: 5
    DC: 25
  - name: hold monster
    source: Enchanter
    level: 5
    DC: 25
  - name: mind fog
    source: Enchanter
    level: 5
    DC: 25
  - name: teleport
    source: Enchanter
    level: 5
  - name: charm monster
    source: Enchanter
    level: 4
    DC: 24
  - name: confusion
    source: Enchanter
    level: 4
    DC: 24
  - name: crushing despair
    source: Enchanter
    level: 4
    DC: 24
  - name: dimension door
    source: Enchanter
    level: 4
  - name: enervation
    source: Enchanter
    level: 4
  - name: stoneskin
    source: Enchanter
    level: 4
  - name: deep slumber
    source: Enchanter
    level: 3
    DC: 23
  - name: dispel magic
    source: Enchanter
    level: 3
  - name: displacement
    source: Enchanter
    level: 3
  - name: fireball
    source: Enchanter
    level: 3
    DC: 21
  - name: hold person
    source: Enchanter
    level: 3
    DC: 23
  - name: ray of exhaustion
    source: Enchanter
    level: 3
    DC: 21
  - name: suggestion
    source: Enchanter
    level: 3
    DC: 23
  - name: glitterdust
    source: Enchanter
    level: 2
    DC: 20
  - name: hideous laughter
    source: Enchanter
    level: 2
    DC: 22
  - name: invisibility
    source: Enchanter
    level: 2
  - name: protection from arrows
    source: Enchanter
    level: 2
  - name: resist energy
    source: Enchanter
    level: 2
    DC: 20
  - name: scorching ray
    source: Enchanter
    level: 2
  - name: touch of idiocy
    source: Enchanter
    level: 2
  - name: alarm
    source: Enchanter
    level: 1
  - name: burning hands
    source: Enchanter
    level: 1
    DC: 19
  - name: charm person
    source: Enchanter
    level: 1
    DC: 21
  - name: disguise self
    source: Enchanter
    level: 1
  - name: magic missile
    source: Enchanter
    level: 1
    count: 2
  - name: unseen servant
    source: Enchanter
    level: 1
  - name: detect magic
    source: Enchanter
    level: 0
  - name: light
    source: Enchanter
    level: 0
  - name: mage hand
    source: Enchanter
    level: 0
  - name: read magic
    source: Enchanter
    level: 0
  sources:
  - name: Enchanter
    type: prepared
    CL: 17
    concentration: 25
    slots:
      0: at-will
    opposition_schools:
    - divination
    - transmutation
tactics:
  Before Combat: The arcane trickster casts stoneskin.
  During Combat: The arcane trickster begins combat by casting dominate monster, mass
    hold person, and similar enchantment spells before casting destructive spells
    augmented by surprise spell.
  Base Statistics: Without stoneskin, the arcane trickster's statistics are DR none.
ability_scores:
  STR: 8
  DEX: 18
  CON: 18
  INT: 26
  WIS: 10
  CHA: 13
BAB: 10
CMB: 9
CMD: 26
feats:
- name: Combat Casting
- name: Empower Spell
- name: Greater Spell Focus (enchantment)
- name: Heighten Spell
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Lightning Reflexes
- name: Point-Blank Shot
- name: Scribe Scroll
- name: Spell Focus (enchantment)
- name: Weapon Finesse
- name: Weapon Focus (ray)
skills:
  Acrobatics: 27
  Bluff: 14
  Climb: 7
  Disable Device: 27
  Escape Artist: 27
  Fly: 10
  Intimidate: 14
  Knowledge (arcana): 16
  Knowledge (dungeoneering): 16
  Knowledge (engineering): 16
  Knowledge (history): 16
  Knowledge (local): 16
  Knowledge (religion): 21
  Perception: 25
  Sense Motive: 8
  Sleight of Hand: 27
  Spellcraft: 21
    to identify magic item properties: 23
  Stealth: 27
  Survival: 10
  Swim: 12
  Use Magic Device: 24
languages:
- Abyssal
- Celestial
- Common
- Dwarven
- Elf
- Giant
- Goblin
- Ignan
- Infernal
special_qualities:
- arcane bond (+1 unholy longsword)
- elven magic
- enchanting smile
- invisible thief (10 rounds/day)
- ranged legerdemain
- rogue talents (finesse rogue)
- trapfinding +1
- tricky spell 5/day
- weapon familiarity
gear:
  combat:
  - potions of cure serious wounds (2)
  - wand of lightning bolt (15 charges)
  other:
  - +1 unholy rapier
  - amulet of natural armor +1
  - bag of holding (type II)
  - belt of physical might +4 (Dex, Con)
  - bracers of armor +5
  - cloak of resistance +3
  - headband of vast intelligence +6
  - ring of protection +3
  - 805 gp
desc_long: Often serving the priesthood of vile cults, these tricksters steal from
  powerful good temples.

---

# God Stealer

**Source** NPC Codex pg. 207
**XP** 204,800
Elf _[[classes/Rogue|rogue]]_ 3/enchanter 7/arcane trickster 10

NE Medium humanoid (elf)
**Init** +8; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +25

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+5 armor, +3 _[[spells/Deflection|deflection]]_, +4 Dex, +1 natural)
**hp** 163 (3d8+7d6+10d6+87)
**Fort** +13, **Ref** +19, **Will** +16; +2 vs. enchantments
**Defensive Abilities** evasion, trap sense +1; **DR** 10/adamantine (150 points); **Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Rapier|rapier]]_ +15/+10 (1d6/18–20)
**Ranged** ray +15 (by spell)
**Special Attacks** impromptu sneak attack 2/day, sneak attack +7d6, surprise spells
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +25)
11/day—dazing touch
**Enchanter Spells Prepared **(CL 17th; concentration +25)
9th—_[[spells/Dominate Monster|dominate monster]]_ (DC 29), _[[universal monster rules/Energy Drain|energy drain]]_ (DC 27)
8th—_[[spells/Irresistible Dance|irresistible dance]]_ (DC 28), mass _[[spells/Charm Monster|charm monster]]_ (DC 28), _[[spells/Polar Ray|polar ray]]_, _[[spells/Power Word Stun|power word stun]]_
7th—_[[spells/Insanity|insanity]]_ (DC 27), mass _[[spells/Hold Person|hold person]]_ (DC 27), _[[spells/Phase Door|phase door]]_, _[[spells/Power Word Blind|power word blind]]_, _[[spells/Project Image|project image]]_ (DC 25)
6th—_[[spells/Acid Fog|acid fog]]_, _[[spells/Chain Lightning|chain lightning]]_ (DC 24), _[[spells/Circle Of Death|circle of death]]_ (DC 24), _[[spells/Disintegrate|disintegrate]]_ (DC 24), _[[spells/Eyebite|eyebite]]_ (DC 24), mass _[[spells/Suggestion|suggestion]]_ (DC 26)
5th—_[[spells/Cloudkill|cloudkill]]_ (DC 23), _[[spells/Dominate Person|dominate person]]_ (DC 25), _[[spells/Feeblemind|feeblemind]]_ (DC 25), _[[spells/Hold Monster|hold monster]]_ (DC 25), _[[spells/Mind Fog|mind fog]]_ (DC 25), teleport
4th—_charm monster_ (DC 24), _[[spells/Confusion|confusion]]_ (DC 24), _[[spells/Crushing Despair|crushing despair]]_ (DC 24), _[[spells/Dimension Door|dimension door]]_, _[[spells/Enervation|enervation]]_, _[[spells/Stoneskin|stoneskin]]_
3rd—_[[spells/Deep Slumber|deep slumber]]_ (DC 23), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Displacement|displacement]]_, _[[spells/Fireball|fireball]]_ (DC 21), _hold person_ (DC 23), _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 21), _suggestion_ (DC 23)
2nd—_[[spells/Glitterdust|glitterdust]]_ (DC 20), _[[spells/Hideous Laughter|hideous laughter]]_ (DC 22), _[[spells/Invisibility|invisibility]]_, _[[spells/Protection From Arrows|protection from arrows]]_, _[[spells/Resist Energy|resist energy]]_ (DC 20), _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_
1st—_[[spells/Alarm|alarm]]_, _[[spells/Burning Hands|burning hands]]_ (DC 19), _[[spells/Charm Person|charm person]]_ (DC 21), _[[spells/Disguise Self|disguise self]]_, _[[spells/Magic Missile|magic missile]]_ (2), _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_
**Opposition Schools **_[[spells/Divination|divination]]_, transmutation

### Tactics

**Before Combat **The arcane trickster casts _stoneskin_.
**During Combat **The arcane trickster begins combat by casting _dominate monster_, mass _hold person_, and similar enchantment spells before casting destructive spells augmented by surprise spell.
**Base Statistics **Without _stoneskin_, the arcane trickster’s statistics are **DR **none.

##### Statistics
**Str** 8, **Dex** 18, **Con** 18, **Int** 26, **Wis** 10, **Cha** 13
**Base Atk** +10; **CMB** +9; **CMD** 26
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (enchantment), _[[feats/Heighten Spell|Heighten Spell]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment), _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (ray)
**Skills** Acrobatics +27, Bluff +14, _[[universal monster rules/Climb|Climb]]_ +7, Disable Device +27, Escape Artist +27, Fly +10, Intimidate +14, Knowledge (arcana, dungeoneering, engineering, history, local) +16, Knowledge (religion) +21, Perception +25, Sense Motive +8, Sleight of Hand +27, Spellcraft +21 (+23 to _[[spells/Identify|identify]]_ magic item properties), Stealth +27, Survival +10, Swim +12, Use Magic Device +24
**Languages** Abyssal, Celestial, Common, Dwarven, Elf, Giant, _[[monsters/Goblin|Goblin]]_, Ignan, Infernal
**SQ** arcane bond (+1 _unholy_ _[[items/Weapon/Longsword|longsword]]_), elven magic, enchanting smile, _[[conditions/Invisible|invisible]]_ thief (10 rounds/day), ranged legerdemain, _rogue_ talents (finesse _rogue_), trapfinding +1, tricky spell 5/day, weapon familiarity
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), wand of _[[spells/Lightning Bolt|lightning bolt]]_ (15 charges); **Other Gear** +1 _unholy_ _rapier_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, bag of holding (type II), _[[items/Wondrous Item/Belt of Physical Might +4|belt of physical might +4]]_ (Dex, Con), _[[items/Wondrous Item/Bracers of Armor +5|bracers of armor +5]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +6|headband of vast intelligence +6]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, 805 gp

Often serving the priesthood of vile cults, these tricksters steal from powerful good temples.