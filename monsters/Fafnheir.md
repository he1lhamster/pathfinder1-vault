---
cssclass: [monsters]
title1: Fafnheir
desc_short: The scales of this craggy serpentine dragon are scarred and blackened.
  Its eyes flare with nightmarish power, and its mouth drips with liquid flame.
title2: Fafnheir
CR: 24
sources:
- name: Lands of the Linnorm Kings
  page: 56
  link: http://paizo.com/products/btpy8ode?Pathfinder-Campaign-Setting-Lands-of-the-Linnorm-Kings
XP: 1228800
alignment: CE
size: Colossal
type: dragon
initiative:
  bonus: 14
senses:
  darkvision: 60
  low-light vision: true
  scent: true
  true seeing: true
AC:
  AC: 42
  touch: 12
  flat_footed: 32
  components:
    dex: 10
    natural: 30
    size: -8
HP:
  HP: 526
  long: 27d12+351
saves:
  fort: 28
  ref: 25
  will: 23
defensive_abilities:
- freedom of movement
DR:
- amount: 20
  weakness: cold iron and epic
immunities:
- curse effects
- dragon traits
- electricity
- fire
- mind-affecting effects
- paralysis
- poison
- sleep
SR: 35
speeds:
  base: 50
  burrow: 30
  fly: 100
  fly_maneuverability: average
  swim: 50
attacks:
  melee:
  - - text: bite +36 (6d6+17/19-20 plus poison)
      entries:
      - - damage: 6d6+17
          crit_range: 19-20
        - effect: poison
      attack: bite
      bonus:
      - 36
    - text: 2 claws +36 (2d8+17/19-20)
      entries:
      - - damage: 2d8+17
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 36
    - text: gore +36 (4d6+17/19-20)
      entries:
      - - damage: 4d6+17
          crit_range: 19-20
      attack: gore
      bonus:
      - 36
    - text: tail slap +31 (4d6+8 plus grab)
      entries:
      - - damage: 4d6+8
        - effect: grab
      attack: tail slap
      bonus:
      - 31
  special:
  - breath weapon
  - constrict (tail, 4d6+8)
  - death curse
space: 30
reach: 30
spell_like_abilities:
  entries:
  - name: greater dispel magic
    source: default
    freq: At will
  - name: quickened greater dispel magic
    source: default
    freq: 3/day
  - name: limited wish
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 3/day
    other: between First World and Material Plane only
  - name: spell turning
    source: default
    freq: 3/day
  - name: wall of force
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 20
    concentration: 29
ability_scores:
  STR: 45
  DEX: 30
  CON: 36
  INT: 18
  WIS: 27
  CHA: 29
BAB: 27
CMB: 52
CMB_other: +56 grapple
CMD: 72
CMD_other: can't be tripped
feats:
- name: Awesome Blow
- name: Combat Reflexes
- name: Critical Focus
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Critical (claws)
- name: Improved Critical (gore)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Power Attack
- name: Quicken Spell-Like Ability (greater dispel magic)
- name: Staggering Critical
- name: Vital Strike
skills:
  Fly: 32
  Intimidate: 39
  Knowledge (arcana): 34
  Knowledge (geography): 34
  Knowledge (history): 34
  Knowledge (nature): 34
  Perception: 46
  Stealth: 24
  Swim: 55
  Use Magic Device: 39
  _racial_mods:
    Perception:
      _: 8
languages:
- Aklo
- Common
- Draconic
- Skald
- Sylvan
ecology:
  environment: any (Grungir Forest)
  organization: solitary
  treasure_type: triple
special_abilities:
  Breath Weapon (Su): |-
    Once every 1d4 rounds as a standard action, Fafnheir can breathe a 90-foot cone of burning wind, dealing 26d10 points of fire damage to all creatures in the area of effect. A DC 36 Reflex save halves the fire damage dealt. The save DC is Constitution-based. This wind has two additional effects as well.

    Deafening: Any creature in the area of effect that does not succeed at a DC 36 Fortitude save is deafened by the thunderous wind.

    Storm-Laced: The closest creature to Fafnheir in the area of effect is also blasted by a bolt of lightning and takes 20d6 points of electricity damage in addition to the fire damage dealt. This creature can make a second DC 36 Reflex save to halve this electricity damage.

    Tornado Force: The winds themselves gust at nearly 300 miles per hour, affecting all creatures in the area of effect as if they were caught in tornado-force winds. The wind lasts only a few moments during Fafnheir's action, so it has no real effect on ranged attacks, but it blows away any Large or smaller creature (or Huge or smaller flying creature) that fails a DC 15 Strength check.
  Death Curse (Su): |-
    Fafnheir is a difficult creature to slay, especially since he lives on in the body of any creature that slays him. When a creature slays Fafnheir, it becomes afflicted by the Curse of Fafnheir.

    Curse of Fafnheir: save Will DC 32; effect creature's sense of self erodes as its personality is slowly replaced by Fafnheir's-this manifests as 1d6 points of Charisma drain every 24 hours. A target whose Charisma drops to 0 becomes comatose and must immediately make a DC 32 Fortitude save or die; every 24 hours that passes thereafter, the victim must make a new Fortitude save to avoid death (unless its Charisma score rises above 0, at which point it takes 1d6 points of Charisma drain). If a creature dies from the effects of this curse, its body explodes in a 60-foot burst of burning wind, with effects identical to Fafnheir's breath weapon. This effect occurs if the cursed victim dies from any effect, not just from the curse. One round later, Fafnheir gains the effect of a true resurrection spell, appearing at the same spot where the cursed victim died (or the closest area large enough to contain the Colossal creature), with full memories of the cursed victim's doings and accomplishments while cursed. The only way to permanently slay Fafnheir is to avoid becoming cursed after killing him, or to remove the curse before the victim dies. The effects of this curse end prematurely and immediately if Fafnheir is restored to life by other means. The save DC is Charisma-based.
  Freedom of Movement (Ex): Fafnheir is under the constant effect of freedom of movement,
    as the spell of the same name. This effect cannot be dispelled.
  Poison (Su): Bite-injury; save Fort DC 34; frequency 1/round for 10 rounds; effect
    10d6 fire damage and 1d4 drain from each ability score; cure 3 consecutive saves.
    The save DC is Constitution-based.
  True Seeing (Ex): Fafnheir has true seeing, as the spell of the same name. This
    effect cannot be dispelled.
desc_long: |-
  Called the Father of All Linnorms, Fafnheir is the oldest and mightiest of his kind to dwell upon Golarion-other, even more powerful linnorms exist on the First World, but on Golarion, Fafnheir is king. Crafty and powerful, Fafnheir is more than just a creature of rage or hunger, and is sometimes known to speak with those who come to him as supplicants for his wisdom. Tales say that to gain Fafnheir's advice, one must travel through Grungir Forest to the cavern entrance of the linnorm's lair, whereupon the supplicant must call into the opening several secret names for the ancient linnorm. A single step into the lair renders the supplication moot, for Fafnheir does not suffer intrusions. It is customary to bring a herd of sheep, oxen, or several thralls for him to feast upon.

  Those who find Fafnheir in a talkative mood and live to tell the tale report that the linnorm is well versed in numerous fields, and capable of working a wide range of magic through wishcrafting, though how much of his bragging is true is debatable. Fafnheir claims to have been the first linnorm to cross to Golarion from the First World after slaying three of that realm's Eldest, as well as to remember a time when the dragon god Dahak came to this world, and to have taken part in ancient battles against humanity as an ally of the serpentfolk. Certain Thassilonian accounts give support to his claim of providing advice and aid at times to Runelord Xanderghul, and he endured the Age of Darkness with ease. The past few thousand years have passed in the blink of an eye for the ancient linnorm, and he expects to survive for thousands more.

  Fafnheir is aware of the prophecy that the hero who kills him will become king of all Ulfen. The linnorm also knows that in death he will be reborn from the burnt flesh of his slayer, and suggests to those who raise this topic with him that only by becoming him can such a Linnorm King rule. While Fafnheir has seen many challengers, few have offered him a true battle.

  Fafnheir spends much of his time slumbering, but wakes quickly at the slightest deviation in the patterns of the world around him, and his dreaming mind touches the woods above and the blood of his children. Those who would come upon him unawares should not expect success unless they travel into his lair from other worlds, for his attunement to Grungir Forest is uncanny. The linnorm rarely ventures far from his lair, preferring to lure his enemies close and dispatch them on familiar ground. He loves nothing but his treasure, and cannot be bribed or threatened-the lure of potential treasure does not excite him nearly as much as what he already possesses. He is a subtle combatant, preferring to use trickery before launching into melee. Unlike his lesser kin, Fafnheir has a number of potent, if limited, spell-like abilities, and he often uses his limited wishes to great effect. He has long experience with direct confrontation, and his millennia of action have taught him tricks that few remember. He is one of the most deadly creatures in the Inner Sea region, and even the mightiest dragons fear his power.

---

# Fafnheir
_[[diseases/The Scales|The scales]]_ of this craggy serpentine dragon are scarred and blackened. Its eyes _[[spells/Flare|flare]]_ with nightmarish power, and its mouth drips with liquid flame.
**Source** Lands of the Linnorm Kings pg. 56
**XP** 1,228,800
CE Colossal dragon
**Init** +14; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_, _[[spells/True Seeing|true seeing]]_; Perception +46

##### Defense

**AC** 42, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+10 Dex, +30 natural, –8 size)
**hp** 526 (27d12+351)
**Fort** +28, **Ref** +25, **Will** +23
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 20/cold iron and epic; **Immune** curse effects, dragon traits, electricity, fire, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, poison, sleep; **SR** 35

##### Offense
**Speed** 50 ft., _[[universal monster rules/Burrow|burrow]]_ 30 ft., fly 100 ft. (average), swim 50 ft.
**Melee** bite +36 (6d6+17/19–20 plus poison), 2 claws +36 (2d8+17/19–20), gore +36 (4d6+17/19–20), tail slap +31 (4d6+8 plus _[[universal monster rules/Grab|grab]]_)
**Space** 30 ft., **Reach** 30 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_, _[[universal monster rules/Constrict|constrict]]_ (tail, 4d6+8), death curse
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +29)
At will—greater _[[spells/Dispel Magic|dispel magic]]_
3/day—quickened greater _dispel magic_, _[[spells/Limited Wish|limited wish]]_, _[[spells/Plane Shift|plane shift]]_ (between First World and Material Plane only), _[[spells/Spell Turning|spell turning]]_, _[[spells/Wall Of Force|wall of force]]_

##### Statistics
**Str** 45, **Dex** 30, **Con** 36, **Int** 18, **Wis** 27, **Cha** 29
**Base Atk** +27; **CMB** +52 (+56 grapple); **CMD** 72 (can’t be tripped)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (claws), _Improved Critical_ (gore), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (greater _dispel magic_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +32, Intimidate +39, Knowledge (arcana) +34, Knowledge (geography) +34, Knowledge (history) +34, Knowledge (nature) +34, Perception +46, Stealth +24, Swim +55, Use Magic Device +39; **Racial Modifiers** +8 Perception
**Languages** Aklo, Common, Draconic, _[[classes/Skald|Skald]]_, Sylvan

##### Ecology

**Environment** any (Grungir Forest)
**Organization** solitary
**Treasure** triple

### Special Abilities

**_Breath Weapon_ (Su)** Once every 1d4 rounds as a standard action, _[[monsters/Fafnheir|Fafnheir]]_ can breathe a 90-foot cone of _[[items/Weapon Magic Abilities/Burning|burning]]_ wind, dealing 26d10 points of fire damage to all creatures in the area of effect. A DC 36 Reflex save halves the fire damage dealt. The save DC is Constitution-based. This wind has two additional effects as well.

Deafening: Any creature in the area of effect that does not succeed at a DC 36 Fortitude save is _[[conditions/Deafened|deafened]]_ by the thunderous wind.

Storm-Laced: The closest creature to _Fafnheir_ in the area of effect is also blasted by a bolt of lightning and takes 20d6 points of electricity damage in addition to the fire damage dealt. This creature can make a second DC 36 Reflex save to halve this electricity damage.

Tornado Force: The winds themselves gust at nearly 300 miles per hour, affecting all creatures in the area of effect as if they were caught in tornado-force winds. The wind lasts only a few moments during _Fafnheir_’s action, so it has no real effect on ranged attacks, but it blows away any Large or smaller creature (or Huge or smaller flying creature) that fails a DC 15 Strength check.

**Death Curse (Su) **_Fafnheir_ is a difficult creature to slay, especially since he lives on in the body of any creature that slays him. When a creature slays _Fafnheir_, it becomes afflicted by the Curse of _Fafnheir_.

Curse of _Fafnheir_: save Will DC 32; effect creature’s sense of self erodes as its personality is slowly replaced by _Fafnheir_’s—this manifests as 1d6 points of Charisma drain every 24 hours. A target whose Charisma drops to 0 becomes comatose and must immediately make a DC 32 Fortitude save or die; every 24 hours that passes thereafter, the victim must make a new Fortitude save to avoid death (unless its Charisma score rises above 0, at which point it takes 1d6 points of Charisma drain). If a creature dies from the effects of this curse, its body explodes in a 60-foot burst of _burning_ wind, with effects identical to _Fafnheir_’s _breath weapon_. This effect occurs if the cursed victim dies from any effect, not just from the curse. One round later, _Fafnheir_ gains the effect of a _[[spells/True Resurrection|true resurrection]]_ spell, appearing at the same spot where the cursed victim died (or the closest area large enough to contain the Colossal creature), with full memories of the cursed victim’s doings and accomplishments while cursed. The only way to permanently slay _Fafnheir_ is to avoid becoming cursed after killing him, or to remove the curse before the victim dies. The effects of this curse end prematurely and immediately if _Fafnheir_ is restored to life by other means. The save DC is Charisma-based.

**_Freedom of Movement_ (Ex)** _Fafnheir_ is under the constant effect of _freedom of movement_, as the spell of the same name. This effect cannot be dispelled.

**Poison (Su)** Bite—injury; save Fort DC 34; frequency 1/round for 10 rounds; effect 10d6 fire damage and 1d4 drain from each ability score; cure 3 consecutive saves. The save DC is Constitution-based.

**_True Seeing_ (Ex)** _Fafnheir_ has _true seeing_, as the spell of the same name. This effect cannot be dispelled.

##### Description

_[[items/Weapon Magic Abilities/Called|Called]]_ the Father of All Linnorms, _Fafnheir_ is the oldest and mightiest of his kind to dwell upon Golarion—other, even more powerful linnorms exist on the First World, but on Golarion, _Fafnheir_ is _[[npcs/King|king]]_. Crafty and powerful, _Fafnheir_ is more than just a creature of _[[spells/Rage|rage]]_ or hunger, and is sometimes known to speak with those who come to him as supplicants for his wisdom. Tales say that to gain _Fafnheir_’s advice, one must travel through Grungir Forest to the cavern entrance of the linnorm’s lair, whereupon the supplicant must call into the opening several secret names for the ancient linnorm. A single step into the lair renders the supplication moot, for _Fafnheir_ does not suffer intrusions. It is customary to bring a herd of sheep, oxen, or several thralls for him to feast upon.

Those who find _Fafnheir_ in a talkative mood and live to tell the tale report that the linnorm is well versed in numerous fields, and capable of working a wide range of magic through wishcrafting, though how much of his bragging is true is debatable. _Fafnheir_ claims to have been the first linnorm to cross to Golarion from the First World after slaying three of that realm’s Eldest, as well as to remember a time when the dragon god Dahak came to this world, and to have taken part in ancient battles against humanity as an ally of the _[[monsters/Serpentfolk|serpentfolk]]_. Certain Thassilonian accounts give support to his claim of providing advice and aid at times to Runelord Xanderghul, and he endured the Age of _[[spells/Darkness|Darkness]]_ with ease. The past few thousand years have passed in the _[[spells/Blink|blink]]_ of an eye for the ancient linnorm, and he expects to survive for thousands more.

_Fafnheir_ is aware of the prophecy that the hero who kills him will become _king_ of all Ulfen. The linnorm also knows that in death he will be reborn from the burnt flesh of his _[[classes/Slayer|slayer]]_, and suggests to those who raise this topic with him that only by becoming him can such a Linnorm _King_ rule. While _Fafnheir_ has seen many challengers, few have offered him a true battle.

_Fafnheir_ spends much of his time slumbering, but wakes quickly at the slightest deviation in the patterns of the world around him, and his dreaming mind touches the woods above and the blood of his children. Those who would come upon him unawares should not expect success unless they travel into his lair from other worlds, for his attunement to Grungir Forest is uncanny. The linnorm rarely ventures far from his lair, preferring to lure his enemies close and dispatch them on familiar ground. He loves nothing but his treasure, and cannot be bribed or threatened—the lure of potential treasure does not excite him nearly as much as what he already possesses. He is a subtle combatant, preferring to use trickery before launching into melee. Unlike his lesser kin, _Fafnheir_ has a number of _[[items/Weapon Magic Abilities/Potent|potent]]_, if limited, _spell-like abilities_, and he often uses his limited wishes to great effect. He has long experience with direct confrontation, and his millennia of action have taught him tricks that few remember. He is one of the most _[[items/Weapon Magic Abilities/Deadly|deadly]]_ creatures in the Inner Sea region, and even the mightiest dragons _[[universal monster rules/Fear|fear]]_ his power.