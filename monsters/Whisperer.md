---
cssclass: [monsters]
title1: Whisperer
desc_short: This luminous shape stands twice the height of a human. A palelight shines
  where its face should be.
title2: Whisperer
CR: 20
sources:
- name: Bestiary 6
  page: 276
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 307200
alignment: NE
size: Large
type: fey
subtypes:
- extraplanar
- incorporeal
initiative:
  bonus: 20
senses:
  blindsight: 360
  low-light vision: true
  see indarkness: true
auras:
- name: whispers
  radius: 120
  DC: 30
AC:
  AC: 35
  touch: 35
  flat_footed: 24
  components:
    deflection: 9
    dex: 10
    dodge,+6 insight: 1
    size: -1
HP:
  HP: 363
  long: 22d6+286
saves:
  fort: 20
  ref: 23
  will: 21
defensive_abilities:
- anticipation
- incorporeal
- rejuvenate
DR:
- amount: 15
  weakness: cold iron
immunities:
- cold
- disease
- mind-affecting effects,poison
- sonic
SR: 31
speeds:
  fly: 100
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 6 mist tendrils +20 touch (3d10/19-20 plus cursed wound)
      entries:
      - - damage: 3d10
          crit_range: 19-20
        - effect: cursed wound
      count: 6
      attack: mist tendrils
      bonus:
      - 20
      touch: true
  special:
  - compel sacrifice
  - inescapable curse
space: 10
reach: 20
spell_like_abilities:
  entries:
  - name: animate plants
    source: default
    freq: At will
  - name: arboreal hammer
    source: default
    freq: At will
  - name: control water
    source: default
    freq: At will
  - name: control weather
    source: default
    freq: At will
  - name: dominate animal
    source: default
    freq: At will
    DC: 22
  - name: dream
    source: default
    freq: At will
  - name: etherealness
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: nightmare
    source: default
    freq: At will
    DC: 24
  - name: telekinesis
    source: default
    freq: At will
    DC: 24
  - name: transport via plants
    source: default
    freq: At will
  - name: triggered suggestion
    source: default
    freq: At will
    DC: 23
  - name: wind walk
    source: default
    freq: At will
  - name: commune with nature
    source: default
    freq: 3/day
  - name: quickened confusion
    source: default
    freq: 3/day
    DC: 23
  - name: quickened greater dispel magic
    source: default
    freq: 3/day
  - name: green caress
    source: default
    freq: 3/day
    DC: 25
  - name: earthquake
    source: default
    freq: 1/day
  - name: reverse gravity
    source: default
    freq: 1/day
  - name: whirlwind
    source: default
    freq: 1/day
    DC: 27
  - name: wish
    source: default
    freq: 1/day
    other: to duplicate druid spells of 7th or lower level only
  sources:
  - name: default
    CL: 20
    concentration: 29
ability_scores:
  STR:
  DEX: 31
  CON: 36
  INT: 24
  WIS: 23
  CHA: 29
BAB: 11
CMB: 22
CMD: 48
CMD_other: can't be tripped
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Flyby Attack
- name: Improved Critical (touch)
- name: Improved Initiative
- name: Iron Will
- name: Mobility
- name: Quicken Spell-Like Ability (confusion)
- name: Quicken Spell-Like Ability (greater dispelmagic)
- name: Skill Focus (Perception)
skills:
  Bluff: 34
  Disable Device: 32
  Fly: 41
  Knowledge (arcana,planes): 29
  Knowledge (religion): 29
  Knowledge (geography): 32
  Knowledge (nature): 32
  Perception: 37
  Sense Motive: 31
  Spellcraft: 29
  Stealth: 31
  Survival: 28
languages:
- Aklo
- Sylvan
- telepathy 300 ft.
special_qualities:
- primeval landscape
- unsuspected
ecology:
  environment: any wilderness
  organization: solitary
  treasure_type: double
special_abilities:
  Anticipation (Ex): A whisperer applies its Wisdom modifier to initiative checks
    and as an insight bonus to its Armor Class.
  Aura of Whispers (Su): Within 120 feet of a whisperer, the effects of its primeval
    landscape are significantly quickened. Creatures in the primeval landscape must
    attempt Will saves once per round to avoid its effects, rather than once per day.
  Compel Sacrifice (Su): When a whisperer uses its triggered suggestion spell-like
    ability on a creature currently under the influence of its primeval landscape,
    it can implant a suggestion to perform an act of self-destruction, such as “The
    next time you speak to someone you love, you will instead tell them you have found
    something better to love and then walk into the nearest body of water and drown
    yourself.”
  Cursed Wound (Su): Damage caused by a whisperer's mist tendrils overcomes all damage
    reduction and ignores all hardness, but damage the tendrils deal to objects is
    halved. Mist tendril damage does not heal naturally. A character attempting to
    use magical healing on a creature damaged in this way must succeed at a DC 31
    caster level check or the healing has no effect on the injured creature. Mist
    tendrils are primary natural touch attacks that create deep, bloodless, crater-shaped
    wounds.
  Inescapable Curse (Su): Once per day, a whisperer can focus its attention on a single
    sentient creature (any living creature with an Intelligence score of 3 or higher)
    within 120 feet to plant a potent curse on the target. The victim can resist this
    curse with a successful DC 30 Will save. If successful, that creature is immune
    to that whisperer's inescapable curse for 24 hours. If the victim fails the save,
    she grows increasingly obsessed with the whisperer's primeval landscape and will
    not voluntarily leave this region. If forced to exit this area, the victim becomes
    sickened, and the next time the victim falls asleep, she vanishes and returns
    to the exact point where the whisperer first placed the inescapable curse upon
    her, as per greater teleport. This is a curse effect. The save DC is Charisma-based.
  Primeval Landscape (Su): |-
    When a whisperer arrives on the Material Plane, it can spend 24 hours in a wilderness area to lay claim to a region of up to 10 miles in diameter as its territory, which then becomes its primeval landscape. While in a whisperer's primeval landscape, the DCs of Survival checks to navigate or avoid becoming lost are increased by 20. A divination that offers guidance, such as find the path, requires a successful DC 31 caster level check as it is cast or the result is corrupted and it instead leads explorers into the whisperer's embrace. A whisperer's primeval landscape is always under the effects of a grand perilous demesne curse (Pathfinder RPG Horror Adventures 144), as if the whisperer had cast supreme curse terrain. The total CR of hazards encountered simultaneously must be 18 or lower, rather than 15, and each individual hazard is CR 17 or lower, rather than 14. If any of the hazards are defeated, the whisperer automatically replaces them 24 hours later. A primeval landscape can be removed via remove curse or similar methods (against DC 30), as detailed for all cursed lands (Horror Adventures 143). Any creature that enters a primeval landscape begins to suffer increasingly vivid and maddening hallucinations. After spending 24 hours in the region, and again every 24 hours thereafter as long as it remains in the area, a creature can attempt a DC 30 Will save to resist being increasingly affected by the primeval landscape. Upon each failed saving throw, the creature moves one step down the following track. Casting greater restoration or psychic surgery on an affected creature moves it one step up the track. Miracle or wish removes all cumulative effects. Every full 24 hours spent outside of the primeval landscape, the victim moves one step up along this track. At the GM's discretion, the whisperer can choose to not to affect specific creatures or to stop their progression at a specific step. While the effects of a primeval landscape are not mind-affecting, mindless creatures and creatures with an Intelligence score of 2 or lower are immune to the effects. The save DC is Charisma-based. 

    First Failed Save: Things seem strange, and otherwise normal events or objects become ominous and unsettling. The victim gains the sickened condition. 

    Second Failed Save: The terrain seems to shift and warp while sounds are twisted into atonal parodies or blocked out by eerie whispering. In addition to being sickened, an affected creature moves at half speed and treats all other creatures as if they had concealment. 

    Third Failed Save: The subject's hallucinations crowd out actual events, and her perception bears little relationship to reality. In addition to the effects of earlier failed saves, an affected creature is staggered. 

    Fourth Failed Save: The subject's autonomic processes begin to fail as pain and paranoia take hold. The subject is nauseated. 

    Fifth Failed Save: The victim is slain.
  Rejuvenate (Su): A whisperer that is killed reappears in its primeval landscape
    at the next new moon. The only way to prevent a whisperer from rejuvenating is
    to remove the primeval landscape effect before the whisperer's rejuvenation.
  Unsuspected (Su): A creature that attempts a save against any of a whisperer's abilities
    is unaware that it has done so unless obvious visual evidence is present. Under
    such circumstances, the GM should roll saving throws for player characters in
    secret.
desc_long: |-
  Civilization spreads like an invasive species, destroying and consuming, transforming and dominating. There are some realms, though-primeval and pristine tracts of wilderness-that civilization will never claim. These are the whisperers' domains. 

  The whisperers are fey in the most otherworldly and alien way possible. They resent those who trespass on their primeval landscapes, the lone exceptions being the undead that rise from the spirits of their victims or those fey who, by their natures or through cruel fate, have fallen to evil. These fey seek out the whisperer's realm, both for the protection it provides and because they find its alien presence strangely euphoric; they often delight in leading intruders into the whisperer's grasp. 

  A whisperer's domain is nearly as hostile to intruders as the whisperer itself is. Lethal hazards, unexplainable occurrences, and eerie happenings are common in a primeval landscape, as are haunts formed from previous trespassers. Plant creatures and animals attack viciously, and even “ordinary” plants seem hostile to intruders. 

  A whisperer is 15 feet tall and, being incorporeal, is completely weightless.

---

# Whisperer
This luminous shape stands twice the height of a human. A pale

light shines where its face should be.
**Source** Bestiary 6 pg. 276
**XP** 307,200

NE Large fey (extraplanar, _[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +20; **Senses** _[[universal monster rules/Blindsight|blindsight]]_ 360 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, see in

_[[spells/Darkness|darkness]]_; Perception +37
**Aura** whispers (120 ft., DC 30)

##### Defense

**AC** 35, touch 35, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+9 deflection, +10 Dex, +1 _[[feats/Dodge|dodge]]_,

+6 insight, –1 size)
**hp** 363 (22d6+286)
**Fort** +20, **Ref** +23, **Will** +21
**Defensive Abilities** anticipation, _incorporeal_, rejuvenate; **DR** 15/cold iron; **Immune** cold, disease, mind-affecting effects,

poison, sonic; **SR** 31

##### Offense
**Speed** fly 100 ft. (perfect)
**Melee** 6 mist tendrils +20 touch (3d10/19–20 plus cursed wound)
**Space** 10 ft., **Reach** 20 ft.
**Special Attacks** compel _[[spells/Sacrifice|sacrifice]]_, inescapable curse
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +29)
At will—_[[spells/Animate Plants|animate plants]]_, _[[spells/Arboreal Hammer|arboreal hammer]]_, _[[spells/Control Water|control water]]_, _[[spells/Control Weather|control weather]]_, _[[spells/Dominate Animal|dominate animal]]_ (DC 22), _[[spells/Dream|dream]]_, _[[spells/Etherealness|etherealness]]_, greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Nightmare|nightmare]]_ (DC 24), _[[spells/Telekinesis|telekinesis]]_ (DC 24), _[[spells/Transport via Plants|transport via plants]]_, _[[spells/Triggered Suggestion|triggered suggestion]]_ (DC 23), _[[spells/Wind Walk|wind walk]]_ 
3/day—_[[spells/Commune with Nature|commune with nature]]_, quickened _[[spells/Confusion|confusion]]_ (DC 23), quickened greater _dispel magic_, _[[spells/Green Caress|green caress]]_ (DC 25) 
1/day—_[[spells/Earthquake|earthquake]]_, _[[spells/Reverse Gravity|reverse gravity]]_, _[[universal monster rules/Whirlwind|whirlwind]]_ (DC 27), _[[spells/Wish|wish]]_ (to duplicate _[[classes/Druid|druid]]_ spells of 7th or lower level only)

##### Statistics
**Str** —, **Dex** 31, **Con** 36, **Int** 24, **Wis** 23, **Cha** 29
**Base Atk** +11; **CMB** +22; **CMD** 48 (can’t be tripped)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_ (touch), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_confusion_, greater dispel

magic), _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Bluff +34, Disable Device +32, Fly +41, Knowledge (arcana,

planes, religion) +29, Knowledge (geography, nature) +32,

Perception +37, Sense Motive +31, Spellcraft +29, Stealth +31,

Survival +28
**Languages** Aklo, Sylvan; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** primeval landscape, unsuspected

##### Ecology

**Environment** any wilderness
**Organization** solitary
**Treasure** double

### Special Abilities

**Anticipation (Ex)** A _[[monsters/Whisperer|whisperer]]_ applies its Wisdom modifier to initiative checks and as an insight bonus to its Armor Class.

**Aura of Whispers (Su)** Within 120 feet of a _whisperer_, the effects of its primeval landscape are significantly quickened. Creatures in the primeval landscape must attempt Will saves once per round to avoid its effects, rather than once per day.

**Compel _Sacrifice_ (Su)** When a _whisperer_ uses its _triggered suggestion_ spell-like ability on a creature currently under the influence of its primeval landscape, it can implant a _[[spells/Suggestion|suggestion]]_ to perform an act of self-destruction, such as “The next time you speak to someone you love, you will instead tell them you have found something better to love and then walk into the nearest body of water and drown yourself.”

**Cursed Wound (Su)** Damage caused by a _whisperer_’s mist tendrils overcomes all _[[universal monster rules/Damage Reduction|damage reduction]]_ and ignores all hardness, but damage the tendrils deal to objects is halved. Mist tendril damage does not _[[spells/Heal|heal]]_ naturally. A character attempting to use magical healing on a creature damaged in this way must succeed at a DC 31 caster level check or the healing has no effect on the injured creature. Mist tendrils are primary natural touch attacks that create deep, bloodless, crater-shaped wounds.

**Inescapable Curse (Su)** Once per day, a _whisperer_ can focus its attention on a single sentient creature (any living creature with an Intelligence score of 3 or higher) within 120 feet to plant a _[[items/Weapon Magic Abilities/Potent|potent]]_ curse on the target. The victim can resist this curse with a successful DC 30 Will save. If successful, that creature is immune to that _whisperer_’s inescapable curse for 24 hours. If the victim fails the save, she grows increasingly obsessed with the _whisperer_’s primeval landscape and will not voluntarily leave this region. If forced to exit this area, the victim becomes _[[conditions/Sickened|sickened]]_, and the next time the victim falls asleep, she vanishes and returns to the exact point where the _whisperer_ first placed the inescapable curse upon her, as per greater teleport. This is a curse effect. The save DC is Charisma-based.

**Primeval Landscape (Su)** When a _whisperer_ arrives on the Material Plane, it can spend 24 hours in a wilderness area to lay claim to a region of up to 10 miles in diameter as its territory, which then becomes its primeval landscape. While in a _whisperer_’s primeval landscape, the DCs of Survival checks to navigate or avoid becoming lost are increased by 20. A _[[spells/Divination|divination]]_ that offers _[[spells/Guidance|guidance]]_, such as _[[spells/Find the Path|find the path]]_, requires a successful DC 31 caster level check as it is cast or the result is corrupted and it instead leads explorers into the _whisperer_’s embrace. A _whisperer_’s primeval landscape is always under the effects of a grand perilous demesne curse (Pathfinder RPG Horror Adventures 144), as if the _whisperer_ had cast supreme _[[spells/Curse Terrain|curse terrain]]_. The total CR of hazards encountered simultaneously must be 18 or lower, rather than 15, and each individual hazard is CR 17 or lower, rather than 14. If any of the hazards are defeated, the _whisperer_ automatically replaces them 24 hours later. A primeval landscape can be removed via _[[spells/Remove Curse|remove curse]]_ or similar methods (against DC 30), as detailed for all cursed lands (Horror Adventures 143). Any creature that enters a primeval landscape begins to suffer increasingly vivid and maddening hallucinations. After spending 24 hours in the region, and again every 24 hours thereafter as long as it remains in the area, a creature can attempt a DC 30 Will save to resist being increasingly affected by the primeval landscape. Upon each failed saving throw, the creature moves one step down the following track. Casting greater _[[spells/Restoration|restoration]]_ or _[[spells/Psychic Surgery|psychic surgery]]_ on an affected creature moves it one _[[feats/Step Up|step up]]_ the track. _[[spells/Miracle|Miracle]]_ or _wish_ removes all cumulative effects. Every full 24 hours spent outside of the primeval landscape, the victim moves one _step up_ along this track. At the GM’s discretion, the _whisperer_ can choose to not to affect specific creatures or to stop their progression at a specific step. While the effects of a primeval landscape are not mind-affecting, mindless creatures and creatures with an Intelligence score of 2 or lower are immune to the effects. The save DC is Charisma-based.

First Failed Save: Things seem strange, and otherwise normal events or objects become _[[items/Weapon Magic Abilities/Ominous|ominous]]_ and unsettling. The victim gains the _sickened_ condition.

Second Failed Save: The terrain seems to shift and warp while sounds are twisted into atonal parodies or blocked out by eerie whispering. In addition to being _sickened_, an affected creature moves at half speed and treats all other creatures as if they had concealment.

Third Failed Save: The subject’s hallucinations crowd out actual events, and her perception bears little relationship to reality. In addition to the effects of earlier failed saves, an affected creature is _[[conditions/Staggered|staggered]]_.

Fourth Failed Save: The subject’s autonomic processes begin to fail as pain and _[[spells/Paranoia|paranoia]]_ take hold. The subject is _[[conditions/Nauseated|nauseated]]_.

Fifth Failed Save: The victim is slain.

**Rejuvenate (Su)** A _whisperer_ that is killed reappears in its primeval landscape at the next new moon. The only way to prevent a _whisperer_ from rejuvenating is to remove the primeval landscape effect before the _whisperer_’s rejuvenation.

**Unsuspected (Su)** A creature that attempts a save against any of a _whisperer_’s abilities is unaware that it has done so unless obvious visual evidence is present. Under such circumstances, the GM should roll saving throws for player characters in secret.

##### Description

Civilization spreads like an invasive species, destroying and consuming, transforming and dominating. There are some realms, though—primeval and pristine tracts of wilderness—that civilization will never claim. These are the whisperers’ domains.

The whisperers are fey in the most otherworldly and alien way possible. They resent those who trespass on their primeval landscapes, the lone exceptions being the undead that rise from the spirits of their victims or those fey who, by their natures or through _[[items/Weapon Magic Abilities/Cruel|cruel]]_ fate, have _[[monsters/Fallen|fallen]]_ to evil. These fey seek out the _whisperer_’s realm, both for the protection it provides and because they find its alien presence strangely euphoric; they often delight in leading intruders into the _whisperer_’s _[[spells/Grasp|grasp]]_.

A _whisperer_’s domain is nearly as hostile to intruders as the _whisperer_ itself is. Lethal hazards, unexplainable occurrences, and eerie happenings are common in a primeval landscape, as are haunts formed from previous trespassers. Plant creatures and animals attack viciously, and even “ordinary” plants seem hostile to intruders.

A _whisperer_ is 15 feet tall and, being _incorporeal_, is completely weightless.