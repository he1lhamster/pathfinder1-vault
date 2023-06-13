---
cssclass: [monsters]
title1: Devil, Apostate Devil (Deimavigga)
desc_short: A grim metal mask floats above ceremonial armor that shifts and writhes,
  and long blades form fingers on gauntleted hands.
title2: Apostate Devil (Deimavigga)
CR: 17
sources:
- name: Bestiary 5
  page: 78
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
- name: 'Book of the Damned - Volume 1: Princes of Darkness'
  page: 54
  link: http://paizo.com/store/downloads/pathfinder/pathfinderChronicles/pathfinderRPG/v5748btpy8a6f
XP: 102400
alignment: LE
size: Medium
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 14
senses:
  darkvision: 60
  see in darkness: true
AC:
  AC: 46
  touch: 20
  flat_footed: 36
  components:
    armor: 14
    dex: 10
    natural: 12
HP:
  HP: 261
  long: 18d10+162
  regeneration: 5
saves:
  fort: 20
  ref: 16
  will: 20
DR:
- amount: 10
  weakness: good and silver
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 27
speeds:
  base: 30
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 claws +28 (1d8+9/19-20 plus 1d6 Wisdom drain)
      entries:
      - - damage: 1d8+9
          crit_range: 19-20
        - damage: 1d6
          type: Wisdom drain
      count: 2
      attack: claws
      bonus:
      - 28
  special:
  - boundless reach
  - ohrwurm
space: 5
reach: 10
spell_like_abilities:
  entries:
  - name: alter self
    source: default
    freq: At will
  - name: dream
    source: default
    freq: At will
    DC: 24
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: major image
    source: default
    freq: At will
    DC: 22
  - name: mirage arcana
    source: default
    freq: At will
    DC: 24
  - name: ventriloquism
    source: default
    freq: At will
    DC: 19
  - name: blasphemy
    source: default
    freq: 3/day
    DC: 26
  - name: dominate person
    source: default
    freq: 3/day
    DC: 24
  - name: hold monster
    source: default
    freq: 3/day
    DC: 24
  - name: insanity
    source: default
    freq: 3/day
    DC: 26
  - name: touch of idiocy
    source: default
    freq: 3/day
  - name: veil
    source: default
    freq: 3/day
    DC: 25
  - name: mind fog
    source: default
    freq: 1/day
    DC: 24
  - name: screen
    source: default
    freq: 1/day
    DC: 27
  - name: summon
    source: default
    freq: 1/day
    level: 8
    summons:
    - name: bone devils
      amount: 1d6
    - name: bearded devils
      amount: 2d4
      chance: 50%
    - name: ice devil
      amount: 1
      chance: 20%
  sources:
  - name: default
    CL: 18
    concentration: 27
ability_scores:
  STR: 28
  DEX: 31
  CON: 28
  INT: 21
  WIS: 24
  CHA: 28
BAB: 18
CMB: 28
CMD: 47
feats:
- name: Agile Maneuvers
- name: Combat Expertise
- name: Combat Reflexes
- name: Improved Critical (claw)
- name: Improved Disarm
- name: Improved Initiative
- name: Iron Will
- name: Persuasive
- name: Weapon Focus (claw)
skills:
  Acrobatics: 28
  Bluff: 30
  Diplomacy: 34
  Disguise: 27
  Fly: 18
  Intimidate: 34
  Knowledge (history): 26
  Knowledge (planes): 26
  Knowledge (religion): 26
  Perception: 28
  Sense Motive: 28
  Stealth: 36
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Infernal
- indomitable oration
- telepathy 100 ft.
special_qualities:
- armor bond
- evangelization
- indomitable oration
- malleable form
ecology:
  environment: any (Hell)
  organization: solitary
  treasure_type: double
  treasure:
  - +5 shadow full plate
  - other treasure
special_abilities:
  Armor Bond (Ex): A deimavigga's armor is as much a part of its body as a second
    skin. A deimavigga ignores its armor's speed reduction, max Dex bonus, and armor
    check penalty.
  Boundless Reach (Su): A deimavigga's claws slice through reality, allowing it to
    make melee attacks against any creature it is aware of-typically meaning creatures
    within 100 feet. The devil still only threatens the 10-foot area around it and
    cannot make attacks of opportunity against creatures farther away. This ability
    can span vast distances, allowing a deimavigga making use of divination magic
    to detect distant creatures and attack foes separated by miles or even planes.
    Spells like forbiddance, which prevent planar travel, protect against a deimavigga's
    claws. The spell dimensional anchor also prevents a deimavigga from using this
    ability for the duration of that spell. An attacked creature can retaliate until
    the beginning of the deimavigga's next turn, striking at the devil's claws with
    weapons or spells as if it were physically present, but the deimavigga's claws
    receive a size bonus to AC as if they were two sizes smaller than the deimavigga,
    and the attacked creature cannot grapple or otherwise prevent the claws from vanishing
    out of reach at the end of the round.
  Evangelization (Su): 'The words of deimaviggas are poison to the mind. Every round
    a deimavigga speaks (a free action), all non-devils with an Intelligence score
    of 3 or higher within 30 feet must make a DC 28 Will save or become vulnerable
    to its blasphemous discourse. The DC of this Will save increases by 1 for each
    consecutive round a creature has listened to the same deimavigga speak. Creatures
    must be listening to a deimavigga to be affected by its oration. Deafened creatures
    and those in combat-either with the deimavigga or with other creatures-are not
    considered to be listening. Victims cannot simply declare they are not listening
    without taking steps to impede their hearing. Upon failing this save, a victim
    can be affected by the heretical power of a deimavigga's words. The devil may
    use its speech to affect a listener in ways that mimic any of the following spells:
    calm emotions (DC 21), charm monster (DC 23), command (DC 20), confusion (DC 23),
    crushing despair (DC 23), deep slumber (DC 22), enthrall (DC 21), modify memory
    (DC 23), rage (DC 22), or suggestion (DC 22). Victims still receive saving throws
    against these spell effects, but if they fail their saves they are not aware the
    devil is working its power upon them. A deimavigga can affect multiple victims
    with different spell effects in the same round. This is a sonic mind-affecting
    effect. The base save DC is Charisma-based.'
  Indomitable Oration (Su): A deimavigga's speech is always perfectly clear and cannot
    be silenced or warped. Even in areas of incredible noise, through water or airless
    voids, or in areas of magical silence, these devils' voices can still be heard
    normally. All beings understand deimaviggas, as if these devils constantly spoke
    in all tongues at once.
  Malleable Form (Su): A deimavigga has complete control over its physical form, and
    if transformed into another shape against its will, it can revert to its own form
    as a free action.
  Ohrwurm (Su): As a standard action, three times per day, a deimavigga can whisper
    a fundamental and terrifying multiversal truth to one creature within 5 feet.
    The target must make a DC 28 Will save or have the devil's words take root in
    its psyche. Outsiders and elementals have a +2 bonus on their saves to resist
    this ability. Initially, the deimavigga's words seem to have no effect. Any time
    the victim tries to rest, though, he must make an additional DC 28 Will save or
    be affected as per the spell nightmare (even if the victim doesn't technically
    sleep). After a night of suffering vivid dreams and wrestling with the devil's
    words, the victim must make yet another DC 28 Will save or have its alignment
    shift one step toward lawful evil. Only by unlearning what the deimavigga told
    it can a victim be free of this effect, requiring a spell such as miracle, modify
    memory, or wish.
  Wisdom Drain (Su): A deimavigga drains 1d6 points of Wisdom each time it hits with
    its claw attack. (A deimavigga does not heal any damage when it uses its Wisdom
    drain.)
desc_long: |-
  Regal, fearsome, and unfeeling, deimaviggas seek to turn the faithful from their gods, using cold logic to proselytize the path of atheism, the freedom of the mortal spirit, and the order offered by Hell. Their ever-shifting masks speak envenomed words and give their hollow lies the ring of truth. Speaking out against all deities-except for Asmodeus, whom they subtly tout as a bringer of discipline even as they downplay his divinity-these deadly intellectuals know that those who turn from their deities are more likely to succumb to the temptations of diabolism. Rather than attempting to sway the souls of individual mortals, these cunning fiends take on the roles of prophets of reason, disguising themselves beneath layers of illusion to evangelize the virtues and freedoms of lives unshackled by the demands of egotistical deities. Occasionally one might focus its arguments on a soul of particular piety, delighting in throwing a deity's most devoted servant into an inescapable crisis of faith. Deimaviggas care little for what gods their depredations affect, disenfranchising the worshipers of the pure and the profane alike.

  In their natural shapes, deimaviggas stand 7 feet tall and weigh a mere 120 pounds. When disguised, though, they typically take the forms of wise elders who have lived long enough to understand fundamental truths about the universe, priests who have "realized their folly" and rejected their former dogma, or even "angels" of truth. Though they prefer to fight with words rather than with physical means, deimaviggas attack those who attempt to strip away their disguises and illusions, or who can argue as eloquently as they-though if possible, they prefer to do so discreetly and dispose of the bodies secretly.

  Deimaviggas prefer to spend most of their time upon the Material Plane, swaying the weak and corruptible souls of mortals.There they seek out either vast mortal cities, where their heresy might reach many ears, or small communities where the isolated might fall to their blasphemous philosophizing. When in Hell, though, they linger in Caina, tormenting the souls of those trapped upon its lonely islands, developing and testing complicated and often confusing arguments.

  Preferring to operate alone, these poison-tongued devils rarely work with others of their kind, even though their status affords them control over their lesser brethren. They find that their arguments benefit from a single voice, and that their endeavors are complicated by even the most obedient minions. They bow to Hell's hierarchy, however, and serve if compelled to do so. Pit fiends and infernal dukes sometimes utilize deimaviggas as personal majordomos, spies, and spreaders of dissension, though even among devilkind these enigmatic fiends are considered particularly unnerving.

---

# Devil, Apostate Devil (Deimavigga)
A grim metal _[[items/Mundane/Mask|mask]]_ floats above ceremonial armor that shifts and writhes, and long blades form fingers on gauntleted hands.
**Source** Bestiary 5 pg. 78, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ - Volume 1: Princes of _[[spells/Darkness|Darkness]]_ pg. 54
**XP** 102,400

LE Medium outsider (devil, evil, extraplanar, lawful)
**Init** +14; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +28

##### Defense

**AC** 46, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 36 (+14 armor, +10 Dex, +12 natural)
**hp** 261 (18d10+162); _[[universal monster rules/Regeneration|regeneration]]_ 5
**Fort** +20, **Ref** +16, **Will** +20
**DR** 10/good and silver; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 27

##### Offense
**Speed** 30 ft., fly 60 ft. (perfect)
**Melee** 2 claws +28 (1d8+9/19-20 plus 1d6 Wisdom drain)
**Space** 5 ft., **Reach** 10 ft.
**Special Attacks** boundless reach, ohrwurm
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +27)
At will—_[[spells/Alter Self|alter self]]_, _[[spells/Dream|dream]]_ (DC 24), greater teleport (self plus 50 lbs. of objects only), _[[spells/Major Image|major image]]_ (DC 22), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 24), _[[spells/Ventriloquism|ventriloquism]]_ (DC 19) 
3/day—_[[spells/Blasphemy|blasphemy]]_ (DC 26), _[[spells/Dominate Person|dominate person]]_ (DC 24), _[[spells/Hold Monster|hold monster]]_ (DC 24), _[[spells/Insanity|insanity]]_ (DC 26), _[[spells/Touch of Idiocy|touch of idiocy]]_, _[[spells/Veil|veil]]_ (DC 25) 
1/day—_[[spells/Mind Fog|mind fog]]_ (DC 24), screen (DC 27), _[[universal monster rules/Summon|summon]]_ (level 8, 1d6 bone devils or 2d4 bearded devils 50% or 1 ice devil 20%)

##### Statistics
**Str** 28, **Dex** 31, **Con** 28, **Int** 21, **Wis** 24, **Cha** 28
**Base Atk** +18; **CMB** +28; **CMD** 47
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Acrobatics +28, Bluff +30, Diplomacy +34, Disguise +27, Fly +18, Intimidate +34, Knowledge (history, planes, religion) +26, Perception +28, Sense Motive +28, Stealth +36
**Languages** Abyssal, Celestial, Common, Draconic, Infernal; indomitable oration, _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** armor bond, evangelization, indomitable oration, _[[feats/Malleable Form|malleable form]]_

##### Ecology

**Environment** any (Hell)
**Organization** solitary
**Treasure** double (+5 _[[items/Armor Magic Abilities/Shadow|shadow]]_ _[[items/Armor/Full plate|full plate]]_, other treasure)

### Special Abilities

**Armor Bond (Ex)** A deimavigga’s armor is as much a part of its body as a second skin. A deimavigga ignores its armor’s speed reduction, max Dex bonus, and armor check penalty.

**Boundless Reach (Su)** A deimavigga’s claws slice through reality, allowing it to make melee attacks against any creature it is aware of—typically meaning creatures within 100 feet. The devil still only threatens the 10-foot area around it and cannot make attacks of opportunity against creatures farther away. This ability can span vast distances, allowing a deimavigga making use of _[[spells/Divination|divination]]_ magic to detect distant creatures and attack foes separated by miles or even planes. Spells like _[[spells/Forbiddance|forbiddance]]_, which prevent _[[items/Weapon Magic Abilities/Planar|planar]]_ travel, protect against a deimavigga’s claws. The spell _[[spells/Dimensional Anchor|dimensional anchor]]_ also prevents a deimavigga from using this ability for the duration of that spell. An attacked creature can retaliate until the beginning of the deimavigga’s next turn, striking at the devil’s claws with weapons or spells as if it were physically present, but the deimavigga’s claws receive a size bonus to AC as if they were two sizes smaller than the deimavigga, and the attacked creature cannot grapple or otherwise prevent the claws from vanishing out of reach at the end of the round.

**Evangelization (Su)** The words of deimaviggas are poison to the mind. Every round a deimavigga speaks (a free action), all non-devils with an Intelligence score of 3 or higher within 30 feet must make a DC 28 Will save or become vulnerable to its blasphemous discourse. The DC of this Will save increases by 1 for each consecutive round a creature has listened to the same deimavigga speak. Creatures must be listening to a deimavigga to be affected by its oration. _[[conditions/Deafened|Deafened]]_ creatures and those in combat—either with the deimavigga or with other creatures—are not considered to be listening. Victims cannot simply declare they are not listening without taking steps to impede their hearing. Upon failing this save, a victim can be affected by the _[[items/Weapon Magic Abilities/Heretical|heretical]]_ power of a deimavigga’s words. The devil may use its speech to affect a listener in ways that _[[monsters/Mimic|mimic]]_ any of the following spells: _[[spells/Calm Emotions|calm emotions]]_ (DC 21), _[[spells/Charm Monster|charm monster]]_ (DC 23), _[[spells/Command|command]]_ (DC 20), _[[spells/Confusion|confusion]]_ (DC 23), _[[spells/Crushing Despair|crushing despair]]_ (DC 23), _[[spells/Deep Slumber|deep slumber]]_ (DC 22), _[[spells/Enthrall|enthrall]]_ (DC 21), _[[spells/Modify Memory|modify memory]]_ (DC 23), _[[spells/Rage|rage]]_ (DC 22), or _[[spells/Suggestion|suggestion]]_ (DC 22). Victims still receive saving throws against these spell effects, but if they fail their saves they are not aware the devil is working its power upon them. A deimavigga can affect multiple victims with different spell effects in the same round. This is a sonic mind-affecting effect. The base save DC is Charisma-based.

**Indomitable Oration (Su)** A deimavigga’s speech is always perfectly clear and cannot be silenced or warped. Even in areas of incredible noise, through water or airless voids, or in areas of magical _[[spells/Silence|silence]]_, these devils’ voices can still be heard normally. All beings understand deimaviggas, as if these devils constantly spoke in all _[[spells/Tongues|tongues]]_ at once.

**_Malleable Form_ (Su)** A deimavigga has complete control over its physical form, and if transformed into another shape against its will, it can revert to its own form as a free action.

**Ohrwurm (Su)** As a standard action, three times per day, a deimavigga can whisper a fundamental and terrifying multiversal truth to one creature within 5 feet. The target must make a DC 28 Will save or have the devil’s words take _[[spells/Root|root]]_ in its psyche. Outsiders and elementals have a +2 bonus on their saves to resist this ability. Initially, the deimavigga’s words seem to have no effect. Any time the victim tries to rest, though, he must make an additional DC 28 Will save or be affected as per the spell _[[spells/Nightmare|nightmare]]_ (even if the victim doesn’t technically sleep). After a night of suffering vivid dreams and wrestling with the devil’s words, the victim must make yet another DC 28 Will save or have its alignment shift one step toward lawful evil. Only by unlearning what the deimavigga told it can a victim be free of this effect, requiring a spell such as _[[spells/Miracle|miracle]]_, _modify memory_, or _[[spells/Wish|wish]]_.

**Wisdom Drain (Su)** A deimavigga drains 1d6 points of Wisdom each time it hits with its claw attack. (A deimavigga does not _[[spells/Heal|heal]]_ any damage when it uses its Wisdom drain.)

##### Description

Regal, fearsome, and unfeeling, deimaviggas seek to turn the faithful from their gods, using cold logic to proselytize the path of atheism, the _[[spells/Freedom|freedom]]_ of the mortal spirit, and the order offered by Hell. Their ever-shifting masks speak envenomed words and give their hollow lies the _[[items/Ring/Ring of Truth|ring of truth]]_. Speaking out against all deities—except for Asmodeus, whom they subtly tout as a bringer of discipline even as they downplay his divinity—these _[[items/Weapon Magic Abilities/Deadly|deadly]]_ intellectuals know that those who turn from their deities are more likely to succumb to the temptations of diabolism. Rather than attempting to sway the souls of individual mortals, these _[[items/Weapon Magic Abilities/Cunning|cunning]]_ fiends take on the roles of prophets of reason, disguising themselves beneath layers of illusion to evangelize the virtues and freedoms of lives unshackled by the demands of egotistical deities. Occasionally one might focus its arguments on a soul of particular piety, delighting in _[[items/Weapon Magic Abilities/Throwing|throwing]]_ a deity’s most devoted servant into an inescapable crisis of faith. Deimaviggas care little for what gods their depredations affect, disenfranchising the worshipers of the pure and the profane alike.

In their natural shapes, deimaviggas stand 7 feet tall and weigh a mere 120 pounds. When disguised, though, they typically take the forms of wise elders who have lived long enough to understand fundamental truths about the universe, priests who have "realized their folly" and rejected their former dogma, or even "angels" of truth. Though they prefer to fight with words rather than with physical means, deimaviggas attack those who attempt to strip away their disguises and illusions, or who can argue as eloquently as they—though if possible, they prefer to do so discreetly and dispose of the bodies secretly.

Deimaviggas prefer to spend most of their time upon the Material Plane, swaying the weak and corruptible souls of mortals.There they seek out either vast mortal cities, where their heresy might reach many ears, or small communities where the isolated might fall to their blasphemous philosophizing. When in Hell, though, they linger in Caina, tormenting the souls of those trapped upon its lonely islands, developing and testing complicated and often confusing arguments.

Preferring to operate alone, these poison-tongued devils rarely work with others of their kind, even though their _[[spells/Status|status]]_ affords them control over their lesser brethren. They find that their arguments benefit from a single voice, and that their endeavors are complicated by even the most obedient minions. They bow to Hell’s hierarchy, however, and serve if compelled to do so. Pit fiends and infernal dukes sometimes utilize deimaviggas as personal majordomos, spies, and spreaders of dissension, though even among devilkind these enigmatic fiends are considered particularly unnerving.