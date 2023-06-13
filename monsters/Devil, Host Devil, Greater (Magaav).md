---
cssclass: [monsters]
title1: Devil, Host Devil, Greater (Magaav)
desc_short: Twisted horns rise from the skinless head of this winged creature, and
  noxious fumes leak from between its yellowed fangs.
title2: Host Devil, Greater (Magaav)
CR: 6
sources:
- name: Bestiary 4
  page: 53
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
- name: 'Book of the Damned - Volume 1: Princes of Darkness'
  page: 58
  link: http://paizo.com/store/downloads/pathfinder/pathfinderChronicles/pathfinderRPG/v5748btpy8a6f
XP: 2400
alignment: LE
size: Medium
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 4
senses:
  darkvision: 60
  detect magic: true
  see in darkness: true
AC:
  AC: 23
  touch: 15
  flat_footed: 18
  components:
    dex: 4
    dodge: 1
    natural: 8
HP:
  HP: 59
  long: 7d10+21
saves:
  fort: 8
  ref: 9
  will: 3
DR:
- amount: 5
  weakness: good
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 17
speeds:
  base: 20
  fly: 50
  fly_maneuverability: average
attacks:
  melee:
  - - text: mwk ranseur +12/+7 (2d4+6/×3)
      entries:
      - - damage: 2d4+6
          crit_multiplier: 3
      attack: mwk ranseur
      bonus:
      - 12
      - 7
  - - text: 2 claws +11 (1d6+4 plus 2 bleed)
      entries:
      - - damage: 1d6+4
        - damage: '2'
          type: bleed
      count: 2
      attack: claws
      bonus:
      - 11
  special:
  - noxious breath
  - rend (2 claws, 1d6+6 plus 2 bleed)
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: Constant
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: summon
    source: default
    freq: 1/day
    CL: 3
    other: 1 magaav 40%
  sources:
  - name: default
    CL: 12
    concentration: 12
ability_scores:
  STR: 18
  DEX: 19
  CON: 16
  INT: 10
  WIS: 12
  CHA: 11
BAB: 7
CMB: 11
CMD: 26
feats:
- name: Combat Reflexes
- name: Dodge
- name: Hover
- name: Mobility
skills:
  Acrobatics: 14
    when jumping: 10
  Escape Artist: 14
  Fly: 14
  Intimidate: 10
  Perception: 11
  Stealth: 14
languages:
- Celestial
- Draconic
- Infernal
- telepathy 100 ft.
special_qualities:
- master grappler
- shared senses
ecology:
  environment: any (Hell)
  organization: solitary, pair, or flock (2-6)
  treasure_type: standard
  treasure:
  - mwk ranseur
  - other treasure
special_abilities:
  Master Grappler (Ex): A magaav can wield a weapon and still attempt grapple checks.
    While not wielding a weapon, a magaav gains a +4 bonus on grapple checks.
  Noxious Breath (Su): Three times per day, as a standard action a magaav can exhale
    a breath that reeks of pure corruption upon a creature within 5 feet. The target
    must succeed at a DC 16 Fortitude save or be sickened for 1d4 rounds. Creatures
    that successfully save cannot be affected by the same magaav's noxious breath
    for 24 hours. This is a poison effect. The save DC is Constitution-based.
  Shared Senses (Su): All magaavs within 100 feet of one another share the same senses.
    Thus, if one individual perceives something (for example, with a successful Perception
    check), all others within range are immediately aware of it. Senses are instantly
    relayed from one magaav to the next, allowing for the senses of a single devil
    to potentially spread through and inform an entire swarm instantly. It is still
    possible for a magaav to be flat-footed for other reasons even if other magaavs
    nearby are not.
desc_long: |-
  Hunters of souls, host devils retrieve Hell's most elusive property. Whether souls that have long evaded capture upon the plains of Avernus, damned beings who have somehow managed to escape Hell, or creatures that have reneged upon infernal contracts, vast flocks of these winged fiends fly from the Pit to recover their prey. Rarely seen alone, host devils travel in great swarms that often number in the thousands. These four-winged mockeries of the angelic form swarm in enormous columns, moving in tandem as though they were one colossal, infernal beast controlled by a single brain.

  Magaavs stand 5-1/2 feet tall and weigh 150 pounds, with wingspans reaching 10 feet across. Their fetid breath draws flies that swarm over their bodies.

---

# Devil, Host Devil, Greater (Magaav)
Twisted horns rise from the skinless head of this winged creature, and noxious fumes leak from between its yellowed fangs.
**Source** Bestiary 4 pg. 53, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ - Volume 1: Princes of _[[spells/Darkness|Darkness]]_ pg. 58
**XP** 2,400

LE Medium outsider (devil, evil, extraplanar, lawful)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Magic|detect magic]]_, _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +11

##### Defense

**AC** 23, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 Dex, +1 _[[feats/Dodge|dodge]]_, +8 natural)
**hp** 59 (7d10+21)
**Fort** +8, **Ref** +9, **Will** +3
**DR** 5/good; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 17

##### Offense
**Speed** 20 ft., fly 50 ft. (average)
**Melee** mwk _[[items/Weapon/Ranseur|ranseur]]_ +12/+7 (2d4+6/×3) or 2 claws +11 (1d6+4 plus 2 _[[universal monster rules/Bleed|bleed]]_)
**Special Attacks** noxious breath, _[[universal monster rules/Rend|rend]]_ (2 claws, 1d6+6 plus 2 _bleed_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +12)
Constant—_detect magic_
At will—greater teleport (self plus 50 lbs. of objects only)
1/day—_[[universal monster rules/Summon|summon]]_ (CL 3rd, 1 magaav 40%)

##### Statistics
**Str** 18, **Dex** 19, **Con** 16, **Int** 10, **Wis** 12, **Cha** 11
**Base Atk** +7; **CMB** +11; **CMD** 26
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Hover|Hover]]_, _[[feats/Mobility|Mobility]]_
**Skills** Acrobatics +14 (+10 when jumping), Escape Artist +14, Fly +14, Intimidate +10, Perception +11, Stealth +14
**Languages** Celestial, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** master grappler, shared senses

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or flock (2–6)
**Treasure** standard (mwk _ranseur_, other treasure)

### Special Abilities

**Master Grappler (Ex)** A magaav can wield a weapon and still attempt grapple checks. While not wielding a weapon, a magaav gains a +4 bonus on grapple checks.

**Noxious Breath (Su)** Three times per day, as a standard action a magaav can exhale a breath that reeks of pure corruption upon a creature within 5 feet. The target must succeed at a DC 16 Fortitude save or be _[[conditions/Sickened|sickened]]_ for 1d4 rounds. Creatures that successfully save cannot be affected by the same magaav’s noxious breath for 24 hours. This is a poison effect. The save DC is Constitution-based.
**Shared Senses (Su)** All magaavs within 100 feet of one another share the same senses. Thus, if one individual perceives something (for example, with a successful Perception check), all others within range are immediately aware of it. Senses are instantly relayed from one magaav to the next, allowing for the senses of a single devil to potentially spread through and inform an entire swarm instantly. It is still possible for a magaav to be _flat-footed_ for other reasons even if other magaavs nearby are not.

##### Description

Hunters of souls, host devils retrieve Hell’s most elusive property. Whether souls that have long evaded capture upon the plains of Avernus, _[[feats/Damned|damned]]_ beings who have somehow managed to escape Hell, or creatures that have reneged upon infernal contracts, vast flocks of these winged fiends fly from the Pit to recover their prey. Rarely seen alone, host devils travel in great swarms that often number in the thousands. These four-winged mockeries of the angelic form swarm in enormous columns, moving in tandem as though they were one colossal, infernal beast controlled by a single brain.

Magaavs stand 5-1/2 feet tall and weigh 150 pounds, with wingspans reaching 10 feet across. Their _[[feats/Fetid Breath|fetid breath]]_ draws flies that swarm over their bodies.