---
cssclass: [monsters]
title1: Uvaglor, the Misbegotten Prince
desc_short: This vulture-headed demon has crimson wings and a baleful third eye in
  his forehead. He is clad in lengths of chain and metal plates, and carries a cruel-looking
  sword in one hand and a glowing sphere of violet crystal in the other.
title2: Uvaglor, the Misbegotten Prince
CR: 20
sources:
- name: Demons Revisited
  page: 62
  link: http://paizo.com/products/btpy8yvo?Pathfinder-Campaign-Setting-Demons-Revisited
XP: 307200
race: Male
classes:
- advanced vrock oracle 15 (Pathfinder RPG Bestiary 69)
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 13
senses:
  darkvision: 60
  true seeing: true
AC:
  AC: 34
  touch: 11
  flat_footed: 32
  components:
    armor: 10
    dex: 2
    natural: 13
    size: -1
HP:
  HP: 371
  long: 9d10+15d8+255
  HD: 24
saves:
  fort: 21
  ref: 20
  will: 18
DR:
- amount: 10
  weakness: good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 20
speeds:
  base: 20
  fly: 50
  fly_maneuverability: average
attacks:
  melee:
  - - text: +4 unholy longsword +34/+29/+24/+19 (2d6+15/17-20)
      entries:
      - - damage: 2d6+15
          crit_range: 17-20
      attack: +4 unholy longsword
      bonus:
      - 34
      - 29
      - 24
      - 19
    - text: bite +30 (1d8+5)
      entries:
      - - damage: 1d8+5
      attack: bite
      bonus:
      - 30
    - text: claw +30 (2d6+5)
      entries:
      - - damage: 2d6+5
      attack: claw
      bonus:
      - 30
    - text: 2 talons +30 (1d6+5)
      entries:
      - - damage: 1d6+5
      count: 2
      attack: talons
      bonus:
      - 30
  special:
  - command avian
  - dance of ruin
  - spores
  - stunning screech
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: telekinesis
    source: default
    freq: At will
    DC: 22
  - name: dominate monster
    source: default
    freq: 3/day
    other: creatures with wings only
  - name: heroism
    source: default
    freq: 1/day
  - name: mirror image
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: vrock
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 12
    concentration: 19
spells:
  entries:
  - name: destruction
    source: Oracle
    level: 7
    DC: 24
  - name: insanity
    source: Oracle
    level: 7
    DC: 24
  - name: mass cure serious wounds
    source: Oracle
    level: 7
  - name: refuge
    source: Oracle
    level: 7
  - name: reverse gravity
    source: Oracle
    level: 7
  - name: blade barrier
    source: Oracle
    level: 6
    DC: 23
  - name: geas/quest
    source: Oracle
    level: 6
  - name: heal
    source: Oracle
    level: 6
  - name: mass cure moderate wounds
    source: Oracle
    level: 6
  - name: planar binding
    source: Oracle
    level: 6
    DC: 23
  - name: breath of life
    source: Oracle
    level: 5
  - name: greater command
    source: Oracle
    level: 5
    DC: 22
  - name: insect plague
    source: Oracle
    level: 5
  - name: lesser planar binding
    source: Oracle
    level: 5
    DC: 22
  - name: mass cure light wounds
    source: Oracle
    level: 5
  - name: telekinesis
    source: Oracle
    level: 5
  - name: unhallow
    source: Oracle
    level: 5
  - name: confusion
    source: Oracle
    level: 4
    DC: 21
  - name: cure critical wounds
    source: Oracle
    level: 4
  - name: dimensional anchor
    source: Oracle
    level: 4
  - name: freedom of movement
    source: Oracle
    level: 4
  - name: poison
    source: Oracle
    level: 4
    DC: 21
  - name: sending
    source: Oracle
    level: 4
  - name: blindness/deafness
    source: Oracle
    level: 3
    DC: 20
  - name: cure serious wounds
    source: Oracle
    level: 3
  - name: dispel magic
    source: Oracle
    level: 3
  - name: searing light
    source: Oracle
    level: 3
  - name: vermin shape I
    source: Oracle
    level: 3
  - name: water breathing
    source: Oracle
    level: 3
  - name: bull's strength
    source: Oracle
    level: 2
  - name: cure moderate wounds
    source: Oracle
    level: 2
  - name: death knell
    source: Oracle
    level: 2
    DC: 19
  - name: hold person
    source: Oracle
    level: 2
    DC: 19
  - name: levitate
    source: Oracle
    level: 2
  - name: minor image
    source: Oracle
    level: 2
    DC: 19
  - name: resist energy
    source: Oracle
    level: 2
  - name: sound burst
    source: Oracle
    level: 2
    DC: 19
  - name: status
    source: Oracle
    level: 2
  - name: command
    source: Oracle
    level: 1
    DC: 18
  - name: cure light wounds
    source: Oracle
    level: 1
  - name: divine favor
    source: Oracle
    level: 1
  - name: endure elements
    source: Oracle
    level: 1
  - name: entropic shield
    source: Oracle
    level: 1
  - name: sanctuary
    source: Oracle
    level: 1
    DC: 18
  - name: shield of faith
    source: Oracle
    level: 1
  - name: bleed
    source: Oracle
    level: 0
    DC: 17
  - name: create water
    source: Oracle
    level: 0
  - name: detect magic
    source: Oracle
    level: 0
  - name: ghost sound
    source: Oracle
    level: 0
  - name: guidance
    source: Oracle
    level: 0
  - name: light
    source: Oracle
    level: 0
  - name: mage hand
    source: Oracle
    level: 0
  - name: mending
    source: Oracle
    level: 0
  - name: read magic
    source: Oracle
    level: 0
  - name: resistance
    source: Oracle
    level: 0
  - name: stabilize
    source: Oracle
    level: 0
  sources:
  - name: Oracle
    type: known
    CL: 15
    concentration: 22
    slots:
      7: 5
      6: 7
      5: 7
      4: 7
      3: 8
      2: 8
      1: 8
      0: at-will
    mystery: outer rifts
ability_scores:
  STR: 32
  DEX: 21
  CON: 31
  INT: 18
  WIS: 22
  CHA: 24
BAB: 20
CMB: 32
CMD: 47
feats:
- name: Blinding Critical
- name: Combat Reflexes
- name: Craft Magic Arms and Armor
- name: Critical Focus
- name: Extend Spell
- name: Greater Vital Strike
- name: Improved Critical (longsword)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Power Attack
- name: Quicken Spell
- name: Vital Strike
skills:
  Acrobatics: 28
    when jumping: 24
  Bluff: 34
  Fly: 26
  Knowledge (arcana): 31
  Knowledge (religion): 31
  Perception: 41
  Sense Motive: 33
  Spellcraft: 25
  Stealth: 24
languages:
- Abyssal
- Celestial
- Common
- Draconic
- Varisian
- telepathy 100 ft.
special_qualities:
- oracle's curse (haunted)
- revelations (balefire [2/day], dread resilience, planar haze [3/day], rift weapon
  [4/day], unearthly terrain [10/day])
- third eye
gear:
  gear:
  - +4 chainmail
  - +4 unholy longsword
  - crystal ball with telepathy
  - strand of prayer beads
special_abilities:
  Command Avian (Su): Uvaglor gains a +4 racial bonus on the save DC of charm or compulsion
    effects used against winged creatures.
  Third Eye (Su): Uvaglor's third eye sees a few seconds into the future. This grants
    him a +4 racial bonus on initiative checks and Reflex saves.
desc_long: |-
  In the ancient past, long before the rise of Azlant, during the near-mythical era known to scholars as the Age of Creation, two powerful demons met for the first time and descended to a world in the Material Plane to enjoy a short-lived but violently ardent dalliance in the mortal realm. The planet itself heaved and buckled before their blasphemous passions, thrusting upward to create a rasp-like ridge. The result of this vile union quickened much more quickly than a normal pregnancy, and the spawn of the two demons was birthed even as they continued their frolic. When the demons left the world, they left behind a landscape scarred by their coupling, and a just-whelped fiend of tremendous power and potential that slithered into a deep cave in the ridge to hide and grow.

  Certain rare texts on demonology maintain that these two demons were none other than Lamashtu and Pazuzu, and that not long after their meeting their lusts turned to hatred. Today, there is no greater enmity in all the Abyss than the hostility between those two demon lords, and both of their cults deny vehemently that such an encounter as described above could ever have taken place.

  And yet, the spawn of that union lived and grew, and in the Age of Anguish it emerged to conquer the Varisians even as they were beginning to recover from their slavery under Thassilon's rule and the devastation of Earthfall. This fiend was Uvaglor, a vrock who possessed a singular third eye in his brow that could see brief glimpses into the future. Uvaglor ruled the Varisians for many years until the desperate indigenous people invoked Lamashtu's aid in defeating the demon. The Mother of Monsters seemed eager to comply with this request, but as the battle against Uvaglor went on, her minions turned on the Varisians and attempted to destroy them as well. Only the heroics of a priestess of the empyreal lord Ashava, a woman named Sazzleru, saved the people from annihilation and liberated them from Lamashtu's inf luence while banishing Uvaglor from the Rasp into a nameless prison adrift deep in the Maelstrom.

  Uvaglor lives on still, but only recently managed to escape from the nameless prison to return to the Abyss. After gathering his power, he has turned his attention once again to the site of his conception-the Lost Coast of Varisia, formed when the land west of the Rasp fell into the sea. Already he has installed several of his agents, including a mysterious mothman priest known as the Red Bishop, but his actions have attracted the attention of others who would rule this region, and this time, greater eyes than those of mortals look down upon this building conf lict. Lamashtu and Pazuzu's interest in the region cannot be denied, and their unknown ultimate plans, as well as Uvaglor's recent secret arrival in the region, portend dark times indeed.

  Uvaglor prefers offerings of fine art depicting imagery of Ashava, or of clerics of that empyreal lord-works of art the vrock enjoys befouling and destroying in increasingly creative methods. It's a DC 30 check to research the Misbegotten Prince.

---

# Uvaglor, the Misbegotten Prince
This vulture-headed demon has crimson wings and a baleful _[[items/Wondrous Item/Third Eye|third eye]]_ in his forehead. He is clad in lengths of chain and metal plates, and carries a cruel-looking sword in one hand and a glowing sphere of violet crystal in the other.
**Source** Demons Revisited pg. 62
**XP** 307,200
Male advanced vrock _[[classes/Oracle|oracle]]_ 15 (Pathfinder RPG Bestiary 69)
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +13; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +41

##### Defense

**AC** 34, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+10 armor, +2 Dex, +13 natural, –1 size)
**hp** 371 (24 HD; 9d10+15d8+255)
**Fort** +21, **Ref** +20, **Will** +18
**DR** 10/good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 20

##### Offense
**Speed** 20 ft., fly 50 ft. (average)
**Melee** +4 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Longsword|longsword]]_ +34/+29/+24/+19 (2d6+15/17–20), bite +30 (1d8+5), claw +30 (2d6+5), 2 talons +30 (1d6+5)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[spells/Command|command]]_ avian, dance of ruin, spores, stunning _[[spells/Screech|screech]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +19)
At will—greater teleport (self plus 50 lbs. of objects only), _[[spells/Telekinesis|telekinesis]]_ (DC 22)
3/day—_[[spells/Dominate Monster|dominate monster]]_ (creatures with wings only)
1/day—_[[spells/Heroism|heroism]]_, _[[spells/Mirror Image|mirror image]]_, _[[universal monster rules/Summon|summon]]_ (level 3, 1 vrock 35%)
**_Oracle_ Spells Known **(CL 15th; concentration +22)
7th (5/day)—_[[spells/Destruction|destruction]]_ (DC 24), _[[spells/Insanity|insanity]]_ (DC 24), mass _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Refuge|refuge]]_, _[[spells/Reverse Gravity|reverse gravity]]_
6th (7/day)—_[[spells/Blade Barrier|blade barrier]]_ (DC 23), geas/quest, _[[spells/Heal, Mass|heal, mass]]_ _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Planar Binding|planar binding]]_ (DC 23)
5th (7/day)—_[[spells/Breath Of Life|breath of life]]_, greater _command_ (DC 22), _[[spells/Insect Plague|insect plague]]_, lesser _planar binding_ (DC 22), mass _[[spells/Cure Light Wounds|cure light wounds]]_, _telekinesis_, _[[spells/Unhallow|unhallow]]_
4th (7/day)—_[[spells/Confusion|confusion]]_ (DC 21), _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Freedom of Movement|freedom of movement]]_, poison (DC 21), _[[spells/Sending|sending]]_
3rd (8/day)—blindness/deafness (DC 20), _cure serious wounds_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Searing Light|searing light]]_, _[[spells/Vermin Shape I|vermin shape I]]_, _[[universal monster rules/Water Breathing|water breathing]]_
2nd (8/day)—bull’s strength, _cure moderate wounds_, _[[spells/Death Knell|death knell]]_ (DC 19), _[[spells/Hold Person|hold person]]_ (DC 19), _[[spells/Levitate|levitate]]_, _[[spells/Minor Image|minor image]]_ (DC 19), _[[spells/Resist Energy|resist energy]]_, _[[spells/Sound Burst|sound burst]]_ (DC 19), _[[spells/Status|status]]_
1st (8/day)—_command_ (DC 18), _cure light wounds_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Sanctuary|sanctuary]]_ (DC 18), _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 17), _[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Guidance|guidance]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, stabilize
**Mystery **outer rifts

##### Statistics
**Str** 32, **Dex** 21, **Con** 31, **Int** 18, **Wis** 22, **Cha** 24
**Base Atk** +20; **CMB** +32; **CMD** 47
**Feats** _[[feats/Blinding Critical|Blinding Critical]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (_longsword_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +28 (+24 when jumping), Bluff +34, Fly +26, Knowledge (arcana) +31, Knowledge (religion) +31, Perception +41, Sense Motive +33, Spellcraft +25, Stealth +24
**Languages** Abyssal, Celestial, Common, Draconic, Varisian; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _oracle_’s curse (haunted), revelations (balefire [2/day], dread resilience, _[[items/Weapon Magic Abilities/Planar|planar]]_ haze [3/day], rift weapon [4/day], unearthly terrain [10/day]), _third eye_
**Gear** +4 _[[items/Armor/Chainmail|chainmail]]_, +4 _unholy_ _longsword_, crystal ball with _telepathy_, strand of _[[spells/Prayer|prayer]]_ beads

### Special Abilities

**_Command_ Avian (Su) **Uvaglor gains a +4 racial bonus on the save DC of charm or compulsion effects used against winged creatures.

**_Third Eye_ (Su)** Uvaglor’s _third eye_ sees a few seconds into the future. This grants him a +4 racial bonus on initiative checks and Reflex saves.

##### Description

In the ancient past, long before the rise of Azlant, during the near-mythical era known to scholars as the Age of Creation, two powerful demons met for the first time and descended to a world in the Material Plane to enjoy a short-lived but violently ardent dalliance in the mortal realm. The planet itself heaved and buckled before their blasphemous passions, thrusting upward to create a rasp-like ridge. The result of this vile union quickened much more quickly than a normal pregnancy, and the spawn of the two demons was birthed even as they continued their frolic. When the demons left the world, they left behind a landscape scarred by their coupling, and a just-whelped fiend of tremendous power and potential that slithered into a deep cave in the ridge to hide and grow.

Certain rare texts on demonology maintain that these two demons were none other than Lamashtu and Pazuzu, and that not long after their meeting their lusts turned to hatred. Today, there is no greater enmity in all the Abyss than the hostility between those two demon lords, and both of their cults deny vehemently that such an encounter as described above could ever have taken place.

And yet, the spawn of that union lived and grew, and in the Age of Anguish it emerged to conquer the Varisians even as they were beginning to recover from their slavery under Thassilon’s rule and the devastation of Earthfall. This fiend was Uvaglor, a vrock who possessed a singular _third eye_ in his brow that could see brief glimpses into the future. Uvaglor ruled the Varisians for many years until the desperate indigenous people invoked Lamashtu’s aid in defeating the demon. The Mother of Monsters seemed eager to comply with this request, but as the battle against Uvaglor went on, her minions turned on the Varisians and attempted to destroy them as well. Only the heroics of a priestess of the empyreal lord Ashava, a woman named Sazzleru, saved the people from annihilation and liberated them from Lamashtu’s inf luence while banishing Uvaglor from the Rasp into a nameless prison adrift deep in the Maelstrom.

Uvaglor lives on still, but only recently managed to escape from the nameless prison to return to the Abyss. After gathering his power, he has turned his attention once again to the site of his conception—the Lost Coast of Varisia, formed when the land west of the Rasp fell into the sea. Already he has installed several of his agents, including a mysterious _[[monsters/Mothman|mothman]]_ priest known as the Red Bishop, but his actions have attracted the attention of others who would rule this region, and this time, greater eyes than those of mortals look down upon this building conf lict. Lamashtu and Pazuzu’s interest in the region cannot be denied, and their _[[monsters/Unknown|unknown]]_ ultimate plans, as well as Uvaglor’s recent secret arrival in the region, portend dark times indeed.

Uvaglor prefers offerings of fine art depicting imagery of Ashava, or of clerics of that empyreal lord—works of art the vrock enjoys befouling and destroying in increasingly creative methods. It’s a DC 30 check to research the Misbegotten Prince.