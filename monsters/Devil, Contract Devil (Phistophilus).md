---
cssclass: [monsters]
title1: Devil, Contract Devil (Phistophilus)
desc_short: With rust-colored skin and a jutting crown of ridge-like horns, this muscular
  devil is draped in lengthy contracts.
title2: Contract Devil (Phistophilus)
CR: 10
sources:
- name: Bestiary 3
  page: 76
  link: http://paizo.com/products/btpy8odu?Pathfinder-Roleplaying-Game-Bestiary-3
- name: 'Pathfinder #12: Crown of Fangs'
  page: 86
  link: http://paizo.com/pathfinder/adventurePath/curseOfTheCrimsonThrone/v5748btpy84el
XP: 9600
alignment: LE
size: Medium
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 11
senses:
  darkvision: 60
  see in darkness: true
AC:
  AC: 25
  touch: 18
  flat_footed: 17
  components:
    dex: 7
    dodge: 1
    natural: 7
HP:
  HP: 136
  long: 13d10+65
saves:
  fort: 9
  ref: 15
  will: 16
DR:
- amount: 10
  weakness: good
immunities:
- fire
- mind-affecting effects
- poison
resistances:
  acid: 10
  cold: 10
SR: 21
speeds:
  base: 30
attacks:
  melee:
  - - text: binding contract (whip) +20/+15/+10 (1d4+7 plus bleed and grab)
      entries:
      - - damage: 1d4+7
        - effect: bleed
        - effect: grab
      attack: binding contract (whip)
      bonus:
      - 20
      - 15
      - 10
    - text: gore +11 (2d6+1)
      entries:
      - - damage: 2d6+1
      attack: gore
      bonus:
      - 11
  special:
  - binding contract
  - bleed (1d6)
  - impale (2d8+4)
space: 5
reach: 5
reach_other: 10 ft. with binding contract
spell_like_abilities:
  entries:
  - name: tongues
    source: default
    freq: Constant
  - name: bestow curse
    source: default
    freq: At will
    DC: 20
  - name: detect thoughts
    source: default
    freq: At will
    DC: 18
  - name: dimension door
    source: default
    freq: At will
  - name: erase
    source: default
    freq: At will
  - name: identify
    source: default
    freq: At will
  - name: major image
    source: default
    freq: At will
    DC: 19
  - name: produce flame
    source: default
    freq: At will
  - name: sending
    source: default
    freq: At will
  - name: arcane eye
    source: default
    freq: 3/day
  - name: break enchantment
    source: default
    freq: 3/day
  - name: greater teleport
    source: default
    freq: 3/day
    other: self plus 50 lbs. of objects only
  - name: hold person
    source: default
    freq: 3/day
    DC: 19
  - name: locate creature
    source: default
    freq: 3/day
  - name: mage's private sanctum
    source: default
    freq: 3/day
  - name: scorching ray
    source: default
    freq: 3/day
  - name: silence
    source: default
    freq: 3/day
    DC: 18
  - name: vision
    source: default
    freq: 3/day
  - name: contact other plane
    source: default
    freq: 1/day
  - name: delayed blast fireball
    source: default
    freq: 1/day
    DC: 23
  - name: dismissal
    source: default
    freq: 1/day
    DC: 21
  - name: plane shift
    source: default
    freq: 1/day
    DC: 23
  - name: summon
    source: default
    freq: 1/day
    level: 4
    summons:
    - name: bearded devils
      amount: 1d6
    - name: bone devil
      amount: 1
      chance: 50%
  - name: symbol of pain
    source: default
    freq: 1/day
    DC: 21
  sources:
  - name: default
    CL: 13
    concentration: 19
ability_scores:
  STR: 17
  DEX: 25
  CON: 20
  INT: 24
  WIS: 23
  CHA: 22
BAB: 13
CMB: 16
CMD: 34
feats:
- name: Alertness
- name: Deceitful
- name: Dodge
- name: Improved Initiative
- name: Iron Will
- name: Mobility
- name: Persuasive
skills:
  Bluff: 26
  Diplomacy: 26
  Disguise: 8
  Intimidate: 26
  Knowledge (arcana): 23
  Knowledge (nobility): 20
  Knowledge (planes): 23
  Knowledge (religion): 23
  Linguistics: 20
  Perception: 26
  Profession (scribe): 19
  Sense Motive: 26
  Sleight of Hand: 20
  Spellcraft: 20
languages:
- Abyssal
- Aklo
- Aquan
- Auran
- Celestial
- Common
- Draconic
- Dwarven
- Elven
- Giant
- Gnome
- Goblin
- Gnoll
- Halfling
- Ignan
- Infernal
- Orc
- Sylvan
- Terran
- Undercommon
- telepathy 100 ft.
- tongues
special_qualities:
- infernal contract
- infernal investment
ecology:
  environment: any (Hell)
  organization: solitary, pair, or court (2-12)
  treasure_type: standard
special_abilities:
  Binding Contract (Su): All contract devils carry numerous lengthy contracts draped
    over their horns or within their numerous carrying cases. They can wield these
    contracts like whips, but deal lethal damage regardless of the armor bonus of
    their target. A contract devil modifies attack and damage rolls when using a binding
    contract by its Intelligence modifier, not its Strength modifier (this equates
    to a +7 bonus for most contract devils). Wounds created by a binding contract
    resemble horrifically deep paper cuts and cause 1d6 points of bleed damage. A
    contract devil can use its binding contract to disarm and trip foes as if the
    contract were a whip. If it is itself disarmed of the contract, the devil can
    rearm itself with a new contract as an immediate action.
  Impale (Ex): As a swift action, a contract devil can impale an opponent grappled
    by its binding contract, dealing 2d8+4 points of piercing damage.
  Infernal Contract (Su): As a full-round action, a contract devil can produce an
    infernal contract for a single living mortal creature. This contract can grant
    a wide range of abilities and effects, as detailed on the following page. To receive
    any of these bonuses, however, the mortal must sign its true name to the document
    of its own free will. Upon doing so, that mortal's soul is sworn to the contract
    devil, condemning the soul to an eternity of servitude in Hell rather than whatever
    fate would naturally befall it upon the mortal's death. Breaking a contract with
    a contract devil is difficult and dangerous (see the next page); as long as the
    infernal contract remains in effect, the victim cannot be restored to life after
    death save by a miracle or a wish. If a mortal is restored to life in this way,
    the contract devil immediately senses the development-it not only knows which
    soul has been restored to life, but also gains the benefits of a discern location
    spell targeted on the character or creature that restored the damned soul to life.
  Infernal Investment (Su): As a subclause of all infernal contracts, a contract devil
    can use greater scrying at will upon any creature it has a contract with. The
    target creature always fails its save against the devil's scrying attempt-this
    ability otherwise functions at caster level 20th.
desc_long: |-
  A contract devil, also a called phistophilus, always appears handsome and confident, its chiseled features housing a perpetually smug grin. Contract devils have red skin and black hair and stand near 6-1/2 feet in height, not counting their horns. The thicket of horns around a contract devil's body increases its height to 7 feet and its weight to 350 pounds.

  They exist to keep track of the damned, to manage Hell's endless ordinances, and, when time and opportunity permit, to coax mortals into damnation. Most phistophiluses spend their eternities in the various courts of Hell's nine layers, particularly in the maze-like fortress-libraries where all infernal laws and oaths are recorded. Occasionally they serve similar roles on the Material Plane when summoned by particularly desperate, arrogant, or foolish mortals.

  When one of the souls damned by a contract devil is restored to life (typically via powerful magic like a wish or miracle), the phistophilus immediately notices the transgression. Usually, the contract devil recruits the aid of more powerful allies to track down and punish such transgressors and to collect the escaped soul as quickly as possible.

---

# Devil, Contract Devil (Phistophilus)
With rust-colored skin and a jutting crown of ridge-like horns, this muscular devil is draped in lengthy contracts.
**Source** Bestiary 3 pg. 76, Pathfinder #12: _[[items/Wondrous Item/Crown of Fangs|Crown of Fangs]]_ pg. 86
**XP** 9,600

LE Medium outsider (devil, evil, extraplanar, lawful)
**Init** +11; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +26

##### Defense

**AC** 25, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+7 Dex, +1 _[[feats/Dodge|dodge]]_, +7 natural)
**hp** 136 (13d10+65)
**Fort** +9, **Ref** +15, **Will** +16
**DR** 10/good; **Immune** fire, mind-affecting effects, poison; **Resist** acid 10, cold 10; **SR** 21

##### Offense
**Speed** 30 ft.
**Melee** _[[spells/Binding|binding]]_ contract (_[[items/Weapon/Whip|whip]]_) +20/+15/+10 (1d4+7 plus _[[universal monster rules/Bleed|bleed]]_ and _[[universal monster rules/Grab|grab]]_), gore +11 (2d6+1)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _binding_ contract)
**Special Attacks** _binding_ contract, _bleed_ (1d6), impale (2d8+4)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +19)
Constant—_[[spells/Tongues|tongues]]_
At will—_[[spells/Bestow Curse|bestow curse]]_ (DC 20), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), _[[spells/Dimension Door|dimension door]]_, _[[spells/Erase|erase]]_, _[[spells/Identify|identify]]_, _[[spells/Major Image|major image]]_ (DC 19), _[[spells/Produce Flame|produce flame]]_, _[[spells/Sending|sending]]_
3/day—_[[spells/Arcane Eye|arcane eye]]_, _[[spells/Break Enchantment|break enchantment]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Hold Person|hold person]]_ (DC 19), _[[spells/Locate Creature|locate creature]]_, mage’s private sanctum, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Silence|silence]]_ (DC 18), _[[spells/Vision|vision]]_
1/day—_[[spells/Contact Other Plane|contact other plane]]_, _[[spells/Delayed Blast Fireball|delayed blast fireball]]_ (DC 23), _[[spells/Dismissal|dismissal]]_ (DC 21), _[[spells/Plane Shift|plane shift]]_ (DC 23), _[[universal monster rules/Summon|summon]]_ (level 4, 1d6 bearded devils or 1 bone devil 50%), _[[spells/Symbol of Pain|symbol of pain]]_ (DC 21)

##### Statistics
**Str** 17, **Dex** 25, **Con** 20, **Int** 24, **Wis** 23, **Cha** 22
**Base Atk** +13; **CMB** +16; **CMD** 34
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Deceitful|Deceitful]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Persuasive|Persuasive]]_
**Skills** Bluff +26, Diplomacy +26, Disguise +8, Intimidate +26, Knowledge (arcana) +23, Knowledge (nobility) +20, Knowledge (planes) +23, Knowledge (religion) +23, Linguistics +20, Perception +26, Profession (scribe) +19, Sense Motive +26, Sleight of Hand +20, Spellcraft +20
**Languages** Abyssal, Aklo, Aquan, Auran, Celestial, Common, Draconic, Dwarven, Elven, Giant, Gnome, _[[monsters/Goblin|Goblin]]_, _[[monsters/Gnoll|Gnoll]]_, Halfling, Ignan, Infernal, _[[monsters/Orc|Orc]]_, Sylvan, Terran, Undercommon; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft., _tongues_
**SQ** infernal contract, infernal investment

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or court (2–12)
**Treasure** standard

### Special Abilities

**_Binding_ Contract (Su)** All contract devils carry numerous lengthy contracts draped over their horns or within their numerous carrying cases. They can wield these contracts like whips, but deal lethal damage regardless of the armor bonus of their target. A contract devil modifies attack and damage rolls when using a _binding_ contract by its Intelligence modifier, not its Strength modifier (this equates to a +7 bonus for most contract devils). Wounds created by a _binding_ contract resemble horrifically deep paper cuts and cause 1d6 points of _bleed_ damage. A contract devil can use its _binding_ contract to disarm and _[[universal monster rules/Trip|trip]]_ foes as if the contract were a _whip_. If it is itself disarmed of the contract, the devil can rearm itself with a new contract as an immediate action.

**Impale (Ex)** As a swift action, a contract devil can impale an opponent _[[conditions/Grappled|grappled]]_ by its _binding_ contract, dealing 2d8+4 points of piercing damage.

**Infernal Contract (Su) **As a full-round action, a contract devil can produce an infernal contract for a single living mortal creature. This contract can grant a wide range of abilities and effects, as detailed on the following page. To receive any of these bonuses, however, the mortal must sign its _[[feats/True Name|true name]]_ to the document of its own free will. Upon doing so, that mortal’s soul is sworn to the contract devil, condemning the soul to an eternity of servitude in Hell rather than whatever fate would naturally befall it upon the mortal’s death. _[[items/Weapon Magic Abilities/Breaking|Breaking]]_ a contract with a contract devil is difficult and dangerous (see the next page); as long as the infernal contract remains in effect, the victim cannot be restored to life after death save by a _[[spells/Miracle|miracle]]_ or a _[[spells/Wish|wish]]_. If a mortal is restored to life in this way, the contract devil immediately senses the development—it not only knows which soul has been restored to life, but also gains the benefits of a _[[spells/Discern Location|discern location]]_ spell targeted on the character or creature that restored the _[[feats/Damned|damned]]_ soul to life.

**Infernal Investment (Su)** As a subclause of all infernal contracts, a contract devil can use greater _[[spells/Scrying|scrying]]_ at will upon any creature it has a contract with. The target creature always fails its save against the devil’s _scrying_ attempt—this ability otherwise functions at caster level 20th.

##### Description

A contract devil, also a _[[items/Weapon Magic Abilities/Called|called]]_ phistophilus, always appears handsome and confident, its chiseled features housing a perpetually smug grin. Contract devils have red skin and black hair and stand near 6-1/2 feet in height, not counting their horns. The thicket of horns around a contract devil’s body increases its height to 7 feet and its weight to 350 pounds.

They exist to keep track of the _damned_, to manage Hell’s endless ordinances, and, when time and opportunity permit, to coax mortals into _[[spells/Damnation|damnation]]_. Most phistophiluses spend their eternities in the various courts of Hell’s nine layers, particularly in the maze-like fortress-libraries where all infernal laws and oaths are recorded. Occasionally they serve similar roles on the Material Plane when summoned by particularly desperate, arrogant, or foolish mortals.

When one of the souls _damned_ by a contract devil is restored to life (typically via powerful magic like a _wish_ or _miracle_), the phistophilus immediately notices the transgression. Usually, the contract devil _[[feats/Recruits|recruits]]_ the aid of more powerful allies to track down and punish such transgressors and to collect the escaped soul as quickly as possible.