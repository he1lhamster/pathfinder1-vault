---
cssclass: [monsters]
title1: Intellect Devourer
desc_short: Devoid of a head, or any features at all save for four short, clawed legs,
  this creature's body looks like a large, glistening brain.
title2: Intellect Devourer
CR: 8
sources:
- name: Pathfinder RPG Bestiary
  page: 180
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 4800
alignment: CE
size: Small
type: aberration
initiative:
  bonus: 10
senses:
  blindsight: 60
  detect magic: true
AC:
  AC: 22
  touch: 17
  flat_footed: 16
  components:
    dex: 6
    natural: 5
    size: 1
HP:
  HP: 84
  long: 8d8+48
saves:
  fort: 7
  ref: 8
  will: 8
DR:
- amount: 10
  weakness: adamantine and magic
immunities:
- fire
- mind-affecting effects
resistances:
  cold: 20
  electricity: 20
  sonic: 20
SR: 23
weaknesses:
- vulnerability to protection from evil
speeds:
  base: 40
attacks:
  melee:
  - - text: 4 claws +13 (1d4+1)
      entries:
      - - damage: 1d4+1
      count: 4
      attack: claws
      bonus:
      - 13
  special:
  - body thief
  - sneak attack +3d6
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: confusion
    source: default
    freq: At will
    DC: 17
    other: single target only
  - name: daze monster
    source: default
    freq: At will
    DC: 15
    other: no HD limit
  - name: inflict serious wounds
    source: default
    freq: At will
    DC: 16
  - name: invisibility
    source: default
    freq: At will
  - name: reduce size
    source: default
    freq: At will
    other: as reduce person but self only
  - name: cure moderate wounds
    source: default
    freq: 3/day
  - name: globe of invulnerability
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 8
ability_scores:
  STR: 12
  DEX: 23
  CON: 21
  INT: 16
  WIS: 10
  CHA: 17
BAB: 6
CMB: 6
CMD: 22
CMD_other: 26 vs. trip
feats:
- name: Improved Initiative
- name: Iron Will
- name: Toughness
- name: Weapon Finesse
skills:
  Bluff: 19
  Disguise: 11
  Knowledge (local): 14
  Perception: 19
  Sense Motive: 8
  Stealth: 29
  Use Magic Device: 11
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
    Stealth:
      _: 8
languages:
- Undercommon (cannot speak)
- telepathy 100 ft.
ecology:
  environment: any underground
  organization: solitary, brood (2-6), or tribe (7-16)
  treasure_type: double
special_abilities:
  Body Thief (Su): As a full-round action that provokes an attack of opportunity,
    an intellect devourer can reduce its size, crawl into the mouth of a helpless
    or dead creature, and burrow into the victim's skull to devour its brain. This
    is a coup de grace attempt that inflicts 8d4+3d6+8 points of damage. If the victim
    is slain (or already dead), the intellect devourer usurps control of the body
    and may use it as its own, as if it controlled the target via a dominate monster
    spell. The intellect devourer has full access to all of the host's defensive and
    offensive abilities save for spellcasting and spell-like abilities (although the
    intellect devourer can still use its own spell-like abilities). A host body may
    not have been dead for longer than 1 day for this ability to function, and even
    successfully inhabited bodies decay to uselessness in 7 days (unless this time
    is extended via gentle repose). As long as the intellect devourer occupies the
    body, it knows (and can speak) the languages known by the victim and basic information
    about the victim's identity and personality, yet has none of the victim's specific
    memories or knowledge. Damage done to a host body does not harm the intellect
    devourer, and if the host body is slain, the intellect devourer emerges and is
    dazed for 1 round. Raise dead cannot restore a victim of body theft, but resurrection
    or more powerful magic can.
  Vulnerable to Protection from Evil (Ex): An intellect devourer is treated as a summoned
    creature for the purpose of determining how it is affected by a protection from
    evil spell.
desc_long: |-
  Thought by some to be invaders from another dimension or planet, the sinister intellect devourers are certainly one of the world's cruelest races. Incapable of experiencing emotions or wallowing in the sins of physical pleasure on their own, intellect devourers are forced to steal bodies in order to indulge their gluttony, lust, and cruelty. Stories tell of entire cities of these creatures deep underground, where host bodies are worn like clothes to hideous orgies and vile feasts. Lone intellect devourers often dwell in ruins or caves on the edge of a civilized region so they can make periodic forays into town to “shop” for an attractive new body.

  An intellect devourer is 3 feet long and weighs about 60 pounds.

---

# Intellect Devourer
Devoid of a head, or any features at all save for four short, clawed legs, this creature’s body looks like a large, glistening brain.
**Source** Pathfinder RPG Bestiary pg. 180
**XP** 4,800
CE Small aberration
**Init** +10; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_; Perception +19

##### Defense

**AC** 22, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 Dex, +5 natural, +1 size)
**hp** 84 (8d8+48)
**Fort** +7, **Ref** +8, **Will** +8
**DR** 10/adamantine and magic; **Immune** fire, mind-affecting effects; **Resist** cold 20, electricity 20, sonic 20; **SR** 23
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to _[[spells/Protection From Evil|protection from evil]]_

##### Offense
**Speed** 40 ft.
**Melee** 4 claws +13 (1d4+1)
**Special Attacks** body thief, sneak attack +3d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th)
Constant - _detect magic_
At will - _[[spells/Confusion|confusion]]_ (DC 17, single target only), _[[spells/Daze Monster|daze monster]]_ (DC 15, no HD limit), _[[spells/Inflict Serious Wounds|inflict serious wounds]]_ (DC 16), _[[spells/Invisibility|invisibility]]_, reduce size (as _[[spells/Reduce Person|reduce person]]_ but self only)
3/day - _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Globe Of Invulnerability|globe of invulnerability]]_

##### Statistics
**Str** 12, **Dex** 23, **Con** 21, **Int** 16, **Wis** 10, **Cha** 17
**Base Atk** +6; **CMB** +6; **CMD** 22 (26 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +19, Disguise +11, Knowledge (local) +14, Perception +19, Sense Motive +8, Stealth +29, Use Magic Device +11; **Racial Modifiers** +8 Bluff, +8 Perception, +8 Stealth
**Languages** Undercommon (cannot speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any underground
**Organization** solitary, brood (2–6), or tribe (7–16)
**Treasure** double

### Special Abilities

**Body Thief (Su)** As a full-round action that provokes an attack of opportunity, an _[[monsters/Intellect Devourer|intellect devourer]]_ can reduce its size, crawl into the mouth of a _[[conditions/Helpless|helpless]]_ or dead creature, and _[[universal monster rules/Burrow|burrow]]_ into the victim’s skull to devour its brain. This is a coup de _[[spells/Grace|grace]]_ attempt that inflicts 8d4+3d6+8 points of damage. If the victim is slain (or already dead), the _intellect devourer_ usurps control of the body and may use it as its own, as if it controlled the target via a _[[spells/Dominate Monster|dominate monster]]_ spell. The _intellect devourer_ has full access to all of the host’s defensive and offensive abilities save for spellcasting and _spell-like abilities_ (although the _intellect devourer_ can still use its own _spell-like abilities_). A host body may not have been dead for longer than 1 day for this ability to function, and even successfully inhabited bodies decay to uselessness in 7 days (unless this time is extended via _[[spells/Gentle Repose|gentle repose]]_). As long as the _intellect devourer_ occupies the body, it knows (and can speak) the languages known by the victim and basic information about the victim’s identity and personality, yet has none of the victim’s specific memories or knowledge. Damage done to a host body does not _[[spells/Harm|harm]]_ the _intellect devourer_, and if the host body is slain, the _intellect devourer_ emerges and is _[[conditions/Dazed|dazed]]_ for 1 round. _[[spells/Raise Dead|Raise dead]]_ cannot restore a victim of body theft, but _[[spells/Resurrection|resurrection]]_ or more powerful magic can.

**Vulnerable to _Protection from Evil_ (Ex) **An _intellect devourer_ is treated as a summoned creature for the purpose of determining how it is affected by a _protection from evil_ spell.

##### Description

Thought by some to be invaders from another dimension or planet, the sinister intellect devourers are certainly one of the world’s cruelest races. Incapable of experiencing emotions or wallowing in the sins of physical pleasure on their own, intellect devourers are forced to steal bodies in order to indulge their gluttony, lust, and _[[feats/Cruelty|cruelty]]_. Stories tell of entire cities of these creatures deep underground, where host bodies are worn like clothes to hideous orgies and vile feasts. Lone intellect devourers often dwell in ruins or caves on the edge of a civilized region so they can make periodic forays into town to “shop” for an attractive new body.

An _intellect devourer_ is 3 feet long and weighs about 60 pounds.