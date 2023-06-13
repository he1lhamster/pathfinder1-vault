---
cssclass: [monsters]
title1: Goblin, Goblin Frog-Talker
title2: Goblin Frog-Talker
CR: 5
sources:
- name: Monster Codex
  page: 110
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 1600
race: Goblin
classes:
- witch 6 (Pathfinder RPG Advanced Player's Guide 65)
alignment: NE
size: Small
type: humanoid
subtypes:
- goblinoid
initiative:
  bonus: 3
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 15
  flat_footed: 16
  components:
    armor: 4
    deflection: 1
    dex: 3
    size: 1
HP:
  HP: 47
  long: 6d6+24
saves:
  fort: 5
  ref: 6
  will: 7
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +2 (1d3-2/19-20)
      entries:
      - - damage: 1d3-2
          crit_range: 19-20
      attack: dagger
      bonus:
      - 2
  ranged:
  - - text: javelin +7 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: javelin
      bonus:
      - 7
  special:
  - hexes (evil eye [-2, 6 rounds], misfortune [1 round], mud witch, poison steep,
    swamp hag)
spells:
  entries:
  - name: blink
    source: Witch
    level: 3
  - name: lightning bolt
    source: Witch
    level: 3
    DC: 16
  - superscripts:
    - UM
    name: spit venom
    source: Witch
    level: 3
    DC: 16
  - superscripts:
    - APG
    name: feast of ashes
    source: Witch
    level: 2
    DC: 15
  - superscripts:
    - UC
    name: frost fall
    source: Witch
    level: 2
    DC: 15
  - name: invisibility
    source: Witch
    level: 2
  - superscripts:
    - APG
    name: vomit swarm
    source: Witch
    level: 2
  - name: command
    source: Witch
    level: 1
    DC: 14
  - name: mage armor
    source: Witch
    level: 1
  - name: obscuring mist
    source: Witch
    level: 1
  - name: sleep
    source: Witch
    level: 1
    DC: 14
  - name: dancing lights
    source: Witch
    level: 0
  - name: daze
    source: Witch
    level: 0
    DC: 13
  - name: detect magic
    source: Witch
    level: 0
  - name: touch of fatigue
    source: Witch
    level: 0
    DC: 13
  sources:
  - name: Witch
    type: prepared
    CL: 6
    concentration: 9
    slots:
      0: at-will
    patron: deception
tactics:
  Before Combat: The frog-talker casts mage armor.
  During Combat: A frog-talker uses blink and invisibility to avoid melee opponents,
    and attacks with hexes and ranged spells.
  Base Statistics: Without mage armor, the frog-talker's statistics are AC 15, touch
    15, flat-footed 12.
ability_scores:
  STR: 6
  DEX: 17
  CON: 14
  INT: 16
  WIS: 12
  CHA: 8
BAB: 3
CMB: 0
CMD: 14
feats:
- name: Brew Potion
- name: Extra Hex
- name: Toughness
skills:
  Craft (alchemy): 9
  Intimidate: 8
  Perception: 7
  Ride: 7
  Spellcraft: 12
  Stealth: 17
  Swim: 1
  _racial_mods:
    Ride:
      _: 4
    Stealth:
      _: 4
languages:
- Common
- Giant
- Goblin
- Orc
special_qualities:
- witch's familiar (frog)
gear:
  combat:
  - potion of air bubble
  - potions of alter self (2)
  - potions of cure moderate wounds (3)
  - potion of fly
  - potions of ghostly disguise (2)
  - potion of hex ward
  - alchemist's fire (2)
  - antitoxin (2)
  - smokesticks (2)
  - tanglefoot bags (2)
  other:
  - dagger
  - javelin
  - cloak of resistance +1
  - ring of protection +1
  - delicious poisoned food (1 lb.)
  - 79 gp
ecology:
  environment: temperate forest and plains (usually coastal regions)
desc_long: |-
  Frog-talkers are among the most feared of all goblins; most don't even want to be on the good sides of these witches. Frog-talkers are cruel and fearless masters. It's said the frog-talkers bathe in mud and leeches every fortnight to renew their dedication to their patron, the god of filth and blood-and based on their pale complexions and emaciated frames, few doubt it. These mysterious witches often live alone, or surround themselves with acolytes and terrified goblin minions given to them by superstitious chieftains.

   No two goblins will give you the same answer about why they fear frog-talkers. Some legends claim that the frog-talkers aren't real goblins, but swamp ghosts in disguise. Others claim that they're indeed goblins, but controlled by hideous brain-leeches that have wriggled into their ears. And still others say that worshiping the filth god is scary enough on its own.

   Regardless of what their origins may be, frog-talkers are powerful spellcasters who vomit up swarms of swamp creatures to do their bidding and fry disobedient minions with sizzling lightning. The only mortal creatures a frogtalker seems to truly respect are (naturally) frogs, and most keep a frog or toad on their person at all times. But the most worrying aspect of frog-talkers is that they don't appear to feel fear-an otherwise omnipresent aspect of goblin life.

---

# Goblin, Goblin Frog-Talker

**Source** Monster Codex pg. 110
**XP** 1,600
_[[monsters/Goblin|Goblin]]_ _[[classes/Witch|witch]]_ 6 (Pathfinder RPG Advanced Player’s Guide 65)

NE Small humanoid (goblinoid)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +7

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 armor, +1 deflection, +3 Dex, +1 size)
**hp** 47 (6d6+24)
**Fort** +5, **Ref** +6, **Will** +7

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +2 (1d3–2/19–20)
**Ranged** _[[items/Weapon/Javelin|javelin]]_ +7 (1d4–2)
**Special Attacks** hexes (evil eye [–2, 6 rounds], misfortune [1 round], mud _witch_, poison steep, swamp hag)
**_Witch_ Spells Prepared **(CL 6th; concentration +9)
3rd—_[[spells/Blink|blink]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 16), _[[spells/Spit Venom|spit venom]]_ (DC 16)
2nd—_[[spells/Feast Of Ashes|feast of ashes]]_ (DC 15), _[[spells/Frost Fall|frost fall]]_ (DC 15), _[[spells/Invisibility|invisibility]]_, _[[spells/Vomit Swarm|vomit swarm]]_
1st—_[[spells/Command|command]]_ (DC 14), _[[spells/Mage Armor|mage armor]]_, _[[spells/Obscuring Mist|obscuring mist]]_, sleep (DC 14)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 13), _[[spells/Detect Magic|detect magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 13)
**Patron** deception

### Tactics

**Before Combat** The frog-talker casts _mage armor_.
 **During Combat** A frog-talker uses _blink_ and _invisibility_ to avoid melee opponents, and attacks with hexes and ranged spells.
 **Base Statistics** Without _mage armor_, the frog-talker’s statistics are **AC **15, touch 15, _flat-footed_ 12.

##### Statistics
**Str** 6, **Dex** 17, **Con** 14, **Int** 16, **Wis** 12, **Cha** 8
**Base Atk** +3; **CMB** +0; **CMD** 14
**Feats** _[[feats/Brew Potion|Brew Potion]]_, _[[feats/Extra Hex|Extra Hex]]_, _[[feats/Toughness|Toughness]]_
**Skills** Craft (alchemy) +9, Intimidate +8, Perception +7, Ride +7, Spellcraft +12, Stealth +17, Swim +1; **Racial Modifiers** +4 Ride, +4 Stealth
**Languages** Common, Giant, _Goblin_, _[[monsters/Orc|Orc]]_
**SQ** _witch_’s familiar (frog)
**Combat Gear** potion of _[[spells/Air Bubble|air bubble]]_, potions of _[[spells/Alter Self|alter self]]_ (2), potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (3), potion of fly, potions of _[[spells/Ghostly Disguise|ghostly disguise]]_ (2), potion of _[[spells/Hex Ward|hex ward]]_, _[[classes/Alchemist|alchemist]]_’s fire (2), _[[items/Mundane/Antitoxin|antitoxin]]_ (2), smokesticks (2), tanglefoot bags (2); **Other Gear** _dagger_, _javelin_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, delicious poisoned food (1 lb.), 79 gp

##### Ecology

**Environment** temperate forest and plains (usually coastal regions)

##### Description

Frog-talkers are among the most feared of all goblins; most don’t even want to be on the good sides of these witches. Frog-talkers are _[[items/Weapon Magic Abilities/Cruel|cruel]]_ and fearless masters. It’s said the frog-talkers bathe in mud and leeches every fortnight to renew their dedication to their patron, the god of filth and blood—and based on their pale complexions and emaciated frames, few doubt it. These mysterious witches often live alone, or surround themselves with acolytes and terrified _goblin_ minions given to them by superstitious chieftains.

No two goblins will give you the same answer about why they _[[universal monster rules/Fear|fear]]_ frog-talkers. Some legends claim that the frog-talkers aren’t real goblins, but swamp ghosts in disguise. Others claim that they’re indeed goblins, but controlled by hideous brain-leeches that have wriggled into their ears. And still others say that worshiping the filth god is scary enough on its own.

Regardless of what their origins may be, frog-talkers are powerful spellcasters who vomit up swarms of swamp creatures to do their bidding and fry disobedient minions with sizzling lightning. The only mortal creatures a frogtalker seems to truly respect are (naturally) frogs, and most keep a frog or toad on their person at all times. But the most worrying aspect of frog-talkers is that they don’t appear to feel _fear_—an otherwise omnipresent aspect of _goblin_ life.