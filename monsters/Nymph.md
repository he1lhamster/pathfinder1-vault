---
cssclass: [monsters]
title1: Nymph
desc_short: A delicate figure rises from the water, her long ears tapering to points
  above her head, her beauty painful in its perfection.
title2: Nymph
CR: 7
sources:
- name: Pathfinder RPG Bestiary
  page: 217
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 3200
alignment: CG
size: Medium
type: fey
initiative:
  bonus: 5
senses:
  low-light vision: true
auras:
- name: blinding beauty
  radius: 30
  DC: 21
AC:
  AC: 23
  touch: 23
  flat_footed: 17
  components:
    deflection: 7
    dex: 5
    dodge: 1
HP:
  HP: 60
  long: 8d6+32
saves:
  fort: 13
  ref: 18
  will: 16
DR:
- amount: 10
  weakness: cold iron
speeds:
  base: 30
  swim: 20
attacks:
  melee:
  - - text: mwk dagger +10 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 10
  special:
  - stunning glance
spell_like_abilities:
  entries:
  - name: dimension door
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 8
spells:
  entries:
  - name: summon nature's ally IV
    source: '?'
    level: 4
  - name: call lightning
    source: '?'
    level: 3
    DC: 16
  - name: cure moderate wounds
    source: '?'
    level: 3
  - name: water breathing
    source: '?'
    level: 3
  - name: barkskin
    source: '?'
    level: 2
  - name: flame blade
    source: '?'
    level: 2
  - name: resist energy
    source: '?'
    level: 2
  - name: tree shape
    source: '?'
    level: 2
  - name: charm animal
    source: '?'
    level: 1
    DC: 14
  - name: endure elements
    source: '?'
    level: 1
  - name: entangle
    source: '?'
    level: 1
    DC: 14
  - name: obscuring mist
    source: '?'
    level: 1
  - name: produce flame
    source: '?'
    level: 1
  - name: detect magic
    source: '?'
    level: 0
  - name: guidance
    source: '?'
    level: 0
  - name: light
    source: '?'
    level: 0
  - name: stabilize
    source: '?'
    level: 0
  sources:
  - name: '?'
    type: prepared
    CL: 7
ability_scores:
  STR: 10
  DEX: 21
  CON: 18
  INT: 16
  WIS: 17
  CHA: 25
BAB: 4
CMB: 9
CMD: 27
feats:
- name: Agile Maneuvers
- name: Combat Casting
- name: Dodge
- name: Weapon Finesse
skills:
  Diplomacy: 18
  Escape Artist: 16
  Handle Animal: 15
  Heal: 11
  Knowledge (nature): 14
  Perception: 14
  Sense Motive: 14
  Stealth: 16
  Swim: 19
languages:
- Common
- Sylvan
special_qualities:
- inspiration
- unearthly grace
- wild empathy +21
ecology:
  environment: temperate forest
  organization: solitary
  treasure_type: standard
  treasure:
  - dagger
  - other treasure
special_abilities:
  Blinding Beauty (Su): This ability affects all humanoids within 30 feet of a nymph.
    Those who look directly at a nymph must succeed on a DC 21 Fortitude save or be
    blinded permanently. A nymph can suppress or resume this ability as a free action.
    The save DC is Charisma-based.
  Inspiration (Su): A nymph can choose an intelligent creature to inspire and serve
    as a muse by giving that creature some token of her affection (typically a lock
    of her hair). As long as the nymph retains her favor for this creature and as
    long as the creature carries the nymph's token, the creature gains a +4 insight
    bonus on all Will saving throws, Craft checks, and Perform checks. A bard who
    has a nymph for a muse in this way can use his bardic performance for an additional
    number of rounds per day equal to his nymph muse's Charisma modifier. The nymph
    retains a link to her token and its carrier as if she had cast a status spell
    on the carrier. The nymph can end this effect at any time as a free action. A
    single nymph may only inspire one creature at a time in this manner.
  Spells: A nymph casts spells as a 7th-level druid, but cannot swap out prepared
    spells to cast summon spells.
  Stunning Glance (Su): As a standard action, a nymph can stun a creature within 30
    feet with a look. The target must succeed on a DC 21 Fortitude save or be stunned
    for 2d4 rounds. The save DC is Charisma-based.
  Unearthly Grace (Su): A nymph adds her Charisma modifier as a racial bonus on all
    her saving throws, and as a deflection bonus to her Armor Class.
  Wild Empathy (Su): This works like the druid's wild empathy class feature, except
    the nymph has a +6 racial bonus on the check. The nymph's effective druid level
    is equal to her HD for determining her total modifer to the check.
desc_long: Many have lost their lives in vain search of the beauty of the nymph, and
  many more to the madness and obsession their grace has upon minds and bodies unprepared
  for their companionship. Yet the nymph herself is not a cruel creature-a guardian
  of nature's purest places and most beautiful realms, she treats those who respect
  her and her abode with kindness, and may even favor someone who takes her fancy
  with magical gifts. Yet those who would seek to abuse or harm her or her home quickly
  find that behind her beauty is a fierce protector more than capable of defending
  her charge.

---

# Nymph
A delicate figure rises from the water, her long ears tapering to points above her head, her beauty painful in its perfection.
**Source** Pathfinder RPG Bestiary pg. 217
**XP** 3,200

CG Medium fey
**Init** +5; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14
**Aura** _[[items/Armor Magic Abilities/Blinding|blinding]]_ beauty (30 ft., DC 21)

##### Defense

**AC** 23, touch 23, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+7 _[[spells/Deflection|deflection]]_, +5 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 60 (8d6+32)
**Fort** +13, **Ref** +18, **Will** +16
**DR** 10/cold iron

##### Offense
**Speed** 30 ft., swim 20 ft.
**Melee** mwk _[[items/Weapon/Dagger|dagger]]_ +10 (1d4/19–20)
**Special Attacks** stunning glance
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th)
1/day—_[[spells/Dimension Door|dimension door]]_
**Spells Prepared **(CL 7th)
4th—_[[universal monster rules/Summon|summon]]_ nature’s ally IV
3rd—_[[spells/Call Lightning|call lightning]]_ (DC 16), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[universal monster rules/Water Breathing|water breathing]]_
2nd—_[[spells/Barkskin|barkskin]]_, _[[spells/Flame Blade|flame blade]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Tree Shape|tree shape]]_
1st—_[[spells/Charm Animal|charm animal]]_ (DC 14), _[[spells/Endure Elements|endure elements]]_, _[[spells/Entangle|entangle]]_ (DC 14), _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Produce Flame|produce flame]]_
0—_[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, light, stabilize

##### Statistics
**Str** 10, **Dex** 21, **Con** 18, **Int** 16, **Wis** 17, **Cha** 25
**Base Atk** +4; **CMB** +9; **CMD** 27
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Diplomacy +18, Escape Artist +16, Handle Animal +15, _[[spells/Heal|Heal]]_ +11, Knowledge (nature) +14, Perception +14, Sense Motive +14, Stealth +16, Swim +19
**Languages** Common, Sylvan
**SQ** inspiration, unearthly _[[spells/Grace|grace]]_, wild _[[feats/Empathy|empathy]]_ +21

##### Ecology

**Environment** temperate forest
**Organization** solitary
**Treasure** standard (_dagger_, other treasure)

### Special Abilities

**_Blinding_ Beauty (Su)** This ability affects all humanoids within 30 feet of a _[[monsters/Nymph|nymph]]_. Those who look directly at a _nymph_ must succeed on a DC 21 Fortitude save or be _[[conditions/Blinded|blinded]]_ permanently. A _nymph_ can suppress or resume this ability as a free action. The save DC is Charisma-based.

**Inspiration (Su)** A _nymph_ can choose an intelligent creature to inspire and serve as a _[[monsters/Muse|muse]]_ by giving that creature some token of her affection (typically a lock of her hair). As long as the _nymph_ retains her favor for this creature and as long as the creature carries the _nymph_’s token, the creature gains a +4 insight bonus on all Will saving throws, Craft checks, and Perform checks. A _[[classes/Bard|bard]]_ who has a _nymph_ for a _muse_ in this way can use his bardic performance for an additional number of rounds per day equal to his _nymph_ _muse_’s Charisma modifier. The _nymph_ retains a link to her token and its carrier as if she had cast a _[[spells/Status|status]]_ spell on the carrier. The _nymph_ can end this effect at any time as a free action. A single _nymph_ may only inspire one creature at a time in this manner.
**Spells **A _nymph_ casts spells as a 7th-level _[[classes/Druid|druid]]_, but cannot swap out prepared spells to cast _summon_ spells.
**Stunning Glance (Su)** As a standard action, a _nymph_ can stun a creature within 30 feet with a look. The target must succeed on a DC 21 Fortitude save or be _[[conditions/Stunned|stunned]]_ for 2d4 rounds. The save DC is Charisma-based.

**Unearthly _Grace_ (Su)** A _nymph_ adds her Charisma modifier as a racial bonus on all her saving throws, and as a _deflection_ bonus to her Armor Class.

**Wild _Empathy_ (Su)** This works like the _druid_’s wild _empathy_ class feature, except the _nymph_ has a +6 racial bonus on the check. The _nymph_’s effective _druid_ level is equal to her HD for determining her total modifer to the check.

##### Description

Many have lost their lives in vain search of the beauty of the _nymph_, and many more to the madness and obsession their _grace_ has upon minds and bodies unprepared for their companionship. Yet the _nymph_ herself is not a _[[items/Weapon Magic Abilities/Cruel|cruel]]_ creature—a _[[items/Weapon Magic Abilities/Guardian|guardian]]_ of nature’s purest places and most beautiful realms, she treats those who respect her and her abode with kindness, and may even favor someone who takes her fancy with magical gifts. Yet those who would seek to abuse or _[[spells/Harm|harm]]_ her or her home quickly find that behind her beauty is a fierce protector more than capable of _[[items/Weapon Magic Abilities/Defending|defending]]_ her charge.