---
cssclass: [monsters]
title1: Demon, Shachath
desc_short: This winged abomination is a horrid mix of demonic and angelic features,
  as if two bodies were carelessly fused into one. Its fanged, inhuman face is frozen
  in permanent contempt, while a beautiful visage with an expression of horror bulges
  from the back of its skull.
title2: Shachath
CR: 11
sources:
- name: "Pathfinder #75: Demon's Heresy"
  page: 84
  link: http://paizo.com/products/btpy91dm?Pathfinder-Adventure-Path-75-Demons-Heresy
XP: 12800
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 11
senses:
  all-around vision: true
  darkvision: 60
  detect good: true
AC:
  AC: 25
  touch: 18
  flat_footed: 17
  components:
    dex: 7
    dodge: 1
    natural: 7
HP:
  HP: 148
  long: 11d10+88
saves:
  fort: 11
  ref: 14
  will: 14
DR:
- amount: 10
  weakness: cold iron or good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 22
speeds:
  base: 30
  fly: 50
  fly_maneuverability: average
attacks:
  melee:
  - - text: +1 longsword +19/+14/+9 (1d8+8/19-20)
      entries:
      - - damage: 1d8+8
          crit_range: 19-20
      attack: +1 longsword
      bonus:
      - 19
      - 14
      - 9
    - text: 2 claws +14 (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 2
      attack: claws
      bonus:
      - 14
  special:
  - blasphemous influence
  - lingering doubt
  - merge with host
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: misdirection
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 17
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: telekinesis
    source: default
    freq: At will
    DC: 20
  - name: chaos hammer
    source: default
    freq: 3/day
    DC: 19
  - name: desecrate
    source: default
    freq: 3/day
  - name: greater invisibility
    source: default
    freq: 3/day
  - name: major image
    source: default
    freq: 3/day
    DC: 18
  - name: suggestion
    source: default
    freq: 3/day
    DC: 18
  - name: blasphemy
    source: default
    freq: 1/day
    DC: 22
  - name: scrying
    source: default
    freq: 1/day
    DC: 19
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: succubus
      amount: 1
    - name: incubus
      amount: 1
      chance: 65%
  - name: unhallow
    source: default
    freq: 1/week
    other: only one such effect can be active at a time
  sources:
  - name: default
    CL: 13
    concentration: 18
ability_scores:
  STR: 25
  DEX: 25
  CON: 26
  INT: 18
  WIS: 20
  CHA: 21
BAB: 11
CMB: 18
CMD: 36
feats:
- name: Combat Reflexes
- name: Deceitful
- name: Dodge
- name: Improved Initiative
- name: Iron Will
- name: Weapon Focus (claw)
skills:
  Bluff: 23
  Diplomacy: 19
  Disguise: 14
  Fly: 21
  Knowledge (planes): 16
  Knowledge (religion): 16
  Perception: 27
  Sense Motive: 19
  Sleight of Hand: 18
  Stealth: 21
  Use Magic Device: 19
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Common
- Draconic
- telepathy 100 ft.
special_qualities:
- change shape (Medium or Large humanoid; alter self)
- subtle magic
- trophy taker
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or cabal (1 plus 1-2 succubi and 1-3 incubi)
  treasure_type: standard
  treasure:
  - +1 longsword
  - other treasure
special_abilities:
  Blasphemous Influence (Su): A victim that falls under the effects of a shachath's
    merge with host ability becomes chaotic evil. Divine spellcasters subject to a
    shachath's merge with host ability temporarily lose connection with their faith,
    and now gain their divine powers from the Abyss or a demon lord the shachath serves.
    Though they can still cast the spells they had prepared, they cannot cast spells
    with the lawful or good descriptor. If the victim of a shachath's merging had
    access to the Good domain, that access changes to the Evil domain. If the victim
    had access to the Law domain, that access changes to the Chaos domain. If the
    victim had access to a subdomain associated with the Good or Law domain, that
    subdomain changes to the Demon subdomain. These changes last as long as the shachath
    remains merged with the victim. Other domain choices are not adjusted. If the
    victim is rescued from the shachath's influence and the merge ends without the
    victim's death, the victim remains chaotic evil-this may result in the victim
    losing some or all class abilities. An atonement spell can restore the victim's
    alignment at no additional cost, at which point lost class abilities are restored.
  Lingering Doubt (Su): Once per day, a shachath can use a touch attack to affect
    a creature with lingering doubt. The target must be able to cast divine spells,
    be able to channel positive energy, or have the lay on hands ability. If the target
    fails a DC 20 Will save, all augury, commune, divination, and similar spells cast
    by the target automatically fail. In addition, using divine spells and spell-like
    abilities, channeling positive energy, or using lay on hands has a 20% chance
    of failure. This curse is permanent, but can be removed normally. The target cannot
    detect the curse on itself, but other creatures may detect the curse normally.
    A shachath may use scrying on the cursed creature as if it knew the target well,
    and doing so requires only a full-round action. A shachath may only curse one
    creature at any given time. The save DC is Charisma-based.
  Merge with Host (Su): As a full-round action that provokes an attack of opportunity,
    a shachath can merge its body with that of a helpless creature and control it
    if the victim fails a DC 20 Will save. A creature that successfully saves is not
    subject to the same shachath's merge with host ability for 24 hours. While merged
    with a victim, a shachath gains control of the body and may use it as its own,
    as if it controlled the target via dominate monster. Misdirection or similar effects
    can hide the victim's alignment change. The shachath has full access to all of
    the host's defensive and offensive abilities, and the shachath can still use its
    own spell-like abilities as well. As long as the shachath occupies the host, it
    knows (and can speak) the languages known by the victim and basic information
    about the victim's identity and personality. It can learn specific memories or
    knowledge from the victim by telepathic communication as needed. Damage dealt
    to a host body does not harm the shachath, and if the host body is slain, the
    shachath emerges and is dazed for 1 round. A shachath can choose to abandon a
    host body as an immediate action, but doing so causes the host to be dazed for
    1 round, and the shachath must wait 24 hours before attempting to use merge with
    host again on any target. A shachath can be ejected from a host through the use
    of break enchantment (against CL 13th), dispel chaos, or dispel evil. Merge with
    host is a mind-affecting possession effect. The save DC is Charisma-based.
  Subtle Magic (Su): Whenever a shachath targets a creature with a spell, spell-like
    ability, or supernatural ability, and that spell or ability has no obvious physical
    effects, the targeted creature has no sense of having been the target of a magical
    effect after making a successful saving throw against the effect. If the ability
    requires a touch attack but the target is unaware of being threatened, the shachath
    can attempt an opposed Bluff or Sleight of Hand check to touch the target without
    arousing suspicion or being noticed.
  Trophy Taker (Su): A shachath that takes a personal item from a prospective target
    can wield greater power over that creature. The item must be something that the
    target considers its own possession and carries with it most of the time (for
    example, a piece of jewelry, a favored weapon, a holy symbol, or some other memento).
    The shachath gains a +2 bonus to the saving throw DCs for all of its supernatural
    or spell-like abilities that target the owner of the trophy. This bonus increases
    to +4 if the trophy is the target's holy symbol. A shachath can only have one
    trophy at any time, and it loses any benefit from an existing trophy if it takes
    a new one.
desc_long: A shachath's duplicitous nature is ref lected in its physical form. It
  is literally two-faced, and sees and speaks easily from either side of its skull.
  One face is angelic and the other horrific, but a shachath is a single being of
  pure malevolence. Shachaths are concerned with the destruction of mortal faith in
  anything, and are most often found in the service of Baphomet, Pazuzu, Sif kesh,
  or Socothbenoth. A typical shachath is 7-1/2 feet tall and weighs 320 pounds.

---

# Demon, Shachath
This winged abomination is a horrid mix of demonic and angelic features, as if two bodies were carelessly fused into one. Its fanged, inhuman face is frozen in permanent contempt, while a beautiful visage with an expression of horror bulges from the back of its skull.
**Source** Pathfinder #75: Demon's Heresy pg. 84
**XP** 12,800
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +11; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_; Perception +27

##### Defense

**AC** 25, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+7 Dex, +1 _[[feats/Dodge|dodge]]_, +7 natural)
**hp** 148 (11d10+88)
**Fort** +11, **Ref** +14, **Will** +14
**DR** 10/cold iron or good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 22

##### Offense
**Speed** 30 ft., fly 50 ft. (average)
**Melee** +1 _[[items/Weapon/Longsword|longsword]]_ +19/+14/+9 (1d8+8/19–20), 2 claws +14 (1d4+3)
**Special Attacks** blasphemous influence, lingering doubt, merge with host
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +18)
Constant—_detect good_, _[[spells/Misdirection|misdirection]]_
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), greater teleport (self plus 50 lbs. of objects only), _[[spells/Telekinesis|telekinesis]]_ (DC 20)
3/day—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 19), _[[spells/Desecrate|desecrate]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Major Image|major image]]_ (DC 18), _[[spells/Suggestion|suggestion]]_ (DC 18)
1/day—_[[spells/Blasphemy|blasphemy]]_ (DC 22), _[[spells/Scrying|scrying]]_ (DC 19), _[[universal monster rules/Summon|summon]]_ (level 4, 1 succubus or 1 incubus 65%)
1/week—_[[spells/Unhallow|unhallow]]_ (only one such effect can be active at a time)

##### Statistics
**Str** 25, **Dex** 25, **Con** 26, **Int** 18, **Wis** 20, **Cha** 21
**Base Atk** +11; **CMB** +18; **CMD** 36
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deceitful|Deceitful]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Bluff +23, Diplomacy +19, Disguise +14, Fly +21, Knowledge (planes) +16, Knowledge (religion) +16, Perception +27, Sense Motive +19, Sleight of Hand +18, Stealth +21, Use Magic Device +19; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_Medium_ or Large humanoid; _[[spells/Alter Self|alter self]]_), subtle magic, trophy taker

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or cabal (1 plus 1–2 succubi and 1–3 incubi)
**Treasure** standard (+1 _longsword_, other treasure)

### Special Abilities

**Blasphemous Influence (Su)** A victim that falls under the effects of a shachath’s merge with host ability becomes chaotic evil. Divine spellcasters subject to a shachath’s merge with host ability temporarily lose connection with their faith, and now gain their divine powers from the Abyss or a demon lord the shachath serves. Though they can still cast the spells they had prepared, they cannot cast spells with the lawful or good descriptor. If the victim of a shachath’s _[[items/Armor Magic Abilities/Merging|merging]]_ had access to the Good domain, that access changes to the Evil domain. If the victim had access to the Law domain, that access changes to the Chaos domain. If the victim had access to a subdomain associated with the Good or Law domain, that subdomain changes to the Demon subdomain. These changes last as long as the shachath remains merged with the victim. Other domain choices are not adjusted. If the victim is rescued from the shachath’s influence and the merge ends without the victim’s death, the victim remains chaotic evil—this may result in the victim losing some or all class abilities. An _[[spells/Atonement|atonement]]_ spell can restore the victim’s alignment at no additional cost, at which point lost class abilities are restored.

**Lingering Doubt (Su)** Once per day, a shachath can use a touch attack to affect a creature with lingering doubt. The target must be able to cast divine spells, be able to channel positive energy, or have the lay on hands ability. If the target fails a DC 20 Will save, all _[[spells/Augury|augury]]_, _[[spells/Commune|commune]]_, _[[spells/Divination|divination]]_, and similar spells cast by the target automatically fail. In addition, using divine spells and _spell-like abilities_, _[[items/Armor Magic Abilities/Channeling|channeling]]_ positive energy, or using lay on hands has a 20% chance of failure. This curse is permanent, but can be removed normally. The target cannot detect the curse on itself, but other creatures may detect the curse normally. A shachath may use _scrying_ on the cursed creature as if it knew the target well, and doing so requires only a full-round action. A shachath may only curse one creature at any given time. The save DC is Charisma-based.

**Merge with Host (Su)** As a full-round action that provokes an attack of opportunity, a shachath can merge its body with that of a _[[conditions/Helpless|helpless]]_ creature and control it if the victim fails a DC 20 Will save. A creature that successfully saves is not subject to the same shachath’s merge with host ability for 24 hours. While merged with a victim, a shachath gains control of the body and may use it as its own, as if it controlled the target via _[[spells/Dominate Monster|dominate monster]]_. _Misdirection_ or similar effects can hide the victim’s alignment change. The shachath has full access to all of the host’s defensive and offensive abilities, and the shachath can still use its own _spell-like abilities_ as well. As long as the shachath occupies the host, it knows (and can speak) the languages known by the victim and basic information about the victim’s identity and personality. It can learn specific memories or knowledge from the victim by telepathic communication as needed. Damage dealt to a host body does not _[[spells/Harm|harm]]_ the shachath, and if the host body is slain, the shachath emerges and is _[[conditions/Dazed|dazed]]_ for 1 round. A shachath can choose to abandon a host body as an immediate action, but doing so causes the host to be _dazed_ for 1 round, and the shachath must wait 24 hours before attempting to use merge with host again on any target. A shachath can be ejected from a host through the use of _[[spells/Break Enchantment|break enchantment]]_ (against CL 13th), _[[spells/Dispel Chaos|dispel chaos]]_, or _[[spells/Dispel Evil|dispel evil]]_. Merge with host is a mind-affecting _[[spells/Possession|possession]]_ effect. The save DC is Charisma-based.
**Subtle Magic (Su)** Whenever a shachath targets a creature with a spell, spell-like ability, or supernatural ability, and that spell or ability has no obvious physical effects, the targeted creature has no sense of having been the target of a magical effect after making a successful saving throw against the effect. If the ability requires a touch attack but the target is unaware of being threatened, the shachath can attempt an opposed Bluff or Sleight of Hand check to touch the target without arousing suspicion or being noticed.

**Trophy Taker (Su)** A shachath that takes a personal item from a prospective target can wield greater power over that creature. The item must be something that the target considers its own _possession_ and carries with it most of the time (for example, a piece of _[[items/Mundane/Jewelry|jewelry]]_, a favored weapon, a holy symbol, or some other memento). The shachath gains a +2 bonus to the saving throw DCs for all of its supernatural or _spell-like abilities_ that target the owner of the trophy. This bonus increases to +4 if the trophy is the target’s holy symbol. A shachath can only have one trophy at any time, and it loses any benefit from an existing trophy if it takes a new one.

##### Description

A shachath’s duplicitous nature is ref lected in its physical form. It is literally two-faced, and sees and speaks easily from either side of its skull. One face is angelic and the other horrific, but a shachath is a single being of pure malevolence. Shachaths are concerned with the _[[spells/Destruction|destruction]]_ of mortal faith in anything, and are most often found in the service of Baphomet, Pazuzu, Sif kesh, or Socothbenoth. A typical shachath is 7-1/2 feet tall and weighs 320 pounds.