---
cssclass: [monsters]
title1: Alghollthu, Veiled Master
desc_short: This monstrosity has six eyes and six long tentacles-four that end in
  glowing spheres, and two with what look like hands.
title2: Veiled Master
CR: 14
sources:
- name: Bestiary 6
  page: 270
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
- name: Inner Sea Bestiary
  page: 56
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 38400
alignment: LE
size: Large
type: aberration
subtypes:
- aquatic
- shapechanger
initiative:
  bonus: 10
senses:
  darkvision: 120
auras:
- name: mucus cloud
  radius: 30
AC:
  AC: 30
  touch: 15
  flat_footed: 24
  components:
    armor: 4
    dex: 6
    natural: 11
    size: -1
HP:
  HP: 200
  long: 16d8+128
saves:
  fort: 13
  ref: 13
  will: 14
immunities:
- electricity
- mind-affecting effects
resistances:
  cold: 20
SR: 25
speeds:
  base: 10
  swim: 80
attacks:
  melee:
  - - text: bite +17 (2d6+6 plus consume memory and slime)
      entries:
      - - damage: 2d6+6
        - effect: consume memory
        - effect: slime
      attack: bite
      bonus:
      - 17
    - text: 2 claws +17 (1d6+6 plus slime)
      entries:
      - - damage: 1d6+6
        - effect: slime
      count: 2
      attack: claws
      bonus:
      - 17
    - text: 4 tentacles +12 touch (2d6 electricity plus thoughtlance)
      entries:
      - - damage: 2d6
          type: electricity
        - effect: thoughtlance
      count: 4
      attack: tentacles
      bonus:
      - 12
      touch: true
  special:
  - delayed suggestion
space: 10
reach: 10
reach_other: 20 ft. with claws and tentacles
spell_like_abilities:
  entries:
  - name: mage armor
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 18
  - name: dominate person
    source: default
    freq: At will
    DC: 21
  - name: hypnotic pattern
    source: default
    freq: At will
    DC: 18
  - name: illusory wall
    source: default
    freq: At will
    DC: 20
  - name: mirage arcana
    source: default
    freq: At will
    DC: 21
  - name: persistent image
    source: default
    freq: At will
    DC: 21
  - name: programmed image
    source: default
    freq: At will
    DC: 22
  - name: project image
    source: default
    freq: At will
    DC: 23
  - name: veil
    source: default
    freq: At will
    DC: 22
  - name: dominate monster
    source: default
    freq: 3/day
    DC: 25
  - name: quickened dominate person
    source: default
    freq: 3/day
    DC: 21
  - name: geas/quest
    source: default
    freq: 3/day
  - name: mass suggestion
    source: default
    freq: 3/day
    DC: 22
  sources:
  - name: default
    CL: 20
    concentration: 26
spells:
  entries:
  - name: symbol of persuasion
    source: Sorcerer
    level: 6
    DC: 23
  - name: symbol of pain
    source: Sorcerer
    level: 5
    DC: 22
  - name: teleport
    source: Sorcerer
    level: 5
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: phantasmal killer
    source: Sorcerer
    level: 4
    DC: 20
  - name: symbol of slowing
    source: Sorcerer
    level: 4
    DC: 21
  - name: clairaudience/clairvoyance
    source: Sorcerer
    level: 3
  - name: explosive runes
    source: Sorcerer
    level: 3
    DC: 20
  - name: hold person
    source: Sorcerer
    level: 3
    DC: 19
  - name: secret page
    source: Sorcerer
    level: 3
  - name: blindness/deafness
    source: Sorcerer
    level: 2
    DC: 18
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: levitate
    source: Sorcerer
    level: 2
  - name: symbol of mirroring
    source: Sorcerer
    level: 2
    DC: 19
  - name: touch of idiocy
    source: Sorcerer
    level: 2
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 17
  - name: comprehend languages
    source: Sorcerer
    level: 1
  - name: erase
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 17
  - name: silent image
    source: Sorcerer
    level: 1
    DC: 17
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 16
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 16
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 16
  sources:
  - name: Sorcerer
    type: known
    CL: 12
    concentration: 18
    slots:
      6: 4
      5: 6
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 22
  DEX: 22
  CON: 27
  INT: 21
  WIS: 19
  CHA: 22
BAB: 12
CMB: 19
CMD: 35
feats:
- name: Arcane Strike
- name: Combat Casting
- name: Combat Expertise
- name: Eschew Materials
- name: Extend Spell
- name: Improved Initiative
- name: Lightning Reflexes
- name: Quicken Spell
- name: Quicken Spell-Like Ability (dominate person)
skills:
  Knowledge (arcana): 21
  Knowledge (history): 21
  Knowledge (nature): 21
  Perception: 23
  Sense Motive: 20
  Spellcraft: 24
  Stealth: 21
  Swim: 33
  Use Magic Device: 22
languages:
- Aboleth
- Aklo
- Aquan
- Common
- Undercommon
special_qualities:
- change shape (any Small or Medium; greater polymorph)
- runemastery
- swift transformation
ecology:
  environment: any water
  organization: solitary or shoal (1 and 2-8 aboleths)
  treasure_type: triple
special_abilities:
  Consume Memory (Su): When a veiled master bites a creature, it consumes some of
    that creature's memories. The creature bitten must succeed at a DC 24 Fortitude
    save or gain 1 negative level. A veiled master has 5 hit points restored each
    time it gives a creature a negative level in this way, and it also learns some
    of the target creature's memories (subject to the GM's discretion). This is a
    mind-affecting effect. A veiled master can suppress this ability as a free action.
    The save DC is Charisma-based.
  Delayed Suggestion (Sp): Whenever a veiled master successfully uses dominate person
    or dominate monster on a creature, it can also implant a delayed suggestion that
    triggers when the dominate effect ends. Typically, this suggestion (which functions
    as a spell-like ability, CL 20th, Will DC 19 negates) is for the previously dominated
    creature to seek out the veiled master and submit to a new domination attempt,
    but sometimes, a veiled master implants other suggestions (such as a suggestion
    to attack the first person the creature sees).
  Mucus Cloud (Ex): While underwater, a veiled master exudes a 30-foot-radius cloud
    of transparent slime. All creatures in this area must succeed at a DC 26 Fortitude
    save each round or lose the ability to breathe air (but gain the ability to breathe
    water) for 24 hours. Renewed contact with this mucus cloud and failing another
    save extends the effect for another 24 hours. The save DC is Constitution-based.
  Runemastery (Ex): A veiled master is particularly skilled at casting spells that
    create magical writing, such as explosive runes, secret page, and spells with
    the word “symbol” in their names. It never requires material components or focus
    components when casting such spells, and the save DC of these spells increases
    by 1. A veiled master's symbol spells are difficult to disarm-the Disable Device
    DC for these symbols increases by 2.
  Slime (Ex): A creature hit by any of a veiled master's bite or claw attacks must
    succeed at a DC 26 Fortitude save or have its skin and flesh transform into a
    clear, slimy membrane over the course of 1d4 rounds. The creature's new flesh
    is soft and tender, reducing its Constitution score by 4 as long as the condition
    persists. If the creature's flesh isn't kept moist, it dries quickly and the creature
    takes 1d12 points of damage every 10 minutes. Remove disease and similar effects
    can restore an afflicted creature to normal, but immunity to disease offers no
    protection from this attack. The save DC is Constitution-based.
  Spells: A veiled master casts spells as a 12th-level sorcerer.
  Swift Transformation (Su): A veiled master can use its change shape ability as a
    swift action.
  Thoughtlance (Su): Four of a veiled master's tentacles end in glowing spheres of
    light. These spheres deal 2d6 points of electricity damage on a successful touch
    attack and also blast a creature's mind with waves of mental energy. A creature
    touched by one of these tentacles (regardless of whether the touch deals electricity
    damage) must succeed at a DC 24 Will save or be staggered for 1 round. Additional
    touches increase the duration of this effect by 1 round. While a creature is staggered
    in this manner, it must attempt concentration checks to cast spells as if it were
    experiencing extremely violent motion while casting (DC = 20 + spell level). The
    save DC is Charisma-based.
desc_long: |-
  Aboleths are among the oldest of the world's denizens, creatures that can trace back their presence in the deepest reaches of the world's oceans to times far before humanity came to dwell upon the globe-or before even most deities turned their attention to this tiny sphere of water and stone. In those ancient times, only elder forces and eldritch entities knew of the world. Even the gods were dismissed and ignored by the aboleth race, for while they were not gods as are known today, aboleths knew themselves capable, given time, of anything the gods could accomplish. And the aboleths have always had time. 

  During an ancient era, when aboleths manipulated humanity like puppets, some of their kind disguised themselves to walk among their pets, veiling themselves with magic to appear as humanoids. These were the veiled masters-if one were to foolishly attempt to impose human hierarchies upon this alien race, veiled masters would be considered the nobility among their aboleth kin. In truth, while aboleths do treat veiled masters with utmost respect and defer to their decisions, they are not regarded as the rulers of the race. Stranger and still more dangerous entities rule over veiled masters from the deepest trenches below the sea. 

  Aboleths are undoubtedly skilled at domination and illusion, but veiled masters are the true experts of the arcane. Veiled masters engineered the deceptions and manipulations of ancient humanity's culture. Their hidden gifts and subtle coaxings did much to encourage humanity's first rise to glory in that age, and in many of those first empires, veiled masters walking among the populace, whispering into their leaders' ears. The people knew the veiled masters as powerful wizards, and there were murmurs that the mysterious cabal was more than human, but few suspected the truth for very long. The veiled masters quelled such suspicions by doing violence to the bodies and minds of those who proved too curious. When the veiled masters first learned of humanity's growing hubris-of their belief that they were greater than their patrons-these manipulators punished humanity. At first, the punishments were minor, yet to the veiled masters' surprise and frustration, they only strengthened humanity's resolve. In the end, destruction was deemed the answer, and as human culture fell into ruins, the veiled masters retreated to the depths of the sea, content for now that the devastation above would serve as a lesson that would never be forgotten. 

  Today, veiled masters live on. They walk among the humanoid races again, watching and waiting. The time to teach a new lesson draws ever closer. 

  The average veiled master measures 14 feet in length and weighs 1,500 pounds.

---

# Alghollthu, Veiled Master
This monstrosity has six eyes and six long tentacles—four that end in glowing spheres, and two with what look like hands.
**Source** Bestiary 6 pg. 270, Inner Sea Bestiary pg. 56
**XP** 38,400

LE Large aberration (aquatic, shapechanger)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +23
**Aura** mucus cloud (30 ft.)

##### Defense

**AC** 30, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+4 armor, +6 Dex, +11 natural, –1 size)
**hp** 200 (16d8+128)
**Fort** +13, **Ref** +13, **Will** +14
**Immune** electricity, mind-affecting effects; **Resist** cold 20; **SR** 25

##### Offense
**Speed** 10 ft., swim 80 ft.
**Melee** bite +17 (2d6+6 plus consume memory and slime), 2 claws +17 (1d6+6 plus slime), 4 tentacles +12 touch (2d6 electricity plus thoughtlance)
**Space** 10 ft., **Reach** 10 ft. (20 ft. with claws and tentacles)
**Special Attacks** delayed _[[spells/Suggestion|suggestion]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +26)
Constant—_[[spells/Mage Armor|mage armor]]_ 
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), _[[spells/Dominate Person|dominate person]]_ (DC 21), _[[spells/Hypnotic Pattern|hypnotic pattern]]_ (DC 18), _[[spells/Illusory Wall|illusory wall]]_ (DC 20), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 21), _[[spells/Persistent Image|persistent image]]_ (DC 21), _[[spells/Programmed Image|programmed image]]_ (DC 22), _[[spells/Project Image|project image]]_ (DC 23), _[[spells/Veil|veil]]_ (DC 22) 
3/day—_[[spells/Dominate Monster|dominate monster]]_ (DC 25), quickened _dominate person_ (DC 21), geas/quest, mass _suggestion_ (DC 22)
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known** (CL 12th; concentration +18)
6th (4)—_[[spells/Symbol of Persuasion|symbol of persuasion]]_ (DC 23) 
5th (6)—_[[spells/Symbol of Pain|symbol of pain]]_ (DC 22), teleport 
4th (7)—_[[spells/Dimension Door|dimension door]]_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 20), _[[spells/Symbol of Slowing|symbol of slowing]]_ (DC 21) 
3rd (7)—clairaudience/clairvoyance, _[[spells/Explosive Runes|explosive runes]]_ (DC 20), _[[spells/Hold Person|hold person]]_ (DC 19), _[[spells/Secret Page|secret page]]_ 
2nd (8)—blindness/deafness (DC 18), _[[spells/Invisibility|invisibility]]_, _[[spells/Levitate|levitate]]_, _[[spells/Symbol of Mirroring|symbol of mirroring]]_ (DC 19), _[[spells/Touch of Idiocy|touch of idiocy]]_ 
1st (8)— _[[spells/Charm Person|charm person]]_ (DC 17), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Erase|erase]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 17), _[[spells/Silent Image|silent image]]_ (DC 17) 
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 16), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 16)

##### Statistics
**Str** 22, **Dex** 22, **Con** 27, **Int** 21, **Wis** 19, **Cha** 22
**Base Atk** +12; **CMB** +19; **CMD** 35
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_dominate person_)
**Skills** Knowledge (arcana, history, nature) +21, Perception +23, Sense Motive +20, Spellcraft +24, Stealth +21, Swim +33, Use Magic Device +22
**Languages** Aboleth, Aklo, Aquan, Common, Undercommon
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any Small or Medium; greater _[[spells/Polymorph|polymorph]]_), runemastery, swift _[[spells/Transformation|transformation]]_

##### Ecology

**Environment** any water
**Organization** solitary or shoal (1 and 2–8 aboleths)
**Treasure** triple

### Special Abilities

**Consume Memory (Su)** When a veiled master bites a creature, it consumes some of that creature’s memories. The creature bitten must succeed at a DC 24 Fortitude save or gain 1 negative level. A veiled master has 5 hit points restored each time it gives a creature a negative level in this way, and it also learns some of the target creature’s memories (subject to the GM’s discretion). This is a mind-affecting effect. A veiled master can suppress this ability as a free action. The save DC is Charisma-based.

**Delayed _Suggestion_ (Sp)** Whenever a veiled master successfully uses _dominate person_ or _dominate monster_ on a creature, it can also implant a delayed _suggestion_ that triggers when the dominate effect ends. Typically, this _suggestion_ (which functions as a spell-like ability, CL 20th, Will DC 19 negates) is for the previously dominated creature to seek out the veiled master and submit to a new domination attempt, but sometimes, a veiled master implants other suggestions (such as a _suggestion_ to attack the first person the creature sees).

**Mucus Cloud (Ex)** While _[[items/Weapon Magic Abilities/Underwater|underwater]]_, a veiled master exudes a 30-foot-radius cloud of transparent slime. All creatures in this area must succeed at a DC 26 Fortitude save each round or lose the ability to breathe air (but gain the ability to breathe water) for 24 hours. Renewed contact with this mucus cloud and failing another save extends the effect for another 24 hours. The save DC is Constitution-based.

**Runemastery (Ex)** A veiled master is particularly skilled at casting spells that create magical writing, such as _explosive runes_, _secret page_, and spells with the word “symbol” in their names. It never requires material components or focus components when casting such spells, and the save DC of these spells increases by 1. A veiled master’s symbol spells are difficult to disarm—the Disable Device DC for these symbols increases by 2.
**Slime (Ex)** A creature hit by any of a veiled master’s bite or claw attacks must succeed at a DC 26 Fortitude save or have its skin and flesh transform into a clear, slimy membrane over the course of 1d4 rounds. The creature’s new flesh is soft and tender, reducing its Constitution score by 4 as long as the condition persists. If the creature’s flesh isn’t kept moist, it dries quickly and the creature takes 1d12 points of damage every 10 minutes. _[[spells/Remove Disease|Remove disease]]_ and similar effects can restore an afflicted creature to normal, but _[[universal monster rules/Immunity|immunity]]_ to disease offers no protection from this attack. The save DC is Constitution-based.
**Spells** A veiled master casts spells as a 12th-level _sorcerer_.
**Swift _Transformation_ (Su)** A veiled master can use its _change shape_ ability as a swift action.

**Thoughtlance (Su)** Four of a veiled master’s tentacles end in glowing spheres of light. These spheres deal 2d6 points of electricity damage on a successful touch attack and also blast a creature’s mind with waves of mental energy. A creature touched by one of these tentacles (regardless of whether the touch deals electricity damage) must succeed at a DC 24 Will save or be _[[conditions/Staggered|staggered]]_ for 1 round. Additional touches increase the duration of this effect by 1 round. While a creature is _staggered_ in this manner, it must attempt concentration checks to cast spells as if it were experiencing extremely violent motion while casting (DC = 20 + spell level). The save DC is Charisma-based.

##### Description

Aboleths are among the oldest of the world’s denizens, creatures that can trace back their presence in the deepest reaches of the world’s oceans to times far before humanity came to dwell upon the globe—or before even most deities turned their attention to this tiny sphere of water and stone. In those ancient times, only elder forces and eldritch entities knew of the world. Even the gods were dismissed and ignored by the aboleth race, for while they were not gods as are known today, aboleths knew themselves capable, given time, of anything the gods could accomplish. And the aboleths have always had time.

During an ancient era, when aboleths manipulated humanity like puppets, some of their kind disguised themselves to walk among their pets, veiling themselves with magic to appear as humanoids. These were the veiled masters—if one were to foolishly attempt to impose human hierarchies upon this alien race, veiled masters would be considered the nobility among their aboleth kin. In truth, while aboleths do treat veiled masters with utmost respect and defer to their decisions, they are not regarded as the rulers of the race. Stranger and still more dangerous entities rule over veiled masters from the deepest trenches below the sea.

Aboleths are undoubtedly skilled at domination and illusion, but veiled masters are the true experts of the arcane. Veiled masters engineered the deceptions and manipulations of ancient humanity’s culture. Their hidden gifts and subtle coaxings did much to encourage humanity’s first rise to glory in that age, and in many of those first empires, veiled masters walking among the populace, whispering into their leaders’ ears. The people knew the veiled masters as powerful wizards, and there were murmurs that the mysterious cabal was more than human, but few suspected the truth for very long. The veiled masters quelled such suspicions by doing violence to the bodies and minds of those who proved too curious. When the veiled masters first learned of humanity’s _[[items/Weapon Magic Abilities/Growing|growing]]_ hubris—of their belief that they were greater than their patrons—these manipulators punished humanity. At first, the punishments were minor, yet to the veiled masters’ surprise and frustration, they only strengthened humanity’s resolve. In the end, _[[spells/Destruction|destruction]]_ was deemed the answer, and as human culture fell into ruins, the veiled masters retreated to the depths of the sea, content for now that the devastation above would serve as a lesson that would never be forgotten.

Today, veiled masters live on. They walk among the humanoid races again, watching and waiting. The time to teach a new lesson draws ever closer.

The average veiled master measures 14 feet in length and weighs 1,500 pounds.