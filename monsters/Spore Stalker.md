---
cssclass: [monsters]
title1: Spore Stalker
desc_short: This fungoid canine creature skitters forward on many segmented legs,
  a gurgling growl issuing from its fanged maw.
title2: Spore Stalker
CR: 7
sources:
- name: Seers of the Drowned City
  page: 62
  link: http://paizo.com/products/btpy9op2?Pathfinder-Module-Seers-of-the-Drowned-City
XP: 3200
alignment: NE
size: Medium
type: plant
initiative:
  bonus: 7
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 20
  touch: 13
  flat_footed: 17
  components:
    dex: 3
    natural: 7
HP:
  HP: 85
  long: 9d8+45
saves:
  fort: 11
  ref: 6
  will: 5
defensive_abilities:
- reactive escape
immunities:
- plant traits
speeds:
  base: 40
  climb: 30
attacks:
  melee:
  - - text: bite +14 (2d6+12 plus grab)
      entries:
      - - damage: 2d6+12
        - effect: grab
      attack: bite
      bonus:
      - 14
  special:
  - colonize victim
  - paralytic spores
spell_like_abilities:
  entries:
  - name: ethereal jaunt
    source: default
    freq: 3/day
    other: self only
  sources:
  - name: default
    CL: 7
    concentration: 6
ability_scores:
  STR: 26
  DEX: 16
  CON: 20
  INT: 7
  WIS: 15
  CHA: 9
BAB: 6
CMB: 14
CMB_other: +18 grapple
CMD: 27
CMD_other: can't be tripped
feats:
- name: Improved Initiative
- name: Power Attack
- name: Skill Focus (Stealth)
- name: Step Up
- name: Vital Strike
skills:
  Climb: 16
  Perception: 14
  Stealth: 14
  Survival: 10
  _racial_mods:
    Stealth:
      _: 8
    Survival:
      _: 8
languages:
- Aklo
- telepathy 100 ft.
ecology:
  environment: warm swamps
  organization: solitary, pair, or pack (3-12)
  treasure_type: incidental
special_abilities:
  Colonize Victim (Ex): As a standard action, a spore stalker can inject spores into
    the body of a Small or larger living, corporeal, nonplant creature that is pinned
    or helpless. The victim can resist the spores' infestation with a successful DC
    19 Fortitude save. If it fails this save, the victim takes 1d2 points of Constitution
    drain per round for 6 rounds but can attempt a new DC 19 Fortitude save to end
    the effect each round, similar to saving against a poison (although this is not
    a poison effect). Multiple colonizations do not increase the Constitution damage
    or save DC, but they do increase the duration of the effect by 6 rounds per infestation.
    A creature that perishes from this Constitution damage splits open, and a fully
    grown spore stalker crawls from the rapidly decaying remains. This is an infestation
    effect. The save DC is Constitution-based.
  Paralytic Spores (Ex): When a spore stalker is hit by a melee or ranged weapon,
    it can release a cloud of paralytic spores in a 5-foot radius around itself as
    an immediate action. Any creature within range when the cloud is released must
    succeed at a DC 19 Fortitude save or be paralyzed for 1d3 rounds. At the start
    of a creature's turn, it can attempt a new DC 19 Fortitude save as a standard
    action to end this paralysis effect early. This is a poison effect; the save DC
    is Constitution-based.
  Reactive Escape (Su): Whenever a spore stalker is hit by a melee or ranged weapon,
    it can teleport up to 30 feet in any direction as an immediate action. This ability
    otherwise functions as per dimension door (CL 7th).
desc_long: Capable of spreading and colonizing with disturbing speed, a spore stalker
  and its kin can quickly overrun an area. Fortunately, a spore stalker's life span
  is relatively short; a typical spore stalker perishes of natural causes in only
  a few weeks. Spore stalkers are often used by mi-go or agents of the Dominion of
  the Black as biological weapons against unsuspecting citizens of newly discovered
  planets.

---

# Spore Stalker
This fungoid canine creature skitters forward on many segmented legs, a gurgling growl issuing from its fanged maw.
**Source** Seers of the Drowned City pg. 62
**XP** 3,200

NE Medium plant
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +14

##### Defense

**AC** 20, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+3 Dex, +7 natural)
**hp** 85 (9d8+45)
**Fort** +11, **Ref** +6, **Will** +5
**Defensive Abilities** reactive escape; **Immune** _[[universal monster rules/Plant Traits|plant traits]]_

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** bite +14 (2d6+12 plus _[[universal monster rules/Grab|grab]]_)
**Special Attacks** colonize victim, paralytic spores
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +6)
3/day—_[[spells/Ethereal Jaunt|ethereal jaunt]]_ (self only)

##### Statistics
**Str** 26, **Dex** 16, **Con** 20, **Int** 7, **Wis** 15, **Cha** 9
**Base Atk** +6; **CMB** +14 (+18 grapple); **CMD** 27 (can't be tripped)
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Step Up|Step Up]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** _Climb_ +16, Perception +14, Stealth +14, Survival +10; **Racial Modifiers** +8 Stealth, +8 Survival
**Languages** Aklo; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** warm swamps
**Organization** solitary, pair, or pack (3-12)
**Treasure** incidental

### Special Abilities

**Colonize Victim (Ex)** As a standard action, a _[[monsters/Spore Stalker|spore stalker]]_ can inject spores into the body of a Small or larger living, corporeal, nonplant creature that is _[[conditions/Pinned|pinned]]_ or _[[conditions/Helpless|helpless]]_. The victim can resist the spores’ infestation with a successful DC 19 Fortitude save. If it fails this save, the victim takes 1d2 points of Constitution drain per round for 6 rounds but can attempt a new DC 19 Fortitude save to end the effect each round, similar to saving against a poison (although this is not a poison effect). Multiple colonizations do not increase the Constitution damage or save DC, but they do increase the duration of the effect by 6 rounds per infestation. A creature that perishes from this Constitution damage splits open, and a fully grown _spore stalker_ crawls from the rapidly decaying remains. This is an infestation effect. The save DC is Constitution-based.

**Paralytic Spores (Ex)** When a _spore stalker_ is hit by a melee or ranged weapon, it can release a cloud of paralytic spores in a 5-foot radius around itself as an immediate action. Any creature within range when the cloud is released must succeed at a DC 19 Fortitude save or be _[[conditions/Paralyzed|paralyzed]]_ for 1d3 rounds. At the start of a creature’s turn, it can attempt a new DC 19 Fortitude save as a standard action to end this _[[universal monster rules/Paralysis|paralysis]]_ effect early. This is a poison effect; the save DC is Constitution-based.

**Reactive Escape (Su)** Whenever a _spore stalker_ is hit by a melee or ranged weapon, it can teleport up to 30 feet in any direction as an immediate action. This ability otherwise functions as per _[[spells/Dimension Door|dimension door]]_ (CL 7th).

##### Description

Capable of spreading and colonizing with disturbing speed, a _spore stalker_ and its kin can quickly overrun an area. Fortunately, a _spore stalker_’s life span is relatively short; a typical _spore stalker_ perishes of natural causes in only a few weeks. Spore stalkers are often used by _[[monsters/Mi-go|mi-go]]_ or agents of the Dominion of the Black as biological weapons against unsuspecting citizens of newly discovered planets.