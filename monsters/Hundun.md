---
cssclass: [monsters]
title1: Hundun
desc_short: The wrinkled, blotchy skin of this giant hangs from its body like hooded
  robes, masking its face.
title2: Hundun
CR: 21
sources:
- name: Bestiary 5
  page: 144
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 409600
alignment: CE
size: Large
type: aberration
subtypes:
- chaotic
- extraplanar
initiative:
  bonus: 10
senses:
  blindsense: 300
  detect law: true
AC:
  AC: 37
  touch: 23
  flat_footed: 31
  components:
    deflection: 8
    dex: 6
    natural: 14
    size: -1
HP:
  HP: 364
  long: 27d8+243
saves:
  fort: 18
  ref: 23
  will: 21
defensive_abilities:
- entropic mind
- evasion
- negative energy affinity
- spacetime shifting
DR:
- amount: 15
  weakness: lawful and piercing
immunities:
- aging effects
- cold
- disease
- mind-affecting effects
- petrification
- poison
resistances:
  fire: 30
SR: 32
speeds:
  base: 60
  other_semicolon: air walk
attacks:
  melee:
  - - text: unarmed strike +32/+32/+27/+27/+22/+22/+17 (4d8+12/19-20 plus 1d6 negative
        energy)
      entries:
      - - damage: 4d8+12
          crit_range: 19-20
        - damage: 1d6
          type: negative energy
      attack: unarmed strike
      bonus:
      - 32
      - 32
      - 27
      - 27
      - 22
      - 22
      - 17
  special:
  - befuddling strike (6/day, DC 29)
  - punishing kick (6/day, DC 29)
  - strange attractor
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: air walk
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: chaos hammer
    source: default
    freq: At will
    DC: 22
  - name: dimension door
    source: default
    freq: At will
  - name: enervation
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: mass inflict moderate wounds
    source: default
    freq: At will
    DC: 24
  - name: plane shift
    source: default
    freq: At will
    DC: 23
  - name: quickened dimension door
    source: default
    freq: 3/day
  - name: disintegrate
    source: default
    freq: 3/day
    DC: 24
  - name: quickened mass inflict moderate wounds
    source: default
    freq: 3/day
    DC: 24
  - name: word of chaos
    source: default
    freq: 3/day
    DC: 25
  - name: orb of the void
    source: default
    freq: 1/day
    DC: 26
  sources:
  - name: default
    CL: 21
    concentration: 29
ability_scores:
  STR: 34
  DEX: 22
  CON: 29
  INT: 18
  WIS: 23
  CHA: 27
BAB: 20
CMB: 33
CMD: 57
feats:
- name: Befuddling Strike
- name: Blind-Fight
- name: Combat Reflexes
- name: Dimensional Agility
- name: Dimensional Assault
- name: Dimensional Dervish
- name: Greater Blind-Fight
- name: Improved Blind-Fight
- name: Improved Critical (unarmed strike)
- name: Improved Initiative
- name: Improved Unarmed Strike
- name: Punishing Kick
- name: Quicken Spell-Like Ability (dimension door)
- name: Quicken Spell-Like Ability (mass inflict moderate wounds)
- name: Weapon Focus (unarmed strike)
skills:
  Acrobatics: 36
  Climb: 30
  Escape Artist: 36
  Intimidate: 38
  Knowledge (planes): 22
  Perception: 36
  Sense Motive: 27
  Spellcraft: 22
  Stealth: 32
  Swim: 30
languages:
- Abyssal
- Aklo
- Protean (can't speak any languages)
- telepathy 300 ft.
special_qualities:
- faceless
- no breath
ecology:
  environment: any (Abyss, Limbo, or Negative Energy Plane)
  organization: solitary, pair, or mob (3-5)
  treasure_type: none
special_abilities:
  Entropic Mind (Ex): A hundun's mind is a maelstrom of utter chaos. A hundun is immune
    to mind-affecting effects, and any creature that attempts to affect a hundun with
    a mind-affecting effect gains 1d4 temporary negative levels (Will DC 31 negates)
    from entropic feedback. These negative levels disappear automatically after 8
    hours. The save DC is Charisma-based.
  Faceless (Ex): A hundun has no eyes, but detects infinitesimal gravitic distortions
    through its skin, gaining blindsense 300 feet. A hundun is blind and deaf, and
    is immune to effects that depend on sight or hearing. It subsists on negative
    energy and doesn't breathe, eat, or drink.
  Spacetime Shifting (Ex): Reality constantly reconfigures in the vicinity of a hundun,
    correcting the paradoxes the creature's existence in space and time generates.
    This causes all attacks against the hundun to suffer a 20% miss chance, and grants
    the hundun a deflection bonus to AC and a racial bonus on Reflex saves equal to
    its Charisma modifier.
  Strange Attractor (Sp): |-
    A hundun can activate or deactivate the stafflike strange attractor it carries as a free action. While active, a strange attractor hovers in place, and the hundun can mentally move it up to 60 feet through space as a move action, to a maximum range of 300 feet. If it enters a space with a creature, it stops moving for the round and that creature must attempt a DC 31 Will saving throw. The creature falls unconscious for 1 round if it fails this save, or is nauseated for 1 round if it succeeds. The space around an active strange attractor twists and warps, trapping creatures within its gravity well. This functions like repulsion but in reverse: creatures within 60 feet attempting to move away from it are prevented from doing so, wasting their move actions (Reflex DC 31 negates). Lawful creatures beginning their turn within 60 feet of an active strange attractor are nauseated for 1 round (Will DC 31 negates). Nausea caused by a strange attractor is a mind-affecting effect. Creatures with the chaotic subtype are immune to all effects of the strange attractor. The save DCs are Charisma-based.
    A strange attractor can't be attacked or harmed by physical attacks, but disintegrate, mage's disjunction, a sphere of annihilation, or a rod of cancellation affect it. A strange attractor's touch AC is 18 (+8 deflection), and attacks against it suffer a 20% miss chance. If a hundun's strange attractor is destroyed, the hundun can create a new one after 1d8 hours of uninterrupted meditation. If a hundun is slain, its strange attractor disappears.
  Unarmed Strikes (Ex): A hundun's unarmed strikes deal 4d8 points of damage, and
    function as chaotic, magic, and adamantine weapons for the purpose of overcoming
    damage reduction. A hundun can make a flurry of blows attack with its unarmed
    strikes as a 20th-level monk, without increasing its base attack bonus or taking
    the -2 penalty on attack rolls. This ability also grants the hundun the befuddling
    strike rogue talent and the punishing kick hungry ghost monk class feature.
desc_long: |-
  In the nightmare dimensions of unreality beyond space and time, the power of alien Gods is sufficient to give life to intention. Hunduns are the incarnation of the desire to reduce the multiverse to a space filled with nothing but randomly f luctuating energy fields and gravitic curvatures. Hunduns are primordial alien monks who embody aspects of the gaping, formless void that preceded the creation of the multiverse. They are out of step with reality, which accommodates their individual existences as intractable errors that must be continually accounted for yet that can never fully be corrected. These bizarre aberrations of life are sustained by negative energy-life's antithetical force-yet they are not undead, nor do they differentiate between the living and the unliving in the pursuit of their purpose. Few beings can exist on the Negative Energy Plane for long, making the hunduns, who often make their homes there, something of an anomaly. Some scholars speculate that early hunduns came to the Negative Energy Plane as explorers, and remained there, addicted to the mixture of pain and euphoric release caused by the effects of negative energy on their skin.

   Hunduns are tireless antagonists of archons, asuras, axiomites, devils, inevitables, kytons, and other exemplars of law. They oppose any effort to impose or maintain discipline, structure, or regulation. They loathe and undermine the prospect of peace or tranquility, and relish confusion, disorder, and destruction. Though these attitudes would seem to make them ideological allies of the proteans, hunduns hold those creatures in contempt, caring nothing for that race's strange religion, nor the spontaneous, ephemeral acts of creation in which proteans delight. Hunduns believe that the freedom and truth of pure entropy are preferable to the artificial illusions of structure, and they seek to spread this brand of enlightenment to others as part of their goal to free all creation from order's fetters.

   Hunduns appear as gigantic humanoids with faces hidden by voluminous, hooded robes made out of their own wrinkled skin. In truth, their faces are not hidden, for they are faceless; the interiors of their hoods are just filled with more folds of skin. They carry staff-like objects known as strange attractors, which appear as different things to different observers but always as something that causes some form of revulsion or nausea: a shaft of knotted intestines and vital organs, studded with colored, weeping eyes; a polished metallic rod on which distorted ref lections of the observer indulge in extreme self-harm; a column of darkness in which worlds spiral toward a black heart that snuffs out the life on them. These implements are not artificial objects, but part of a hundun's body. As well as being weapons and snares, they are methods of reproduction. Two hunduns can bring their strange attractors together, causing them to merge into an egg-shaped object under the control of one of the parents; the other parent must create a new strange attractor. This ovoid is still a strange attractor in all respects save for its shape, but if it is moved, the development of the embryonic hundun within must begin anew. The gestation of the new hundun takes many years. When the egg hatches, the strange attractor is destroyed and a fully formed hundun emerges. Reproduction between hunduns doesn't involve any sort of love or even affection. Rather, the two hunduns feel a premonition that another hundun will be needed to fight order in the future, then meet and breed wordlessly.

   Hunduns can be found f loating in the Negative Energy Plane or within stable voids in the planes of chaos, meditating on ways to corrupt universal truths and undermine the laws of nature on a cosmic scale-anything they can exploit to trigger the collapse and implosion of entire dimensions or planes of existence. Though they spend the majority of their time in solitary contemplation or action, hunduns sometimes gather to oppose forms of creation or manifestations of law that require greater numbers to counteract. The creatures come together spontaneously, drawn by an innate sensitivity to the structuring forces that operate on reality.

   Hunduns stand around 10 feet tall, yet weigh only about 700 pounds. Sustained entirely by negative energy, hunduns never eat or rest and are immune to aging; they are effectively immortal and die only through violence.

---

# Hundun
The wrinkled, blotchy skin of this giant hangs from its body like hooded robes, masking its face.
**Source** Bestiary 5 pg. 144
**XP** 409,600
CE Large aberration (chaotic, extraplanar)
**Init** +10; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 300 ft., _[[spells/Detect Law|detect law]]_; Perception +36

##### Defense

**AC** 37, touch 23, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+8 deflection, +6 Dex, +14 natural, −1 size)
**hp** 364 (27d8+243)
**Fort** +18, **Ref** +23, **Will** +21
**Defensive Abilities** entropic mind, evasion, _[[universal monster rules/Negative Energy Affinity|negative energy affinity]]_, spacetime shifting; **DR** 15/lawful and piercing; **Immune** aging effects, cold, disease, mind-affecting effects, petrification, poison; **Resist** fire 30; **SR** 32

##### Offense
**Speed** 60 ft.; _[[spells/Air Walk|air walk]]_
**Melee** unarmed strike +32/+32/+27/+27/+22/+22/+17 (4d8+12/19–20 plus 1d6 negative energy)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[feats/Befuddling Strike|befuddling strike]]_ (6/day, DC 29), _[[feats/Punishing Kick|punishing kick]]_ (6/day, DC 29), strange attractor
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 21st; concentration +29)
Constant—_air walk_, _detect law_
 At will—_[[spells/Chaos Hammer|chaos hammer]]_ (DC 22), _[[spells/Dimension Door|dimension door]]_, _[[spells/Enervation|enervation]]_, greater _[[spells/Dispel Magic|dispel magic]]_, mass _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_ (DC 24), _[[spells/Plane Shift|plane shift]]_ (DC 23)
 3/day—quickened _dimension door_, _[[spells/Disintegrate|disintegrate]]_ (DC 24), quickened mass _inflict moderate wounds_ (DC 24), _[[spells/Word Of Chaos|word of chaos]]_ (DC 25)
 1/day—_[[spells/Orb Of The Void|orb of the void]]_ (DC 26)

##### Statistics
**Str** 34, **Dex** 22, **Con** 29, **Int** 18, **Wis** 23, **Cha** 27
**Base Atk** +20; **CMB** +33; **CMD** 57
**Feats** _Befuddling Strike_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Dimensional Agility|Dimensional Agility]]_, _[[feats/Dimensional Assault|Dimensional Assault]]_, _[[feats/Dimensional Dervish|Dimensional Dervish]]_, _[[feats/Greater Blind-Fight|Greater Blind-Fight]]_, _[[feats/Improved Blind-Fight|Improved Blind-Fight]]_, _[[feats/Improved Critical|Improved Critical]]_ (unarmed strike), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _Punishing Kick_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_dimension door_), _Quicken Spell-Like Ability_ (mass _inflict moderate wounds_), _[[feats/Weapon Focus|Weapon Focus]]_ (unarmed strike)
**Skills** Acrobatics +36, _[[universal monster rules/Climb|Climb]]_ +30, Escape Artist +36, Intimidate +38, Knowledge (planes) +22, Perception +36, Sense Motive +27, Spellcraft +22, Stealth +32, Swim +30
**Languages** Abyssal, Aklo, Protean (can’t speak any languages); _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** faceless, _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any (Abyss, Limbo, or Negative Energy Plane)
**Organization** solitary, pair, or mob (3–5)
**Treasure** none

### Special Abilities

**Entropic Mind (Ex)** A _[[monsters/Hundun|hundun]]_’s mind is a maelstrom of utter chaos. A _hundun_ is immune to mind-affecting effects, and any creature that attempts to affect a _hundun_ with a mind-affecting effect gains 1d4 temporary negative levels (Will DC 31 negates) from entropic feedback. These negative levels disappear automatically after 8 hours. The save DC is Charisma-based.
**Faceless (Ex)** A _hundun_ has no eyes, but detects infinitesimal gravitic distortions through its skin, gaining _blindsense_ 300 feet. A _hundun_ is blind and deaf, and is immune to effects that depend on sight or hearing. It subsists on negative energy and doesn’t breathe, eat, or drink.
**Spacetime Shifting (Ex)** Reality constantly reconfigures in the vicinity of a _hundun_, correcting the paradoxes the creature’s existence in space and time generates. This causes all attacks against the _hundun_ to suffer a 20% miss chance, and grants the _hundun_ a _deflection_ bonus to AC and a racial bonus on Reflex saves equal to its Charisma modifier.
**Strange Attractor (Sp)** A _hundun_ can activate or deactivate the stafflike strange attractor it carries as a free action. While active, a strange attractor hovers in place, and the _hundun_ can mentally move it up to 60 feet through space as a move action, to a maximum range of 300 feet. If it enters a space with a creature, it stops moving for the round and that creature must attempt a DC 31 Will saving throw. The creature falls _[[conditions/Unconscious|unconscious]]_ for 1 round if it fails this save, or is _[[conditions/Nauseated|nauseated]]_ for 1 round if it succeeds. The space around an active strange attractor twists and warps, trapping creatures within its _[[spells/Gravity Well|gravity well]]_. This functions like _[[spells/Repulsion|repulsion]]_ but in reverse: creatures within 60 feet attempting to move away from it are prevented from doing so, wasting their move actions (Reflex DC 31 negates). Lawful creatures beginning their turn within 60 feet of an active strange attractor are _nauseated_ for 1 round (Will DC 31 negates). Nausea caused by a strange attractor is a mind-affecting effect. Creatures with the chaotic subtype are immune to all effects of the strange attractor. The save DCs are Charisma-based.
A strange attractor can’t be attacked or harmed by physical attacks, but _disintegrate_, mage’s disjunction, a _[[items/Wondrous Item/Sphere of Annihilation|sphere of annihilation]]_, or a _[[items/Rod/Rod of Cancellation|rod of cancellation]]_ affect it. A strange attractor’s touch AC is 18 (+8 _deflection_), and attacks against it suffer a 20% miss chance. If a _hundun_’s strange attractor is destroyed, the _hundun_ can create a new one after 1d8 hours of uninterrupted meditation. If a _hundun_ is slain, its strange attractor disappears.
**Unarmed Strikes (Ex)** A _hundun_’s unarmed strikes deal 4d8 points of damage, and function as chaotic, magic, and adamantine weapons for the purpose of overcoming _[[universal monster rules/Damage Reduction|damage reduction]]_. A _hundun_ can make a flurry of blows attack with its unarmed strikes as a 20th-level _[[classes/Monk|monk]]_, without increasing its base attack bonus or taking the –2 penalty on attack rolls. This ability also grants the _hundun_ the _befuddling strike_ _[[classes/Rogue|rogue]]_ talent and the _punishing kick_ hungry _[[monsters/Ghost|ghost]]_ _monk_ class feature.

##### Description

In the _[[spells/Nightmare|nightmare]]_ dimensions of unreality beyond space and time, the power of alien Gods is sufficient to give life to intention. Hunduns are the incarnation of the desire to reduce the multiverse to a space filled with nothing but randomly f luctuating energy fields and gravitic curvatures. Hunduns are primordial alien monks who embody aspects of the gaping, formless void that preceded the creation of the multiverse. They are out of step with reality, which accommodates their individual existences as intractable errors that must be continually accounted for yet that can never fully be corrected. These bizarre aberrations of life are sustained by negative energy—life’s antithetical force—yet they are not undead, nor do they differentiate between the living and the unliving in the pursuit of their purpose. Few beings can exist on the Negative Energy Plane for long, making the hunduns, who often make their homes there, something of an anomaly. Some scholars speculate that early hunduns came to the Negative Energy Plane as explorers, and remained there, addicted to the mixture of pain and euphoric release caused by the effects of negative energy on their skin.

Hunduns are tireless antagonists of archons, asuras, axiomites, devils, inevitables, kytons, and other exemplars of law. They oppose any effort to impose or maintain discipline, structure, or regulation. They loathe and _[[feats/Undermine|undermine]]_ the prospect of peace or tranquility, and relish _[[spells/Confusion|confusion]]_, disorder, and _[[spells/Destruction|destruction]]_. Though these attitudes would seem to make them ideological allies of the proteans, hunduns hold those creatures in contempt, caring nothing for that race’s strange religion, nor the spontaneous, ephemeral acts of creation in which proteans delight. Hunduns believe that the _[[spells/Freedom|freedom]]_ and truth of pure entropy are preferable to the artificial illusions of structure, and they seek to spread this _[[spells/Brand|brand]]_ of enlightenment to others as part of their goal to free all creation from order’s fetters.

Hunduns appear as gigantic humanoids with faces hidden by voluminous, hooded robes made out of their own wrinkled skin. In truth, their faces are not hidden, for they are faceless; the interiors of their hoods are just filled with more folds of skin. They carry staff-like objects known as strange attractors, which appear as different things to different observers but always as something that causes some form of revulsion or nausea: a shaft of knotted intestines and vital organs, studded with colored, _[[items/Armor Magic Abilities/Weeping|weeping]]_ eyes; a polished metallic rod on which distorted ref lections of the observer indulge in extreme self-harm; a column of _[[spells/Darkness|darkness]]_ in which worlds spiral toward a _[[items/Wondrous Item/Black Heart|black heart]]_ that snuffs out the life on them. These implements are not artificial objects, but part of a _hundun_’s body. As well as being weapons and snares, they are methods of reproduction. Two hunduns can bring their strange attractors together, causing them to merge into an egg-shaped object under the control of one of the parents; the other parent must create a new strange attractor. This ovoid is still a strange attractor in all respects save for its shape, but if it is moved, the development of the embryonic _hundun_ within must begin anew. The gestation of the new _hundun_ takes many years. When the egg hatches, the strange attractor is destroyed and a fully formed _hundun_ emerges. Reproduction between hunduns doesn’t involve any sort of love or even affection. Rather, the two hunduns feel a premonition that another _hundun_ will be needed to fight order in the future, then meet and breed wordlessly.

Hunduns can be found f loating in the Negative Energy Plane or within _[[conditions/Stable|stable]]_ voids in the planes of chaos, meditating on ways to corrupt universal truths and _undermine_ the laws of nature on a cosmic scale—anything they can exploit to trigger the collapse and _[[spells/Implosion|implosion]]_ of entire dimensions or planes of existence. Though they spend the majority of their time in solitary contemplation or action, hunduns sometimes gather to oppose forms of creation or manifestations of law that require greater numbers to counteract. The creatures come together spontaneously, drawn by an innate sensitivity to the structuring forces that operate on reality.

Hunduns stand around 10 feet tall, yet weigh only about 700 pounds. Sustained entirely by negative energy, hunduns never eat or rest and are immune to aging; they are effectively immortal and die only through violence.