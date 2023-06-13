---
cssclass: [monsters]
title1: Undead Pirate, Draugr Captain
title2: Draugr Captain
CR: 4
sources:
- name: Isles of the Shackles
  page: 62
  link: http://paizo.com/products/btpy8qzx?Pathfinder-Campaign-Setting-Isles-of-the-Shackles
XP: 1200
race: Draugr
classes:
- captain rogue 2 (Pathfinder RPG Bestiary 2 110)
alignment: CE
size: Medium
type: undead
subtypes:
- water
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 20
  touch: 14
  flat_footed: 16
  components:
    armor: 2
    dex: 4
    natural: 4
HP:
  HP: 39
  long: 3d8+2d8+17
  HD: 5
saves:
  fort: 4
  ref: 8
  will: 6
defensive_abilities:
- evasion
DR:
- amount: 5
  weakness: bludgeoning or slashing
immunities:
- undead traits
resistances:
  fire: 10
speeds:
  base: 30
  swim: 30
attacks:
  melee:
  - - text: mwk scimitar +12 (1d6+10/18-20 plus 1 negative level)
      entries:
      - - damage: 1d6+10
          crit_range: 18-20
        - damage: '1'
          type: negative level
      attack: mwk scimitar
      bonus:
      - 12
  - - text: slam +10 (1d10+10 plus 1 negative level)
      entries:
      - - damage: 1d10+10
        - damage: '1'
          type: negative level
      attack: slam
      bonus:
      - 10
  special:
  - sneak attack +1d6
spell_like_abilities:
  entries:
  - name: obscuring mist
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 5
    concentration: 8
ability_scores:
  STR: 25
  DEX: 18
  CON:
  INT: 14
  WIS: 16
  CHA: 17
BAB: 3
CMB: 10
CMD: 24
feats:
- name: Combat Reflexes
- name: Power Attack
- name: Weapon Focus (scimitar)
skills:
  Acrobatics: 12
  Bluff: 9
  Climb: 15
  Intimidate: 11
  Perception: 11
  Profession (sailor): 11
  Stealth: 12
  Swim: 23
languages:
- Common (cannot speak)
special_qualities:
- rogue talents (bleeding attack +1)
- trapfinding +1
ecology:
  environment: any oceans or coastlines
  organization: solitary
  treasure_type: NPC Gear
  treasure:
  - leather armor
  - masterwork scimitar
  - other treasure
desc_long: While most draugr captains were the masters of their ships in life, exceptions
  have been known to exist, particularly among lowly crew drudges who derived the
  most power from their transition to undeath. Such gifted individuals are usually
  seen by their fellow undead crew members as the rightful captains of the ghost ships
  they have come to command.

---

# Undead Pirate, Draugr Captain

**Source** Isles of the Shackles pg. 62
**XP** 1,200
_[[monsters/Draugr|Draugr]]_ captain _[[classes/Rogue|rogue]]_ 2 (Pathfinder RPG Bestiary 2 110)
CE Medium undead (water)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +11

##### Defense

**AC** 20, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+2 armor, +4 Dex, +4 natural)
**hp** 39 (5 HD; 3d8+2d8+17)
**Fort** +4, **Ref** +8, **Will** +6
**Defensive Abilities** evasion; **DR** 5/bludgeoning or slashing; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** fire 10

##### Offense
**Speed** 30 ft., swim 30 ft.
**Melee** mwk _[[items/Weapon/Scimitar|scimitar]]_ +12 (1d6+10/18–20 plus 1 negative level) or slam +10 (1d10+10 plus 1 negative level)
**Special Attacks** sneak attack +1d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +8)
3/day—_[[spells/Obscuring Mist|obscuring mist]]_

##### Statistics
**Str** 25, **Dex** 18, **Con** —, **Int** 14, **Wis** 16, **Cha** 17
**Base Atk** +3; **CMB** +10; **CMD** 24
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scimitar_)
**Skills** Acrobatics +12, Bluff +9, _[[universal monster rules/Climb|Climb]]_ +15, Intimidate +11, Perception +11, Profession (sailor) +11, Stealth +12, Swim +23
**Languages** Common (cannot speak)
**SQ** _rogue_ talents (bleeding attack +1), trapfinding +1

##### Ecology

**Environment** any oceans or coastlines
**Organization** solitary
**Treasure** NPC gear (_[[items/Armor/Leather armor|leather armor]]_, masterwork _scimitar_, other treasure)

##### Description

While most _draugr_ captains were the masters of their ships in life, exceptions have been known to exist, particularly among lowly crew drudges who derived the most power from their transition to undeath. Such gifted individuals are usually seen by their fellow undead crew members as the rightful captains of the _[[monsters/Ghost|ghost]]_ ships they have come to _[[spells/Command|command]]_.