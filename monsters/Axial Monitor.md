---
cssclass: [monsters]
title1: Axial Monitor
desc_short: This imposing creature stands on three legs, with a body like three torsos
  fused together. These torsos are topped with a single head bearing three faces,
  each set in a bland, serene expression.
title2: Axial Monitor
CR: 15
sources:
- name: "Pathfinder #131: The Reaper's Right Hand"
  page: 82
  link: http://paizo.com/products/btpy9x04?Pathfinder-Adventure-Path-The-Reaper-s-Right-Hand
XP: 51200
alignment: LN
size: Large
type: outsider
subtypes:
- extraplanar
- lawful
initiative:
  bonus: 7
senses:
  blindsight: 30
  darkvision: 90
  true seeing: true
AC:
  AC: 30
  touch: 12
  flat_footed: 27
  components:
    armor: 6
    dex: 3
    natural: 12
    size: -1
HP:
  HP: 210
  long: 20d10+100
  regeneration: 5
  regeneration_weakness: chaotic or magic
saves:
  fort: 17
  ref: 11
  will: 18
DR:
- amount: 10
  weakness: chaotic
immunities:
- disease
- electricity
- mind-affecting effects
resistances:
  cold: 10
  fire: 10
SR: 26
speeds:
  base: 40
  base_other: 30 ft. in armor
attacks:
  melee:
  - - text: +1 merciful greatclub +26/+21/+16/+11 (2d8+10)
      entries:
      - - damage: 2d8+10
      attack: +1 merciful greatclub
      bonus:
      - 26
      - 21
      - 16
      - 11
    - text: tentacle +20 (1d6+3 plus grab)
      entries:
      - - damage: 1d6+3
        - effect: grab
      attack: tentacle
      bonus:
      - 20
    - text: slam +20 (2d6+3 plus energized maul)
      entries:
      - - damage: 2d6+3
        - effect: energized maul
      attack: slam
      bonus:
      - 20
  - - text: +1 axiomatic glaive +26 (2d8+10/×3)
      entries:
      - - damage: 2d8+10
          crit_multiplier: 3
      attack: +1 axiomatic glaive
      bonus:
      - 26
    - text: +1 merciful greatclub +26 (2d8+10)
      entries:
      - - damage: 2d8+10
      attack: +1 merciful greatclub
      bonus:
      - 26
    - text: tentacle +25 (1d6+3 plus grab)
      entries:
      - - damage: 1d6+3
        - effect: grab
      attack: tentacle
      bonus:
      - 25
    - text: slam +25 (2d6+3 plus energized maul)
      entries:
      - - damage: 2d6+3
        - effect: energized maul
      attack: slam
      bonus:
      - 25
  special:
  - energized maul
  - tripartite assault
  - watchful faces
space: 10
reach: 10
reach_other: 15 ft. with glaive and tentacle
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: detect chaos
    source: default
    freq: At will
  - name: overland flight
    source: default
    freq: At will
  - name: detect thoughts
    source: default
    freq: 3/day
    DC: 15
  - name: dimension door
    source: default
    freq: 3/day
  - name: dimensional anchor
    source: default
    freq: 3/day
  - name: dispel chaos
    source: default
    freq: 3/day
    DC: 18
  - name: hold monster
    source: default
    freq: 3/day
    DC: 18
  - name: order's wrath
    source: default
    freq: 3/day
    DC: 17
  - name: sending
    source: default
    freq: 3/day
  - name: break enchantment
    source: default
    freq: 1/day
  - name: dictum
    source: default
    freq: 1/day
    DC: 20
  - name: mass hold monster
    source: default
    freq: 1/day
    DC: 22
  sources:
  - name: default
    CL: 20
    concentration: 23
ability_scores:
  STR: 23
  DEX: 16
  CON: 21
  INT: 14
  WIS: 18
  CHA: 17
BAB: 20
CMB: 27
CMB_other: +29 disarm and trip
CMD: 40
CMD_other: 42 vs. disarm and trip
feats:
- name: Cleave
- name: Combat Expertise
- name: Great Cleave
- name: Improved Disarm
- name: Improved Initiative
- name: Improved Trip
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Skill Focus (Perception)
skills:
  Acrobatics: 23
  Diplomacy: 26
  Intimidate: 26
  Knowledge (local): 25
  Knowledge (planes): 25
  Perception: 41
  Sense Motive: 31
  Spellcraft: 22
  _racial_mods:
    Perception:
      _: 8
    Sense Motive:
      _: 4
languages:
- Abyssal
- Celestial
- Common
- truespeech
special_qualities:
- interrogate
ecology:
  environment: any urban (Axis)
  organization: solitary, patrol (2-4), squad (5-8), precinct (9-16), or academy (21-40)
  treasure_type: double
  treasure:
  - Large mwk breastplate
  - Large +1 axiomatic glaive
  - Large +1 merciful greatclub
  - other treasure
special_abilities:
  Energized Maul (Su): As a swift action, an Axial monitor can add the axiomatic,
    flaming, frost, ghost touch, or thundering weapon special ability to its slam
    attack for 1 round, but it cannot add more than one ability at a time.
  Interrogate (Su): When an Axial monitor questions a creature that is helpless or
    pinned, it can compel the creature to answer its questions truthfully unless the
    creature succeeds at a DC 23 Will save. A creature that fails its save is affected
    as though subject to zone of truth, except that the creature must answer questions
    if it is able and cannot refuse to answer or answer evasively. A creature that
    successfully saves cannot be affected by the same Axial monitor's interrogate
    ability for 24 hours. This is a mind-affecting compulsion effect. The save DC
    is Charisma-based.
  Tripartite Assault (Ex): When it makes a full attack, an Axial monitor can choose
    to make a full attack with one weapon and secondary attacks with its tentacle
    and slam, or it can choose to make a single attack with each weapon it wields,
    including its tentacle and slam attacks, with no penalties to its attack rolls
    for fighting with multiple weapons.
  Watchful Faces (Ex): An Axial monitor can make three additional attacks of opportunity
    in a round, one for each head, although it can make no more than a single attack
    for any given opportunity.
desc_long: |-
  The Eternal City of Axis lies at the center of the multiverse, holding the very fabric of reality in some semblance of order through the constant calculations of the axiomite Godmind. Yet even a city of order such as Axis, open as it is to visitors from across the planes, must deal with its own internal law and order on a daily basis. The Axial monitors are tasked with preventing disturbances of order and, when crimes do occur, investigating them to bring the perpetrators to justice.

   Each Axial monitor has the same unusual form: its large, hairless head bears three faces set equidistantly around it, each expression the picture of bland serenity. These faces appear roughly humanoid but are completely smooth, without contours for a brow, nose, or mouth, as though its faces were painted on canvas. The creature's triangular torso has three shoulders, each with two powerful arms. Two pairs of its arms are humanoid, while the third set is mismatched, with one a long, undulating tentacle and the other an articulated limb of banded iron ending in a maul-like head. Below its waist, the creature's body divides into a tripod of legs, each ending in a long foot.

   Axial monitors only attack those presenting a disturbance to Axis's order, whether through the commission of a crime or another civil malfeasance. They call for surrender before a fight and prefer to subdue opponents rather than slay them. Their mandate is to bring prisoners into their dispatch stations so they can be examined and interrogated, and the reasons for their disturbance identified and measured in formal reports. These reports are provided directly to the Godmind, which calculates the mathematically ideal method to counteract and prevent any such future disturbances. After incarceration and calculation, an offender is either set free or transferred to one of the city's rehabilitative prisons under escort by Axial monitors. Although they follow this same process for nearly all creatures, the Axial monitors show no mercy or leniency to proteans and always attack these embodiments of disorder with lethal force on sight.

   Axial monitors are 12 feet tall and weigh 1,200 pounds.

---

# Axial Monitor
This imposing creature stands on three legs, with a body like three torsos fused together. These torsos are topped with a single head bearing three faces, each set in a bland, serene expression.
**Source** Pathfinder #131: The Reaper's Right Hand pg. 82
**XP** 51,200

LN Large outsider (extraplanar, lawful)
**Init** +7; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 90 ft., _[[spells/True Seeing|true seeing]]_; Perception +41

##### Defense

**AC** 30, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+6 armor, +3 Dex, +12 natural, –1 size)
**hp** 210 (20d10+100); _[[universal monster rules/Regeneration|regeneration]]_ 5 (chaotic or magic)
**Fort** +17, **Ref** +11, **Will** +18
**DR** 10/chaotic; **Immune** disease, electricity, mind-affecting effects; **Resist** cold 10, fire 10; **SR** 26

##### Offense
**Speed** 40 ft. (30 ft. in armor)
**Melee** +1 _[[items/Weapon Magic Abilities/Merciful|merciful]]_ _[[items/Weapon/Greatclub|greatclub]]_ +26/+21/+16/+11 (2d8+10), tentacle +20 (1d6+3 plus _[[universal monster rules/Grab|grab]]_), slam +20 (2d6+3 plus energized maul) or
+1 _[[items/Weapon Magic Abilities/Axiomatic|axiomatic]]_ _[[items/Weapon/Glaive|glaive]]_ +26 (2d8+10/×3), +1 _merciful_ _greatclub_ +26 (2d8+10), tentacle +25 (1d6+3 plus _grab_), slam +25 (2d6+3 plus energized maul)
**Space** 10 ft., **Reach** 10 ft. (15 ft. with _glaive_ and tentacle)
**Special Attacks** energized maul, tripartite assault, watchful faces
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +23)
Constant—_true seeing_ 
At will—_[[spells/Detect Chaos|detect chaos]]_, _[[spells/Overland Flight|overland flight]]_ 
3/day—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 15), _[[spells/Dimension Door|dimension door]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Dispel Chaos|dispel chaos]]_ (DC 18), _[[spells/Hold Monster|hold monster]]_ (DC 18), order’s wrath (DC 17), _[[spells/Sending|sending]]_ 
1/day—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Dictum|dictum]]_ (DC 20), mass _hold monster_ (DC 22)

##### Statistics
**Str** 23, **Dex** 16, **Con** 21, **Int** 14, **Wis** 18, **Cha** 17
**Base Atk** +20; **CMB** +27 (+29 disarm and _[[universal monster rules/Trip|trip]]_); **CMD** 40 (42 vs. disarm and _trip_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Acrobatics +23, Diplomacy +26, Intimidate +26, Knowledge (local) +25, Knowledge (planes) +25, Perception +41, Sense Motive +31, Spellcraft +22; **Racial Modifiers** +8 Perception, +4 Sense Motive
**Languages** Abyssal, Celestial, Common; truespeech
**SQ** interrogate

##### Ecology

**Environment** any urban (Axis)
**Organization** solitary, patrol (2–4), squad (5–8), precinct (9–16), or academy (21–40)
**Treasure** double (Large mwk _[[items/Armor/Breastplate|breastplate]]_, Large +1 _axiomatic_ _glaive_, Large +1 _merciful_ _greatclub_, other treasure)

### Special Abilities

**Energized Maul (Su)** As a swift action, an _[[monsters/Axial Monitor|Axial monitor]]_ can add the _axiomatic_, _[[items/Weapon Magic Abilities/Flaming|flaming]]_, frost, _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_, or _[[items/Weapon Magic Abilities/Thundering|thundering]]_ weapon special ability to its slam attack for 1 round, but it cannot add more than one ability at a time.

**Interrogate (Su)** When an _Axial monitor_ questions a creature that is _[[conditions/Helpless|helpless]]_ or _[[conditions/Pinned|pinned]]_, it can compel the creature to answer its questions truthfully unless the creature succeeds at a DC 23 Will save. A creature that fails its save is affected as though subject to _[[spells/Zone of Truth|zone of truth]]_, except that the creature must answer questions if it is able and cannot refuse to answer or answer evasively. A creature that successfully saves cannot be affected by the same _Axial monitor_'s interrogate ability for 24 hours. This is a mind-affecting compulsion effect. The save DC is Charisma-based.

**Tripartite Assault (Ex)** When it makes a full attack, an _Axial monitor_ can choose to make a full attack with one weapon and secondary attacks with its tentacle and slam, or it can choose to make a single attack with each weapon it wields, including its tentacle and slam attacks, with no penalties to its attack rolls for fighting with multiple weapons.

**Watchful Faces (Ex)** An _Axial monitor_ can make three additional attacks of opportunity in a round, one for each head, although it can make no more than a single attack for any given opportunity.

##### Description

The Eternal City of Axis lies at the center of the multiverse, holding the very fabric of reality in some semblance of order through the constant calculations of the _[[monsters/Axiomite|axiomite]]_ Godmind. Yet even a city of order such as Axis, open as it is to visitors from across the planes, must deal with its own internal law and order on a daily basis. The Axial monitors are tasked with preventing disturbances of order and, when crimes do occur, investigating them to bring the perpetrators to justice.

Each _Axial monitor_ has the same unusual form: its large, hairless head bears three faces set equidistantly around it, each expression the picture of bland _[[spells/Serenity|serenity]]_. These faces appear roughly humanoid but are completely smooth, without contours for a brow, nose, or mouth, as though its faces were painted on canvas. The creature’s triangular torso has three shoulders, each with two powerful arms. Two pairs of its arms are humanoid, while the third set is mismatched, with one a long, undulating tentacle and the other an articulated limb of banded iron ending in a maul-like head. Below its waist, the creature’s body divides into a tripod of legs, each ending in a long foot.

Axial monitors only attack those presenting a disturbance to Axis’s order, whether through the commission of a crime or another civil malfeasance. They call for surrender before a fight and prefer to subdue opponents rather than slay them. Their mandate is to bring prisoners into their dispatch stations so they can be examined and interrogated, and the reasons for their disturbance identified and measured in formal reports. These reports are provided directly to the Godmind, which calculates the mathematically ideal method to counteract and prevent any such future disturbances. After incarceration and calculation, an offender is either set free or transferred to one of the city’s rehabilitative prisons under escort by Axial monitors. Although they follow this same process for nearly all creatures, the Axial monitors show no mercy or leniency to proteans and always attack these embodiments of disorder with lethal force on sight.

Axial monitors are 12 feet tall and weigh 1,200 pounds.