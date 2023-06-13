---
cssclass: [monsters]
title1: Archdevil, Geryon
desc_short: This tripartite being has three humanoid bodies engulfed fromthe waist
  down by a tangle of three immense serpents.
title2: Geryon
CR: 29
sources:
- name: Bestiary 6
  page: 24
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 6553600
alignment: LE
size: Huge
type: outsider
subtypes:
- aquatic
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 9
senses:
  darkvision: 60
  detect chaos: true
  detect good: true
  scent: true
  see in darkness: true
  true seeing: true
auras:
- name: frightful presence
  radius: 120
  DC: 38
- name: shield of law
  DC: 29
AC:
  AC: 47
  touch: 32
  flat_footed: 42
  components:
    deflection: 4
    dex,+8 natural: 5
    profane: 15
    shield: 7
    size: -2
HP:
  HP: 731
  long: 34d10+544
  regeneration: 30
  regeneration_weakness: deific or mythic
saves:
  fort: 31
  ref: 28
  will: 33
  other: +8 vs. mind-affecting effects
defensive_abilities:
- all-around vision
- envenomed scales,infernal resurrection
- mind blank
- threefold body
DR:
- amount: 20
  weakness: epic, good, and silver
immunities:
- ability damage
- ability drain,charm
- cold
- compulsion
- death effects
- energy drain
- fire,memory loss effects
- petrification
- poison
resistances:
  acid: 30
SR: 40
speeds:
  base: 50
  swim: 50
  other:
  - air walk
attacks:
  melee:
  - - text: +5 cruel dispelling burst unholy flail +47/+42/+37/+32(3d6+19/19-20)
      entries:
      - - damage: 3d6+19
          crit_range: 19-20
      attack: +5 cruel dispelling burst unholy flail
      bonus:
      - 47
      - 42
      - 37
      - 32
    - text: +1 heavy shield +43/+38 (2d6+15/19-20)
      entries:
      - - damage: 2d6+15
          crit_range: 19-20
      attack: +1 heavy shield
      bonus:
      - 43
      - 38
    - text: 3 claws +41 (1d6+7)
      entries:
      - - damage: 1d6+7
      count: 3
      attack: claws
      bonus:
      - 41
    - text: 3 tail slaps +41 (2d6+7/19-20 plus poison)
      entries:
      - - damage: 2d6+7
          crit_range: 19-20
        - effect: poison
      count: 3
      attack: tail slaps
      bonus:
      - 41
  special:
  - casterbane
  - corrupting caress
  - perceive destiny
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: mind blank
    source: default
    freq: Constant
  - name: shield of law
    source: default
    freq: Constant
    DC: 29
  - name: true seeing
    source: default
    freq: Constant
  - name: astral projection
    source: default
    freq: At will
  - is_mythic_spell: true
    name: black tentacles
    source: default
    freq: At will
  - is_mythic_spell: true
    name: desecrate
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dictum
    source: default
    freq: At will
    DC: 28
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: mindwipe
    source: default
    freq: At will
    DC: 25
  - is_mythic_spell: true
    name: modify memory
    source: default
    freq: At will
    DC: 25
  - is_mythic_spell: true
    name: order's wrath
    source: default
    freq: At will
    DC: 25
  - name: unhallow
    source: default
    freq: At will
  - name: wall of ice
    source: default
    freq: At will
  - name: feeblemind
    source: default
    freq: 3/day
    DC: 26
  - name: quickened mindwipe
    source: default
    freq: 3/day
    DC: 25
  - name: mislead
    source: default
    freq: 3/day
  - name: persistent image
    source: default
    freq: 3/day
    DC: 26
  - name: summon devils
    source: default
    freq: 3/day
  - name: vision
    source: default
    freq: 3/day
  - name: prediction of failure
    source: default
    freq: 1/day
    DC: 29
  - is_mythic_spell: true
    name: time stop
    source: default
    freq: 1/day
  - is_mythic_spell: true
    name: wish
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 29
    concentration: 40
    mythic_restriction: Geryon can use this ability's mythic version in its realm.
ability_scores:
  STR: 38
  DEX: 21
  CON: 42
  INT: 33
  WIS: 30
  CHA: 33
BAB: 34
CMB: 50
CMB_other: +54 disarm, trip
CMD: 84
CMD_other: 86 vs.disarm, can't be tripped
feats:
- name: Blinding Critical
- name: Combat Expertise
- name: Critical Focus
- name: Double Slice
- name: Greater Disarm
- name: Greater Trip
- name: Improved Critical(flail, heavy shield, tail slap)
- name: Improved Disarm
- name: ImprovedInitiative
- name: Improved Shield Bash
- name: Improved Trip
- name: ImprovedTwo-Weapon Fighting
- name: Power Attack
- name: Quicken Spell-LikeAbility (mindwipe)
- name: Spellbreaker
- name: Two-Weapon Fighting
skills:
  Bluff: 48
  Diplomacy: 48
  Intimidate: 48
  Know. (arcana,dungeoneering): 45
  Know. (engineering): 45
  Know. (geography): 45
  Know. (history): 45
  Know. (local): 45
  Know. (nature,nobility): 45
  Know. (religion): 45
  Know. (planes): 48
  Linguistics: 48
  Perception: 47
  Sense Motive: 47
  Spellcraft: 48
  Swim: 21
languages:
- all (language mastery)
- telepathy 300 ft.
special_qualities:
- amphibious
- change shape (humanoid and serpentine;shapechange)
ecology:
  environment: any (Hell)
  organization: solitary (unique)
  treasure_type: triple
  treasure:
  - +5 arrow deflection bashing heavy steelshield
  - +5 cruel dispelling burst unholy flail
  - Horn of Lies,other treasure
special_abilities:
  Casterbane (Ex): Geryon's foresight allows it to counterspell using greater dispel
    magic as an immediate action, with a +4 bonus to counter or dispel divine spells.
    It gains Spellbreaker as a bonus feat, and a spellcaster who fails a concentration
    check to cast defensively become flat-footed to Geryon until the end of its next
    turn.
  Corrupting Caress (Su): A creature damaged by Geryon's natural attacks or melee
    weapons becomes unable to cast divine spells or activate domain powers, channel
    positive energy, or smite evil for 1 round (Will DC 38 negates). The duration
    stacks with multiple failed saves, but a creature that successfully saves cannot
    be further targeted by Geryon's corrupting caress for 24 hours. This is a curse
    effect. The save DC is Charisma-based.
  Envenomed Scales (Ex): Creatures that strike Geryon with melee touch attacks, unarmed
    strikes, or natural attacks are exposed to its poison, as are creatures that confirm
    a critical hit on Geryon with a piercing or slashing weapon in melee.
  Immune to Memory Loss (Ex): Geryon is immune to the effects of the River Styx and
    to all effects that cause memory loss or manipulate memories.
  Perceive Destiny (Su): As an immediate action, Geryon can train its threefold gaze
    upon a creature to perceive its past, present, and future, granting Geryon a +4
    insight bonus to its AC and on attack rolls, opposed skill checks, and Reflex
    saves against that creature and attacks or effects created by that creature until
    the end of its next turn. This affects creatures using mind blank, nondetection,
    or similar protection from divination only if Geryon succeeds at a caster level
    check (DC = 11 + the effect's caster level + the mythic tier of the caster, for
    mythic effects).
  Poison (Ex): Tail slap-injury; save Fort DC 43; frequency 1/round for 6 rounds;
    effect 1d6 Int drain; cure 3 saves.
  Threefold Body (Ex): Geryon's vital organs and senses are spread across all three
    of its linked bodies. An effect that would cause it to become blinded or deafened
    instead affects only one of its bodies, unless it affects an area or targets each
    body as a separate creature. If one body is blinded or deafened, Geryon suffers
    no ill effects. If two bodies are blinded or deafened, it loses its all-around
    vision and is dazzled. Geryon is blinded or deafened only if all three bodies
    are blinded or deafened. It likewise has a 75% chance to ignore critical hits,
    sneak attack damage, and similar precision-based damage.
desc_long: |-
  Geryon, the source of blasphemies, has ruled in Hell longer than any other archdevil. When Asmodeus and his legions migrated to Hell, Geryon reigned as an asura rana, an emperor among divine mistakes. After bargaining with Asmodeus, Geryon betrayed its brethren, assuring devilkind's stranglehold over Hell and cementing its continued rule over the bleak marshes of Stygia. Ever since, Geryon has numbered among Hell's greatest and most enigmatic rulers, a connoisseur of impossible truths and a font of heresies. 

  Geryon is a knot of three 20-foot-long, scaled worms. From its maws it can partially regurgitate and speak with the voices of any being it has ever devoured-be they mortals, fiends, or stranger eldritch beings. As a result of its covenant with Asmodeus, Geryon is now a true devil.

---

# Archdevil, Geryon
This tripartite being has three humanoid bodies engulfed from

the waist down by a tangle of three immense serpents.
**Source** Bestiary 6 pg. 24
**XP** 6,553,600

LE Huge outsider (aquatic, devil, evil, extraplanar, lawful)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Good|detect good]]_,

_[[universal monster rules/Scent|scent]]_, _[[universal monster rules/See in Darkness|see in darkness]]_, _[[spells/True Seeing|true seeing]]_; Perception +47
**Aura** _[[universal monster rules/Frightful Presence|frightful presence]]_ (120 ft., DC 38), _[[spells/Shield of Law|shield of law]]_ (DC 29)

##### Defense

**AC** 47, touch 32, _[[conditions/Flat-Footed|flat-footed]]_ 42 (+4 deflection, +5 Dex,

+8 natural, +15 profane, +7 _[[spells/Shield|shield]]_, –2 size)
**hp** 731 (34d10+544); _[[universal monster rules/Regeneration|regeneration]]_ 30 (deific or mythic)
**Fort** +31, **Ref** +28, **Will** +33; +8 vs. mind-affecting effects
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, envenomed scales,

infernal _[[spells/Resurrection|resurrection]]_, _[[spells/Mind Blank|mind blank]]_, threefold body; **DR** 20/

epic, good, and silver; **Immune** ability damage, ability drain,

charm, cold, compulsion, death effects, _[[universal monster rules/Energy Drain|energy drain]]_, fire,

memory loss effects, petrification, poison; **Resist** acid 30; **SR** 40

##### Offense
**Speed** 50 ft., swim 50 ft., _[[spells/Air Walk|air walk]]_
**Melee** +5 _[[items/Weapon Magic Abilities/Cruel|cruel]]_ _[[items/Weapon Magic Abilities/Dispelling Burst|dispelling burst]]_ _[[items/Weapon Magic Abilities/Unholy|unholy]]_ flail +47/+42/+37/+32

(3d6+19/19–20), +1 heavy _shield_ +43/+38 (2d6+15/19–20),

3 claws +41 (1d6+7), 3 tail slaps +41 (2d6+7/19–20 plus poison)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** casterbane, corrupting caress, perceive destiny
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 29th; concentration +40)
Constant—_air walk_, _detect chaos_, _detect good_, _mind blank_, _shield of law_ (DC 29), _true seeing_ 
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Black Tentacles|black tentacles]]_, _[[spells/Desecrate|desecrate]]_, _[[spells/Dictum|dictum]]_ (DC 28), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Mindwipe|mindwipe]]_ (DC 25), _[[spells/Modify Memory|modify memory]]_ (DC 25), order’s wrath (DC 25), _[[spells/Unhallow|unhallow]]_, _[[spells/Wall Of Ice|wall of ice]]_ 
3/day—_[[spells/Feeblemind|feeblemind]]_ (DC 26), quickened _mindwipe_ (DC 25), _[[spells/Mislead|mislead]]_, _[[spells/Persistent Image|persistent image]]_ (DC 26), _[[universal monster rules/Summon|summon]]_ devils, _[[spells/Vision|vision]]_ 
1/day—_[[spells/Prediction of Failure|prediction of failure]]_ (DC 29), _[[spells/Time Stop|time stop]]_, _[[spells/Wish|wish]]_ 
 Geryon can use this ability’s mythic version in its realm.

##### Statistics
**Str** 38, **Dex** 21, **Con** 42, **Int** 33, **Wis** 30, **Cha** 33
**Base Atk** +34; **CMB** +50 (+54 disarm, _[[universal monster rules/Trip|trip]]_); **CMD** 84 (86 vs.

disarm, can’t be tripped)
**Feats** _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Double Slice|Double Slice]]_, _[[feats/Greater Disarm|Greater Disarm]]_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Critical|Improved Critical]]_

(flail, heavy _shield_, tail slap), _[[feats/Improved Disarm|Improved Disarm]]_, Improved

Initiative, _[[feats/Improved _Shield_ Bash|Improved _Shield_ Bash]]_, _[[feats/Improved Trip|Improved Trip]]_, Improved

_[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Power Attack|Power Attack]]_, Quicken Spell-Like

Ability (_mindwipe_), _[[items/Weapon/Spellbreaker|Spellbreaker]]_, _Two-Weapon Fighting_
**Skills** Bluff +48, Diplomacy +48, Intimidate +48, Know. (arcana,

dungeoneering, engineering, geography, history, local, nature,

nobility, religion) +45, Know. (planes) +48, Linguistics +48,

Perception +47, Sense Motive +47, Spellcraft +48, Swim +21
**Languages** all (language mastery); _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** _[[universal monster rules/Amphibious|amphibious]]_, _[[universal monster rules/Change Shape|change shape]]_ (humanoid and serpentine;

_[[spells/Shapechange|shapechange]]_)

##### Ecology

**Environment** any (Hell)
**Organization** solitary (unique)
**Treasure** triple (+5 _[[items/Armor Magic Abilities/Arrow Deflection|arrow deflection]]_ _[[items/Armor Magic Abilities/Bashing|bashing]]_ heavy steel

_shield_, +5 _cruel_ _dispelling burst_ _unholy_ flail, _[[items/Wondrous Item/Horn of Lies|Horn of Lies]]_,

other treasure)

### Special Abilities

**Casterbane (Ex)** Geryon’s _[[spells/Foresight|foresight]]_ allows it to counterspell using greater _[[spells/Dispel Magic|dispel magic]]_ as an immediate action, with a +4 bonus to counter or dispel divine spells. It gains _Spellbreaker_ as a bonus feat, and a spellcaster who fails a concentration check to cast defensively become _flat-footed_ to Geryon until the end of its next turn.

**Corrupting Caress (Su)** A creature damaged by Geryon’s _[[universal monster rules/Natural Attacks|natural attacks]]_ or melee weapons becomes unable to cast divine spells or activate domain powers, channel positive energy, or smite evil for 1 round (Will DC 38 negates). The duration stacks with multiple failed saves, but a creature that successfully saves cannot be further targeted by Geryon’s corrupting caress for 24 hours. This is a curse effect. The save DC is Charisma-based.

**Envenomed Scales (Ex)** Creatures that strike Geryon with melee touch attacks, unarmed strikes, or _natural attacks_ are exposed to its poison, as are creatures that confirm a critical hit on Geryon with a piercing or slashing weapon in melee.

**Immune to Memory Loss (Ex)** Geryon is immune to the effects of the River Styx and to all effects that cause memory loss or manipulate memories.

**Perceive Destiny (Su)** As an immediate action, Geryon can train its threefold _[[universal monster rules/Gaze|gaze]]_ upon a creature to perceive its past, present, and future, granting Geryon a +4 insight bonus to its AC and on attack rolls, opposed skill checks, and Reflex saves against that creature and attacks or effects created by that creature until the end of its next turn. This affects creatures using _mind blank_, _[[spells/Nondetection|nondetection]]_, or similar protection from _[[spells/Divination|divination]]_ only if Geryon succeeds at a caster level check (DC = 11 + the effect’s caster level + the mythic tier of the caster, for mythic effects).

**Poison (Ex)** Tail slap—injury; save Fort DC 43; frequency 1/round for 6 rounds; effect 1d6 Int drain; cure 3 saves.

**Threefold Body (Ex)** Geryon’s vital organs and senses are spread across all three of its linked bodies. An effect that would cause it to become _[[conditions/Blinded|blinded]]_ or _[[conditions/Deafened|deafened]]_ instead affects only one of its bodies, unless it affects an area or targets each body as a separate creature. If one body is _blinded_ or _deafened_, Geryon suffers no ill effects. If two bodies are _blinded_ or _deafened_, it loses its _all-around vision_ and is _[[conditions/Dazzled|dazzled]]_. Geryon is _blinded_ or _deafened_ only if all three bodies are _blinded_ or _deafened_. It likewise has a 75% chance to ignore critical hits, sneak attack damage, and similar precision-based damage.

##### Description

Geryon, the source of blasphemies, has ruled in Hell longer than any other archdevil. When Asmodeus and his legions migrated to Hell, Geryon reigned as an asura rana, an emperor among divine mistakes. After bargaining with Asmodeus, Geryon _[[feats/Betrayed|betrayed]]_ its brethren, assuring devilkind’s stranglehold over Hell and cementing its continued rule over the bleak marshes of Stygia. Ever since, Geryon has numbered among Hell’s greatest and most enigmatic rulers, a connoisseur of impossible truths and a font of heresies.

Geryon is a knot of three 20-foot-long, scaled worms. From its maws it can partially regurgitate and speak with the voices of any being it has ever devoured—be they mortals, fiends, or stranger eldritch beings. As a result of its covenant with Asmodeus, Geryon is now a true devil.