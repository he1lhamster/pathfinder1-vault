---
cssclass: [monsters]
title1: Brain Ooze
desc_short: Two slimy tentacles protrude from the sides of this brain-shaped mass
  of quivering ooze.
title2: Brain Ooze
CR: 7
sources:
- name: Bestiary 3
  page: 43
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 3200
alignment: NE
size: Tiny
type: ooze
initiative:
  bonus: 6
senses:
  blindsight: 60
auras:
- name: psychic noise
  radius: 10
  DC: 19
AC:
  AC: 23
  touch: 19
  flat_footed: 18
  components:
    armor: 4
    dex: 4
    dodge: 1
    insight: 2
    size: 2
HP:
  HP: 75
  long: 10d8+30
saves:
  fort: 6
  ref: 9
  will: 6
defensive_abilities:
- evasion
- prescience
immunities:
- ooze traits
speeds:
  base: 5
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 tentacles +13 touch (1d6 electricity plus neural pulse)
      entries:
      - - damage: 1d6
          type: electricity
        - effect: neural pulse
      count: 2
      attack: tentacles
      bonus:
      - 13
      touch: true
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: detect thoughts
    source: default
    freq: Constant
  - name: mage armor
    source: default
    freq: Constant
  - name: charm monster
    source: default
    freq: At will
    DC: 18
  - name: dominate animal
    source: default
    freq: At will
    DC: 17
  - name: dominate person
    source: default
    freq: At will
    DC: 19
  - name: dispel magic
    source: default
    freq: 3/day
  - name: modify memory
    source: default
    freq: 3/day
    DC: 18
  sources:
  - name: default
    CL: 10
    concentration: 14
ability_scores:
  STR: 4
  DEX: 19
  CON: 16
  INT: 15
  WIS: 12
  CHA: 19
BAB: 7
CMB: 9
CMD: 22
CMD_other: can't be tripped
feats:
- name: Defensive Training
- name: Dodge
- name: Iron Will
- name: Mobility
- name: Weapon Finesse
skills:
  Bluff: 10
  Diplomacy: 5
  Fly: 25
  Perception: 11
  Sense Motive: 11
  Stealth: 15
languages:
- Aklo (cannot speak)
- telepathy 100 ft.
ecology:
  environment: any ruins or underground
  organization: solitary, pair, flight (3-6), or colony (7-12)
  treasure_type: incidental
special_abilities:
  Neural Pulse (Su): Creatures hit by a brain ooze's tentacle must succeed at a DC
    18 Fortitude save or take 1d6 points of Intelligence damage and be staggered for
    1d4 rounds. Each time a brain ooze causes Intelligence damage, it gains 5 temporary
    hit points. The save DC is Constitution-based.
  Prescience (Su): Limited precognitive abilities grant a brain ooze a +2 insight
    bonus on initiative checks, on Reflex saves, and to its Armor Class. Brain oozes
    are never surprised or flat-footed.
  Psychic Noise (Su): The discordant psychic noise emitted by a brain ooze dazes nearby
    creatures for 1d4 rounds. When a creature begins its turn within the aura, it
    must succeed at a DC 19 Will save to negate this effect. Whether or not the save
    is successful, that creature cannot be affected again by the same brain ooze's
    psychic noise for 24 hours. An affected creature may attempt a new save to shake
    off the effect at the end of each of its turns. This is a mind-affecting effect.
    The save DC is Charisma-based.
desc_long: |-
  A brain ooze (sometimes known as a “killer brain”) resembles almost precisely the raw brain of a human, save for the eldritch energy surrounding it and the twin tentacles extending from its sides. The creature's thought patterns are unusually powerful, and cause painful mental feedback in the minds of other conscious beings.

  Other intelligent beings are nothing more than cattle and playthings to brain oozes-victims to be tormented, thought patterns to be consumed. Brain oozes prefer to manipulate their prey from the shadows. Rather than assaulting openly, they provoke fights and conflict within groups, or lure one or two victims away for the kill. Brain oozes derive particular satisfaction from forcing an individual to commit terrible acts, then wiping away all knowledge of the crimes from the victim's memory. They torment such hapless puppets again and again, forcing them to commit ever greater atrocities. Once weary of their sport they return the modified memories with dispel magic, and feast upon the delicious misery of the victim's final despair.

  Brain oozes feed through their tentacles by extracting the thoughts of living creatures. Animals and less intelligent creatures provide little nourishment, but they prize fey, outsiders, and spellcasters as delicacies. After several feedings, a brain ooze divides into two nearly identical brains, each retaining only a portion of the knowledge and experiences of the parent.

  The similarities between intellect devourers and brain oozes have not gone unnoticed, but the two species appear to have little in common beyond appearance. Some theorize that brain oozes are actually the result of an ancient race's failed attempt to achieve immortality by preserving their minds via alien technology or magic.

---

# Brain Ooze
Two slimy tentacles protrude from the sides of this brain-shaped mass of quivering ooze.
**Source** Bestiary 3 pg. 43
**XP** 3,200

NE Tiny ooze
**Init** +6; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 60 ft.; Perception +11
**Aura** _[[classes/Psychic|psychic]]_ noise (10 ft., DC 19)

##### Defense

**AC** 23, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +4 Dex, +1 dodge, +2 insight, +2 size)
**hp** 75 (10d8+30)
**Fort** +6, **Ref** +9, **Will** +6
**Defensive Abilities** evasion, prescience; **Immune** ooze traits

##### Offense
**Speed** 5 ft., fly 60 ft. (good)
**Melee** 2 tentacles +13 touch (1d6 electricity plus neural pulse)
**Space** 2-1/2 feet, **Reach** 0 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
Constant—_[[spells/Detect Thoughts|detect thoughts]]_, _[[spells/Mage Armor|mage armor]]_
At will—_[[spells/Charm Monster|charm monster]]_ (DC 18), _[[spells/Dominate Animal|dominate animal]]_ (DC 17), _[[spells/Dominate Person|dominate person]]_ (DC 19)
3/day—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Modify Memory|modify memory]]_ (DC 18)

##### Statistics
**Str** 4, **Dex** 19, **Con** 16, **Int** 15, **Wis** 12, **Cha** 19
**Base Atk** +7; **CMB** +9; **CMD** 22 (can’t be tripped)
**Feats** Defensive _[[items/Weapon Magic Abilities/Training|Training]]_, _Dodge_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +10, Diplomacy +5, Fly +25, Perception +11, Sense Motive +11, Stealth +15
**Languages** Aklo (cannot speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any ruins or underground
**Organization** solitary, pair, _[[universal monster rules/Flight|flight]]_ (3–6), or colony (7–12)
**Treasure** incidental

### Special Abilities

**Neural Pulse (Su)** Creatures hit by a _[[monsters/Brain Ooze|brain ooze]]_’s tentacle must succeed at a DC 18 Fortitude save or take 1d6 points of Intelligence damage and be _[[conditions/Staggered|staggered]]_ for 1d4 rounds. Each time a _brain ooze_ causes Intelligence damage, it gains 5 temporary hit points. The save DC is Constitution-based.

**Prescience (Su)** Limited precognitive abilities grant a _brain ooze_ a +2 insight bonus on initiative checks, on Reflex saves, and to its Armor Class. Brain oozes are never surprised or _flat-footed_.

**_Psychic_ Noise (Su) **The discordant _psychic_ noise emitted by a _brain ooze_ dazes nearby creatures for 1d4 rounds. When a creature begins its turn within the aura, it must succeed at a DC 19 Will save to negate this effect. Whether or not the save is successful, that creature cannot be affected again by the same _brain ooze_’s _psychic_ noise for 24 hours. An affected creature may attempt a new save to shake off the effect at the end of each of its turns. This is a mind-affecting effect. The save DC is Charisma-based.

##### Description

A _brain ooze_ (sometimes known as a “killer brain”) resembles almost precisely the raw brain of a human, save for the eldritch energy surrounding it and the twin tentacles extending from its sides. The creature’s thought patterns are unusually powerful, and cause painful mental feedback in the minds of other conscious beings.

Other intelligent beings are nothing more than cattle and playthings to brain oozes—victims to be tormented, thought patterns to be consumed. Brain oozes prefer to manipulate their prey from the shadows. Rather than assaulting openly, they provoke fights and conflict within groups, or lure one or two victims away for the kill. Brain oozes derive particular satisfaction from forcing an individual to commit terrible acts, then wiping away all knowledge of the crimes from the victim’s memory. They torment such hapless puppets again and again, forcing them to commit ever greater atrocities. Once weary of their sport they return the modified memories with _dispel magic_, and feast upon the delicious misery of the victim’s final despair.

Brain oozes feed through their tentacles by extracting the thoughts of living creatures. Animals and less intelligent creatures provide little nourishment, but they prize fey, outsiders, and spellcasters as delicacies. After several feedings, a _brain ooze_ divides into two nearly identical brains, each retaining only a portion of the knowledge and experiences of the parent.

The similarities between intellect devourers and brain oozes have not gone unnoticed, but the two species appear to have little in common beyond appearance. Some theorize that brain oozes are actually the result of an ancient race’s failed attempt to achieve immortality by preserving their minds via alien technology or magic.