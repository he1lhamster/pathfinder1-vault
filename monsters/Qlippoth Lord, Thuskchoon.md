---
cssclass: [monsters]
title1: Qlippoth Lord, Thuskchoon
desc_short: This sluglike creature leaves a swath of tar wherever he goes, andhis
  upper body opens into a gaping, sludge-dripping mouth.
title2: Thuskchoon
CR: 21
sources:
- name: Bestiary 6
  page: 238
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 409600
alignment: CE
size: Gargantuan
type: outsider
subtypes:
- chaotic
- evil
- extraplanar
- qlippoth
initiative:
  bonus: 14
senses:
  darkvision: 60
  detect good: true
  detect law: true
  tremorsense: 120
  true seeing: true
auras:
- name: cloak of chaos
  DC: 23
AC:
  AC: 37
  touch: 21
  flat_footed: 26
  components:
    deflection: 4
    dex: 10
    dodge,+16 natural: 1
    size: -4
HP:
  HP: 396
  long: 24d10+264
  regeneration: 15
  regeneration_weakness: lawful
saves:
  fort: 23
  ref: 28
  will: 27
defensive_abilities:
- freedom of movement
DR:
- amount: 15
  weakness: cold ironand lawful
immunities:
- acid
- cold
- death effects
- mind-affectingeffects
- poison
resistances:
  electricity: 30
  fire: 30
SR: 32
weaknesses:
- nearly mindless
speeds:
  base: 40
  burrow: 20
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +33 (6d8+13/19-20 plus 2d6 acid and grab)
      entries:
      - - damage: 6d8+13
          crit_range: 19-20
        - damage: 2d6
          type: acid
        - effect: grab
      attack: bite
      bonus:
      - 33
    - text: 4 talons 33 (2d6+13)
      entries:
      - - damage: 2d6+13
      count: 4
      attack: talons 33
  special:
  - breath weapon (120-ft. line, 20d10 acid damage,Reflex DC 33 half, every 1d4 rounds)
  - fast swallow
  - horrificappearance (DC 27)
  - swallow whole (10d6 bludgeoning damage,10d6 acid damage, and 1d6 Intelligence
    damage; AC 18; 39 hp)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: cloak of chaos
    source: default
    freq: Constant
    DC: 23
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: fly
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: acid fog
    source: default
    freq: At will
  - is_mythic_spell: true
    name: blindness/deafness
    source: default
    freq: At will
    DC: 17
  - is_mythic_spell: true
    name: desecrate
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
  - is_mythic_spell: true
    name: slow
    source: default
    freq: At will
    DC: 18
  - is_mythic_spell: true
    name: foresight
    source: default
    freq: 3/day
  - name: mass hunger for flesh
    source: default
    freq: 3/day
    DC: 21
  - is_mythic_spell: true
    name: power word blind
    source: default
    freq: 3/day
  - name: quickened slow
    source: default
    freq: 3/day
    DC: 18
  - name: vision
    source: default
    freq: 3/day
  - name: waves of exhaustion
    source: default
    freq: 3/day
  - name: imprisonment
    source: default
    freq: 1/day
    DC: 24
  - name: summon qlippoth
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 21
    concentration: 26
    mythic_restriction: Thuskchoon can use the mythic version of this ability within
      his sanctum.
ability_scores:
  STR: 36
  DEX: 30
  CON: 33
  INT: 3
  WIS: 28
  CHA: 21
BAB: 24
CMB: 41
CMB_other: +43 bull rush
CMD: 66
CMD_other: 68 vs. bullrush, can't be tripped
feats:
- name: Awesome Blow
- name: Blinding Critical
- name: Combat Reflexes
- name: CriticalFocus
- name: Dodge
- name: Improved Bull Rush
- name: Improved Critical (bite)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Power Attack
- name: Quicken Spell-Like Ability (slow)
- name: Vital Strike
skills:
  Fly: 45
  Perception: 36
languages:
- Abyssal (can't speak)
- telepathy 300 ft.
special_qualities:
- entangling acid
- false intellect
- intellectual flash
- no breath,trailing tar
ecology:
  environment: any (Abyss)
  organization: solitary (unique)
  treasure_type: triple
special_abilities:
  Entangling Acid (Ex): Any creature that takes acid damage from any of Thuskchoon's
    attacks or abilities (whether an extraordinary, supernatural, or spell-like ability)
    becomes entangled by the thick, sticky acid this qlippoth lord generates. Freedom
    of movement prevents this entangle effect; otherwise, it persists until a character
    peels off and discards the acidic sludge; doing so requires a successful DC 20
    Strength check. Attempting to do so is a standard action that provokes attacks
    of opportunity.
  False Intellect (Su): In any round that Thuskchoon causes any Intelligence damage
    to a creature via his swallow whole ability, the qlippoth lord can use that digested
    intellect to gain the benefits of his intellectual flash ability for 1 round per
    point of Intelligence damage dealt in that round. This duration stacks if Thuskchoon
    has swallowed multiple creatures, or if the Intelligence damage continues for
    more than 1 round.
  Horrific Appearance (Su): A creature that succumbs to Thuskchoon's horrific appearance
    has its mind flooded with horrific recollections that may or may not be real,
    repressed terrors knocked loose and brought to the conscious mind by the presence
    of the monstrosity that is Thuskchoon. Often these memories are a strange mix
    of racial memory and flashes from past lives. The victim also experiences genetic
    reversions. The victim is immediately affected by feeblemind (as per the spell),
    and its body is deformed and hideously twisted. Select (or choose randomly) from
    the list of deformities gained from the mutant template (see page 180 of Pathfinder
    RPG Bestiary 5) to apply to the victim. Alternatively, simply reduce one of the
    victim's physical ability scores by 4 points (feel free to devise an appropriate
    cosmetic atrocity to add flavor to this reduction). The feeblemind effect can
    be cured normally by any effect that removes that condition (see the spell description
    for more details), but the mutation is permanent and can be removed only via a
    miracle or wish spell, or by death and subsequent resurrection. Thuskchoon's horrific
    appearance has no effect on creatures with an Intelligence score of 1 or 0.
  Intellectual Flash (Ex): When Thuskchoon enters combat, there's a cumulative 20%
    chance per round that he receives a flash of intellect. Check for this flash at
    the start of the qlippoth lord's turn in combat. If the chance succeeds, for that
    round Thuskchoon loses his nearly mindless weakness and can use his spell-like
    abilities freely and engage in combat tactics on par with those of a typical human.
    During that round, Thuskchoon can attempt Knowledge checks untrained with a +20
    insight bonus (he retains his -4 penalty from his Intelligence score of 3, so
    this means his Knowledge checks are attempted with a +16 bonus for this round).
    The next round, the chance of an intellectual flash occurring is reduced to 0%,
    but then increases by 20% each subsequent round.
  Nearly Mindless (Ex): Thuskchoon's limited intellect and his overwhelming hunger
    combine to make the creature nearly mindless in his actions. Unless he uses his
    intellectual flash ability or gains the benefit of false intellect, he cannot
    activate any spell-like abilities and his tactical choices in combat are those
    of a violent animal. While in his nearly mindless state, Thuskchoon gains a +8
    bonus on all saving throws against mind-affecting effects.
  Trailing Tar (Ex): Thuskchoon exudes a thick swath of sticky, tarlike sludge whenever
    he moves using his base speed. Any square he passes over using this base speed
    is transformed into difficult terrain for 1 hour. Freedom of movement allows free
    passage through this sticky terrain, and a dose of universal solvent can cleanse
    one 5-foot-square area of tar. Spell effects that cleanse an area of filth or
    detritus can also remove this difficult terrain, provided the spell effect in
    question is 6th level or higher.
desc_long: |-
  Not all of the qlippoth lords have alien intelligences that outstrip the minds of most mortals. In the case of Thuskchoon, the qlippoth lord's intellect is replaced almost entirely by a ravenous need to consume and feed. Now and then, the qlippoth lord gains flashes of insight and momentarily comprehends vast puzzles of reality, yet those brief insights fade quickly. These periods of insight are lengthened when Thuskchoon consumes prey, for as he digests flesh, he also digests thought, and can parasitize his victim's minds in order to act with purpose. 

  Thuskchoon's Abyssal sanctum is a vast warren of tunnels that wind through the depths of the Abyss and connect most, if not all, of the other qlippoth sanctums. Rarely does he spend time in this maze of caves, though, instead aimlessly wandering the depths of the Abyss in constant search of anything to sate his eternal hunger. Now and then, the qlippoth lord blunders through portals that bring his ravenings to other planes, whereupon it is but a matter of time before he is banished or slain and forced to start his wanderings over anew from his sanctum's heart. 

  Thuskchoon measures 40 feet in length and weighs 16,000 pounds.

---

# Qlippoth Lord, Thuskchoon
This sluglike creature leaves a swath of tar wherever he goes, and

his upper body opens into a gaping, sludge-dripping mouth.
**Source** Bestiary 6 pg. 238
**XP** 409,600
CE Gargantuan outsider (chaotic, evil, extraplanar, qlippoth)
**Init** +14; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_,

_[[universal monster rules/Tremorsense|tremorsense]]_ 120 ft., _[[spells/True Seeing|true seeing]]_; Perception +36
**Aura** _[[spells/Cloak of Chaos|cloak of chaos]]_ (DC 23)

##### Defense

**AC** 37, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+4 deflection, +10 Dex, +1 _[[feats/Dodge|dodge]]_,

+16 natural, –4 size)
**hp** 396 (24d10+264); _[[universal monster rules/Regeneration|regeneration]]_ 15 (lawful)
**Fort** +23, **Ref** +28, **Will** +27
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 15/cold iron

and lawful; **Immune** acid, cold, death effects, mind-affecting

effects, poison; **Resist** electricity 30, fire 30; **SR** 32
**Weaknesses** nearly mindless

##### Offense
**Speed** 40 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., fly 60 ft. (good)
**Melee** bite +33 (6d8+13/19–20 plus 2d6 acid and _[[universal monster rules/Grab|grab]]_),

4 talons 33 (2d6+13)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (120-ft. line, 20d10 acid damage,

Reflex DC 33 half, every 1d4 rounds), _[[universal monster rules/Fast Swallow|fast swallow]]_, horrific

appearance (DC 27), _[[universal monster rules/Swallow Whole|swallow whole]]_ (10d6 bludgeoning damage,

10d6 acid damage, and 1d6 Intelligence damage; AC 18; 39 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 21st; concentration +26)
Constant—_cloak of chaos_ (DC 23), _detect good_, _detect law_, fly, _freedom of movement_, _true seeing_ 
At will—_[[spells/Acid Fog|acid fog]]_, blindness/deafness (DC 17), _[[spells/Desecrate|desecrate]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport, _[[spells/Slow|slow]]_ (DC 18) 
3/day—_[[spells/Foresight|foresight]]_, mass _[[spells/Hunger For Flesh|hunger for flesh]]_ (DC 21), _[[spells/Power Word Blind|power word blind]]_, quickened _slow_ (DC 18), _[[spells/Vision|vision]]_, _[[spells/Waves of Exhaustion|waves of exhaustion]]_ 
1/day—_[[spells/Imprisonment|imprisonment]]_ (DC 24), _[[universal monster rules/Summon|summon]]_ qlippoth 
 Thuskchoon can use the mythic version of this ability within his sanctum.

##### Statistics
**Str** 36, **Dex** 30, **Con** 33, **Int** 3, **Wis** 28, **Cha** 21
**Base Atk** +24; **CMB** +41 (+43 bull rush); **CMD** 66 (68 vs. bull

rush, can’t be tripped)
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, Critical

Focus, _Dodge_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_slow_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Fly +45, Perception +36
**Languages** Abyssal (can’t speak); _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** entangling acid, false intellect, intellectual flash, _[[universal monster rules/No Breath|no breath]]_,

trailing tar

##### Ecology

**Environment** any (Abyss)
**Organization** solitary (unique)
**Treasure** triple

### Special Abilities

**Entangling Acid (Ex)** Any creature that takes acid damage from any of Thuskchoon’s attacks or abilities (whether an extraordinary, supernatural, or spell-like ability) becomes _[[conditions/Entangled|entangled]]_ by the thick, _[[items/Weapon Magic Abilities/Sticky|sticky]]_ acid this qlippoth lord generates. _Freedom of movement_ prevents this _[[spells/Entangle|entangle]]_ effect; otherwise, it persists until a character peels off and discards the acidic sludge; doing so requires a successful DC 20 Strength check. Attempting to do so is a standard action that provokes attacks of opportunity.

**False Intellect (Su)** In any round that Thuskchoon causes any Intelligence damage to a creature via his _swallow whole_ ability, the qlippoth lord can use that digested intellect to gain the benefits of his intellectual flash ability for 1 round per point of Intelligence damage dealt in that round. This duration stacks if Thuskchoon has swallowed multiple creatures, or if the Intelligence damage continues for more than 1 round.

**Horrific Appearance (Su)** A creature that succumbs to Thuskchoon’s horrific appearance has its mind flooded with horrific recollections that may or may not be real, repressed terrors knocked loose and brought to the conscious mind by the presence of the monstrosity that is Thuskchoon. Often these memories are a strange mix of racial memory and flashes from past lives. The victim also experiences genetic reversions. The victim is immediately affected by _[[spells/Feeblemind|feeblemind]]_ (as per the spell), and its body is deformed and hideously twisted. Select (or choose randomly) from the list of deformities gained from the mutant template (see page 180 of Pathfinder RPG Bestiary 5) to apply to the victim. Alternatively, simply reduce one of the victim’s physical ability scores by 4 points (feel free to devise an appropriate cosmetic atrocity to add flavor to this reduction). The _feeblemind_ effect can be cured normally by any effect that removes that condition (see the spell description for more details), but the mutation is permanent and can be removed only via a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_ spell, or by death and subsequent _[[spells/Resurrection|resurrection]]_. Thuskchoon’s horrific appearance has no effect on creatures with an Intelligence score of 1 or 0.

**Intellectual Flash (Ex)** When Thuskchoon enters combat, there’s a cumulative 20% chance per round that he receives a flash of intellect. Check for this flash at the start of the qlippoth lord’s turn in combat. If the chance succeeds, for that round Thuskchoon loses his nearly mindless weakness and can use his _spell-like abilities_ freely and engage in combat tactics on par with those of a typical human. During that round, Thuskchoon can attempt Knowledge checks untrained with a +20 insight bonus (he retains his –4 penalty from his Intelligence score of 3, so this means his Knowledge checks are attempted with a +16 bonus for this round). The next round, the chance of an intellectual flash occurring is reduced to 0%, but then increases by 20% each subsequent round.

**Nearly Mindless (Ex)** Thuskchoon’s limited intellect and his overwhelming hunger combine to make the creature nearly mindless in his actions. Unless he uses his intellectual flash ability or gains the benefit of false intellect, he cannot activate any _spell-like abilities_ and his tactical choices in combat are those of a violent animal. While in his nearly mindless state, Thuskchoon gains a +8 bonus on all saving throws against mind-affecting effects.

**Trailing Tar (Ex)** Thuskchoon exudes a thick swath of _sticky_, tarlike sludge whenever he moves using his base speed. Any square he passes over using this base speed is transformed into difficult terrain for 1 hour. _Freedom of movement_ allows free passage through this _sticky_ terrain, and a dose of _[[items/Wondrous Item/Universal Solvent|universal solvent]]_ can _[[spells/Cleanse|cleanse]]_ one 5-foot-square area of tar. Spell effects that _cleanse_ an area of filth or detritus can also remove this difficult terrain, provided the spell effect in question is 6th level or higher.

##### Description

Not all of the qlippoth lords have alien intelligences that outstrip the minds of most mortals. In the case of Thuskchoon, the qlippoth lord’s intellect is replaced almost entirely by a _[[curses/Ravenous|ravenous]]_ need to consume and feed. Now and then, the qlippoth lord gains flashes of insight and momentarily comprehends vast puzzles of reality, yet those brief insights fade quickly. These periods of insight are lengthened when Thuskchoon consumes prey, for as he digests flesh, he also digests thought, and can parasitize his victim’s minds in order to act with purpose.

Thuskchoon’s Abyssal sanctum is a vast warren of tunnels that wind through the depths of the Abyss and connect most, if not all, of the other qlippoth sanctums. Rarely does he spend time in this _[[spells/Maze|maze]]_ of caves, though, instead aimlessly wandering the depths of the Abyss in constant search of anything to sate his eternal hunger. Now and then, the qlippoth lord blunders through portals that bring his ravenings to other planes, whereupon it is but a matter of time before he is banished or slain and forced to start his wanderings over anew from his sanctum’s heart.

Thuskchoon measures 40 feet in length and weighs 16,000 pounds.