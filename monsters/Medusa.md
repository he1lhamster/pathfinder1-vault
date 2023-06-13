---
cssclass: [monsters]
title1: Medusa
desc_short: This unnatural woman has scaled skin, white bird wings, and long snake-hair
  that hangs past her feet.
title2: Mythic Medusa
CR: 9
MR: 3
sources:
- name: Mythic Adventures
  page: 209
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 6400
alignment: LE
size: Medium
type: monstrous humanoid
subtypes:
- mythic
initiative:
  bonus: 10
senses:
  all-around vision: true
  darkvision: 60
AC:
  AC: 23
  touch: 13
  flat_footed: 20
  components:
    dex: 3
    natural: 10
HP:
  HP: 115
  long: 9d10+66
saves:
  fort: 7
  ref: 11
  will: 8
DR:
- amount: 5
  weakness: epic
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: mwk bastard sword +10/+5 (1d10/19-20 plus poison)
      entries:
      - - damage: 1d10
          crit_range: 19-20
        - effect: poison
      attack: mwk bastard sword
      bonus:
      - 10
      - 5
    - text: 2 snake bites +12 (1d6+3 plus poison)
      entries:
      - - damage: 1d6+3
        - effect: poison
      count: 2
      attack: snake bites
      bonus:
      - 12
  ranged:
  - - text: mwk longbow +13/+8 (1d8/×3 plus poison)
      entries:
      - - damage: 1d8
          crit_multiplier: 3
        - effect: poison
      attack: mwk longbow
      bonus:
      - 13
      - 8
  special:
  - mythic power (3/day, surge +1d6)
  - petrifying gaze
  - poison
  - poison weapons
  - summon snake
  - unpetrify
space: 5
reach: 5
reach_other: 10 ft. with snake bite
ability_scores:
  STR: 10
  DEX: 17
  CON: 18
  INT: 12
  WIS: 15
  CHA: 19
BAB: 9
CMB: 9
CMD: 22
feats:
- is_mythic: true
  name: Improved Initiative
- name: Lightning Reflexes
- name: Point-Blank Shot
- name: Precise Shot
- is_mythic: true
  name: Weapon Finesse
skills:
  Bluff: 13
  Disguise: 13
  Fly: 7
  Intimidate: 16
  Perception: 18
  Stealth: 15
  _racial_mods:
    Perception:
      _: 4
languages:
- Common
ecology:
  environment: temperate marshes and underground
  organization: solitary
  treasure_type: double
  treasure:
  - mwk bastard sword
  - mwk longbow with 20 arrows
  - other treasure
special_abilities:
  Petrifying Gaze (Su): Turn to stone permanently, 30 feet, Fortitude DC 18 negates.
    The save DC is Charisma-based.
  Poison (Ex): Snake bite; save Fort DC 18; frequency 1/round for 6 rounds; effect
    1d4 Con; cure 2 consecutive saves. The save DC is Constitution-based.
  Poison Weapons (Ex): A mythic medusa can spend a standard action to apply her snake
    poison to her sword or to two arrows, and normally poisons her weapons in advance.
  Summon Snake (Sp): As a full-round action, a mythic medusa can summon an emperor
    cobra (Bestiary 2 252) or 1d3 amphisbaenas (Bestiary 2 25) as if using a summon
    monster spell. The summoned snakes are immune to the medusa's gaze attack and
    remain for 8 rounds before disappearing.
  Unpetrify (Su): A mythic medusa can expend one use of mythic power to return a petrified
    creature to life (as if using stone to flesh) for 1 minute. The creature is under
    the medusa's control (as if using dominate monster) and reverts to a statue at
    the end of this time. If the medusa expends three uses of mythic power, the creature
    remains unpetrified for 24 hours instead of 1 minute. A typical petrified victim
    in a mythic medusa's lair is a half-elf fighter 6 (Pathfinder RPG NPC Codex 82)
    or human warrior 6 (NPC Codex 268).
desc_long: A mythic medusa is one of the near-immortal progenitors of the medusa race,
  who mate with humanoids in order to produce weaker (but still deadly) offspring.
  With deadly poison, power over snakes, and the ability to animate and command those
  she has turned to stone, a mythic medusa is a dangerous foe who can't be easily
  overcome by mirrored shields and blindfolds; she waits, strikes, and retreats, allowing
  her minions and venom to weaken her foes before she is ready to take their lives.

---

# Medusa
This slender, attractive woman has strangely glowing eyes and a full head of hissing snakes for hair.
**Source** Pathfinder RPG Bestiary pg. 201
**XP** 3,200

LE Medium monstrous humanoid
**Init** +6; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +16

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 13 ( +2 Dex, +3 natural)
**hp** 76 (8d10+32)
**Fort** +6, **Ref** +8, **Will** +7

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +10/+5 (1d4/19–20), snake bite +5 (1d4 plus poison)
**Ranged** mwk _[[items/Weapon/Longbow|longbow]]_ +11/+6 (1d8/×3)
**Special Attacks** petrifying _[[universal monster rules/Gaze|gaze]]_

##### Statistics
**Str** 10, **Dex** 15, **Con** 18, **Int** 12, **Wis** 13, **Cha** 15
**Base Atk** +8; **CMB** +8; **CMD** 20
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +10, Disguise +10, Intimidate +13, Perception +16, Stealth +13; **Racial Modifiers** +4 Perception
**Languages** Common

##### Ecology

**Environment** temperate marshes and underground
**Organization** solitary
**Treasure** double (_dagger_, masterwork _longbow_ with 20 arrows, other treasure)

### Special Abilities

**_All-Around Vision_ (Ex)** A _[[monsters/Medusa|medusa]]_’s snake-hair allows her to see in all directions. Medusas gain a +4 racial bonus to Perception checks and cannot be flanked.

**Petrifying _Gaze_ (Su)** Turn to stone permanently, 30 feet, Fortitude DC 16 negates. The save DC is Charisma-based.

**Poison (Ex)** Bite—injury; save Fort DC 18; frequency 1/round for 6 rounds; effect 1d3 Str; cure 2 consecutive saves. The save DC is Constitution-based.

##### Description

Medusas are human-like creatures with snakes instead of hair. At distances of 30 feet or more, a _medusa_ can easily pass for a beautiful woman if she wears something to cover her serpentine locks—when wearing clothing that conceals her head and face, she can be mistaken for a human at even closer distances. Medusas use lies and disguises that conceal their faces to get close enough to opponents to use their petrifying _gaze_, though they like playing with their prey and may fire arrows from a distance to lead enemies into traps. Some enjoy creating intricate decorations out of their victims, using their _[[conditions/Petrified|petrified]]_ remains as accents to their swampy lairs, but most medusas take care to hide the evidence of their previous conflicts so that new foes won’t have advance warning of their presence.

Used to concealing themselves, medusas in cities are usually rogues, while those in the wilderness often pass themselves off as rangers or trackers. The most notorious and legendary medusas, though, are those who take levels as bards or clerics. Charismatic and intelligent, urban medusas are often involved with thieves’ guilds or other aspects of the criminal underworld. Medusas may form alliances with blind creatures or intelligent undead, both of which are immune to their stony _gaze_. Spellcasting medusas often serve as oracles or prophets, usually dwelling in remote locations of legendary power or infamous history. Such _[[classes/Oracle|oracle]]_ medusas take great delight in their roles, and if presented with the proper gifts and flattery, the secrets they offer can be quite helpful. Of course, the lairs of such _[[items/Weapon Magic Abilities/Potent|potent]]_ creatures are liberally decorated with statues of those who have offended them, so the seeker of knowledge is well advised to tred carefully during such meetings.

All known medusas are female. Rarely, a _medusa_ may decide to keep a male humanoid as a mate, usually with the help of elixirs of love or similar magic, and is always careful to not petrify her prisoner—at least until she grows tired of his company.