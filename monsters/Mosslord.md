---
cssclass: [monsters]
title1: Mosslord
desc_short: This towering, four-armed humanoid seems to be made of moss andsplintered
  wood, its face sinister and mouthless.
title2: Mosslord
CR: 18
sources:
- name: Bestiary 6
  page: 194
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 153600
alignment: LE
size: Large
type: plant
initiative:
  bonus: 13
senses:
  darkvision: 60
  greensight: true
  low-light vision: true
  see invisibility: true
AC:
  AC: 33
  touch: 19
  flat_footed: 23
  components:
    dex: 9
    dodge: 1
    natural,-1 size: 14
HP:
  HP: 312
  long: 25d8+200
  regeneration: 10
  regeneration_weakness: cold
saves:
  fort: 22
  ref: 17
  will: 17
defensive_abilities:
- perennial
DR:
- amount: 15
  weakness: magic and slashing
immunities:
- fire
- plant traits
resistances:
  electricity: 30
speeds:
  base: 30
attacks:
  melee:
  - - text: 4 claws +28 (2d8+11/19-20 plus curse)
      entries:
      - - damage: 2d8+11
          crit_range: 19-20
        - effect: curse
      count: 4
      attack: claws
      bonus:
      - 28
  special:
  - deadwood curse
  - sheets of moss
  - yellow mold blast
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: nondetection
    source: default
    freq: Constant
  - name: pass without trace
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: speak with plants
    source: default
    freq: Constant
  - name: command plants
    source: default
    freq: At will
    DC: 20
  - name: fear
    source: default
    freq: At will
    DC: 20
  - name: mind thrust VI
    source: default
    freq: At will
    DC: 22
  - name: transport via plants
    source: default
    freq: At will
  - name: tree shape
    source: default
    freq: At will
  - name: animate plants
    source: default
    freq: 3/day
  - name: displacement
    source: default
    freq: 3/day
  - name: quickened fungal infestation
    source: default
    freq: 3/day
    DC: 19
  - name: control plants
    source: default
    freq: 1/day
    DC: 24
  - name: microcosm
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 18
    concentration: 24
ability_scores:
  STR: 32
  DEX: 28
  CON: 26
  INT: 27
  WIS: 25
  CHA: 23
BAB: 18
CMB: 30
CMB_other: +34 sunder
CMD: 50
CMD_other: 52 vs. sunder
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Critical Focus
- name: Dodge
- name: Greater Sunder
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Improved Sunder
- name: Iron Will
- name: Mobility
- name: Power Attack
- name: QuickenSpell-Like Ability (fungal infestation)
- name: Staggering Critical
skills:
  Climb: 36
  Intimidate: 31
  Knowledge (arcana): 33
  Knowledge (geography,nature): 33
  Perception: 35
  Sense Motive: 32
  Spellcraft: 33
  Stealth: 33
  Survival: 32
languages:
- Aklo
- Common
- Sylvan
- speak with plants
- telepathy100 ft.
ecology:
  environment: temperate forests
  organization: solitary
  treasure_type: triple
special_abilities:
  Deadwood Curse (Su): When a mosslord confirms a critical hit with one of its claws,
    the victim must succeed at a DC 30 Fortitude save or a horrid curse transforms
    one of its limbs into an immobile wooden branch. Roll 1d4 to determine which limb
    is affected (1-right arm, 2-left arm, 3-right leg, 4-left leg; adjust the die
    as necessary for creatures with fewer or more limbs). The cursed limb hardens
    and becomes entirely immobile until the curse is lifted. If an arm is affected,
    the victim's Strength is reduced by 2 and it cannot wield weapons in that hand
    or use the hand in any way. If a victim's leg is affected, the victim's Dexterity
    is reduced by 2 and its base speed is reduced by 15 feet. Each time a creature
    is affected by this curse, a new limb is affected, and the effects stack. If a
    cursed limb is amputated and regrown via magic, the new limb regrows as deadwood
    as long as the curse persists. This is a curse effect. The save DC is Constitution-based.
  Perennial (Su): When a mosslord dies, its body decomposes normally but regrows in
    60 days. A dead mosslord cannot regrow during winter months or when there is frost
    or snow on the ground where it was slain; in such a condition, its regrowth is
    delayed until the thaw. If the region where the mosslord was slain is affected
    by a lasting winter (either via magic or as a result of natural conditions), its
    regrowth can be delayed indefinitely. Even completely destroying a mosslord's
    body won't stop its eventual regrowth. A blight or diminish plants spell applied
    to a mosslord's remains can ensure its permanent death if the caster succeeds
    at a DC 30 caster level check. A mosslord slain on any plane other than the Material
    Plane remains dead permanently. Obscure rituals can also aid in the permanent
    death of a mosslord, at the GM's discretion.
  Sheets of Moss (Su): Once every 1d4 rounds as a move action, a mosslord can cover
    a 20-foot-square area in a thick blanket of toxic moss at a range of up to 90
    feet. Living creatures in the area are automatically entangled and sickened and
    must succeed at a DC 30 Fortitude save or take 1d4 points of Constitution damage
    per round until the moss dissipates or is destroyed. The moss has 25 hit points
    per 5-foot square, but can only be damaged by cold or effects that specifically
    target plants (such as blight) or deal additional damage to plants (such as horrid
    wilting). Otherwise, the sheets of moss wither away automatically after 1d4+4
    rounds. The sickened effect and Constitution damage are poison effects. The save
    DC is Constitution-based.
  Yellow Mold Blast (Su): As a standard action, a mosslord can swiftly extrude a puffball
    and hurl it up to 60 feet. Upon impact, the puffball bursts into an unusually
    thick and potent cloud of yellow mold spores. This cloud of spores fills a 10-foot-radius
    area, obscuring vision as if it were a fog cloud and affecting all creatures within
    the area with yellow mold (Pathfinder RPG Core Rulebook 416), except the Fortitude
    save to resist the mold's poisonous effects is DC 30. A creature that takes Constitution
    damage from these thick spores is also nauseated for 1 round. The cloud of spores
    persists for 1d4 rounds, after which it automatically dissipates. Creatures with
    greensight can see through these clouds of spores with ease. The save DC is Constitution-based.
desc_long: |-
  Tales of the wretched mosslord have existed for as long as humanity has dared dwell amid the forests of the world. It appears in grotesque pictographs of long dead civilizations, covering the walls of lost cities on sunken continents or hidden in overgrown jungles. So ancient is the creature that its true origin remains unknown. In the cultures whose lore and legend tell of the mosslord, it is described as the living incarnation of the forest's vengeance against the encroachment of civilization, a fury given mind and focus toward the destruction of humanity. To date, no one has ever reported spotting more than a single mosslord at a time, prompting speculation as to whether more than a single mosslord exists, or if it is a singular entity that simply regrows itself each time it is destroyed. 

  Most tales of the mosslord's intentions hold true, although the legends of there being but one mosslord are a false hope-in truth, multiple mosslords exist, and wherever one surfaces, ruin inevitably follows. Yet mosslords are hardly the simple, violent juggernauts that old legends purport. Instead, these wickedly intelligent creatures mastermind elaborate campaigns against civilization. Capable of commanding hordes of plant creatures, they typically spend months or even years seeding a target before launching an incursion-even if their attacks seem sudden and unprovoked to the victims. They are clever combatants, shielding themselves from direct attacks and avoiding melee if at all possible, in order to command and maneuver allies. Still, the creature is an able warrior in addition to having a potent arsenal of spells, and it doesn't shy from engaging opponents in melee when directly faced with an immediate opponent. Among all humanoid forms of life, they despise humans and halflings in particular. 

  A mosslord has no known or ties to the fey world or to those worlds or planes beyond the material realm. Though the mosslord is no deity, it is a wholly supernatural being and the apocalyptic texts of over a dozen different religions depict its wrath. These texts often revile the mosslord and condemn those who would worship it or pay it reverence. Despite ominous warnings, history reports a handful of occasions when doom cults praised, venerated, and pledged fealty to mosslords. Some even credit or blame such cults for the creation of the first mosslords, for it seems odd that plant creatures would naturally form upon the wooden frames that hold its fungal flesh in the form of a bipedal humanoid. Regardless, such efforts tend to be short lived; as soon as the cultists capture the mosslord's attention, they find they have only attracted its relentless and utter destruction. 

  The mosslord's body consists of a large skeletal frame that towers over 15 feet tall, fashioned from rough-cut pieces of wood. A thick layer of moss encompasses this frame, creating the appearance of flesh. While a mosslord's body appears constructed, the creature is fully sentient and highly intelligent. Despite their similar hateful and destructive views of civilization, mosslords do not cooperate with blights or whisperers, and they often compete with these strange entities for control over their woodland territories.

---

# Mosslord
This towering, four-armed humanoid seems to be made of moss and

splintered wood, its face sinister and mouthless.
**Source** Bestiary 6 pg. 194
**XP** 153,600

LE Large plant
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Greensight|greensight]]_, _[[universal monster rules/Low-Light Vision|low-light vision]]_,

_[[spells/See Invisibility|see invisibility]]_; Perception +35

##### Defense

**AC** 33, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+9 Dex, +1 dodge, +14 natural,

–1 size)
**hp** 312 (25d8+200); _[[universal monster rules/Regeneration|regeneration]]_ 10 (cold)
**Fort** +22, **Ref** +17, **Will** +17
**Defensive Abilities** perennial; **DR** 15/magic and slashing; **Immune** fire, _[[universal monster rules/Plant Traits|plant traits]]_; **Resist** electricity 30

##### Offense
**Speed** 30 ft.
**Melee** 4 claws +28 (2d8+11/19–20 plus curse)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** deadwood curse, sheets of moss, yellow mold blast
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +24)
Constant—_[[spells/Nondetection|nondetection]]_, _[[spells/Pass without Trace|pass without trace]]_, _see invisibility_, _[[spells/Speak with Plants|speak with plants]]_ 
At will—_[[spells/Command Plants|command plants]]_ (DC 20), _[[universal monster rules/Fear|fear]]_ (DC 20), _[[spells/Mind Thrust VI|mind thrust VI]]_ (DC 22), _[[spells/Transport via Plants|transport via plants]]_, _[[spells/Tree Shape|tree shape]]_ 
3/day—_[[spells/Animate Plants|animate plants]]_, _[[spells/Displacement|displacement]]_, quickened _[[spells/Fungal Infestation|fungal infestation]]_ (DC 19) 
1/day—_[[spells/Control Plants|control plants]]_ (DC 24), _[[spells/Microcosm|microcosm]]_ (DC 25)

##### Statistics
**Str** 32, **Dex** 28, **Con** 26, **Int** 27, **Wis** 25, **Cha** 23
**Base Atk** +18; **CMB** +30 (+34 sunder); **CMD** 50 (52 vs. sunder)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, Quicken

Spell-Like Ability (_fungal infestation_), _[[feats/Staggering Critical|Staggering Critical]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +36, Intimidate +31, Knowledge (arcana, geography,

nature) +33, Perception +35, Sense Motive +32, Spellcraft +33,

Stealth +33, Survival +32
**Languages** Aklo, Common, Sylvan; _speak with plants_; _[[universal monster rules/Telepathy|telepathy]]_

100 ft.

##### Ecology

**Environment** temperate forests
**Organization** solitary
**Treasure** triple

### Special Abilities

**Deadwood Curse (Su)** When a _[[monsters/Mosslord|mosslord]]_ confirms a critical hit with one of its claws, the victim must succeed at a DC 30 Fortitude save or a horrid curse transforms one of its limbs into an immobile wooden branch. Roll 1d4 to determine which limb is affected (1—right arm, 2—left arm, 3—right leg, 4—left leg; adjust the die as necessary for creatures with fewer or more limbs). The cursed limb hardens and becomes entirely immobile until the curse is lifted. If an arm is affected, the victim’s Strength is reduced by 2 and it cannot wield weapons in that hand or use the hand in any way. If a victim’s leg is affected, the victim’s Dexterity is reduced by 2 and its base speed is reduced by 15 feet. Each time a creature is affected by this curse, a new limb is affected, and the effects stack. If a cursed limb is amputated and regrown via magic, the new limb regrows as deadwood as long as the curse persists. This is a curse effect. The save DC is Constitution-based.

**Perennial (Su)** When a _mosslord_ dies, its body decomposes normally but regrows in 60 days. A dead _mosslord_ cannot regrow during winter months or when there is frost or snow on the ground where it was slain; in such a condition, its regrowth is delayed until the thaw. If the region where the _mosslord_ was slain is affected by a lasting winter (either via magic or as a result of natural conditions), its regrowth can be delayed indefinitely. Even completely destroying a _mosslord_’s body won’t stop its eventual regrowth. A _[[spells/Blight|blight]]_ or _[[spells/Diminish Plants|diminish plants]]_ spell applied to a _mosslord_’s remains can ensure its permanent death if the caster succeeds at a DC 30 caster level check. A _mosslord_ slain on any plane other than the Material Plane remains dead permanently. Obscure rituals can also aid in the permanent death of a _mosslord_, at the GM’s discretion.
**Sheets of Moss (Su)** Once every 1d4 rounds as a move action, a _mosslord_ can cover a 20-foot-square area in a thick _[[items/Mundane/Blanket|blanket]]_ of _[[items/Weapon Magic Abilities/Toxic|toxic]]_ moss at a range of up to 90 feet. Living creatures in the area are automatically _[[conditions/Entangled|entangled]]_ and _[[conditions/Sickened|sickened]]_ and must succeed at a DC 30 Fortitude save or take 1d4 points of Constitution damage per round until the moss dissipates or is destroyed. The moss has 25 hit points per 5-foot square, but can only be damaged by cold or effects that specifically target plants (such as _blight_) or deal additional damage to plants (such as _[[spells/Horrid Wilting|horrid wilting]]_). Otherwise, the sheets of moss wither away automatically after 1d4+4 rounds. The _sickened_ effect and Constitution damage are poison effects. The save DC is Constitution-based.

**Yellow Mold Blast (Su)** As a standard action, a _mosslord_ can swiftly extrude a puffball and hurl it up to 60 feet. Upon _[[items/Weapon Magic Abilities/Impact|impact]]_, the puffball bursts into an unusually thick and _[[items/Weapon Magic Abilities/Potent|potent]]_ cloud of yellow mold spores. This cloud of spores fills a 10-foot-radius area, obscuring _[[spells/Vision|vision]]_ as if it were a _[[spells/Fog Cloud|fog cloud]]_ and affecting all creatures within the area with yellow mold (Pathfinder RPG Core Rulebook 416), except the Fortitude save to resist the mold’s poisonous effects is DC 30. A creature that takes Constitution damage from these thick spores is also _[[conditions/Nauseated|nauseated]]_ for 1 round. The cloud of spores persists for 1d4 rounds, after which it automatically dissipates. Creatures with _greensight_ can see through these clouds of spores with ease. The save DC is Constitution-based.

##### Description

Tales of the wretched _mosslord_ have existed for as long as humanity has dared dwell amid the forests of the world. It appears in grotesque pictographs of long dead civilizations, covering the walls of lost cities on sunken continents or hidden in overgrown jungles. So ancient is the creature that its true origin remains _[[monsters/Unknown|unknown]]_. In the cultures whose lore and legend tell of the _mosslord_, it is described as the living incarnation of the forest’s _[[feats/Vengeance|vengeance]]_ against the encroachment of civilization, a fury given mind and focus toward the _[[spells/Destruction|destruction]]_ of humanity. To date, no one has ever reported spotting more than a single _mosslord_ at a time, prompting speculation as to whether more than a single _mosslord_ exists, or if it is a singular entity that simply regrows itself each time it is destroyed.

Most tales of the _mosslord_’s intentions hold true, although the legends of there being but one _mosslord_ are a false hope—in truth, multiple mosslords exist, and wherever one surfaces, ruin inevitably follows. Yet mosslords are hardly the simple, violent juggernauts that old legends purport. Instead, these wickedly intelligent creatures mastermind elaborate campaigns against civilization. Capable of commanding hordes of plant creatures, they typically spend months or even years seeding a target before launching an incursion—even if their attacks seem sudden and unprovoked to the victims. They are clever combatants, shielding themselves from direct attacks and avoiding melee if at all possible, in order to _[[spells/Command|command]]_ and maneuver allies. Still, the creature is an able warrior in addition to having a _potent_ arsenal of spells, and it doesn’t shy from engaging opponents in melee when directly faced with an immediate opponent. Among all humanoid forms of life, they despise humans and halflings in particular.

A _mosslord_ has no known or ties to the fey world or to those worlds or planes beyond the material realm. Though the _mosslord_ is no deity, it is a wholly supernatural being and the apocalyptic texts of over a dozen different religions depict its wrath. These texts often revile the _mosslord_ and condemn those who would worship it or pay it reverence. Despite _[[items/Weapon Magic Abilities/Ominous|ominous]]_ warnings, history reports a handful of occasions when _[[spells/Doom|doom]]_ cults praised, venerated, and pledged fealty to mosslords. Some even credit or blame such cults for the creation of the first mosslords, for it seems odd that plant creatures would naturally form upon the wooden frames that hold its fungal flesh in the form of a bipedal humanoid. Regardless, such efforts tend to be short lived; as soon as the cultists capture the _mosslord_’s attention, they find they have only attracted its relentless and utter _destruction_.

The _mosslord_’s body consists of a large skeletal frame that towers over 15 feet tall, fashioned from rough-cut pieces of wood. A thick layer of moss encompasses this frame, creating the appearance of flesh. While a _mosslord_’s body appears constructed, the creature is fully sentient and highly intelligent. Despite their similar hateful and destructive views of civilization, mosslords do not cooperate with blights or whisperers, and they often compete with these strange entities for control over their woodland territories.