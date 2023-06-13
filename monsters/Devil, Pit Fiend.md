---
cssclass: [monsters]
title1: Devil, Pit Fiend
desc_short: A pair of gigantic, flame-seared wings and eyes smoldering like embers
  give this towering devil a truly horrific appearance.
title2: Pit Fiend
CR: 20
sources:
- name: Pathfinder RPG Bestiary
  page: 80
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 307200
alignment: LE
size: Large
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 13
senses:
  darkvision: 60
  see in darkness: true
auras:
- name: fear
  radius: 20
  DC: 23
AC:
  AC: 38
  touch: 18
  flat_footed: 29
  components:
    dex: 9
    natural: 20
    size: -1
HP:
  HP: 350
  long: 20d10+240
  regeneration: 5
  regeneration_weakness: good weapons, good spells
saves:
  fort: 24
  ref: 21
  will: 18
DR:
- amount: 15
  weakness: good and silver
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 31
speeds:
  base: 40
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 claws +32 (2d8+13)
      entries:
      - - damage: 2d8+13
      count: 2
      attack: claws
      bonus:
      - 32
    - text: 2 wings +30 (2d6+6)
      entries:
      - - damage: 2d6+6
      count: 2
      attack: wings
      bonus:
      - 30
    - text: bite +32 (4d6+13 plus poison and disease)
      entries:
      - - damage: 4d6+13
        - effect: poison
        - effect: disease
      attack: bite
      bonus:
      - 32
    - text: tail slap +30 (2d8+6 plus grab)
      entries:
      - - damage: 2d8+6
        - effect: grab
      attack: tail slap
      bonus:
      - 30
  special:
  - constrict 2d8+19
  - devil shaping
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: blasphemy
    source: default
    freq: At will
    DC: 25
  - name: create undead
    source: default
    freq: At will
  - name: fireball
    source: default
    freq: At will
    DC: 21
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: greater scrying
    source: default
    freq: At will
    DC: 25
  - name: invisibility
    source: default
    freq: At will
  - name: magic circle against good
    source: default
    freq: At will
  - name: mass hold monster
    source: default
    freq: At will
    DC: 27
  - name: persistent image
    source: default
    freq: At will
    DC: 23
  - name: power word stun
    source: default
    freq: At will
  - name: scorching ray
    source: default
    freq: At will
  - name: trap the soul
    source: default
    freq: At will
    DC: 26
  - name: unholy aura
    source: default
    freq: At will
    DC: 26
  - name: wall of fire
    source: default
    freq: At will
  - name: quickened fireball
    source: default
    freq: 3/day
    DC: 21
  - name: meteor swarm
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: any 1 CR 19
      chance: 100%
    - name: lower devil
      chance: 100%
  - name: wish
    source: default
    freq: 1/year
  sources:
  - name: default
    CL: 18
ability_scores:
  STR: 37
  DEX: 29
  CON: 35
  INT: 26
  WIS: 30
  CHA: 26
BAB: 20
CMB: 34
CMB_other: +38 grapple
CMD: 53
feats:
- name: Cleave
- name: Great Cleave
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Vital Strike
- name: Iron Will
- name: Multiattack
- name: Power Attack
- name: Quicken Spell-Like Ability (fireball)
- name: Vital Strike
skills:
  Appraise: 17
  Bluff: 31
  Diplomacy: 31
  Disguise: 27
  Fly: 30
  Intimidate: 31
  Knowledge (arcana): 28
  Knowledge (planes): 31
  Knowledge (religion): 31
  Perception: 33
  Sense Motive: 33
  Spellcraft: 31
  Stealth: 28
  Survival: 22
  Use Magic Device: 28
languages:
- Celestial
- Common
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Hell)
  organization: solitary, pair, or council (3-9)
  treasure_type: double
special_abilities:
  Devil Shaping (Su): Three times per day, a pit fiend can spend a minute to transform
    nearby lemures into other lesser devils. A pit fiend can transform one lemure
    for every Hit Die the pit fiend possesses. It can then reshape these lemures into
    a number of Hit Dice's worth of lesser devils equal to the number of lemures affected.
    For example, a typical 20 Hit Dice pit fiend could transform 20 lemures into two
    bone devils (10 HD each), or three bearded devils (6 HD each, leaving two lemures
    unchanged), or any other combination of lesser devils. Lemures to be reshaped
    must be within 50 feet of the pit fiend, becoming stationary and unable to move
    once the shaping begins. After a minute passes, the lemures reform into the shape
    of a new lesser devil ready to follow the orders of the pit fiend. Although pit
    fiends can, technically, elevate a mass of 20 lemures into a new pit fiend, most
    are hesitant to do so since they have no special control over a devil created
    in this manner.
  Disease (Su): 'Devil Chills: Bite-injury; save Fort DC 32; onset immediate; frequency
    1/day; effect 1d4 Str damage; cure 3 consecutive saves. The save DC is Constitution-based.'
  Poison (Ex): Bite-injury; save Fort DC 32; frequency 1/round for 10 rounds; effect
    1d6 Con damage; cure 3 consecutive saves. The save DC is Constitution-based.
desc_long: |-
  Rulers of infernal realms, generals of Hell's armies, and advisors to the archfiends, pit fiends embody the awesome and terrible pinnacle of devilkind. Massive, physically indomitable, and possessed of ingenious evil intellects, these diabolical tyrants hold great autonomy whether in their service to the archfiends, in their rule of vast infernal fiefdoms, or in subjugation of mortal worlds. Thick muscles cling to their gigantic frames, armored over by dense, bladed scales capable of deflecting all but the most potent assaults. Fangs as thick as daggers fill their maws, bestial visages disguising some of the most insidious minds in Hell. Born within the depths of Nessus, the ninth and deepest layer of Hell, pit fiends are raised from the ranks of cornugons and gelugons by the archdevils and their dukes alone. While many travel to higher layers and far from Hell to command infernal legions, most remain in Nessus serving in the courts of Hell's elite or in dark councils with unknowable purposes. Pit fiends always stand over 14 feet tall, with wingspans in excess of 20 feet and weights over 1,000 pounds.

  Pit fiends are masters of fire and prefer lands bathed in flame. In Hell, this predisposes them to Avernus, Dis, Malebolge, Nessus, and Phlegethon the layers most likely to harbor their burning temple-citadels. Fanatics obsessed with diabolical superiority and ironclad obedience, pit fiends left to their own devices raise massive armies, scouring the pits of Hell for the most depraved lemures to transform into true fiends. When convinced they've formed the perfect legions, they turn their attentions to vulnerable demiplanes and mortal worlds, eyeing them for infernal domination and the glory of conquest. While obedient to the hierarchies of their kind, they are also strict in their enforcement, and should a pit fiend find itself subservient to a master unfit to rule, it holds itself duty bound to cast down such an incompetent lord. Thus, whether as masters or servants, pit fiends embody the will of Hell's merciless law and assure that only the strongest of devilkind flourish (or dare to).

  Only the most powerful of mortal spellcasters can or dare summon a pit fiend. These devils' reactions to summoning are deliberate and swift, usually typified by overwhelming rage that such insignificant beings would waste their immortal time. Those that cannot weather the devils' burning rage are slain-their souls typically racing the pit fiends back to Hell. Those who manage to keep control of the greater devils, though, intrigue them. A pit fiend might dutifully serve a mortal master for centuries, but its goal is always the same: to further corrupt the mortal soul, assure its absolute damnation, and when the mortal inevitably dies, claim its soul and begin the process of creating a perfectly corrupt lemure servant. Pit fiends know they are immortal and are intelligent enough to indulge in impossibly disciplined patience. As such, the eldest pit fiends see in their legions the faces of countless fools who once presumed themselves the devils' masters.

---

# Devil, Pit Fiend
A pair of gigantic, flame-seared wings and eyes smoldering like embers give this towering devil a truly horrific appearance.
**Source** Pathfinder RPG Bestiary pg. 80
**XP** 307,200

LE Large outsider (devil, evil, extraplanar, lawful)
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +33
**Aura** _[[universal monster rules/Fear|fear]]_ (20 ft., DC 23)

##### Defense

**AC** 38, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 29 (+9 Dex, +20 natural, –1 size)
**hp** 350 (20d10+240); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good weapons, good spells)
**Fort** +24, **Ref** +21, **Will** +18
**DR** 15/good and silver; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 31

##### Offense
**Speed** 40 ft., fly 60 ft. (average)
**Melee** 2 claws +32 (2d8+13), 2 wings +30 (2d6+6), bite +32 (4d6+13 plus poison and disease), tail slap +30 (2d8+6 plus _[[universal monster rules/Grab|grab]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ 2d8+19, devil shaping
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th)
At will—_[[spells/Blasphemy|blasphemy]]_ (DC 25), _[[spells/Create Undead|create undead]]_, _[[spells/Fireball|fireball]]_ (DC 21), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), greater _[[spells/Scrying|scrying]]_ (DC 25), _[[spells/Invisibility|invisibility]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, mass _[[spells/Hold Monster|hold monster]]_ (DC 27), _[[spells/Persistent Image|persistent image]]_ (DC 23), _[[spells/Power Word Stun|power word stun]]_, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Trap the Soul|trap the soul]]_ (DC 26), _[[spells/Unholy Aura|unholy aura]]_ (DC 26), _[[spells/Wall Of Fire|wall of fire]]_
3/day—quickened _fireball_ (DC 21)
1/day—_[[spells/Meteor Swarm|meteor swarm]]_, _[[universal monster rules/Summon|summon]]_ (level 9, any 1 CR 19 or lower devil, 100%)
1/year—_[[spells/Wish|wish]]_

##### Statistics
**Str** 37, **Dex** 29, **Con** 35, **Int** 26, **Wis** 30, **Cha** 26
**Base Atk** +20; **CMB** +34 (+38 grapple); **CMD** 53
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Great Cleave|Great Cleave]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_fireball_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Appraise +17, Bluff +31, Diplomacy +31, Disguise +27, Fly +30, Intimidate +31, Knowledge (arcana) +28, Knowledge (planes) +31, Knowledge (religion) +31, Perception +33, Sense Motive +33, Spellcraft +31, Stealth +28, Survival +22, Use Magic Device +28
**Languages** Celestial, Common, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or council (3–9)
**Treasure** double

### Special Abilities

**Devil Shaping (Su)** Three times per day, a pit fiend can spend a minute to transform nearby lemures into other lesser devils. A pit fiend can transform one lemure for every Hit Die the pit fiend possesses. It can then reshape these lemures into a number of Hit Dice’s worth of lesser devils equal to the number of lemures affected. For example, a typical 20 Hit Dice pit fiend could transform 20 lemures into two bone devils (10 HD each), or three bearded devils (6 HD each, leaving two lemures unchanged), or any other combination of lesser devils. Lemures to be reshaped must be within 50 feet of the pit fiend, becoming stationary and unable to move once the shaping begins. After a minute passes, the lemures reform into the shape of a new lesser devil ready to follow the orders of the pit fiend. Although pit fiends can, technically, elevate a mass of 20 lemures into a new pit fiend, most are hesitant to do so since they have no special control over a devil created in this manner.

**Disease (Su)** _[[diseases/Devil Chills|Devil Chills]]_: Bite—injury; save Fort DC 32; onset immediate; frequency 1/day; effect 1d4 Str damage; cure 3 consecutive saves. The save DC is Constitution-based.

**Poison (Ex) **Bite—injury; save Fort DC 32; frequency 1/round for 10 rounds; effect 1d6 Con damage; cure 3 consecutive saves. The save DC is Constitution-based.

##### Description

Rulers of infernal realms, generals of Hell’s armies, and advisors to the archfiends, pit fiends embody the awesome and terrible pinnacle of devilkind. Massive, physically indomitable, and possessed of ingenious evil intellects, these diabolical tyrants hold great autonomy whether in their service to the archfiends, in their rule of vast infernal fiefdoms, or in subjugation of mortal worlds. Thick muscles cling to their gigantic frames, armored over by dense, bladed scales capable of _[[items/Armor Magic Abilities/Deflecting|deflecting]]_ all but the most _[[items/Weapon Magic Abilities/Potent|potent]]_ assaults. Fangs as thick as daggers fill their maws, bestial visages disguising some of the most insidious minds in Hell. Born within the depths of Nessus, the ninth and deepest layer of Hell, pit fiends are raised from the ranks of cornugons and gelugons by the archdevils and their dukes alone. While many travel to higher layers and far from Hell to _[[spells/Command|command]]_ infernal legions, most remain in Nessus serving in the courts of Hell’s elite or in dark councils with unknowable purposes. Pit fiends always stand over 14 feet tall, with wingspans in excess of 20 feet and weights over 1,000 pounds.

Pit fiends are masters of fire and prefer lands bathed in flame. In Hell, this predisposes them to Avernus, Dis, Malebolge, Nessus, and Phlegethon the layers most likely to harbor their _[[items/Weapon Magic Abilities/Burning|burning]]_ temple-citadels. Fanatics obsessed with diabolical superiority and ironclad obedience, pit fiends left to their own devices raise massive armies, scouring the pits of Hell for the most depraved lemures to transform into true fiends. When convinced they’ve formed the perfect legions, they turn their attentions to vulnerable demiplanes and mortal worlds, eyeing them for infernal domination and the glory of conquest. While obedient to the hierarchies of their kind, they are also strict in their enforcement, and should a pit fiend find itself subservient to a master unfit to rule, it holds itself duty bound to cast down such an incompetent lord. Thus, whether as masters or servants, pit fiends embody the will of Hell’s merciless law and assure that only the strongest of devilkind flourish (or dare to).

Only the most powerful of mortal spellcasters can or dare _summon_ a pit fiend. These devils’ reactions to summoning are deliberate and swift, usually typified by overwhelming _[[spells/Rage|rage]]_ that such insignificant beings would waste their immortal time. Those that cannot weather the devils’ _burning_ _rage_ are slain—their souls typically racing the pit fiends back to Hell. Those who manage to keep control of the greater devils, though, intrigue them. A pit fiend might dutifully serve a mortal master for centuries, but its goal is always the same: to further corrupt the mortal soul, assure its absolute _[[spells/Damnation|damnation]]_, and when the mortal inevitably dies, claim its soul and begin the process of creating a perfectly corrupt lemure servant. Pit fiends know they are immortal and are intelligent enough to indulge in impossibly disciplined patience. As such, the eldest pit fiends see in their legions the faces of countless fools who once presumed themselves the devils’ masters.