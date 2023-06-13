---
cssclass: [monsters]
title1: Herald, Arcanotheign
desc_short: This cloud of swirling energy flickers like lightning, with raw magical
  power playing across its form.
title2: Arcanotheign
CR: 15
sources:
- name: Inner Sea Gods
  page: 298
  link: http://paizo.com/products/btpy94wj?Pathfinder-Campaign-Setting-Inner-Sea-Gods-Hardcover
- name: 'Pathfinder #41: The Thousand Fangs Below'
  page: 82
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/serpentsSkull/v5748btpy8i8r
XP: 51200
alignment: N
size: Medium
type: outsider
subtypes:
- herald
- incorporeal
initiative:
  bonus: 12
senses:
  blindsense: 60
  darkvision: 60
  arcane sight: 120
auras:
- name: energy channel
  radius: 30
  DC: 26
AC:
  AC: 27
  touch: 27
  flat_footed: 18
  components:
    deflection: 8
    dex: 8
    dodge: 1
HP:
  HP: 195
  long: 17d10+102
saves:
  fort: 18
  ref: 13
  will: 17
  other: +2 vs. chaos/evil/good/law
defensive_abilities:
- incorporeal
immunities:
- poison
resistances:
  acid: 30
  cold: 30
  divine power: 30
  divine power_other: such as from flame strike
  electricity: 30
  fire: 30
  sonic: 30
SR: 31
speeds:
  base: 40
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 2 incorporeal touches +25 (4d6 plus energy channel)
      entries:
      - - damage: 4d6
        - effect: energy channel
      count: 2
      attack: incorporeal touches
      bonus:
      - 25
  ranged:
  - - text: 2 eldritch blasts +25 touch (4d6 plus special)
      entries:
      - - damage: 4d6
        - effect: special
      count: 2
      attack: eldritch blasts
      bonus:
      - 25
      touch: true
spell_like_abilities:
  entries:
  - name: arcane sight
    source: default
    freq: Constant
  - name: protection from chaos/evil/good/law
    source: default
    freq: Constant
  - name: clairaudience/clairvoyance
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: cloudkill
    source: default
    freq: 3/day
    DC: 23
  - name: cure critical wounds
    source: default
    freq: 3/day
  - name: lightning bolt
    source: default
    freq: 3/day
    DC: 21
  - name: telekinesis
    source: default
    freq: 3/day
    DC: 23
  - name: harm
    source: default
    freq: 1/day
    DC: 24
  - name: heal
    source: default
    freq: 1/day
  - name: limited wish
    source: default
    freq: 1/day
    DC: 25
  - name: plane shift
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 17
    concentration: 25
ability_scores:
  STR:
  DEX: 27
  CON: 22
  INT: 31
  WIS: 20
  CHA: 27
BAB: 17
CMB: 25
CMD: 44
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Command Undead
- name: Dodge
- name: Great Fortitude
- name: Greater Spell Penetration
- name: Improved Initiative
- name: Iron Will
- name: Spell Penetration
skills:
  Craft (alchemy): 30
  Diplomacy: 25
  Fly: 36
  Heal: 22
  Intimidate: 25
  Knowledge (arcana): 30
  Knowledge (planes): 30
  Knowledge (religion): 30
  Knowledge (history): 27
  Linguistics: 27
  Perception: 25
  Perform (sing): 25
  Sense Motive: 25
  Spellcraft: 30
  Stealth: 28
  Use Magic Device: 28
languages:
- Abyssal
- Ancient Osiriani
- Celestial
- Common
- Draconic
- Infernal
- Protean
- telepathy 100 ft.
special_qualities:
- change shape (corporeal form)
ecology:
  environment: any (Maelstrom)
  organization: solitary
  treasure_type: standard
special_abilities:
  Corporeal Form (Ex): As an immediate action, the herald can take physical form,
    losing its incorporeal special quality and subtype and its deflection bonus to
    AC, but gaining a Strength score of 20 and a natural armor bonus equal to its
    incorporeal deflection bonus.
  Eldritch Blast (Su): |-
    The herald chooses an additional effect for its eldritch blasts each round (DC 26 negates). A creature that fails its saves against both blasts in the same round suffers an increased effect. The save DC is Charisma-based.

    Dement (Will): The creature is confused for 1 minute. Increased effect: The creature goes insane (as insanity).
     Displace (Fortitude): The creature teleports (as dimension door) 5 feet in a random horizontal direction at the end of its turn each round for the next 10 rounds. Increased effect: The creature is affected by maze.
     Ignite (Reflex): The creature takes 2d6 points of fire damage. Increased effect: The creature catches on fire.
  Energy Channel Aura (Su): On its turn, the herald can channel energy (Will DC 26
    half) to deal 2d6 points of acid, cold, electricity, or fire damage to each creature
    in its aura. A creature struck by its incorporeal touch attack also takes this
    damage (no saving throw). The save DC is Charisma-based.
desc_long: In its natural, incorporeal form, Nethys's herald is a storm of magic,
  immediately recognizable as a creature of the arcane and divine. It rises just over
  7 feet tall, and has a habit of floating a few inches above the ground instead of
  walking.

---

# Herald, Arcanotheign
This cloud of swirling energy flickers like lightning, with raw magical power playing across its form.
**Source** Inner Sea Gods pg. 298, Pathfinder #41: The Thousand Fangs Below pg. 82
**XP** 51,200

N Medium outsider (herald, _[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +12; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Arcane Sight|arcane sight]]_ 120 ft.; Perception +25
**Aura** _[[feats/Energy Channel|energy channel]]_ (30 ft., DC 26)

##### Defense

**AC** 27, touch 27, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+8 _[[spells/Deflection|deflection]]_, +8 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 195 (17d10+102)
**Fort** +18, **Ref** +13, **Will** +17; +2 vs. chaos/evil/good/law
**Defensive Abilities** _incorporeal_; **Immune** poison; **Resist** acid 30, cold 30, _[[spells/Divine Power|divine power]]_ 30 (such as from _[[spells/Flame Strike|flame strike]]_), electricity 30, fire 30, sonic 30; **SR** 31

##### Offense
**Speed** 40 ft., fly 60 ft. (perfect)
**Melee** 2 _incorporeal_ touches +25 (4d6 plus _energy channel_)
**Ranged** 2 eldritch blasts +25 touch (4d6 plus special)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +25)
Constant—_arcane sight_, protection from chaos/evil/good/law
At will—clairaudience/clairvoyance, greater teleport (self plus 50 lbs. of objects only)
3/day—_[[spells/Cloudkill|cloudkill]]_ (DC 23), _[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Lightning Bolt|lightning bolt]]_ (DC 21), _[[spells/Telekinesis|telekinesis]]_ (DC 23)
1/day—_[[spells/Harm|harm]]_ (DC 24), _[[spells/Heal|heal]]_, _[[spells/Limited Wish|limited wish]]_ (DC 25), _[[spells/Plane Shift|plane shift]]_ (DC 25)

##### Statistics
**Str** —, **Dex** 27, **Con** 22, **Int** 31, **Wis** 20, **Cha** 27
**Base Atk** +17; **CMB** +25; **CMD** 44
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[spells/Command Undead|Command Undead]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Spell Penetration|Greater Spell Penetration]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Spell Penetration|Spell Penetration]]_
**Skills** Craft (alchemy) +30, Diplomacy +25, Fly +36, _Heal_ +22, Intimidate +25, Knowledge (arcana, planes, religion) +30, Knowledge (history) +27, Linguistics +27, Perception +25, Perform (sing) +25, Sense Motive +25, Spellcraft +30, Stealth +28, Use Magic Device +28
**Languages** Abyssal, Ancient Osiriani, Celestial, Common, Draconic, Infernal, Protean; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (corporeal form)

##### Ecology

**Environment** any (Maelstrom)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Corporeal Form (Ex)** As an immediate action, the herald can take physical form, losing its _incorporeal_ special quality and subtype and its _deflection_ bonus to AC, but gaining a Strength score of 20 and a natural armor bonus equal to its _incorporeal_ _deflection_ bonus.

**Eldritch Blast (Su)** The herald chooses an additional effect for its eldritch blasts each round (DC 26 negates). A creature that fails its saves against both blasts in the same round suffers an increased effect. The save DC is Charisma-based.

Dement (Will): The creature is _[[conditions/Confused|confused]]_ for 1 minute. Increased effect: The creature goes insane (as _[[spells/Insanity|insanity]]_).
 Displace (Fortitude): The creature teleports (as _[[spells/Dimension Door|dimension door]]_) 5 feet in a random horizontal direction at the end of its turn each round for the next 10 rounds. Increased effect: The creature is affected by _[[spells/Maze|maze]]_.
 Ignite (Reflex): The creature takes 2d6 points of fire damage. Increased effect: The creature catches on fire.

**_Energy Channel_ Aura (Su)** On its turn, the herald can channel energy (Will DC 26 half) to deal 2d6 points of acid, cold, electricity, or fire damage to each creature in its aura. A creature struck by its _incorporeal_ touch attack also takes this damage (no saving throw). The save DC is Charisma-based.

##### Description

In its natural, _incorporeal_ form, Nethys’s herald is a storm of magic, immediately recognizable as a creature of the arcane and divine. It rises just over 7 feet tall, and has a habit of floating a few inches above the ground instead of walking.