---
cssclass: [monsters]
second_statblock: true
title1: Mammoth Rider
title2: Mammoth Rider
CR: 14
sources:
- name: Inner Sea NPC Codex
  page: 36
  link: http://paizo.com/products/btpy92lj?Pathfinder-Campaign-Setting-Inner-Sea-NPC-Codex
XP: 38400
race: Human
classes:
- barbarian 3
- druid 6
- mammoth rider 6
alignment: CN
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 1
AC:
  AC: 20
  touch: 12
  flat_footed: 18
  components:
    armor: 6
    dex: 1
    dodge: 1
    shield: 2
HP:
  HP: 112
  long: 3d12+6d8+6d12+21
  HD: 15
saves:
  fort: 16
  ref: 10
  ref_other: +1 vs. traps
  will: 13
  other: +2 vs. arcane spells, +4 vs. fey and plant-targeted effects
defensive_abilities:
- mistrust of magic
- uncanny dodge
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 returning spear +20/+15/+10 (1d8+9/×3)
      entries:
      - - damage: 1d8+9
          crit_multiplier: 3
      attack: +2 returning spear
      bonus:
      - 20
      - 15
      - 10
  - - text: mwk battleaxe +19/+14/+9 (1d8+5/×3)
      entries:
      - - damage: 1d8+5
          crit_multiplier: 3
      attack: mwk battleaxe
      bonus:
      - 19
      - 14
      - 9
  ranged:
  - - text: +2 returning spear +22 (1d8+7/×3)
      entries:
      - - damage: 1d8+7
          crit_multiplier: 3
      attack: +2 returning spear
      bonus:
      - 22
  special:
  - colossus hunter
  - rage (9 rounds/day)
  - rage powers (ferocious mount)
  - wild shape 2/day
spells:
  entries:
  - name: call lightning
    source: Druid
    level: 3
    DC: 16
  - name: greater magic fang
    source: Druid
    level: 3
  - name: protection from energy
    source: Druid
    level: 3
  - superscripts:
    - APG
    name: aspect of the bear
    source: Druid
    level: 2
  - name: bear's endurance
    source: Druid
    level: 2
  - name: cat's grace
    source: Druid
    level: 2
  - name: resist energy
    source: Druid
    level: 2
  - superscripts:
    - APG
    name: keen senses
    source: Druid
    level: 1
  - name: obscuring mist
    source: Druid
    level: 1
  - name: pass without trace
    source: Druid
    level: 1
  - name: speak with animals
    source: Druid
    level: 1
  - name: flare
    source: Druid
    level: 0
    DC: 13
  - name: guidance
    source: Druid
    level: 0
  - name: resistance
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 6
    concentration: 9
    slots:
      0: at-will
ability_scores:
  STR: 20
  DEX: 13
  CON: 12
  INT: 8
  WIS: 16
  CHA: 10
BAB: 13
CMB: 18
CMD: 30
feats:
- name: Animal Affinity
- name: Deadly Aim
- name: Dodge
- name: Great Fortitude
- name: Lightning Reflexes
- name: Mobility
- name: Mounted Archery
- name: Mounted Combat
- name: Ride-By Attack
- name: Spirited Charge
- name: Trample
skills:
  Handle Animal: 22
  Intimidate: 12
  Knowledge (nature): 9
  Ride: 21
  Spellcraft: 8
  Survival: 18
  Perception: 3
languages:
- Common
- Druidic
- Hallit
- Sylvan
special_qualities:
- fast movement
- hunter's instinct
- nature bond (animal companion)
- nature sense
- rapid straddle
- steed
- trackless step
- trap sense +1
- undaunted
- wild coercion
- wild empathy +12
- woodland stride
gear:
  combat:
  - potion of barkskin (CL 6th)
  - potion of bull's strength
  - potions of cure serious wounds (2)
  - scrolls of reduce animal (2)
  - wand of endure elements (40 charges)
  other:
  - +2 hide armor
  - +1 light wooden shield
  - +2 returning spear
  - mwk battleaxe
  - cloak of resistance +2
  - lesser belt of mighty hurling
  - holly and mistletoe
  - exotic military saddle
  - 10 gp
special_abilities:
  Colossus Hunter (Ex): The mammoth rider gains a +1 bonus on weapon attack and damage
    rolls against Large and Huge creatures, and a +2 bonus on weapon attack and damage
    rolls against Gargantuan and Colossal creatures.
  Hunter's Instinct (Ex): A mammoth rider gains the quarry class ability; this is
    exactly like the ranger ability of the same name. She can use this ability on
    any creature, not just a favored enemy.
  Mistrust of Magic (Ex): As long as she doesn't possess any levels in a class that
    grants her the ability to cast arcane spells, the mammoth rider gains a +2 morale
    bonus on saving throws against arcane spells.
  Rapid Straddle (Ex): A mammoth rider can attempt Ride checks to fast mount or fast
    dismount her steed even if it's more than one size category larger than her, provided
    she still has a move action available that round.
  Steed (Ex): A mammoth lord treats levels in the mammoth lord prestige class as druid
    levels for the purpose of determining the advancement of her animal companion.
  Undaunted (Ex): A mammoth rider adds her Strength bonus to the DC of Intimidate
    checks made against her. Additionally, creatures attempting to intimidate her
    don't gain a bonus for being larger than her.
  Wild Coercion (Ex): A mammoth rider's prestige class levels stack with her druid
    levels for the purposes of determining the effects of her wild empathy class feature.
    In addition, a mammoth rider can use her wild empathy to demoralize an animal
    or magical beast, or force it to be friendly to her, as if using Intimidate rather
    than Diplomacy. She adds her Strength modifier to these checks in addition to
    her Charisma modifier.
desc_long: ''

---

# Mammoth Rider

**Source** Inner Sea NPC Codex pg. 36
**XP** 38,400
Human _[[classes/Barbarian|barbarian]]_ 3/druid 6/mammoth rider 6

CN Medium humanoid (human)
**Init** +1; **Senses** Perception +3

##### Defense

**AC** 20, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+6 armor, +1 Dex, +1 _[[feats/Dodge|dodge]]_, +2 _[[spells/Shield|shield]]_)
**hp** 112 (15 HD; 3d12+6d8+6d12+21)
**Fort** +16, **Ref** +10 (+1 vs. traps), **Will** +13; +2 vs. arcane spells, +4 vs. fey and plant–targeted effects
**Defensive Abilities** mistrust of magic, uncanny _dodge_

##### Offense
**Speed** 30 ft.
**Melee** +2 returning _[[items/Weapon/Spear|spear]]_ +20/+15/+10 (1d8+9/×3) or mwk _[[items/Weapon/Battleaxe|battleaxe]]_ +19/+14/+9 (1d8+5/×3)
**Ranged** +2 returning _spear_ +22 (1d8+7/×3)
**Special Attacks** colossus _[[classes/Hunter|hunter]]_, _[[spells/Rage|rage]]_ (9 rounds/day), _rage_ powers (ferocious _[[spells/Mount|mount]]_), wild shape 2/day
**_[[classes/Druid|Druid]]_ Spells Prepared **(CL 6th; concentration +9)
3rd—_[[spells/Call Lightning|call lightning]]_ (DC 16), greater _[[spells/Magic Fang|magic fang]]_, _[[spells/Protection from Energy|protection from energy]]_
2nd—_[[spells/Aspect of the Bear|aspect of the bear]]_, bear’s _[[feats/Endurance|endurance]]_, cat’s _[[spells/Grace|grace]]_, _[[spells/Resist Energy|resist energy]]_
1st—_[[spells/Keen Senses|keen senses]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Pass without Trace|pass without trace]]_, _[[spells/Speak with Animals|speak with animals]]_
0 (at will)— _[[spells/Flare|flare]]_ (DC 13), _[[spells/Guidance|guidance]]_, _[[universal monster rules/Resistance|resistance]]_, stabilize

##### Statistics
**Str** 20, **Dex** 13, **Con** 12, **Int** 8, **Wis** 16, **Cha** 10
**Base Atk** +13; **CMB** +18; **CMD** 30
**Feats** _[[feats/Animal Affinity|Animal Affinity]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Mounted Archery|Mounted Archery]]_, _[[feats/Mounted Combat|Mounted Combat]]_, _[[feats/Ride-By Attack|Ride-By Attack]]_, _[[feats/Spirited Charge|Spirited Charge]]_, _[[universal monster rules/Trample|Trample]]_
**Skills** Handle Animal +22, Intimidate +12, Knowledge (nature) +9, Ride +21, Spellcraft +8, Survival +18
**Languages** Common, Druidic, Hallit, Sylvan
**SQ** fast movement, _hunter_’s instinct, nature bond (animal companion), nature sense, rapid straddle, steed, _[[items/Armor Magic Abilities/Trackless|trackless]]_ step, trap sense +1, undaunted, wild coercion, wild _[[feats/Empathy|empathy]]_ +12, woodland stride
**Combat Gear** potion of _[[spells/Barkskin|barkskin]]_ (CL 6th), potion of bull’s strength, potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), scrolls of _[[spells/Reduce Animal|reduce animal]]_ (2), wand of _[[spells/Endure Elements|endure elements]]_ (40 charges); **Other Gear** +2 _[[items/Armor/Hide armor|hide armor]]_, +1 _[[items/Shield/Light wooden shield|light wooden shield]]_, +2 returning _spear_, mwk _battleaxe_, _[[items/Wondrous Item/Cloak of _Resistance_ +2|cloak of _resistance_ +2]]_, lesser belt of mighty hurling, _[[items/Mundane/Holly and mistletoe|holly and mistletoe]]_, exotic military saddle, 10 gp

### Special Abilities

**Colossus _Hunter_ (Ex)** The _[[npcs/Mammoth Rider|mammoth rider]]_ gains a +1 bonus on weapon attack and damage rolls against Large and Huge creatures, and a +2 bonus on weapon attack and damage rolls against Gargantuan and Colossal creatures.

**_Hunter_’s Instinct (Ex)** A _mammoth rider_ gains the quarry class ability; this is exactly like the _[[classes/Ranger|ranger]]_ ability of the same name. She can use this ability on any creature, not just a favored enemy.

**Mistrust of Magic (Ex)** As long as she doesn’t possess any levels in a class that grants her the ability to cast arcane spells, the _mammoth rider_ gains a +2 morale bonus on saving throws against arcane spells.

**Rapid Straddle (Ex)** A _mammoth rider_ can attempt Ride checks to fast _mount_ or fast dismount her steed even if it’s more than one size category larger than her, provided she still has a move action available that round.
**Steed (Ex)** A mammoth lord treats levels in the mammoth lord prestige class as _druid_ levels for the purpose of determining the advancement of her animal companion.

**Undaunted (Ex)** A _mammoth rider_ adds her Strength bonus to the DC of Intimidate checks made against her. Additionally, creatures attempting to intimidate her don’t gain a bonus for being larger than her.

**Wild Coercion (Ex)** A _mammoth rider_’s prestige class levels stack with her _druid_ levels for the purposes of determining the effects of her wild _empathy_ class feature. In addition, a _mammoth rider_ can use her wild _empathy_ to demoralize an animal or magical beast, or force it to be friendly to her, as if using Intimidate rather than Diplomacy. She adds her Strength modifier to these checks in addition to her Charisma modifier.

## Mammoth Steed

Mastodon animal companion (Pathfinder RPG Bestiary 128)
 N Huge animal
 **Init **+2; **Senses **_[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +15

##### Defense

**AC **25, touch 10, _flat-footed_ 23 (+2 Dex, +15 natural, –2 size)
 **hp **115 (10d8+70)
 **Fort **+13, **Ref **+9, **Will **+7 (+4 vs. enchantments); +4 vs. charm, compulsion, and _[[universal monster rules/Fear|fear]]_
 **Defensive Abilities** evasion

##### Offense
**Speed **40 ft.
 **Melee **gore +16 (2d8+11), slam +16 (2d6+11)
 **Space **15 ft.; **Reach **10 ft.
 **Special Attacks **_trample_ (2d8+16, DC 26)

##### Statistics
**Str **32, **Dex **14, **Con **22, **Int **2, **Wis **14, **Cha **7
 **Base Atk** +7; **CMB **+20; **CMD **32 (36 vs. _[[universal monster rules/Trip|trip]]_)
 **Feats **_[[feats/Diehard|Diehard]]_, _Endurance_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_
 **Skills **Perception +15
 **SQ **tricks (attack [all creatures], come, defend, down, fetch, _[[npcs/Guard|guard]]_, heel, perform, stay, work)

In the Realm of the Mammoth Lords, strength is the key to survival, and there’s no greater symbol of that strength than a powerful Kellid warrior astride one of the massive beasts that roam those untamed lands. Though these warrior’s massive mounts are not always mammoths, the rest of the Inner Sea region has long been captivated by this romantic (and terrifying) image, leading to the name of the Mammoth Lords and their followers.

Mammoth riders are fierce hunters and defenders of the lands they call home. Whether part of a “following”—a loose affiliation of individual Kellid families and tribes united under a powerful leader—or loners traveling the wilds with only their gigantic steeds for company, mammoth riders are as much forces of nature as the winds that blast across the Ginji Mesa.

While it might be hard for citizens of southern nations to imagine who in their right minds would challenge a man or woman atop thousands of pounds of fur and tusk, mammoth riders do in fact face numerous foes, ranging from other dangerous megafauna to the giant tribes of the Tusk and Kodar Mountains to demonic forces from the Worldwound to the east. Orcs from Belkzen to the south are also a problem, as the warring tribes also see the value in using megafauna as terrible weapons in battle, and they frequently lead raiding parties into mammoth warrior lands in order to capture the giant creatures. Along the southern borders of their land, most mammoth warriors have a particular hatred for Belkzen invaders, as the orcs’ use of mammoths and other megafauna as engines of war tends to be crude, wasteful, and unnecessarily _[[items/Weapon Magic Abilities/Cruel|cruel]]_ to the animals, creating a dark parody of the mammoth riders themselves.

Along these same lines, mammoths are more than just beasts of burden for their riders. The ability to acquire and train a mammoth is far from universal, and many riders come to value their mounts as friends or even totem animals. A mammoth is a symbol of its rider’s strength of will and prowess in battle, and as such it’s common for riders to decorate their mounts with dyes and warpaint that matches their own, or to pierce or wrap their tusks with rings of metal. Some tribes even engage in elaborate scrimshaw, carving the life stories of each creature’s riders into its tusks.

Mammoth riders can be powerful allies in the rugged lands just south of the Crown of the World. Their survival skills, strength in battle, and strong connection to nature spirits allow them to protect themselves and others against the dangers of the wild. But these same abilities can make them dangerous enemies, and they grow even more dangerous if other tribes add their strength to that of a powerful and respected leader. Further, most mammoth riders are suspicious of outsiders and deeply superstitious about magic, especially when the latter comes from arcane sources. Travelers making their way through the Realm of the Mammoth Lords are wise to enlist local guides to help them placate local rulers and negotiate taboos, lest they find themselves in the path of a stampeding beast or the set _spear_ of a charging rider.