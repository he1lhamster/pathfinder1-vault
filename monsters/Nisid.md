---
cssclass: [monsters]
title1: Nisid
desc_short: This small, naked creature looks like a lithe halfling, but with long,
  tapered ears and tough, brown skin. His hair is unkempt and his flesh is weathered,
  but his large eyes glitter violet.
title2: Nisid
CR: 4
sources:
- name: 'Pathfinder #122: Into the Shattered Continent'
  page: 83
  link: http://paizo.com/products/btpy9uk0?Pathfinder-Adventure-Path-122-Into-the-Shattered-Continent
XP: 1200
alignment: CG
size: Small
type: fey
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 17
  touch: 14
  flat_footed: 14
  components:
    dex: 3
    natural: 3
    size: 1
HP:
  HP: 33
  long: 6d6+12
saves:
  fort: 4
  ref: 8
  will: 8
DR:
- amount: 5
  weakness: cold iron
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +7 (1d3-1/19-20)
      entries:
      - - damage: 1d3-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 7
  - - text: spear +3 (1d6-1/×3)
      entries:
      - - damage: 1d6-1
          crit_multiplier: 3
      attack: spear
      bonus:
      - 3
  ranged:
  - - text: longbow +7 (1d6/×3)
      entries:
      - - damage: 1d6
          crit_multiplier: 3
      attack: longbow
      bonus:
      - 7
  - - text: spear +7 (1d6-1/×3)
      entries:
      - - damage: 1d6-1
          crit_multiplier: 3
      attack: spear
      bonus:
      - 7
spell_like_abilities:
  entries:
  - name: charm animal
    source: default
    freq: At will
    DC: 15
  - name: create water
    source: default
    freq: At will
  - name: endure elements
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: 3/day
    DC: 16
  - name: entangle
    source: default
    freq: 3/day
    DC: 15
  - name: invisibility
    source: default
    freq: 3/day
    other: self only
  - name: call lightning
    source: default
    freq: 1/day
    DC: 17
  - name: confusion
    source: default
    freq: 1/day
    DC: 18
  - name: gust of wind
    source: default
    freq: 1/day
    DC: 16
  - name: hallucinatory terrain
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 6
    concentration: 10
ability_scores:
  STR: 9
  DEX: 16
  CON: 15
  INT: 13
  WIS: 16
  CHA: 18
BAB: 3
CMB: 1
CMD: 14
feats:
- name: Alertness
- name: Self-Sufficient
- name: Weapon Finesse
skills:
  Bluff: 13
  Climb: 8
  Heal: 5
  Knowledge (geography): 7
  Knowledge (nature): 7
  Perception: 14
  Sense Motive: 14
  Stealth: 16
  Survival: 18
  _racial_mods:
    Survival:
      _: 4
languages:
- Common
- Sylvan
special_qualities:
- island bond
- isolation
- never come back
ecology:
  environment: any island
  organization: solitary
  treasure_type: double
  treasure:
  - dagger
  - spear
  - longbow with 20 arrows
  - other treasure
special_abilities:
  Island Bond (Ex): A nisid who resides on a small, uninhabited island for an extended
    period of time forms a strong bond with the land, gaining a number of powers meant
    to protect the sanctity of its territory. The island must be no larger than 1
    square mile in area per Hit Die the nisid has (usually 6 HD), and the nisid must
    be the only intelligent creature on the island for 1 uninterrupted year to cement
    the bond. After the bond has been formed, the nisid gains the isolation and never
    come back abilities (see below), and receives a +4 racial bonus on Survival checks
    while on his island. A nisid who leaves his island for more than 1 hour per Hit
    Die or whose island is inhabited by an intelligent creature for longer than 1
    month per Hit Die loses its island bond and must restart the bonding process,
    either on a new island or on the same island once all prerequisite conditions
    are met.
  Isolation (Su): A trespasser on the nisid's bonded island must succeed at a DC 17
    Will save every full day she remains on the island or she takes 1d2 points of
    Wisdom damage as the nisid magnifies the trials of survival on an uninhabited
    and dangerous island with little hope of rescue. This Wisdom damage does not heal
    naturally until the trespasser leaves the nisid's island (though it can be healed
    through magic normally), slowly driving her mad. The nisid can suppress this ability
    at will; typically, it does so until it determines the trespasser will not soon
    leave of her own volition or is otherwise going to be trouble. This is a mind-affecting
    curse effect. The saving throw DC is Charisma-based.
  Never Come Back (Su): The nisid's ties to its island help keep it hidden from repeat
    visits, ensuring that even trespassers who want to return find doing so difficult.
    When a trespasser leaves a nisid's bonded island, she must attempt a DC 17 Will
    saving throw. Failure results in her memories of the place becoming hazy-especially
    when it comes to locating it again. She takes a -10 penalty on Survival and Knowledge
    (geography) checks to determine the island's location or find it again, and the
    island and the nisid are treated as though under the effects of a permanent nondetection
    spell for any divination spells the target casts (use the nisid's caster level
    to determine the difficulty of overcoming this effect). This is a mind-affecting
    curse effect. The save DC is Charisma-based.
desc_long: |-
  Nisids are castaway spirits, protectors of uninhabited or deserted islands. These little fey look like they might once have maintained a more delicate and youthful appearance, but after having spent decades or centuries alone, they look haggard, with unkempt hair and tough skin. Nisids rarely wear clothing, as they have little need for modesty or protection. They are excellent survivalists, living off what their island can provide.

   Loners by nature, a nisid claims and forms a bond with a single uninhabited island as his territory, and he seeks to preserve the island's untouched sanctity-and his own solitude. Should someone happen upon a nisid's island, whether as a castaway, stranded by a storm, or deliberately seeking something, the nisid first spies on the interloper using invisibility and detect thoughts to assess her intent. If he determines that the trespasser simply wishes to get off the island, the nisid often offers to help his guest survive and escape (if only to hasten the process and return the island to its isolation). Using magic and his natural skill at survival, he may give the castaway access to water, food, or shelter-in exchange for leaving the island unsullied when she leaves. Those who agree and please the nisid might even be gifted with a final gust of wind to send them on their way.

   However, those who arrive with no intention of leaving hastily, or who drastically overstay their welcome without hope of escape, find the nisid a more hostile host, as a nisid finds murder a small price to pay for solitude. Unwelcome guests find the trials of survival and hopelessness to be maddening, and every day drift closer to insanity through the nisid's isolation ability. Once the trespassers have been driven toward madness, the nisid attempts to turn them against each other, sowing distrust and casting confusion on large groups. If all else fails, the nisid might coax charmed animals, the nisid's only companions, into attacking interlopers: nothing says “get off my island” like a giant beast crashing out of the jungle.

   With no desire to die-only to be left alone-the nisid eschews direct combat as much as possible, preferring to have his enemies deal with each other or succumb to the dangers of the island itself. If pushed to combat, he casts call lightning and attempts to strike down his enemies from hiding, using his knowledge of the island to his advantage.

   Even when helping agreeable castaways, the nisid won't make life too easy, lest the trespassers decide to extend their stay. He makes just enough food and water available to sustain the “guests,” using abilities like hallucinatory terrain to keep any particularly bountiful areas of the island hidden. Should the island be a truly deserted one, perhaps where an ancient civilization once flourished, a nisid is especially vigilant in keeping ruins or artifacts that could attract further interest in the island well hidden. And once a castaway leaves a nisid's island, she rarely finds a way to return.

   A typical nisid stands 4 feet tall and weighs 70 pounds.

---

# Nisid
This small, naked creature looks like a lithe halfling, but with long, tapered ears and tough, brown skin. His hair is unkempt and his flesh is weathered, but his large eyes glitter violet.
**Source** Pathfinder #122: Into the Shattered Continent pg. 83
**XP** 1,200

CG Small fey
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14

##### Defense

**AC** 17, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 Dex, +3 natural, +1 size)
**hp** 33 (6d6+12)
**Fort** +4, **Ref** +8, **Will** +8
**DR** 5/cold iron

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +7 (1d3–1/19–20) or _[[items/Weapon/Spear|spear]]_ +3 (1d6–1/×3)
**Ranged** _[[items/Weapon/Longbow|longbow]]_ +7 (1d6/×3) or _spear_ +7 (1d6–1/×3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +10)
At will—_[[spells/Charm Animal|charm animal]]_ (DC 15), _[[spells/Create Water|create water]]_, _[[spells/Endure Elements|endure elements]]_ 
3/day—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), _[[spells/Entangle|entangle]]_ (DC 15), _[[spells/Invisibility|invisibility]]_ (self only) 
1/day—_[[spells/Call Lightning|call lightning]]_ (DC 17), _[[spells/Confusion|confusion]]_ (DC 18), _[[spells/Gust Of Wind|gust of wind]]_ (DC 16), _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 18)

##### Statistics
**Str** 9, **Dex** 16, **Con** 15, **Int** 13, **Wis** 16, **Cha** 18
**Base Atk** +3; **CMB** +1; **CMD** 14
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Self-Sufficient|Self-Sufficient]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +13, _[[universal monster rules/Climb|Climb]]_ +8, _[[spells/Heal|Heal]]_ +5, Knowledge (geography, nature) +7, Perception +14, Sense Motive +14, Stealth +16, Survival +18; **Racial Modifiers** +4 Survival
**Languages** Common, Sylvan
**SQ** island bond, isolation, never come back

##### Ecology

**Environment** any island
**Organization** solitary
**Treasure** double (_dagger_, _spear_, _longbow_ with 20 arrows, other treasure)

### Special Abilities

**Island Bond (Ex)** A _[[monsters/Nisid|nisid]]_ who resides on a small, uninhabited island for an extended period of time forms a strong bond with the land, gaining a number of powers meant to protect the sanctity of its territory. The island must be no larger than 1 square mile in area per Hit Die the _nisid_ has (usually 6 HD), and the _nisid_ must be the only intelligent creature on the island for 1 uninterrupted year to cement the bond. After the bond has been formed, the _nisid_ gains the isolation and never come back abilities (see below), and receives a +4 racial bonus on Survival checks while on his island. A _nisid_ who leaves his island for more than 1 hour per Hit Die or whose island is inhabited by an intelligent creature for longer than 1 month per Hit Die loses its island bond and must restart the bonding process, either on a new island or on the same island once all prerequisite conditions are met.

**Isolation (Su)** A trespasser on the _nisid_’s bonded island must succeed at a DC 17 Will save every full day she remains on the island or she takes 1d2 points of Wisdom damage as the _nisid_ magnifies the trials of survival on an uninhabited and dangerous island with little hope of rescue. This Wisdom damage does not _heal_ naturally until the trespasser leaves the _nisid_’s island (though it can be healed through magic normally), slowly driving her mad. The _nisid_ can suppress this ability at will; typically, it does so until it determines the trespasser will not soon leave of her own volition or is otherwise going to be trouble. This is a mind-affecting curse effect. The saving throw DC is Charisma-based.

**Never Come Back (Su)** The _nisid_’s ties to its island help keep it hidden from repeat visits, ensuring that even trespassers who want to return find doing so difficult. When a trespasser leaves a _nisid_’s bonded island, she must attempt a DC 17 Will saving throw. Failure results in her memories of the place becoming hazy—especially when it comes to locating it again. She takes a –10 penalty on Survival and Knowledge (geography) checks to determine the island’s location or find it again, and the island and the _nisid_ are treated as though under the effects of a permanent _[[spells/Nondetection|nondetection]]_ spell for any _[[spells/Divination|divination]]_ spells the target casts (use the _nisid_’s caster level to determine the difficulty of overcoming this effect). This is a mind-affecting curse effect. The save DC is Charisma-based.

##### Description

Nisids are _[[npcs/Castaway|castaway]]_ spirits, protectors of uninhabited or deserted islands. These little fey look like they might once have maintained a more delicate and _[[spells/Youthful Appearance|youthful appearance]]_, but after having spent decades or centuries alone, they look haggard, with unkempt hair and tough skin. Nisids rarely wear clothing, as they have little need for modesty or protection. They are excellent survivalists, living off what their island can provide.

Loners by nature, a _nisid_ claims and forms a bond with a single uninhabited island as his territory, and he seeks to _[[spells/Preserve|preserve]]_ the island’s untouched sanctity—and his own solitude. Should someone happen upon a _nisid_’s island, whether as a _castaway_, stranded by a storm, or deliberately seeking something, the _nisid_ first spies on the interloper using _invisibility_ and _detect thoughts_ to assess her intent. If he determines that the trespasser simply wishes to get off the island, the _nisid_ often offers to help his guest survive and escape (if only to hasten the process and return the island to its isolation). Using magic and his natural skill at survival, he may give the _castaway_ access to water, food, or shelter—in exchange for leaving the island unsullied when she leaves. Those who agree and please the _nisid_ might even be gifted with a final _gust of wind_ to send them on their way.

However, those who arrive with no intention of leaving hastily, or who drastically overstay their welcome without hope of escape, find the _nisid_ a more hostile host, as a _nisid_ finds murder a small price to pay for solitude. Unwelcome guests find the trials of survival and hopelessness to be maddening, and every day drift closer to _[[spells/Insanity|insanity]]_ through the _nisid_’s isolation ability. Once the trespassers have been driven toward madness, the _nisid_ attempts to turn them against each other, sowing distrust and casting _confusion_ on large groups. If all else fails, the _nisid_ might coax charmed animals, the _nisid_’s only companions, into attacking interlopers: nothing says “get off my island” like a giant beast crashing out of the jungle.

With no desire to die—only to be left alone—the _nisid_ eschews direct combat as much as possible, preferring to have his enemies deal with each other or succumb to the dangers of the island itself. If pushed to combat, he casts _call lightning_ and attempts to strike down his enemies from hiding, using his knowledge of the island to his advantage.

Even when helping agreeable castaways, the _nisid_ won’t make life too easy, lest the trespassers decide to extend their stay. He makes just enough food and water available to sustain the “guests,” using abilities like _hallucinatory terrain_ to keep any particularly bountiful areas of the island hidden. Should the island be a truly deserted one, perhaps where an ancient civilization once flourished, a _nisid_ is especially _[[items/Armor Magic Abilities/Vigilant|vigilant]]_ in keeping ruins or artifacts that could attract further interest in the island well hidden. And once a _castaway_ leaves a _nisid_’s island, she rarely finds a way to return.

A typical _nisid_ stands 4 feet tall and weighs 70 pounds.