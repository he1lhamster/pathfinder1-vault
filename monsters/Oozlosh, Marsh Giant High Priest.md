---
cssclass: [monsters]
title1: Oozlosh, Marsh Giant High Priest
desc_short: This creature has the bulbous eyes of a fish, and his mottled green skin
  glistens with slime where it isn't bedecked in gaudy jewelry.
title2: Oozlosh, Marsh Giant High Priest
CR: 14
sources:
- name: Giants Revisited
  page: 38
  link: http://paizo.com/products/btpy8rv4?Pathfinder-Campaign-Setting-Giants-Revisited
XP: 38400
race: Male
classes:
- marsh giant cleric of Dagon 10
alignment: CE
size: Large
type: humanoid
subtypes:
- giant
initiative:
  bonus: 8
senses:
  low-light vision: true
AC:
  AC: 28
  touch: 15
  flat_footed: 24
  components:
    armor: 3
    deflection: 2
    dex: 4
    natural: 10
    size: -1
HP:
  HP: 209
  long: 12d8+10d8+110
  HD: 22
saves:
  fort: 21
  ref: 12
  will: 18
defensive_abilities:
- rock catching
resistances:
  cold: 10
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 trident +23/+18/+13/+8 (2d6+8)
      entries:
      - - damage: 2d6+8
      attack: +1 trident
      bonus:
      - 23
      - 18
      - 13
      - 8
  - - text: 2 slams +22 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 2
      attack: slams
      bonus:
      - 22
  ranged:
  - - text: rock +19 (1d8+7)
      entries:
      - - damage: 1d8+7
      attack: rock
      bonus:
      - 19
  special:
  - channel negative energy 7/day (DC 19, 5d6)
  - rock throwing (120 ft.)
  - scythe of evil (5 rounds, 1/day)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: augury
    source: default
    freq: 3/day
  - name: bestow curse
    source: default
    freq: 3/day
    DC: 16
  - name: fog cloud
    source: default
    freq: 3/day
  - name: touch of evil
    source: domain
    freq: 9/day
    other: 5 rounds
  - name: icicle
    source: domain
    freq: 9/day
    other: 1d6+5 cold damage
  sources:
  - name: default
    CL: 12
    concentration: 14
  - name: domain
    CL: 10
    concentration: 16
spells:
  entries:
  - is_domain_spell: true
    name: ice storm
    source: Cleric
    level: 5
  - name: insect plague
    source: Cleric
    level: 5
  - name: snake staff
    source: Cleric
    level: 5
  - name: summon monster V
    source: Cleric
    level: 5
  - name: chaos hammer
    source: Cleric
    level: 4
    DC: 20
  - is_domain_spell: true
    name: control water
    source: Cleric
    level: 4
  - name: plague carrier
    source: Cleric
    level: 4
    DC: 20
  - name: spit venom
    source: Cleric
    level: 4
    DC: 20
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 20
  - name: badger's ferocity
    source: Cleric
    level: 3
  - name: deeper darkness
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: water breathing
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: align weapon
    source: Cleric
    level: 2
    other: evil only
  - name: death knell
    source: Cleric
    level: 2
    DC: 18
  - name: dread bolt
    source: Cleric
    level: 2
    DC: 18
  - name: grace
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 18
  - name: silence
    source: Cleric
    level: 2
    DC: 18
  - name: spiritual weapon
    source: Cleric
    level: 2
  - name: cause fear
    source: Cleric
    level: 1
    DC: 17
  - name: doom
    source: Cleric
    level: 1
    DC: 17
  - name: entropic shield
    source: Cleric
    level: 1
  - name: magic stone
    source: Cleric
    level: 1
  - name: murderous command
    source: Cleric
    level: 1
    DC: 17
  - is_domain_spell: true
    name: protection from good
    source: Cleric
    level: 1
  - name: ray of sickening
    source: Cleric
    level: 1
    DC: 17
  - name: bleed
    source: Cleric
    level: 0
    DC: 16
  - name: guidance
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
    CL: 10
    concentration: 16
    slots:
      0: at-will
    domains:
    - evil
    - water
ability_scores:
  STR: 25
  DEX: 19
  CON: 21
  INT: 12
  WIS: 23
  CHA: 14
BAB: 16
CMB: 24
CMB_other: +26 sunder
CMD: 40
feats:
- name: Channel Smite
- name: Cleave
- name: Combat Reflexes
- name: Extra Channel
- name: Improved Channel
- name: Improved Initiative
- name: Improved Sunder
- name: Power Attack
- name: Quicken Spell
- name: Selective Channeling
- name: Vital Strike
skills:
  Knowledge (religion): 19
  Perception: 24
  Spellcraft: 19
  Stealth: 16
    in swamps: 24
  Swim: 30
  _racial_mods:
    Stealth:
      in swamps: 8
languages:
- Boggard
- Common
- Giant
gear:
  combat:
  - necklace of fireballs (type II)
  - potions of cure serious wounds (2)
  other:
  - +1 trident
  - amulet of natural armor +1
  - bracers of armor +3
  - belt of incredible dexterity +2
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - ring of protection +2
  - wooden unholy symbol of Dagon
desc_long: |-
  The grotesque marsh giant known as Oozlosh is the high priest of a large tribe in Varisia's Mushfens. His reputation has spread throughout the entire wetlands, and he regards himself as the unofficial ruler of all marsh giants in that wild region. He earned notoriety by bringing many goblins in southern Varisia under his heel and establishing relations with the swamp's boggards. Little occurs among the marsh giants of the Mushfens that the high priest does not command (or at least tolerate).

  The Mushfens are bordered on the south by Conqueror's Bay, forming a long coastline where the brutes practice their frightening rituals to Dagon. They are visited often by the demon lord's sea-spawn, resulting in many births of deformed brineborn. One of Dagon's horrific emissaries stays with Oozlosh's tribe occasionally, reveling in the giants' vulgar devotion. It has tasked Oozlosh with safeguarding the tribe's brineborn until they are called to fulfill a dark purpose, a secret the high priest guards with his life.

  Oozlosh's zealotry for Dagon knows no bounds. He debases himself physically to honor the demon lord and expects his followers to do the same. The high priest's swamp hovel is not grand, but in the muck around his shack, he secretly conceals prizes scavenged from the tribe's victims. Oozlosh also keeps a cage of shocker lizards outside his home, having become addicted to the jolts he receives when chewing the creatures.

---

# Oozlosh, Marsh Giant High Priest
This creature has the bulbous eyes of a fish, and his mottled green skin glistens with slime where it isn’t bedecked in gaudy _[[items/Mundane/Jewelry|jewelry]]_.
**Source** Giants Revisited pg. 38
**XP** 38,400
Male marsh giant _[[classes/Cleric|cleric]]_ of Dagon 10
CE Large humanoid (giant)
**Init** +8; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +24

##### Defense

**AC** 28, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+3 armor, +2 deflection, +4 Dex, +10 natural, –1 size)
**hp** 209 (22 HD; 12d8+10d8+110)
**Fort** +21, **Ref** +12, **Will** +18
**Defensive Abilities** _[[universal monster rules/Rock Catching|rock catching]]_; **Resist** cold 10

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Trident|trident]]_ +23/+18/+13/+8 (2d6+8) or 2 slams +22 (1d6+7)
**Ranged** rock +19 (1d8+7)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** channel negative energy 7/day (DC 19, 5d6), _[[universal monster rules/Rock Throwing|rock throwing]]_ (120 ft.), _[[items/Weapon/Scythe|scythe]]_ of evil (5 rounds, 1/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +14)
3/day—_[[spells/Augury|augury]]_, _[[spells/Bestow Curse|bestow curse]]_ (DC 16), _[[spells/Fog Cloud|fog cloud]]_
**Domain _Spell-Like Abilities_ **(CL 10th; concentration +16)
9/day—_[[feats/Touch Of Evil|touch of evil]]_ (5 rounds)
9/day—icicle (1d6+5 cold damage)
**_Cleric_ Spells Prepared **(CL 10th; concentration +16)
5th—_[[spells/Ice Storm|ice storm]]_, _[[spells/Insect Plague|insect plague]]_, _[[spells/Snake Staff|snake staff]]_*, _[[spells/Summon Monster V|summon monster V]]_
4th—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 20), _[[spells/Control Water|control water]]_, _[[spells/Plague Carrier|plague carrier]]_** (DC 20), _[[spells/Spit Venom|spit venom]]_** (DC 20), _[[spells/Unholy Blight|unholy blight]]_ (DC 20)
3rd—_[[monsters/Badger|badger]]_’s _[[universal monster rules/Ferocity|ferocity]]_**, _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Prayer|prayer]]_, _[[universal monster rules/Water Breathing|water breathing]]_
2nd—_[[spells/Align Weapon|align weapon]]_ (evil only), _[[spells/Death Knell|death knell]]_ (DC 18), _[[spells/Dread Bolt|dread bolt]]_** (DC 18), _[[spells/Grace|grace]]_*, _[[spells/Hold Person|hold person]]_ (DC 18), _[[spells/Silence|silence]]_ (DC 18), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Cause Fear|cause fear]]_ (DC 17), _[[spells/Doom|doom]]_ (DC 17), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Magic Stone|magic stone]]_, _[[spells/Murderous Command|murderous command]]_** (DC 17), _[[spells/Protection From Good|protection from good]]_, _[[spells/Ray of Sickening|ray of sickening]]_** (DC 17)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**D **Domain spell; **Domains **Evil, Water
* See the Advanced Player’s Guide.
** See Ultimate Magic.

##### Statistics
**Str** 25, **Dex** 19, **Con** 21, **Int** 12, **Wis** 23, **Cha** 14
**Base Atk** +16; **CMB** +24 (+26 sunder); **CMD** 40
**Feats** _[[feats/Channel Smite|Channel Smite]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Knowledge (religion) +19, Perception +24, Spellcraft +19, Stealth +16 (+24 in swamps), Swim +30; **Racial Modifiers** +8 Stealth in swamps
**Languages** _[[monsters/Boggard|Boggard]]_, Common, Giant
**Combat Gear** necklace of fireballs (type II), potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2); **Other Gear** +1 _trident_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Bracers of Armor +3|bracers of armor +3]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +2|belt of incredible dexterity +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, wooden _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol of Dagon

##### Description

The grotesque marsh giant known as Oozlosh is the high priest of a large tribe in Varisia’s Mushfens. His reputation has spread throughout the entire wetlands, and he regards himself as the unofficial ruler of all marsh giants in that wild region. He earned notoriety by bringing many goblins in southern Varisia under his heel and establishing relations with the swamp’s boggards. Little occurs among the marsh giants of the Mushfens that the high priest does not _[[spells/Command|command]]_ (or at least tolerate).

The Mushfens are bordered on the south by Conqueror’s Bay, forming a long coastline where the brutes practice their frightening rituals to Dagon. They are visited often by the demon lord’s sea-spawn, resulting in many births of deformed brineborn. One of Dagon’s horrific emissaries stays with Oozlosh’s tribe occasionally, reveling in the giants’ vulgar devotion. It has tasked Oozlosh with safeguarding the tribe’s brineborn until they are _[[items/Weapon Magic Abilities/Called|called]]_ to fulfill a dark purpose, a secret the high priest guards with his life.

Oozlosh’s zealotry for Dagon knows no bounds. He debases himself physically to honor the demon lord and expects his followers to do the same. The high priest’s swamp hovel is not grand, but in the muck around his shack, he secretly conceals prizes scavenged from the tribe’s victims. Oozlosh also keeps a cage of shocker lizards outside his home, having become addicted to the jolts he receives when chewing the creatures.