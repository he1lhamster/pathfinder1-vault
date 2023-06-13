---
cssclass: [monsters]
title1: Neothelid Overlord
desc_short: Two disgusting heads rise above this enormous mass of slime-drenched coils
  and slithering tentacles.
title2: Neothelid Overlord
CR: 20
sources:
- name: Occult Bestiary
  page: 36
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 307200
alignment: CE
size: Gargantuan
type: aberration
initiative:
  bonus: 4
senses:
  blindsight: 100
  trace teleport: 60
auras:
- name: madness
  radius: 60
  DC: 33
AC:
  AC: 34
  touch: 6
  flat_footed: 34
  components:
    natural: 28
    size: -4
HP:
  HP: 400
  long: 32d8+256
saves:
  fort: 20
  ref: 12
  will: 24
  other: +4 vs. psychic spells
defensive_abilities:
- psychic resilience
DR:
- amount: 15
  weakness: cold iron
SR: 31
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 6 tongues +32 (3d6+12/19-20 plus grab)
      entries:
      - - damage: 3d6+12
          crit_range: 19-20
        - effect: grab
      count: 6
      attack: tongues
      bonus:
      - 32
  special:
  - breath weapon (50-ft. cone, 18d10 acid, Reflex DC 34 half, once every 1d4 rounds)
  - coordinated attacks
  - swallow whole (2d6+12 plus 2d6 acid, AC 24, hp 40)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: clairvoyance/clairaudience
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: At will
    DC: 19
  - name: mass charm monster
    source: default
    freq: At will
    DC: 25
  - name: mass suggestion
    source: default
    freq: At will
    DC: 23
  - name: poison
    source: default
    freq: At will
    DC: 20
  - name: telekinesis
    source: default
    freq: At will
  - name: teleport
    source: default
    freq: At will
  - name: quickened mass suggestion
    source: default
    freq: 3/day
    DC: 23
  sources:
  - name: default
    CL: 20
    concentration: 27
psychic_magic:
  entries:
  - superscripts:
    - OA
    name: demand offering
    PE: 2
    DC: 19
  - superscripts:
    - OA
    name: ego whip V
    PE: 6
    DC: 23
  - superscripts:
    - OA
    name: id insinuation IV
    PE: 5
    DC: 22
  - superscripts:
    - OA
    name: mass inflict pain
    PE: 6
    DC: 23
  - superscripts:
    - OA
    name: mind thrust VI
    PE: 6
    DC: 23
  - superscripts:
    - OA
    name: psychic crush V
    PE: 9
    DC: 26
  - superscripts:
    - OA
    name: telekinetic storm
    PE: 9
    DC: 26
  sources:
  - name: default
    CL: 20
    concentration: 27
  PE: 27
ability_scores:
  STR: 34
  DEX: 11
  CON: 26
  INT: 24
  WIS: 19
  CHA: 25
BAB: 24
CMB: 40
CMB_other: +44 bull rush, +44 grapple, +44 overrun
CMD: 50
CMD_other: 52 vs. bull rush, 52 vs. overrun
feats:
- name: Alertness
- name: Cleave
- name: Great Cleave
- name: Great Fortitude
- name: Greater Bull Rush
- name: Greater Overrun
- name: Improved Bull Rush
- name: Improved Critical (tongue)
- name: Improved Initiative
- name: Improved Lightning Reflexes
- name: Improved Overrun
- name: Iron Will
- name: Lightning Reflexes
- name: Persuasive
- name: Power Attack
- name: Quicken Spell-Like Ability (mass suggestion)
skills:
  Bluff: 39
  Climb: 47
  Diplomacy: 43
  Fly: 33
  Intimidate: 46
  Knowledge (arcana): 42
  Knowledge (dungeoneering): 39
  Knowledge (planes): 39
  Perception: 43
  Sense Motive: 40
  Spellcraft: 42
languages:
- Aboleth
- Abyssal
- Aklo
- Elder Thing
- Infernal
- Orvian
- Terran
- Undercommon
- telepathy 100 ft.
special_qualities:
- divided consciousness
ecology:
  environment: any underground
  organization: solitary, pair, or conclave (3-5 served by a cult of neothelids and
    9-24 seugathi)
  treasure_type: standard
special_abilities:
  Aura of Madness (Su): Any sane being within 60 feet of a conscious neothelid overlord
    must succeed at a DC 33 Will saving throw each round or become confused for 1
    round. A creature that fails 5 saves in a row becomes permanently insane, as per
    the insanity spell. A neothelid overlord can suppress or activate this aura as
    a free action. This is a mind-affecting insanity effect. The save DC is Charisma-based.
  Coordinated Attacks (Ex): A neothelid overlord can make attacks with the three tongues
    in each of its two heads. It can attempt to swallow two targets at the same time,
    but if the neothelid overlord instead attacks the same target with all six tongues,
    it gains a +4 bonus on all combat maneuver checks to grab and swallow that target,
    regardless of how many tongues successfully hit. On a round in which it uses its
    breath weapon, a neothelid overlord can still attack with the three tongues belonging
    to its other head.
  Divided Consciousness (Ex): The neothelid overlord's two heads share a split consciousness
    that allows it to operate as though the overlord were constantly under the effect
    of a divide mindOA spell.
  Trace Teleport (Ex): A neothelid overlord telepathically and reflexively learns
    the mental coordinates of the destination of all creatures that use a teleport
    spell or effect within 60 feet of it, gaining an awareness of the location equivalent
    to “seen casually.” This knowledge fades and is lost after 1 minute. This ability
    does not grant any environmental information about the conditions of the destination.
desc_long: |-
  Those who have learned secrets of the deepest vaults of Orv know of the neothelids of Denebrum. In fetid pools of poisonous swamps and surreal forests of twisted, phosphorescent fungi, these gigantic worm-things rule and wage war against Orv's other denizens and each other. While most know that the neothelids are ancient creatures, spawned by eldritch beings in a time and place far removed from the known world, very few are aware that some neothelids are old beyond imagining. In their eons of existence, they have changed, surviving the centuries of mindless hunger that drives the youngest of their kind and ultimately defeating enough of their peers to become truly hideous masters of the damp, nearly lightless depths of Orv.

  Scholars of such lore can only speculate as to what causes a neothelid to begin the transformation into an overlord. The change could be a natural process of age and development, though nothing about neothelids can truly be called natural. It may be that by delving into forbidden lore, they discover potent secrets, just as other rituals grant mortals the hideous power of lichdom. It might instead be that overlords' ascendant power comes from some link to the blasphemous entities they venerate, a connection that only the most dedicated among the neothelids are able to cultivate. Whatever the cause, the result is terrifying-even maddening-to behold.

  An overlord achieves such immense power and intellect that it reaches a state in which its consciousness splits into two minds that work as one. In a horrifying metamorphosis, the creature's head splits down the middle to form two separate heads, each of which contains a portion of the neothelid's intellect. The new neothelid overlord's enhanced cognition grants it a deeper understanding of reality and enables it to harness psychic magic beyond the ken of its younger kin. Though still able to crush a victim with pure psychic force, the neothelid overlord develops an awesome level of finesse and skill in the manipulation of both mind and matter.

  Neothelid overlords undergo other physical changes as well. Although they do not become significantly larger than typical neothelids, overlords take on a darker hue and their bodies sprout myriad tentacles that constantly squirm, as though each possessed a sentience of its own. The creatures' tails also split into three parts, the ends of which claw and dig at the ground as though trying to take root in the very bedrock. The functions of overlords' tentacles and triple tails are a mystery. It is possible that they have something to do with reproduction or the spawning of their seugathi (Pathfinder RPG Bestiary 2 243) servants, but the truth is something that only the most insane researchers could hope to uncover. Along with these physical changes comes an increase in might and a swiftness that one would not expect from something so large. A typical neothelid overlord measures approximately 100 feet in length from head to tail, though it usually remains coiled and takes up about one-fifth of that space. Overlords weigh about 100,000 pounds, though individuals can vary wildly in size.

  Neothelid overlords rise to become tyrannical rulers, directing less developed members of their race toward goals that no healthy mind can fathom. They reinforce their power over subordinates through manipulation and punitive displays of power, believing that fear of random-appearing punishments keeps their followers in line even when they are not under observation. Most assume that neothelid overlords serve either their own whims or those of the ones they worship-the shapeless and terrible entities of the Dark Tapestry that created neothelids and countless other horrors in the darkest reaches of space and time. Few who know of these monsters, though, dare to think that their purposes are anything but anathema to normal life whether aboveground or belowground.

  In The Dream Diary of Lady Elliara Celmenari, written in 3875 ar, the Taldan author claims to have visited Denebrum while in an astral form and to have seen at least one neothelid overlord. Her writings depicts the creature as guarding the resting place of two dormant bholes (Pathfinder RPG Bestiary 4 18). The text describes the overlord sending out madness-inducing offspring into the world to find a means of awakening and controlling the legendary beasts. Most learned folk attribute Lady Celmenari's dreams of doom and destruction to a chronic nervous condition, compounded by the impending collapse of Taldan supremacy. But in recent years, rumors have come to light indicating that a certain cult of Groetus is working with agents of a mysterious and unwholesome nature toward a similar goal, which has dangerous implications for all of Golarion. To occult scholars, visions and whispers such as these serve as further evidence that terrible things wait in the dark places of the multiverse and must be opposed.

---

# Neothelid Overlord
Two disgusting heads rise above this enormous mass of slime-drenched coils and _[[items/Weapon Magic Abilities/Slithering|slithering]]_ tentacles.
**Source** Occult Bestiary pg. 36
**XP** 307,200
CE Gargantuan aberration
**Init** +4; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 100 ft., _[[spells/Trace Teleport|trace teleport]]_ 60 ft.; Perception +43
**Aura** madness (60 ft., DC 33)

##### Defense

**AC** 34, touch 6, _[[conditions/Flat-Footed|flat-footed]]_ 34 (+28 natural, –4 size)
**hp** 400 (32d8+256)
**Fort** +20, **Ref** +12, **Will** +24; +4 vs. _[[classes/Psychic|psychic]]_ spells
**Defensive Abilities** _[[universal monster rules/Psychic Resilience|psychic resilience]]_; **DR** 15/cold iron; **SR** 31

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** 6 _[[spells/Tongues|tongues]]_ +32 (3d6+12/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (50-ft. cone, 18d10 acid, Reflex DC 34 half, once every 1d4 rounds), coordinated attacks, _[[universal monster rules/Swallow Whole|swallow whole]]_ (2d6+12 plus 2d6 acid, AC 24, hp 40)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—fly
At will—clairvoyance/clairaudience, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 19), mass _[[spells/Charm Monster|charm monster]]_ (DC 25), mass _[[spells/Suggestion|suggestion]]_ (DC 23), poison (DC 20), _[[spells/Telekinesis|telekinesis]]_, teleport
3/day—quickened mass _suggestion_ (DC 23)
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 20th; concentration +27)
27 PE—_[[spells/Demand Offering|demand offering]]_ (2 PE, DC 19), _[[spells/Ego _[[items/Weapon/Whip|Whip]]_ V|ego _whip_ V]]_ (6 PE, DC 23), _[[spells/Id Insinuation IV|id insinuation IV]]_ (5 PE, DC 22), mass _[[spells/Inflict Pain|inflict pain]]_ (6 PE, DC 23), _[[spells/Mind Thrust VI|mind thrust VI]]_ (6 PE, DC 23), _[[spells/Psychic Crush V|psychic crush V]]_ (9 PE, DC 26), _[[spells/Telekinetic Storm|telekinetic storm]]_ (9 PE, DC 26)

##### Statistics
**Str** 34, **Dex** 11, **Con** 26, **Int** 24, **Wis** 19, **Cha** 25
**Base Atk** +24; **CMB** +40 (+44 bull rush, +44 grapple, +44 overrun); **CMD** 50 (52 vs. bull rush, 52 vs. overrun)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Overrun|Greater Overrun]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (tongue), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (mass _suggestion_)
**Skills** Bluff +39, _[[universal monster rules/Climb|Climb]]_ +47, Diplomacy +43, Fly +33, Intimidate +46, Knowledge (arcana) +42, Knowledge (dungeoneering, planes) +39, Perception +43, Sense Motive +40, Spellcraft +42
**Languages** Aboleth, Abyssal, Aklo, _[[monsters/Elder Thing|Elder Thing]]_, Infernal, Orvian, Terran, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** divided consciousness

##### Ecology

**Environment** any underground
**Organization** solitary, pair, or conclave (3–5 served by a cult of neothelids and 9–24 _[[monsters/Seugathi|seugathi]]_)
**Treasure** standard

### Special Abilities

**Aura of Madness (Su)** Any sane being within 60 feet of a conscious _[[monsters/Neothelid Overlord|neothelid overlord]]_ must succeed at a DC 33 Will saving throw each round or become _[[conditions/Confused|confused]]_ for 1 round. A creature that fails 5 saves in a row becomes permanently insane, as per the _[[spells/Insanity|insanity]]_ spell. A _neothelid overlord_ can suppress or activate this aura as a free action. This is a mind-affecting _insanity_ effect. The save DC is Charisma-based.

**Coordinated Attacks (Ex)** A _neothelid overlord_ can make attacks with the three _tongues_ in each of its two heads. It can attempt to swallow two targets at the same time, but if the _neothelid overlord_ instead attacks the same target with all six _tongues_, it gains a +4 bonus on all combat maneuver checks to _grab_ and swallow that target, regardless of how many _tongues_ successfully hit. On a round in which it uses its _breath weapon_, a _neothelid overlord_ can still attack with the three _tongues_ belonging to its other head.

**Divided Consciousness (Ex)** The _neothelid overlord_’s two heads share a _[[universal monster rules/Split|split]]_ consciousness that allows it to operate as though the overlord were constantly under the effect of a _[[spells/Divide Mind|divide mind]]_ spell.

**_Trace Teleport_ (Ex)** A _neothelid overlord_ telepathically and reflexively learns the mental coordinates of the destination of all creatures that use a teleport spell or effect within 60 feet of it, gaining an awareness of the location equivalent to “seen casually.” This knowledge fades and is lost after 1 minute. This ability does not grant any environmental information about the conditions of the destination.

##### Description

Those who have learned secrets of the deepest vaults of Orv know of the neothelids of Denebrum. In fetid pools of poisonous swamps and surreal forests of twisted, phosphorescent fungi, these gigantic worm-things rule and wage war against Orv’s other denizens and each other. While most know that the neothelids are ancient creatures, spawned by eldritch beings in a time and place far removed from the known world, very few are aware that some neothelids are old beyond imagining. In their eons of existence, they have changed, surviving the centuries of mindless hunger that drives the youngest of their kind and ultimately defeating enough of their peers to become truly hideous masters of the damp, nearly lightless depths of Orv.

Scholars of such lore can only speculate as to what causes a _[[monsters/Neothelid|neothelid]]_ to begin the _[[spells/Transformation|transformation]]_ into an overlord. The change could be a natural process of age and development, though nothing about neothelids can truly be _[[items/Weapon Magic Abilities/Called|called]]_ natural. It may be that by _[[items/Armor Magic Abilities/Delving|delving]]_ into forbidden lore, they discover _[[items/Weapon Magic Abilities/Potent|potent]]_ secrets, just as other rituals grant mortals the hideous power of lichdom. It might instead be that overlords’ _[[feats/Ascendant|ascendant]]_ power comes from some link to the blasphemous entities they venerate, a connection that only the most dedicated among the neothelids are able to cultivate. Whatever the cause, the result is terrifying—even maddening—to behold.

An overlord achieves such immense power and intellect that it reaches a state in which its consciousness splits into two minds that work as one. In a horrifying metamorphosis, the creature’s head splits down the middle to form two separate heads, each of which contains a portion of the _neothelid_’s intellect. The new _neothelid overlord_’s enhanced cognition grants it a deeper understanding of reality and enables it to harness _psychic magic_ beyond the ken of its younger kin. Though still able to crush a victim with pure _psychic_ force, the _neothelid overlord_ develops an awesome level of finesse and skill in the manipulation of both mind and matter.

_Neothelid_ overlords undergo other physical changes as well. Although they do not become significantly larger than typical neothelids, overlords take on a darker hue and their bodies sprout myriad tentacles that constantly squirm, as though each possessed a sentience of its own. The creatures’ tails also _split_ into three parts, the ends of which claw and dig at the ground as though trying to take _[[spells/Root|root]]_ in the very bedrock. The functions of overlords’ tentacles and triple tails are a mystery. It is possible that they have something to do with reproduction or the spawning of their _seugathi_ (Pathfinder RPG Bestiary 2 243) servants, but the truth is something that only the most insane researchers could hope to uncover. Along with these physical changes comes an increase in might and a swiftness that one would not expect from something so large. A typical _neothelid overlord_ measures approximately 100 feet in length from head to tail, though it usually remains coiled and takes up about one-fifth of that space. Overlords weigh about 100,000 pounds, though individuals can vary wildly in size.

_Neothelid_ overlords rise to become tyrannical rulers, directing less developed members of their race toward goals that no healthy mind can fathom. They reinforce their power over subordinates through manipulation and punitive displays of power, believing that _[[universal monster rules/Fear|fear]]_ of random-appearing punishments keeps their followers in line even when they are not under observation. Most assume that _neothelid_ overlords serve either their own whims or those of the ones they worship—the shapeless and terrible entities of the Dark Tapestry that created neothelids and countless other horrors in the darkest reaches of space and time. Few who know of these monsters, though, dare to think that their purposes are anything but anathema to normal life whether aboveground or belowground.

In The _[[spells/Dream|Dream]]_ Diary of Lady Elliara Celmenari, written in 3875 ar, the Taldan author claims to have visited Denebrum while in an astral form and to have seen at least one _neothelid overlord_. Her writings depicts the creature as _[[items/Armor Magic Abilities/Guarding|guarding]]_ the resting place of two dormant bholes (Pathfinder RPG Bestiary 4 18). The text describes the overlord _[[spells/Sending|sending]]_ out madness-inducing offspring into the world to find a means of awakening and controlling the legendary beasts. Most learned folk attribute Lady Celmenari’s dreams of _[[spells/Doom|doom]]_ and _[[spells/Destruction|destruction]]_ to a chronic nervous condition, compounded by the impending collapse of Taldan supremacy. But in recent years, rumors have come to light indicating that a certain cult of Groetus is working with agents of a mysterious and unwholesome nature toward a similar goal, which has dangerous implications for all of Golarion. To occult scholars, visions and whispers such as these serve as further evidence that terrible things wait in the dark places of the multiverse and must be opposed.