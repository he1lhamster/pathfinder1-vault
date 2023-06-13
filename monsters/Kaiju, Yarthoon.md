---
cssclass: [monsters]
title1: Kaiju, Yarthoon
desc_short: This immense pale blue worm raises one end of its body like a serpent,
  its many-toothed maw opening amid a ring of glowing eyes.
title2: Yarthoon
CR: 25
sources:
- name: Bestiary 6
  page: 174
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 1638400
alignment: CN
size: Colossal
type: magical beast
subtypes:
- air
- kaiju
initiative:
  bonus: 13
senses:
  low-light vision: true
  mistsight: true
  see in darkness: true
  tremorsense: 300
AC:
  AC: 44
  touch: 12
  flat_footed: 34
  components:
    dex: 9
    dodge: 1
    natural: 32
    size: -8
HP:
  HP: 565
  long: 29d10+406
  fast_healing: 30
saves:
  fort: 30
  ref: 25
  will: 19
defensive_abilities:
- ferocity
- recovery
DR:
- amount: 20
  weakness: epic
immunities:
- ability damage
- ability drain
- cold
- death effects
- disease
- energy drain
- fear
resistances:
  acid: 30
  electricity: 30
  fire: 30
  negative energy: 30
  sonic: 30
speeds:
  base: 60
  burrow: 100
  fly: 100
  fly_maneuverability: average
  swim: 100
attacks:
  melee:
  - - text: 2 bites +39 (4d6+27/19-20 plus 4d6 cold and grab)
      entries:
      - - damage: 4d6+27
          crit_range: 19-20
        - damage: 4d6
          type: cold
        - effect: grab
      count: 2
      attack: bites
      bonus:
      - 39
    - text: slam +39 (4d8+27/19-20 plus 4d6 cold and staggering strike)
      entries:
      - - damage: 4d8+27
          crit_range: 19-20
        - damage: 4d6
          type: cold
        - effect: staggering strike
      attack: slam
      bonus:
      - 39
  special:
  - clinging frost
  - eye beams
  - fast swallow
  - freezing mist
  - hurl foe
  - penetrating cold
  - swallow whole (6d6 bludgeoning and 6d6 cold damage, AC 26, 56 hp)
  - swift bite
space: 30
reach: 30
ability_scores:
  STR: 46
  DEX: 29
  CON: 38
  INT: 3
  WIS: 26
  CHA: 21
BAB: 29
CMB: 55
CMB_other: +59 overrun
CMD: 75
CMD_other: 77 vs. overrun, can't be tripped
feats:
- name: Critical Focus
- name: Dodge
- name: Flyby Attack
- name: Greater Overrun
- name: Improved Critical (bite)
- name: Improved Critical (slam)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Overrun
- name: Improved Vital Strike
- name: Iron Will
- name: Power Attack
- name: Staggering Critical
- name: Vital Strike
- name: Wingover
skills:
  Fly: 32
  Perception: 28
  Swim: 26
  _racial_mods:
    Perception:
      _: 16
languages:
- Auran (can't speak)
special_qualities:
- massive
- no breath
- powerful blows (bite, slam)
- starflight
ecology:
  environment: any cold (the world's moon or outer space)
  organization: solitary (unique)
  treasure_type: incidental
special_abilities:
  Clinging Frost (Su): Whenever a creature takes cold damage from Yarthoon (including
    from her freezing mist), the creature becomes encrusted with a layer of clinging
    frost for 1 round. The duration of this clinging frost stacks with multiple instances
    of cold damage from Yarthoon. As long as a creature has at least 1 round of clinging
    frost remaining, it takes a -2 penalty on all Reflex saving throws and Dexterity-based
    skill checks. As long as a creature has at least 2 rounds of clinging frost remaining,
    it is staggered. Freedom of movement negates the effects of clinging frost, and
    if a creature activates a firebased supernatural ability on its turn, it reduces
    the number of rounds remaining by 1d4. Creatures with the fire subtype, the heat
    ability, or any similar ability to shed significant warmth are immune to clinging
    frost.
  Eye Beams (Su): Once every 4 rounds as a standard action, Yarthoon can emit several
    beams of freezing energy from her eyes. When Yarthoon uses this attack, she can
    choose to fire all of the beams in one direction to create a single line 1,200
    feet long, or she can instead fire eight separate beams as ranged touch attacks
    with a range of 1,200 feet. If she chooses to fire them in a line, all creatures
    within the area of effect take 20d6 points of cold damage (Reflex DC 38 half).
    If she fires the beams as ranged touch attacks, she has a +30 attack bonus but
    can target a single creature with no more than two eye beams at a time (though
    she can fire the beams in any direction to attack multiple targets in range).
    A single eye beam deals 8d6 points of cold damage on a hit (no save). The save
    DC for the line-based attack is Constitution-based.
  Freezing Mist (Su): Once per day as a swift action, Yarthoon can exhale a cloud
    of freezing mist, filling a 200-foot-radius sphere surrounding her. This mist
    obscures vision as per obscuring mist and persists for 10 rounds, and is not dispersed
    by moderate wind. A strong wind (21+ mph) disperses the mist in 2d4 rounds, while
    fireball, flame strike, or similar spells burn away the mist in the spell's area.
    Any creature within the area of the mist when Yarthoon creates it takes 8d6 points
    of cold damage (Reflex DC 38 half). A creature that begins its turn within the
    mist takes 4d6 points of cold damage (no save) at the start of its turn. The save
    DC is Constitution-based.
  Penetrating Cold (Su): When Yarthoon deals cold damage, the damage ignores the first
    30 points of cold resistance the target has.
  Staggering Strike (Ex): If Yarthoon hits a Gargantuan or smaller foe that's standing
    on the ground with her slam attack, the target struck must succeed at a DC 42
    Reflex save or be knocked prone and become staggered for 1d6 rounds. If she hits
    a Gargantuan or smaller flying foe, the creature is staggered for 1d6 rounds and
    must succeed at a DC 42 Fly check or lose 30 feet of altitude (a winged flying
    creature loses 60 feet of altitude instead; this replaces the normal rule for
    being attacked while flying for winged creatures). A Colossal creature struck
    by Yarthoon's slam must succeed at a DC 42 Reflex save to resist being staggered
    for 1 round, but is not knocked prone or forced to lose altitude. The save DC
    is Strength-based.
  Starflight (Su): Yarthoon can survive in the void of outer space. She flies through
    space at incredible speeds, but generally only does so to travel between the moon
    and the world below when her attention is caught or her curiosity piqued. It takes
    Yarthoon only 2d4 hours to travel from the moon to the world below. If she were
    to travel to a more distant point in the same solar system, she requires only
    3d6 days to make the journey, while trips beyond this range generally take her
    3d6 weeks.
  Swift Bite (Ex): Yarthoon strikes with astonishing speed when she attacks with her
    bite. Whenever Yarthoon makes a bite attack on her turn, she can attack two times,
    either as a standard action to bite twice, or as part of a full attack to bite
    two times in addition to making one slam attack. She can make any number of attacks
    of opportunity with her bite attack, but does not get to bite more than once when
    she does so.
desc_long: |-
  Yarthoon is among the least powerful of the kaiju, yet even she is of staggering size and capable of unleashing devastation on an apocalyptic scale. Known as the Moon Grub to kaiju scholars, Yarthoon does indeed dwell upon the moon itself, where she spends much of her time in a frozen reach of ice and snow, created, in part, by her presence and the effects of her freezing breath over the course of centuries. (Note that although Yarthoon's exhalations fill the region with freezing mist, the Moon Grub herself has no need to breathe and can exist comfortably in the vacuum of space.) 

  Were Yarthoon content to remain upon the moon, there would be little known about the frozen kaiju; unfortunately, the larger world her home orbits is a constant fascination for her. Indeed, certain events have been known to specifically attract Yarthoon's attention, whether they're intentional calls such as powerful rituals led by apocalyptic cultists, or accidental lures that occur when powerful effects of magical cold occur. The exact nature of these attractions varies, and even the most learned scholars argue over what exactly it is that draws Yarthoon to visit the world. None, however, dispute the devastation Yarthoon unleashes, if unintentionally, when she visits the world. Unlike many kaiju, Yarthoon seems not to purposefully seek out civilizations to destroy, but her immense size and her freezing breath wreak havoc nonetheless. Fortunately, Yarthoon's visits to the world typically last for only a few days before she slithers off into the sky like an eel swimming through water to return to her den on the moon. 

  Yarthoon has a complex relationship with Mogaru, the Final King (Pathfinder RPG Bestiary 4 170). Often, Mogaru's devastation on a region is enough to lure Yarthoon down from the moon, in which case she often clashes with the more powerful kaiju. Likewise, Mogaru's ability to sense kaiju often results in him coming to investigate a region that Yarthoon has decided to visit. Yet the two kaiju never seem willing to finish a fight against the other, and rather than deliver a death blow when the chance rises, each seems content to let the other flee. The one thing that seems to unite the two kaiju is their shared hatred of Lord Varklops, and the two kaiju have teamed up several times to drive off the three-headed fiend more than once. 

  Although Yarthoon is the least powerful of the known kaiju, the Moon Grub has been remarkably resilient. Time and time again, Yarthoon has returned after suffering what seemed to be a complete defeat, at either the hands of powerful heroes or the claws and fangs of fellow kaiju. Scholars of these immense monsters have theorized that Yarthoon may not be a unique creature, and that in its hidden lair on the moon, multiple Moon Grubs writhe and dream. Others posit that Yarthoon is but the larval stage of a kaiju, and that while only one may live at any time, numerous other eggs lie in a hidden crèche on the moon, waiting to hatch and release replacement Moon Grubs as needed. 

  Yarthoon is 250 feet long from head to tail and weighs 14,000 tons.

---

# Kaiju, Yarthoon
This immense pale blue worm raises one end of its body like a serpent, its many-toothed maw opening amid a ring of glowing eyes.
**Source** Bestiary 6 pg. 174
**XP** 1,638,400

CN Colossal magical beast (air, kaiju)
**Init** +13; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Mistsight|mistsight]]_, _[[universal monster rules/See in Darkness|see in darkness]]_, _[[universal monster rules/Tremorsense|tremorsense]]_ 300 ft.; Perception +28

##### Defense

**AC** 44, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 34 (+9 Dex, +1 dodge, +32 natural, –8 size)
**hp** 565 (29d10+406); _[[universal monster rules/Fast Healing|fast healing]]_ 30
**Fort** +30, **Ref** +25, **Will** +19
**Defensive Abilities** _[[universal monster rules/Ferocity|ferocity]]_, recovery; **DR** 20/epic; **Immune** ability damage, ability drain, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, _[[universal monster rules/Fear|fear]]_; **Resist** acid 30, electricity 30, fire 30, negative energy 30, sonic 30

##### Offense
**Speed** 60 ft., _[[universal monster rules/Burrow|burrow]]_ 100 ft., fly 100 ft. (average), swim 100 ft.
**Melee** 2 bites +39 (4d6+27/19–20 plus 4d6 cold and _[[universal monster rules/Grab|grab]]_), slam +39 (4d8+27/19–20 plus 4d6 cold and staggering strike)
**Space** 30 ft., **Reach** 30 ft.
**Special Attacks** clinging frost, eye beams, _[[universal monster rules/Fast Swallow|fast swallow]]_, freezing mist, hurl foe, penetrating cold, _[[universal monster rules/Swallow Whole|swallow whole]]_ (6d6 bludgeoning and 6d6 cold damage, AC 26, 56 hp), swift bite

##### Statistics
**Str** 46, **Dex** 29, **Con** 38, **Int** 3, **Wis** 26, **Cha** 21
**Base Atk** +29; **CMB** +55 (+59 overrun); **CMD** 75 (77 vs. overrun, can’t be tripped)
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Overrun|Greater Overrun]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, slam), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Overrun|Improved Overrun]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Wingover|Wingover]]_
**Skills** Fly +32, Perception +28, Swim +26; **Racial Modifiers** +16 Perception
**Languages** Auran (can’t speak)
**SQ** massive, _[[universal monster rules/No Breath|no breath]]_, powerful blows (bite, slam), starflight

##### Ecology

**Environment** any cold (the world’s moon or outer space)
**Organization** solitary (unique)
**Treasure** incidental

### Special Abilities

**Clinging Frost (Su)** Whenever a creature takes cold damage from Yarthoon (including from her freezing mist), the creature becomes encrusted with a layer of clinging frost for 1 round. The duration of this clinging frost stacks with multiple instances of cold damage from Yarthoon. As long as a creature has at least 1 round of clinging frost remaining, it takes a –2 penalty on all Reflex saving throws and Dexterity-based skill checks. As long as a creature has at least 2 rounds of clinging frost remaining, it is _[[conditions/Staggered|staggered]]_. _[[spells/Freedom of Movement|Freedom of movement]]_ negates the effects of clinging frost, and if a creature activates a firebased supernatural ability on its turn, it reduces the number of rounds remaining by 1d4. Creatures with the fire subtype, the _[[universal monster rules/Heat|heat]]_ ability, or any similar ability to shed significant warmth are immune to clinging frost.

**Eye Beams (Su)** Once every 4 rounds as a standard action, Yarthoon can emit several beams of freezing energy from her eyes. When Yarthoon uses this attack, she can choose to fire all of the beams in one direction to create a single line 1,200 feet long, or she can instead fire eight separate beams as ranged touch attacks with a range of 1,200 feet. If she chooses to fire them in a line, all creatures within the area of effect take 20d6 points of cold damage (Reflex DC 38 half). If she fires the beams as ranged touch attacks, she has a +30 attack bonus but can target a single creature with no more than two eye beams at a time (though she can fire the beams in any direction to attack multiple targets in range). A single eye beam deals 8d6 points of cold damage on a hit (no save). The save DC for the line-based attack is Constitution-based.

**Freezing Mist (Su)** Once per day as a swift action, Yarthoon can exhale a cloud of freezing mist, filling a 200-foot-radius sphere surrounding her. This mist obscures _[[spells/Vision|vision]]_ as per _[[spells/Obscuring Mist|obscuring mist]]_ and persists for 10 rounds, and is not dispersed by moderate wind. A strong wind (21+ mph) disperses the mist in 2d4 rounds, while _[[spells/Fireball|fireball]]_, _[[spells/Flame Strike|flame strike]]_, or similar spells _[[universal monster rules/Burn|burn]]_ away the mist in the spell’s area. Any creature within the area of the mist when Yarthoon creates it takes 8d6 points of cold damage (Reflex DC 38 half). A creature that begins its turn within the mist takes 4d6 points of cold damage (no save) at the start of its turn. The save DC is Constitution-based.

**Penetrating Cold (Su)** When Yarthoon deals cold damage, the damage ignores the first 30 points of cold _[[universal monster rules/Resistance|resistance]]_ the target has.
**Staggering Strike (Ex)** If Yarthoon hits a Gargantuan or smaller foe that’s standing on the ground with her slam attack, the target struck must succeed at a DC 42 Reflex save or be knocked _[[conditions/Prone|prone]]_ and become _staggered_ for 1d6 rounds. If she hits a Gargantuan or smaller flying foe, the creature is _staggered_ for 1d6 rounds and must succeed at a DC 42 Fly check or lose 30 feet of altitude (a winged flying creature loses 60 feet of altitude instead; this replaces the normal rule for being attacked while flying for winged creatures). A Colossal creature struck by Yarthoon’s slam must succeed at a DC 42 Reflex save to resist being _staggered_ for 1 round, but is not knocked _prone_ or forced to lose altitude. The save DC is Strength-based.
**Starflight (Su)** Yarthoon can survive in the void of outer space. She flies through space at incredible speeds, but generally only does so to travel between the moon and the world below when her attention is caught or her curiosity piqued. It takes Yarthoon only 2d4 hours to travel from the moon to the world below. If she were to travel to a more distant point in the same solar system, she requires only 3d6 days to make the journey, while trips beyond this range generally take her 3d6 weeks.
**Swift Bite (Ex)** Yarthoon strikes with astonishing speed when she attacks with her bite. Whenever Yarthoon makes a bite attack on her turn, she can attack two times, either as a standard action to bite twice, or as part of a full attack to bite two times in addition to making one slam attack. She can make any number of attacks of opportunity with her bite attack, but does not get to bite more than once when she does so.

##### Description

Yarthoon is among the least powerful of the kaiju, yet even she is of staggering size and capable of unleashing devastation on an apocalyptic scale. Known as the Moon Grub to kaiju scholars, Yarthoon does indeed dwell upon the moon itself, where she spends much of her time in a frozen reach of ice and snow, created, in part, by her presence and the effects of her freezing breath over the course of centuries. (Note that although Yarthoon’s exhalations fill the region with freezing mist, the Moon Grub herself has no need to breathe and can exist comfortably in the vacuum of space.)

Were Yarthoon content to remain upon the moon, there would be little known about the frozen kaiju; unfortunately, the larger world her home orbits is a constant fascination for her. Indeed, certain events have been known to specifically attract Yarthoon’s attention, whether they’re intentional calls such as powerful rituals led by apocalyptic cultists, or accidental lures that occur when powerful effects of magical cold occur. The exact nature of these attractions varies, and even the most learned scholars argue over what exactly it is that draws Yarthoon to visit the world. None, however, dispute the devastation Yarthoon unleashes, if unintentionally, when she visits the world. Unlike many _[[monsters/Kaiju, Yarthoon|kaiju, Yarthoon]]_ seems not to purposefully seek out civilizations to destroy, but her immense size and her freezing breath wreak havoc nonetheless. Fortunately, Yarthoon’s visits to the world typically last for only a few days before she slithers off into the sky like an eel swimming through water to return to her den on the moon.

Yarthoon has a complex relationship with Mogaru, the Final _[[npcs/King|King]]_ (Pathfinder RPG Bestiary 4 170). Often, Mogaru’s devastation on a region is enough to lure Yarthoon down from the moon, in which case she often clashes with the more powerful kaiju. Likewise, Mogaru’s ability to sense kaiju often results in him coming to investigate a region that Yarthoon has decided to visit. Yet the two kaiju never seem willing to finish a fight against the other, and rather than deliver a death blow when the chance rises, each seems content to let the other flee. The one thing that seems to unite the two kaiju is their shared hatred of Lord Varklops, and the two kaiju have teamed up several times to drive off the three-headed fiend more than once.

Although Yarthoon is the least powerful of the known kaiju, the Moon Grub has been remarkably resilient. Time and time again, Yarthoon has returned after suffering what seemed to be a complete defeat, at either the hands of powerful heroes or the claws and fangs of fellow kaiju. Scholars of these immense monsters have theorized that Yarthoon may not be a unique creature, and that in its hidden lair on the moon, multiple Moon Grubs writhe and _[[spells/Dream|dream]]_. Others posit that Yarthoon is but the larval stage of a kaiju, and that while only one may live at any time, numerous other eggs lie in a hidden crèche on the moon, waiting to hatch and release replacement Moon Grubs as needed.

Yarthoon is 250 feet long from head to tail and weighs 14,000 tons.