---
cssclass: [monsters]
title1: Couatl, Chicome
desc_short: The feathers of this winged serpent are hues of verdant green, save for
  the crimson feathers on its head and crest. Its wings let forth thin clouds of golden
  pollen and showers of dew.
title2: Chicome
CR: 16
sources:
- name: "Pathfinder #143: Borne by the Sun's Grace"
  page: 82
  link: https://paizo.com/products/btq01vyh
XP: 76800
alignment: LG
size: Huge
type: outsider
subtypes:
- native
initiative:
  bonus: 9
senses:
  darkvision: 120
  '': true
  detect chaos/evil/good/law: true
auras:
- name: resplendence
  other:
  - 1/2 mile
AC:
  AC: 31
  touch: 14
  flat_footed: 25
  components:
    dex: 5
    dodge: 1
    natural: 17
    size: -2
HP:
  HP: 250
  long: 20d10+140
saves:
  fort: 13
  ref: 19
  will: 21
DR:
- amount: 10
  weakness: cold iron or evil
immunities:
- acid
- disease
- poison
resistances:
  cold: 15
  electricity: 15
  fire: 15
SR: 28
speeds:
  base: 30
  fly: 120
  fly_maneuverability: poor
attacks:
  melee:
  - - text: bite +28 (2d8+15 plus grab and poison)
      entries:
      - - damage: 2d8+15
        - effect: grab
        - effect: poison
      attack: bite
      bonus:
      - 28
  special:
  - constrict (2d8+10)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: detect chaos
    source: default
    freq: Constant
  - name: detect evil
    source: default
    freq: Constant
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 19
  - name: ethereal jaunt
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
  - name: plane shift
    source: default
    freq: At will
    DC: 24
  - name: reincarnate
    source: default
    freq: 1/week
  sources:
  - name: default
    CL: 18
    concentration: 26
spells:
  entries:
  - name: antipathy
    source: '?'
    level: 9
    DC: 28
  - name: regenerate
    source: '?'
    level: 9
  - name: summon nature's ally IX
    source: '?'
    level: 9
  - name: control plants
    source: '?'
    level: 8
    DC: 27
  - name: mass cure serious wounds
    source: '?'
    level: 8
  - name: repel metal or stone
    source: '?'
    level: 8
  - name: whirlwind
    source: '?'
    level: 8
    DC: 27
  - name: animate plants
    source: '?'
    level: 7
  - name: control weather
    source: '?'
    level: 7
  - name: heal
    source: '?'
    level: 7
  - name: transmute metal to wood
    source: '?'
    level: 7
  - name: greater dispel magic
    source: '?'
    level: 6
  - name: liveoak
    source: '?'
    level: 6
  - name: move earth
    source: '?'
    level: 6
  - name: transport via plants
    source: '?'
    level: 6
  - name: wall of stone
    source: '?'
    level: 6
  - name: animal growth
    source: '?'
    level: 5
    DC: 24
  - name: awaken
    source: '?'
    level: 5
    DC: 24
  - name: commune with nature
    source: '?'
    level: 5
  - name: control winds
    source: '?'
    level: 5
    DC: 24
  - name: hallow
    source: '?'
    level: 5
  - name: wall of thorns
    source: '?'
    level: 5
  - name: antiplant shell
    source: '?'
    level: 4
  - name: command plants
    source: '?'
    level: 4
    DC: 23
  - name: control water
    source: '?'
    level: 4
  - name: dispel magic
    source: '?'
    level: 4
  - name: freedom of movement
    source: '?'
    level: 4
  - name: repel vermin
    source: '?'
    level: 4
  - name: daylight
    source: '?'
    level: 3
  - name: dominate animal
    source: '?'
    level: 3
    DC: 22
  - name: neutralize poison
    source: '?'
    level: 3
  - name: quench
    source: '?'
    level: 3
    DC: 22
  - name: remove disease
    source: '?'
    level: 3
  - name: speak with plants
    source: '?'
    level: 3
  - name: animal messenger
    source: '?'
    level: 2
  - name: gust of wind
    source: '?'
    level: 2
    DC: 21
  - name: lesser restoration
    source: '?'
    level: 2
  - name: soften earth and stone
    source: '?'
    level: 2
  - name: warp wood
    source: '?'
    level: 2
    DC: 21
  - name: wood shape
    source: '?'
    level: 2
    DC: 21
  - name: calm animals
    source: '?'
    level: 1
    DC: 20
  - name: charm animal
    source: '?'
    level: 1
    DC: 20
  - name: detect animals or plants
    source: '?'
    level: 1
  - name: entangle
    source: '?'
    level: 1
    DC: 20
  - name: faerie fire
    source: '?'
    level: 1
  - name: obscuring mist
    source: '?'
    level: 1
  - name: speak with animals
    source: '?'
    level: 1
  - name: create water
    source: '?'
    level: 0
  - name: detect magic
    source: '?'
    level: 0
  - name: know direction
    source: '?'
    level: 0
  - name: purify food and drink
    source: '?'
    level: 0
    DC: 19
  sources:
  - name: '?'
    type: prepared
    CL: 18
    concentration: 27
    slots:
      0: at-will
ability_scores:
  STR: 30
  DEX: 20
  CON: 25
  INT: 18
  WIS: 29
  CHA: 27
BAB: 20
CMB: 32
CMB_other: +36 grapple
CMD: 48
CMD_other: can't be tripped
feats:
- name: Alertness
- name: Dodge
- name: Empower Spell
- is_bonus: true
  name: Eschew Materials
- name: Hover
- name: Improved Initiative
- name: Lightning Reflexes
- name: Natural Spell
- name: Spell Penetration
- name: Widen Spell
- name: Wingover
skills:
  Bluff: 31
  Fly: 20
  Intimidate: 31
  Knowledge (geography): 27
  Knowledge (nature): 27
  Perception: 36
  Sense Motive: 36
  Spellcraft: 24
  Stealth: 20
  Survival: 32
languages:
- Celestial
- Common
- Draconic
- Druidic
- telepathy 100 ft.
special_qualities:
- natural form
- wild empathy +32
ecology:
  environment: warm badlands or ruins
  organization: solitary
  treasure_type: standard
special_abilities:
  Aura of Resplendence (Sp): A chicome constantly radiates an aura of plant growth,
    as the spell, providing enrichment to plants within a half-mile radius. The chicome
    can suppress or resume the aura as a free action.
  Natural Form (Sp): Once per day as a standard action, a chicome can take the form
    of any animal, dragon, magical beast, or vermin with 18 Hit Dice or fewer. This
    functions as if using beast shape IV, form of the dragon III, magical beast shape,
    or vermin shape II, as appropriate, and otherwise counts as a druid's wild shape
    ability for the purposes of abilities and prerequisites. The chicome can maintain
    this form indefinitely and can end the transformation as a free action.
  Poison (Ex): Injury-bite; save Fort DC 27; frequency 1/minute for 10 minutes; effect
    2d4 Str; cure 2 consecutive saves.
  Spells: A chicome casts spells as an 18th-level druid, but cannot swap out prepared
    spells to cast summon spells.
  Wild Empathy (Su): This works like the druid's wild empathy class feature, except
    the chicome has a +6 racial bonus on the check. The chicome's effective druid
    level is 18 for the purpose of determining its total modifier to the check.
desc_long: |-
  Chicomes are a powerful but gentle variety of couatl- winged serpentine outsiders who act as agents of lawful good deities-whose purpose is to reestablish nature in destroyed and ravaged lands, especially those that have been recently cleansed of evil. Chicomes accomplish this by way of powerful druidic magic and the cloud of restorative pollen and dew that constantly drifts from their wings. Like other couatls, chicomes have varicolored feathers and beautiful, glossy scales. The couatls' wing feathers are typically shades of green or brown, but their crests are always a brilliant crimson. Like for other couatls, the feathers of chicomes are incredibly powerful magic items when bestowed upon chosen mortals. Such a freely given feather can be used as the material component for a planar ally spell. In addition, if buried in at least 6 inches of soil and undisturbed for 24 hours, the feather can be used as the material component to cast a hallow spell; the spell effect tied to the hallowed site is always the enrichment version of plant growth. By using a chicome feather in this way, the caster need not expend the typical payment of gold or other valuables required by the spell.

   A typical chicome is 40 feet long with a wingspan of 30 feet and weighs 5,500 pounds.

---

# Couatl, Chicome
The feathers of this winged serpent are hues of verdant green, save for the crimson feathers on its head and crest. Its wings let forth thin clouds of golden pollen and showers of dew.
**Source** Pathfinder #143: Borne by the Sun's _[[spells/Grace|Grace]]_ pg. 82
**XP** 76,800

LG Huge outsider (native)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., ,detect chaos/evil/good/law; Perception +36
**Aura** resplendence (1/2 mile)

##### Defense

**AC** 31, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+5 Dex, +1 dodge, +17 natural, –2 size)
**hp** 250 (20d10+140)
**Fort** +13, **Ref** +19, **Will** +21
**DR** 10/cold iron or evil; **Immune** acid, disease, poison; **Resist** cold 15, electricity 15, fire 15; **SR** 28

##### Offense
**Speed** 30 ft., fly 120 ft. (poor)
**Melee** bite +28 (2d8+15 plus _[[universal monster rules/Grab|grab]]_ and poison)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** _[[universal monster rules/Constrict|constrict]]_ (2d8+10)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +26)
Constant—_[[spells/Detect Chaos|detect chaos]]_, _[[spells/Detect Evil|detect evil]]_, _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 19), _[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Plane Shift|plane shift]]_ (DC 24)
 1/week—_[[spells/Reincarnate|reincarnate]]_
**Spells Prepared** (CL 18th; concentration +27)
9th—_[[spells/Antipathy|antipathy]]_ (DC 28), _[[spells/Regenerate|regenerate]]_, _[[universal monster rules/Summon|summon]]_ nature’s ally IX 
8th—_[[spells/Control Plants|control plants]]_ (DC 27), mass _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Repel Metal or Stone|repel metal or stone]]_, _[[universal monster rules/Whirlwind|whirlwind]]_ (DC 27) 
7th—_[[spells/Animate Plants|animate plants]]_, _[[spells/Control Weather|control weather]]_, _[[spells/Heal|heal]]_, _[[spells/Transmute Metal to Wood|transmute metal to wood]]_ 
6th—greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Liveoak|liveoak]]_, _[[spells/Move Earth|move earth]]_, _[[spells/Transport via Plants|transport via plants]]_, _[[spells/Wall Of Stone|wall of stone]]_ 
5th—_[[spells/Animal Growth|animal growth]]_ (DC 24), _[[spells/Awaken|awaken]]_ (DC 24), _[[spells/Commune with Nature|commune with nature]]_, _[[spells/Control Winds|control winds]]_ (DC 24), _[[spells/Hallow|hallow]]_, _[[spells/Wall Of Thorns|wall of thorns]]_ 
4th—_[[spells/Antiplant Shell|antiplant shell]]_, _[[spells/Command Plants|command plants]]_ (DC 23), _[[spells/Control Water|control water]]_, _dispel magic_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Repel Vermin|repel vermin]]_ 
3rd—_[[spells/Daylight|daylight]]_, _[[spells/Dominate Animal|dominate animal]]_ (DC 22), _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Quench|quench]]_ (DC 22), _[[spells/Remove Disease|remove disease]]_, _[[spells/Speak with Plants|speak with plants]]_ 
2nd—_[[spells/Animal Messenger|animal messenger]]_, _[[spells/Gust Of Wind|gust of wind]]_ (DC 21), lesser _[[spells/Restoration|restoration]]_, _[[spells/Soften Earth and Stone|soften earth and stone]]_, _[[spells/Warp Wood|warp wood]]_ (DC 21), _[[spells/Wood Shape|wood shape]]_ (DC 21) 
1st—_[[spells/Calm Animals|calm animals]]_ (DC 20), _[[spells/Charm Animal|charm animal]]_ (DC 20), _[[spells/Detect Animals or Plants|detect animals or plants]]_, _[[spells/Entangle|entangle]]_ (DC 20), _[[spells/Faerie Fire|faerie fire]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Speak with Animals|speak with animals]]_ 
0 (at will)—_[[spells/Create Water|create water]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Know Direction|know direction]]_, _[[spells/Purify Food and Drink|purify food and drink]]_ (DC 19)

##### Statistics
**Str** 30, **Dex** 20, **Con** 25, **Int** 18, **Wis** 29, **Cha** 27
**Base Atk** +20; **CMB** +32 (+36 grapple); **CMD** 48 (can't be tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Natural Spell|Natural Spell]]_, _[[feats/Spell Penetration|Spell Penetration]]_, _[[feats/Widen Spell|Widen Spell]]_, _[[feats/Wingover|Wingover]]_
**Skills** Bluff +31, Fly +20, Intimidate +31, Knowledge (geography) +27, Knowledge (nature) +27, Perception +36, Sense Motive +36, Spellcraft +24, Stealth +20, Survival +32
**Languages** Celestial, Common, Draconic, Druidic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** natural form, wild _[[feats/Empathy|empathy]]_ +32

##### Ecology

**Environment** warm badlands or ruins
**Organization** solitary
**Treasure** standard

### Special Abilities

**Aura of Resplendence (Sp)** A chicome constantly radiates an aura of _[[spells/Plant Growth|plant growth]]_, as the spell, providing enrichment to plants within a half-mile radius. The chicome can suppress or resume the aura as a free action.

**Natural Form (Sp)** Once per day as a standard action, a chicome can take the form of any animal, dragon, magical beast, or vermin with 18 Hit Dice or fewer. This functions as if using _[[spells/Beast Shape IV|beast shape IV]]_, _[[spells/Form of the Dragon III|form of the dragon III]]_, _[[spells/Magical Beast Shape|magical beast shape]]_, or _[[spells/Vermin Shape II|vermin shape II]]_, as appropriate, and otherwise counts as a _[[classes/Druid|druid]]_’s wild shape ability for the purposes of abilities and prerequisites. The chicome can maintain this form indefinitely and can end the _[[spells/Transformation|transformation]]_ as a free action.

**Poison (Ex)** Injury—bite; save Fort DC 27; frequency 1/minute for 10 minutes; effect 2d4 Str; cure 2 consecutive saves.
**Spells** A chicome casts spells as an 18th-level _druid_, but cannot swap out prepared spells to cast _summon_ spells.

**Wild _Empathy_ (Su)** This works like the _druid_’s wild _empathy_ class feature, except the chicome has a +6 racial bonus on the check. The chicome’s effective _druid_ level is 18 for the purpose of determining its total modifier to the check.

##### Description

Chicomes are a powerful but gentle variety of _[[monsters/Couatl|couatl]]_— winged serpentine outsiders who act as agents of lawful good deities—whose purpose is to reestablish nature in destroyed and ravaged lands, especially those that have been recently cleansed of evil. Chicomes accomplish this by way of powerful druidic magic and the cloud of restorative pollen and dew that constantly drifts from their wings. Like other couatls, chicomes have varicolored feathers and beautiful, glossy scales. The couatls' wing feathers are typically _[[spells/Shades|shades]]_ of green or brown, but their crests are always a brilliant crimson. Like for other couatls, the feathers of chicomes are incredibly powerful magic items when bestowed upon chosen mortals. Such a freely given feather can be used as the material component for a _[[spells/Planar Ally|planar ally]]_ spell. In addition, if buried in at least 6 inches of soil and undisturbed for 24 hours, the feather can be used as the material component to cast a _hallow_ spell; the spell effect tied to the hallowed site is always the enrichment version of _plant growth_. By using a chicome feather in this way, the caster need not _[[spells/Expend|expend]]_ the typical payment of gold or other valuables required by the spell.

A typical chicome is 40 feet long with a wingspan of 30 feet and weighs 5,500 pounds.