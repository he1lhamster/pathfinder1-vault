---
cssclass: [monsters]
title1: Gremlin, Pugwampi
desc_short: As if the world's most revolting lapdog had somehow learned to walk on
  its back legs, this sickly creature slinks forward carefully.
title2: Pugwampi
CR: 1/2
sources:
- name: Bestiary 2
  page: 144
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
- name: 'Pathfinder #19: Howl of the Carrion King'
  page: 83
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy8735
XP: 200
alignment: NE
size: Tiny
type: fey
initiative:
  bonus: 5
senses:
  darkvision: 120
  low-light vision: true
auras:
- name: unluck
  radius: 20
AC:
  AC: 13
  touch: 13
  flat_footed: 12
  components:
    dex: 1
    size: 2
HP:
  HP: 6
  long: 1d6+3
saves:
  fort: 0
  ref: 3
  will: 4
DR:
- amount: 2
  weakness: cold iron
SR: 7
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +3 (1d2-4/19-20)
      entries:
      - - damage: 1d2-4
          crit_range: 19-20
      attack: dagger
      bonus:
      - 3
  ranged:
  - - text: shortbow +3 (1d3-4/×3)
      entries:
      - - damage: 1d3-4
          crit_multiplier: 3
      attack: shortbow
      bonus:
      - 3
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: prestidigitation
    source: default
    freq: At will
  - name: speak with animals
    source: default
    freq: At will
  - name: shatter
    source: default
    freq: 1/day
    DC: 10
  sources:
  - name: default
    CL: 1
    concentration: -1
ability_scores:
  STR: 3
  DEX: 13
  CON: 11
  INT: 10
  WIS: 14
  CHA: 6
BAB: 0
CMB: -1
CMD: 5
feats:
- name: Improved Initiative
- is_bonus: true
  name: Toughness
- is_bonus: true
  name: Weapon Finesse
skills:
  Bluff: 2
  Craft (traps): 4
  Disable Device: 2
  Perception: 6
    Listening: 2
  Ride: 2
  Stealth: 17
  _racial_mods:
    Stealth:
      _: 4
    Perception:
      when listening: -4
languages:
- Gnoll
- Undercommon
ecology:
  environment: warm hills
  organization: solitary, pair, mob (3-12), or infestation (13-20 with 1-3 druids
    of 1st-3rd level, 1 fighter leader of 2nd-4th level, 2-8 trained stirges, and
    2-5 trained baboons)
  treasure_type: standard
  treasure:
  - dagger
  - shortbow with 20 arrows
  - other treasure
special_abilities:
  Unluck Aura (Su): A pugwampi radiates an aura of unluck to a radius of 20 feet.
    Any creature in this area must roll two d20s whenever a situation calls for a
    d20 roll (such as an attack roll, a skill check, or a saving throw) and must use
    the lower of the two results generated. This is a mind-affecting effect that does
    not work on animals, other gremlins, or gnolls. Any character who gains any sort
    of luck bonus (such as that granted by a luckstone or divine favor) is immune
    to the pugwampi unluck aura.
desc_long: |-
  Mean, dog-faced, and cowardly, pugwampis are loved by no one-not even other gremlins. These gremlins take disproportionate amounts of enjoyment from the accidents and missteps of other creatures, often going to great lengths to manufacture the perfect deadfalls or stumbling blocks. They then wait nearby, both to laugh at the inevitable mishaps and to make sure their personal unluckiness is passed off on their victims.

  Pugwampis live in caves or ruined buildings, occasionally venturing forth to find victims upon which to inflict their sick senses of humor. Their “jokes” tend to involve spikes and excrement, or sometimes pits full of spiders or campsites that flood with swamp water. Certainly only the pugwampis consider their jokes funny. As all pugwampis are somewhat deaf, when not trying to be stealthy, they tend to scream and yell loudly so they can hear themselves and each other.

  At some point in the distant past, pugwampis became enamored of gnolls, seeing in the beast-men a kindred form and thus aspiring to the height and deadly prowess of the savage warriors, whom they honor as gods. Gnolls, for their part, hate pugwampis even more than other creatures, mostly because of the gremlins' weakness and sickening fawning, though they sometimes keep the gremlins around just to torment them.

---

# Gremlin, Pugwampi
As if the world’s most revolting lapdog had somehow learned to walk on its back legs, this sickly creature slinks forward carefully.
**Source** Bestiary 2 pg. 144, Pathfinder #19: Howl of the Carrion _[[npcs/King|King]]_ pg. 83
**XP** 200

NE Tiny fey
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +6
**Aura** _[[curses/Unluck|unluck]]_ (20 ft.)

##### Defense

**AC** 13, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+1 Dex, +2 size)
**hp** 6 (1d6+3)
**Fort** +0, **Ref** +3, **Will** +4
**DR** 2/cold iron; **SR** 7

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +3 (1d2–4/19–20)
**Ranged** _[[items/Weapon/Shortbow|shortbow]]_ +3 (1d3–4/×3)
**Space** 2-1/2 ft., **Reach** 0 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 1st; concentration –1)
At will—_[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
1/day—_[[spells/Shatter|shatter]]_ (DC 10)

##### Statistics
**Str** 3, **Dex** 13, **Con** 11, **Int** 10, **Wis** 14, **Cha** 6
**Base Atk** +0; **CMB** –1; **CMD** 5
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +2, Craft (traps) +4, Disable Device +2, Perception +6 (+2 Listening), Ride +2, Stealth +17; **Racial Modifiers** +4 Stealth, –4 Perception when listening
**Languages** _[[monsters/Gnoll|Gnoll]]_, Undercommon

##### Ecology

**Environment** warm hills
**Organization** solitary, pair, mob (3–12), or infestation (13–20 with 1–3 druids of 1st–3rd level, 1 _[[classes/Fighter|fighter]]_ leader of 2nd–4th level, 2–8 trained stirges, and 2–5 trained baboons)
**Treasure** standard (_dagger_, _shortbow_ with 20 arrows, other treasure)

### Special Abilities

**_Unluck_ Aura (Su) **A pugwampi radiates an aura of _unluck_ to a radius of 20 feet. Any creature in this area must roll two d20s whenever a situation calls for a d20 roll (such as an attack roll, a skill check, or a saving throw) and must use the lower of the two results generated. This is a mind-affecting effect that does not work on animals, other gremlins, or gnolls. Any character who gains any sort of luck bonus (such as that granted by a luckstone or _[[spells/Divine Favor|divine favor]]_) is immune to the pugwampi _unluck_ aura.

##### Description

Mean, dog-faced, and cowardly, pugwampis are loved by no one—not even other gremlins. These gremlins take disproportionate amounts of enjoyment from the accidents and missteps of other creatures, often going to great lengths to manufacture the perfect deadfalls or stumbling blocks. They then wait nearby, both to laugh at the inevitable mishaps and to make sure their personal unluckiness is passed off on their victims.

Pugwampis live in caves or ruined buildings, occasionally venturing forth to find victims upon which to inflict their sick senses of humor. Their “jokes” tend to involve spikes and excrement, or sometimes pits full of spiders or campsites that flood with swamp water. Certainly only the pugwampis consider their jokes funny. As all pugwampis are somewhat deaf, when not trying to be _[[feats/Stealthy|stealthy]]_, they tend to scream and yell loudly so they can hear themselves and each other.

At some point in the distant past, pugwampis became enamored of gnolls, seeing in the beast-men a kindred form and thus aspiring to the height and _[[items/Weapon Magic Abilities/Deadly|deadly]]_ prowess of the savage warriors, whom they honor as gods. Gnolls, for their part, hate pugwampis even more than other creatures, mostly because of the gremlins’ weakness and sickening fawning, though they sometimes keep the gremlins around just to torment them.