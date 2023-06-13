---
cssclass: [monsters]
title1: Daemon, Genthodaemon
desc_short: 'Jagged bits of metal, armor, and sharp pieces of wire embed the flesh
  of this towering fiend. '
title2: Genthodaemon
CR: 5
sources:
- name: 'Pathfinder #71: Rasputin Must Die!'
  page: 86
  link: http://paizo.com/products/btpy8yv5?Pathfinder-Adventure-Path-71-Rasputin-Must-Die
XP: 1600
alignment: NE
size: Large
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 0
senses:
  darkvision: 60
auras:
- name: destruction
  radius: 30
AC:
  AC: 18
  touch: 9
  flat_footed: 18
  components:
    natural: 9
    size: -1
HP:
  HP: 51
  long: 6d10+18
saves:
  fort: 8
  ref: 5
  will: 3
defensive_abilities:
- barbed defense
DR:
- amount: 5
  weakness: good or silver
immunities:
- acid
- death effects
- disease
- poison
resistances:
  cold: 10
  electricity: 10
  fire: 10
speeds:
  base: 30
  fly: 30
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +10 (1d8+4)
      entries:
      - - damage: 1d8+4
      attack: bite
      bonus:
      - 10
    - text: 2 claws +10 (1d6+4 plus bleed 1d4)
      entries:
      - - damage: 1d6+4
        - damage: 1d4
          type: bleed
      count: 2
      attack: claws
      bonus:
      - 10
    - text: tail slap +4 (1d8+2 plus bleed 1d4)
      entries:
      - - damage: 1d8+2
        - damage: 1d4
          type: bleed
      attack: tail slap
      bonus:
      - 4
  ranged:
  - - text: 4 shrapnel +5 (1d6+4/19-20)
      entries:
      - - damage: 1d6+4
          crit_range: 19-20
      count: 4
      attack: shrapnel
      bonus:
      - 5
  special:
  - penetrating slivers
  - trample (1d6+6 plus bleed 1d4, DC 17)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: cause fear
    source: default
    freq: At will
    DC: 13
  - name: lesser confusion
    source: default
    freq: At will
    DC: 13
  - name: message
    source: default
    freq: At will
  - name: obscuring mist
    source: default
    freq: At will
  - name: crushing despair
    source: default
    freq: 1/day
    DC: 16
  - name: dispel magic
    source: default
    freq: 1/day
  - name: meld into stone
    source: default
    freq: 1/day
  - name: move earth
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 6
    concentration: 8
ability_scores:
  STR: 18
  DEX: 11
  CON: 16
  INT: 11
  WIS: 12
  CHA: 15
BAB: 6
CMB: 11
CMD: 21
feats:
- name: Power Attack
- name: Weapon Focus (bite)
- name: Weapon Focus (claws)
skills:
  Fly: 7
  Intimidate: 11
  Knowledge (engineering): 9
  Knowledge (planes): 9
  Perception: 10
  Stealth: 5
languages:
- Abyssal
- Draconic
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary or squad (2-18)
  treasure_type: standard
special_abilities:
  Aura of Destruction (Su): A genthodaemon can create an aura of pure carnage. All
    critical threats made against targets within the aura (including the genthodaemon)
    are automatically confirmed. Dying creatures within the aura take a -10 penalty
    on stabilization checks. The genthodaemon can activate or suppress this aura as
    a free action.
  Barbed Defense (Su): A creature that strikes a genthodaemon with a melee weapon,
    an unarmed strike, or a natural weapon takes 1d4+4 points of piercing damage from
    the barbed wire and other pieces of jagged metal embedded in the genthodaemon's
    body. Melee weapons with reach do not endanger their users in this way.
  Penetrating Slivers (Ex): When a genthodaemon confirms a critical hit with a claw
    attack, pieces of its metal nails break off and enter the target's body, working
    their way toward its heart. When the slivers reach the heart 1d3 rounds later,
    the creature takes 1d6 points of Constitution damage. The slivers are destroyed
    by anything that removes curses, diseases, or death effects. Likewise, creatures
    immune to curses, diseases, and death effects are immune to this ability.
  Shrapnel (Ex): A genthodaemon can shake loose four large pieces of the shrapnel
    embedded in its body as a standard action (make a separate attack roll for each
    piece). This attack has a range of 180 feet with no range increment. All targets
    of this attack must be within 30 feet of each other. The daemon can launch at
    most 24 pieces of shrapnel in any 24-hour period.
desc_long: |-
  Genthodaemons are common troops of daemonic armies, resolutely obedient to any greater type of daemon that gives them orders. They personify death in hopeless or futile wars, genocide, and the despair created by long, bloody stalemates where the combatants lose their will to live and forget why they were fighting in the first place. They have almost no role in corrupting mortals, as they are devoid of interest in the fates of most other creatures, but are sometimes called by daemonologists or greater daemons for use in war or their ability to shape battlefields. Any daemon that can summon a ceustodaemon can instead use its summon ability to summon a genthodaemon. 

  A genthodaemon looks like a stereotypical fiend- basically humanoid, but with claws, a tail, batlike wings, and cloven hooves. Metal armored plates, barbs, and spikes cover its body, though these are part of the daemon rather than armor it wears. Its claws are jagged metal shards sprouting from its fingers where nails should be. 

  Genthodaemons are only slightly above cacodaemons and lacridaemons in the hierarchy of Abaddon. A greater daemon may create a genthodaemon from a cacodaemon or one of the hunted (a dead soul trying to survive on Abaddon); however, most arise naturally from war-battered souls who band together as hunted, transforming into true daemons simultaneously when the group has cannibalized enough souls. Genthodaemons show unusual loyalty to others in their band, though this doesn't interfere with their obligations to more powerful daemons. 

  A typical genthodaemon stands over 9 feet tall and weighs 500 to 600 pounds (with much of this weight stemming from the daemon's embedded metal).

---

# Daemon, Genthodaemon
Jagged bits of metal, armor, and sharp pieces of _[[items/Mundane/Wire|wire]]_ embed the
flesh of this towering fiend.

**Source** Pathfinder #71: Rasputin Must Die! pg. 86
**XP** 1,600

NE Large outsider (daemon, evil, extraplanar)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10
**Aura** _[[spells/Destruction|destruction]]_ (30 ft.)

##### Defense

**AC** 18, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+9 natural, –1 size)
**hp** 51 (6d10+18)
**Fort** +8, **Ref** +5, **Will** +3
**Defensive Abilities** barbed defense; **DR** 5/good or silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10,
electricity 10, fire 10

##### Offense
**Speed** 30 ft., fly 30 ft. (average)
**Melee** bite +10 (1d8+4), 2 claws +10 (1d6+4 plus _[[universal monster rules/Bleed|bleed]]_ 1d4),
tail slap +4 (1d8+2 plus _bleed_ 1d4)
**Ranged** 4 shrapnel +5 (1d6+4/19–20)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** penetrating slivers, _[[universal monster rules/Trample|trample]]_ (1d6+6 plus _bleed_
 1d4, DC 17)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +8)
Constant—_[[spells/Detect Good|detect good]]_
At will—_[[spells/Cause Fear|cause fear]]_ (DC 13), lesser _[[spells/Confusion|confusion]]_ (DC 13),
_[[spells/Message|message]]_, _[[spells/Obscuring Mist|obscuring mist]]_
1/day—_[[spells/Crushing Despair|crushing despair]]_ (DC 16), _[[spells/Dispel Magic|dispel magic]]_, meld into
stone, _[[spells/Move Earth|move earth]]_

##### Statistics
**Str** 18, **Dex** 11, **Con** 16, **Int** 11, **Wis** 12, **Cha** 15
**Base Atk** +6; **CMB** +11; **CMD** 21
**Feats** _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (claws)
**Skills** Fly +7, Intimidate +11, Knowledge (engineering) +9,
Knowledge (planes) +9, Perception +10, Stealth +5
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary or squad (2–18)
**Treasure** standard

### Special Abilities

**Aura of _Destruction_ (Su) **A genthodaemon can create an
aura of pure carnage. All critical threats made against
targets within the aura (including the genthodaemon)
are automatically confirmed. _[[conditions/Dying|Dying]]_ creatures within
the aura take a –10 penalty on stabilization checks. The
genthodaemon can activate or suppress this aura as a
free action.

**Barbed Defense (Su)** A creature that strikes a genthodaemon
with a melee weapon, an unarmed strike, or a natural
weapon takes 1d4+4 points of piercing damage from the
barbed _wire_ and other pieces of jagged metal embedded in
the genthodaemon’s body. Melee weapons with reach do
not endanger their users in this way.

**Penetrating Slivers (Ex)** When a genthodaemon confirms a
critical hit with a claw attack, pieces of its metal nails break
off and enter the target’s body, working their way toward its
heart. When the slivers reach the heart 1d3 rounds later, the
creature takes 1d6 points of Constitution damage. The slivers
are destroyed by anything that removes curses, diseases,
or death effects. Likewise, creatures immune to curses,
diseases, and death effects are immune to this ability.
**Shrapnel (Ex)** A genthodaemon can shake loose four large pieces
of the shrapnel embedded in its body as a standard action
(make a separate attack roll for each piece). This attack has a
range of 180 feet with no range increment. All targets of this
attack must be within 30 feet of each other. The daemon can
launch at most 24 pieces of shrapnel in any 24-hour period.

##### Description

Genthodaemons are common troops of daemonic armies,
resolutely obedient to any greater type of daemon that
gives them orders. They personify death in hopeless or
futile wars, genocide, and the despair created by long,
bloody stalemates where the combatants lose their will
to live and forget why they were fighting in the first
place. They have almost no role in corrupting mortals,
as they are devoid of interest in the fates of most other
creatures, but are sometimes _[[items/Weapon Magic Abilities/Called|called]]_ by daemonologists
or greater daemons for use in war or their ability to
shape battlefields. Any daemon that can _[[universal monster rules/Summon|summon]]_ a
ceustodaemon can instead use its _summon_ ability to
_summon_ a genthodaemon.

A genthodaemon looks like a stereotypical fiend—
basically humanoid, but with claws, a tail, batlike wings,
and cloven hooves. Metal armored plates, barbs, and spikes
cover its body, though these are part of the daemon rather
than armor it wears. Its claws are jagged metal shards
sprouting from its fingers where nails should be.

Genthodaemons are only slightly above cacodaemons
and lacridaemons in the hierarchy of Abaddon. A greater
daemon may create a genthodaemon from a cacodaemon
or one of the hunted (a dead soul trying to survive on
Abaddon); however, most arise naturally from war-battered
souls who band together as hunted, transforming into true
daemons simultaneously when the group has cannibalized
enough souls. Genthodaemons show unusual loyalty to
others in their band, though this doesn’t interfere with
their obligations to more powerful daemons.

A typical genthodaemon stands over 9 feet tall and
weighs 500 to 600 pounds (with much of this weight
stemming from the daemon’s embedded metal).