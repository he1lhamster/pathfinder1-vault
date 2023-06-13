---
cssclass: [monsters]
title1: Empyreal Lord, Cernunnos
desc_short: This tall, graceful person has elven features, the horns of a majestic
  stag and a piercing, ageless stare.
title2: Cernunnos
CR: 30
sources:
- name: Bestiary 4
  page: 88
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 9830400
alignment: CG
size: Large
type: outsider
subtypes:
- azata
- chaotic
- extraplanar
- good
initiative:
  bonus: 16
senses:
  blindsense: 60
  darkvision: 60
  detect evil: true
  detect lies: true
  detect poison: true
  low-light vision: true
  true seeing: true
auras:
- name: primal
  radius: 30
AC:
  AC: 48
  touch: 22
  flat_footed: 35
  components:
    dex: 12
    dodge: 1
    natural: 26
    size: -1
HP:
  HP: 663
  long: 34d10+476
  regeneration: 10
  regeneration_weakness: evil artifacts, effects, and spells
saves:
  fort: 25
  ref: 31
  will: 25
defensive_abilities:
- freedom of movement
- lightning rod
- unbound
DR:
- amount: 15
  weakness: epic and evil
immunities:
- ability damage
- ability drain
- charm effects
- compulsion effects
- death effects
- electricity
- energy drain
- petrification
resistances:
  cold: 30
  fire: 30
SR: 41
speeds:
  base: 40
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: +5 holy cold iron club +48/+43/+38/+33 (1d8+18/15-20)
      entries:
      - - damage: 1d8+18
          crit_range: 15-20
      attack: +5 holy cold iron club
      bonus:
      - 48
      - 43
      - 38
      - 33
    - text: gore +43 (2d8+18)
      entries:
      - - damage: 2d8+18
      attack: gore
      bonus:
      - 43
  ranged:
  - - text: +5 evil outsider bane composite longbow +51/+46/+41/+36 (2d6+14/19-20/×4)
      entries:
      - - damage: 2d6+14
          crit_range: 19-20
          crit_multiplier: 4
      attack: +5 evil outsider bane composite longbow
      bonus:
      - 51
      - 46
      - 41
      - 36
  special:
  - greater slaying arrow
  - horned lord's charge
  - powerful charge (gore, 4d8+13 and horned lord's charge)
  - wild shape (as 20th level druid)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: Constant
  - name: detect lies
    source: default
    freq: Constant
  - name: detect poison
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
  - name: haste
    source: default
    freq: At will
  - name: true strike
    source: default
    freq: At will
  - name: break enchantment
    source: default
    freq: 3/day
  - name: breath of life
    source: default
    freq: 3/day
  - name: dimensional anchor
    source: default
    freq: 3/day
    DC: 19
  - name: discern location
    source: default
    freq: 1/day
  - name: mage's disjunction
    source: default
    freq: 1/day
    DC: 24
  - name: time stop
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 25
spells:
  entries:
  - name: elemental swarm
    source: Druid
    level: 9
  - name: foresight
    source: Druid
    level: 9
  - name: summon nature's ally IX
    source: Druid
    level: 9
    count: 2
  - name: control plants
    source: Druid
    level: 8
    DC: 24
  - name: repel metal or stone
    source: Druid
    level: 8
  - name: sunburst
    source: Druid
    level: 8
    DC: 24
  - name: whirlwind
    source: Druid
    level: 8
    DC: 24
  - name: control weather
    source: Druid
    level: 7
  - name: creeping doom
    source: Druid
    level: 7
    DC: 23
  - name: heal
    source: Druid
    level: 7
  - name: sunbeam
    source: Druid
    level: 7
    DC: 23
  - name: antilife shell
    source: Druid
    level: 6
  - name: greater dispel magic
    source: Druid
    level: 6
    count: 2
  - name: move earth
    source: Druid
    level: 6
  - name: wall of stone
    source: Druid
    level: 6
    DC: 22
  - name: atonement
    source: Druid
    level: 5
  - name: baleful polymorph
    source: Druid
    level: 5
    DC: 21
  - name: deathward
    source: Druid
    level: 5
  - name: transmute rock to mud
    source: Druid
    level: 5
  - name: wall of thorns
    source: Druid
    level: 5
  - name: cure serious wounds
    source: Druid
    level: 4
    count: 2
  - name: freedom of movement
    source: Druid
    level: 4
  - name: rusting grasp
    source: Druid
    level: 4
  - superscripts:
    - APG
    name: true form
    source: Druid
    level: 4
    DC: 20
  - name: call lightning
    source: Druid
    level: 3
    DC: 19
  - name: cure moderate wounds
    source: Druid
    level: 3
  - name: neutralize poison
    source: Druid
    level: 3
    count: 2
  - name: remove disease
    source: Druid
    level: 3
  - name: chill metal
    source: Druid
    level: 2
    DC: 18
  - name: fog cloud
    source: Druid
    level: 2
  - name: heat metal
    source: Druid
    level: 2
    DC: 18
  - name: lesser restoration
    source: Druid
    level: 2
  - name: resist energy
    source: Druid
    level: 2
    count: 2
  - name: calm animals
    source: Druid
    level: 1
    DC: 17
    count: 2
  - name: cure light wounds
    source: Druid
    level: 1
    count: 2
  - name: pass without trace
    source: Druid
    level: 1
    count: 2
  - name: create water
    source: Druid
    level: 0
  - name: mending
    source: Druid
    level: 0
  - name: purify food and drink
    source: Druid
    level: 0
  - name: read magic
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 20
    concentration: 26
ability_scores:
  STR: 29
  DEX: 35
  CON: 39
  INT: 18
  WIS: 22
  CHA: 21
BAB: 34
CMB: 44
CMD: 67
feats:
- name: Combat Reflexes
- name: Deadly Aim
- name: Dodge
- name: Improved Critical (longbow)
- name: Improved Critical (scimitar)
- name: Improved Initiative
- name: Improved Precise Shot
- name: Mobility
- name: Point-Blank Shot
- name: Power Attack
- name: Precise Shot
- name: Quick Draw
- name: Rapid Shot
- name: Shot on the Run
- name: Weapon Focus (club)
- name: Weapon Focus (gore)
- name: Weapon Focus (longbow)
skills:
  Acrobatics: 46
    when jumping: 50
  Diplomacy: 22
  Disguise: 22
  Fly: 10
  Handle Animal: 22
  Intimidate: 22
  Knowledge (geography): 24
  Knowledge (nature): 24
  Knowledge (planes): 24
  Knowledge (religion): 21
  Perception: 43
  Ride: 32
  Sense Motive: 43
  Stealth: 45
  Survival: 43
  Swim: 26
languages:
- Celestial
- Draconic
- Infernal
- Sylvan
- truespeech
special_qualities:
- change shape (any humanoid, alter self)
- empyreal lord traits
- perfect archer
- seed of life
ecology:
  environment: any forest or plain (Elysium)
  organization: unique
  treasure_type: standard
  treasure:
  - +5 holy cold iron club
  - +5 evil outsider bane longbow
  - other treasure
special_abilities:
  Greater Slaying Arrow (Su): Cernunnos can spend 1 minute crafting any kind of greater
    slaying arrow (DC 32). He can have only one such arrow at a time, and it only
    functions for him. The save DC is Charisma-based.
  Horned Lord's Charge (Ex): An opponent hit by Cernunnos's powerful charge must succeed
    at a DC 39 Fort save or be exhausted, sickened, or stunned (Cernunnos's choice)
    for 1d4 rounds. The save DC is Constitution-based.
  Lightning Rod (Su): Cernunnos absorbs and negates any electricity effect that targets
    him or includes him in its area. As an immediate action on his next turn, he can
    release this energy to grant the shock weapon special ability to all weapons wielded
    by his allies within 30 feet for 1 round.
  Perfect Archer (Ex): Cernunnos does not provoke attacks of opportunity for firing
    bow weapons in melee. He threatens squares out to his normal reach when wielding
    a bow. He automatically creates arrows when firing a bow and treats any bow he
    wields as if it had a range increment of 500 feet.
  Primal Aura (Su): Any summoned animal or creature summoned by summon nature's ally
    gains a +4 enhancement bonus to its Strength and Constitution while within Cernunnos's
    aura. Any such creature summoned within his aura obeys him as if he had summoned
    it (if given conflicting orders, the creature obeys Cernunnos instead of its summoner).
  Spells: Cernunnos casts spells as 20th-level druid.
  Unbound (Su): Cernunnos is immune to any effects that restrict or force extradimensional
    movement upon him, such as banishment or dimensional anchor. He may allow these
    effects to affect him.
desc_long: |-
  Cernunnos is a powerful empyreal lord who embodies the primeval force of nature as well as its wildness. He surrounds himself with counselors and advisors from all of the celestial races. Although he rarely makes a rash decision, he occasionally lets anger overwhelm his better judgment, even going so far as to swear personal vendettas against specific demon lords or archdevils. A peerless archer and hunter, in such moments of vengeance Cernunnos is tempted to visit Hell or the Abyss to personally exact his revenge.

  His preference for decisive action against enemies puts Cernunnos at odds with Korada. Though Cernunnos agrees that even the wickedest souls can seek redemption, he worries that lives would be lost in the time it would take to allow a fiend to seek enlightenment.

  The Horned Lord appears as a tall and muscular humanoid with elven features, tan skin, and a pair of antlers growing from his brow. Cernunnos dresses in simple clothes and leathers, died in natural colors but typically woven or worked with motifs of birds in flight or leaping animals.

  On Elysium, Cernunnos dwells in an expansive palace constructed of interwoven trees and capped with lush foliage. Known as Briarbough, this sprawling complex of gardens and pools is his seat of power and a place of healing where celestials and good mortals come to have their most grievous wounds tended. Beyond lies hundreds of miles of pristine forest and plains; animals killed here are reborn the next day, fully healed. In times of war, Briarbough serves as a headquarters and hospital for good outsiders.

  When not in Elysium, Cernunnos works with other celestial races to stem the spread of evil throughout the cosmos. Recognizing that-despite his power-he is still only one person, the Horned Lord uses his abilities to strengthen and bolster those already allied against darkness, training marshals and emissaries to work as his agents in the mortal and fey worlds. He favors druids and rangers-archers in particular-among his devotees.

  In combat, Cernunnos uses stealth and range to draw enemies to terrain of his choosing. The Empyreal Lord then uses his magic to further shape the battlefield to hamper his foes before closing for melee.

---

# Empyreal Lord, Cernunnos
This tall, graceful person has elven features, the horns of a majestic stag and a piercing, ageless stare.
**Source** Bestiary 4 pg. 88
**XP** 9,830,400

CG Large outsider (azata, chaotic, extraplanar, good)
**Init** +16; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Evil|detect evil]]_, detect lies, _[[spells/Detect Poison|detect poison]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +43
**Aura** primal (30 ft.)

##### Defense

**AC** 48, touch 22, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+12 Dex, +1 dodge, +26 natural, –1 size)
**hp** 663 (34d10+476); _[[universal monster rules/Regeneration|regeneration]]_ 10 (evil artifacts, effects, and spells)
**Fort** +25, **Ref** +31, **Will** +25
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, lightning rod, _[[items/Armor Magic Abilities/Unbound|unbound]]_; **DR** 15/epic and evil; **Immune** ability damage, ability drain, charm effects, compulsion effects, death effects, electricity, _[[universal monster rules/Energy Drain|energy drain]]_, petrification; **Resist** cold 30, fire 30; **SR** 41

##### Offense
**Speed** 40 ft., fly 60 ft. (average)
**Melee** +5 holy cold iron _[[items/Weapon/Club|club]]_ +48/+43/+38/+33 (1d8+18/15–20), gore +43 (2d8+18)
**Ranged** +5 evil outsider _[[spells/Bane|bane]]_ _[[items/Weapon/Composite longbow|composite longbow]]_ +51/+46/+41/+36 (2d6+14/19–20/×4)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** greater slaying arrow, horned lord’s charge, _[[universal monster rules/Powerful Charge|powerful charge]]_ (gore, 4d8+13 and horned lord’s charge), wild shape (as 20th level _[[classes/Druid|druid]]_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +25)
Constant—_detect evil_, detect lies, _detect poison_, _freedom of movement_, _true seeing_
At will—greater teleport, _[[spells/Haste|haste]]_*, _[[spells/True Strike|true strike]]_*
3/day—_[[spells/Break Enchantment|break enchantment]]_*, _[[spells/Breath Of Life|breath of life]]_*, _[[spells/Dimensional Anchor|dimensional anchor]]_ (DC 19)
1/day—_[[spells/Discern Location|discern location]]_, mage’s disjunction* (DC 24), _[[spells/Time Stop|time stop]]_*
* Cernunnos can use the mythic version of this ability in his realm.
**_Druid_ Spells Prepared **(CL 20th; concentration +26)
9th—_[[spells/Elemental Swarm|elemental swarm]]_, _[[spells/Foresight|foresight]]_, _[[universal monster rules/Summon|summon]]_ nature’s ally IX (2)
8th—_[[spells/Control Plants|control plants]]_ (DC 24), _[[spells/Repel Metal or Stone|repel metal or stone]]_, _[[spells/Sunburst|sunburst]]_ (DC 24), _[[universal monster rules/Whirlwind|whirlwind]]_ (DC 24)
7th—_[[spells/Control Weather|control weather]]_, _[[spells/Creeping Doom|creeping doom]]_ (DC 23), _[[spells/Heal|heal]]_, _[[spells/Sunbeam|sunbeam]]_ (DC 23)
6th—_[[spells/Antilife Shell|antilife shell]]_, greater _[[spells/Dispel Magic|dispel magic]]_ (2), _[[spells/Move Earth|move earth]]_, _[[spells/Wall Of Stone|wall of stone]]_ (DC 22)
5th—_[[spells/Atonement|atonement]]_, _[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 21), deathward, _[[spells/Transmute Rock to Mud|transmute rock to mud]]_, _[[spells/Wall Of Thorns|wall of thorns]]_
4th—_[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), _freedom of movement_, _[[spells/Rusting Grasp|rusting grasp]]_, _[[spells/True Form|true form]]_ (DC 20)
3rd—_[[spells/Call Lightning|call lightning]]_ (DC 19), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Neutralize Poison|neutralize poison]]_ (2), _[[spells/Remove Disease|remove disease]]_
2nd—_[[spells/Chill Metal|chill metal]]_ (DC 18), _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Heat Metal|heat metal]]_ (DC 18), lesser _[[spells/Restoration|restoration]]_, _[[spells/Resist Energy|resist energy]]_ (2)
1st—_[[spells/Calm Animals|calm animals]]_ (DC 17, 2), _[[spells/Cure Light Wounds|cure light wounds]]_ (2), _[[spells/Pass without Trace|pass without trace]]_ (2)
0—_[[spells/Create Water|create water]]_, _[[spells/Mending|mending]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 29, **Dex** 35, **Con** 39, **Int** 18, **Wis** 22, **Cha** 21
**Base Atk** +34; **CMB** +44; **CMD** 67
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_[[items/Weapon/Longbow|longbow]]_), _Improved Critical_ (_[[items/Weapon/Scimitar|scimitar]]_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Precise Shot|Improved Precise Shot]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Quick Draw|Quick Draw]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Shot on the Run|Shot on the Run]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_club_), _Weapon Focus_ (gore), _Weapon Focus_ (_longbow_)
**Skills** Acrobatics +46 (+50 when jumping), Diplomacy +22, Disguise +22, Fly +10, Handle Animal +22, Intimidate +22, Knowledge (geography) +24, Knowledge (nature) +24, Knowledge (planes) +24, Knowledge (religion) +21, Perception +43, Ride +32, Sense Motive +43, Stealth +45, Survival +43, Swim +26
**Languages** Celestial, Draconic, Infernal, Sylvan; truespeech
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any humanoid, _[[spells/Alter Self|alter self]]_), _[[universal monster rules/Empyreal Lord Traits|empyreal lord traits]]_, perfect archer, seed of life

##### Ecology

**Environment** any forest or plain (Elysium)
**Organization** unique
**Treasure** standard (+5 holy cold iron _club_, +5 evil outsider _bane_ _longbow_, other treasure)

### Special Abilities

**Greater Slaying Arrow (Su)** Cernunnos can spend 1 minute crafting any kind of greater slaying arrow (DC 32). He can have only one such arrow at a time, and it only functions for him. The save DC is Charisma-based.

**Horned Lord’s Charge (Ex)** An opponent hit by Cernunnos’s _powerful charge_ must succeed at a DC 39 Fort save or be _[[conditions/Exhausted|exhausted]]_, _[[conditions/Sickened|sickened]]_, or _[[conditions/Stunned|stunned]]_ (Cernunnos’s choice) for 1d4 rounds. The save DC is Constitution-based.

**Lightning Rod (Su)** Cernunnos absorbs and negates any electricity effect that targets him or includes him in its area. As an immediate action on his next turn, he can release this energy to grant the _[[items/Weapon Magic Abilities/Shock|shock]]_ weapon special ability to all weapons wielded by his allies within 30 feet for 1 round.

**Perfect Archer (Ex)** Cernunnos does not provoke attacks of opportunity for firing bow weapons in melee. He threatens squares out to his normal reach when wielding a bow. He automatically creates arrows when firing a bow and treats any bow he wields as if it had a range increment of 500 feet.

**Primal Aura (Su)** Any summoned animal or creature summoned by _summon_ nature’s ally gains a +4 enhancement bonus to its Strength and Constitution while within Cernunnos’s aura. Any such creature summoned within his aura obeys him as if he had summoned it (if given conflicting orders, the creature obeys Cernunnos instead of its _[[classes/Summoner|summoner]]_).
**Spells** Cernunnos casts spells as 20th-level _druid_.

**_Unbound_ (Su)** Cernunnos is immune to any effects that restrict or force extradimensional movement upon him, such as _[[spells/Banishment|banishment]]_ or _dimensional anchor_. He may allow these effects to affect him.

##### Description

Cernunnos is a powerful empyreal lord who embodies the primeval force of nature as well as its wildness. He surrounds himself with counselors and advisors from all of the celestial races. Although he rarely makes a rash decision, he occasionally lets anger _[[feats/Overwhelm|overwhelm]]_ his better judgment, even going so far as to swear personal vendettas against specific demon lords or archdevils. A peerless archer and _[[classes/Hunter|hunter]]_, in such moments of _[[feats/Vengeance|vengeance]]_ Cernunnos is tempted to visit Hell or the Abyss to personally exact his revenge.

His preference for decisive action against enemies puts Cernunnos at odds with Korada. Though Cernunnos agrees that even the wickedest souls can seek _[[feats/Redemption|redemption]]_, he worries that lives would be lost in the time it would take to allow a fiend to seek enlightenment.

The Horned Lord appears as a tall and muscular humanoid with elven features, tan skin, and a pair of antlers _[[items/Weapon Magic Abilities/Growing|growing]]_ from his brow. Cernunnos dresses in simple clothes and leathers, died in natural colors but typically woven or worked with motifs of birds in _[[universal monster rules/Flight|flight]]_ or leaping animals.

On Elysium, Cernunnos dwells in an expansive palace constructed of interwoven trees and capped with lush foliage. Known as Briarbough, this sprawling complex of gardens and pools is his seat of power and a place of healing where celestials and good mortals come to have their most grievous wounds tended. Beyond lies hundreds of miles of pristine forest and plains; animals killed here are reborn the next day, fully healed. In times of war, Briarbough serves as a headquarters and hospital for good outsiders.

When not in Elysium, Cernunnos works with other celestial races to stem the spread of evil throughout the cosmos. Recognizing that—despite his power—he is still only one person, the Horned Lord uses his abilities to strengthen and bolster those already allied against _[[spells/Darkness|darkness]]_, _[[items/Weapon Magic Abilities/Training|training]]_ marshals and emissaries to work as his agents in the mortal and fey worlds. He favors druids and rangers—archers in particular—among his devotees.

In combat, Cernunnos uses stealth and range to draw enemies to terrain of his choosing. The Empyreal Lord then uses his magic to further shape the battlefield to hamper his foes before closing for melee.