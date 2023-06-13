---
cssclass: [monsters]
title1: Enforcer
title2: Enforcer
CR: 3
sources:
- name: NPC Codex
  page: 246
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 800
race: Human
classes:
- adept 5
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 1
AC:
  AC: 15
  touch: 11
  flat_footed: 14
  components:
    armor: 4
    dex: 1
HP:
  HP: 27
  long: 5d6+10
saves:
  fort: 2
  ref: 5
  will: 7
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk club +7 (1d6+6)
      entries:
      - - damage: 1d6+6
      attack: mwk club
      bonus:
      - 7
  ranged:
  - - text: dagger +3 (1d4+4/19-20)
      entries:
      - - damage: 1d4+4
          crit_range: 19-20
      attack: dagger
      bonus:
      - 3
spells:
  entries:
  - name: bull's strength
    source: Adept
    level: 2
  - name: mirror image
    source: Adept
    level: 2
  - name: cause fear
    source: Adept
    level: 1
    DC: 13
  - name: command
    source: Adept
    level: 1
    DC: 13
  - name: cure light wounds
    source: Adept
    level: 1
  - name: ghost sound
    source: Adept
    level: 0
    DC: 12
  - name: light
    source: Adept
    level: 0
  - name: stabilize
    source: Adept
    level: 0
  sources:
  - name: Adept
    type: prepared
    CL: 5
    concentration: 7
    slots:
      0: at-will
tactics:
  Before Combat: The adept casts bull's strength.
  During Combat: The adept casts mirror image, then attacks with his club. If he has
    trouble landing blows, he switches to his wand of burning hands.
  Base Statistics: Without bull's strength, the adept's statistics are Melee mwk club
    +5 (1d6+3); Ranged dagger +3 (1d4+2/19-20); Str 14; CMB +4; CMD 15.
ability_scores:
  STR: 18
  DEX: 12
  CON: 11
  INT: 9
  WIS: 14
  CHA: 8
BAB: 2
CMB: 6
CMD: 17
feats:
- name: Cleave
- name: Light Armor Proficiency
- name: Power Attack
- name: Toughness
skills:
  Intimidate: 4
  Knowledge (local): 4
  Knowledge (religion): 3
  Perception: 4
languages:
- Common
special_qualities:
- summon familiar (weasel)
gear:
  combat:
  - scroll of cure moderate wounds
  - wand of burning hands (CL 5th, 9 charges)
  - alchemist's fire (3)
  - tanglefoot bag
  other:
  - chain shirt
  - dagger
  - masterwork club
  - cloak of resistance +1
  - belt pouch
  - manacles (2)
  - silver holy symbol
  - spell component pouch
  - 2 gp
desc_long: 'The enforcer uses threats and violence to serve a dual purpose: to intimidate
  enemies of his religion, and to pass judgment on members who believe they can betray
  or desert the holy cause.'

---

# Enforcer

**Source** NPC Codex pg. 246
**XP** 800
Human adept 5

NE Medium humanoid (human)
**Init** +1; **Senses** Perception +4

##### Defense

**AC** 15, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 armor, +1 Dex)
**hp** 27 (5d6+10)
**Fort** +2, **Ref** +5, **Will** +7

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Club|club]]_ +7 (1d6+6)
**Ranged** _[[items/Weapon/Dagger|dagger]]_ +3 (1d4+4/19–20)
**Adept Spells Prepared **(CL 5th; concentration +7)
2nd—bull’s strength, _[[spells/Mirror Image|mirror image]]_
1st—_[[spells/Cause Fear|cause fear]]_ (DC 13), _[[spells/Command|command]]_ (DC 13), _[[spells/Cure Light Wounds|cure light wounds]]_
0 (at will)—_[[spells/Ghost Sound|ghost sound]]_ (DC 12), light, stabilize

### Tactics

**Before Combat **The adept casts bull’s strength.
**During Combat **The adept casts _mirror image_, then attacks with his _club_. If he has trouble landing blows, he switches to his wand of _[[spells/Burning Hands|burning hands]]_.
**Base Statistics **Without bull’s strength, the adept’s statistics are **Melee **mwk _club_ +5 (1d6+3); **Ranged **_dagger_ +3 (1d4+2/19–20); **Str **14; **CMB **+4; **CMD **15.

##### Statistics
**Str** 18, **Dex** 12, **Con** 11, **Int** 9, **Wis** 14, **Cha** 8
**Base Atk** +2; **CMB** +6; **CMD** 17
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Light Armor Proficiency|Light Armor Proficiency]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
**Skills** Intimidate +4, Knowledge (local) +4, Knowledge (religion) +3, Perception +4
**Languages** Common
**SQ** _[[universal monster rules/Summon|summon]]_ familiar (weasel)
**Combat Gear** scroll of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, wand of _burning hands_ (CL 5th, 9 charges), _[[classes/Alchemist|alchemist]]_’s fire (3), _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_; **Other Gear** _[[items/Armor/Chain shirt|chain shirt]]_, _dagger_, masterwork _club_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Mundane/Belt pouch|belt pouch]]_, manacles (2), silver holy symbol, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 2 gp

The _[[feats/Enforcer|enforcer]]_ uses threats and violence to serve a dual purpose: to intimidate enemies of his religion, and to pass judgment on members who believe they can betray or desert the holy cause.