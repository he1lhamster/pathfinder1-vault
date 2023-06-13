---
cssclass: [monsters]
title1: Duergar, Duergar Taskmaster
title2: Duergar Taskmaster
CR: 9
sources:
- name: Monster Codex
  page: 47
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 6400
race: Duergar
classes:
- rogue 6
- shadowdancer 4
alignment: LE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 7
senses:
  darkvision: 150
AC:
  AC: 21
  touch: 15
  flat_footed: 17
  components:
    armor: 5
    deflection: 1
    dex: 3
    dodge: 1
    natural: 1
HP:
  HP: 64
  long: 10d8+16
saves:
  fort: 5
  ref: 11
  will: 7
  other: +2 vs. spells
defensive_abilities:
- evasion
- improved uncanny dodge
- trap sense +2
immunities:
- paralysis
- phantasms
- poison
weaknesses:
- light sensitivity
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 short sword +11/+6 (1d6+2/19-20)
      entries:
      - - damage: 1d6+2
          crit_range: 19-20
      attack: +1 short sword
      bonus:
      - 11
      - 6
  ranged:
  - - text: +1 light slaver's crossbow +11 (1d4+1 nonlethal/19-20 plus entangle)
      entries:
      - - damage: 1d4+1
          type: nonlethal
          crit_range: 19-20
        - effect: entangle
      attack: +1 light slaver's crossbow
      bonus:
      - 11
  special:
  - sneak attack +3d6
spell_like_abilities:
  entries:
  - name: invisibility
    source: default
    freq: 1/day
    other: self only
  - name: ironskin
    source: default
    freq: 1/day
  - name: shadow illusion
    source: shadowdancer
    freq: 2/day
    DC: 8
  - name: shadow call
    source: shadowdancer
    freq: 1/day
    DC: 11
  sources:
  - name: default
    CL: 10
    concentration: 7
  - name: shadowdancer
    CL: 4
    concentration: 1
ability_scores:
  STR: 13
  DEX: 17
  CON: 12
  INT: 12
  WIS: 16
  CHA: 4
BAB: 7
CMB: 8
CMD: 23
CMD_other: 27 vs. bull rush or trip
feats:
- name: Combat Reflexes
- name: Dodge
- name: Exotic Weapon Proficiency (slaver's crossbow)
- name: Improved Initiative
- name: Mobility
- name: Point-Blank Shot
- name: Weapon Finesse
skills:
  Acrobatics: 15
    when jumping: 11
  Climb: 9
  Disable Device: 12
  Escape Artist: 15
  Knowledge (dungeoneering): 10
  Perception: 16
  Perform (dance): 2
  Sense Motive: 16
  Sleight of Hand: 15
  Stealth: 15
  Survival: 4
languages:
- Common
- Dwarven
- Undercommon
special_qualities:
- hide in plain sight
- ironskinned
- rogue talents (combat trick, fast stealth, finesse rogue, stand up)
- shadow jump (40 ft./day)
- slow and steady
- stability
- summon shadow
- trapfinding +3
gear:
  combat:
  - potions of cure moderate wounds (2)
  - tanglefoot bags (2)
  other:
  - +1 chain shirt
  - +1 light slaver's crossbow with 10 bolas bolts
  - +1 short sword
  - amulet of natural armor +1
  - cloak of resistance +1
  - ring of protection +1
  - mwk manacles (2)
  - mwk thieves' tools
  - 720 gp
ecology:
  environment: any underground
desc_long: Duergar rogues primarily capture and discipline slaves.

---

# Duergar, Duergar Taskmaster

**Source** Monster Codex pg. 47
**XP** 6,400
_[[monsters/Duergar|Duergar]]_ _[[classes/Rogue|rogue]]_ 6/shadowdancer 4

LE Medium humanoid (dwarf)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 150 ft.; Perception +16

##### Defense

**AC** 21, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 armor, +1 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural)
**hp** 64 (10d8+16)
**Fort** +5, **Ref** +11, **Will** +7; +2 vs. spells
**Defensive Abilities** evasion, improved uncanny _dodge_, trap sense +2; **Immune** _[[universal monster rules/Paralysis|paralysis]]_, phantasms, poison
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Short sword|short sword]]_ +11/+6 (1d6+2/19–20)
**Ranged** +1 light slaver’s crossbow +11 (1d4+1 nonlethal/19–20 plus _[[spells/Entangle|entangle]]_)
**Special Attacks** sneak attack +3d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +7)
1/day—_[[spells/Invisibility|invisibility]]_ (self only), _[[spells/Ironskin|ironskin]]_
**Shadowdancer _Spell-Like Abilities_** (CL 4th; concentration +1)
2/day—_[[items/Armor Magic Abilities/Shadow|shadow]]_ illusion (DC 8)
1/day—_shadow_ call (DC 11)

##### Statistics
**Str** 13, **Dex** 17, **Con** 12, **Int** 12, **Wis** 16, **Cha** 4
**Base Atk** +7; **CMB** +8; **CMD** 23 (27 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Exotic Weapon Proficiency|Exotic Weapon Proficiency]]_ (slaver’s crossbow), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +15 (+11 when jumping), _[[universal monster rules/Climb|Climb]]_ +9, Disable Device +12, Escape Artist +15, Knowledge (dungeoneering) +10, Perception +16, Perform (dance) +2, Sense Motive +16, Sleight of Hand +15, Stealth +15, Survival +4
**Languages** Common, Dwarven, Undercommon
**SQ** hide in plain sight, ironskinned, _rogue_ talents (combat trick, fast stealth, finesse _rogue_, stand up), _shadow_ _[[spells/Jump|jump]]_ (40 ft./day), _[[spells/Slow|slow]]_ and steady, stability, _[[universal monster rules/Summon|summon]]_ _shadow_, trapfinding +3
**Combat Gear** potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), tanglefoot bags (2); **Other Gear** +1 _[[items/Armor/Chain shirt|chain shirt]]_, +1 light slaver’s crossbow with 10 _[[items/Ammunition/Bolas bolts|bolas bolts]]_, +1 _short sword_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, mwk manacles (2), mwk thieves’ tools, 720 gp

##### Ecology

**Environment** any underground

##### Description

_Duergar_ rogues primarily capture and discipline slaves.