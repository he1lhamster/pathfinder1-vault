---
cssclass: [monsters]
title1: Shaman
title2: Shaman
CR: 1/2
sources:
- name: NPC Codex
  page: 244
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 200
race: Half-orc
classes:
- adept 2
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: -1
senses:
  darkvision: 60
AC:
  AC: 11
  touch: 9
  flat_footed: 11
  components:
    armor: 2
    dex: -1
HP:
  HP: 11
  long: 2d6+4
saves:
  fort: 1
  ref: 1
  will: 5
defensive_abilities:
- orc ferocity
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +0 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 0
  ranged:
  - - text: dart +0 (1d4-1)
      entries:
      - - damage: 1d4-1
      attack: dart
      bonus:
      - 0
spells:
  entries:
  - name: burning hands
    source: Adept
    level: 1
    DC: 13
  - name: sleep
    source: Adept
    level: 1
    DC: 13
  - name: ghost sound
    source: Adept
    level: 0
    DC: 12
  - name: read magic
    source: Adept
    level: 0
  - name: touch of fatigue
    source: Adept
    level: 0
    DC: 12
  sources:
  - name: Adept
    type: prepared
    CL: 2
    concentration: 4
    slots:
      0: at-will
tactics:
  During Combat: If fighting foes that lack darkvision, the adept reads his scroll
    of darkness. He looks for groups to target with burning hands or sleep, resorting
    to darts or alchemist's fire otherwise.
ability_scores:
  STR: 9
  DEX: 8
  CON: 12
  INT: 10
  WIS: 15
  CHA: 11
BAB: 1
CMB: 0
CMD: 9
feats:
- name: Combat Casting
skills:
  Heal: 9
  Intimidate: 2
  Knowledge (religion): 5
  Perception: 2
languages:
- Common
- Orc
special_qualities:
- orc blood
- summon familiar (weasel)
- weapon familiarity
gear:
  combat:
  - scroll of bless
  - scrolls of cure light wounds (2)
  - scroll of darkness
  - scroll of protection from good
  - alchemist's fire (2)
  other:
  - leather armor
  - dagger
  - darts (10)
  - healer's kit
  - smokestick
  - spell component pouch
  - tindertwig
  - unholy symbol (bone-and-tooth necklace worth 5 gp)
  - 2 gp
desc_long: |-
  A shaman serves a small tribe as a visionary and source of wisdom-the sole authority on supernatural matters, and the only one who can communicate with the worlds beyond. His familiar may be a representation of his spirit animal or a spy who allows him to learn more about other tribesfolk and appear wiser than he is.

  This stat block can also be used as a lesser adept apprenticed to an initiate (adept 3), doom prophet (adept 4), or guru (adept 6).

---

# Shaman

**Source** NPC Codex pg. 244
**XP** 200
Half-orc adept 2

NE Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** –1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +2

##### Defense

**AC** 11, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+2 armor, –1 Dex)
**hp** 11 (2d6+4)
**Fort** +1, **Ref** +1, **Will** +5
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +0 (1d4–1/19–20)
**Ranged** _[[items/Weapon/Dart|dart]]_ +0 (1d4–1)
**Adept Spells Prepared **(CL 2nd; concentration +4)
1st—_[[spells/Burning Hands|burning hands]]_ (DC 13), sleep (DC 13)
0 (at will)—_[[spells/Ghost Sound|ghost sound]]_ (DC 12), _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 12)

### Tactics

**During Combat **If fighting foes that lack _darkvision_, the adept reads his scroll of _[[spells/Darkness|darkness]]_. He looks for groups to target with _burning hands_ or sleep, resorting to darts or _[[classes/Alchemist|alchemist]]_’s fire otherwise.

##### Statistics
**Str** 9, **Dex** 8, **Con** 12, **Int** 10, **Wis** 15, **Cha** 11
**Base Atk** +1; **CMB** +0; **CMD** 9
**Feats** _[[feats/Combat Casting|Combat Casting]]_
**Skills** _[[spells/Heal|Heal]]_ +9, Intimidate +2, Knowledge (religion) +5
**Languages** Common, _Orc_
**SQ** _orc_ blood, _[[universal monster rules/Summon|summon]]_ familiar (weasel), weapon familiarity
**Combat Gear** scroll of _[[spells/Bless|bless]]_, scrolls of _[[spells/Cure Light Wounds|cure light wounds]]_ (2), scroll of _darkness_, scroll of _[[spells/Protection From Good|protection from good]]_, _alchemist_’s fire (2); **Other Gear** _[[items/Armor/Leather armor|leather armor]]_, _dagger_, darts (10), _[[npcs/Healer|healer]]_’s kit, _[[items/Mundane/Smokestick|smokestick]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, _[[items/Mundane/Tindertwig|tindertwig]]_, _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol (bone-and-tooth necklace worth 5 gp), 2 gp

A _[[classes/Shaman|shaman]]_ serves a small tribe as a visionary and source of wisdom—the sole authority on supernatural matters, and the only one who can communicate with the worlds beyond. His familiar may be a representation of his spirit animal or a spy who allows him to learn more about other tribesfolk and appear wiser than he is.

This stat block can also be used as a lesser adept apprenticed to an _[[npcs/Initiate|initiate]]_ (adept 3), _[[npcs/Doom Prophet|doom prophet]]_ (adept 4), or _[[npcs/Guru|guru]]_ (adept 6).