---
cssclass: [monsters]
title1: Smoke Haunt
is_3.5: true
desc_short: The smell of wood smoke bears the taint of burning flesh. A branch in
  the campfire sputters and hisses. From within the fire's embers a smoldering skull
  glares out, its eyes wells of cold darkness. Tendrils of smoke dance around and
  through it like tongues or writhing snakes.
title2: Smoke Haunt
CR: 4
sources:
- name: 'Pathfinder #3: The Hook Mountain Massacre'
  page: 81
  link: http://paizo.com/pathfinder/adventurePath/riseOfTheRunelords/v5748btpy80e4
alignment: Always CE
size: Small
type: undead
subtypes:
- fire
initiative:
  bonus: 9
senses:
  darkvision: 60
auras:
- name: lifedrinking
  radius: 20
- name: smoke patterns
  radius: 20
AC:
  AC: 20
  touch: 20
  flat_footed: 15
  components:
    dexterity: 5
    natural: 4
    size: 1
HP:
  HP: 39
  long: 6d12
saves:
  fort: 2
  ref: 9
  will: 7
defensive_abilities:
- undead traits
immunities:
- fire
weaknesses:
- vulnerable to cold
speeds:
  fly: 50
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: slam +9 (1d3 plus 2d6 negative energy)
      entries:
      - - damage: 1d3
        - damage: 2d6
          type: negative energy
      attack: slam
      bonus:
      - 9
spell_like_abilities:
  entries:
  - name: ghost sound
    source: default
    freq: 3/day
    DC: 14
  - name: heat metal
    source: default
    freq: 3/day
    DC: 16
  - name: scorching ray
    source: default
    freq: 3/day
  - name: deep slumber
    source: default
    freq: 1/day
    DC: 17
  - name: fire shield
    source: default
    freq: 1/day
  - name: suggestion
    source: default
    freq: 1/day
    DC: 17
  sources:
  - name: default
    CL: 5
    touch_attack_ranged: 9
ability_scores:
  STR:
  DEX: 20
  CON:
  INT: 8
  WIS: 15
  CHA: 19
BAB: 3
grapple_3.5: '-'
feats:
- name: Dodge
- name: Improved Initiative
- name: Lightning Reflexes
skills:
  Hide: 18
  Move Silently: 14
  Tumble: 14
  Listen: 2
  Spot: 2
languages:
- Common
special_qualities:
- flameseer
- flamewalker
ecology:
  environment: cold forests and mountains
  organization: solitary
  treasure_type: none
  advancement_3.5:
  - type: size
    HD_min: 7
    size: Small
    HD_max: 18
special_abilities:
  Flameseer (Su): A smoke haunt can sense any fire of torch size or larger within
    a half mile. By concentrating, it can peer through such flames as if using clairaudience/clairvoyance.
  Flamewalker (Su): Once per day, a smoke haunt can use greater teleport to appear
    in any fire of Small size or larger. When a smoke haunt teleports into a fire,
    it can make a Hide check as part of the teleportation to avoid notice from any
    creatures nearby.
  Lifedrinking (Su): A smoke haunt feeds on the heat of the living. A haunt seems
    to shed soothing warmth, but this is actually the sensation of life being absorbed
    by the ravenous undead. Any living creature within 20 feet of a smoke haunt must
    make a DC 17 Fortitude save or take 2d6 points of negative energy damage. A victim
    who fails to resist this attack feels warm and complacent, having no idea he has
    taken any damage unless he makes a DC 15 Wisdom check. If a victim makes this
    save, he feels strangely weak, but does not necessarily notice the smoke haunt.
    The save DCs are Charisma-based.
  Smoke Patterns (Su): A smoke haunt exudes coils of smoke whenever it is surrounded
    by a fire of Small size or larger. Anyone within 20 feet of a smoke haunt immersed
    in fire must make a DC 17 Will save or become entranced by the eerie patterns
    formed amid the rising smoke, taking a -4 penalty on Listen and Spot checks and
    a -2 penalty on Will saves for as long as the smoke haunt remains in range. This
    is a mind-affecting pattern. A creature that successfully saves against this ability
    cannot be affected by the same smoke haunt's smoke patterns for 24 hours. The
    save DC is Charisma-based.
desc_long: Said to form from the spirits of lost wanderers slain by exposure and despair,
  smoke haunts hunger for life, warmth, and a home they're cursed to never find again.

---

# Smoke Haunt
The smell of wood smoke bears the taint of _[[items/Weapon Magic Abilities/Burning|burning]]_ flesh. A branch in the campfire sputters and hisses. From within the fire’s embers a smoldering skull glares out, its eyes wells of cold _[[spells/Darkness|darkness]]_. Tendrils of smoke dance around and through it like _[[spells/Tongues|tongues]]_ or writhing snakes.
**Source** Pathfinder #3: The Hook Mountain _[[spells/Massacre|Massacre]]_ pg. 81
Always CE Small undead (fire) 
**Init** +9 ; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Listen +2, Spot +2 
**Aura** lifedrinking (20 ft.), smoke patterns (20 ft.)

##### Defense

**AC** 20, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 Dexterity, +4 natural, +1 size) 
**hp** 39 (6d12) 
**Fort** +2 , **Ref** +9 , **Will** +7 
**Defensive Abilities** _[[universal monster rules/Undead Traits|undead traits]]_; **Immune** fire 
**Weaknesses** vulnerable to cold

##### Offense
**Speed** fly 50 ft. (perfect) 
**Melee** slam +9 (1d3 plus 2d6 negative energy) 
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th, +9 ranged)
3/day - _[[spells/Ghost Sound|ghost sound]]_ (DC 14), _[[spells/Heat Metal|heat metal]]_ (DC 16), _[[spells/Scorching Ray|scorching ray]]_
1/day - _[[spells/Deep Slumber|deep slumber]]_ (DC 17), _[[spells/Fire Shield|fire shield]]_, _[[spells/Suggestion|suggestion]]_ (DC 17)

##### Statistics
**Str** —, **Dex** 20 , **Con** —, **Int** 8 , **Wis** 15 , **Cha** 19 
**Base Atk** +3 ; **Grapple** —
**Feats** Dodge, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Hide +18, Move Silently +14, Tumble +14 
**Languages** Common 
**SQ** flameseer, flamewalker

##### Ecology

**Environment** cold forests and mountains 
**Organization** solitary 
**Treasure** none 
**Advancement** 7-18 HD (Small)

### Special Abilities

**Flameseer (Su)** A _[[monsters/Smoke Haunt|smoke haunt]]_ can sense any fire of _[[items/Mundane/Torch|torch]]_ size or larger within a half mile. By concentrating, it can peer through such flames as if using clairaudience/clairvoyance.

**Flamewalker (Su)** Once per day, a _smoke haunt_ can use greater teleport to appear in any fire of Small size or larger. When a _smoke haunt_ teleports into a fire, it can make a Hide check as part of the teleportation to avoid notice from any creatures nearby.

**Lifedrinking (Su)** A _smoke haunt_ feeds on the _[[universal monster rules/Heat|heat]]_ of the living. A haunt seems to shed soothing warmth, but this is actually the sensation of life being absorbed by the _[[curses/Ravenous|ravenous]]_ undead. Any living creature within 20 feet of a _smoke haunt_ must make a DC 17 Fortitude save or take 2d6 points of negative energy damage. A victim who fails to resist this attack feels warm and complacent, having no idea he has taken any damage unless he makes a DC 15 Wisdom check. If a victim makes this save, he feels strangely weak, but does not necessarily notice the _smoke haunt_. The save DCs are Charisma-based.
**Smoke Patterns (Su)** A _smoke haunt_ exudes coils of smoke whenever it is surrounded by a fire of Small size or larger. Anyone within 20 feet of a _smoke haunt_ immersed in fire must make a DC 17 Will save or become entranced by the eerie patterns formed amid the rising smoke, taking a –4 penalty on Listen and Spot checks and a –2 penalty on Will saves for as long as the _smoke haunt_ remains in range. This is a mind-affecting pattern. A creature that successfully saves against this ability cannot be affected by the same _smoke haunt_’s smoke patterns for 24 hours. The save DC is Charisma-based.

##### Description

Said to form from the spirits of lost wanderers slain by exposure and despair, smoke haunts hunger for life, warmth, and a home they’re cursed to never find again.