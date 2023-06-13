---
cssclass: [monsters]
title1: Star Monarch
desc_short: This brilliantly colored moth rises taller than a house. A long tail resembling
  peacock feathers trails behind the creature.
title2: Star Monarch
CR: 9
sources:
- name: Inner Sea Bestiary
  page: 50
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 6400
alignment: CG
size: Huge
type: magical beast
initiative:
  bonus: 10
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: dreamwarden
  radius: 30
AC:
  AC: 22
  touch: 15
  flat_footed: 15
  components:
    dex: 6
    dodge: 1
    natural: 7
    size: -2
HP:
  HP: 114
  long: 12d10+48
saves:
  fort: 12
  ref: 14
  will: 9
DR:
- amount: 5
  weakness: silver
immunities:
- cold
SR: 20
speeds:
  base: 30
  other_semicolon: starflight
  fly: 80
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 claws +14 (1d8+4 plus grab)
      entries:
      - - damage: 1d8+4
        - effect: grab
      count: 2
      attack: claws
      bonus:
      - 14
    - text: tail +14 (2d6+4 nonlethal)
      entries:
      - - damage: 2d6+4
          type: nonlethal
      attack: tail
      bonus:
      - 14
  special:
  - glowsap
  - rake (4 claws +10, 1d6+3)
space: 15
reach: 5
reach_other: 15 ft. with tail
spell_like_abilities:
  entries:
  - name: entropic shield
    source: default
    freq: Constant
  - name: dancing lights
    source: default
    freq: At will
  - superscripts:
    - APG
    name: restful sleep
    source: default
    freq: At will
  - name: deep slumber
    source: default
    freq: 3/day
    DC: 17
  - name: dream
    source: default
    freq: 3/day
  - superscripts:
    - APG
    name: wandering star motes
    source: default
    freq: 3/day
    DC: 18
  - superscripts:
    - APG
    name: cloak of dreams
    source: default
    freq: 1/day
    DC: 20
  sources:
  - name: default
    CL: 12
    concentration: 16
ability_scores:
  STR: 18
  DEX: 23
  CON: 18
  INT: 11
  WIS: 17
  CHA: 18
BAB: 12
CMB: 18
CMB_other: +22 grapple
CMD: 35
CMD_other: 43 vs. trip
feats:
- name: Alertness
- name: Dodge
- name: Flyby Attack
- name: Hover
- name: Improved Initiative
- name: Iron Will
skills:
  Fly: 14
  Perception: 16
  Sense Motive: 12
languages:
- Common (can't speak)
- telepathy touch
special_qualities:
- navigational awareness
- no breath
- toxic flesh
ecology:
  environment: any (Varisia)
  organization: solitary, pair, or rabble (3-6)
  treasure_type: none
special_abilities:
  Dreamwarden (Su): Any sleeping creature within 30 feet of a star monarch is protected
    by protection from evil and sanctuary (Will DC 15 negates). The save DC is Constitution-based.
  Glowsap (Ex): As a standard action, a star monarch can spray a target within 30
    feet with an adhesive spittle as a ranged touch attack. A creature struck is affected
    as a tanglefoot bag (Reflex DC 20 partial; see Core Rulebook 160). In addition,
    this adhesive glows under starlight or moonlight, limning the target as faerie
    fire if used outdoors at night. The save DC is Constitution-based.
  Navigational Awareness (Ex): Star monarchs never become lost and are immune to maze
    spells or any effect that would cause them to lose their sense of direction.
  Starflight (Su): A star monarch can survive in the void of outer space. It flies
    through space at an incredible speed. Although exact travel times vary, a trip
    within a single solar system should take 3d20 hours, while a trip beyond should
    take 3d20 days (or more, at the GM's discretion).
  Toxic Flesh (Ex): A star monarch's flesh is poisonous. A creature biting it or ingesting
    any part of its body becomes sickened for 1d4 rounds (Fortitude DC 20 negates)
    and is affected as if it had consumed a dose of arsenic (Core Rulebook 558).
desc_long: Star monarchs are magical emissaries of Desna, the guide and protector
  of those who wander and guardian of dreams. They fly in glowing clouds through the
  void of space, visiting Golarion to watch over the faithful of Desna. Star monarchs
  spin streamers of sticky silver, weaving evanescent gossamer cocoons to enrobe those
  who slumber under their protection. These cocoons sublimate into wisps of half-remembered
  dreams with the coming of dawn. Star monarchs rarely intervene directly in combat,
  more often helping good creatures by aiding them from the shadows, guiding their
  paths, or guarding them while they sleep. Star monarchs can be found across Golarion
  in a variety of iridescent hues, and all are sacred to followers of the Song of
  the Spheres.

---

# Star Monarch
This brilliantly colored moth rises taller than a house. A long tail resembling peacock feathers trails behind the creature.
**Source** Inner Sea Bestiary pg. 50
**XP** 6,400

CG Huge magical beast
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +16
**Aura** dreamwarden (30 ft.)

##### Defense

**AC** 22, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+6 Dex, +1 dodge, +7 natural, –2 size)
**hp** 114 (12d10+48)
**Fort** +12, **Ref** +14, **Will** +9
**DR** 5/silver; **Immune** cold; **SR** 20

##### Offense
**Speed** 30 ft., fly 80 ft. (average); starflight
**Melee** 2 claws +14 (1d8+4 plus _[[universal monster rules/Grab|grab]]_), tail +14 (2d6+4 nonlethal)
**Space** 15 ft., **Reach** 5 ft. (15 ft. with tail)
**Special Attacks** glowsap, _[[universal monster rules/Rake|rake]]_ (4 claws +10, 1d6+3)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
Constant—_[[spells/Entropic Shield|entropic shield]]_
At will—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Restful Sleep|restful sleep]]_
3/day—_[[spells/Deep Slumber|deep slumber]]_ (DC 17), _[[spells/Dream|dream]]_, _[[spells/Wandering Star Motes|wandering star motes]]_ (DC 18)
1/day—_[[spells/Cloak of Dreams|cloak of dreams]]_ (DC 20)

##### Statistics
**Str** 18, **Dex** 23, **Con** 18, **Int** 11, **Wis** 17, **Cha** 18
**Base Atk** +12; **CMB** +18 (+22 grapple); **CMD** 35 (43 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_
**Skills** Fly +14, Perception +16, Sense Motive +12
**Languages** Common (can’t speak); _[[universal monster rules/Telepathy|telepathy]]_ touch
**SQ** navigational awareness, _[[universal monster rules/No Breath|no breath]]_, _[[items/Weapon Magic Abilities/Toxic|toxic]]_ flesh

##### Ecology

**Environment** any (Varisia)
**Organization** solitary, pair, or rabble (3–6)
**Treasure** none

### Special Abilities

**Dreamwarden (Su)** Any sleeping creature within 30 feet of a _[[monsters/Star Monarch|star monarch]]_ is protected by _[[spells/Protection From Evil|protection from evil]]_ and _[[spells/Sanctuary|sanctuary]]_ (Will DC 15 negates). The save DC is Constitution-based.

**Glowsap (Ex)** As a standard action, a _star monarch_ can spray a target within 30 feet with an _[[spells/Adhesive Spittle|adhesive spittle]]_ as a ranged touch attack. A creature struck is affected as a _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_ (Reflex DC 20 partial; see Core Rulebook 160). In addition, this _[[items/Armor Magic Abilities/Adhesive|adhesive]]_ glows under starlight or moonlight, _[[items/Weapon Magic Abilities/Limning|limning]]_ the target as _[[spells/Faerie Fire|faerie fire]]_ if used outdoors at night. The save DC is Constitution-based.

**Navigational Awareness (Ex) **Star monarchs never become lost and are immune to _[[spells/Maze|maze]]_ spells or any effect that would cause them to lose their sense of direction.
**Starflight (Su) **A _star monarch_ can survive in the void of outer space. It flies through space at an incredible speed. Although exact travel times vary, a _trip_ within a single solar system should take 3d20 hours, while a _trip_ beyond should take 3d20 days (or more, at the GM’s discretion).

**_Toxic_ Flesh (Ex) **A _star monarch_’s flesh is poisonous. A creature biting it or ingesting any part of its body becomes _[[conditions/Sickened|sickened]]_ for 1d4 rounds (Fortitude DC 20 negates) and is affected as if it had consumed a dose of _[[poisons/Arsenic|arsenic]]_ (Core Rulebook 558).

##### Description

Star monarchs are magical emissaries of Desna, the guide and protector of those who wander and _[[items/Weapon Magic Abilities/Guardian|guardian]]_ of dreams. They fly in glowing clouds through the void of space, visiting Golarion to watch over the faithful of Desna. Star monarchs spin streamers of _[[items/Weapon Magic Abilities/Sticky|sticky]]_ silver, weaving evanescent gossamer cocoons to enrobe those who slumber under their protection. These cocoons sublimate into wisps of half-remembered dreams with the coming of dawn. Star monarchs rarely intervene directly in combat, more often helping good creatures by aiding them from the shadows, guiding their paths, or _[[items/Armor Magic Abilities/Guarding|guarding]]_ them while they sleep. Star monarchs can be found across Golarion in a variety of iridescent hues, and all are _[[items/Weapon Magic Abilities/Sacred|sacred]]_ to followers of the Song of the Spheres.