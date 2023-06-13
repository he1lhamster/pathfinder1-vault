---
cssclass: [monsters]
title1: Erotundee, Keeper of the Risen Light
desc_short: This wretched demon combines the worst features of a deformed boar and
  a repellent hag, then somehow manages to make things worse by decorating the whole
  with an ugly patchwork of scars and a rancidly obese body.
title2: Erotundee, Keeper of the Risen Light
CR: 22
sources:
- name: Demons Revisited
  page: 49
  link: http://paizo.com/products/btpy8yvo?Pathfinder-Campaign-Setting-Demons-Revisited
XP: 614400
race: Female
classes:
- nalfeshnee wizard 15 (Pathfinder RPG Bestiary 65)
alignment: CE
size: Huge
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 6
senses:
  darkvision: 60
  true seeing: true
auras:
- name: unholy aura
  DC: 28
AC:
  AC: 41
  touch: 17
  flat_footed: 38
  components:
    armor: 8
    deflection: 4
    dex: 2
    dodge: 1
    luck: 2
    natural: 16
    size: -2
HP:
  HP: 434
  long: 14d10+15d6+305
  HD: 29
saves:
  fort: 30
  ref: 19
  will: 30
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
SR: 25
speeds:
  base: 30
  fly: 40
  fly_maneuverability: poor
attacks:
  melee:
  - - text: staff of power +31/+26/+21/+16 (2d6+17/19-20)
      entries:
      - - damage: 2d6+17
          crit_range: 19-20
      attack: staff of power
      bonus:
      - 31
      - 26
      - 21
      - 16
    - text: bite +24 (3d8+5)
      entries:
      - - damage: 3d8+5
      attack: bite
      bonus:
      - 24
  special:
  - hand of the apprentice (16/day)
  - metamagic mastery (4/day)
  - unholy nimbus (DC 27)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 28
  - name: call lightning
    source: default
    freq: At will
    DC: 23
  - name: feeblemind
    source: default
    freq: At will
    DC: 25
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: slow
    source: default
    freq: At will
    DC: 23
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: nalfeshnee
      amount: 1
      chance: 20%
    - name: hezrous
      amount: 1d4
      chance: 40%
    - name: vrocks
      amount: 1d4
      chance: 50%
  sources:
  - name: default
    CL: 12
    concentration: 22
spells:
  entries:
  - name: quickened confusion
    source: Wizard
    level: 8
    DC: 27
  - name: demand
    source: Wizard
    level: 8
    DC: 31
  - name: scintillating pattern
    source: Wizard
    level: 8
  - name: quickened displacement
    source: Wizard
    level: 7
  - name: quickened lightning bolt
    source: Wizard
    level: 7
    DC: 26
  - name: prismatic spray
    source: Wizard
    level: 7
  - name: project image
    source: Wizard
    level: 7
    DC: 30
  - name: flesh to stone
    source: Wizard
    level: 6
    DC: 29
  - name: geas/quest
    source: Wizard
    level: 6
  - name: mass suggestion
    source: Wizard
    level: 6
    DC: 29
  - name: quickened mirror image
    source: Wizard
    level: 6
  - name: mislead
    source: Wizard
    level: 6
  - name: extended charm monster
    source: Wizard
    level: 5
    DC: 27
  - name: dominate person
    source: Wizard
    level: 5
    count: 2
    DC: 28
  - name: mind fog
    source: Wizard
    level: 5
    DC: 28
  - name: nightmare
    source: Wizard
    level: 5
    DC: 28
  - name: persistent image
    source: Wizard
    level: 5
    DC: 28
  - name: polymorph
    source: Wizard
    level: 5
  - name: bestow curse
    source: Wizard
    level: 4
    DC: 27
  - name: charm monster
    source: Wizard
    level: 4
    count: 2
    DC: 27
  - name: dimensional anchor
    source: Wizard
    level: 4
  - name: greater invisibility
    source: Wizard
    level: 4
  - name: extended haste
    source: Wizard
    level: 4
  - name: phantasmal killer
    source: Wizard
    level: 4
    count: 2
    DC: 27
  - name: rainbow pattern
    source: Wizard
    level: 4
    DC: 27
  - name: resilient sphere
    source: Wizard
    level: 4
    DC: 27
  - name: scrying
    source: Wizard
    level: 4
    DC: 27
  - name: extended alter self
    source: Wizard
    level: 3
    count: 2
  - name: beast shape I
    source: Wizard
    level: 3
  - name: hold person
    source: Wizard
    level: 3
    DC: 26
  - name: major image
    source: Wizard
    level: 3
    DC: 26
  - name: nondetection
    source: Wizard
    level: 3
  - name: suggestion
    source: Wizard
    level: 3
    DC: 26
  - name: alter self
    source: Wizard
    level: 2
  - name: detect thoughts
    source: Wizard
    level: 2
    DC: 25
  - name: invisibility
    source: Wizard
    level: 2
  - name: minor image
    source: Wizard
    level: 2
    DC: 25
  - name: misdirection
    source: Wizard
    level: 2
  - name: scorching ray
    source: Wizard
    level: 2
    count: 2
  - name: charm person
    source: Wizard
    level: 1
    count: 2
    DC: 24
  - name: magic missile
    source: Wizard
    level: 1
    count: 4
  - name: reduce person
    source: Wizard
    level: 1
    DC: 24
  - name: silent image
    source: Wizard
    level: 1
    DC: 24
  - name: bleed
    source: Wizard
    level: 0
    DC: 23
  - name: dancing lights
    source: Wizard
    level: 0
  - name: ghost sound
    source: Wizard
    level: 0
    DC: 23
  - name: message
    source: Wizard
    level: 0
  sources:
  - name: Wizard
    type: prepared
    CL: 15
    concentration: 28
    slots:
      0: at-will
ability_scores:
  STR: 30
  DEX: 15
  CON: 31
  INT: 36
  WIS: 22
  CHA: 30
BAB: 21
CMB: 33
CMB_other: +35 bull rush
CMD: 50
CMD_other: 52 vs. bull rush
feats:
- name: Arcane Strike
- name: Awesome Blow
- name: Combat Expertise
- name: Craft Construct
- name: Craft Magic Arms and Armor
- name: Craft Rod
- name: Craft Staff
- name: Craft Wondrous Item
- name: Dodge
- name: Eschew Materials
- name: Extend Spell
- name: Greater Spell Penetration
- name: Improved Bull Rush
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- name: Quicken Spell
- name: Scribe Scroll
- name: Spell Penetration
skills:
  Bluff: 42
  Diplomacy: 42
  Fly: 24
  Intimidate: 42
  Knowledge (arcana): 45
  Knowledge (dungeoneering): 45
  Knowledge (engineering): 45
  Knowledge (history): 45
  Knowledge (local): 45
  Knowledge (nature): 45
  Knowledge (nobility): 45
  Knowledge (planes): 45
  Knowledge (religion): 45
  Perception: 46
  Sense Motive: 38
  Spellcraft: 45
  Use Magic Device: 39
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
special_qualities:
- arcane bond (ring of wizardry IV)
gear:
  combat:
  - staff of power
  other:
  - bracers of armor +8
  - headband of mental prowess +6 (Int
  - Cha
desc_long: |-
  The city of Vantian is one of the great wonders of the planes-a massive sprawl perched along a constantly crumbling cliffside above a turbulent ocean. Ruled by Sif kesh, the demon lord of suicide, Vantian is forever being rebuilt by its denizens as portions of the city tumble away into the surf. As a result, very few buildings in Vantian qualify as truly old, since a building constructed at the city's inland-creeping edge will generally tumble into the sea within a decade.

  Some of Vantian's inhabitants have found ways to secure homes of a more permanent type, even without access to Sifkesh's power to maintain her palace at the everchanging heart of the city while the rest of its streets and structures slowly “flow” around this one island of stability. One of the most iconic structures of the Abyssal city is the towering 20-story spire known as the Risen Light.

  This structure is something akin to a lighthouse in shape and function, save that the pale green light shining from its apex does not ward ships away from treacherous coastlines; rather, it warns Vantian's coastal citizens, through the pulsing and flaring of its radiances, of neighborhoods about to crumble into the ocean. The tower itself does not rest upon the ground, but rather floats in the air hundreds of feet above the waves. Rootlike tangles of iron extend from the tower's base, to which are attached immense chains anchored to huge piercings of cold iron that decorate the backs of a dozen retrievers that cling to the city's edge, crawling forward and towing the tower behind them as necessary to keep the Light attached to the city.

  This singular site is the lair of one of Vantian's most dangerous and knowledgeable denizens-a nalfeshnee crone named Erotundee. This ancient demon keeps track of Vantian's suicides in an endless scroll crafted from the flesh of countless virginal lovers who died of their own hand before consummating their desires. That Erotundee manages to keep this list accurate while studying her ever-growing library of heretical and apocryphal religious texts is a testament to her obsessive qualities. She does not suffer visitors to the Light, and any who would seek her advice must first brave the lower 20 floors of the tower and its frightening guardians before reaching her inner sanctum near the tower's peak-simply approaching the tower from the top is as sure an invitation for destruction as any in Vantian.

  Those who would seek to conjure Erotundee must use a gate spell to work such a mighty feat. She prefers offerings of heretical writings or rare religious texts, particularly those that hold secrets their faiths would rather see redacted. It's a DC 32 check to research the Keeper of the Risen Light.

---

# Erotundee, Keeper of the Risen Light
This wretched demon combines the worst features of a deformed _[[monsters/Boar|boar]]_ and a repellent hag, then somehow manages to make things worse by decorating the whole with an ugly patchwork of scars and a rancidly obese body.
**Source** Demons Revisited pg. 49
**XP** 614,400
Female nalfeshnee _[[classes/Wizard|wizard]]_ 15 (Pathfinder RPG Bestiary 65)
CE Huge outsider (chaotic, demon, evil, extraplanar)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +46
**Aura** _[[spells/Unholy Aura|unholy aura]]_ (DC 28)

##### Defense

**AC** 41, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 38 (+8 armor, +4 deflection, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +2 luck, +16 natural, –2 size)
**hp** 434 (29 HD; 14d10+15d6+305)
**Fort** +30, **Ref** +19, **Will** +30
**DR** 10/good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 25

##### Offense
**Speed** 30 ft., fly 40 ft. (poor)
**Melee** _[[items/Staff/Staff of Power|staff of power]]_ +31/+26/+21/+16 (2d6+17/19–20), bite +24 (3d8+5)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** hand of the apprentice (16/day), metamagic mastery (4/day), _[[items/Weapon Magic Abilities/Unholy|unholy]]_ nimbus (DC 27)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +22)
Constant—_true seeing_, _unholy aura_ (DC 28)
At will—_[[spells/Call Lightning|call lightning]]_ (DC 23), _[[spells/Feeblemind|feeblemind]]_ (DC 25), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Slow|slow]]_ (DC 23)
1/day—_[[universal monster rules/Summon|summon]]_ (level 5, 1 nalfeshnee 20%, 1d4 hezrous 40%, or 1d4 vrocks 50%)
**_Wizard_ Spells Prepared **(CL 15th; concentration +28)
8th—quickened _[[spells/Confusion|confusion]]_ (DC 27), _[[spells/Demand|demand]]_ (DC 31), _[[spells/Scintillating Pattern|scintillating pattern]]_
7th—quickened _[[spells/Displacement|displacement]]_, quickened _[[spells/Lightning Bolt|lightning bolt]]_ (DC 26), _[[spells/Prismatic Spray|prismatic spray]]_, _[[spells/Project Image|project image]]_ (DC 30)
6th—_[[spells/Flesh to Stone|flesh to stone]]_ (DC 29), geas/quest, mass _[[spells/Suggestion|suggestion]]_ (DC 29), quickened _[[spells/Mirror Image|mirror image]]_, _[[spells/Mislead|mislead]]_
5th—extended _[[spells/Charm Monster|charm monster]]_ (DC 27), _[[spells/Dominate Person|dominate person]]_ (2, DC 28), _[[spells/Mind Fog|mind fog]]_ (DC 28), _[[spells/Nightmare|nightmare]]_ (DC 28), _[[spells/Persistent Image|persistent image]]_ (DC 28), _[[spells/Polymorph|polymorph]]_
4th—_[[spells/Bestow Curse|bestow curse]]_ (DC 27), _charm monster_ (2, DC 27), _[[spells/Dimensional Anchor|dimensional anchor]]_, greater _[[spells/Invisibility|invisibility]]_, extended _[[spells/Haste|haste]]_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (2, DC 27), _[[spells/Rainbow Pattern|rainbow pattern]]_ (DC 27), _[[spells/Resilient Sphere|resilient sphere]]_ (DC 27), _[[spells/Scrying|scrying]]_ (DC 27)
3rd—extended _[[spells/Alter Self|alter self]]_ (2), _[[spells/Beast Shape I|beast shape I]]_, _[[spells/Hold Person|hold person]]_ (DC 26), _[[spells/Major Image|major image]]_ (DC 26), _[[spells/Nondetection|nondetection]]_, _suggestion_ (DC 26)
2nd—_alter self_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 25), _invisibility_, _[[spells/Minor Image|minor image]]_ (DC 25), _[[spells/Misdirection|misdirection]]_, _[[spells/Scorching Ray|scorching ray]]_ (2)
1st—_[[spells/Charm Person|charm person]]_ (2, DC 24), _[[spells/Magic Missile|magic missile]]_ (4), _[[spells/Reduce Person|reduce person]]_ (DC 24), _[[spells/Silent Image|silent image]]_ (DC 24)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 23), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 23), _[[spells/Message|message]]_

##### Statistics
**Str** 30, **Dex** 15, **Con** 31, **Int** 36, **Wis** 22, **Cha** 30
**Base Atk** +21; **CMB** +33 (+35 bull rush); **CMD** 50 (52 vs. bull rush)
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Craft Construct|Craft Construct]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Rod|Craft Rod]]_, _[[feats/Craft Staff|Craft Staff]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Greater Spell Penetration|Greater Spell Penetration]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Penetration|Spell Penetration]]_
**Skills** Bluff +42, Diplomacy +42, Fly +24, Intimidate +42, Knowledge (arcana) +45, Knowledge (dungeoneering) +45, Knowledge (engineering) +45, Knowledge (history) +45, Knowledge (local) +45, Knowledge (nature) +45, Knowledge (nobility) +45, Knowledge (planes) +45, Knowledge (religion) +45, Perception +46, Sense Motive +38, Spellcraft +45, Use Magic Device +39
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** arcane bond (ring of wizardry IV)
**Combat Gear** _staff of power_; **Other Gear** _[[items/Wondrous Item/Bracers of Armor +8|bracers of armor +8]]_, _[[items/Wondrous Item/Headband of Mental Prowess +6|headband of mental prowess +6]]_ (Int, Cha

##### Description

The city of Vantian is one of the great wonders of the planes—a massive sprawl perched along a constantly crumbling cliffside above a turbulent ocean. Ruled by Sif kesh, the demon lord of suicide, Vantian is forever being rebuilt by its denizens as portions of the city tumble away into the surf. As a result, very few buildings in Vantian qualify as truly old, since a building constructed at the city’s inland-creeping edge will generally tumble into the sea within a decade.

Some of Vantian’s inhabitants have found ways to secure homes of a more permanent type, even without access to Sifkesh’s power to maintain her palace at the everchanging heart of the city while the rest of its streets and structures slowly “flow” around this one island of stability. One of the most iconic structures of the Abyssal city is the towering 20-story spire known as the Risen Light.

This structure is something akin to a lighthouse in shape and function, save that the pale green light shining from its apex does not ward ships away from treacherous coastlines; rather, it warns Vantian’s coastal citizens, through the pulsing and flaring of its radiances, of neighborhoods about to crumble into the ocean. The tower itself does not rest upon the ground, but rather floats in the air hundreds of feet above the waves. Rootlike tangles of iron extend from the tower’s base, to which are attached immense chains anchored to huge piercings of cold iron that decorate the backs of a dozen retrievers that cling to the city’s edge, crawling forward and towing the tower behind them as necessary to keep the Light attached to the city.

This singular site is the lair of one of Vantian’s most dangerous and knowledgeable denizens—a nalfeshnee crone named Erotundee. This ancient demon keeps track of Vantian’s suicides in an endless scroll crafted from the flesh of countless virginal lovers who died of their own hand before consummating their desires. That Erotundee manages to keep this list accurate while studying her ever-growing library of _[[items/Weapon Magic Abilities/Heretical|heretical]]_ and apocryphal religious texts is a testament to her obsessive qualities. She does not suffer visitors to the Light, and any who would seek her advice must first brave the lower 20 floors of the tower and its frightening guardians before reaching her inner sanctum near the tower’s peak—simply approaching the tower from the top is as sure an invitation for _[[spells/Destruction|destruction]]_ as any in Vantian.

Those who would seek to conjure Erotundee must use a _[[spells/Gate|gate]]_ spell to work such a mighty feat. She prefers offerings of _heretical_ writings or rare religious texts, particularly those that hold secrets their faiths would rather see redacted. It’s a DC 32 check to research the Keeper of the Risen Light.