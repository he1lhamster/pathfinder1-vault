---
cssclass: [monsters]
title1: Hag, Blood Hag
desc_short: This woman would be pretty if it were not for her sharp teeth and nails,
  and her ghastly pale skin.
title2: Blood Hag
CR: 8
sources:
- name: Bestiary 4
  page: 19
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 4800
alignment: NE
size: Medium
type: monstrous humanoid
subtypes:
- shapechanger
initiative:
  bonus: 10
senses:
  darkvision: 60
  detect good: true
  detect magic: true
AC:
  AC: 23
  touch: 17
  flat_footed: 16
  components:
    dex: 6
    dodge: 1
    natural: 6
HP:
  HP: 90
  long: 12d10+24
saves:
  fort: 6
  ref: 14
  will: 11
DR:
- amount: 5
  weakness: cold iron and magic
immunities:
- charm
- disease
- fear
- fire
- sleep
SR: 19
speeds:
  base: 30
  fly: 60
  fly_other: perfect; in fiery form only
attacks:
  melee:
  - - text: bite +18 (2d4+4)
      entries:
      - - damage: 2d4+4
      attack: bite
      bonus:
      - 18
    - text: 2 claws +18 (1d6+4 plus grab)
      entries:
      - - damage: 1d6+4
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 18
  special:
  - blood drain (1d2 Con)
  - detonate
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: inflict moderate wounds
    source: default
    freq: At will
    DC: 16
  - name: scorching ray
    source: default
    freq: At will
  - name: spider climb
    source: default
    freq: At will
    other: self only
  - name: deep slumber
    source: default
    freq: 3/day
    DC: 17
  sources:
  - name: default
    CL: 12
    concentration: 16
ability_scores:
  STR: 18
  DEX: 22
  CON: 15
  INT: 14
  WIS: 17
  CHA: 19
BAB: 12
CMB: 18
CMB_other: +22 grapple
CMD: 33
feats:
- name: Agile Maneuvers
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Weapon Finesse
skills:
  Acrobatics: 18
  Bluff: 16
  Disguise: 16
  Fly: 14
  Intimidate: 19
  Perception: 18
  Stealth: 21
languages:
- Abyssal
- Common
- Giant
- Infernal
special_qualities:
- fiery form (DC 20)
- mask evil
ecology:
  environment: any land
  organization: solitary or coven (3 hags of any kind)
  treasure_type: standard
special_abilities:
  Detonate (Su): A blood hag in fiery form can explode in a 30-foot-radius burst that
    deals 8d6 points of fire damage (Reflex DC 18 for half). Using this ability returns
    a blood hag to her normal form. The save DC is Constitution-based.
  Fiery Form (Su): As a standard action, a blood hag who has removed her skin by using
    mask evil can assume the form of a flying ball of fire for up to 12 rounds. After
    leaving fiery form, a blood hag must wait 1d4 rounds before assuming it again.
    A blood hag in this form who enters the same space as another creature stops moving
    for that round and deals 3d6 points of fire damage (Reflex DC 20 negates) to that
    creature. A blood hag can suppress her heat and dim her light to that of an ember
    if she chooses, and can pass through openings and cracks as though in gaseous
    form. A blood hag in fiery form retains her AC and also has immunity to nonmagical
    attacks and effects. A successful targeted dispel magic spell or 20 points of
    cold damage returns her from her fiery form to her normal form. A blood hag can
    assume fiery form a number of times per day equal to her Charisma modifier (typically
    4). The save DC is Charisma-based.
  Mask Evil (Su): During the day, a blood hag “wears her skin,” giving her the appearance
    of a young woman. When so disguised, the blood hag can't use her bite, claws,
    or fiery form ability. At night, she bursts out of her skin and returns to her
    monstrous form. The hag regrows her skin each dawn. While a blood hag is wearing
    her skin, her alignment is masked as though by a constant undetectable alignment
    spell.
desc_long: |-
  Blood hags, known to some as soucouyants, prefer to live near isolated human communities or on the edge of civilized lands. A blood hag takes the appearance of a young woman by day. At night, she assumes her true form, as her skin peels back and sloughs off to reveal the monstrosity beneath.

  A hunting blood hag preys on unsuspecting neighbors during the night, sneaking into their homes and feeding off their blood or burning them alive. When a blood hag finds a particularly choice victim, she forgoes simply feeding on her, and instead abducts her, spiriting her away to the hag's hidden lair, where she'll be tortured and drained dry of blood over the course of days or weeks. Once the hag has properly prepared the victim's skin, she wears it. Bold and particularly clever blood hags attempt to masquerade as their victims for a time.

  Blood hags of exceptional talent typically gain levels in the witch class.

---

# Hag, Blood Hag
This woman would be pretty if it were not for her sharp teeth and nails, and her ghastly pale skin.
**Source** Bestiary 4 pg. 19
**XP** 4,800

NE Medium monstrous humanoid (shapechanger)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_; Perception +18

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 90 (12d10+24)
**Fort** +6, **Ref** +14, **Will** +11
**DR** 5/cold iron and magic; **Immune** charm, disease, _[[universal monster rules/Fear|fear]]_, fire, sleep; **SR** 19

##### Offense
**Speed** 30 ft., fly 60 ft. (perfect; in fiery form only)
**Melee** bite +18 (2d4+4), 2 claws +18 (1d6+4 plus _[[universal monster rules/Grab|grab]]_)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_ (1d2 Con), _[[spells/Detonate|detonate]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
Constant—_detect good_, _detect magic_
At will—_[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_ (DC 16), _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Spider Climb|spider climb]]_ (self only)
3/day—_[[spells/Deep Slumber|deep slumber]]_ (DC 17)

##### Statistics
**Str** 18, **Dex** 22, **Con** 15, **Int** 14, **Wis** 17, **Cha** 19
**Base Atk** +12; **CMB** +18 (+22 grapple); **CMD** 33
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +18, Bluff +16, Disguise +16, Fly +14, Intimidate +19, Perception +18, Stealth +21
**Languages** Abyssal, Common, Giant, Infernal
**SQ** fiery form (DC 20), _[[items/Mundane/Mask|mask]]_ evil

##### Ecology

**Environment** any land
**Organization** solitary or coven (3 hags of any kind)
**Treasure** standard

### Special Abilities

**_Detonate_ (Su)** A blood hag in fiery form can explode in a 30-foot-radius burst that deals 8d6 points of fire damage (Reflex DC 18 for half). Using this ability returns a blood hag to her normal form. The save DC is Constitution-based.

**Fiery Form (Su)** As a standard action, a blood hag who has removed her skin by using _mask_ evil can assume the form of a flying ball of fire for up to 12 rounds. After leaving fiery form, a blood hag must wait 1d4 rounds before assuming it again. A blood hag in this form who enters the same space as another creature stops moving for that round and deals 3d6 points of fire damage (Reflex DC 20 negates) to that creature. A blood hag can suppress her _[[universal monster rules/Heat|heat]]_ and dim her light to that of an ember if she chooses, and can pass through openings and cracks as though in _[[spells/Gaseous Form|gaseous form]]_. A blood hag in fiery form retains her AC and also has _[[universal monster rules/Immunity|immunity]]_ to nonmagical attacks and effects. A successful targeted _[[spells/Dispel Magic|dispel magic]]_ spell or 20 points of cold damage returns her from her fiery form to her normal form. A blood hag can assume fiery form a number of times per day equal to her Charisma modifier (typically 4). The save DC is Charisma-based.

**_Mask_ Evil (Su)** During the day, a blood hag “wears her skin,” giving her the appearance of a young woman. When so disguised, the blood hag can’t use her bite, claws, or fiery form ability. At night, she bursts out of her skin and returns to her monstrous form. The hag regrows her skin each dawn. While a blood hag is wearing her skin, her alignment is masked as though by a constant _[[spells/Undetectable Alignment|undetectable alignment]]_ spell.

##### Description

Blood hags, known to some as soucouyants, prefer to live near isolated human communities or on the edge of civilized lands. A blood hag takes the appearance of a young woman by day. At night, she assumes her _[[spells/True Form|true form]]_, as her skin peels back and sloughs off to reveal the monstrosity beneath.

A hunting blood hag preys on unsuspecting neighbors during the night, sneaking into their homes and feeding off their blood or _[[items/Weapon Magic Abilities/Burning|burning]]_ them alive. When a blood hag finds a particularly choice victim, she forgoes simply feeding on her, and instead abducts her, spiriting her away to the hag’s hidden lair, where she’ll be tortured and drained dry of blood over the course of days or weeks. Once the hag has properly prepared the victim’s skin, she wears it. Bold and particularly clever blood hags attempt to masquerade as their victims for a time.

Blood hags of exceptional talent typically gain levels in the _[[classes/Witch|witch]]_ class.