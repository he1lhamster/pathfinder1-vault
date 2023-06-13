---
cssclass: [monsters]
title1: Edimmu
is_3.5: true
desc_short: A flickering ghostly form soaring upon a front of roiling storm clouds,
  its skeletal torso lies cloaked in tattered wrappings. Powerful winds seem to lash
  about the spectre, and malevolent embers flare within its eye sockets as its claw-like
  fingerbones reach forth.
title2: Edimmu
CR: 3
sources:
- name: 'Pathfinder #20: House of the Beast'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/legacyOfFire/v5748btpy86xw
alignment: CE
size: Medium
type: undead
subtypes:
- incorporeal
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 15
  touch: 15
  flat_footed: 12
  components:
    deflection: 2
    dex: 3
HP:
  HP: 32
  long: 5d12
saves:
  fort: 1
  ref: 3
  will: 5
speeds:
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: frigid touch +5 (1d6 cold)
      entries:
      - - damage: 1d6
          type: cold
      attack: frigid touch
      bonus:
      - 5
  special:
  - frigid touch
  - life-implosion
  - moan
  - storm mastery
spell_like_abilities:
  entries:
  - name: fog cloud
    source: default
    freq: At will
  - name: silent image
    source: default
    freq: At will
    DC: 13
  - name: unseen servant
    source: default
    freq: At will
  - name: whispering wind
    source: default
    freq: At will
  sources:
  - name: default
    CL: 6
ability_scores:
  STR:
  DEX: 17
  CON:
  INT: 13
  WIS: 15
  CHA: 15
BAB: 2
grapple_3.5: 2
feats:
- name: Improved Initiative
- name: Lightning Reflexes
skills:
  Hide: 11
  Intimidation: 10
  Knowledge (history): 9
  Listen: 10
  Spot: 10
languages:
- Auran
- Qadiran
special_qualities:
- incorporeal
- rejuvenation
ecology:
  environment: any desert
  organization: solitary or clan (2-12)
  treasure_type: standard
  advancement_3.5:
  - type: size
    HD_min: 6
    size: Medium
    HD_max: 12
special_abilities:
  Frigid Touch (Su): An edimmu's frigid touch deals 1d6 points of cold damage.
  Life Implosion (Su): Once an edimmu reaches 0 hit points it collapses upon itself,
    imploding with a final shriek that rips the life force from nearby creatures.
    Any living being within 20 feet of the edimmu at the time of its destruction must
    succeed a DC 14 Fortitude save or take 1d4 points of Constitution damage. The
    save is Charisma-based.
  Moan (Su): An edimmu's sorrowful moans force every living creature within 30 feet
    to make a DC 14 Will save to avoid becoming shaken. This is a sonic mind-affecting
    fear effect. Whether or not the save is successful, an affected creature is immune
    to the same ediummu's moan for 24 hours. The save is Charisma-based.
  Rejuvenation (Su): Upon an edimmu's destruction, the magics that bind it to the
    mortal world linger on. Thus, 1d4+1 days after an edimmu's destruction, the creature
    reforms with full hit points. The only way to destroy an edimmu is with an atonement
    spell. The atonement absolves the creature of its sins and sorrows, allowing it
    to finally return to its native plane.
  Storm Mastery (Su): Once per day, an edimmu can spend a fullround action to control
    the winds within 50 feet of it. It may change the speed and strength of the wind
    within this area, raising wind force to as strong as severe (see page 95 of the
    DMG for details on wind effects). It may control such winds for up to 1 minute,
    but can perform no other action while doing so. At the end of this minute, or
    when the edimmu takes another action, the force of the winds reduces by one level
    of strength per round until returning to normal.
  Weaknesses: If dismissal is cast upon an edimmu, it is immediately destroyed without
    its life implosion ability taking effect.
desc_long: |-
  Edimmus rise from the corpses of slain genies unable to return to their elemental homelands. Whether through powerful magics or as part of bargains made with mortal spellcasters, genies occasionally find themselves tied to the Material Plane for a specific term or until they complete a set task. As the conditions of some such magics remain binding even in death, genies that perish before the terms of their service are fulfilled sometimes manifest as creatures of uncontrolled fury. Even in their undead state, these genies still possess a measure of their mastery over the elements, using their powers to seek revenge upon those who led them to be trapped to their horrifying forms.

  Edimmus are ghostly, with ancient-looking, hunched skeletal frames that make them appear shorter than their average 6-foot heights.

---

# Edimmu
A flickering ghostly form soaring upon a front of roiling storm clouds, its skeletal torso lies cloaked in tattered wrappings. Powerful winds seem to lash about the _[[monsters/Spectre|spectre]]_, and _[[items/Armor Magic Abilities/Malevolent|malevolent]]_ embers _[[spells/Flare|flare]]_ within its eye sockets as its claw-like fingerbones reach forth.
**Source** Pathfinder #20: House of the Beast pg. 82
CE Medium undead (_[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Listen +10, Spot +10

##### Defense

**AC** 15, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 _[[spells/Deflection|deflection]]_, +3 Dex)
**hp** 32 (5d12)
**Fort** +1, **Ref** +3, **Will** +5

##### Offense
**Speed** fly 60 ft. (perfect)
**Melee** _[[spells/Frigid Touch|frigid touch]]_ +5 (1d6 cold)
**Special Attacks** _frigid touch_, life-implosion, moan, storm mastery
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th)
At will - _[[spells/Fog Cloud|fog cloud]]_, _[[spells/Silent Image|silent image]]_ (DC 13), _[[spells/Unseen Servant|unseen servant]]_, _[[spells/Whispering Wind|whispering wind]]_

##### Statistics
**Str** —, **Dex** 17, **Con** —, **Int** 13, **Wis** 15, **Cha** 15
**Base Atk** +2; **Grapple** +2
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Hide +11, Intimidate +10, Knowledge (history) +9, Listen +10, Spot +10
**Languages** Auran, Qadiran
**SQ** _incorporeal_, rejuvenation

##### Ecology

**Environment** any desert
**Organization** solitary or clan (2-12)
**Treasure** standard
**Advancement** 6-12 HD (_Medium_)

### Special Abilities

**_Frigid Touch_ (Su)** An _[[monsters/Edimmu|edimmu]]_’s _frigid touch_ deals 1d6 points of cold damage.

**Life _[[spells/Implosion|Implosion]]_ (Su)** Once an _edimmu_ reaches 0 hit points it collapses upon itself, imploding with a final shriek that rips the life force from nearby creatures. Any living being within 20 feet of the _edimmu_ at the time of its _[[spells/Destruction|destruction]]_ must succeed a DC 14 Fortitude save or take 1d4 points of Constitution damage. The save is Charisma-based.

**Moan (Su)** An _edimmu_’s sorrowful moans force every living creature within 30 feet to make a DC 14 Will save to avoid becoming _[[conditions/Shaken|shaken]]_. This is a sonic mind-affecting _[[universal monster rules/Fear|fear]]_ effect. Whether or not the save is successful, an affected creature is immune to the same ediummu’s moan for 24 hours. The save is Charisma-based.

**Rejuvenation (Su)** Upon an _edimmu_’s _destruction_, the magics that bind it to the mortal world linger on. Thus, 1d4+1 days after an _edimmu_’s _destruction_, the creature reforms with full hit points. The only way to destroy an _edimmu_ is with an _[[spells/Atonement|atonement]]_ spell. The _atonement_ absolves the creature of its sins and sorrows, allowing it to finally return to its native plane.
**Storm Mastery (Su)** Once per day, an _edimmu_ can spend a fullround action to control the winds within 50 feet of it. It may change the speed and strength of the wind within this area, raising wind force to as strong as severe (see page 95 of the DMG for details on wind effects). It may control such winds for up to 1 minute, but can perform no other action while doing so. At the end of this minute, or when the _edimmu_ takes another action, the force of the winds reduces by one level of strength per round until returning to normal.

**Weaknesses** If _[[spells/Dismissal|dismissal]]_ is cast upon an _edimmu_, it is immediately destroyed without its life _implosion_ ability taking effect.

##### Description

Edimmus rise from the corpses of slain genies unable to return to their elemental homelands. Whether through powerful magics or as part of bargains made with mortal spellcasters, genies occasionally find themselves tied to the Material Plane for a specific term or until they complete a set task. As the conditions of some such magics remain _[[spells/Binding|binding]]_ even in death, genies that perish before the terms of their service are fulfilled sometimes manifest as creatures of uncontrolled fury. Even in their undead state, these genies still possess a measure of their mastery over the elements, using their powers to seek revenge upon those who led them to be trapped to their horrifying forms.

Edimmus are ghostly, with ancient-looking, hunched skeletal frames that make them appear shorter than their average 6-foot heights.