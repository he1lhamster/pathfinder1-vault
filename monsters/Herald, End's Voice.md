---
cssclass: [monsters]
title1: Herald, End's Voice
desc_short: A long crimson cloak drapes over the form of this large faceless being,
  which floats just above the ground on footless legs as its menacing flail crackles
  with blue currents of electricity.
title2: End's Voice
CR: 15
sources:
- name: 'Pathfinder #64: Beyond the Doomsday Door'
  page: 84
  link: http://paizo.com/products/btpy8t35?Pathfinder-Adventure-Path-64-Beyond-the-Doomsday
    Door
XP: 51200
alignment: CN
size: Large
type: outsider
subtypes:
- chaotic
- extraplanar
initiative:
  bonus: 7
senses:
  darkvision: 60
  trueseeing: true
AC:
  AC: 31
  touch: 15
  flat_footed: 27
  components:
    dex: 3
    dodge: 1
    insight: 2
    natural: 16
    size: -1
    other:
    - never surprised or flat-footed
HP:
  HP: 225
  long: 18d10+126
  fast_healing: 5
saves:
  fort: 18
  ref: 11
  will: 19
DR:
- amount: 10
  weakness: law and magic
immunities:
- confusion
- insanity
resistances:
  acid: 30
  cold: 30
  electricity: 30
  fire: 30
SR: 26
speeds:
  base: 40
  fly: 40
  fly_maneuverability: average
attacks:
  melee:
  - - text: +1 shock heavy flail +23/+18/+13/+8 (2d8+7/17-20 plus 1d6 electricity
        and maddening strike)
      entries:
      - - damage: 2d8+7
          crit_range: 17-20
        - damage: 1d6
          type: electricity
        - effect: maddening strike
      attack: +1 shock heavy flail
      bonus:
      - 23
      - 18
      - 13
      - 8
  special:
  - destructive aura
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: foresight
    source: default
    freq: Constant
    other: self only
  - name: true seeing
    source: default
    freq: Constant
    other: self only
  - name: arcane eye
    source: default
    freq: At will
  - name: quickened bleed
    source: default
    freq: At will
    DC: 16
  - name: hideous laughter
    source: default
    freq: At will
    DC: 18
  - name: knock
    source: default
    freq: At will
  - name: magic missile
    source: default
    freq: At will
  - name: shatter
    source: default
    freq: At will
    DC: 18
  - name: telepathic bond
    source: default
    freq: At will
  - name: touch of idiocy
    source: default
    freq: At will
  - name: true strike
    source: default
    freq: At will
  - name: confusion
    source: default
    freq: 5/day
    DC: 20
  - name: contact other plane
    source: default
    freq: 5/day
    other: see below
  - name: feeblemind
    source: default
    freq: 5/day
    DC: 21
  - name: greater teleport
    source: default
    freq: 5/day
    other: self plus 50 lbs. of objects only
  - name: mind fog
    source: default
    freq: 5/day
    DC: 21
  - name: nightmare
    source: default
    freq: 5/day
    DC: 21
  - name: phantasmal killer
    source: default
    freq: 5/day
    DC: 21
  - name: break enchantment
    source: default
    freq: 1/day
  - name: disintegrate
    source: default
    freq: 1/day
    DC: 22
  - name: harm
    source: default
    freq: 1/day
    DC: 22
  - name: insanity
    source: default
    freq: 1/day
    DC: 23
  - name: mage's disjunction
    source: default
    freq: 1/day
    DC: 25
  - name: mass invisibility
    source: default
    freq: 1/day
  - name: moment of prescience
    source: default
    freq: 1/day
  - name: power word kill
    source: default
    freq: 1/day
  - name: weird
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 18
    concentration: 24
ability_scores:
  STR: 18
  DEX: 17
  CON: 24
  INT: 17
  WIS: 16
  CHA: 22
BAB: 18
CMB: 23
CMB_other: +25 sunder
CMD: 39
CMD_other: 41 vs. sunder, can't be tripped
feats:
- name: Combat Casting
- name: Combat Expertise
- name: Dodge
- name: Improved Critical (heavy flail)
- name: Improved Initiative
- name: Improved Iron Will
- name: Improved Sunder
- name: Iron Will
- name: Weapon Focus (heavy flail)
skills:
  Disable Device: 18
  Fly: 16
  Intimidate: 24
  Knowledge (geography): 18
  Knowledge (history): 21
  Knowledge (religion): 21
  Perception: 21
  Sense Motive: 21
  Spellcraft: 18
  Stealth: 17
  Use Magic Device: 24
  _racial_mods:
    Acrobatics:
      when jumping: 4
languages:
- Aklo
- Ancient Osiriani
- Azlanti
- Common
- Cyclops
- Draconic
- Orvian
- telepathy 100 ft.
special_qualities:
- madness
- no breath
ecology:
  environment: any (Astral Plane or Pharasma's Boneyard)
  organization: solitary
  treasure_type: standard
  treasure:
  - Large +1 shock heavy flail
  - other treasure
special_abilities:
  Adaptable Life Force (Su): Any effect that heals living creatures and harms undead
    or heals undead and harms living creatures (such as cure spells, inflict spells,
    and channeled energy) always heals the herald, even if the source of the power
    intended to harm it.
  Contact Other Plane (Sp): This ability functions as the spell contact other plane,
    but the herald can only ask questions on the behalf of another creature, the questioner
    (not the herald) must make the Intelligence check (if any) to avoid losing Intelligence
    or Charisma, and the loss is permanent rather than temporary.
  Destructive Aura (Su): As a swift action, the herald can emit a 30-foot aura of
    destruction for 15 rounds per day. All attacks made against targets in this aura
    (including the herald) gain a +7 morale bonus on damage rolls, and all critical
    threats are automatically confirmed. These rounds do not need to be consecutive.
  Maddening Strike (Su): If the herald successfully hits a creature with its flail,
    as a swift action it may force the opponent to make a DC 25 Will save. If the
    creature fails its save, it is confused for 1 round. The save DC is Charisma-based.
  Madness (Ex): The herald uses its Charisma modifier on Will saves instead of its
    Wisdom modifier, and is immune to insanity and confusion effects. Only a miracle
    or wish can remove its madness. If this occurs, the herald gains 6 points of Wisdom
    and loses 6 points of Charisma; it automatically reverts to its insane state 1d10
    minutes later.
  Telepathic Bond (Sp): This ability functions like telepathic bond, except any creature
    linked to the herald's disturbing thoughts takes 1 point of Wisdom damage every
    10 minutes.
desc_long: |-
  Groetus's herald is End's Voice, an enigmatic creature that is both more and less mysterious than its master. It looks like a giant shrouded figure floating above the ground, legless and faceless, wielding a heavy flail with ends made of glowing energy. Its visage is often confused with a reaping undead, though it is a living outsider and acts mildly insulted when others assume it to be otherwise. Its voice is hollow and distorted, as if echoing from the far end of a long metal tube, and colored with accents from ruined empires and dead languages. It rarely comes to Golarion, and for most of these visits it is merely a silent witness to a great slaughter upon the battlefield or the last gasp of a dying city, though it may strike out with its weapon or magic at a seemingly random wounded or dying target, as if making sure the creature dies as expected.

  The herald may be insane from associating with Groetus, but it has a clarity unknown to mortal worshipers of the God of the End Times; perhaps its vast knowledge somehow protected it from a truly insane fate, or its status as a herald may give it a kind of lucidity that pierces the fog of madness. It does not cackle at itself like a madman, respond to unheard voices, kill for pleasure, or exhibit any of a dozen other obvious signs of insanity typically exhibited by the mad followers of Groetus.

---

# Herald, End's Voice
A long crimson cloak drapes over the form of this large faceless being, which floats just above the ground on footless legs as its _[[items/Weapon Magic Abilities/Menacing|menacing]]_ flail crackles with blue currents of electricity.
**Source** Pathfinder #64: Beyond the Doomsday Door pg. 84
**XP** 51,200

CN Large outsider (chaotic, extraplanar)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., trueseeing; Perception +21

##### Defense

**AC** 31, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+3 Dex, +1 dodge, +2 insight, +16 natural, –1 size; never surprised or _flat-footed_)
**hp** 225 (18d10+126); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +18, **Ref** +11, **Will** +19
**DR** 10/law and magic; **Immune** _[[spells/Confusion|confusion]]_, _[[spells/Insanity|insanity]]_; **Resist** acid 30, cold 30, electricity 30, fire 30; **SR** 26

##### Offense
**Speed** 40 ft., fly 40 ft. (average)
**Melee** +1 _[[items/Weapon Magic Abilities/Shock|shock]]_ _[[items/Weapon/Heavy flail|heavy flail]]_ +23/+18/+13/+8 (2d8+7/17–20 plus 1d6 electricity and _[[feats/Maddening Strike|maddening strike]]_)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** destructive aura
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +24)
Constant—_[[spells/Foresight|foresight]]_ (self only), _[[spells/True Seeing|true seeing]]_ (self only)
At will—_[[spells/Arcane Eye|arcane eye]]_, quickened _[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Hideous Laughter|hideous laughter]]_ (DC 18), _[[spells/Knock|knock]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shatter|shatter]]_ (DC 18), _[[spells/Telepathic Bond|telepathic bond]]_, _[[spells/Touch of Idiocy|touch of idiocy]]_, _[[spells/True Strike|true strike]]_
5/day—_confusion_ (DC 20), _[[spells/Contact Other Plane|contact other plane]]_ (see below), _[[spells/Feeblemind|feeblemind]]_ (DC 21), greater teleport (self plus 50 lbs. of objects only), _[[spells/Mind Fog|mind fog]]_ (DC 21), _[[spells/Nightmare|nightmare]]_ (DC 21), _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 21)
1/day—_[[spells/Break Enchantment|break enchantment]]_, _[[spells/Disintegrate|disintegrate]]_ (DC 22), _[[spells/Harm|harm]]_ (DC 22), _insanity_ (DC 23), mage’s disjunction (DC 25), mass _[[spells/Invisibility|invisibility]]_, _[[spells/Moment of Prescience|moment of prescience]]_, _[[spells/Power Word Kill|power word kill]]_, _[[spells/Weird|weird]]_ (DC 25)

##### Statistics
**Str** 18, **Dex** 17, **Con** 24, **Int** 17, **Wis** 16, **Cha** 22
**Base Atk** +18; **CMB** +23 (+25 sunder); **CMD** 39 (41 vs. sunder, can’t be tripped)
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_heavy flail_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_heavy flail_)
**Skills** Disable Device +18, Fly +16, Intimidate +24, Knowledge (geography) +18, Knowledge (history) +21, Knowledge (religion) +21, Perception +21, Sense Motive +21, Spellcraft +18, Stealth +17, Use Magic Device +24; **Racial Modifiers** +4 Acrobatics when jumping
**Languages** Aklo, Ancient Osiriani, Azlanti, Common, _[[monsters/Cyclops|Cyclops]]_, Draconic, Orvian; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** madness, _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any (Astral Plane or Pharasma’s Boneyard)
**Organization** solitary
**Treasure** standard (Large +1 _shock_ _heavy flail_, other treasure)

### Special Abilities

**Adaptable Life Force (Su)** Any effect that heals living creatures and harms undead or heals undead and harms living creatures (such as cure spells, inflict spells, and channeled energy) always heals the herald, even if the source of the power intended to _harm_ it.

**_Contact Other Plane_ (Sp)** This ability functions as the spell _contact other plane_, but the herald can only ask questions on the behalf of another creature, the questioner (not the herald) must make the Intelligence check (if any) to avoid losing Intelligence or Charisma, and the loss is permanent rather than temporary.

**Destructive Aura (Su) **As a swift action, the herald can emit a 30-foot aura of _[[spells/Destruction|destruction]]_ for 15 rounds per day. All attacks made against targets in this aura (including the herald) gain a +7 morale bonus on damage rolls, and all critical threats are automatically confirmed. These rounds do not need to be consecutive.

**_Maddening Strike_ (Su)** If the herald successfully hits a creature with its flail, as a swift action it may force the opponent to make a DC 25 Will save. If the creature fails its save, it is _[[conditions/Confused|confused]]_ for 1 round. The save DC is Charisma-based.

**Madness (Ex)** The herald uses its Charisma modifier on Will saves instead of its Wisdom modifier, and is immune to _insanity_ and _confusion_ effects. Only a _[[spells/Miracle|miracle]]_ or _[[spells/Wish|wish]]_ can remove its madness. If this occurs, the herald gains 6 points of Wisdom and loses 6 points of Charisma; it automatically reverts to its insane state 1d10 minutes later.

**_Telepathic Bond_ (Sp)** This ability functions like _telepathic bond_, except any creature linked to the herald’s disturbing thoughts takes 1 point of Wisdom damage every 10 minutes.

##### Description

Groetus’s herald is End’s Voice, an enigmatic creature that is both more and less mysterious than its master. It looks like a giant shrouded figure floating above the ground, legless and faceless, wielding a _heavy flail_ with ends made of glowing energy. Its visage is often _confused_ with a reaping undead, though it is a living outsider and acts mildly insulted when others assume it to be otherwise. Its voice is hollow and distorted, as if echoing from the far end of a long metal tube, and colored with accents from ruined empires and dead languages. It rarely comes to Golarion, and for most of these visits it is merely a silent _[[spells/Witness|witness]]_ to a great slaughter upon the battlefield or the last gasp of a _[[conditions/Dying|dying]]_ city, though it may strike out with its weapon or magic at a seemingly random wounded or _dying_ target, as if making sure the creature dies as expected.

The herald may be insane from associating with Groetus, but it has a _[[items/Weapon/Clarity|clarity]]_ _[[monsters/Unknown|unknown]]_ to mortal worshipers of the God of the End Times; perhaps its vast knowledge somehow protected it from a truly insane fate, or its _[[spells/Status|status]]_ as a herald may give it a kind of lucidity that pierces the fog of madness. It does not cackle at itself like a madman, respond to unheard voices, kill for pleasure, or exhibit any of a dozen other obvious signs of _insanity_ typically exhibited by the mad followers of Groetus.