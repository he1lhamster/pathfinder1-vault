---
cssclass: [monsters]
title1: Fastachee
desc_short: This gaunt, two-foot-tall humanoid figure appears made of corn husks,
  and carries an oversized basket filled with corn.
title2: Fastachee
CR: 11
sources:
- name: Bestiary 5
  page: 114
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 12800
alignment: NG
size: Tiny
type: fey
initiative:
  bonus: 10
senses:
  low-light vision: true
  plant projection: true
AC:
  AC: 26
  touch: 18
  flat_footed: 20
  components:
    dex: 6
    natural: 8
    size: 2
HP:
  HP: 153
  long: 18d6+90
saves:
  fort: 12
  ref: 17
  will: 17
DR:
- amount: 10
  weakness: cold iron
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 vines +18 (1d8-2)
      entries:
      - - damage: 1d8-2
      count: 2
      attack: vines
      bonus:
      - 18
space: 2.5
reach: 0
reach_other: 30 ft. with vines
spell_like_abilities:
  entries:
  - name: plant growth
    source: default
    freq: At will
  - name: speak with plants
    source: default
    freq: At will
  - name: thorny entanglement
    source: default
    freq: At will
    DC: 16
  - name: transport via plants
    source: default
    freq: At will
  - name: rebuke death
    source: domain
    freq: 9/day
    other: 1d4+5
  sources:
  - name: default
    CL: 11
    concentration: 15
  - name: domain
    CL: 11
    concentration: 17
spells:
  entries:
  - name: greater dispel magic
    source: Druid
    level: 6
  - is_domain_spell: true
    name: heal
    source: Druid
    level: 6
  - name: mass bear's endurance
    source: Druid
    level: 6
  - name: baleful polymorph
    source: Druid
    level: 5
    DC: 21
  - is_domain_spell: true
    name: breath of life
    source: Druid
    level: 5
  - name: commune with nature
    source: Druid
    level: 5
  - name: wall of thorns
    source: Druid
    level: 5
  - name: command plants
    source: Druid
    level: 4
    DC: 20
  - is_domain_spell: true
    name: cure critical wounds
    source: Druid
    level: 4
  - name: flame strike
    source: Druid
    level: 4
    DC: 20
  - name: freedom of movement
    source: Druid
    level: 4
  - name: spike stones
    source: Druid
    level: 4
    DC: 20
  - name: aqueous orb
    source: Druid
    level: 3
    DC: 20
  - name: call lightning
    source: Druid
    level: 3
    DC: 19
  - is_domain_spell: true
    name: cure serious wounds
    source: Druid
    level: 3
  - name: protection from energy
    source: Druid
    level: 3
  - name: remove disease
    source: Druid
    level: 3
  - name: spike growth
    source: Druid
    level: 3
    DC: 19
  - name: barkskin
    source: Druid
    level: 2
  - name: cat's grace
    source: Druid
    level: 2
  - is_domain_spell: true
    name: cure moderate wounds
    source: Druid
    level: 2
  - name: flaming sphere
    source: Druid
    level: 2
    DC: 18
  - name: lesser restoration
    source: Druid
    level: 2
  - name: soften earth and stone
    source: Druid
    level: 2
  - name: tree shape
    source: Druid
    level: 2
  - name: ant haul
    source: Druid
    level: 1
  - is_domain_spell: true
    name: cure light wounds
    source: Druid
    level: 1
  - name: endure elements
    source: Druid
    level: 1
  - name: faerie fire
    source: Druid
    level: 1
  - name: goodberry
    source: Druid
    level: 1
  - name: longstrider
    source: Druid
    level: 1
  - name: obscuring mist
    source: Druid
    level: 1
  - name: create water
    source: Druid
    level: 0
  - name: detect magic
    source: Druid
    level: 0
  - name: purify food and drink
    source: Druid
    level: 0
  - name: stabilize
    source: Druid
    level: 0
  sources:
  - name: Druid
    type: prepared
    CL: 11
    concentration: 17
    domains:
    - healing
ability_scores:
  STR: 6
  DEX: 23
  CON: 18
  INT: 19
  WIS: 22
  CHA: 17
BAB: 9
CMB: 13
CMD: 21
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Great Fortitude
- name: Improved Initiative
- name: Skill Focus (Heal)
- name: Spell Focus (conjuration)
- name: Toughness
- name: Weapon Finesse
- name: Weapon Focus (vines)
skills:
  Acrobatics: 27
  Craft (alchemy): 25
  Escape Artist: 27
  Heal: 30
  Knowledge (arcana): 22
  Knowledge (nature): 25
  Perception: 27
  Sense Motive: 27
  Spellcraft: 22
  Survival: 24
languages:
- Common
- Sylvan
special_qualities:
- bountiful basket
- healer's blessing
- sow corn
ecology:
  environment: any temperate land
  organization: solitary or court (1 plus 2-26 other good-aligned fey)
  treasure_type: double
special_abilities:
  Bountiful Basket (Su): A fastachee carries a basket full of corn. Once per minute
    as a standard action, a fastachee can refill its basket with 2d6+12 ears of corn.
  Plant Projection (Su): At will as a full-round action, a fastachee can project its
    senses through every non-creature plant within a radius of 1 mile per HD simultaneously.
    While projecting its senses in this way, the fastachee is flat-footed and can
    take no other actions. Alternatively, a fastachee can project its senses through
    a single ear of corn within 1 mile per HD as a free action. It continues projecting
    in this way for 1 round. The fastachee can treat either the corn plant it's projecting
    through or its own body as the origin point for any of its spells or spell-like
    abilities.
  Sow Corn (Su): As a standard action, a fastachee can plant an ear of corn in the
    ground to cause a stand of 1d6 corn stalks to grow to full height and maturity
    in the span of 1 minute.
  Spells: A fastachee can cast spells as an 11th-level druid, and can spontaneously
    swap out any prepared druid spell for the summon nature's ally spell of the same
    level. A fastachee also gains access to all spells and powers of the healing domain
    as an 11th-level cleric.
desc_long: Fastachees are mysterious, wise, and generous fey who foster the growth
  of nearby plants. Many communities who interact with them revere them as bringers
  of food and medicine, as well as protectors of crops. These fey have a particularly
  strong connection to corn; they regularly project their senses through corn plants
  to monitor the health of the field and search the local area for threats. They prefer
  to avoid direct confrontation if possible, using their ability to originate their
  spells from corn plants to harass those they wish to chase away.

---

# Fastachee
This gaunt, two-foot-tall humanoid figure appears made of corn husks, and carries an oversized _[[items/Mundane/Basket|basket]]_ filled with corn.
**Source** Bestiary 5 pg. 114
**XP** 12,800

NG Tiny fey
**Init** +10; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, plant projection; Perception +27

##### Defense

**AC** 26, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+6 Dex, +8 natural, +2 size)
**hp** 153 (18d6+90)
**Fort** +12, **Ref** +17, **Will** +17
**DR** 10/cold iron

##### Offense
**Speed** 30 ft.
**Melee** 2 vines +18 (1d8–2)
**Space** 2-1/2 ft., **Reach** 0 ft. (30 ft. with vines)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +15)
At will—_[[spells/Plant Growth|plant growth]]_, _[[spells/Speak with Plants|speak with plants]]_, _[[spells/Thorny Entanglement|thorny entanglement]]_ (DC 16), _[[spells/Transport via Plants|transport via plants]]_
 **Domain _Spell-Like Abilities_** (CL 11th; concentration +17)
 9/day—_[[spells/Rebuke|rebuke]]_ death (1d4+5)
**_[[classes/Druid|Druid]]_ Spells Prepared** (CL 11th; concentration +17)
6th—greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Heal, Mass|heal, mass]]_ bear’s _[[feats/Endurance|endurance]]_
5th—_[[spells/Baleful Polymorph|baleful polymorph]]_ (DC 21), _[[spells/Breath Of Life|breath of life]]_, _[[spells/Commune with Nature|commune with nature]]_, _[[spells/Wall Of Thorns|wall of thorns]]_
4th—_[[spells/Command Plants|command plants]]_ (DC 20), _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Flame Strike|flame strike]]_ (DC 20), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Spike Stones|spike stones]]_ (DC 20)
3rd—_[[spells/Aqueous Orb|aqueous orb]]_ (DC 20), _[[spells/Call Lightning|call lightning]]_ (DC 19), _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Remove Disease|remove disease]]_, _[[spells/Spike Growth|spike growth]]_ (DC 19)
2nd—_[[spells/Barkskin|barkskin]]_, cat’s _[[spells/Grace|grace]]_, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Flaming Sphere|flaming sphere]]_ (DC 18), lesser _[[spells/Restoration|restoration]]_, _[[spells/Soften Earth and Stone|soften earth and stone]]_, _[[spells/Tree Shape|tree shape]]_
1st—_[[spells/Ant Haul|ant haul]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Endure Elements|endure elements]]_, _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Goodberry|goodberry]]_, _[[spells/Longstrider|longstrider]]_, _[[spells/Obscuring Mist|obscuring mist]]_
0—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Purify Food and Drink|purify food and drink]]_, stabilize
**D** domain spell; **Domain** Healing

##### Statistics
**Str** 6, **Dex** 23, **Con** 18, **Int** 19, **Wis** 22, **Cha** 17
**Base Atk** +9; **CMB** +13; **CMD** 21
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Skill Focus|Skill Focus]]_ (_[[spells/Heal|Heal]]_), _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (vines)
**Skills** Acrobatics +27, Craft (alchemy) +25, Escape Artist +27, _Heal_ +30, Knowledge (arcana) +22, Knowledge (nature) +25, Perception +27, Sense Motive +27, Spellcraft +22, Survival +24
**Languages** Common, Sylvan
**SQ** bountiful _basket_, _[[npcs/Healer|healer]]_’s blessing, sow corn

##### Ecology

**Environment** any temperate land
**Organization** solitary or court (1 plus 2–26 other good–aligned fey)
**Treasure** double

### Special Abilities

**Bountiful _Basket_ (Su)** A _[[monsters/Fastachee|fastachee]]_ carries a _basket_ full of corn. Once per minute as a standard action, a _fastachee_ can refill its _basket_ with 2d6+12 ears of corn.

**Plant Projection (Su)** At will as a full-round action, a _fastachee_ can project its senses through every non-creature plant within a radius of 1 mile per HD simultaneously. While projecting its senses in this way, the _fastachee_ is _flat-footed_ and can take no other actions. Alternatively, a _fastachee_ can project its senses through a single ear of corn within 1 mile per HD as a free action. It continues projecting in this way for 1 round. The _fastachee_ can treat either the corn plant it’s projecting through or its own body as the origin point for any of its spells or _spell-like abilities_.
**Sow Corn (Su)** As a standard action, a _fastachee_ can plant an ear of corn in the ground to cause a stand of 1d6 corn stalks to grow to full height and maturity in the span of 1 minute.
**Spells** A _fastachee_ can cast spells as an 11th-level _druid_, and can spontaneously swap out any prepared _druid_ spell for the _[[universal monster rules/Summon|summon]]_ nature’s ally spell of the same level. A _fastachee_ also gains access to all spells and powers of the healing domain as an 11th-level _[[classes/Cleric|cleric]]_.

##### Description

Fastachees are mysterious, wise, and generous fey who foster the growth of nearby plants. Many communities who interact with them revere them as bringers of food and medicine, as well as protectors of crops. These fey have a particularly strong connection to corn; they regularly project their senses through corn plants to monitor the health of the field and search the local area for threats. They prefer to avoid direct confrontation if possible, using their ability to originate their spells from corn plants to harass those they _[[spells/Wish|wish]]_ to chase away.