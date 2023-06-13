---
cssclass: [monsters]
title1: Shell Sentinel
desc_short: This mass of shells is assembled into a shape that resembles a cross between
  a frog and a squid. Its “head” is a tangle of long limbs composed of razor-sharp
  edges, and its body seeps with foamy, toxic-looking slime.
title2: Shell Sentinel
CR: 5
sources:
- name: 'Pathfinder #98: Turn of the Torrent'
  page: 88
  link: http://paizo.com/products/btpy9gcx?Pathfinder-Adventure-Path-98-Turn-of-the-Torrent
XP: 1600
alignment: LE
size: Medium
type: construct
initiative:
  bonus: 8
  other:
    when ending discorporation: 12
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 18
  touch: 14
  flat_footed: 14
  components:
    dex: 4
    natural: 4
HP:
  HP: 58
  long: 7d10+20
  fast_healing: 5
saves:
  fort: 2
  ref: 8
  will: 4
defensive_abilities:
- freedom of movement
- sharpened edges
DR:
- amount: 5
  weakness: bludgeoning
immunities:
- fire
- construct traits
resistances:
  electricity: 10
weaknesses:
- fragile frame
speeds:
  base: 5
  swim: 30
attacks:
  melee:
  - - text: 4 talons +10 (1d6+2/18-20 plus 1 bleed and poison)
      entries:
      - - damage: 1d6+2
          crit_range: 18-20
        - damage: '1'
          type: bleed
        - effect: poison
      count: 4
      attack: talons
      bonus:
      - 10
  special:
  - poison cloud
  - pounce
spell_like_abilities:
  entries:
  - name: freedom of movement
    source: default
    freq: Constant
  - name: locate creature
    source: default
    freq: At will
    other: see below
  sources:
  - name: default
    CL: 5
    concentration: 3
ability_scores:
  STR: 14
  DEX: 19
  CON:
  INT: 3
  WIS: 15
  CHA: 6
BAB: 7
CMB: 9
CMD: 23
feats:
- name: Improved Initiative
- name: Lightning Reflexes
- name: Skill Focus (Perception)
- name: Weapon Focus (talons)
skills:
  Disguise: 0
    as shells while discorporated: 16
  Perception: 8
  Swim: 12
  _racial_mods:
    Disguise:
      as shells while discorporated: 16
languages:
- Aklo
- Aboleth
special_qualities:
- discorporate
- sense the masters
ecology:
  environment: any (usually aquatic)
  organization: solitary, pair, or gang (3-7)
  treasure_type: none
special_abilities:
  Discorporate (Su): As an immediate action, a shell sentinel can relax the supernatural
    energies that bind together its form, causing it to seem to fall apart into a
    loose tangle of shells. While discorporated, a shell sentinel gains a +16 racial
    bonus on Disguise checks to appear as a mound of shells. Any attempt to disperse
    or scatter the shells immediately ends the disguise, as the shells of a stillfunctional
    shell sentinel cannot be easily parted from the construct's body. A shell sentinel
    can return to its normal shape as a swift action-if it does so in the same round
    it rolls initiative, it gains a +4 racial bonus on its initiative check.
  Fragile Frame (Ex): Whenever a shell sentinel is dealt a critical hit from a bludgeoning
    weapon or rolls a natural 1 on a Reflex saving throw, it must succeed at a DC
    12 Fortitude save to resist being forced to discorporate. For 1 round after being
    forced to discorporate in this way, a shell sentinel gains vulnerability to bludgeoning
    damage.
  Poison (Ex): Poison cloud or talon-contact; save Fort DC 13; frequency 1/round for
    6 rounds; effect staggered plus 1d4 Wisdom; cure 1 save. The save DC is Constitution-based.
  Poison Cloud (Su): As a standard action, or as a free action after it hits a target
    with at least one attack after using pounce, a shell sentinel can exude a dense,
    dark cloud of poisonous ink as long as it is underwater. This ink cloud forms
    a 10-foot-diameter spread centered on the shell sentinel that provides total concealment.
    Creatures other than shell sentinels within the ink cloud are considered to be
    in darkness, and are exposed to the shell sentinel's poison as well. The ink cloud
    persists for 2 rounds before dispersing. A shell sentinel can create a poison
    cloud like this no more than once per minute.
  Sense the Masters (Su): Every shell sentinel has the ability to sense the presence
    and direction of its creator, others of its creator's race, and any creatures
    that are under its creator's magical control (although not those controlled by
    others of the creator's race). Most shell sentinels were created by aboleths,
    but the secret of their construction has been stolen and used by other aquatic
    races. A shell sentinel never attacks its creator, others of its creator's race,
    or creatures magically controlled by its creator, unless it is attacked first
    or its creator gives it direct orders that countermand this. A shell sentinel's
    locate creature spell-like ability functions only to divine the location of these
    creatures, and is not blocked by running water.
  Sharpened Edges (Su): A shell sentinel's component shells are supernaturally sharp.
    In addition to being the source of its talons' enhanced threat range and bleed
    effect, these edges give the creature a dangerous defense. Each time a creature
    damages a shell sentinel with a natural weapon or attempts to grapple it, the
    creature takes 1d4 points of slashing damage; if the creature takes the maximum
    amount of damage from the sharpened edges, it also takes 1 point of bleed damage.
desc_long: Shell sentinels are constructs designed specifically for use by the veiled
  masters or by those talented slaves with whom the veiled masters deign to share
  their secrets. These constructs often serve aboleths, skum, faceless stalkers, and
  cults of dominated humanoids as guardians, particularly of captured prisoners or
  other living victims. Unlike constructs whose traditions are mired in humanoid magical
  tradition, the typical shell sentinel appears more like a streamlined froglike creature
  with flippers instead of feet and a set of four talons on stalks in place of a head.
  A shell sentinel is composed entirely of razor-sharp shells, and the binding matrix
  that holds its form together and gives it its rudimentary but foultempered intelligence
  is a slithery black sludge distilled from the rotted flesh of unwanted slaves. The
  methods of extracting and preparing this slime requires living victims, and the
  decidedly painful and vile rendering process not only poisons the resulting construct's
  personality with an appetite for misery and cruelty, but also imbues poison into
  its form. Contact with this toxin, which runs throughout a shell sentinel's form,
  causes intense pain and clouds the minds of living creatures unfortunate enough
  to be subjected to it.

---

# Shell Sentinel
This mass of shells is assembled into a shape that resembles a cross between a frog and a _[[monsters/Squid|squid]]_. Its “head” is a tangle of long limbs composed of razor-sharp edges, and its body seeps with foamy, toxic-looking slime.
**Source** Pathfinder #98: Turn of the Torrent pg. 88
**XP** 1,600

LE Medium construct
**Init** +8 (+12 when ending discorporation); **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +8

##### Defense

**AC** 18, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 Dex, +4 natural)
**hp** 58 (7d10+20); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +2, **Ref** +8, **Will** +4
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_, sharpened edges; **DR** 5/bludgeoning; **Immune** fire, _[[universal monster rules/Construct Traits|construct traits]]_; **Resist** electricity 10
**Weaknesses** fragile frame

##### Offense
**Speed** 5 ft., swim 30 ft.
**Melee** 4 talons +10 (1d6+2/18–20 plus 1 _[[universal monster rules/Bleed|bleed]]_ and poison)
**Special Attacks** poison cloud, _[[universal monster rules/Pounce|pounce]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +3)
Constant—_freedom of movement_
At will—_[[spells/Locate Creature|locate creature]]_ (see below)

##### Statistics
**Str** 14, **Dex** 19, **Con** —, **Int** 3, **Wis** 15, **Cha** 6
**Base Atk** +7; **CMB** +9; **CMD** 23
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (talons)
**Skills** Disguise +0 (+16 as shells while discorporated), Perception +8, Swim +12; **Racial Modifiers** +16 Disguise as shells while discorporated
**Languages** Aklo, Aboleth
**SQ** discorporate, sense the masters

##### Ecology

**Environment** any (usually aquatic)
**Organization** solitary, pair, or gang (3–7)
**Treasure** none

### Special Abilities

**Discorporate (Su)** As an immediate action, a _[[monsters/Shell Sentinel|shell sentinel]]_ can relax the supernatural energies that bind together its form, causing it to seem to fall apart into a loose tangle of shells. While discorporated, a _shell sentinel_ gains a +16 racial bonus on Disguise checks to appear as a mound of shells. Any attempt to disperse or scatter the shells immediately ends the disguise, as the shells of a stillfunctional _shell sentinel_ cannot be easily parted from the construct’s body. A _shell sentinel_ can return to its normal shape as a swift action—if it does so in the same round it rolls initiative, it gains a +4 racial bonus on its initiative check.

**Fragile Frame (Ex)** Whenever a _shell sentinel_ is dealt a critical hit from a bludgeoning weapon or rolls a natural 1 on a Reflex saving throw, it must succeed at a DC 12 Fortitude save to resist being forced to discorporate. For 1 round after being forced to discorporate in this way, a _shell sentinel_ gains _[[curses/Vulnerability|vulnerability]]_ to bludgeoning damage.

**Poison (Ex)** Poison cloud or talon—contact; save Fort DC 13; frequency 1/round for 6 rounds; effect _[[conditions/Staggered|staggered]]_ plus 1d4 Wisdom; cure 1 save. The save DC is Constitution-based.

**Poison Cloud (Su)** As a standard action, or as a free action after it hits a target with at least one attack after using _pounce_, a _shell sentinel_ can exude a dense, dark cloud of poisonous _[[items/Mundane/Ink|ink]]_ as long as it is _[[items/Weapon Magic Abilities/Underwater|underwater]]_. This _ink_ cloud forms a 10-foot-diameter spread centered on the _shell sentinel_ that provides total concealment. Creatures other than shell sentinels within the _ink_ cloud are considered to be in _[[spells/Darkness|darkness]]_, and are exposed to the _shell sentinel_’s poison as well. The _ink_ cloud persists for 2 rounds before dispersing. A _shell sentinel_ can create a poison cloud like this no more than once per minute.
**Sense the Masters (Su)** Every _shell sentinel_ has the ability to sense the presence and direction of its creator, others of its creator’s race, and any creatures that are under its creator’s magical control (although not those controlled by others of the creator’s race). Most shell sentinels were created by aboleths, but the secret of their construction has been stolen and used by other aquatic races. A _shell sentinel_ never attacks its creator, others of its creator’s race, or creatures magically controlled by its creator, unless it is attacked first or its creator gives it direct orders that countermand this. A _shell sentinel_’s _locate creature_ spell-like ability functions only to divine the location of these creatures, and is not blocked by running water.
**Sharpened Edges (Su)** A _shell sentinel_’s component shells are supernaturally sharp. In addition to being the source of its talons’ enhanced threat range and _bleed_ effect, these edges give the creature a dangerous defense. Each time a creature damages a _shell sentinel_ with a natural weapon or attempts to grapple it, the creature takes 1d4 points of slashing damage; if the creature takes the maximum amount of damage from the sharpened edges, it also takes 1 point of _bleed_ damage.

##### Description

Shell sentinels are constructs designed specifically for use by the veiled masters or by those talented slaves with whom the veiled masters deign to share their secrets. These constructs often serve aboleths, _[[monsters/Skum|skum]]_, faceless stalkers, and cults of dominated humanoids as guardians, particularly of captured prisoners or other living victims. Unlike constructs whose traditions are mired in humanoid magical tradition, the typical _shell sentinel_ appears more like a streamlined froglike creature with flippers instead of feet and a set of four talons on stalks in place of a head. A _shell sentinel_ is composed entirely of razor-sharp shells, and the _[[spells/Binding|binding]]_ matrix that holds its form together and gives it its rudimentary but foultempered intelligence is a slithery black sludge distilled from the rotted flesh of unwanted slaves. The methods of extracting and preparing this slime requires living victims, and the decidedly painful and vile rendering process not only poisons the resulting construct’s personality with an appetite for misery and _[[feats/Cruelty|cruelty]]_, but also imbues poison into its form. Contact with this toxin, which runs throughout a _shell sentinel_’s form, causes _[[feats/Intense Pain|intense pain]]_ and clouds the minds of living creatures unfortunate enough to be subjected to it.