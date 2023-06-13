---
cssclass: [monsters]
title1: Titan, Hekatonkheires
desc_short: This behemoth looks like a towering humanoid with fifty heads and twice
  as many hands, each wielding a different weapon.
title2: Hekatonkheires
CR: 24
sources:
- name: Bestiary 3
  page: 268
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
XP: 1228800
alignment: CE
size: Colossal
type: outsider
subtypes:
- chaotic
- evil
- extraplanar
initiative:
  bonus: 6
senses:
  all-around vision: true
  darkvision: 120
  true seeing: true
AC:
  AC: 42
  touch: 4
  flat_footed: 40
  components:
    armor: 8
    dex: 2
    natural: 30
    size: -8
HP:
  HP: 516
  long: 24d10+384
  regeneration: 10
  regeneration_weakness: epic
saves:
  fort: 30
  ref: 12
  will: 18
defensive_abilities:
- spell turning
DR:
- amount: 20
  weakness: epic and lawful
immunities:
- aging
- death effects
- disease
- mind-affecting effects
SR: 35
speeds:
  base: 60
  other_semicolon: air walk
attacks:
  melee:
  - - text: +3 weapon +38/+33/+28/+23 (6d6+22 plus hundred-handed whirlwind)
      entries:
      - - damage: 6d6+22
        - effect: hundred-handed whirlwind
      attack: +3 weapon
      bonus:
      - 38
      - 33
      - 28
      - 23
  - - text: slam +35 (4d8+28 plus stun)
      entries:
      - - damage: 4d8+28
        - effect: stun
      attack: slam
      bonus:
      - 35
  ranged:
  - - text: rock +22/+17/+12/+7 (8d8+31/18-20)
      entries:
      - - damage: 8d8+31
          crit_range: 18-20
      attack: rock
      bonus:
      - 22
      - 17
      - 12
      - 7
  special:
  - rock throwing (200 ft.)
  - stunning slam
space: 30
reach: 30
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: spell turning
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: bestow curse
    source: default
    freq: At will
    DC: 21
  - name: break enchantment
    source: default
    freq: At will
  - name: chain lightning
    source: default
    freq: At will
    DC: 23
  - name: greater dispel magic
    source: default
    freq: At will
  - name: find the path
    source: default
    freq: At will
  - name: sending
    source: default
    freq: At will
  - name: greater scrying
    source: default
    freq: 3/day
    DC: 24
  - name: heal
    source: default
    freq: 3/day
  - name: mass suggestion
    source: default
    freq: 3/day
    DC: 23
  - name: dominate monster
    source: default
    freq: 1/day
    DC: 26
  - name: greater spell immunity
    source: default
    freq: 1/day
  - name: imprisonment
    source: default
    freq: 1/day
    DC: 26
  - name: storm of vengeance
    source: default
    freq: 1/day
    DC: 26
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 48
  DEX: 15
  CON: 43
  INT: 22
  WIS: 19
  CHA: 24
BAB: 24
CMB: 51
CMD: 71
feats:
- name: Alertness
- name: Cleave
- name: Combat Expertise
- name: Critical Focus
- name: Great Cleave
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Initiative
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Power Attack
- name: Vital Strike
skills:
  Acrobatics: 29
    when jumping: 41
  Bluff: 34
  Climb: 46
  Craft (any): 33
  Diplomacy: 31
  Escape Artist: 29
  Intimidate: 34
  Knowledge (history): 30
  Knowledge (planes): 33
  Perception: 35
  Sense Motive: 35
  Survival: 28
languages:
- Abyssal
- Celestial
- Common
- telepathy 300 ft.
special_qualities:
- hands of war
- planar leap
ecology:
  environment: any
  organization: solitary
  treasure_type: triple
  treasure:
  - 50-100 various weapons
  - other treasure
special_abilities:
  Hands of War (Su): Any weapon a hekatonkheires wields gains a +3 enhancement bonus
    while the titan holds it. A hekatonkheires's attacks are treated as epic and evil
    for the purposes of overcoming damage reduction. In addition, a hekatonkheires's
    multitude of arms allows it to effectively block attacks, granting it a +8 armor
    bonus to its AC.
  Hundred-Handed Whirlwind (Ex): A hekatonkheires carries several dozen weapons of
    various types in its hundred hands, but when it attacks in melee, you don't have
    to resolve each of these as a separate attack. Instead, when the titan attacks
    with its weapons, it rolls its attacks normally (either one attack for a standard
    action, or four as a full-round action) and hits every creature in its reach each
    time an attack roll exceeds that creature's AC. If any such attack roll results
    in a possible critical hit, the critical is applied to one creature of the hekatonkheires's
    choosing. The hekatonkheires can choose to deal bludgeoning, piercing, or slashing
    damage as a free action on each separate hit.
  Planar Leap (Su): A hekatonkheires traverses the planes by physically smashing through
    planar boundaries and crashing devastatingly into the target plane itself. Once
    per year as a full-round action, a hekatonkheires can, as part of a jump, plane
    shift to any other plane (as per the spell of the same name). It can only bring
    itself and its gear when it travels in this manner. When the hekatonkheires reaches
    its destination plane, it falls from the sky and crashes to the ground, creating
    a devastating explosion of thunder and fire. Any creature within 300 feet of the
    point where the hekatonkheires lands (including the titan itself) takes 20d6 points
    of bludgeoning damage and 20d6 points of sonic damage (Reflex DC 38 for half).
    The save DC is Constitution-based.
  Stunning Slam (Ex): As a standard action, a hekatonkheires may forgo any weapon
    attacks to make a single slam attack against any creature in reach. If it hits,
    the target takes damage and must succeed at a DC 41 Fortitude save to avoid being
    stunned for 1d6 rounds. The save DC is Strength-based.
desc_long: |-
  Horrifying abominations shunned by the gods immediately upon their creation, the hekatonkheires are perhaps the most powerful and devastating race of titans in existence. When the titans-envious of the gods' divine strength-rebelled against the deities, the hekatonkheires were among the first to pick up arms, weary of the scorn their own creators felt for them. The betrayal of the Elysian titans led to the hekatonkheires' swift capture by the gods, who found the hekatonkheires' power to be so immense that they were not banished to the Abyss with their Thanatotic brethren. Instead, the gods cast the hekatonkheires into the furthest reaches of the multiverse they could find. There, the hekatonkheires drifted in expanses of nothingness for unknown eons, and the madness wrought upon them by isolation destroyed their memories. Yet from their madness these shattered monstrosities spawned progeny to replace them in their pursuit to destroy, and some of these monstrous offspring discovered ways to break through planar boundaries and wander the multiverse freely.

  The gods initially created only three hekatonkheires, seeking to make the ultimate warriors in order to guard the gates to the Abyss. These three ancient titans still drift in the unknown expanses between planes-the hekatonkheires that now walk the worlds are their lesser spawn. But these so-called “lesser” titans remain almost unimaginably powerful themselves. They have no knowledge of why their forgotten ancestors were originally banished, and so they wander in search of answers, all the while destroying entire worlds. They are warped engines of mayhem, their existence based wholly on the devastation of life and anything that might remind them of their age-old war against the gods, having inherited only the haunting ghosts of such memories from their ancestors.

  Those hekatonkheires who have emerged back into the multiverse have done so in different realms, and to date, no record of any two of these spawn meeting one another exists. It is fortunate that only one hekatonkheires is encountered on a world at any given time, as even scholars cannot fathom the power that would arise out of two or more of the titans' collective strength. They traverse the planes alone, caring not for allies of any sort until they can remember what their purpose was when they were born eons ago.

  Though hekatonkheires are as intelligent as the rest of their titan relatives, they wander with such destructive and seemingly mindless intentions that they spare no time in communicating with other creatures, especially those that would beg for mercy. The hekatonkheires were created to destroy, and so that is all they desire to do; the crushing blows of their fists and the goring slashes of their weapons speak for themselves. They serve no master, and halt their otherwise endless rampage only if called by their true names, which few-if any-mortals know. Those that do know these names speak them only in whispers, for their mere utterance seems to carry with it immeasurable power.

  A hekatonkheires can only be called via mighty spells such as gate if a conjurer knows the plane the titan is currently on, and only if the conjurer knows the true name of the hekatonkheires it is seeking to call. Only the mad or depraved would dare such a feat, however, as the might of one of these unique goliaths is so massive that the being cannot be controlled, and even if it is banished back to the realm from whence it came, it is never long before the hekatonkheires sets its sights on the world it visited so briefly, if only to sate its lust for destroying it.

  Each hekatonkheires has 50 heads and 100 arms so that one is never caught off guard. The stones that it hurls with its 100 hands are as big as boulders, and those who have seen a hekatonkheires hurl such rocks and lived to tell the tale have said that it is as though an entire mountain is falling from the sky. In addition to their unworldly strength, hekatonkheires are known for their awesome control over the powers of lightning and thunder, and an individual hekatonkheires's arrival is often prefaced by an abrupt and tumultuous storm in the area. Like all titans, hekatonkheires are immortal, and do not die unless they are slain.

  A hekatonkheires is 50 feet tall and weighs 25 tons.

---

# Titan, Hekatonkheires
This behemoth looks like a towering humanoid with fifty heads and twice as many hands, each wielding a different weapon.
**Source** Bestiary 3 pg. 268
**XP** 1,228,800
CE Colossal outsider (chaotic, evil, extraplanar)
**Init** +6; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 120 ft., _[[spells/True Seeing|true seeing]]_; Perception +35

##### Defense

**AC** 42, touch 4, _[[conditions/Flat-Footed|flat-footed]]_ 40 (+8 armor, +2 Dex, +30 natural, –8 size)
**hp** 516 (24d10+384); _[[universal monster rules/Regeneration|regeneration]]_ 10 (epic)
**Fort** +30, **Ref** +12, **Will** +18
**Defensive Abilities** _[[spells/Spell Turning|spell turning]]_; **DR** 20/epic and lawful; **Immune** aging, death effects, disease, mind-affecting effects; **SR** 35

##### Offense
**Speed** 60 ft.; _[[spells/Air Walk|air walk]]_
**Melee** +3 weapon +38/+33/+28/+23 (6d6+22 plus hundred-handed _[[universal monster rules/Whirlwind|whirlwind]]_) or slam +35 (4d8+28 plus stun)
**Ranged** rock +22/+17/+12/+7 (8d8+31/18–20)
**Space** 30 ft., **Reach** 30 ft.
**Special Attacks** _[[universal monster rules/Rock Throwing|rock throwing]]_ (200 ft.), stunning slam
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant—_air walk_, _spell turning_, _true seeing_
At will—_[[spells/Bestow Curse|bestow curse]]_ (DC 21), _[[spells/Break Enchantment|break enchantment]]_, _[[spells/Chain Lightning|chain lightning]]_ (DC 23), greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Find the Path|find the path]]_, _[[spells/Sending|sending]]_
3/day—greater _[[spells/Scrying|scrying]]_ (DC 24), _[[spells/Heal, Mass|heal, mass]]_ _[[spells/Suggestion|suggestion]]_ (DC 23)
1/day—_[[spells/Dominate Monster|dominate monster]]_ (DC 26), greater _[[spells/Spell Immunity|spell immunity]]_, _[[spells/Imprisonment|imprisonment]]_ (DC 26), _[[spells/Storm Of Vengeance|storm of vengeance]]_ (DC 26)

##### Statistics
**Str** 48, **Dex** 15, **Con** 43, **Int** 22, **Wis** 19, **Cha** 24
**Base Atk** +24; **CMB** +51; **CMD** 71
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +29 (+41 when jumping), Bluff +34, _[[universal monster rules/Climb|Climb]]_ +46, Craft (any) +33, Diplomacy +31, Escape Artist +29, Intimidate +34, Knowledge (history) +30, Knowledge (planes) +33, Perception +35, Sense Motive +35, Survival +28
**Languages** Abyssal, Celestial, Common; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** hands of war, _[[items/Weapon Magic Abilities/Planar|planar]]_ leap

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** triple (50–100 various weapons, other treasure)

### Special Abilities

**Hands of War (Su)** Any weapon a hekatonkheires wields gains a +3 enhancement bonus while the titan holds it. A hekatonkheires’s attacks are treated as epic and evil for the purposes of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_. In addition, a hekatonkheires’s multitude of arms allows it to effectively block attacks, granting it a +8 armor bonus to its AC.

**Hundred-Handed _Whirlwind_ (Ex)** A hekatonkheires carries several dozen weapons of various types in its hundred hands, but when it attacks in melee, you don’t have to resolve each of these as a separate attack. Instead, when the titan attacks with its weapons, it rolls its attacks normally (either one attack for a standard action, or four as a full-round action) and hits every creature in its reach each time an attack roll exceeds that creature’s AC. If any such attack roll results in a possible critical hit, the critical is applied to one creature of the hekatonkheires’s choosing. The hekatonkheires can choose to deal bludgeoning, piercing, or slashing damage as a free action on each separate hit.

**_Planar_ Leap (Su)** A hekatonkheires traverses the planes by physically _[[items/Weapon Magic Abilities/Smashing|smashing]]_ through _planar_ boundaries and crashing devastatingly into the target plane itself. Once per year as a full-round action, a hekatonkheires can, as part of a _[[spells/Jump|jump]]_, _[[spells/Plane Shift|plane shift]]_ to any other plane (as per the spell of the same name). It can only bring itself and its gear when it travels in this manner. When the hekatonkheires reaches its destination plane, it falls from the sky and crashes to the ground, creating a devastating explosion of thunder and fire. Any creature within 300 feet of the point where the hekatonkheires lands (including the titan itself) takes 20d6 points of bludgeoning damage and 20d6 points of sonic damage (Reflex DC 38 for half). The save DC is Constitution-based.
**Stunning Slam (Ex)** As a standard action, a hekatonkheires may forgo any weapon attacks to make a single slam attack against any creature in reach. If it hits, the target takes damage and must succeed at a DC 41 Fortitude save to avoid being _[[conditions/Stunned|stunned]]_ for 1d6 rounds. The save DC is Strength-based.

##### Description

Horrifying abominations shunned by the gods immediately upon their creation, the hekatonkheires are perhaps the most powerful and devastating race of titans in existence. When the titans—envious of the gods’ divine strength—rebelled against the deities, the hekatonkheires were among the first to pick up arms, weary of the scorn their own creators felt for them. The betrayal of the Elysian titans led to the hekatonkheires’ swift capture by the gods, who found the hekatonkheires’ power to be so immense that they were not banished to the Abyss with their Thanatotic brethren. Instead, the gods cast the hekatonkheires into the furthest reaches of the multiverse they could find. There, the hekatonkheires drifted in expanses of nothingness for _[[monsters/Unknown|unknown]]_ eons, and the madness wrought upon them by isolation destroyed their memories. Yet from their madness these shattered monstrosities spawned progeny to replace them in their pursuit to destroy, and some of these monstrous offspring discovered ways to break through _planar_ boundaries and wander the multiverse freely.

The gods initially created only three hekatonkheires, seeking to make the ultimate warriors in order to _[[npcs/Guard|guard]]_ the gates to the Abyss. These three ancient titans still drift in the _unknown_ expanses between planes—the hekatonkheires that now walk the worlds are their lesser spawn. But these so-called “lesser” titans remain almost unimaginably powerful themselves. They have no knowledge of why their forgotten ancestors were originally banished, and so they wander in search of answers, all the while destroying entire worlds. They are warped engines of mayhem, their existence based wholly on the devastation of life and anything that might remind them of their age-old war against the gods, having inherited only the haunting ghosts of such memories from their ancestors.

Those hekatonkheires who have emerged back into the multiverse have done so in different realms, and to date, no record of any two of these spawn meeting one another exists. It is fortunate that only one hekatonkheires is encountered on a world at any given time, as even scholars cannot fathom the power that would arise out of two or more of the titans’ collective strength. They traverse the planes alone, caring not for allies of any sort until they can remember what their purpose was when they were born eons ago.

Though hekatonkheires are as intelligent as the rest of their titan relatives, they wander with such destructive and seemingly mindless intentions that they spare no time in communicating with other creatures, especially those that would beg for mercy. The hekatonkheires were created to destroy, and so that is all they desire to do; the crushing blows of their fists and the goring slashes of their weapons speak for themselves. They serve no master, and halt their otherwise endless rampage only if _[[items/Weapon Magic Abilities/Called|called]]_ by their true names, which few—if any—mortals know. Those that do know these names speak them only in whispers, for their mere utterance seems to carry with it immeasurable power.

A hekatonkheires can only be _called_ via mighty spells such as _[[spells/Gate|gate]]_ if a conjurer knows the plane the titan is currently on, and only if the conjurer knows the _[[feats/True Name|true name]]_ of the hekatonkheires it is seeking to call. Only the mad or depraved would dare such a feat, however, as the might of one of these unique goliaths is so massive that the being cannot be controlled, and even if it is banished back to the realm from whence it came, it is never long before the hekatonkheires sets its sights on the world it visited so briefly, if only to sate its lust for destroying it.

Each hekatonkheires has 50 heads and 100 arms so that one is never caught off _guard_. The stones that it hurls with its 100 hands are as big as boulders, and those who have seen a hekatonkheires hurl such rocks and lived to tell the tale have said that it is as though an entire mountain is falling from the sky. In addition to their unworldly strength, hekatonkheires are known for their awesome control over the powers of lightning and thunder, and an individual hekatonkheires’s arrival is often prefaced by an abrupt and tumultuous storm in the area. Like all titans, hekatonkheires are immortal, and do not die unless they are slain.

A hekatonkheires is 50 feet tall and weighs 25 tons.