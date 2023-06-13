---
cssclass: [monsters]
title1: Great Old One, Mhar
desc_short: Eight pairs of crystalline legs support this enormous volcano. The volcano's
  crater constantly spews smoke and roiling lava.
title2: Mhar
CR: 26
sources:
- name: 'Pathfinder #138: Rise of New Thassilon'
  page: 86
  link: https://paizo.com/products/btq01w1w
XP: 2457600
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
  blindsight: 120
  darkvision: 60
  tremorsense: 600
auras:
- name: cloak of ash
  radius: 30
- name: unspeakable presence
  radius: 300
  DC: 35
AC:
  AC: 43
  touch: 13
  flat_footed: 42
  components:
    dex: 1
    insight: 10
    natural: 30
    size: -8
HP:
  HP: 592
  long: 32d8+448
  regeneration: 20
  regeneration_weakness: electricity, see below
saves:
  fort: 24
  ref: 13
  will: 28
defensive_abilities:
- earthen regeneration
- insanity (DC 35)
DR:
- amount: 15
  weakness: epic and good
immunities:
- ability damage
- ability drain
- aging
- cold
- death effects
- disease
- energy drain
- fire
- mind-affecting effects
- paralysis
- petrification
- plane shift
resistances:
  acid: 30
  electricity: 30
  sonic: 10
SR: 37
speeds:
  base: 40
  burrow: 120
attacks:
  melee:
  - - text: 4 claws +33 (4d12+16/19-20 plus 2d6 fire)
      entries:
      - - damage: 4d12+16
          crit_range: 19-20
        - damage: 2d6
          type: fire
      count: 4
      attack: claws
      bonus:
      - 33
  special:
  - mythic power (10/day, surge +1d12)
  - taphophobic dreams
  - volcanic tempest
space: 50
reach: 50
spell_like_abilities:
  entries:
  - is_mythic_spell: true
    name: dimension door
    source: default
    freq: At will
  - is_mythic_spell: true
    name: dream
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: insanity
    source: default
    freq: At will
    DC: 26
  - name: mindwipe
    source: default
    freq: At will
    DC: 23
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
    DC: 24
  - name: synesthesia
    source: default
    freq: At will
    DC: 22
  - name: wall of fire
    source: default
    freq: At will
  - name: wall of stone
    source: default
    freq: At will
  - name: demand
    source: default
    freq: 3/day
    DC: 27
  - name: earthquake
    source: default
    freq: 3/day
    DC: 27
  - name: quickened feeblemind
    source: default
    freq: 3/day
    DC: 24
  - name: meteor swarm
    source: default
    freq: 1/day
    DC: 28
  - name: microcosm
    source: default
    freq: 1/day
    DC: 28
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 27
  sources:
  - name: default
    CL: 32
    concentration: 41
ability_scores:
  STR: 42
  DEX: 13
  CON: 38
  INT: 28
  WIS: 31
  CHA: 29
BAB: 24
CMB: 48
CMB_other: +52 bull rush
CMD: 69
CMD_other: 71 vs. bull rush, can't be tripped
feats:
- name: Awesome Blow
- name: Combat Reflexes
- name: Critical Focus
- name: Greater Bull Rush
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Critical (claw)
- name: Improved Initiative
- name: Improved Lightning Reflexes
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell-Like Ability (feeblemind)
- name: Stunning Critical
- name: Vital Strike
- name: Weapon Focus (claw)
skills:
  Climb: 51
  Intimidate: 44
  Knowledge (arcana): 41
  Knowledge (geography): 41
  Knowledge (history): 41
  Knowledge (local): 41
  Knowledge (nature): 41
  Knowledge (planes): 41
  Perception: 45
  Sense Motive: 42
  Stealth: 20
  Survival: 45
  Swim: 51
languages:
- Aklo
- Ignan
- Terran
- telepathy (100 ft.)
special_qualities:
- massive
- otherworldly insight
ecology:
  environment: any land
  organization: solitary (unique)
  treasure_type: double
special_abilities:
  Cloak of Ash (Ex): A blanketing layer of swirling ash surrounds Mhar's bulk, obscuring
    the vision of anyone who draws too close. All creatures within the area have concealment.
    A strong wind (21+ mph) disperses the ash after 1 round. The ash returns immediately
    once the strong wind ends.
  Earthen Regeneration (Ex): Mhar's regeneration functions only while it is burrowing,
    submerged in lava, or otherwise underground. The regeneration continues for 1
    minute after it emerges aboveground. If Mhar's regeneration is stopped, the regeneration
    automatically resumes when Mhar burrows or enters lava.
  Immortality (Ex): If Mhar is slain, it explodes violently, spraying earth and lava
    in all directions. Creatures within 30 feet of Mhar take 30d6 points of bludgeoning
    damage and 30d6 points of fire damage. A creature can attempt a DC 40 Reflex save
    for half damage. Mhar manifests again 1 year later in the same area, restored
    to life via true resurrection.
  Massive (Ex): Due to Mhar's tremendous size, it treats uneven ground and other terrain
    features that form difficult terrain as normal terrain, though areas of forest
    or significant settlements are still considered difficult terrain to Mhar. A Huge
    or smaller creature can move through any square occupied by Mhar, and vice versa.
    Mhar can make attacks of opportunity only against foes that are Huge or larger,
    and can be flanked only by Huge or larger foes. Mhar gains a bonus for being on
    higher ground only if its entire space is on higher ground than that of its target.
    It's possible for a Huge or smaller creature to climb Mhar-this generally requires
    a successful DC 30 Climb check, and unlike the normal rules regarding Mhar and
    attacks of opportunity, a Small or larger creature that climbs on its body provokes
    an attack of opportunity from Mhar. Any creature that climbs on Mhar is treated
    as if it is totally immersed in lava.
  Taphophobic Dreams (Su): When Mhar uses its nightmare spell-like ability on a creature
    within 5 feet of earth or worked stone, it also afflicts that creature with terrifying
    dreams of an immense presence surging through the ground, ominously circling the
    target and threatening to pull it under. In addition to the effects of nightmare,
    the target must also succeed at a DC 35 Will save or be unwilling to approach
    within 5 feet of any amount of earth or stone and, if within such an area, compelled
    to leave it immediately. The creature is profoundly uncomfortable in such an area,
    reducing its Dexterity score to 1. This is a mind-affecting curse effect. The
    save DC is Charisma-based.
  Unspeakable Presence (Su): Failing a DC 35 Will save against Mhar's unspeakable
    presence causes the victim to experience the crushing entombment of earth and
    lose the ability to breathe as long as it remains within the area of effect. The
    save DC is Charisma-based.
  Volcanic Tempest (Ex): Once every 1d6 rounds, Mhar can spew a torrential rain of
    lava, fire, and caustic ash as a full-round action. All creatures within 60 feet
    of Mhar take 8d6 points of bludgeoning damage and 8d6 points of fire damage (DC
    40 Reflex half). In addition, the ground within 60 feet of Mhar when it uses this
    ability becomes covered in a thin layer of lava. Any creature that ends its turn
    within this lava takes 20d6 points of fire damage. The lava cools after 1 minute.
    Finally, the area within 60 feet of Mhar when it uses this ability fills with
    deadly ash that functions as stinking cloud (Fortitude DC 40 negates). This ash
    disperses naturally after 1 minute. The save DCs are Constitution-based.
desc_long: |-
  Mhar is a Great Old One that was born eons ago on the edge of the Material Plane. A unique planar rift caused pure essence from the Plane of Earth and Plane of Fire to collide and fuse together, coalescing into a being that lived in a state of constant anguish-a mass of volcanic eruptions that cooled and melted away in a cycle that caused it unending pain. Seeking relief from its torment but unable to escape the Material Plane, Mhar alleviated its suffering by traveling the stars.

   Mhar found nascent planets that were still made of roiling magma. For a time, Mhar could rest in the core of these planets, but even such primordial heat could not keep Mhar sedated. Mhar would eventually awaken, destroying the planet and departing to find another haven elsewhere. After destroying countless worlds, Mhar learned a way to escape to the Elemental Plane of Fire. Unfortunately for Mhar, this required greater power than it currently had. Mhar found another young planet-the world called Golarion-burrowed deep into its core, and waited to grow.

   While Mhar rested, the goddess Sarenrae tore open a portion of the Material Plane to seal Rovagug within the Dead Vault. Unbeknownst to her, she slew Mhar in that process, granting it the reprieve from pain it had always sought. However, even oblivion could not quell Mhar's suffering, and its agony was enough to stir it from death. When Mhar awakened yet again, trapped within the crust of Golarion, it went mad, unable to escape its own torment. Mhar let out a psychic scream. As this scream rebounded and echoed between the crust and Mhar itself, intensifying the creature's madness, the mental force of it pushed against the surface of the earth and formed the Kodar Mountains.

   Mhar seeks to break free from beneath Golarion's crust and destroy the world, then use the magma as a focus to open a breach to the Plane of Fire and flood the entire Material Plane with lava. Once all of reality is a mass of fire and destruction, Mhar can finally find peace.

---

# Great Old One, Mhar
Eight pairs of crystalline legs support this enormous volcano. The volcano’s crater constantly spews smoke and roiling lava.
**Source** Pathfinder #138: Rise of New Thassilon pg. 86
**XP** 2,457,600
CE Colossal aberration (chaotic, evil, Great Old One)
**Init** +15; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 120 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Tremorsense|tremorsense]]_ 600 ft.; Perception +45
**Aura** cloak of ash (30 ft.), unspeakable presence (300 ft., DC 35)

##### Defense

**AC** 43, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 42 (+1 Dex, +10 insight, +30 natural, –8 size)
**hp** 592 (32d8+448); _[[universal monster rules/Regeneration|regeneration]]_ 20 (electricity, see below)
**Fort** +24, **Ref** +13, **Will** +28
**Defensive Abilities** earthen _regeneration_, _[[spells/Insanity|insanity]]_ (DC 35); **DR** 15/epic and good; **Immune** ability damage, ability drain, aging, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, fire, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, petrification, _[[spells/Plane Shift|plane shift]]_; **Resist** acid 30, electricity 30, sonic 10; **SR** 37

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 120 ft.
**Melee** 4 claws +33 (4d12+16/19–20 plus 2d6 fire)
**Space** 50 ft., **Reach** 50 ft.
**Special Attacks** mythic power (10/day, surge +1d12), taphophobic dreams, _[[items/Armor Magic Abilities/Volcanic|volcanic]]_ tempest
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 32nd; concentration +41)
At will—_[[spells/Dimension Door|dimension door]]_, _[[spells/Dream|dream]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _insanity_ (DC 26), _[[spells/Mindwipe|mindwipe]]_ (DC 23), _[[spells/Nightmare|nightmare]]_ (DC 24), _[[spells/Synesthesia|synesthesia]]_ (DC 22), _[[spells/Wall Of Fire|wall of fire]]_, _[[spells/Wall Of Stone|wall of stone]]_ 
3/day—_[[spells/Demand|demand]]_ (DC 27), _[[spells/Earthquake|earthquake]]_ (DC 27), quickened _[[spells/Feeblemind|feeblemind]]_ (DC 24) 
1/day—_[[spells/Meteor Swarm|meteor swarm]]_ (DC 28), _[[spells/Microcosm|microcosm]]_ (DC 28), _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 27)

##### Statistics
**Str** 42, **Dex** 13, **Con** 38, **Int** 28, **Wis** 31, **Cha** 29
**Base Atk** +24; **CMB** +48 (+52 bull rush); **CMD** 69 (71 vs. bull rush, can't be tripped)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Bull Rush|Greater Bull Rush]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_feeblemind_), _[[feats/Stunning Critical|Stunning Critical]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** _[[universal monster rules/Climb|Climb]]_ +51, Intimidate +44, Knowledge (arcana, geography, history, local, nature, planes) +41, Perception +45, Sense Motive +42, Stealth +20, Survival +45, Swim +51
**Languages** Aklo, Ignan, Terran; _[[universal monster rules/Telepathy|telepathy]]_ (100 ft.)
**SQ** massive, otherworldly insight

##### Ecology

**Environment** any land
**Organization** solitary (unique)
**Treasure** double

### Special Abilities

**Cloak of Ash (Ex)** A blanketing layer of swirling ash surrounds Mhar’s bulk, obscuring the _[[spells/Vision|vision]]_ of anyone who draws too close. All creatures within the area have concealment. A strong wind (21+ mph) disperses the ash after 1 round. The ash returns immediately once the strong wind ends.

**Earthen _Regeneration_ (Ex)** Mhar’s _regeneration_ functions only while it is burrowing, submerged in lava, or otherwise underground. The _regeneration_ continues for 1 minute after it emerges aboveground. If Mhar’s _regeneration_ is stopped, the _regeneration_ automatically resumes when Mhar burrows or enters lava.

**Immortality (Ex)** If Mhar is slain, it explodes violently, spraying earth and lava in all directions. Creatures within 30 feet of Mhar take 30d6 points of bludgeoning damage and 30d6 points of fire damage. A creature can attempt a DC 40 Reflex save for half damage. Mhar manifests again 1 year later in the same area, restored to life via _[[spells/True Resurrection|true resurrection]]_.

**Massive (Ex)** Due to Mhar’s tremendous size, it treats uneven ground and other terrain features that form difficult terrain as normal terrain, though areas of forest or significant settlements are still considered difficult terrain to Mhar. A Huge or smaller creature can move through any square occupied by Mhar, and vice versa. Mhar can make attacks of opportunity only against foes that are Huge or larger, and can be flanked only by Huge or larger foes. Mhar gains a bonus for being on higher ground only if its entire space is on higher ground than that of its target. It’s possible for a Huge or smaller creature to _climb_ Mhar—this generally requires a successful DC 30 _Climb_ check, and unlike the normal rules regarding Mhar and attacks of opportunity, a Small or larger creature that climbs on its body provokes an attack of opportunity from Mhar. Any creature that climbs on Mhar is treated as if it is totally immersed in lava.

**Taphophobic Dreams (Su)** When Mhar uses its _nightmare_ spell-like ability on a creature within 5 feet of earth or worked stone, it also afflicts that creature with terrifying dreams of an immense presence surging through the ground, ominously circling the target and threatening to _[[universal monster rules/Pull|pull]]_ it under. In addition to the effects of _nightmare_, the target must also succeed at a DC 35 Will save or be unwilling to approach within 5 feet of any amount of earth or stone and, if within such an area, compelled to leave it immediately. The creature is profoundly uncomfortable in such an area, reducing its Dexterity score to 1. This is a mind-affecting curse effect. The save DC is Charisma-based.

**Unspeakable Presence (Su)** Failing a DC 35 Will save against Mhar’s unspeakable presence causes the victim to experience the crushing entombment of earth and lose the ability to breathe as long as it remains within the area of effect. The save DC is Charisma-based.

**_Volcanic_ Tempest (Ex)** Once every 1d6 rounds, Mhar can spew a torrential rain of lava, fire, and caustic ash as a full-round action. All creatures within 60 feet of Mhar take 8d6 points of bludgeoning damage and 8d6 points of fire damage (DC 40 Reflex half). In addition, the ground within 60 feet of Mhar when it uses this ability becomes covered in a thin layer of lava. Any creature that ends its turn within this lava takes 20d6 points of fire damage. The lava cools after 1 minute. Finally, the area within 60 feet of Mhar when it uses this ability fills with _[[items/Weapon Magic Abilities/Deadly|deadly]]_ ash that functions as _[[spells/Stinking Cloud|stinking cloud]]_ (Fortitude DC 40 negates). This ash disperses naturally after 1 minute. The save DCs are Constitution-based.

##### Description

Mhar is a Great Old One that was born eons ago on the edge of the Material Plane. A unique _[[items/Weapon Magic Abilities/Planar|planar]]_ rift caused pure essence from the Plane of Earth and Plane of Fire to collide and fuse together, coalescing into a being that lived in a state of constant anguish—a mass of _volcanic_ eruptions that cooled and melted away in a cycle that caused it unending pain. Seeking relief from its torment but unable to escape the Material Plane, Mhar alleviated its suffering by traveling the stars.

Mhar found nascent planets that were still made of roiling magma. For a time, Mhar could rest in the core of these planets, but even such primordial _[[universal monster rules/Heat|heat]]_ could not keep Mhar sedated. Mhar would eventually _[[spells/Awaken|awaken]]_, destroying the planet and departing to find another haven elsewhere. After destroying countless worlds, Mhar learned a way to escape to the Elemental Plane of Fire. Unfortunately for Mhar, this required greater power than it currently had. Mhar found another young planet—the world _[[items/Weapon Magic Abilities/Called|called]]_ Golarion—burrowed deep into its core, and waited to grow.

While Mhar rested, the goddess Sarenrae tore open a portion of the Material Plane to seal Rovagug within the Dead Vault. Unbeknownst to her, she slew Mhar in that process, granting it the reprieve from pain it had always sought. However, even _[[monsters/Oblivion|oblivion]]_ could not quell Mhar’s suffering, and its agony was enough to stir it from death. When Mhar awakened yet again, trapped within the crust of Golarion, it went mad, unable to escape its own torment. Mhar let out a _[[classes/Psychic|psychic]]_ scream. As this scream rebounded and echoed between the crust and Mhar itself, intensifying the creature’s madness, the mental force of it pushed against the surface of the earth and formed the Kodar Mountains.

Mhar seeks to break free from beneath Golarion’s crust and destroy the world, then use the magma as a focus to open a breach to the Plane of Fire and flood the entire Material Plane with lava. Once all of reality is a mass of fire and _[[spells/Destruction|destruction]]_, Mhar can finally find peace.