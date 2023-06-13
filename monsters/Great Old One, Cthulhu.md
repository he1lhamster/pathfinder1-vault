---
cssclass: [monsters]
title1: Great Old One, Cthulhu
desc_short: This towering impossibility, neither quite octopus nor dragon nor giant
  but something far worse, must surely herald the end of times.
title2: Cthulhu
CR: 30
sources:
- name: Bestiary 4
  page: 138
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 9830400
alignment: CE
size: Colossal
type: aberration
subtypes:
- chaotic
- evil
- Great Old One
initiative:
  bonus: 15
senses:
  darkvision: 60
  true seeing: true
auras:
- name: unspeakable presence
  radius: 300
  DC: 40
AC:
  AC: 49
  touch: 29
  flat_footed: 44
  components:
    deflection: 12
    dex: 5
    insight: 10
    natural: 20
    size: -8
HP:
  HP: 774
  long: 36d8+612
  fast_healing: 30
saves:
  fort: 29
  ref: 29
  will: 33
defensive_abilities:
- freedom of movement
- immortality
- insanity (DC 40)
- non-euclidean
DR:
- amount: 20
  weakness: epic and lawful
immunities:
- ability damage
- ability drain
- aging
- cold
- death effects
- disease
- energy drain
- mind-affecting effects
- paralysis
- petrification
resistances:
  acid: 30
  electricity: 30
  fire: 30
  sonic: 30
SR: 41
speeds:
  base: 60
  fly: 200
  fly_maneuverability: average
  swim: 60
attacks:
  melee:
  - - text: 2 claws +42 (4d6+23/19-20 plus grab)
      entries:
      - - damage: 4d6+23
          crit_range: 19-20
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 42
    - text: 4 tentacles +42 (2d10+34/19-20 plus grab)
      entries:
      - - damage: 2d10+34
          crit_range: 19-20
        - effect: grab
      count: 4
      attack: tentacles
      bonus:
      - 42
  special:
  - cleaving claws
  - constrict (3d6+23)
  - dreams of madness
  - mythic power (10/day, surge +1d12)
  - powerful blows (tentacle)
  - tentacles
  - trample (2d8+30, DC 51)
space: 40
reach: 40
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: astral projection
    source: default
    freq: At will
  - is_mythic_spell: true
    name: control weather
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dream
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - name: insanity
    source: default
    freq: At will
    DC: 29
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
    DC: 29
  - is_mythic_spell: true
    name: sending
    source: default
    freq: At will
  - name: antipathy
    source: default
    freq: 3/day
    DC: 30
  - name: demand
    source: default
    freq: 3/day
    DC: 30
  - name: quickened feeblemind
    source: default
    freq: 3/day
  - name: gate
    source: default
    freq: 3/day
  - name: weird
    source: default
    freq: 3/day
    DC: 31
  - name: implosion
    source: default
    freq: 1/day
    DC: 31
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: star-spawn of Cthulhu
      amount: 2d4
      chance: 100%
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 30
  - is_mythic_spell: true
    name: wish
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 30
    concentration: 42
ability_scores:
  STR: 56
  DEX: 21
  CON: 45
  INT: 31
  WIS: 36
  CHA: 34
BAB: 27
CMB: 58
CMB_other: +60 bull rush, +62 grapple or sunder
CMD: 97
CMD_other: 99 vs. bull rush or sunder
feats:
- name: Ability Focus (nightmare)
- name: Awesome Blow
- name: Combat Reflexes
- name: Craft Wondrous Item
- name: Critical Focus
- name: Flyby Attack
- name: Greater Sunder
- name: Greater Vital Strike
- name: Hover
- name: Improved Bull Rush
- name: Improved Critical (claw)
- name: Improved Critical (tentacle)
- name: Improved Sunder
- name: Improved Vital Strike
- name: Power Attack
- name: Quicken Spell-Like Ability (feeblemind)
- name: Staggering Critical
- name: Vital Strike
skills:
  Fly: 36
  Knowledge (arcana): 49
  Knowledge (dungeoneering): 46
  Knowledge (engineering): 46
  Knowledge (geography): 46
  Knowledge (history): 46
  Knowledge (nature): 46
  Knowledge (planes): 46
  Knowledge (religion): 46
  Perception: 52
  Sense Motive: 49
  Spellcraft: 49
  Swim: 70
  Use Magic Device: 48
languages:
- Aklo
- telepathy 300 ft.
special_qualities:
- compression
- greater starflight
- otherworldly insight
ecology:
  environment: any (R'lyeh)
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Cleaving Claws (Ex): A single attack from one of Cthulhu's claws can target all
    creatures in a 10-foot square. Make one attack roll; any creature in the area
    whose AC is equal to or lower than the result takes damage from the claw.
  Dreams of Madness (Su): When Cthulhu uses his nightmare spell-like ability on a
    creature with one or more ranks in a Craft or Perform skill, he also afflicts
    the creature with maddening dreams. In addition to the effect of nightmare, the
    target must succeed at a DC 40 Will save or contract a random insanity (Pathfinder
    RPG GameMastery Guide 250). This is a mind-affecting effect. A creature that already
    has an insanity is immune to this ability. The save DC is Charisma-based.
  Greater Starflight (Su): Cthulhu can survive in the void of outer space, and flies
    through outer space at incredible speeds. Although the exact travel time will
    vary from one trip to the next, a trip within a solar system normally takes Cthulhu
    2d6 hours, and a trip beyond normally takes 2d6 days (or more, at the GM's discretion).
  Immortality (Ex): If Cthulhu is killed, his body immediately fades away into a noxious
    cloud of otherworldly vapor that fills an area out to his reach. This cloud blocks
    vision as obscuring mist, but can't be dispersed by any amount of wind. Any creature
    in this area must succeed at a DC 45 Fortitude save or be nauseated for as long
    as it remains in the cloud and for an additional 1d10 rounds after it leaves the
    area. Cthulhu returns to life after 2d6 rounds, manifesting from the cloud and
    restored to life via true resurrection, but is staggered for 2d6 rounds (nothing
    can remove this staggered effect). If slain again while he is staggered from this
    effect, Cthulhu reverts to vapor form again and his essence fades away after 2d6
    rounds, returning to his tomb in R'lyeh until he is released again. The save DC
    is Constitution-based.
  Non-Euclidean (Ex): Cthulhu does not exist wholly in the physical world, and space
    and time strain against his presence. This grants Cthulhu a deflection bonus to
    AC and a racial bonus on Reflex saves equal to his Charisma modifier (+12). His
    apparent and actual position are never quite the same, granting him a 50% miss
    chance against all attacks. True seeing can defeat this miss chance, but any creature
    that looks upon Cthulhu while under the effects of true seeing must succeed at
    a DC 40 Will save or be afflicted by a random insanity (this is a mind-affecting
    effect). The save DC is Charisma-based.
  Tentacles (Ex): Cthulhu's tentacles are a primary attack.
  Unspeakable Presence (Su): Failing a DC 40 Will save against Cthulhu's unspeakable
    presence causes the victim to immediately die of fright. This is a death and fear
    effect. A creature immune to fear that fails its save against Cthulhu's unspeakable
    presence is staggered for 1d6 rounds instead of killed. The save DC is Charisma-based.
desc_long: |-
  Known to some as the Dreamer in the Deep, Great Cthulhu is the mightiest of the Great Old Ones. Cthulhu is represented often in artwork-particularly in sculpture, painting, and poetry, for his influence is particularly strong among such sensitive and creative minds. In these eldritch works of art, he is depicted or described as having a vaguely humanoid frame, but with immense draconic wings and an octopus-shaped head. His actual form is somewhat fluid-the Great Old One can shift and reshape his exact countenance as he wills, allowing him to occupy a smaller space than one might expect for a creature that stands over 100 feet tall.

  It is fortunate indeed that Cthulhu is currently imprisoned on a distant planet within the sunken city of R'lyeh. There, the Great Old One slumbers away the eons in a state neither quite dead nor living, held in stasis by ancient magic and the potency of the Elder Sign, yet at times the city rises from the sea and the doors to his tomb open, granting Cthulhu limited mobility before he must return to his tomb.

---

# Great Old One, Cthulhu
This towering impossibility, neither quite _[[monsters/Octopus|octopus]]_ nor dragon nor giant but something far worse, must surely herald the end of times.
**Source** Bestiary 4 pg. 138
**XP** 9,830,400
CE Colossal aberration (chaotic, evil, Great Old One)
**Init** +15; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +52
**Aura** unspeakable presence (300 ft., DC 40)

##### Defense

**AC** 49, touch 29, _[[conditions/Flat-Footed|flat-footed]]_ 44 (+12 deflection, +5 Dex, +10 insight, +20 natural, –8 size)
**hp** 774 (36d8+612); _[[universal monster rules/Fast Healing|fast healing]]_ 30
**Fort** +29, **Ref** +29, **Will** +33
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, immortality, _[[spells/Insanity|insanity]]_ (DC 40), non-euclidean; **DR** 20/epic and lawful; **Immune** ability damage, ability drain, aging, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, and petrification; **Resist** acid 30, electricity 30, fire 30, sonic 30; **SR** 41

##### Offense
**Speed** 60 ft., fly 200 ft. (average), swim 60 ft.
**Melee** 2 claws +42 (4d6+23/19–20 plus _[[universal monster rules/Grab|grab]]_), 4 tentacles +42 (2d10+34/19–20 plus _grab_)
**Space** 40 ft., **Reach** 40 ft.
**Special Attacks** cleaving claws, _[[universal monster rules/Constrict|constrict]]_ (3d6+23), dreams of madness, mythic power (10/day, surge +1d12), powerful blows (tentacle), tentacles, _[[universal monster rules/Trample|trample]]_ (2d8+30, DC 51)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 30th; concentration +42)
Constant—_freedom of movement_, _true seeing_
At will—_[[spells/Astral Projection|astral projection]]_, _[[spells/Control Weather|control weather]]_, _[[spells/Dream|dream]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _insanity_ (DC 29), _[[spells/Nightmare|nightmare]]_ (DC 29), _[[spells/Sending|sending]]_
3/day—_[[spells/Antipathy|antipathy]]_ (DC 30), _[[spells/Demand|demand]]_ (DC 30), quickened _[[spells/Feeblemind|feeblemind]]_, _[[spells/Gate|gate]]_, _[[spells/Weird|weird]]_ (DC 31)
1/day—_[[spells/Implosion|implosion]]_ (DC 31), _[[universal monster rules/Summon|summon]]_ (level 9, 2d4 _[[monsters/Star-Spawn of Cthulhu|star-spawn of Cthulhu]]_ 100%), _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 30), _[[spells/Wish|wish]]_

##### Statistics
**Str** 56, **Dex** 21, **Con** 45, **Int** 31, **Wis** 36, **Cha** 34
**Base Atk** +27; **CMB** +58 (+60 bull rush, +62 grapple or sunder); **CMD** 97 (99 vs. bull rush or sunder)
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_nightmare_), _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _Improved Critical_ (tentacle), _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_feeblemind_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +36, Knowledge (arcana) +49, Knowledge (dungeoneering, engineering, geography, history, nature, planes, religion) +46, Perception +52, Sense Motive +49, Spellcraft +49, Swim +70, Use Magic Device +48
**Languages** Aklo; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** _[[universal monster rules/Compression|compression]]_, greater starflight, otherworldly insight

##### Ecology

**Environment** any (R’lyeh)
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Cleaving Claws (Ex)** A single attack from one of Cthulhu’s claws can target all creatures in a 10-foot square. Make one attack roll; any creature in the area whose AC is equal to or lower than the result takes damage from the claw.

**Dreams of Madness (Su)** When Cthulhu uses his _nightmare_ spell-like ability on a creature with one or more ranks in a Craft or Perform skill, he also afflicts the creature with maddening dreams. In addition to the effect of _nightmare_, the target must succeed at a DC 40 Will save or contract a random _insanity_ (Pathfinder RPG GameMastery Guide 250). This is a mind-affecting effect. A creature that already has an _insanity_ is immune to this ability. The save DC is Charisma-based.

**Greater Starflight (Su)** Cthulhu can survive in the void of outer space, and flies through outer space at incredible speeds. Although the exact travel time will vary from one _[[universal monster rules/Trip|trip]]_ to the next, a _trip_ within a solar system normally takes Cthulhu 2d6 hours, and a _trip_ beyond normally takes 2d6 days (or more, at the GM’s discretion).

**Immortality (Ex)** If Cthulhu is killed, his body immediately fades away into a noxious cloud of otherworldly vapor that fills an area out to his reach. This cloud blocks _[[spells/Vision|vision]]_ as _[[spells/Obscuring Mist|obscuring mist]]_, but can’t be dispersed by any amount of wind. Any creature in this area must succeed at a DC 45 Fortitude save or be _[[conditions/Nauseated|nauseated]]_ for as long as it remains in the cloud and for an additional 1d10 rounds after it leaves the area. Cthulhu returns to life after 2d6 rounds, manifesting from the cloud and restored to life via _[[spells/True Resurrection|true resurrection]]_, but is _[[conditions/Staggered|staggered]]_ for 2d6 rounds (nothing can remove this _staggered_ effect). If slain again while he is _staggered_ from this effect, Cthulhu reverts to vapor form again and his essence fades away after 2d6 rounds, returning to his tomb in R’lyeh until he is released again. The save DC is Constitution-based.

**Non-Euclidean (Ex)** Cthulhu does not exist wholly in the physical world, and space and time strain against his presence. This grants Cthulhu a _deflection_ bonus to AC and a racial bonus on Reflex saves equal to his Charisma modifier (+12). His apparent and actual position are never quite the same, granting him a 50% miss chance against all attacks. _True seeing_ can defeat this miss chance, but any creature that looks upon Cthulhu while under the effects of _true seeing_ must succeed at a DC 40 Will save or be afflicted by a random _insanity_ (this is a mind-affecting effect). The save DC is Charisma-based.

**Tentacles (Ex)** Cthulhu’s tentacles are a primary attack.

**Unspeakable Presence (Su)** Failing a DC 40 Will save against Cthulhu’s unspeakable presence causes the victim to immediately die of fright. This is a death and _[[universal monster rules/Fear|fear]]_ effect. A creature immune to _fear_ that fails its save against Cthulhu’s unspeakable presence is _staggered_ for 1d6 rounds instead of killed. The save DC is Charisma-based.

##### Description

Known to some as the Dreamer in the Deep, Great Cthulhu is the mightiest of the Great Old Ones. Cthulhu is represented often in artwork—particularly in sculpture, painting, and poetry, for his influence is particularly strong among such sensitive and creative minds. In these eldritch works of art, he is depicted or described as having a vaguely humanoid frame, but with immense draconic wings and an octopus-shaped head. His actual form is somewhat fluid—the Great Old One can shift and reshape his exact countenance as he wills, allowing him to occupy a smaller space than one might expect for a creature that stands over 100 feet tall.

It is fortunate indeed that Cthulhu is currently imprisoned on a distant planet within the sunken city of R’lyeh. There, the Great Old One slumbers away the eons in a state neither quite dead nor living, held in stasis by ancient magic and the potency of the _[[items/Wondrous Item/Elder Sign|Elder Sign]]_, yet at times the city rises from the sea and the doors to his tomb open, granting Cthulhu limited _[[feats/Mobility|mobility]]_ before he must return to his tomb.