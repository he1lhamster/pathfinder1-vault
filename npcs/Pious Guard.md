---
cssclass: [monsters]
title1: Pious Guard
title2: Pious Guard
CR: 9
sources:
- name: NPC Codex
  page: 117
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 6400
race: Human
classes:
- paladin of Iomedae 10
alignment: LG
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: -1
auras:
- name: courage
  radius: 10
- name: resolve
  radius: 10
AC:
  AC: 22
  touch: 10
  flat_footed: 22
  components:
    armor: 11
    deflection: 1
    dex: -1
    natural: 1
HP:
  HP: 84
  long: 10d10+25
saves:
  fort: 11
  ref: 4
  will: 9
immunities:
- charm
- disease
- fear
- poison
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 ranseur +17/+12 (2d4+8/×3)
      entries:
      - - damage: 2d4+8
          crit_multiplier: 3
      attack: +1 ranseur
      bonus:
      - 17
      - 12
  - - text: mwk longsword +16/+11 (1d8+7/19-20)
      entries:
      - - damage: 1d8+7
          crit_range: 19-20
      attack: mwk longsword
      bonus:
      - 16
      - 11
  special:
  - channel positive energy (DC 17, 5d6)
  - smite evil 4/day (+2 attack and AC, +10 damage)
space: 5
reach: 5
reach_other: 10 ft. with ranseur
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
  sources:
  - name: default
    CL: 10
    concentration: 12
spells:
  entries:
  - name: bull's strength
    source: Paladin
    level: 2
  - name: delay poison
    source: Paladin
    level: 2
  - name: bless
    source: Paladin
    level: 1
  - name: lesser restoration
    source: Paladin
    level: 1
  - name: protection from evil
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 7
    concentration: 9
tactics:
  Before Combat: The paladin casts bull's strength and delay poison.
  During Combat: The paladin disarms foes to capture and question them. The exceptions
    are mindless creatures, evil outsiders, and undead, all of which he destroys on
    the spot.
  Base Statistics: Without bull's strength, the paladin's statistics are Immune charm,
    disease, fear; Melee +1 ranseur +15/+10 (2d4+5/×3) or mwk longsword +14/+9 (1d8+4/19-20);
    Str 16; CMB +13 (+17 disarm); CMD 23 (25 vs. disarm).
ability_scores:
  STR: 20
  DEX: 8
  CON: 14
  INT: 14
  WIS: 10
  CHA: 14
BAB: 10
CMB: 15
CMB_other: +19 disarm
CMD: 25
CMD_other: 27 vs. disarm
feats:
- name: Cleave
- name: Combat Expertise
- name: Greater Disarm
- name: Improved Disarm
- name: Power Attack
- name: Weapon Focus (ranseur)
skills:
  Diplomacy: 10
  Intimidate: 7
  Knowledge (history): 7
  Knowledge (local): 7
  Knowledge (nobility): 10
  Knowledge (religion): 10
  Perception: 10
  Sense Motive: 13
  Spellcraft: 10
languages:
- Common
- Dwarven
- Elven
special_qualities:
- aura
- code of conduct
- divine bond (weapon +2, 2/day)
- lay on hands (5d6, 7/day)
- mercies (cursed, nauseated, shaken)
desc_long: These paladins often serve as guards, or administer justice for judges
  and merchants who perform good works for the god of cities. Often, entire units
  of these paladins are formed to protect holy places in large cities.

---

# Pious Guard

**Source** NPC Codex pg. 117
**XP** 6,400
Human _[[classes/Paladin|paladin]]_ of Iomedae 10

LG Medium humanoid (human)
**Init** –1; **Senses** Perception +10
**Aura** courage (10 ft.), resolve (10 ft.)

##### Defense

**AC** 22, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+11 armor, +1 _[[spells/Deflection|deflection]]_, –1 Dex, +1 natural)
**hp** 84 (10d10+25)
**Fort** +11, **Ref** +4, **Will** +9
**Immune** charm, disease, _[[universal monster rules/Fear|fear]]_, poison

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Ranseur|ranseur]]_ +17/+12 (2d4+8/×3) or mwk _[[items/Weapon/Longsword|longsword]]_ +16/+11 (1d8+7/19–20)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _ranseur_)
**Special Attacks** channel positive energy (DC 17, 5d6), smite evil 4/day (+2 attack and AC, +10 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +12)
At will—_[[spells/Detect Evil|detect evil]]_
**_Paladin_ Spells Prepared **(CL 7th; concentration +9)
2nd—bull’s strength, _[[spells/Delay Poison|delay poison]]_
1st—_[[spells/Bless|bless]]_, lesser _[[spells/Restoration|restoration]]_, _[[spells/Protection From Evil|protection from evil]]_

### Tactics

**Before Combat **The _paladin_ casts bull’s strength and _delay poison_.
**During Combat **The _paladin_ disarms foes to capture and question them. The exceptions are mindless creatures, evil outsiders, and undead, all of which he destroys on the spot.
**Base Statistics **Without bull’s strength, the _paladin_’s statistics are **Immune **charm, disease, _fear_; **Melee** +1 _ranseur_ +15/+10 (2d4+5/×3) or mwk _longsword_ +14/+9 (1d8+4/19–20); **Str **16; **CMB **+13 (+17 disarm); **CMD **23 (25 vs. disarm).

##### Statistics
**Str** 20, **Dex** 8, **Con** 14, **Int** 14, **Wis** 10, **Cha** 14
**Base Atk** +10; **CMB** +15 (+19 disarm); **CMD** 25 (27 vs. disarm)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Greater Disarm|Greater Disarm]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_ranseur_)
**Skills** Diplomacy +10, Intimidate +7, Knowledge (history, local) +7, Knowledge (nobility, religion) +10, Perception +10, Sense Motive +13, Spellcraft +10
**Languages** Common, Dwarven, Elven
**SQ** aura, code of conduct, divine bond (weapon +2, 2/day), lay on hands (5d6, 7/day), mercies (cursed, _[[conditions/Nauseated|nauseated]]_, _[[conditions/Shaken|shaken]]_)

These paladins often serve as guards, or administer justice for judges and merchants who perform good works for the god of cities. Often, entire units of these paladins are formed to protect holy places in large cities.