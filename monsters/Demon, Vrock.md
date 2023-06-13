---
cssclass: [monsters]
title1: Demon, Vrock
desc_short: This vulture-headed demon has great filthy wings, and a beak and claws
  ready to rip and tear.
title2: Mythic Vrock
CR: 11
MR: 4
sources:
- name: Mythic Adventures
  page: 184
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 12800
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
- mythic
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 27
  touch: 12
  flat_footed: 24
  components:
    dex: 3
    natural: 15
    size: -1
HP:
  HP: 152
  long: 9d10+103
saves:
  fort: 13
  ref: 11
  will: 6
DR:
- amount: 10
  weakness: epic and good
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 22
speeds:
  base: 30
  fly: 50
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +14 (1d8+6 plus bleed)
      entries:
      - - damage: 1d8+6
        - effect: bleed
      attack: bite
      bonus:
      - 14
    - text: 2 claws +14 (2d6+6 plus bleed)
      entries:
      - - damage: 2d6+6
        - effect: bleed
      count: 2
      attack: claws
      bonus:
      - 14
    - text: 2 talons +14 (1d6+6 plus bleed)
      entries:
      - - damage: 1d6+6
        - effect: bleed
      count: 2
      attack: talons
      bonus:
      - 14
  special:
  - bleed (1d6)
  - entrapping vines
  - greater stunning screech
  - manic dance of ruin
  - mythic power (4/day, surge +1d8)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: telekinesis
    source: default
    freq: At will
    DC: 18
  - name: heroism
    source: default
    freq: 1/day
  - name: mirror image
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: vrock
      amount: 1
      chance: 35%
  sources:
  - name: default
    CL: 12
    concentration: 15
ability_scores:
  STR: 23
  DEX: 17
  CON: 25
  INT: 14
  WIS: 16
  CHA: 16
BAB: 9
CMB: 16
CMD: 29
feats:
- is_mythic: true
  name: Cleave
- is_mythic: true
  name: Combat Reflexes
- name: Improved Initiative
- name: Lightning Reflexes
- name: Power Attack
- is_bonus: true
  name: Stand Still
skills:
  Fly: 13
  Intimidate: 15
  Knowledge (planes): 14
  Perception: 23
  Sense Motive: 15
  Spellcraft: 14
  Stealth: 11
  Survival: 15
  _racial_mods:
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Common
- telepathy 100 ft.
ecology:
  environment: any (Abyss)
  organization: solitary, pair, or gang (3-10)
  treasure_type: standard
special_abilities:
  Entrapping Vines (Ex): A mythic vrock can expend one use of mythic power as a swift
    action to release a cloud of spores from its body, affecting all adjacent non-demons.
    The spores deal 2d8 points of damage on the first round as they grow into ugly
    vines; for the next 10 rounds, they deal 1d6 points of damage and entrap the affected
    creatures (DC 21, 10 rounds, hardness 5, hp 10). The vines can be destroyed by
    casting bless on the creatures or by sprinkling them with holy water. This is
    a disease effect. The save DC is Constitution-based.
  Greater Stunning Screech (Su): Once per hour, a mythic vrock can emit a shrill screech.
    All non-demons within a 30-footradius spread must succeed at a DC 21 Fortitude
    save or be stunned for 1 round. If the vrock expends one use of mythic power,
    any creature that fails its save is staggered for 1d6 rounds after the stun ends.
    The save DC is Constitution-based.
  Manic Dance of Ruin (Su): A mythic vrock can expend one use of mythic power to dance
    and chant as a full-round action, after which it releases a crackling wave of
    energy, dealing 5d6 points of electricity damage to all creatures within 100 feet
    (Reflex DC 17 for half). Each additional vrock that joins in the dance adds 1
    to the DC and an additional 5d6 points of damage, up to a maximum of 20d6. The
    dance immediately ends and must be started anew if any of the participating vrocks
    is slain, stunned, or otherwise prevented from dancing. The save DC is Charisma-based.
desc_long: A mythic vrock is a violent creature of unrestrained rage that takes out
  its anger on anything weaker than itself.

---

# Demon, Vrock
A cloud of spores and a trail of feathers surrounds this twisted cross between a man and a gigantic _[[monsters/Vulture|vulture]]_.
**Source** Pathfinder RPG Bestiary pg. 69
**XP** 6,400
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +23

##### Defense

**AC** 22, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+2 Dex, +11 natural, –1 size)
**hp** 112 (9d10+63)
**Fort** +13, **Ref** +10, **Will** +6
**DR** 10/good; **Immune** electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 20

##### Offense
**Speed** 30 ft., fly 50 ft. (average)
**Melee** 2 claws +13 (2d6+5), bite +13 (1d8+5), 2 talons +13 (1d6+5)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** dance of ruin, spores, stunning _[[spells/Screech|screech]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th)
At will—greater teleport (self plus 50 lbs. of objects only), _[[spells/Telekinesis|telekinesis]]_ (DC 18)
1/day—_[[spells/Heroism|heroism]]_, _[[spells/Mirror Image|mirror image]]_, _[[universal monster rules/Summon|summon]]_ (level 3, 1 vrock 35%)

##### Statistics
**Str** 21, **Dex** 15, **Con** 25, **Int** 14, **Wis** 16, **Cha** 16
**Base Atk** +9; **CMB** +15; **CMD** 27
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Fly +12, Intimidate +15, Knowledge (planes) +14, Perception +23, Sense Motive +15, Spellcraft +14, Stealth +10, Survival +15; **Racial Modifiers** +8 Perception
**Languages** Abyssal, Celestial, Common; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, or gang (3–10)
**Treasure** standard

### Special Abilities

**Dance of Ruin (Su)** A vrock can dance and _[[spells/Chant|chant]]_ as a full-round action—at the end of 3 rounds, a crackling wave of energy explodes from the vrock, dealing 5d6 points of electricity damage to all creatures within 100 feet. A DC 17 Reflex save halves this damage. For each additional vrock that joins in the dance, the damage increases by 5d6 and the DC to avoid the effect increases by +1, to a maximum of 20d6 when four or more vrocks are _[[items/Weapon Magic Abilities/Dancing|dancing]]_ (the DC continues to increase with additional vrocks, but the damage does not). The dance immediately ends and must be started anew if any of the participating vrocks is slain, _[[conditions/Stunned|stunned]]_, or otherwise prevented from _dancing_. The save DC is Charisma-based.
**Spores (Ex)** A vrock can release a cloud of spores from its body once every 3 rounds as a free action. Adjacent creatures take 1d8 points of damage from the spores, plus 1d4 points of damage per round for 10 rounds as the spores grow into thick green vines. Although ugly, the vines are harmless and wither away in 1d4 days if not shaved off before then. The spores can be destroyed by casting _[[spells/Bless|bless]]_ on the affected creatures or by sprinkling them with _[[items/Mundane/Holy water|holy water]]_. This attack can also be halted by effects that remove or provide _[[universal monster rules/Immunity|immunity]]_ to disease.
**Stunning _Screech_ (Su)** Once per hour, a vrock can emit a shrill _screech_. All creatures except demons within a 30-foot-radius spread must succeed on a DC 21 Fortitude save or be _stunned_ for 1 round. The save DC is Constitution-based.

##### Description

Profane champions of the Abyss, vrocks embody all the _[[spells/Rage|rage]]_, hatred, and violence of that despicable realm. As _[[curses/Ravenous|ravenous]]_ and grotesquely opportunistic as the scavengers they resemble, vrocks delight in bloodshed, relishing the sounds and sensations of ripping the still-pulsing entrails from a living husk.

A typical vrock stands 8 feet tall and weighs 400 pounds. Vrocks generally form from the evil souls of hateful and wrathful mortals, particularly those who were career criminals, mercenaries, or assassins.