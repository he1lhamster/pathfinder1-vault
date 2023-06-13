---
cssclass: [monsters]
title1: Kaiju, Varklops
desc_short: This immense, fiery-orange serpent has three horned heads, a pairof draconic
  wings, and a long tail tipped with four bony spikes.
title2: Varklops
CR: 30
sources:
- name: Bestiary 6
  page: 170
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 9830400
alignment: CE
size: Colossal
type: magical beast
subtypes:
- fire
- kaiju
initiative:
  bonus: 17
senses:
  darkvision: 600
  low-light vision: true
  mistsight: true
  tremorsense: 300
AC:
  AC: 48
  touch: 16
  flat_footed: 34
  components:
    dex: 13
    dodge: 1
    natural,-8 size: 32
HP:
  HP: 752
  long: 35d10+560
  fast_healing: 30
saves:
  fort: 35
  ref: 32
  will: 23
defensive_abilities:
- deflect cold
- ferocity
- recovery
DR:
- amount: 20
  weakness: epic
immunities:
- ability damage
- ability drain
- death effects
- disease,energy drain
- fear
- fire
resistances:
  acid: 30
  cold: 30
  electricity: 30
  negative energy: 30
  sonic: 30
weaknesses:
- distracted when outnumbered
- vulnerable to cold
speeds:
  base: 80
  burrow: 60
  fly: 150
  fly_maneuverability: poor
attacks:
  melee:
  - - text: 3 bites +46 (6d6+26/19-20 plus burn)
      entries:
      - - damage: 6d6+26
          crit_range: 19-20
        - effect: burn
      count: 3
      attack: bites
      bonus:
      - 46
    - text: 2 wings +44(3d8+16/19-20 plus burn)
      entries:
      - - damage: 3d8+16
          crit_range: 19-20
        - effect: burn
      count: 2
      attack: wings
      bonus:
      - 44
    - text: tail slap +46 (4d8+35/19-20/×3plus burn)
      entries:
      - - damage: 4d8+35
          type: /19-20/×3plus burn
      attack: tail slap
      bonus:
      - 46
  special:
  - breath weapon
  - burn (2d6 fire, DC 43)
  - eruption,fire monsoon
  - improved hurl foe
  - kaijuslayer
  - rend (2 bites,6d6+28; or 3 bites, 12d6+28)
space: 60
reach: 60
ability_scores:
  STR: 48
  DEX: 37
  CON: 42
  INT: 3
  WIS: 30
  CHA: 29
BAB: 35
CMB: 62
CMB_other: +66 bull rush
CMD: 86
CMD_other: 88 vs. bull rush,can't be tripped
feats:
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Greater Bull Rush
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Critical(bite, tail slap, wing)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Vital Strike
- name: Iron Will
- name: Lunge
- name: Multiattack
- name: PowerAttack
- name: Staggering Critical
- name: Vital Strike
skills:
  Fly: 34
  Perception: 34
  _racial_mods:
    Perception:
      _: 16
languages:
- Ignan (can't speak)
special_qualities:
- devastating
- massive
- powerful blows (tail slap)
ecology:
  environment: warm mountains
  organization: solitary (unique)
  treasure_type: incidental
special_abilities:
  Breath Weapon (Su): Each of Varklops's three heads can exhale a blast of searing
    fire and billowing ash in a 1,200-foot line once every 4 rounds. Each head's breath
    weapon is a separate attack with its own 4-round recharge period. The kaiju can
    exhale one line of fire as a move action, two lines as a standard action, or three
    lines as a full-round action. Each breath weapon deals 20d6 points of fire damage
    and 20d6 points of bludgeoning damage to all creatures in the area of effect as
    they are barraged with semi-solid chunks of superheated rock and magma expelled
    in the torrent of fire; targets are also stunned for 1 round by the overwhelming
    force. With a successful DC 43 Reflex save, a creature takes half damage and negates
    the stun effect. If Varklops exhales more than one breath weapon, he can use them
    in different directions. If a creature is subjected to more than one breath weapon
    in a round in this manner, it takes damage from and must attempt separate saves
    against each breath weapon. The save DCs are Constitution-based.
  Deflect Cold (Ex): Although Varklops is vulnerable to cold damage, he can shield
    himself from a cold attack by reflexively curling his wings around himself as
    an immediate action when he would otherwise take cold damage. He must choose to
    use this ability before any cold damage from the attack is applied and before
    he attempts any applicable saving throws to resist the cold damage, but he can
    wait until after the attack hits to choose to deflect cold. When he uses this
    ability, all cold damage from that particular attack is ignored. At Varklops's
    discretion, he can deflect the cold damage to any single adjacent creature, which
    is then instead treated as the target of the cold attack. If the cold attack was
    an area effect that also affected the adjacent creature, that creature does not
    take the cold damage twice, but does need to attempt two saving throws (if applicable)
    against the effect, taking the worse of the two results as the actual result.
  Devastating (Ex): Varklops is particularly devastating, and any attack or special
    ability he uses to deal damage to an object ignores hardness less than 20. Objects
    take full damage from his fire-based attacks.
  Distracted When Outnumbered (Ex): While Varklops is furiously focused on slaying
    kaiju, his rudimentary intellect supports a surprisingly powerful and inflated
    sense of selfworth that crumbles when he faces overwhelming odds. In any combat
    round that involves two allied kaiju focusing their efforts against him, Varklops
    loses his kaijuslayer ability and becomes so distracted by which target to focus
    on that he must succeed at a DC 30 Will save or become staggered for that round.
    Non-kaiju cannot distract Varklops in this manner, even if the non-kaiju is similar
    in size to a kaiju.
  Eruption (Su): Up to three times per day (but no more than once every 4 rounds)
    as Varklops emerges onto the surface of terrain after burrowing, he does so with
    an explosion of ash and magma. All creatures within 150 feet of Varklops when
    he bursts out of the ground in this manner take 20d6 points of fire damage. Huge
    or smaller creatures in this area are knocked prone. With a successful DC 43 Reflex
    save, creatures take half the damage and negate being knocked prone, but a creature
    that takes any damage from this eruption is subjected to Varklops's burn ability.
    In addition, the eruption creates a cloud of ash in the area of effect; this cloud
    of ash lingers in the area for 1 minute, obscuring vision as per obscuring mist.
    The save DC is Constitution-based.
  Fire Monsoon (Su): Once per day as Varklops moves at full speed while flying, he
    can rain down a torrential storm of fire, burning any target up to 300 feet below
    him. All targets Varklops passes over in flight take 20d6 points of fire damage
    (Reflex DC 43 half); any creature that takes any damage from this attack is subjected
    to Varklops's burn ability. The area affected by the fire monsoon continues to
    burn for 1 minute-any creature that begins its turn in this area takes 4d6 points
    of fire damage. The save DC is Constitution-based.
  Improved Hurl Foe (Ex): When Varklops hits a creature with his tail slap and uses
    his hurl foe kaiju ability (see page 305), the distance the foe is knocked back
    doubles.
  Kaijuslayer (Su): Varklops takes particular delight in the slaying of other kaiju,
    and his aggression causes all kaiju to take a -4 penalty on saving throws against
    Varklops's special attacks. Another kaiju cannot use recovery to prevent itself
    from being killed by one of Varklops's attacks. This ability does not function
    against the kaiju known as King Mogaru.
desc_long: |-
  Lord Varklops is indisputably the most powerful of the known kaiju, a tremendously destructive force of devastation that dwells in the heart of an active volcano in a tropical mountain range when not hunting his favorite prey-other kaiju. Although the fact that Lord Varklops so eagerly hunts and slays kaiju might seem to make him an ally of all civilizations threatened by such creatures, in truth Varklops is also one of the few kaiju to be actively evil in his predations upon the world. When no other kaiju present themselves as victims and the urge to destroy seizes Varklops, the socalled Thrice-Headed Fiend thinks nothing of razing entire cities for his pleasure. 

  This eagerness to destroy appeals to apocalypse-minded cultists and to deranged exiles who seek revenge against the cities they were forced to flee. Varklops is known to look favorably upon those who approach him with requests for targeted devastation-particularly if the offer includes the opportunity to attack another kaiju. Varklops has little interest in assaulting civilizations in polar regions, but his greatest weakness is his inflated, if rudimentary, ego. 

  When facing multiple kaiju, Varklops often gets distracted and frustrated-a condition that several societies have risked using to their advantage by luring other kaiju to their defense. Of course, the devastation a city might suffer when three or more kaiju fight may well exceed that wrought by Varklops alone, so such desperate actions are not taken lightly. 

  Varklops has a particularly strong hatred of King Mogaru, as this kaiju alone can resist Varklops's rage. The reasons for this immunity are unknown, but certainly Mogaru matches Varklops's hatred, and battles between the two kaiju are the stuff of legend. Varklops is 200 feet long and weighs 16,000 tons.

---

# Kaiju, Varklops
This immense, fiery-orange serpent has three horned heads, a pair

of draconic wings, and a long tail tipped with four bony spikes.
**Source** Bestiary 6 pg. 170
**XP** 9,830,400
CE Colossal magical beast (fire, kaiju)
**Init** +17; **Senses** _[[spells/Darkvision|darkvision]]_ 600 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Mistsight|mistsight]]_,

_[[universal monster rules/Tremorsense|tremorsense]]_ 300 ft.; Perception +34

##### Defense

**AC** 48, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 34 (+13 Dex, +1 dodge, +32 natural,

–8 size)
**hp** 752 (35d10+560); _[[universal monster rules/Fast Healing|fast healing]]_ 30
**Fort** +35, **Ref** +32, **Will** +23
**Defensive Abilities** deflect cold, _[[universal monster rules/Ferocity|ferocity]]_, recovery; **DR** 20/epic; **Immune** ability damage, ability drain, death effects, disease,

_[[universal monster rules/Energy Drain|energy drain]]_, _[[universal monster rules/Fear|fear]]_, fire; **Resist** acid 30, cold 30, electricity 30,

negative energy 30, sonic 30
**Weaknesses** distracted when outnumbered, vulnerable to cold

##### Offense
**Speed** 80 ft., _[[universal monster rules/Burrow|burrow]]_ 60 ft., fly 150 ft. (poor)
**Melee** 3 bites +46 (6d6+26/19–20 plus _[[universal monster rules/Burn|burn]]_), 2 wings +44

(3d8+16/19–20 plus _burn_), tail slap +46 (4d8+35/19–20/×3

plus _burn_)
**Space** 60 ft., **Reach** 60 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_, _burn_ (2d6 fire, DC 43), eruption,

fire monsoon, improved hurl foe, kaijuslayer, _[[universal monster rules/Rend|rend]]_ (2 bites,

6d6+28; or 3 bites, 12d6+28)

##### Statistics
**Str** 48, **Dex** 37, **Con** 42, **Int** 3, **Wis** 30, **Cha** 29
**Base Atk** +35; **CMB** +62 (+66 bull rush); **CMD** 86 (88 vs. bull rush,

can’t be tripped)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_

(bite, tail slap, wing), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lunge|Lunge]]_, _[[feats/Multiattack|Multiattack]]_, Power

Attack, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +34, Perception +34; **Racial Modifiers** +16 Perception
**Languages** Ignan (can’t speak)
**SQ** devastating, massive, powerful blows (tail slap)

##### Ecology

**Environment** warm mountains
**Organization** solitary (unique)
**Treasure** incidental

### Special Abilities

**_Breath Weapon_ (Su)** Each of Varklops’s three heads can exhale a blast of searing fire and _[[items/Armor Magic Abilities/Billowing|billowing]]_ ash in a 1,200-foot line once every 4 rounds. Each head’s _breath weapon_ is a separate attack with its own 4-round _[[spells/Recharge|recharge]]_ period. The kaiju can exhale one line of fire as a move action, two lines as a standard action, or three lines as a full-round action. Each _breath weapon_ deals 20d6 points of fire damage and 20d6 points of bludgeoning damage to all creatures in the area of effect as they are barraged with semi-solid chunks of superheated rock and magma expelled in the torrent of fire; targets are also _[[conditions/Stunned|stunned]]_ for 1 round by the overwhelming force. With a successful DC 43 Reflex save, a creature takes half damage and negates the stun effect. If Varklops exhales more than one _breath weapon_, he can use them in different directions. If a creature is subjected to more than one _breath weapon_ in a round in this manner, it takes damage from and must attempt separate saves against each _breath weapon_. The save DCs are Constitution-based.

**Deflect Cold (Ex)** Although Varklops is vulnerable to cold damage, he can _[[spells/Shield|shield]]_ himself from a cold attack by reflexively curling his wings around himself as an immediate action when he would otherwise take cold damage. He must choose to use this ability before any cold damage from the attack is applied and before he attempts any applicable saving throws to resist the cold damage, but he can wait until after the attack hits to choose to deflect cold. When he uses this ability, all cold damage from that particular attack is ignored. At Varklops’s discretion, he can deflect the cold damage to any single adjacent creature, which is then instead treated as the target of the cold attack. If the cold attack was an area effect that also affected the adjacent creature, that creature does not take the cold damage twice, but does need to attempt two saving throws (if applicable) against the effect, taking the worse of the two results as the actual result.

**Devastating (Ex)** Varklops is particularly devastating, and any attack or special ability he uses to deal damage to an object ignores hardness less than 20. Objects take full damage from his fire-based attacks.

**Distracted When Outnumbered (Ex)** While Varklops is furiously focused on slaying kaiju, his rudimentary intellect supports a surprisingly powerful and inflated sense of selfworth that crumbles when he faces overwhelming odds. In any combat round that involves two allied kaiju focusing their efforts against him, Varklops loses his kaijuslayer ability and becomes so distracted by which target to focus on that he must succeed at a DC 30 Will save or become _[[conditions/Staggered|staggered]]_ for that round. Non-kaiju cannot distract Varklops in this manner, even if the non-kaiju is similar in size to a kaiju.

**Eruption (Su)** Up to three times per day (but no more than once every 4 rounds) as Varklops emerges onto the surface of terrain after burrowing, he does so with an explosion of ash and magma. All creatures within 150 feet of Varklops when he bursts out of the ground in this manner take 20d6 points of fire damage. Huge or smaller creatures in this area are knocked _[[conditions/Prone|prone]]_. With a successful DC 43 Reflex save, creatures take half the damage and negate being knocked _prone_, but a creature that takes any damage from this eruption is subjected to Varklops’s _burn_ ability. In addition, the eruption creates a cloud of ash in the area of effect; this cloud of ash lingers in the area for 1 minute, obscuring _[[spells/Vision|vision]]_ as per _[[spells/Obscuring Mist|obscuring mist]]_. The save DC is Constitution-based.

**Fire Monsoon (Su)** Once per day as Varklops moves at full speed while flying, he can rain down a torrential storm of fire, _[[items/Weapon Magic Abilities/Burning|burning]]_ any target up to 300 feet below him. All targets Varklops passes over in _[[universal monster rules/Flight|flight]]_ take 20d6 points of fire damage (Reflex DC 43 half); any creature that takes any damage from this attack is subjected to Varklops’s _burn_ ability. The area affected by the fire monsoon continues to _burn_ for 1 minute—any creature that begins its turn in this area takes 4d6 points of fire damage. The save DC is Constitution-based.

**Improved Hurl Foe (Ex)** When Varklops hits a creature with his tail slap and uses his hurl foe kaiju ability (see page 305), the distance the foe is knocked back doubles.

**Kaijuslayer (Su)** Varklops takes particular delight in the slaying of other kaiju, and his aggression causes all kaiju to take a –4 penalty on saving throws against Varklops’s special attacks. Another kaiju cannot use recovery to prevent itself from being killed by one of Varklops’s attacks. This ability does not function against the kaiju known as _[[npcs/King|King]]_ Mogaru.

##### Description

Lord Varklops is indisputably the most powerful of the known kaiju, a tremendously destructive force of devastation that dwells in the heart of an active volcano in a tropical mountain range when not hunting his favorite prey—other kaiju. Although the fact that Lord Varklops so eagerly hunts and slays kaiju might seem to make him an ally of all civilizations threatened by such creatures, in truth Varklops is also one of the few kaiju to be actively evil in his predations upon the world. When no other kaiju present themselves as victims and the urge to destroy seizes Varklops, the socalled Thrice-Headed Fiend thinks nothing of razing entire cities for his pleasure.

This eagerness to destroy appeals to apocalypse-minded cultists and to deranged exiles who seek revenge against the cities they were forced to flee. Varklops is known to look favorably upon those who approach him with requests for targeted devastation—particularly if the offer includes the opportunity to attack another kaiju. Varklops has little interest in assaulting civilizations in polar regions, but his greatest weakness is his inflated, if rudimentary, ego.

When facing multiple _[[monsters/Kaiju, Varklops|kaiju, Varklops]]_ often gets distracted and frustrated—a condition that several societies have risked using to their advantage by luring other kaiju to their defense. Of course, the devastation a city might suffer when three or more kaiju fight may well exceed that wrought by Varklops alone, so such desperate actions are not taken lightly.

Varklops has a particularly strong hatred of _King_ Mogaru, as this kaiju alone can resist Varklops’s _[[spells/Rage|rage]]_. The reasons for this _[[universal monster rules/Immunity|immunity]]_ are _[[monsters/Unknown|unknown]]_, but certainly Mogaru matches Varklops’s hatred, and battles between the two kaiju are the stuff of legend. Varklops is 200 feet long and weighs 16,000 tons.