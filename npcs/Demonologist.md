---
cssclass: [monsters]
title1: Demonologist
title2: Demonologist
CR: 19
sources:
- name: NPC Codex
  page: 227
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 204800
race: Human
classes:
- conjurer 10
- loremaster 10
alignment: CE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 4
senses:
  see invisibility: true
AC:
  AC: 27
  touch: 15
  flat_footed: 27
  components:
    armor: 7
    deflection: 5
    natural: 5
HP:
  HP: 112
  long: 10d6+10d6+40
saves:
  fort: 14
  ref: 13
  will: 21
speeds:
  base: 30
attacks:
  melee:
  - - text: quarterstaff +9/+4 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: quarterstaff
      bonus:
      - 9
      - 4
spell_like_abilities:
  entries:
  - name: dimensional steps
    source: default
    freq: At will
    other: 300 feet/day
  - name: acid dart
    source: default
    freq: 10/day
    other: 1d6+5 acid
  sources:
  - name: default
    CL: 10
    concentration: 17
spells:
  entries:
  - name: dominate monster
    source: Conjurer
    level: 9
    DC: 28
  - name: foresight
    source: Conjurer
    level: 9
  - name: quickened hold monster
    source: Conjurer
    level: 9
    DC: 24
  - name: prismatic wall
    source: Conjurer
    level: 9
  - name: summon monster IX
    source: Conjurer
    level: 9
  - name: maze
    source: Conjurer
    level: 8
    count: 2
  - name: moment of prescience
    source: Conjurer
    level: 8
  - name: summon monster VIII
    source: Conjurer
    level: 8
    count: 2
  - name: banishment
    source: Conjurer
    level: 7
    DC: 24
  - name: quickened displacement
    source: Conjurer
    level: 7
  - name: mass hold person
    source: Conjurer
    level: 7
    DC: 26
  - name: phase door
    source: Conjurer
    level: 7
  - name: plane shift
    source: Conjurer
    level: 7
    DC: 26
  - name: spell turning
    source: Conjurer
    level: 7
  - name: acid fog
    source: Conjurer
    level: 6
  - name: chain lightning
    source: Conjurer
    level: 6
    DC: 23
  - name: forceful hand
    source: Conjurer
    level: 6
  - name: geas/quest
    source: Conjurer
    level: 6
  - name: quickened glitterdust
    source: Conjurer
    level: 6
  - name: mass suggestion
    source: Conjurer
    level: 6
    DC: 25
  - name: cloudkill
    source: Conjurer
    level: 5
    count: 2
    DC: 24
  - name: contact other plane
    source: Conjurer
    level: 5
  - name: sending
    source: Conjurer
    level: 5
  - name: teleport
    source: Conjurer
    level: 5
    count: 2
  - name: confusion
    source: Conjurer
    level: 4
    DC: 23
  - name: dimensional anchor
    source: Conjurer
    level: 4
  - name: fire shield
    source: Conjurer
    level: 4
  - name: greater invisibility
    source: Conjurer
    level: 4
  - name: stoneskin
    source: Conjurer
    level: 4
  - name: summon monster IV
    source: Conjurer
    level: 4
  - name: arcane sight
    source: Conjurer
    level: 3
  - name: dispel magic
    source: Conjurer
    level: 3
    count: 2
  - name: fireball
    source: Conjurer
    level: 3
    DC: 20
  - name: invisibility sphere
    source: Conjurer
    level: 3
  - name: protection from energy
    source: Conjurer
    level: 3
  - name: stinking cloud
    source: Conjurer
    level: 3
    DC: 22
  - name: acid arrow
    source: Conjurer
    level: 2
  - name: detect thoughts
    source: Conjurer
    level: 2
    DC: 19
  - name: invisibility
    source: Conjurer
    level: 2
    count: 2
  - name: scorching ray
    source: Conjurer
    level: 2
  - name: see invisibility
    source: Conjurer
    level: 2
  - name: web
    source: Conjurer
    level: 2
    DC: 21
  - name: alarm
    source: Conjurer
    level: 1
  - name: charm person
    source: Conjurer
    level: 1
    DC: 20
  - name: disguise self
    source: Conjurer
    level: 1
  - name: floating disk
    source: Conjurer
    level: 1
  - name: magic missile
    source: Conjurer
    level: 1
  - name: protection from evil
    source: Conjurer
    level: 1
  - name: unseen servant
    source: Conjurer
    level: 1
  - name: dancing lights
    source: Conjurer
    level: 0
  - name: daze
    source: Conjurer
    level: 0
    DC: 19
  - name: detect magic
    source: Conjurer
    level: 0
  - name: ray of frost
    source: Conjurer
    level: 0
  sources:
  - name: Conjurer
    type: prepared
    CL: 20
    concentration: 27
    slots:
      0: at-will
    opposition_schools:
    - necromancy
    - transmutation
tactics:
  Before Combat: The loremaster casts see invisibility.
  During Combat: The loremaster casts greater invisibility. He summons demons, then
    casts maze, hold monster, and mass suggestion.
ability_scores:
  STR: 8
  DEX: 10
  CON: 12
  INT: 24
  WIS: 14
  CHA: 17
BAB: 10
CMB: 9
CMD: 24
feats:
- name: Augment Summoning
- name: Blind-Fight
- name: Combat Casting
- name: Craft Wondrous Item
- name: Forge Ring
- name: Greater Spell Focus (conjuration)
- name: Greater Spell Focus (enchantment)
- name: Greater Spell Penetration
- name: Improved Initiative
- name: Quicken Spell
- name: Scribe Scroll
- name: Skill Focus (Knowledge [planes])
- name: Spell Focus (conjuration)
- name: Spell Focus (enchantment)
- name: Spell Penetration
- name: Toughness
skills:
  Diplomacy: 13
  Fly: 18
  Intimidate: 23
  Knowledge (arcana): 25
  Knowledge (dungeoneering): 25
  Knowledge (religion): 25
  Knowledge (engineering): 20
  Knowledge (geography): 20
  Knowledge (history): 20
  Knowledge (local): 20
  Knowledge (nature): 20
  Knowledge (nobility): 20
  Knowledge (planes): 41
  Perception: 22
  Sense Motive: 22
  Spellcraft: 30
    to identify magic item properties: 40
  Stealth: 20
  Use Magic Device: 21
languages:
- Abyssal
- Aklo
- Celestial
- Common
- Draconic
- Elven
- Ignan
- Infernal
- Orc
- Undercommon
special_qualities:
- arcane bond (staff of charming)
- greater lore
- lore +5
- secrets (applicable knowledge, lore of true stamina, secret health, secret knowledge
  of avoidance, secrets of inner strength)
- summoner's charm (5 rounds)
- true lore
gear:
  combat:
  - potions of cure serious wounds (3)
  - potion of darkvision
  - scroll of ethereal jaunt
  - scroll of mage's lucubration
  - staff of charming
  other:
  - amulet of natural armor +5
  - bracers of armor +7
  - cloak of resistance +5
  - figurine of wondrous power (ebony fly)
  - portable hole
  - ring of freedom of movement
  - ring of protection +5
  - forked rods
  - diamond dust (worth 500 gp)
  - 3,188 gp
desc_long: Demonologists compel and manipulate their foes, and summon demon minions
  to do their dirty work.

---

# Demonologist

**Source** NPC Codex pg. 227
**XP** 204,800
Human conjurer 10/loremaster 10
CE Medium humanoid (human)
**Init** +4; **Senses** _[[spells/See Invisibility|see invisibility]]_, Perception +22

##### Defense

**AC** 27, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+7 armor, +5 _[[spells/Deflection|deflection]]_, +5 natural)
**hp** 112 (10d6+10d6+40)
**Fort** +14, **Ref** +13, **Will** +21

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Quarterstaff|quarterstaff]]_ +9/+4 (1d6–1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +17)
At will—dimensional steps (300 feet/day)
10/day—acid _[[items/Weapon/Dart|dart]]_ (1d6+5 acid)
**Conjurer Spells Prepared **(CL 20th; concentration +27)
9th—_[[spells/Dominate Monster|dominate monster]]_ (DC 28), _[[spells/Foresight|foresight]]_, quickened _[[spells/Hold Monster|hold monster]]_ (DC 24), _[[spells/Prismatic Wall|prismatic wall]]_, _[[spells/Summon Monster IX|summon monster IX]]_
8th—_[[spells/Maze|maze]]_ (2), _[[spells/Moment of Prescience|moment of prescience]]_, _[[spells/Summon Monster VIII|summon monster VIII]]_ (2)
7th—_[[spells/Banishment|banishment]]_ (DC 24), quickened _[[spells/Displacement|displacement]]_, mass _[[spells/Hold Person|hold person]]_ (DC 26), _[[spells/Phase Door|phase door]]_, _[[spells/Plane Shift|plane shift]]_ (DC 26), _[[spells/Spell Turning|spell turning]]_
6th—_[[spells/Acid Fog|acid fog]]_, _[[spells/Chain Lightning|chain lightning]]_ (DC 23), _[[spells/Forceful Hand|forceful hand]]_, geas/quest, quickened _[[spells/Glitterdust|glitterdust]]_, mass _[[spells/Suggestion|suggestion]]_ (DC 25)
5th—_[[spells/Cloudkill|cloudkill]]_ (2, DC 24), _[[spells/Contact Other Plane|contact other plane]]_, _[[spells/Sending|sending]]_, teleport (2)
4th—_[[spells/Confusion|confusion]]_ (DC 23), _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Fire Shield|fire shield]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Stoneskin|stoneskin]]_, _[[spells/Summon Monster IV|summon monster IV]]_
3rd—_[[spells/Arcane Sight|arcane sight]]_, _[[spells/Dispel Magic|dispel magic]]_ (2), _[[spells/Fireball|fireball]]_ (DC 20), _[[spells/Invisibility Sphere|invisibility sphere]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Stinking Cloud|stinking cloud]]_ (DC 22)
2nd—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 19), _invisibility_ (2), _[[spells/Scorching Ray|scorching ray]]_, _see invisibility_, web (DC 21)
1st—_[[spells/Alarm|alarm]]_, _[[spells/Charm Person|charm person]]_ (DC 20), _[[spells/Disguise Self|disguise self]]_, _[[spells/Floating Disk|floating disk]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Protection From Evil|protection from evil]]_, _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 19), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ray of Frost|ray of frost]]_
**Opposition Schools **necromancy, transmutation

### Tactics

**Before Combat **The loremaster casts _see invisibility_.
**During Combat **The loremaster casts greater _invisibility_. He summons demons, then casts _maze_, _hold monster_, and mass _suggestion_.

##### Statistics
**Str** 8, **Dex** 10, **Con** 12, **Int** 24, **Wis** 14, **Cha** 17
**Base Atk** +10; **CMB** +9; **CMD** 24
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Forge Ring|Forge Ring]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (conjuration, enchantment), _[[feats/Greater Spell Penetration|Greater Spell Penetration]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Skill Focus|Skill Focus]]_ (Knowledge [planes]), _[[feats/Spell Focus|Spell Focus]]_ (conjuration, enchantment), _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Toughness|Toughness]]_
**Skills** Diplomacy +13, Fly +18, Intimidate +23, Knowledge (arcana, dungeoneering, religion) +25, Knowledge (engineering, geography, history, local, nature, nobility) +20, Knowledge (planes) +41, Perception +22, Sense Motive +22, Spellcraft +30 (+40 to _[[spells/Identify|identify]]_ magic item properties), Stealth +20, Use Magic Device +21
**Languages** Abyssal, Aklo, Celestial, Common, Draconic, Elven, Ignan, Infernal, _[[monsters/Orc|Orc]]_, Undercommon
**SQ** arcane bond (_[[items/Staff/Staff of Charming|staff of charming]]_), greater lore, lore +5, secrets (applicable knowledge, lore of true stamina, secret health, secret knowledge of avoidance, secrets of inner strength), _[[classes/Summoner|summoner]]_’s charm (5 rounds), true lore
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (3), potion of _[[spells/Darkvision|darkvision]]_, scroll of _[[spells/Ethereal Jaunt|ethereal jaunt]]_, scroll of mage’s lucubration, _staff of charming_; **Other Gear** _[[items/Wondrous Item/Amulet of Natural Armor +5|amulet of natural armor +5]]_, _[[items/Wondrous Item/Bracers of Armor +7|bracers of armor +7]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +5|cloak of _resistance_ +5]]_, figurine of wondrous power (ebony fly), _[[items/Wondrous Item/Portable Hole|portable hole]]_, _[[items/Ring/Ring of _[[spells/Freedom|Freedom]]_ of Movement|ring of _freedom_ of movement]]_, _[[items/Ring/Ring of Protection +5|ring of protection +5]]_, forked rods, diamond dust (worth 500 gp), 3,188 gp

Demonologists compel and manipulate their foes, and _[[universal monster rules/Summon|summon]]_ demon minions to do their dirty work.