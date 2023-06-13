---
cssclass: [monsters]
title1: Leng Hound
desc_short: This unnatural beast's clawed hands dangle in front of its hindpaws. Its
  bat-winged form blends humanoid features with canine.
title2: Leng Hound
CR: 10
sources:
- name: Bestiary 6
  page: 180
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 9600
alignment: CE
size: Medium
type: aberration
subtypes:
- extraplanar
initiative:
  bonus: 11
senses:
  darkvision: 60
  scent: true
  sense fear: true
AC:
  AC: 25
  touch: 18
  flat_footed: 17
  components:
    dex: 7
    dodge: 1
    natural: 7
HP:
  HP: 123
  long: 13d8+65
  fast_healing: 10
saves:
  fort: 9
  ref: 11
  will: 13
defensive_abilities:
- negative energy affinity
immunities:
- cold
- disease
speeds:
  base: 40
  fly: 40
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +18 (2d6+9/19-20)
      entries:
      - - damage: 2d6+9
          crit_range: 19-20
      attack: bite
      bonus:
      - 18
    - text: 2 claws +18 (1d6+9)
      entries:
      - - damage: 1d6+9
      count: 2
      attack: claws
      bonus:
      - 18
  special:
  - haunting howl
  - mutilate
spell_like_abilities:
  entries:
  - name: sense fear
    source: default
    freq: Constant
  - name: locate creature
    source: default
    freq: At will
  - name: locate object
    source: default
    freq: At will
  - name: dimension door
    source: default
    freq: 3/day
  - name: quickened summon swarm
    source: default
    freq: 3/day
    other: bats only
  - name: word of recall
    source: default
    freq: 1/day
    other: see grave link
  sources:
  - name: default
    CL: 12
    concentration: 16
ability_scores:
  STR: 29
  DEX: 24
  CON: 21
  INT: 14
  WIS: 20
  CHA: 19
BAB: 9
CMB: 18
CMD: 36
feats:
- name: Dodge
- name: Flyby Attack
- name: Improved Critical(bite)
- name: Improved Initiative
- name: Mobility
- name: Quicken Spell-Like Ability (summon swarm)
- name: Vital Strike
skills:
  Acrobatics: 23
  Disguise: 17
    _other: +27when using charnel deception
  Fly: 27
  Perception: 21
  Stealth: 23
  Survival: 21
  _racial_mods:
    Disguise:
      whenusing charnel deception: 10
languages:
- Aklo
- Common
special_qualities:
- charnel deception
- freeze (ashuman skeleton when using charneldeception)
- grave link
- no breath
ecology:
  environment: any
  organization: solitary or pack (2-8)
  treasure_type: standard
special_abilities:
  Charnel Deception (Ex): A Leng hound can retract its bestial features into its body
    as a full-round action-its fur and wings retract, the skin covering them slithers
    into hidden cavities, and its jaws pull back into a humanlike face. This grants
    it a +10 bonus on Disguise checks to appear as the decayed corpse of a slightly
    deformed human or similarly sized humanoid.
  Grave Link (Su): As a full-round action, a Leng hound can designate a grave containing
    the corpse of a creature that was evil in life as its grave link. When the Leng
    hound uses word of recall, it returns to this grave (a Leng hound with no active
    grave link cannot use word of recall). If a creature disturbs this grave or loots
    it, the Leng hound's locate creature and locate object spell-like abilities have
    no range limit when searching for the creature that disturbed the grave or any
    objects looted from the grave.
  Haunting Howl (Su): Three times per day, a Leng hound can emit a deep, sardonic
    howl. Only creatures within 300 feet that the Leng hound has tracked or attempted
    to find with divination spell-like abilities can hear this haunting howl. Such
    creatures must succeed at a DC 20 Will save or take 1d4 points of Intelligence,
    Wisdom, and Charisma damage and become shaken for 1 hour. This is a mind-affecting
    fear effect. The save DC is Charisma-based.
  Mutilate (Ex): A Leng hound savages its victims, shredding flesh and crushing bones.
    Whenever a Leng hound hits a creature with all three natural attacks in a single
    round, or with Vital Strike, the target must succeed at a DC 21 Fortitude save
    or take 2 points of Constitution drain. The save DC is Constitution-based.
desc_long: |-
  Leng hounds hail from the nightmare plateau of Leng, where they haunt its eternity-old ruins. They are most often beckoned to the Material Plane to serve as guardians of grave sites, a duty they eagerly perform in exchange for the opportunity to feast upon the dead things elsewhere in the cemetery. Leng hounds prefer to lurk inside the coffins they guard, rearranging their bodies into skeletal shapes. 

  A Leng hound can be contacted by a contact entity III spell. The caster must provide a corpse with grave goods worth at least 2,000 gp for the Leng hound to guard. 

  A Leng hound is 7 feet tall but weighs only 150 pounds.

---

# Leng Hound
This unnatural beast’s clawed hands dangle in front of its hind

paws. Its bat-winged form blends humanoid features with canine.
**Source** Bestiary 6 pg. 180
**XP** 9,600
CE Medium aberration (extraplanar)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_, _[[spells/Sense Fear|sense fear]]_; Perception +21

##### Defense

**AC** 25, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+7 Dex, +1 _[[feats/Dodge|dodge]]_, +7 natural)
**hp** 123 (13d8+65); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +9, **Ref** +11, **Will** +13
**Defensive Abilities** _[[universal monster rules/Negative Energy Affinity|negative energy affinity]]_; **Immune** cold, disease

##### Offense
**Speed** 40 ft., fly 40 ft. (good)
**Melee** bite +18 (2d6+9/19–20), 2 claws +18 (1d6+9)
**Special Attacks** haunting howl, mutilate
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
Constant—_sense fear_ 
At will—_[[spells/Locate Creature|locate creature]]_, _[[spells/Locate Object|locate object]]_ 
3/day—_[[spells/Dimension Door|dimension door]]_, quickened _[[spells/Summon Swarm|summon swarm]]_ (bats only) 
1/day—_[[spells/Word of Recall|word of recall]]_ (see grave link)

##### Statistics
**Str** 29, **Dex** 24, **Con** 21, **Int** 14, **Wis** 20, **Cha** 19
**Base Atk** +9; **CMB** +18; **CMD** 36
**Feats** _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Improved Critical|Improved Critical]]_

(bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_summon swarm_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +23, Disguise +17 (+27

when using charnel deception), Fly +27,

Perception +21, Stealth +23, Survival +21;

**Racial Modifiers** +10 Disguise when

using charnel deception
**Languages** Aklo, Common
**SQ** charnel deception, _[[universal monster rules/Freeze|freeze]]_ (as

human skeleton when using charnel

deception), grave link, _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any
**Organization** solitary or pack (2–8)
**Treasure** standard

### Special Abilities

**Charnel Deception (Ex)** A _[[monsters/Leng Hound|Leng hound]]_ can retract its bestial features into its body as a full-round action—its fur and wings retract, the skin covering them slithers into hidden cavities, and its jaws _[[universal monster rules/Pull|pull]]_ back into a humanlike face. This grants it a +10 bonus on Disguise checks to appear as the decayed corpse of a slightly deformed human or similarly sized humanoid.

**Grave Link (Su)** As a full-round action, a _Leng hound_ can designate a grave containing the corpse of a creature that was evil in life as its grave link. When the _Leng hound_ uses _word of recall_, it returns to this grave (a _Leng hound_ with no active grave link cannot use _word of recall_). If a creature disturbs this grave or loots it, the _Leng hound_’s _locate creature_ and _locate object_ _spell-like abilities_ have no range limit when searching for the creature that disturbed the grave or any objects looted from the grave.

**Haunting Howl (Su)** Three times per day, a _Leng hound_ can emit a deep, sardonic howl. Only creatures within 300 feet that the _Leng hound_ has tracked or attempted to find with _[[spells/Divination|divination]]_ _spell-like abilities_ can hear this haunting howl. Such creatures must succeed at a DC 20 Will save or take 1d4 points of Intelligence, Wisdom, and Charisma damage and become _[[conditions/Shaken|shaken]]_ for 1 hour. This is a mind-affecting _[[universal monster rules/Fear|fear]]_ effect. The save DC is Charisma-based.

**Mutilate (Ex)** A _Leng hound_ savages its victims, shredding flesh and crushing bones. Whenever a _Leng hound_ hits a creature with all three _[[universal monster rules/Natural Attacks|natural attacks]]_ in a single round, or with _Vital Strike_, the target must succeed at a DC 21 Fortitude save or take 2 points of Constitution drain. The save DC is Constitution-based.

##### Description

Leng hounds hail from the _[[spells/Nightmare|nightmare]]_ plateau of Leng, where they haunt its eternity-old ruins. They are most often beckoned to the Material Plane to serve as guardians of grave sites, a duty they eagerly perform in exchange for the opportunity to feast upon the dead things elsewhere in the cemetery. Leng hounds prefer to lurk inside the coffins they _[[npcs/Guard|guard]]_, rearranging their bodies into skeletal shapes.

A _Leng hound_ can be contacted by a _[[spells/Contact Entity III|contact entity III]]_ spell. The caster must provide a corpse with grave goods worth at least 2,000 gp for the _Leng hound_ to _guard_.

A _Leng hound_ is 7 feet tall but weighs only 150 pounds.