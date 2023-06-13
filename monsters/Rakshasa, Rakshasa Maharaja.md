---
cssclass: [monsters]
title1: Rakshasa, Rakshasa Maharaja
desc_short: Impeccably dressed and bedecked in exotic jewelry, this fiend holds an
  ornate saber in its backward-facing hands.
title2: Rakshasa Maharaja
CR: 20
sources:
- name: Bestiary 3
  page: 226
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: 'Pathfinder #9: Escape from Old Korvosa'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/curseOfTheCrimsonThrone/v5748btpy82t5
XP: 307200
alignment: LE
size: Medium
type: outsider
subtypes:
- native
- rakshasa
- shapechanger
initiative:
  bonus: 13
senses:
  all-around vision: true
  darkvision: 60
AC:
  AC: 37
  touch: 24
  flat_footed: 27
  components:
    deflection: 4
    dex: 9
    dodge: 1
    natural: 13
HP:
  HP: 310
  long: 20d10+200
saves:
  fort: 16
  ref: 21
  will: 18
DR:
- amount: 20
  weakness: good and piercing
SR: 35
speeds:
  base: 40
  fly: 30
  fly_maneuverability: good
attacks:
  melee:
  - - text: +3 falchion +31/+26/+21/+16 (2d4+15/15-20)
      entries:
      - - damage: 2d4+15
          crit_range: 15-20
      attack: +3 falchion
      bonus:
      - 31
      - 26
      - 21
      - 16
    - text: 4 bites +23 (1d6+4)
      entries:
      - - damage: 1d6+4
      count: 4
      attack: bites
      bonus:
      - 23
  special:
  - detect thoughts (DC 29)
  - extra initiative
spell_like_abilities:
  entries:
  - name: comprehend languages
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: clairaudience/clairvoyance
    source: default
    freq: At will
  - name: dominate monster
    source: default
    freq: 1/day
    DC: 28
  sources:
  - name: default
    CL: 18
    concentration: 27
spells:
  entries:
  - name: weird
    source: '?'
    level: 9
    DC: 28
  - name: greater shadow evocation
    source: '?'
    level: 8
  - name: mind blank
    source: '?'
    level: 8
  - name: greater shadow conjuration
    source: '?'
    level: 7
  - name: mass invisibility
    source: '?'
    level: 7
  - name: spell turning
    source: '?'
    level: 7
  - name: greater dispel magic
    source: '?'
    level: 6
  - name: mass suggestion
    source: '?'
    level: 6
    DC: 25
  - name: true seeing
    source: '?'
    level: 6
  - name: baleful polymorph
    source: '?'
    level: 5
    DC: 24
  - name: feeblemind
    source: '?'
    level: 5
    DC: 24
  - name: mind fog
    source: '?'
    level: 5
    DC: 24
  - name: teleport
    source: '?'
    level: 5
  - name: charm monster
    source: '?'
    level: 4
    DC: 23
  - name: dimension door
    source: '?'
    level: 4
  - name: lesser globe of invulnerability
    source: '?'
    level: 4
  - name: scrying
    source: '?'
    level: 4
  - name: dispel magic
    source: '?'
    level: 3
  - name: nondetection
    source: '?'
    level: 3
  - name: suggestion
    source: '?'
    level: 3
    DC: 22
  - name: vampiric touch
    source: '?'
    level: 3
    DC: 22
  - name: darkness
    source: '?'
    level: 2
  - name: knock
    source: '?'
    level: 2
  - name: misdirection
    source: '?'
    level: 2
    DC: 21
  - name: resist energy
    source: '?'
    level: 2
  - name: see invisibility
    source: '?'
    level: 2
  - name: charm person
    source: '?'
    level: 1
    DC: 20
  - name: identify
    source: '?'
    level: 1
  - name: mage armor
    source: '?'
    level: 1
  - name: magic missile
    source: '?'
    level: 1
  - name: ventriloquism
    source: '?'
    level: 1
    DC: 20
  - name: arcane mark
    source: '?'
    level: 0
  - name: bleed
    source: '?'
    level: 0
    DC: 19
  - name: daze
    source: '?'
    level: 0
    DC: 19
  - name: detect magic
    source: '?'
    level: 0
  - name: ghost sound
    source: '?'
    level: 0
  - name: mage hand
    source: '?'
    level: 0
  - name: message
    source: '?'
    level: 0
  - name: prestidigitation
    source: '?'
    level: 0
  - name: read magic
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: known
    CL: 18
    concentration: 27
    slots:
      9: 4
      8: 6
      7: 7
      6: 7
      5: 8
      4: 8
      3: 8
      2: 8
      1: 9
      0: at-will
ability_scores:
  STR: 27
  DEX: 28
  CON: 30
  INT: 25
  WIS: 22
  CHA: 29
BAB: 20
CMB: 28
CMD: 52
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Hover
- name: Improved Critical (falchion)
- name: Improved Initiative
- name: Mobility
- name: Quicken Spell
- name: Silent Spell
- name: Still Spell
skills:
  Acrobatics: 27
    when jumping: 31
  Appraise: 25
  Bluff: 35
  Diplomacy: 30
  Disguise: 30
  Fly: 31
  Intimidate: 30
  Knowledge (arcana): 25
  Knowledge (history): 25
  Knowledge (nobility): 25
  Knowledge (religion): 25
  Perception: 31
  Sense Motive: 27
  Spellcraft: 25
  Stealth: 30
  _racial_mods:
    Bluff:
      _: 4
    Disguise:
      _: 8
    Perception:
      _: 4
languages:
- Abyssal
- Common
- Infernal
- Undercommon
- comprehend languages
- tongues
special_qualities:
- change shape (any humanoid; alter self)
ecology:
  environment: any
  organization: solitary
  treasure_type: double
  treasure:
  - +3 falchion
  - other treasure
special_abilities:
  Extra Initiative (Su): When an encounter starts, a maharaja rolls twice for initiative.
    The maharaja acts normally on the higher of the two initiative counts each round.
    On the lower initiative count, the maharaja can take a single standard action.
  Spells: A maharaja casts arcane spells as an 18th-level sorcerer.
desc_long: |-
  All rakshasas aspire to power, but there are those for whom this hunger is more than an obsession: It's a birthright. Legends among the rakshasas tell of the maharajas-those rakshasas whose depredations and acts of cruelty have elevated them above others of their kind and allowed them to reincarnate as embodiments of every myth, fable, and cautionary tale involving the beast-headed fiends. Accorded the respect and deference of their lessers, maharajas inspire one emotion within the rakshasa race that few can: fear.

  A maharaja rakshasa emerges only after a rakshasa of great power and influence has spent several lives as a member of the samrata, the height of the rakshasa's social-spiritual caste system. When a rakshasa ascends to maharaja status, others of its kind take notice, with rakshasas coming from far and wide to serve even a young maharaja-eager to curry its favor at an early age. The birth of a maharaja denotes that great change is imminent: The maharaja will fulfill some terrible destiny, found a lasting nation of rakshasas, undergo some manner of divine ascension, or defeat some greater foe and commandeer its domain, often splitting the region into large enough chunks for its lieutenants and servants to claim and still have room to expand. It is rare in the extreme for more than a handful of maharajas to emerge in the same century.

  So great is a maharaja's power and influence and so long is its life that one can spend most of its time enjoying the luxury of its years of toil. When not manipulating armies or the machinations of lesser rakshasas, it can often be found surrounded by the most beautiful of its servitors-often charmed or dominated humanoids, or, if the maharaja is powerful enough, good-aligned outsiders-lounging in opulence.

  The lair of a maharaja is typically a glorious, decadent mansion. After decades or centuries of work, gold filigree decorates the columns, and great friezes embossed with rakshasa myths and folklore decorate the walls. Rather than couches or divans, luxurious pillows stuffed with exotic feathers and crafted from the hides of even rarer creatures serve for furniture, and all about hang the trophies of a centuries-long life of tyranny: the crowns of defeated rulers, the wealth of ruined countries, and the heads of failed lieutenants.

  A maharaja's great experience and power, however, does not make it immune to or ignorant of threats. Disloyal servants, powerful kings, ambitious rivals, and meddling adventurers all might step forth to challenge a maharaja's rule. To that end, a maharaja employs devious methods to ensure its own safety, with assassination, false rumors, and illusory doubles serving as useful tools to ferret out threats. Wary of attack and often with wide territories to control, most rakshasa maharajas have several secluded palaces and lavish redoubts, and travel among them endlessly.

---

# Rakshasa, Rakshasa Maharaja
Impeccably dressed and bedecked in exotic _[[items/Mundane/Jewelry|jewelry]]_, this fiend holds an ornate saber in its backward-facing hands.
**Source** Bestiary 3 pg. 226, Pathfinder #9: Escape from Old Korvosa pg. 86
**XP** 307,200

LE Medium outsider (native, _[[monsters/Rakshasa|rakshasa]]_, shapechanger)
**Init** +13; **Senses** _[[universal monster rules/All-Around Vision|all-around vision]]_, _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +31

##### Defense

**AC** 37, touch 24, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+4 _[[spells/Deflection|deflection]]_, +9 Dex, +1 _[[feats/Dodge|dodge]]_, +13 natural)
**hp** 310 (20d10+200)
**Fort** +16, **Ref** +21, **Will** +18
**DR** 20/good and piercing; **SR** 35

##### Offense
**Speed** 40 ft., fly 30 ft. (good)
**Melee** +3 _[[items/Weapon/Falchion|falchion]]_ +31/+26/+21/+16 (2d4+15/15–20), 4 bites +23 (1d6+4)
**Special Attacks** _[[spells/Detect Thoughts|detect thoughts]]_ (DC 29), extra initiative
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +27)
Constant—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Tongues|tongues]]_
At will—clairaudience/clairvoyance
1/day—_[[spells/Dominate Monster|dominate monster]]_ (DC 28)
**Spells Known **(CL 18th; concentration +27)
9th (4/day)—_[[spells/Weird|weird]]_ (DC 28)
8th (6/day)—greater _[[spells/Shadow Evocation|shadow evocation]]_, _[[spells/Mind Blank|mind blank]]_
7th (7/day)—greater _[[spells/Shadow Conjuration|shadow conjuration]]_, mass _[[spells/Invisibility|invisibility]]_, _[[spells/Spell Turning|spell turning]]_
6th (7/day)—greater _[[spells/Dispel Magic|dispel magic]]_, mass _[[spells/Suggestion|suggestion]]_ (DC 25), _[[spells/True Seeing|true seeing]]_
5th (8/day)—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 24), _[[spells/Feeblemind|feeblemind]]_ (DC 24), _[[spells/Mind Fog|mind fog]]_ (DC 24), teleport
4th (8/day)—_[[spells/Charm Monster|charm monster]]_ (DC 23), _[[spells/Dimension Door|dimension door]]_, lesser _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, _[[spells/Scrying|scrying]]_
3rd (8/day)—_dispel magic_, _[[spells/Nondetection|nondetection]]_, _suggestion_ (DC 22), _[[spells/Vampiric Touch|vampiric touch]]_ (DC 22)
2nd (8/day)—_[[spells/Darkness|darkness]]_, _[[spells/Knock|knock]]_, _[[spells/Misdirection|misdirection]]_ (DC 21), _[[spells/Resist Energy|resist energy]]_, _[[spells/See Invisibility|see invisibility]]_
1st (9/day)—_[[spells/Charm Person|charm person]]_ (DC 20), _[[spells/Identify|identify]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 20)
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 19), _[[spells/Daze|daze]]_ (DC 19), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 27, **Dex** 28, **Con** 30, **Int** 25, **Wis** 22, **Cha** 29
**Base Atk** +20; **CMB** +28; **CMD** 52
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (_falchion_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Still Spell|Still Spell]]_
**Skills** Acrobatics +27 (+31 when jumping), Appraise +25, Bluff +35, Diplomacy +30, Disguise +30, Fly +31, Intimidate +30, Knowledge (arcana, history, nobility, religion) +25, Perception +31, Sense Motive +27, Spellcraft +25, Stealth +30; **Racial Modifiers** +4 Bluff, +8 Disguise, +4 Perception
**Languages** Abyssal, Common, Infernal, Undercommon; _comprehend languages_, _tongues_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (any humanoid; _[[spells/Alter Self|alter self]]_)

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** double (+3 _falchion_, other treasure)

### Special Abilities

**Extra Initiative (Su)** When an encounter starts, a maharaja rolls twice for initiative. The maharaja acts normally on the higher of the two initiative counts each round. On the lower initiative count, the maharaja can take a single standard action.
**Spells **A maharaja casts arcane spells as an 18th-level _[[classes/Sorcerer|sorcerer]]_.

##### Description

All rakshasas aspire to power, but there are those for whom this hunger is more than an obsession: It’s a birthright. Legends among the rakshasas tell of the maharajas—those rakshasas whose depredations and acts of _[[feats/Cruelty|cruelty]]_ have elevated them above others of their kind and allowed them to _[[spells/Reincarnate|reincarnate]]_ as embodiments of every myth, fable, and cautionary tale involving the beast-headed fiends. Accorded the respect and deference of their lessers, maharajas inspire one emotion within the _rakshasa_ race that few can: _[[universal monster rules/Fear|fear]]_.

A maharaja _rakshasa_ emerges only after a _rakshasa_ of great power and influence has spent several lives as a member of the samrata, the height of the _rakshasa_’s social-spiritual caste system. When a _rakshasa_ ascends to maharaja _[[spells/Status|status]]_, others of its kind take notice, with rakshasas coming from far and wide to serve even a young maharaja—eager to curry its favor at an early age. The birth of a maharaja denotes that great change is imminent: The maharaja will fulfill some terrible destiny, found a lasting nation of rakshasas, undergo some manner of divine _[[spells/Ascension|ascension]]_, or defeat some greater foe and commandeer its domain, often splitting the region into large enough chunks for its lieutenants and servants to claim and still have room to expand. It is rare in the extreme for more than a handful of maharajas to emerge in the same century.

So great is a maharaja’s power and influence and so long is its life that one can spend most of its time enjoying the luxury of its years of toil. When not manipulating armies or the machinations of lesser rakshasas, it can often be found surrounded by the most beautiful of its servitors—often charmed or dominated humanoids, or, if the maharaja is powerful enough, good-aligned outsiders—lounging in opulence.

The lair of a maharaja is typically a _[[items/Weapon Magic Abilities/Glorious|glorious]]_, decadent mansion. After decades or centuries of work, gold filigree decorates the columns, and great friezes embossed with _rakshasa_ myths and folklore decorate the walls. Rather than couches or divans, luxurious pillows stuffed with exotic feathers and crafted from the hides of even rarer creatures serve for furniture, and all about hang the trophies of a centuries-long life of tyranny: the crowns of defeated rulers, the wealth of ruined countries, and the heads of failed lieutenants.

A maharaja’s great experience and power, however, does not make it immune to or ignorant of threats. Disloyal servants, powerful kings, ambitious rivals, and meddling adventurers all might step forth to challenge a maharaja’s rule. To that end, a maharaja employs devious methods to ensure its own safety, with assassination, false rumors, and illusory doubles serving as useful tools to ferret out threats. Wary of attack and often with wide territories to control, most _rakshasa_ maharajas have several secluded palaces and lavish redoubts, and travel among them endlessly.