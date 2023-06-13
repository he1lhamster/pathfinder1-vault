---
cssclass: [monsters]
title1: Fey Enchantress
title2: Fey Enchantress
CR: 11
sources:
- name: NPC Codex
  page: 169
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 12800
race: Elf
classes:
- sorcerer 12
alignment: CN
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 21
  touch: 16
  flat_footed: 17
  components:
    armor: 4
    deflection: 2
    dex: 3
    dodge: 1
    natural: 1
HP:
  HP: 56
  long: 12d6+12
saves:
  fort: 5
  ref: 10
  will: 12
  other: +2 vs. enchantments
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk rapier +10/+5 (1d6-1/18-20)
      entries:
      - - damage: 1d6-1
          crit_range: 18-20
      attack: mwk rapier
      bonus:
      - 10
      - 5
  ranged:
  - - text: mwk shortbow +10/+5 (1d6/×3)
      entries:
      - - damage: 1d6
          crit_multiplier: 3
      attack: mwk shortbow
      bonus:
      - 10
      - 5
spell_like_abilities:
  entries:
  - name: laughing touch
    source: default
    freq: 8/day
  - name: fleeting glance
    source: default
    freq: 12 rounds/day
  sources:
  - name: default
    CL: 12
    concentration: 17
spells:
  entries:
  - name: mass suggestion
    source: Sorcerer
    level: 6
    DC: 25
  - name: dominate person
    source: Sorcerer
    level: 5
    DC: 24
  - name: mind fog
    source: Sorcerer
    level: 5
    DC: 24
  - name: tree stride
    source: Sorcerer
    level: 5
  - name: bestow curse
    source: Sorcerer
    level: 4
    DC: 19
  - name: charm monster
    source: Sorcerer
    level: 4
    DC: 21
  - name: crushing despair
    source: Sorcerer
    level: 4
    DC: 23
  - name: poison
    source: Sorcerer
    level: 4
    DC: 19
  - name: deep slumber
    source: Sorcerer
    level: 3
    DC: 22
  - name: fly
    source: Sorcerer
    level: 3
  - name: hold person
    source: Sorcerer
    level: 3
    DC: 22
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 18
  - name: suggestion
    source: Sorcerer
    level: 3
    DC: 22
  - name: false life
    source: Sorcerer
    level: 2
  - name: glitterdust
    source: Sorcerer
    level: 2
    DC: 17
  - name: hideous laughter
    source: Sorcerer
    level: 2
    DC: 21
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: spectral hand
    source: Sorcerer
    level: 2
  - name: touch of idiocy
    source: Sorcerer
    level: 2
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 18
  - name: entangle
    source: Sorcerer
    level: 1
    DC: 16
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: ventriloquism
    source: Sorcerer
    level: 1
    DC: 16
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 19
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 15
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 12
    concentration: 17
    slots:
      6: 3
      5: 6
      4: 7
      3: 7
      2: 7
      1: 8
      0: at-will
    bloodline: fey
tactics:
  Before Combat: The sorcerer casts false life and mage armor.
  During Combat: The sorcerer uses her fleeting glance ability to turn invisible,
    then casts mind fog before using her enchantment spells. She casts spectral hand
    to deliver touch spells such as bestow curse, poison, or touch of idiocy.
  Base Statistics: Without false life and mage armor, the sorcerer's statistics are
    AC 17, touch 16, flat-footed 13; hp 44.
ability_scores:
  STR: 8
  DEX: 16
  CON: 10
  INT: 12
  WIS: 13
  CHA: 20
BAB: 6
CMB: 5
CMD: 21
feats:
- name: Dodge
- name: Eschew Materials
- name: Greater Spell Focus (enchantment)
- name: Improved Iron Will
- name: Iron Will
- name: Lightning Reflexes
- name: Spell Focus (enchantment)
- name: Weapon Finesse
skills:
  Bluff: 18
  Diplomacy: 15
  Fly: 7
  Intimidate: 18
  Knowledge (arcana): 6
  Knowledge (nature): 5
  Perception: 12
  Spellcraft: 9
    to identify magic item properties: 11
languages:
- Common
- Elven
- Sylvan
special_qualities:
- bloodline arcana (+2 DC for compulsion spells)
- elven magic
- weapon familiarity
- woodland stride
gear:
  combat:
  - elixir of love (2)
  - scroll of wall of force
  other:
  - masterwork rapier
  - masterwork shortbow with 20 arrows
  - cloak of resistance +1
  - hat of disguise
  - headband of alluring charisma +2
  - ring of protection +2
  - jewelry (worth 300 gp)
  - 1,825 gp
desc_long: The fey enchantress uses her powers to manipulate others, acquire power,
  and gain wealth.

---

# Fey Enchantress

**Source** NPC Codex pg. 169
**XP** 12,800
Elf _[[classes/Sorcerer|sorcerer]]_ 12

CN Medium humanoid (elf)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +12

##### Defense

**AC** 21, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +2 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural)
**hp** 56 (12d6+12)
**Fort** +5, **Ref** +10, **Will** +12; +2 vs. enchantments
**Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Rapier|rapier]]_ +10/+5 (1d6–1/18–20)
**Ranged** mwk _[[items/Weapon/Shortbow|shortbow]]_ +10/+5 (1d6/×3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +17)
8/day—laughing touch
12 rounds/day—fleeting glance
**_Sorcerer_ Spells Known **(CL 12th; concentration +17)
6th (3/day)—mass _[[spells/Suggestion|suggestion]]_ (DC 25)
5th (6/day)—_[[spells/Dominate Person|dominate person]]_ (DC 24), _[[spells/Mind Fog|mind fog]]_ (DC 24), _[[spells/Tree Stride|tree stride]]_
4th (7/day)—_[[spells/Bestow Curse|bestow curse]]_ (DC 19), _[[spells/Charm Monster|charm monster]]_ (DC 21), _[[spells/Crushing Despair|crushing despair]]_ (DC 23), poison (DC 19)
3rd (7/day)—_[[spells/Deep Slumber|deep slumber]]_ (DC 22), fly, _[[spells/Hold Person|hold person]]_ (DC 22), _[[spells/Lightning Bolt|lightning bolt]]_ (DC 18), _suggestion_ (DC 22)
2nd (7/day)—_[[spells/False Life|false life]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 17), _[[spells/Hideous Laughter|hideous laughter]]_ (DC 21), _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Spectral Hand|spectral hand]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_
1st (8/day)—_[[spells/Charm Person|charm person]]_ (DC 18), _[[spells/Entangle|entangle]]_ (DC 16), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 16)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 19), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_
**Bloodline **fey

### Tactics

**Before Combat **The _sorcerer_ casts _false life_ and _mage armor_.
**During Combat **The _sorcerer_ uses her fleeting glance ability to turn _[[conditions/Invisible|invisible]]_, then casts _mind fog_ before using her enchantment spells. She casts _spectral hand_ to deliver touch spells such as _bestow curse_, poison, or _touch of idiocy_.
**Base Statistics **Without _false life_ and _mage armor_, the _sorcerer_’s statistics are **AC **17, touch 16, _flat-footed_ 13; **hp **44.

##### Statistics
**Str** 8, **Dex** 16, **Con** 10, **Int** 12, **Wis** 13, **Cha** 20
**Base Atk** +6; **CMB** +5; **CMD** 21
**Feats** _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (enchantment), _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment), _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +18, Diplomacy +15, Fly +7, Intimidate +18, Knowledge (arcana) +6, Knowledge (nature) +5, Perception +12, Spellcraft +9 (+11 to _[[spells/Identify|identify]]_ magic item properties)
**Languages** Common, Elven, Sylvan
**SQ** bloodline arcana (+2 DC for compulsion spells), elven magic, weapon familiarity, woodland stride
**Combat Gear** _[[items/Wondrous Item/Elixir of Love|elixir of love]]_ (2), scroll of _[[spells/Wall Of Force|wall of force]]_; **Other Gear** masterwork _rapier_, masterwork _shortbow_ with 20 arrows, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Hat of Disguise|hat of disguise]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, _[[items/Mundane/Jewelry|jewelry]]_ (worth 300 gp), 1,825 gp

The _[[npcs/Fey Enchantress|fey enchantress]]_ uses her powers to manipulate others, acquire power, and gain wealth.