---
cssclass: [monsters]
title1: Kaicharek
desc_short: This grotesque, crimson wormlike creature has a circular mouth full of
  fangs. A pair of segmented tentacles sporting razor-edged ridges protrudes from
  the sides of its mouth.
title2: Kaicharek
CR: 4
sources:
- name: 'Pathfinder #139: The Dead Road'
  page: 84
  link: https://paizo.com/products/btq01ws3
XP: 1200
alignment: NE
size: Medium
type: magical beast
subtypes:
- extraplanar
initiative:
  bonus: 2
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 17
  touch: 12
  flat_footed: 15
  components:
    dex: 2
    natural: 5
HP:
  HP: 42
  long: 5d10+15
saves:
  fort: 7
  ref: 6
  will: 4
speeds:
  base: 20
  burrow: 20
  climb: 20
attacks:
  melee:
  - - text: bite +7 (1d6+2 plus grab)
      entries:
      - - damage: 1d6+2
        - effect: grab
      attack: bite
      bonus:
      - 7
    - text: 2 tentacles +2 (1d4+1 plus 1d4 bleed)
      entries:
      - - damage: 1d4+1
        - damage: 1d4
          type: bleed
      count: 2
      attack: tentacles
      bonus:
      - 2
  special:
  - blood drain (1 Constitution)
  - impaling thrust
  - slashing talons
spell_like_abilities:
  entries:
  - name: hidden presence
    source: default
    freq: 3/day
    DC: 13
  sources:
  - name: default
    CL: 5
    concentration: 7
ability_scores:
  STR: 14
  DEX: 15
  CON: 16
  INT: 11
  WIS: 13
  CHA: 14
BAB: 5
CMB: 7
CMB_other: +11 grapple
CMD: 19
feats:
- name: Combat Reflexes
- name: Iron Will
- name: Skill Focus (Stealth)
skills:
  Climb: 15
  Perception: 7
  Stealth: 13
languages:
- Abyssal (can't speak)
special_qualities:
- hidden feeding
ecology:
  environment: any (Blood Vale)
  organization: solitary, pair, or cluster (3-6)
  treasure_type: none
special_abilities:
  Hidden Feeding (Ex): When a kaicharek hits with its bite attack against a target
    of its size or larger that is unaware of its presence, it latches onto its target
    and automatically grapples. The kaicharek loses its Dexterity bonus to AC (reducing
    its AC to 15), but it holds on with great tenacity and automatically inflicts
    its blood drain each round. A kaicharek has a +8 racial bonus to maintain its
    grapple on a foe once it is attached. An attached kaicharek can still be attacked.
    The grappled creature remains unaware of the kaicharek as if under the effects
    of the kaicharek's hidden presence spell-like ability, but it can attempt a DC
    15 Will save to notice the signs of the kaicharek's feeding. The grappled creature
    gains a cumulative +1 bonus on its Will save for every round the kaicharek remains
    attached. Other creatures can notice the kaicharek by succeeding at a DC 15 Perception
    check. The DC is Constitution-based.
  Impaling Thrust (Ex): A kaicharek can engage specific muscles in its body to violently
    thrust its bladed tentacles out at foes as a swift action. For the following round,
    the kaicharek increases the reach of its tentacle attacks to 10 feet. This act
    misaligns the musculature of its tentacles and the kaicharek thereafter loses
    the use of its tentacle attacks until it spends a move action to retract them.
  Slashing Talons (Ex): The tips of a kaicharek's tentacles are covered in serrated
    bone blades, causing them to deal slashing damage and bleed damage instead of
    bludgeoning damage.
desc_long: |-
  With slashing tentacles and a blood-hungry maw, kaichareks lie in wait for the foolish entering Achaekek's realm, ambushing and exsanguinating the weak and grabbing a quick meal from the strong. This latter feature has earned kaichareks the name “parasites of Achaekek.” Though hardly the strongest creatures associated with the Mantis God, kaichareks are vicious yet cowardly creatures that seem to live for the anguish and bloodshed they unleash on the world around them.

   A typical kaicharek is 5 feet long and weighs 270 pounds.

---

# Kaicharek
This grotesque, crimson wormlike creature has a circular mouth full of fangs. A pair of segmented tentacles sporting razor-edged ridges protrudes from the sides of its mouth.
**Source** Pathfinder #139: The Dead Road pg. 84
**XP** 1,200

NE Medium magical beast (extraplanar)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +7

##### Defense

**AC** 17, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+2 Dex, +5 natural)
**hp** 42 (5d10+15)
**Fort** +7, **Ref** +6, **Will** +4

##### Offense
**Speed** 20 ft., _[[universal monster rules/Burrow|burrow]]_ 20 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** bite +7 (1d6+2 plus _[[universal monster rules/Grab|grab]]_), 2 tentacles +2 (1d4+1 plus 1d4 _[[universal monster rules/Bleed|bleed]]_)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_ (1 Constitution), impaling thrust, slashing talons
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +7)
3/day—_[[spells/Hidden Presence|hidden presence]]_ (DC 13)

##### Statistics
**Str** 14, **Dex** 15, **Con** 16, **Int** 11, **Wis** 13, **Cha** 14
**Base Atk** +5; **CMB** +7 (+11 grapple); **CMD** 19
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth)
**Skills** _Climb_ +15, Perception +7, Stealth +13
**Languages** Abyssal (can't speak)
**SQ** hidden feeding

##### Ecology

**Environment** any (Blood Vale)
**Organization** solitary, pair, or cluster (3-6)
**Treasure** none

### Special Abilities

**Hidden Feeding (Ex)** When a _[[monsters/Kaicharek|kaicharek]]_ hits with its bite attack against a target of its size or larger that is unaware of its presence, it latches onto its target and automatically grapples. The _kaicharek_ loses its Dexterity bonus to AC (reducing its AC to 15), but it holds on with great tenacity and automatically inflicts its _blood drain_ each round. A _kaicharek_ has a +8 racial bonus to maintain its grapple on a foe once it is attached. An attached _kaicharek_ can still be attacked. The _[[conditions/Grappled|grappled]]_ creature remains unaware of the _kaicharek_ as if under the effects of the _kaicharek_'s _hidden presence_ spell-like ability, but it can attempt a DC 15 Will save to notice the signs of the _kaicharek_'s feeding. The _grappled_ creature gains a cumulative +1 bonus on its Will save for every round the _kaicharek_ remains attached. Other creatures can notice the _kaicharek_ by succeeding at a DC 15 Perception check. The DC is Constitution-based.

**Impaling Thrust (Ex)** A _kaicharek_ can engage specific muscles in its body to violently thrust its bladed tentacles out at foes as a swift action. For the following round, the _kaicharek_ increases the reach of its tentacle attacks to 10 feet. This act misaligns the musculature of its tentacles and the _kaicharek_ thereafter loses the use of its tentacle attacks until it spends a move action to retract them.
**Slashing Talons (Ex)** The tips of a _kaicharek_'s tentacles are covered in serrated bone blades, causing them to deal slashing damage and _bleed_ damage instead of bludgeoning damage.

##### Description

With slashing tentacles and a blood-hungry maw, kaichareks lie in wait for the foolish entering Achaekek's realm, ambushing and exsanguinating the weak and grabbing a quick meal from the strong. This latter feature has earned kaichareks the name “parasites of Achaekek.” Though hardly the strongest creatures associated with the Mantis God, kaichareks are _[[items/Weapon Magic Abilities/Vicious|vicious]]_ yet cowardly creatures that seem to live for the anguish and bloodshed they unleash on the world around them.

A typical _kaicharek_ is 5 feet long and weighs 270 pounds.