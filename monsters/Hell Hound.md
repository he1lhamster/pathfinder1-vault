---
cssclass: [monsters]
title1: Hell Hound
desc_short: This brawny hound is wreathed in flames, and its footsteps leave burning
  prints that sputter and smoke.
title2: Mythic Hell Hound
CR: 4
MR: 1
sources:
- name: Mythic Adventures
  page: 203
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 1200
alignment: LE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
- fire
- lawful
- mythic
initiative:
  bonus: 5
senses:
  darkvision: 60
  scent: true
AC:
  AC: 17
  touch: 11
  flat_footed: 16
  components:
    dex: 1
    natural: 6
HP:
  HP: 47
  long: 5d10+20
saves:
  fort: 6
  ref: 5
  will: 1
DR:
- amount: 5
  weakness: epic
immunities:
- fire
weaknesses:
- vulnerable to cold
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +9 (2d6+3 plus burn)
      entries:
      - - damage: 2d6+3
        - effect: burn
      attack: bite
      bonus:
      - 9
  special:
  - breath weapon (10-ft. cone, 2d6 fire plus clinging flames, Reflex DC 14 half,
    usable every 1d4 rounds)
  - burn (1d6, DC 14)
  - mythic power (1/day, surge +1d6)
ability_scores:
  STR: 15
  DEX: 13
  CON: 15
  INT: 6
  WIS: 10
  CHA: 6
BAB: 5
CMB: 7
CMD: 18
CMD_other: 22 vs. trip
feats:
- name: Improved Initiative
- name: Run
- is_mythic: true
  name: Weapon Focus (bite)
skills:
  Acrobatics: 9
    when jumping: 13
  Perception: 8
  Stealth: 14
  Survival: 8
  _racial_mods:
    Stealth:
      _: 5
languages:
- Infernal (can't speak)
ecology:
  environment: any (Hell)
  organization: solitary, pair, or pack (3-12)
  treasure_type: incidental
special_abilities:
  Clinging Flames (Ex): A creature that takes damage from a mythic hell hound's breath
    weapon also catches on fire (using the save DC for its burn ability).
desc_long: A mythic hell hound is a prince among the wolves of Hell, feral but still
  subservient to the archdevils. Allowed to run wild, they are the original creatures
  from which the “tamer” common hell hounds were made.

---

# Hell Hound
This creature resembles a thin, lanky _[[monsters/Wolf|wolf]]_ with reddish-brown fur, white claws, and _[[items/Weapon Magic Abilities/Burning|burning]]_, fiery red eyes.
**Source** Pathfinder RPG Bestiary pg. 173
**XP** 800

LE Medium outsider (evil, extraplanar, fire, lawful)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +7

##### Defense

**AC** 16, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+1 Dex, +5 natural)
**hp** 30 (4d10+8)
**Fort** +6, **Ref** +5, **Will** +1
**Immune** fire
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 40 ft.
**Melee** bite +5 (1d8+1 plus 1d6 fire)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (10-ft. cone, once every 2d4 rounds, 2d6 fire damage, Reflex DC 14 for half)

##### Statistics
**Str** 13, **Dex** 13, **Con** 15, **Int** 6, **Wis** 10, **Cha** 6
**Base Atk** +4; **CMB** +5; **CMD** 16 (20 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, Run
**Skills** Acrobatics +8, Perception +7, Stealth +13, Survival +7; **Racial Modifiers** +5 Stealth
**Languages** Infernal (cannot speak)

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or pack (3–12)
**Treasure** incidental

##### Description

A typical _[[monsters/Hell Hound|hell hound]]_ stands 4–5 feet tall at the shoulder and weighs 120 pounds. Efficient hunters, a favorite pack tactic is to surround prey quietly, then attack with one or two hounds, driving prey toward the rest of the pack with their fiery breath. If the prey doesn’t run, the pack closes in. Hell hounds track fleeing creatures relentlessly.

Hell hounds are particularly favored by fire giants, as the creatures are immune to fire and share the fire giant’s sense of _[[feats/Cruelty|cruelty]]_ when it comes to handling intruders. Only when a fire giant goes too far toward treating a relatively intelligent _hell hound_ like a pet do such alliances begin to _[[feats/Falter|falter]]_.