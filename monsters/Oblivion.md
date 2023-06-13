---
cssclass: [monsters]
title1: Oblivion
desc_short: A single sinister eye glares from the heart of this roiling cloud ofdarkness
  as tentacles of smoke coil and writhe beneath it.
title2: Oblivion
CR: 20
sources:
- name: Bestiary 6
  page: 202
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 307200
alignment: NE
size: Colossal
type: ooze
initiative:
  bonus: 17
senses:
  blindsight: 120
  see in darkness: true
auras:
- name: dubiety
  radius: 60
AC:
  AC: 36
  touch: 15
  flat_footed: 23
  components:
    dex: 13
    natural: 21
    size: -8
HP:
  HP: 377
  long: 26d8+260
  regeneration: 15
  regeneration_weakness: positive energy or inspiration
saves:
  fort: 20
  ref: 23
  will: 19
defensive_abilities:
- all-around vision
- negative energy affinity
DR:
- amount: 15
  weakness: epic and good
immunities:
- annihilation
- banishment,electricity
- ooze traits
resistances:
  fire: 30
SR: 31
weaknesses:
- susceptible to creation
- talisman of the sphere
speeds:
  base: 30
  burrow: 30
  fly: 30
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 4 slams +27 (2d8+16/19-20 plus 2d6 negative energyand grab)
      entries:
      - - damage: 2d8+16
          crit_range: 19-20
        - damage: 2d6
          type: negative energyand grab
      count: 4
      attack: slams
      bonus:
      - 27
  special:
  - annihilation
  - constrict (4d8+24)
  - servants of entropy
space: 30
reach: 60
spell_like_abilities:
  entries:
  - name: deeper darkness
    source: default
    freq: At will
  - name: disintegrate
    source: default
    freq: At will
    DC: 21
  - name: quickened disintegrate
    source: default
    freq: 3/day
    DC: 21
  - name: time stop
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 25
ability_scores:
  STR: 43
  DEX: 36
  CON: 31
  INT: 7
  WIS: 28
  CHA: 21
BAB: 19
CMB: 43
CMD: 66
feats:
- name: Blinding Critical
- name: Combat Reflexes
- name: Critical Focus
- name: FlybyAttack
- name: Great Fortitude
- name: Improved Critical (slam)
- name: ImprovedInitiative
- name: Improved Vital Strike
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (disintegrate)
- name: Vital Strike
skills:
  Fly: 21
  Knowledge (planes): 3
  Perception: 17
  Stealth: 21
  _racial_mods:
    Stealth:
      _: 16
languages:
- Common (cannot speak)
- telepathy 100 ft.
special_qualities:
- compression
- master of annihilation
ecology:
  environment: any (Negative Energy Plane)
  organization: solitary
  treasure_type: none
special_abilities:
  Annihilation (Su): Any spaces an oblivion moves through are left fallow and lifeless
    in its wake. Ground that it moves over using its base speed becomes barren and
    is treated as if affected by a diminish plants spell to stunt growth. Dead bodies
    that the oblivion moves through immediately crumble into dust. Any constrict damage
    an oblivion deals to a creature automatically bypasses all damage reduction. A
    creature reduced to 0 or fewer hit points by this constrict damage is immediately
    slain and its remains (but not its gear) are disintegrated. Once per round as
    a free action, an oblivion can target a single object in its space. A non-magical
    object so targeted is immediately destroyed. A magical item must succeed at a
    DC 33 Fortitude save or be destroyed. The save DC is Constitution-based.
  Aura of Dubiety (Su): An oblivion's presence is anathema to the gods and the forces
    that bind creation together. Its presence warps divine magic and severs living
    beings from the power of life. Any living creature that begins its turn within
    range of an oblivion's aura of dubiety takes 2d6 points of negative energy damage.
    This negative energy has no beneficial effect on undead. A creature attempting
    to cast a divine spell within 60 feet of an oblivion must succeed at a concentration
    check as if casting defensively (DC = 15 + double the spell level) or the spell
    is automatically subverted, allowing the oblivion to decide the spell's target
    and effect as if it were the original caster. If the affected spell uses positive
    energy, the subverted spell instead uses negative energy.
  Immunity to Annihilation (Ex): An oblivion is immune to destruction spells, disintegrate
    effects, spheres of annihilation, and similar effects that completely destroy
    living creatures.
  Immunity to Banishment (Ex): An oblivion is never treated as having the extraplanar
    subtype, regardless of what plane it currently inhabits, rendering it immune to
    banishment, dismissal, and similar effects. In addition to this, effects that
    force the oblivion onto another plane (such as plane shift or the violet beam
    of a prismatic spray) do not function against an oblivion unless the effect comes
    from an artifact, a creature capable of granting spells to its worshipers, or
    a mythic source.
  Master of Annihilation (Ex): An oblivion can establish control over a sphere of
    annihilation (Pathfinder RPG Core Rulebook 545) as far away as 100 feet. When
    an oblivion controls a sphere of annihilation, it does so through force of will
    and an inborn understanding of the sphere's reality-the oblivion's control check
    is 1d20 + the oblivion's Hit Dice + its Charisma modifier (the typical oblivion
    has a control check bonus of +31, and thus can never fail to control a sphere
    of annihilation unless control of the sphere is opposed). When an oblivion establishes
    control, it can maintain control at a distance of 100 feet + 20 feet per Hit Die
    (620 feet for the typical oblivion), and the sphere's speed under the oblivion's
    control is 20 feet + 5 feet for every 5 points by which the oblivion's control
    check result in that round exceeded 30.
  Servants of Entropy (Su): As a full-round action, an oblivion can reform any living
    creature it has slain within the past hour, forging an obedient duplicate from
    its own dark mass. Servants created in this manner are identical to their original
    forms, with all their associated memories, racial abilities, and class abilities,
    except the duplicate loses any divine spellcasting ability its original form had.
    A servant's alignment changes to neutral evil, its type changes to native outsider
    (do not recalculate hit points, saving throws, or similar abilities), and it gains
    negative energy affinity. An oblivion can communicate telepathically with its
    servants anywhere on the same plane and can destroy a servant as a free action.
    An oblivion can manifest a total number of Hit Dice worth of servants equal to
    twice its own Hit Dice (52 for a typical oblivion), but no single servant can
    have more Hit Dice than the oblivion's CR. An oblivion cannot manifest more than
    one copy of any given creature at one time.
  Susceptible to Creation (Ex): An oblivion is a manifestation of disbelief and decay,
    and the forces of compassion and creativity are anathema to it. It is vulnerable
    to positive energy, taking damage as if it were undead, though it retains its
    control over any divine spells, allowing it to often usurp and corrupt cure spells
    and similar curative magic. An oblivion loses its regeneration any round in which
    it either takes damage from positive energy or is within 30 feet of a creature
    that succeeds at a DC 35 Perform check. Creatures under the effect of a good hope
    spell, an inspire courage bardic performance, or any spell effect of 5th level
    or higher that grants a morale bonus gain immunity to the negative energy damage
    dealt by an oblivion's slams and aura of dubiety.
  Talisman of the Sphere (Ex): The talisman of the sphere is anathema to an oblivion.
    A character who carries a talisman of the sphere can penetrate an oblivion's damage
    reduction with ease, ignores its spell resistance, is immune to its aura, and
    gains a +10 bonus on saving throws against the oblivion's special attacks and
    spell-like abilities.
desc_long: |-
  Rare and powerful denizens of the Negative Energy Plane, oblivions are void and nothingness given terrible will. They lurk among crystalline sheets of accumulated entropy that line their home plane's darkest interior, hungering to unmake the walls of reality and drag all of the cosmos down to its eventual end, allowing themselves to also finally end. Once unleashed upon mortal worlds, oblivions crisscross the globe, destroying its denizens and laying waste to the land until destroyed themselves or until they strip a planet bare of substance, life, and heat. Despite its vast bulk, a single oblivion must often dedicate years or even centuries to ending a world, and each is so adept at scrubbing away all traces a being leaves upon the cosmos that people, nations, and entire worlds annihilated by an oblivion are soon forgotten by outsiders. Some gods claim that the brutal efficiency of the oblivions are intended to someday be released upon the multiverse to cleanse away creation so a new cycle of life can begin from chaotic nothing, while other deities insist the oblivions' work is nearly complete, leaving only isolated specks of life floating in a vast, unfeeling void. 

  Unlike nightshades (Pathfinder RPG Bestiary 2 199) or other noteworthy denizens of their dark realm, oblivions serve no masters or agendas. They believe themselves to be the way all things must end. Though cunning, they rarely find reason to communicate with other creatures, leaving much of their motives, origins, and philosophy in the cosmos a mystery. 

  Like grim doll makers, oblivions can recreate slain victims from their own dark substance, transforming a world's heroes and villains into hollow pawns they can dispatch to slay would-be heroes or undermine organized resistance. Lacking any inherent ability to traverse the planes, most oblivions rely on such servants created in the shapes of powerful spellcasters or outsiders to provide routes to new worlds. These hollow reproductions know little of their masters' will beyond sharing comfort in the coming end of days, and most desperately fill in the gaps with appealing philosophies. Some of the most powerful servants form doomsday cults on distant planets to prepare them for an oblivion's arrival. 

  Oblivions share a symbiosis with the artifacts known as spheres of annihilation, coveting their powerful, highly destructive magic. The towering oozes are unaffected by the artifact's destructive powers, and can move them as easily as a child might carry a toy. Some speculate that the spheres are in fact the eggs or spores of these apocalyptic beings, as rare survivors recount tales of spheres spontaneously birthing the roiling, devouring entities. 

  Oblivions typically measure several dozen feet across, though their presence corrupts and consumes life, making the roiling darkness that most people mistake for their bodies seem much larger. Despite their size, oblivions have no mass. Upon destruction, an oblivion collapses thunderously into nothing

---

# Oblivion
A single sinister eye glares from the heart of this roiling cloud of

_[[spells/Darkness|darkness]]_ as tentacles of smoke coil and writhe beneath it.
**Source** Bestiary 6 pg. 202
**XP** 307,200

NE Colossal ooze
**Init** +17; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +17
**Aura** dubiety (60 ft.)

##### Defense

**AC** 36, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+13 Dex, +21 natural, –8 size)
**hp** 377 (26d8+260); _[[universal monster rules/Regeneration|regeneration]]_ 15 (positive energy or inspiration)
**Fort** +20, **Ref** +23, **Will** +19
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[universal monster rules/Negative Energy Affinity|negative energy affinity]]_; **DR** 15/epic and good; **Immune** annihilation, _[[spells/Banishment|banishment]]_,

electricity, ooze traits; **Resist** fire 30; **SR** 31
**Weaknesses** susceptible to creation, _[[items/Wondrous Item/Talisman of the Sphere|talisman of the sphere]]_

##### Offense
**Speed** 30 ft., _[[universal monster rules/Burrow|burrow]]_ 30 ft., fly 30 ft. (perfect)
**Melee** 4 slams +27 (2d8+16/19–20 plus 2d6 negative energy

and _[[universal monster rules/Grab|grab]]_)
**Space** 30 ft., **Reach** 60 ft.
**Special Attacks** annihilation, _[[universal monster rules/Constrict|constrict]]_ (4d8+24), servants of entropy
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +25)
At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Disintegrate|disintegrate]]_ (DC 21) 
3/day—quickened _disintegrate_ (DC 21) 
1/day—_[[spells/Time Stop|time stop]]_

##### Statistics
**Str** 43, **Dex** 36, **Con** 31, **Int** 7, **Wis** 28, **Cha** 21
**Base Atk** +19; **CMB** +43; **CMD** 66
**Feats** _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, Flyby

Attack, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), Improved

Initiative, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_disintegrate_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +21, Knowledge (planes) +3, Perception +17, Stealth +21;

**Racial Modifiers** +16 Stealth
**Languages** Common (cannot speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Compression|compression]]_, master of annihilation

##### Ecology

**Environment** any (Negative Energy Plane)
**Organization** solitary
**Treasure** none

### Special Abilities

**Annihilation (Su)** Any spaces an _[[monsters/Oblivion|oblivion]]_ moves through are left fallow and lifeless in its wake. Ground that it moves over using its base speed becomes barren and is treated as if affected by a _[[spells/Diminish Plants|diminish plants]]_ spell to stunt growth. Dead bodies that the _oblivion_ moves through immediately crumble into dust. Any _constrict_ damage an _oblivion_ deals to a creature automatically bypasses all _[[universal monster rules/Damage Reduction|damage reduction]]_. A creature reduced to 0 or fewer hit points by this _constrict_ damage is immediately slain and its remains (but not its gear) are disintegrated. Once per round as a free action, an _oblivion_ can target a single object in its space. A non-magical object so targeted is immediately destroyed. A magical item must succeed at a DC 33 Fortitude save or be destroyed. The save DC is Constitution-based.

**Aura of Dubiety (Su)** An _oblivion_’s presence is anathema to the gods and the forces that bind creation together. Its presence warps divine magic and severs living beings from the power of life. Any living creature that begins its turn within range of an _oblivion_’s aura of dubiety takes 2d6 points of negative energy damage. This negative energy has no beneficial effect on undead. A creature attempting to cast a divine spell within 60 feet of an _oblivion_ must succeed at a concentration check as if casting defensively (DC = 15 + double the spell level) or the spell is automatically subverted, allowing the _oblivion_ to decide the spell’s target and effect as if it were the original caster. If the affected spell uses positive energy, the subverted spell instead uses negative energy.

**_[[universal monster rules/Immunity|Immunity]]_ to Annihilation (Ex)** An _oblivion_ is immune to _[[spells/Destruction|destruction]]_ spells, _disintegrate_ effects, spheres of annihilation, and similar effects that completely destroy living creatures.

**_Immunity_ to _Banishment_ (Ex)** An _oblivion_ is never treated as having the extraplanar subtype, regardless of what plane it currently inhabits, rendering it immune to _banishment_, _[[spells/Dismissal|dismissal]]_, and similar effects. In addition to this, effects that force the _oblivion_ onto another plane (such as _[[spells/Plane Shift|plane shift]]_ or the violet beam of a _[[spells/Prismatic Spray|prismatic spray]]_) do not function against an _oblivion_ unless the effect comes from an artifact, a creature capable of granting spells to its worshipers, or a mythic source.

**Master of Annihilation (Ex)** An _oblivion_ can establish control over a _[[items/Wondrous Item/Sphere of Annihilation|sphere of annihilation]]_ (Pathfinder RPG Core Rulebook 545) as far away as 100 feet. When an _oblivion_ controls a _sphere of annihilation_, it does so through force of will and an inborn understanding of the sphere’s reality—the _oblivion_’s control check is 1d20 + the _oblivion_’s Hit Dice + its Charisma modifier (the typical _oblivion_ has a control check bonus of +31, and thus can never fail to control a _sphere of annihilation_ unless control of the sphere is opposed). When an _oblivion_ establishes control, it can maintain control at a distance of 100 feet + 20 feet per Hit Die (620 feet for the typical _oblivion_), and the sphere’s speed under the _oblivion_’s control is 20 feet + 5 feet for every 5 points by which the _oblivion_’s control check result in that round exceeded 30.
**Servants of Entropy (Su)** As a full-round action, an _oblivion_ can reform any living creature it has slain within the past hour, forging an obedient duplicate from its own dark mass. Servants created in this manner are identical to their original forms, with all their associated memories, racial abilities, and class abilities, except the duplicate loses any divine spellcasting ability its original form had. A servant’s alignment changes to neutral evil, its type changes to native outsider (do not recalculate hit points, saving throws, or similar abilities), and it gains _negative energy affinity_. An _oblivion_ can communicate telepathically with its servants anywhere on the same plane and can destroy a servant as a free action. An _oblivion_ can manifest a total number of Hit Dice worth of servants equal to twice its own Hit Dice (52 for a typical _oblivion_), but no single servant can have more Hit Dice than the _oblivion_’s CR. An _oblivion_ cannot manifest more than one copy of any given creature at one time.
**Susceptible to Creation (Ex)** An _oblivion_ is a manifestation of disbelief and decay, and the forces of compassion and creativity are anathema to it. It is vulnerable to positive energy, taking damage as if it were undead, though it retains its control over any divine spells, allowing it to often usurp and corrupt cure spells and similar curative magic. An _oblivion_ loses its _regeneration_ any round in which it either takes damage from positive energy or is within 30 feet of a creature that succeeds at a DC 35 Perform check. Creatures under the effect of a _[[spells/Good Hope|good hope]]_ spell, an inspire courage bardic performance, or any spell effect of 5th level or higher that grants a morale bonus gain _immunity_ to the negative energy damage dealt by an _oblivion_’s slams and aura of dubiety.

**_Talisman of the Sphere_ (Ex)** The _talisman of the sphere_ is anathema to an _oblivion_. A character who carries a _talisman of the sphere_ can penetrate an _oblivion_’s _damage reduction_ with ease, ignores its _[[universal monster rules/Spell Resistance|spell resistance]]_, is immune to its aura, and gains a +10 bonus on saving throws against the _oblivion_’s special attacks and _spell-like abilities_.

##### Description

Rare and powerful denizens of the Negative Energy Plane, oblivions are void and nothingness given terrible will. They lurk among crystalline sheets of accumulated entropy that line their home plane’s darkest interior, hungering to unmake the walls of reality and drag all of the cosmos down to its eventual end, allowing themselves to also finally end. Once unleashed upon mortal worlds, oblivions crisscross the globe, destroying its denizens and laying waste to the land until destroyed themselves or until they strip a planet bare of substance, life, and _[[universal monster rules/Heat|heat]]_. Despite its vast bulk, a single _oblivion_ must often dedicate years or even centuries to ending a world, and each is so adept at scrubbing away all traces a being leaves upon the cosmos that people, nations, and entire worlds annihilated by an _oblivion_ are soon forgotten by outsiders. Some gods claim that the brutal efficiency of the oblivions are intended to someday be released upon the multiverse to _[[spells/Cleanse|cleanse]]_ away creation so a new cycle of life can begin from chaotic nothing, while other deities insist the oblivions’ work is nearly complete, leaving only isolated specks of life floating in a vast, unfeeling void.

Unlike nightshades (Pathfinder RPG Bestiary 2 199) or other noteworthy denizens of their dark realm, oblivions serve no masters or agendas. They believe themselves to be the way all things must end. Though _[[items/Weapon Magic Abilities/Cunning|cunning]]_, they rarely find reason to communicate with other creatures, leaving much of their motives, origins, and philosophy in the cosmos a mystery.

Like grim doll makers, oblivions can recreate slain victims from their own dark substance, transforming a world’s heroes and villains into hollow pawns they can dispatch to slay would-be heroes or _[[feats/Undermine|undermine]]_ organized _[[universal monster rules/Resistance|resistance]]_. Lacking any inherent ability to traverse the planes, most oblivions rely on such servants created in the shapes of powerful spellcasters or outsiders to provide routes to new worlds. These hollow reproductions know little of their masters’ will beyond sharing _[[items/Armor Magic Abilities/Comfort|comfort]]_ in the coming end of days, and most desperately fill in the gaps with appealing philosophies. Some of the most powerful servants form doomsday cults on distant planets to prepare them for an _oblivion_’s arrival.

Oblivions share a symbiosis with the artifacts known as spheres of annihilation, coveting their powerful, highly destructive magic. The towering oozes are unaffected by the artifact’s destructive powers, and can move them as easily as a child might carry a toy. Some speculate that the spheres are in fact the eggs or spores of these apocalyptic beings, as rare survivors recount tales of spheres spontaneously birthing the roiling, devouring entities.

Oblivions typically measure several dozen feet across, though their presence corrupts and consumes life, making the roiling _darkness_ that most people mistake for their bodies seem much larger. Despite their size, oblivions have no mass. Upon _destruction_, an _oblivion_ collapses thunderously into nothing