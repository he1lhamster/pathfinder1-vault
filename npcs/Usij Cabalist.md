---
cssclass: [monsters]
title1: Usij Cabalist
title2: Usij Cabalist
CR: 4
sources:
- name: Inner Sea NPC Codex
  page: 59
  link: http://paizo.com/products/btpy92lj?Pathfinder-Campaign-Setting-Inner-Sea-NPC-Codex
XP: 1200
race: Human
classes:
- cleric of Ahriman 5
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 1
AC:
  AC: 16
  touch: 11
  flat_footed: 15
  components:
    armor: 5
    dex: 1
HP:
  HP: 31
  long: 5d8+5
saves:
  fort: 6
  ref: 3
  will: 8
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk scorpion whip +4 (1d4-1)
      entries:
      - - damage: 1d4-1
      attack: mwk scorpion whip
      bonus:
      - 4
  - - text: dagger +4 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 4
  special:
  - channel negative energy 5/day (DC 16, 3d6)
  - destructive smite (+2, 6/day)
spell_like_abilities:
  entries:
  - name: touch of evil
    source: default
    freq: 6/day
    other: 2 rounds
  sources:
  - name: default
    CL: 5
    concentration: 8
spells:
  entries:
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 16
  - is_domain_spell: true
    name: call lightning
    source: Cleric
    level: 3
    DC: 16
  - name: dispel magic
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: gust of wind
    source: Cleric
    level: 2
    DC: 15
  - name: shatter
    source: Cleric
    level: 2
  - name: silence
    source: Cleric
    level: 2
    DC: 15
  - name: undetectable alignment
    source: Cleric
    level: 2
  - name: command
    source: Cleric
    level: 1
    DC: 14
  - name: cure light wounds
    source: Cleric
    level: 1
  - name: doom
    source: Cleric
    level: 1
    DC: 14
  - superscripts:
    - UM
    name: forbid action
    source: Cleric
    level: 1
    DC: 15
  - is_domain_spell: true
    name: true strike
    source: Cleric
    level: 1
  - name: create water
    source: Cleric
    level: 0
  - name: detect magic
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 5
    concentration: 8
    slots:
      0: at-will
    domains:
    - catastrophe
    - evil
ability_scores:
  STR: 8
  DEX: 12
  CON: 12
  INT: 13
  WIS: 16
  CHA: 14
BAB: 3
CMB: 2
CMB_other: +4 trip
CMD: 15
CMD_other: 17 vs. trip
feats:
- name: Combat Expertise
- name: Improved Channel
- name: Improved Trip
- name: Weapon Finesse
skills:
  Bluff: 5
  Craft (alchemy): 5
  Diplomacy: 6
  Disguise: 5
  Knowledge (local): 3
  Linguistics: 6
  Perception: 4
  Spellcraft: 6
  Stealth: 5
  Use Magic Device: 7
languages:
- Abyssal
- Common
- Infernal
- Osiriani
special_qualities:
- aura
gear:
  combat:
  - potion of invisibility
  - scroll of owl's wisdom
  - wand of cure light wounds (50 charges)
  other:
  - +1 chain shirt
  - mwk scorpion whip
  - dagger
  - cloak of resistance +1
desc_long: |-
  The Usij are a secret cabal of nihilistic spellcasters who follow Ahriman-Lord of All Divs, He Who Walks In Ruin, the Father of Oblivion. Originating in Casmaron, cabals of Usij spread to northern Garund with the Keleshite invasion. In the time since, the cult has flourished in Thuvia, where in the vast deserts of that nation the House of Oblivion stands as a permanent marker of Ahriman's presence. Usij blend in with desert societies, keeping their dedication to their lord a secret while spreading ruin and social decay.

  Usij seek to destroy. Some insinuate themselves into high political positions where they steer the might of armies against others, or squander the coffers of wealthy nations and noble houses. Other Usij cabalists spend their efforts to destroy bonds of family, friends, and faith. They maneuver themselves into relationships with troubled people who are easy to sway, and avoid getting their own hands dirty by persuading the desperate to commit ruinous acts. Many Usij are skilled alchemists and entire cells are dedicated to refining deadly poisons and powerful drugs.

  These div-callers and agents of catastrophe sometimes gather in secret societies within urban areas or inhabit desert complexes far from scrutiny. Any large cell of Usij is likely to include at least one div that associates with the cell, typically a pairaka or sepid, and many Usij sorcerers and wizards call dorus as familiars. Usij cabals operate independently of each other, but they always pursue the same goal: ruin. Recent rumors claim a cabal of Usij alchemists have joined with a great wyrm blue dragon and are scouring the desert for sun orchids in order to synthesize their own version of the sun orchid elixir. Some say that certain Usij leaders meet annually at a secret location somewhere in central Casmaron, but this may be only whispers on paranoid lips.

---

# Usij Cabalist

**Source** Inner Sea NPC Codex pg. 59
**XP** 1,200
Human _[[classes/Cleric|cleric]]_ of Ahriman 5

NE Medium humanoid (human)
**Init** +1; **Senses** Perception +4

##### Defense

**AC** 16, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 armor, +1 Dex)
**hp** 31 (5d8+5)
**Fort** +6, **Ref** +3, **Will** +8

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Scorpion whip|scorpion whip]]_ +4 (1d4–1) or _[[items/Weapon/Dagger|dagger]]_ +4 (1d4–1/19–20)
**Special Attacks** channel negative energy 5/day (DC 16, 3d6), destructive smite (+2, 6/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +8)
6/day—_[[feats/Touch Of Evil|touch of evil]]_ (2 rounds)
**_Cleric_ Spells Prepared **(CL 5th; concentration +8)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 16), _[[spells/Call Lightning|call lightning]]_ (DC 16), _[[spells/Dispel Magic|dispel magic]]_
2nd—_[[spells/Gust Of Wind|gust of wind]]_ (DC 15), _[[spells/Shatter|shatter]]_, _[[spells/Silence|silence]]_ (DC 15), _[[spells/Undetectable Alignment|undetectable alignment]]_
1st—_[[spells/Command|command]]_ (DC 14), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Doom|doom]]_ (DC 14), _[[spells/Forbid Action|forbid action]]_ (DC 15), _[[spells/True Strike|true strike]]_
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**D** Domain spell; **Domains** Catastrophe, Evil

##### Statistics
**Str** 8, **Dex** 12, **Con** 12, **Int** 13, **Wis** 16, **Cha** 14
**Base Atk** +3; **CMB** +2 (+4 _[[universal monster rules/Trip|trip]]_); **CMD** 15 (17 vs. _trip_)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +5, Craft (alchemy) +5, Diplomacy +6, Disguise +5, Knowledge (local) +3, Linguistics +6, Perception +4, Spellcraft +6, Stealth +5, Use Magic Device +7
**Languages** Abyssal, Common, Infernal, Osiriani
**SQ** aura
**Combat Gear** potion of _[[spells/Invisibility|invisibility]]_, scroll of owl’s wisdom, wand of _cure light wounds_ (50 charges); **Other Gear** +1 _[[items/Armor/Chain shirt|chain shirt]]_, mwk _scorpion whip_, _dagger_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_

The Usij are a secret cabal of nihilistic spellcasters who follow Ahriman—Lord of All Divs, He Who Walks In Ruin, the Father of _[[monsters/Oblivion|Oblivion]]_. Originating in Casmaron, cabals of Usij spread to northern Garund with the Keleshite invasion. In the time since, the cult has flourished in Thuvia, where in the vast deserts of that nation the House of _Oblivion_ stands as a permanent marker of Ahriman’s presence. Usij _[[spells/Blend|blend]]_ in with desert societies, keeping their dedication to their lord a secret while spreading ruin and social decay.

Usij seek to destroy. Some insinuate themselves into high political positions where they steer the might of armies against others, or squander the coffers of wealthy nations and noble houses. Other Usij cabalists spend their efforts to destroy bonds of family, friends, and faith. They maneuver themselves into relationships with troubled people who are easy to sway, and avoid getting their own hands dirty by persuading the desperate to commit ruinous acts. Many Usij are skilled alchemists and entire cells are dedicated to refining _[[items/Weapon Magic Abilities/Deadly|deadly]]_ poisons and powerful drugs.

These div-callers and agents of catastrophe sometimes gather in secret societies within urban areas or inhabit desert complexes far from scrutiny. Any large cell of Usij is likely to include at least one div that associates with the cell, typically a pairaka or sepid, and many Usij sorcerers and wizards call dorus as familiars. Usij cabals operate independently of each other, but they always pursue the same goal: ruin. Recent rumors claim a cabal of Usij alchemists have joined with a great wyrm blue dragon and are scouring the desert for sun orchids in order to synthesize their own version of the _[[items/Wondrous Item/Sun Orchid Elixir|sun orchid elixir]]_. Some say that certain Usij leaders meet annually at a secret location somewhere in central Casmaron, but this may be only whispers on paranoid lips.