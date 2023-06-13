---
cssclass: [monsters]
title1: Witchcrow, Greater Witchcrow
title2: Greater Witchcrow
CR: 3
sources:
- name: 'Pathfinder #67: The Snows of Summer'
  page: 88
  link: http://paizo.com/products/btpy8ubg?Pathfinder-Adventure-Path-67-The-Snows-of-Summer
XP: 800
alignment: CE
size: Small
type: magical beast
initiative:
  bonus: 3
senses:
  darkvision: 60
  detect magic: true
  low-light vision: true
AC:
  AC: 15
  touch: 15
  flat_footed: 11
  components:
    dex: 3
    dodge: 1
    size: 1
HP:
  HP: 32
  long: 5d10+5
saves:
  fort: 5
  ref: 7
  will: 4
resistances:
  cold: 5
speeds:
  base: 20
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 talons +7 (1d6+1)
      entries:
      - - damage: 1d6+1
      count: 2
      attack: talons
      bonus:
      - 7
  special:
  - hexes (cackle, evil eye [-2, 6 rounds], misfortune [1 round])
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
    other: birds only
  - superscripts:
    - APG
    name: perceive cues
    source: default
    freq: 3/day
  - superscripts:
    - APG
    name: vanish
    source: default
    freq: 3/day
  - name: ventriloquism
    source: default
    freq: 3/day
    DC: 14
  - superscripts:
    - APG
    name: ill omen
    source: default
    freq: 1/day
  - name: mirror image
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 5
    concentration: 8
    DC_ability_score: Intelligence
ability_scores:
  STR: 12
  DEX: 17
  CON: 12
  INT: 17
  WIS: 16
  CHA: 13
BAB: 5
CMB: 5
CMB_other: +7 steal
CMD: 19
CMD_other: 21 vs. steal
feats:
- name: Combat Expertise
- name: Dodge
- is_bonus: true
  name: Flyby Attack
- name: Improved Steal
skills:
  Bluff: 5
  Fly: 15
  Knowledge (arcana): 6
  Perception: 9
  Sense Motive: 6
  Sleight of Hand: 12
  Spellcraft: 6
  Stealth: 15
  _racial_mods:
    Sleight of Hand:
      _: 8
languages:
- Abyssal
- Aklo
- Auran
- Common
- speak with animals (birds only)
special_qualities:
- apportation
ecology:
  environment: cold and temperate forests and plains
  organization: solitary, pair, covey (3-12), or murder (13-30)
  treasure_type: standard
special_abilities:
  Apportation (Su): In large enough groupings (such as a murder), greater witchcrows
    can perform a cooperative form of magic once per day to open a glowing ring in
    one place leading to somewhere else on the planet. This always entails a raucous
    aerial ritual, usually centered on those that wish to make use of this ability.
    The ritual functions like a teleportation circle (CL 17th), except it requires
    1 minute of uninterrupted casting time, the circle doesn't need to be placed on
    a horizontal surface, and it is not invisible or hard to detect. After coming
    into existence, the edges of the circle glow and the effect stays in place for
    1 minute. Most witchcrows loathe using this power, but some offer it as a service
    to those in need of quick travel, demanding a high price for such assistance-usually
    something in the bargainer's possession that is cherished, extremely valuable,
    and almost always magical.
  Hexes (Su): |-
    A greater witchcrow uses hexes as a 5th-level witch. Invariably, these abilities include the cackle, evil eye, and misfortune hexes, and require a successful DC 15 Will save to negate or resist. Witchcrow cackling proves especially unnerving as it sounds like extremely mocking cawing.

    The dreaded witchcrow, renowned as a harbinger of ill deeds and misfortune, preys on the weak and spies on the unwary. Clever, manipulative, and avaricious in the extreme, these foul birds have no conscience and know no fear. Witchcrows strive to steal not only victims' most cherished possessions, but their hopes and dreams as well. They delight in bringing anguish, sowing doubt even as they feign friendly advice designed to tear down alliances, dupe the gullible, and compromise the virtuous. Despite their deceptive nature, witchcrows can also hold valuable information-or come by such if paid to retrieve it.

    Witchcrows value arcane magic above all else, not simply as practitioners-the birds certainly have their own innate talent for witchcraft-but also as collectors. In exchange for their services or valuable information, witchcrows trade for scrolls, potions, and other lesser magic items. Even if such items go unoffered, an intense covetous streak drives witchcrows to pilfer these things if they sense them among a bargainer's possessions. Often, they single out arcane casters as targets for thievery, closing on casters from a distance with their vanish ability and executing flyby attacks to snatch away any baubles they desire. They carry such loot back to their nests to proudly share stories of their daring raids under the preening adulation of their peers. Prolonged spellcasting (casting spells with a casting time greater than 1 round) often attracts witchcrows in the area. They stalk spellcasters in groups, watching for opportunities to steal from them.
desc_long: ''

---

# Witchcrow, Greater Witchcrow

**Source** Pathfinder #67: The Snows of Summer pg. 88
**XP** 800
CE Small magical beast
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +9

##### Defense

**AC** 15, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 11 (+3 Dex, +1 dodge, +1 size)
**hp** 32 (5d10+5)
**Fort** +5, **Ref** +7, **Will** +4
**Resist** cold 5

##### Offense
**Speed** 20 ft., fly 60 ft. (good)
**Melee** 2 talons +7 (1d6+1)
**Special Attacks** hexes (cackle, evil eye [–2, 6 rounds], misfortune [1 round])
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +8; save DCs are Intelligence-based)
Constant—_detect magic_, _[[spells/Speak with Animals|speak with animals]]_ (birds only)
3/day—_[[spells/Perceive Cues|perceive cues]]_, _[[spells/Vanish|vanish]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 14)
1/day—_[[spells/Ill Omen|ill omen]]_, _[[spells/Mirror Image|mirror image]]_

##### Statistics
**Str** 12, **Dex** 17, **Con** 12, **Int** 17, **Wis** 16, **Cha** 13
**Base Atk** +5; **CMB** +5 (+7 steal); **CMD** 19 (21 vs. steal)
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Steal|Improved Steal]]_
**Skills** Bluff +5, Fly +15, Knowledge (arcana) +6, Perception +9, Sense Motive +6, Sleight of Hand +12, Spellcraft +6, Stealth +15; **Racial Modifiers** +8 Sleight of Hand
**Languages** Abyssal, Aklo, Auran, Common; _speak with animals_ (birds only)
**SQ** apportation

##### Ecology

**Environment** cold and temperate forests and plains
**Organization** solitary, pair, covey (3–12), or murder (13–30)
**Treasure** standard

### Special Abilities

**Apportation (Su) **In large enough groupings (such as a murder), greater witchcrows can perform a cooperative form of magic once per day to open a glowing ring in one place leading to somewhere else on the planet. This always entails a raucous aerial ritual, usually centered on those that _[[spells/Wish|wish]]_ to make use of this ability. The ritual functions like a _[[spells/Teleportation Circle|teleportation circle]]_ (CL 17th), except it requires 1 minute of uninterrupted casting time, the circle doesn’t need to be placed on a horizontal surface, and it is not _[[conditions/Invisible|invisible]]_ or hard to detect. After coming into existence, the edges of the circle glow and the effect stays in place for 1 minute. Most witchcrows loathe using this power, but some offer it as a service to those in need of quick travel, demanding a high price for such assistance—usually something in the bargainer’s _[[spells/Possession|possession]]_ that is cherished, extremely valuable, and almost always magical.

**Hexes (Su) **A greater _[[monsters/Witchcrow|witchcrow]]_ uses hexes as a 5th-level _[[classes/Witch|witch]]_. Invariably, these abilities include the cackle, evil eye, and misfortune hexes, and require a successful DC 15 Will save to negate or resist. _Witchcrow_ cackling proves especially unnerving as it sounds like extremely mocking cawing.

The dreaded _witchcrow_, renowned as a harbinger of ill deeds and misfortune, preys on the weak and spies on the unwary. Clever, manipulative, and avaricious in the extreme, these foul birds have no conscience and know no _[[universal monster rules/Fear|fear]]_. Witchcrows strive to steal not only victims’ most cherished possessions, but their hopes and dreams as well. They delight in bringing anguish, sowing doubt even as they feign friendly advice designed to tear down alliances, dupe the gullible, and compromise the virtuous. Despite their _[[items/Weapon Magic Abilities/Deceptive|deceptive]]_ nature, witchcrows can also hold valuable information—or come by such if paid to retrieve it.

Witchcrows value arcane magic above all else, not simply as practitioners—the birds certainly have their own innate talent for witchcraft—but also as collectors. In exchange for their services or valuable information, witchcrows trade for scrolls, potions, and other lesser magic items. Even if such items go unoffered, an intense covetous streak drives witchcrows to pilfer these things if they sense them among a bargainer’s possessions. Often, they single out arcane casters as targets for thievery, closing on casters from a distance with their _vanish_ ability and executing flyby attacks to _[[feats/Snatch|snatch]]_ away any baubles they desire. They carry such loot back to their nests to proudly share stories of their daring raids under the preening adulation of their peers. Prolonged spellcasting (casting spells with a casting time greater than 1 round) often attracts witchcrows in the area. They stalk spellcasters in groups, watching for opportunities to steal from them.