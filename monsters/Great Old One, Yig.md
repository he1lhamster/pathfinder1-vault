---
cssclass: [monsters]
title1: Great Old One, Yig
desc_short: This green-scaled humanoid has a long, serpentine neck and head, and its
  brow is marked by a distinctive crescent shape.
title2: Yig
CR: 27
sources:
- name: Bestiary 6
  page: 150
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 3276800
alignment: CN
size: Large
type: monstrous humanoid
subtypes:
- chaotic
- Great Old One
- shapechanger
initiative:
  bonus: 25
senses:
  darkvision: 60
  low-light vision: true
  scent: true
auras:
- name: unspeakable presence
  radius: 300
  DC: 35
AC:
  AC: 45
  touch: 30
  flat_footed: 34
  components:
    dex: 11
    insight: 10
    natural: 15
    size: -1
HP:
  HP: 635
  long: 31d10+465
  fast_healing: 20
saves:
  fort: 27
  ref: 28
  will: 28
defensive_abilities:
- freedom of movement
- immortality
- insanity (DC 35)
DR:
- amount: 15
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
- poison
resistances:
  acid: 30
  fire: 30
SR: 38
speeds:
  base: 60
  other_semicolon: air walk
  climb: 60
  swim: 60
attacks:
  melee:
  - - text: bite +44 (6d10+21/19-20 plus poison)
      entries:
      - - damage: 6d10+21
          crit_range: 19-20
        - effect: poison
      attack: bite
      bonus:
      - 44
    - text: 2 claws +44 (4d8+21/19-20)
      entries:
      - - damage: 4d8+21
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 44
    - text: tail slap +44 (4d10+21/19-20 plus grab)
      entries:
      - - damage: 4d10+21
          crit_range: 19-20
        - effect: grab
      attack: tail slap
      bonus:
      - 44
  special:
  - constrict (4d10+21)
  - curse of Yig
  - mythic power (10/day, surge +1d12)
  - rend (2 claws, 4d8+21)
  - serpentine dreams
space: 10
reach: 10
reach_other: 20 ft. with tail slap
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: speak with animals
    source: default
    freq: Constant
    other: reptiles only
  - name: awaken
    source: default
    freq: At will
    other: snakes only
  - is_mythic_spell: true
    name: baleful polymorph
    source: default
    freq: At will
    DC: 25
    other: into harmless snakes only
  - name: commune with nature
    source: default
    freq: At will
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
  - is_mythic_spell: true
    name: nightmare
    source: default
    freq: At will
    DC: 25
  - name: transport via plants
    source: default
    freq: At will
  - name: demand
    source: default
    freq: 3/day
  - name: quickened feeblemind
    source: default
    freq: 3/day
    DC: 25
  - is_mythic_spell: true
    name: heal
    source: default
    freq: 3/day
  - name: quickened poison
    source: default
    freq: 3/day
    DC: 24
  - is_mythic_spell: true
    name: control weather
    source: default
    freq: 1/day
  - name: symbol of persuasion
    source: default
    freq: 1/day
    DC: 26
  - name: true resurrection
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 27
    concentration: 37
ability_scores:
  STR: 38
  DEX: 33
  CON: 41
  INT: 30
  WIS: 33
  CHA: 30
BAB: 31
CMB: 46
CMB_other: +50 sunder
CMD: 77
CMD_other: 79 vs. sunder
feats:
- name: Bleeding Critical
- name: Combat Reflexes
- name: Critical Focus
- name: Great Fortitude
- name: Greater Sunder
- name: Greater Vital Strike
- name: Improved Critical (bite)
- name: Improved Critical (claw)
- name: Improved Critical (tail slap)
- name: Improved Initiative
- name: Improved Sunder
- name: Improved Vital Strike
- name: Power Attack
- name: Quicken Spell-Like Ability (feeblemind)
- name: Quicken Spell-Like Ability (poison)
- name: Vital Strike
skills:
  Acrobatics: 42
  Climb: 56
  Handle Animal: 41
  Heal: 42
  Intimidate: 44
  Knowledge (nature): 41
  Knowledge (religion): 41
  Perception: 45
  Sense Motive: 42
  Spellcraft: 41
  Stealth: 41
  Survival: 45
  Swim: 56
  Use Magic Device: 41
languages:
- Aklo
- Common
- Draconic
- Undercommon
- speak with animals (reptiles only)
- telepathy 100 ft.
special_qualities:
- change shape (any serpentine form; shapechange)
- devastating
- otherworldly insight
ecology:
  environment: any
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Curse of Yig (Su): Once per round as a free action when he touches or damages a
    creature with any natural attack, Yig can target that creature with a potent curse.
    The target must succeed at a DC 35 Will save or it takes a -6 penalty on all saving
    throws against poison effects and loses the ability to recover from poison effects
    naturally (though magical effects that remove poison effects still work). The
    cursed creature cannot gain the benefit of immunity to poison, be it from a class
    or racial ability, a magic item, or any other source. As long as it suffers under
    the curse of Yig, the victim becomes staggered for 1d6 rounds whenever it fails
    a saving throw against a mind-affecting or poison effect, and any offspring sired
    or birthed are deformed in some hideous (but mostly cosmetic) fashion. This is
    a curse effect. The save DC is Charisma-based.
  Devastating (Ex): All of Yig's natural attacks are primary attacks that add 1-1/2
    × his Strength modifier to their damage. Yig ignores hardness less than 20 for
    any object he strikes.
  Immortality (Ex): If Yig is slain, his body decays as normal, but he does not stay
    dead for long. He is reborn 3 months after his death, hatching from the egg of
    a venomous serpent (although not necessarily on the same planet on which his previous
    incarnation was slain). He spends a year in the form of a venomous (but otherwise
    normal) snake, after which he sheds his skin and emerges once again as Yig. Typically,
    Yig does not hold grudges against those who slew him, but this is not always the
    case.
  Poison (Ex): Bite-injury; save Fort DC 40; frequency 1/ round for 6 rounds; effect
    1d6 Constitution drain plus nauseated for 1 round; cure 3 consecutive saves. The
    save DC is Constitution-based.
  Serpentine Dreams (Su): Any creature that has ever willfully harmed a snake, has
    suffered the effects of the curse of Yig (see above), or has slain one of Yig's
    clerics can be targeted by the Great Old One's serpentine dreams, regardless of
    the distance between the creature and Yig-even across planar boundaries. In order
    to use serpentine dreams against a target, Yig must first successfully affect
    the target with his nightmare spell-like ability. If the victim fails its save
    against nightmare, it must succeed at a DC 35 Will save or take 2d6 points of
    Intelligence drain in addition to the normal effects of nightmare. When this Intelligence
    drain would reduce the victim's Intelligence score below 2, the victim is instead
    transformed (as if via baleful polymorph) into a Tiny venomous snake. This is
    a mind-affecting polymorph effect. The save DC is Charisma-based.
  Unspeakable Presence (Ex): Failing a DC 35 Will save against Yig's unspeakable presence
    causes the victim to become more susceptible to curse effects. The victim takes
    a -6 penalty on all saving throws against curse effects, and the effective DC
    to remove a curse from such a victim increases by 6. A creature normally immune
    to curses that is affected by Yig's unspeakable presence can now be affected by
    curses (but takes no further penalty against curses as a result of the Great Old
    One's unspeakable presence). This effect lasts for 1 year or until removed by
    a miracle or wish. If a creature suffering from this effect dies and is brought
    back to life, there is a 50% chance the effect persists upon the creature's restoration
    to life.
desc_long: |-
  Of all the Great Old Ones, Yig is without a doubt the most benign. Yet those so foolish as to expect kindness from the so-called Father of Serpents would do well to think again, for Yig does not suffer fools and is as likely to devour those who beseech him for help as he is to provide aid. Even his most devout worshipers realize he may simply wish to feed at times, and on these occasions no amount of devotion can protect a supplicant from death. 

  Yig appears as a scaled, humanoid creature with a serpent's head and lashing tail, but he can appear as any serpentine creature if he so wills. In his true form, Yig stands 14 feet tall and weighs 1,100 pounds.

---

# Great Old One, Yig
This green-scaled humanoid has a long, serpentine neck and head, and its brow is marked by a distinctive crescent shape.
**Source** Bestiary 6 pg. 150
**XP** 3,276,800

CN Large monstrous humanoid (chaotic, Great Old One, shapechanger)
**Init** +25; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[universal monster rules/Scent|scent]]_; Perception +45
**Aura** unspeakable presence (300 ft., DC 35)

##### Defense

**AC** 45, touch 30, _[[conditions/Flat-Footed|flat-footed]]_ 34 (+11 Dex, +10 insight, +15 natural, –1 size)
**hp** 635 (31d10+465); _[[universal monster rules/Fast Healing|fast healing]]_ 20
**Fort** +27, **Ref** +28, **Will** +28
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, immortality, _[[spells/Insanity|insanity]]_ (DC 35); **DR** 15/epic and lawful; **Immune** ability damage, ability drain, aging, cold, death effects, disease, _[[universal monster rules/Energy Drain|energy drain]]_, mind-affecting effects, _[[universal monster rules/Paralysis|paralysis]]_, petrification, poison; **Resist** acid 30, fire 30; **SR** 38

##### Offense
**Speed** 60 ft., _[[universal monster rules/Climb|climb]]_ 60 ft., swim 60 ft.; _[[spells/Air Walk|air walk]]_
**Melee** bite +44 (6d10+21/19–20 plus poison), 2 claws +44 (4d8+21/19–20), tail slap +44 (4d10+21/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft. (20 ft. with tail slap)
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (4d10+21), curse of Yig, mythic power (10/day, surge +1d12), _[[universal monster rules/Rend|rend]]_ (2 claws, 4d8+21), serpentine dreams
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 27th; concentration +37)
Constant—_air walk_, _freedom of movement_, _[[spells/Speak with Animals|speak with animals]]_ (reptiles only) 
At will—_[[spells/Awaken|awaken]]_ (snakes only), _[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 25, into harmless snakes only), _[[spells/Commune with Nature|commune with nature]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Dream|dream]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Nightmare|nightmare]]_ (DC 25), _[[spells/Transport via Plants|transport via plants]]_ 
3/day—_[[spells/Demand|demand]]_, quickened _[[spells/Feeblemind|feeblemind]]_ (DC 25), _[[spells/Heal|heal]]_, quickened poison (DC 24) 
1/day—_[[spells/Control Weather|control weather]]_, _[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 26), _[[spells/True Resurrection|true resurrection]]_ 
**M** mythic spell

##### Statistics
**Str** 38, **Dex** 33, **Con** 41, **Int** 30, **Wis** 33, **Cha** 30
**Base Atk** +31; **CMB** +46 (+50 sunder); **CMD** 77 (79 vs. sunder)
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Sunder|Greater Sunder]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite, claw, tail slap), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_feeblemind_, poison), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +42, _Climb_ +56, Handle Animal +41, _Heal_ +42, Intimidate +44, Knowledge (nature, religion) +41, Perception +45, Sense Motive +42, Spellcraft +41, Stealth +41, Survival +45, Swim +56, Use Magic Device +41
**Languages** Aklo, Common, Draconic, Undercommon; _speak with animals_ (reptiles only); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any serpentine form; _[[spells/Shapechange|shapechange]]_), devastating, otherworldly insight

##### Ecology

**Environment** any
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Curse of Yig (Su)** Once per round as a free action when he touches or damages a creature with any natural attack, Yig can target that creature with a _[[items/Weapon Magic Abilities/Potent|potent]]_ curse. The target must succeed at a DC 35 Will save or it takes a –6 penalty on all saving throws against poison effects and loses the ability to recover from poison effects naturally (though magical effects that remove poison effects still work). The cursed creature cannot gain the benefit of _[[universal monster rules/Immunity|immunity]]_ to poison, be it from a class or racial ability, a magic item, or any other source. As long as it suffers under the curse of Yig, the victim becomes _[[conditions/Staggered|staggered]]_ for 1d6 rounds whenever it fails a saving throw against a mind-affecting or poison effect, and any offspring sired or birthed are deformed in some hideous (but mostly cosmetic) fashion. This is a curse effect. The save DC is Charisma-based.

**Devastating (Ex)** All of Yig’s _[[universal monster rules/Natural Attacks|natural attacks]]_ are primary attacks that add 1-1/2 × his Strength modifier to their damage. Yig ignores hardness less than 20 for any object he strikes.

**Immortality (Ex)** If Yig is slain, his body decays as normal, but he does not stay dead for long. He is reborn 3 months after his death, hatching from the egg of a venomous serpent (although not necessarily on the same planet on which his previous incarnation was slain). He spends a year in the form of a venomous (but otherwise normal) snake, after which he sheds his skin and emerges once again as Yig. Typically, Yig does not hold grudges against those who slew him, but this is not always the case.

**Poison (Ex)** Bite—injury; save Fort DC 40; frequency 1/ round for 6 rounds; effect 1d6 Constitution drain plus _[[conditions/Nauseated|nauseated]]_ for 1 round; cure 3 consecutive saves. The save DC is Constitution-based.
**Serpentine Dreams (Su)** Any creature that has ever willfully harmed a snake, has suffered the effects of the curse of Yig (see above), or has slain one of Yig’s clerics can be targeted by the Great Old One’s serpentine dreams, regardless of the distance between the creature and Yig—even across _[[items/Weapon Magic Abilities/Planar|planar]]_ boundaries. In order to use serpentine dreams against a target, Yig must first successfully affect the target with his _nightmare_ spell-like ability. If the victim fails its save against _nightmare_, it must succeed at a DC 35 Will save or take 2d6 points of Intelligence drain in addition to the normal effects of _nightmare_. When this Intelligence drain would reduce the victim’s Intelligence score below 2, the victim is instead transformed (as if via _baleful polymorph_) into a Tiny venomous snake. This is a mind-affecting _[[spells/Polymorph|polymorph]]_ effect. The save DC is Charisma-based.

**Unspeakable Presence (Ex)** Failing a DC 35 Will save against Yig’s unspeakable presence causes the victim to become more susceptible to curse effects. The victim takes a –6 penalty on all saving throws against curse effects, and the effective DC to remove a curse from such a victim increases by 6. A creature normally immune to curses that is affected by Yig’s unspeakable presence can now be affected by curses (but takes no further penalty against curses as a result of the Great Old One’s unspeakable presence). This effect lasts for 1 year or until removed by a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_. If a creature suffering from this effect dies and is brought back to life, there is a 50% chance the effect persists upon the creature’s _[[spells/Restoration|restoration]]_ to life.

##### Description

Of all the Great Old Ones, Yig is without a doubt the most benign. Yet those so foolish as to expect kindness from the so-called Father of Serpents would do well to think again, for Yig does not suffer fools and is as likely to devour those who beseech him for help as he is to provide aid. Even his most devout worshipers realize he may simply _wish_ to feed at times, and on these occasions no amount of devotion can protect a supplicant from death.

Yig appears as a scaled, humanoid creature with a serpent’s head and _[[feats/Lashing Tail|lashing tail]]_, but he can appear as any serpentine creature if he so wills. In his _[[spells/True Form|true form]]_, Yig stands 14 feet tall and weighs 1,100 pounds.