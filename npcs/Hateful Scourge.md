---
cssclass: [monsters]
title1: Hateful Scourge
title2: Hateful Scourge
CR: 16
sources:
- name: NPC Codex
  page: 76
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Half-elf
classes:
- druid 17
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 1
senses:
  low-light vision: true
AC:
  AC: 28
  touch: 14
  flat_footed: 27
  components:
    armor: 10
    deflection: 2
    dex: 1
    insight: 1
    shield: 4
HP:
  HP: 158
  long: 17d8+78
saves:
  fort: 16
  ref: 9
  will: 20
  other: +2 vs. enchantments, +4 vs. fey and plant-targeted effects
immunities:
- poison
speeds:
  base: 20
attacks:
  melee:
  - - text: 1 club +15/+10/+5 (1d6+3)
      entries:
      - - damage: 1d6+3
      count: 1
      attack: club
      bonus:
      - 15
      - 10
      - 5
  ranged:
  - - text: mwk shortspear +14/+9/+4 (1d6+2)
      entries:
      - - damage: 1d6+2
      attack: mwk shortspear
      bonus:
      - 14
      - 9
      - 4
  special:
  - wild shape 7/day
spell_like_abilities:
  entries:
  - name: lightning lord
    source: default
    freq: 17/day
  - name: storm burst
    source: default
    freq: 10/day
  sources:
  - name: default
    CL: 17
    concentration: 24
spells:
  entries:
  - name: empowered fire storm
    source: Druid
    level: 9
    DC: 24
  - is_domain_spell: true
    name: storm of vengeance
    source: Druid
    level: 9
    DC: 26
  - name: earthquake
    source: Druid
    level: 8
  - is_domain_spell: true
    name: whirlwind
    source: Druid
    level: 8
    DC: 25
  - name: word of recall
    source: Druid
    level: 8
  - is_domain_spell: true
    name: control weather
    source: Druid
    level: 7
  - name: creeping doom
    source: Druid
    level: 7
    DC: 24
  - name: fire storm
    source: Druid
    level: 7
    DC: 24
  - name: heal
    source: Druid
    level: 7
  - name: true seeing
    source: Druid
    level: 7
  - name: antilife shell
    source: Druid
    level: 6
  - is_domain_spell: true
    name: control winds
    source: Druid
    level: 6
    DC: 23
  - name: empowered flame strike
    source: Druid
    level: 6
    count: 2
    DC: 21
  - name: greater dispel magic
    source: Druid
    level: 6
  - name: wall of stone
    source: Druid
    level: 6
  - name: baleful polymorph
    source: Druid
    level: 5
    DC: 22
  - name: call lightning storm
    source: Druid
    level: 5
    DC: 22
  - name: cure critical wounds
    source: Druid
    level: 5
    count: 2
  - is_domain_spell: true
    name: ice storm
    source: Druid
    level: 5
  - name: insect plague
    source: Druid
    level: 5
  - name: control water
    source: Druid
    level: 4
  - name: dispel magic
    source: Druid
    level: 4
  - name: flame strike
    source: Druid
    level: 4
    count: 2
    DC: 21
  - name: freedom of movement
    source: Druid
    level: 4
  - is_domain_spell: true
    name: sleet storm
    source: Druid
    level: 4
  - is_domain_spell: true
    name: call lightning
    source: Druid
    level: 3
    DC: 20
  - name: dominate animal
    source: Druid
    level: 3
    DC: 20
  - name: greater magic fang
    source: Druid
    level: 3
    count: 3
  - name: protection from energy
    source: Druid
    level: 3
    count: 2
  - name: barkskin
    source: Druid
    level: 2
    count: 3
  - name: bull's strength
    source: Druid
    level: 2
    count: 2
  - name: cat's grace
    source: Druid
    level: 2
  - is_domain_spell: true
    name: fog cloud
    source: Druid
    level: 2
  - name: entangle
    source: Druid
    level: 1
    count: 2
    DC: 18
  - name: faerie fire
    source: Druid
    level: 1
    count: 2
  - is_domain_spell: true
    name: obscuring mist
    source: Druid
    level: 1
  - name: shillelagh
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: flare
    source: Druid
    level: 0
    DC: 17
  - name: light
    source: Druid
    level: 0
  - name: purify food and drink
    source: Druid
    level: 0
  - name: resistance
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 17
    concentration: 24
    slots:
      0: at-will
    domains:
    - weather
tactics:
  Before Combat: The druid casts shambler once per week, and liveoak and ironwood
    every 17 days.
  During Combat: The druid sends her shambling mounds and treant to fight while she
    casts storm of vengeance. If physically threatened, the druid casts antilife shell,
    followed by empowered fire storm.
ability_scores:
  STR: 14
  DEX: 12
  CON: 16
  INT: 8
  WIS: 24
  CHA: 10
BAB: 12
CMB: 14
CMB_other: +16 sunder
CMD: 28
CMD_other: 30 vs. sunder
feats:
- name: Combat Casting
- name: Empower Spell
- name: Heavy Armor Proficiency
- name: Improved Sunder
- name: Improved Vital Strike
- name: Natural Spell
- name: Power Attack
- name: Skill Focus (Survival)
- name: Toughness
- name: Vital Strike
skills:
  Fly: 3
  Handle Animal: 6
  Knowledge (geography): 8
  Knowledge (nature): 12
  Linguistics: 3
  Perception: 25
  Perform (sing): 4
  Ride: 2
  Spellcraft: 8
  Survival: 21
  Swim: 3
languages:
- Aquan
- Auran
- Common
- Druidic
- Elven
- Ignan
- Terran
special_qualities:
- a thousand faces
- elf blood
- nature bond (Weather domain)
- nature sense
- timeless body
- trackless step
- wild empathy +17
- woodland stride
gear:
  combat:
  - potions of haste (2)
  other:
  - +1 ironwood wild full plate
  - +2 darkwood heavy wooden shield
  - +1 club
  - masterwork shortspears (3)
  - belt of mighty constitution +2
  - cloak of resistance +3
  - druid's vestments
  - dusty rose prism ioun stone
  - eyes of the eagle
  - headband of inspired wisdom +4
  - ring of protection +2
  - holly and mistletoe
  - spell component pouch
  - waterskin
  - 134 gp
desc_long: These powerful druids see civilization as a pestilence.

---

# Hateful Scourge

**Source** NPC Codex pg. 76
**XP** 76,800
Half-elf _[[classes/Druid|druid]]_ 17

NE Medium humanoid (elf, human)
**Init** +1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +25

##### Defense

**AC** 28, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+10 armor, +2 _[[spells/Deflection|deflection]]_, +1 Dex, +1 insight, +4 _[[spells/Shield|shield]]_)
**hp** 158 (17d8+78)
**Fort** +16, **Ref** +9, **Will** +20; +2 vs. enchantments, +4 vs. fey and plant-targeted effects
**Immune** poison

##### Offense
**Speed** 20 ft.
**Melee** 1 _[[items/Weapon/Club|club]]_ +15/+10/+5 (1d6+3)
**Ranged** mwk _[[items/Weapon/Shortspear|shortspear]]_ +14/+9/+4 (1d6+2)
**Special Attacks** wild shape 7/day
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +24)
17/day—lightning lord
10/day—storm burst
**_Druid_ Spells Prepared **(CL 17th; concentration +24)
9th—empowered _[[spells/Fire Storm|fire storm]]_ (DC 24), storm of vengeanceD (DC 26)
8th—_[[spells/Earthquake|earthquake]]_, whirlwindD (DC 25), _[[spells/Word of Recall|word of recall]]_
7th—_[[spells/Control Weather|control weather]]_, _[[spells/Creeping Doom|creeping doom]]_ (DC 24), _fire storm_ (DC 24), _[[spells/Heal|heal]]_, _[[spells/True Seeing|true seeing]]_
6th—_[[spells/Antilife Shell|antilife shell]]_, control windsD (DC 23), empowered _[[spells/Flame Strike|flame strike]]_ (2, DC 21), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Wall Of Stone|wall of stone]]_
5th—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 22), _[[spells/Call Lightning Storm|call lightning storm]]_ (DC 22), _[[spells/Cure Critical Wounds|cure critical wounds]]_ (2), _[[spells/Ice Storm|ice storm]]_, _[[spells/Insect Plague|insect plague]]_
4th—_[[spells/Control Water|control water]]_, _dispel magic_, _flame strike_ (2, DC 21), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Sleet Storm|sleet storm]]_
3rd—call lightningD (DC 20), _[[spells/Dominate Animal|dominate animal]]_ (DC 20), greater _[[spells/Magic Fang|magic fang]]_ (3), _[[spells/Protection from Energy|protection from energy]]_ (2)
2nd—_[[spells/Barkskin|barkskin]]_ (3), bull’s strength (2), cat’s _[[spells/Grace|grace]]_, _[[spells/Fog Cloud|fog cloud]]_
1st—_[[spells/Entangle|entangle]]_ (2, DC 18), _[[spells/Faerie Fire|faerie fire]]_ (2), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shillelagh|shillelagh]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)—_[[spells/Flare|flare]]_ (DC 17), light, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[universal monster rules/Resistance|resistance]]_
**D **Domain spell; **Domain **Weather

### Tactics

**Before Combat **The _druid_ casts _[[spells/Shambler|shambler]]_ once per week, and _[[spells/Liveoak|liveoak]]_ and _[[spells/Ironwood|ironwood]]_ every 17 days.
**During Combat **The _druid_ sends her shambling mounds and _[[monsters/Treant|treant]]_ to fight while she casts _[[spells/Storm Of Vengeance|storm of vengeance]]_. If physically threatened, the _druid_ casts _antilife shell_, followed by empowered _fire storm_.

##### Statistics
**Str** 14, **Dex** 12, **Con** 16, **Int** 8, **Wis** 24, **Cha** 10
**Base Atk** +12; **CMB** +14 (+16 sunder); **CMD** 28 (30 vs. sunder)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Heavy Armor Proficiency|Heavy Armor Proficiency]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Survival), _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +3, Handle Animal +6, Knowledge (geography) +8, Knowledge (nature) +12, Linguistics +3, Perception +25, Perform (sing) +4, Ride +2, Spellcraft +8, Survival +21, Swim +3
**Languages** Aquan, Auran, Common, Druidic, Elven, Ignan, Terran
**SQ** a thousand faces, elf blood, nature bond (Weather domain), nature sense, timeless body, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, wild _[[feats/Empathy|empathy]]_ +17, woodland stride
**Combat Gear** potions of _[[spells/Haste|haste]]_ (2); **Other Gear** +1 _ironwood_ wild _[[items/Armor/Full plate|full plate]]_, +2 darkwood _[[items/Shield/Heavy wooden shield|heavy wooden shield]]_, +1 _club_, masterwork shortspears (3), _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +3|cloak of _resistance_ +3]]_, _druid_’s vestments, _[[items/Wondrous Item/Dusty Rose Prism Ioun Stone|dusty rose prism ioun stone]]_, _[[items/Wondrous Item/Eyes of the Eagle|eyes of the eagle]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, _[[items/Mundane/Waterskin|waterskin]]_, 134 gp

These powerful druids see civilization as a pestilence.