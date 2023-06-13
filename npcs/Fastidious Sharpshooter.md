---
cssclass: [monsters]
title1: Fastidious Sharpshooter
title2: Fastidious Sharpshooter
CR: 7
sources:
- name: NPC Codex
  page: 83
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 3200
race: Gnome
classes:
- fighter 8
alignment: NE
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 23
  touch: 17
  flat_footed: 20
  components:
    armor: 6
    deflection: 3
    dex: 3
    size: 1
HP:
  HP: 76
  long: 8d10+28
saves:
  fort: 9
  ref: 5
  will: 4
  other: +2 vs. illusions, +2 vs. fear
defensive_abilities:
- bravery +2
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 25
attacks:
  melee:
  - - text: mwk glaive +10/+5 (1d8/×3)
      entries:
      - - damage: 1d8
          crit_multiplier: 3
      attack: mwk glaive
      bonus:
      - 10
      - 5
  - - text: short sword +9/+4 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: short sword
      bonus:
      - 9
      - 4
  ranged:
  - - text: mwk light crossbow +13/+13/+8 (1d6+3/17-20)
      entries:
      - - damage: 1d6+3
          crit_range: 17-20
      attack: mwk light crossbow
      bonus:
      - 13
      - 13
      - 8
  - - text: mwk light crossbow with +1 frost bolts +13/+13/+8 (1d6+4+1d6 cold/17-20)
      entries:
      - - damage: 1d6+4+1d6
          type: cold
          crit_range: 17-20
      attack: mwk light crossbow with +1 frost bolts
      bonus:
      - 13
      - 13
      - 8
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - weapon training (crossbows +1)
space: 5
reach: 5
reach_other: 10 ft. with glaive
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: ghost sound
    source: default
    freq: 1/day
    DC: 11
  - name: prestidigitation
    source: default
    freq: 1/day
  - name: speak with animals
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 8
    concentration: 9
tactics:
  Before Combat: The fighter drinks her potion of shield of faith.
  During Combat: The fighter drinks her potion of haste and launches full attacks
    with screaming bolts.
  Base Statistics: Without shield of faith, the fighter's statistics are AC 20, touch
    14, flat-footed 17; CMD 20.
ability_scores:
  STR: 10
  DEX: 16
  CON: 16
  INT: 8
  WIS: 14
  CHA: 12
BAB: 8
CMB: 7
CMD: 23
feats:
- name: Deadly Aim
- name: Fleet
- name: Improved Critical (light crossbow)
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Reload
- name: Rapid Shot
- name: Weapon Focus (light crossbow)
- name: Weapon Specialization (light crossbow)
skills:
  Perception: 10
  Profession (soldier): 8
  Sense Motive: 7
languages:
- Common
- Gnome
- Sylvan
special_qualities:
- armor training 2
gear:
  combat:
  - +1 frost bolts (8)
  - potion of haste
  - potion of shield of faith (CL 7th)
  - screaming bolts (2)
  other:
  - mithral breastplate
  - masterwork glaive
  - masterwork light crossbow with 40 bolts
  - short sword
  - sunrods (2)
  - 27 gp
desc_long: There is no description for this NPC.

---

# Fastidious Sharpshooter

**Source** NPC Codex pg. 83
**XP** 3,200
Gnome _[[classes/Fighter|fighter]]_ 8

NE Small humanoid (gnome)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +10

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+6 armor, +3 deflection, +3 Dex, +1 size)
**hp** 76 (8d10+28)
**Fort** +9, **Ref** +5, **Will** +4; +2 vs. illusions, +2 vs. _[[universal monster rules/Fear|fear]]_
**Defensive Abilities** bravery +2, defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants)

##### Offense
**Speed** 25 ft.
**Melee** mwk _[[items/Weapon/Glaive|glaive]]_ +10/+5 (1d8/×3) or _[[items/Weapon/Short sword|short sword]]_ +9/+4 (1d4/19–20)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +13/+13/+8 (1d6+3/17–20) or mwk _light crossbow_ with +1 frost bolts +13/+13/+8 (1d6+4+1d6 cold/17–20)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _glaive_)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, weapon _training_ (crossbows +1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +9)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 11), _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_

### Tactics

**Before Combat **The _fighter_ drinks her potion of _[[spells/Shield Of Faith|shield of faith]]_.
**During Combat **The _fighter_ drinks her potion of _[[spells/Haste|haste]]_ and launches full attacks with screaming bolts.
**Base Statistics **Without _shield of faith_, the _fighter_’s statistics are **AC **20, touch 14, _flat-footed_ 17; **CMD **20.

##### Statistics
**Str** 10, **Dex** 16, **Con** 16, **Int** 8, **Wis** 14, **Cha** 12
**Base Atk** +8; **CMB** +7; **CMD** 23
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _[[feats/Fleet|Fleet]]_, _[[feats/Improved Critical|Improved Critical]]_ (_light crossbow_), _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Reload|Rapid Reload]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_light crossbow_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_light crossbow_)
**Skills** Perception +10, Profession (soldier) +8, Sense Motive +7
**Languages** Common, Gnome, Sylvan
**SQ** armor _training_ 2
**Combat Gear** +1 frost bolts (8), potion of _haste_, potion of _shield of faith_ (CL 7th), screaming bolts (2); **Other Gear** mithral _[[items/Armor/Breastplate|breastplate]]_, masterwork _glaive_, masterwork _light crossbow_ with 40 bolts, _short sword_, sunrods (2), 27 gp

There is no description for this NPC.