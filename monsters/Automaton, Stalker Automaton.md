---
cssclass: [monsters]
title1: Automaton, Stalker Automaton
desc_short: This construct resembles a large cat. Its body coloring and the glowing
  core in the center of its head constantly shift in color.
title2: Stalker Automaton
CR: 5
sources:
- name: Construct Handbook
  page: 30
  link: https://paizo.com/products/btq01vam
XP: 1600
alignment: LN
size: Medium
type: construct
subtypes:
- automaton
- extraplanar
initiative:
  bonus: 7
senses:
  darkvision: 120
  low-light vision: true
AC:
  AC: 18
  touch: 13
  flat_footed: 15
  components:
    dex: 3
    natural: 5
HP:
  HP: 53
  long: 6d10+20
  fast_healing: 5
saves:
  fort: 1
  ref: 4
  will: 3
DR:
- amount: 5
  weakness: magic
immunities:
- construct traits
- electricity
resistances:
  cold: 10
  sonic: 10
SR: 16
weaknesses:
- vulnerable mind
speeds:
  base: 50
  other_semicolon: sprint
  climb: 20
attacks:
  melee:
  - - text: bite +10 (1d6+4 plus grab)
      entries:
      - - damage: 1d6+4
        - effect: grab
      attack: bite
      bonus:
      - 10
    - text: 2 claws +10 (1d4+4)
      entries:
      - - damage: 1d4+4
      count: 2
      attack: claws
      bonus:
      - 10
  special:
  - pounce
  - rake (2 claws, 1d4+4)
spell_like_abilities:
  entries:
  - name: dimension door
    source: default
    freq: At will
  - name: blur
    source: default
    freq: 1/day
  - name: invisibility
    source: default
    freq: 1/day
  - name: plane shift
    source: default
    freq: 1/week
    other: self plus 50 lbs. of objects only
  sources:
  - name: default
    CL: 6
    concentration: 7
ability_scores:
  STR: 18
  DEX: 16
  CON:
  INT: 13
  WIS: 15
  CHA: 12
BAB: 6
CMB: 10
CMB_other: +14 grapple
CMD: 23
CMD_other: 27 vs. trip
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Run
skills:
  Acrobatics: 12
  Climb: 21
  Perception: 11
  Stealth: 17
    when not moving: 22
  Survival: 8
  _racial_mods:
    Stealth:
      _: 5
      when not moving: 10
languages:
- Common
- telepathy 50 ft.
special_qualities:
- adaptive camouflage
- automaton core
- astral blink
- intelligent construct
ecology:
  environment: any (Axis)
  organization: solitary, pair, or pack (3-6)
  treasure_type: none
special_abilities:
  Adaptive Camouflage (Su): A stalker automaton's magically treated metal frame constantly
    shifts to match its surroundings, granting the stalker a +10 racial bonus on Stealth
    checks. This bonus is reduced to +5 if the stalker is moving. The stalker can
    use the Stealth skill even while being observed. This ability is overcome by see
    invisibility and similar abilities. The camouflage is suppressed by invisibility
    purge and similar abilities, but the stalker can resume the ability as a free
    action.
  Astral Blink (Su): A stalker automaton can phase in and out of the Astral Plane
    while moving, allowing it to travel quickly between two points. Once per round
    as part of a move action, a stalker automaton can teleport up to 15 feet as per
    dimension door. A stalker can continue to move and act immediately after teleporting.
    If the stalker is charging, it can teleport up to 30 feet with this ability and
    continue its charge from its new destination, so long as it has a clear path toward
    its target.
  Sprint (Ex): Once per hour, a stalker automaton can move at 10 times its normal
    speed (500 feet) when it makes a charge.
desc_long: |-
  Stalker automatons house the minds of the greatest hunters of the Jistka Imperium, serving as the best scouts and assassins among the automatons. Unmatched at pursuing targets, they set out individually or in deadly groups to follow their quarry for days on end, using their construct forms to outlast even the hardiest of targets.

   The bodies of stalker automatons were designed to emulate the various large cats that stalked the Jistka Imperium, such as aurumvoraxes, kamadans, and mountain lions. These creatures served as a basis for the strength and design of the bodies, but members of the Artificer Conclave took it upon themselves to improve upon what they found lacking in nature. A stalker automaton is typically 5 feet long and weighs 300 pounds, but the oldest of their kind remember the construction of larger stalker frames, including those that resemble creatures such as bears and drakes.

   A stalker's automaton core uses a combination of illusion and transmutation magic to physically alter the makeup of its body to better blend into its surroundings, altering features like color and texture. Although the stalker's frame consists mostly of metal, its planar-powered camouflage is capable of extraordinary adaptive feats, such as including creating the appearance of moss or leaves when appropriate. This effect is mostly an illusion, however, and those capable of seeing past such images can see the automaton for what it is.

   A number of hunters jumped at the chance to become more animal-like in their new automaton bodies. The new bodies afforded these hunters enhanced instincts, which allowed them to connect with their quarries on a more primal level. While stalker automatons initially used their new bodies to hunt Jistka's enemies, they quickly took to using their new skills for their own purposes, setting off on their own to seek out the hunts they longed for. Soon, stalker automatons were seen throughout the Inner Sea region, chasing after quarries that even the bravest monster hunters dared not approach.

   The boldest stalkers took to hunting beyond the Material Plane and sought their next targets across the Great Beyond. These stalkers chase dangerous prey throughout the multiverse, hunting outsiders of all kinds, including elementals and genies as well as angels and demons. Most of these stalkers are content with just shadowing these more elusive targets, satisfied in the fact that they can trail them unnoticed for days or weeks. Only the most brazen or most foolish stalkers dare attack these creatures, especially on the creatures' home planes. Rare are the stalkers that attack outsiders and remain intact, but a notable exception is one of the first stalkers, known simply as Mulvara the Quarry-bound. Rumors abound of her hunts, but the most consistent thread in these tales is her ability to consume part of the quintessence of her quarries, granting her untold powers.

   In combat, stalker automatons are a subtle force unrivaled by even the most cunning rogues or deadly assassins. Stalkers are capable of stepping between planar boundaries and reaching the Astral Plane instantly. This ability allows them to appear between different parts of the battlefield in the blink of an eye, not through typical planar travel but instead utilizing a kind of planar overlap similar in nature to ethereal jaunt.

   While pursuing a target, a stalker automaton will first trail its quarry long enough to understand the creature's tactics so that it can strike strategically at a later time. Due to their innate sense of honor, many stalkers prefer to make themselves known before an encounter or at least strike when the target is aware and ready. Stalkers see striking a creature while that target is at its strongest as the only way to prove their combat superiority. The automatons do understand their own limitations, however, and against targets they deem truly fearsome or powerful, they attack with every advantage possible. If it fails to overcome a target, or the target proves itself a worthy opponent, a stalker retreats, content with the outcome and leaving its opponent in peace.

   Though stalker automatons typically live secluded lives, it is not uncommon for them to create tight-knit packs, especially after bonding during a successful combat or hunt. These packs take on group names that match their hunting style or the previous success such as Those of the Cliff and the Titan Slayers. The packs rarely have a true leader, instead rotating leadership among its members. The current leader locates the next hunt and the pack follows. Once the hunt is complete, another member finds the next hunt she deems worthy.

   Today, stalker automatons remain interspersed throughout the planes and the Inner Sea region, with most residing either in Axis or among the remnants of Jistkan ruins. Those within Axis tend to live more subdued lives, seeking out the inevitables and axiomites of the city to learn their ways, though most stalkers eventually grow disinterested in the outsiders' rigid manners and make their own way in Axis. They often go on to serve as guides for those seeking information about the planes and their denizens, or even as teachers, sharing their hunting prowess with other skilled trackers.

   The few stalker automatons that remain on Golarion seem intent on recovering as many remaining automaton cores as they can. The rarity of these artifacts makes for a hunt as worthy as any creature. These automatons tend to be more solitary in fear of other stalkers or master automatons seeking them out to claim their caches of cores. Stalker automatons also see themselves as the guardians of Jistkan ruins, attacking creatures that might stumble upon lost technology too powerful for the modern age or those few surviving creatures still housing remnants of the Night Plague.

   One pack that makes its presence well known is Those That Sought the Beast. The especially powerful stalker automatons in this pack appear to have garnered some spark of divine might in their travels. They now scour Golarion in hopes of slaying the Spawn of Rovagug and welcome other hunters to join their cause.

---

# Automaton, Stalker Automaton
This construct resembles a large cat. Its body coloring and the glowing core in the center of its head constantly shift in color.
**Source** Construct Handbook pg. 30
**XP** 1,600

LN Medium construct (automaton, extraplanar)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +11

##### Defense

**AC** 18, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+3 Dex, +5 natural)
**hp** 53 (6d10+20); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +1, **Ref** +4, **Will** +3
**DR** 5/magic; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_, electricity; **Resist** cold 10, sonic 10; **SR** 16
**Weaknesses** vulnerable mind

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.; sprint
**Melee** bite +10 (1d6+4 plus _[[universal monster rules/Grab|grab]]_), 2 claws +10 (1d4+4)
**Special Attacks** _[[universal monster rules/Pounce|pounce]]_, _[[universal monster rules/Rake|rake]]_ (2 claws, 1d4+4)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +7)
At will—_[[spells/Dimension Door|dimension door]]_
1/day—_[[spells/Blur|blur]]_, _[[spells/Invisibility|invisibility]]_
1/week—_[[spells/Plane Shift|plane shift]]_ (self plus 50 lbs. of objects only)

##### Statistics
**Str** 18, **Dex** 16, **Con** —, **Int** 13, **Wis** 15, **Cha** 12
**Base Atk** +6; **CMB** +10 (+14 grapple); **CMD** 23 (27 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, Run
**Skills** Acrobatics +12, _Climb_ +21, Perception +11, Stealth +17 (+22 when not moving), Survival +8; **Racial Modifiers** +5 Stealth (+10 when not moving)
**Languages** Common; _[[universal monster rules/Telepathy|telepathy]]_ 50 ft.
**SQ** adaptive camouflage, _[[items/Wondrous Item/Automaton Core|automaton core]]_, astral _[[spells/Blink|blink]]_, intelligent construct

##### Ecology

**Environment** any (Axis)
**Organization** solitary, pair, or pack (3-6)
**Treasure** none

### Special Abilities

**Adaptive Camouflage (Su)** A stalker automaton’s magically treated metal frame constantly shifts to match its surroundings, granting the stalker a +10 racial bonus on Stealth checks. This bonus is reduced to +5 if the stalker is moving. The stalker can use the Stealth skill even while being observed. This ability is overcome by _[[spells/See Invisibility|see invisibility]]_ and similar abilities. The camouflage is suppressed by _[[spells/Invisibility Purge|invisibility purge]]_ and similar abilities, but the stalker can resume the ability as a free action.

**Astral _Blink_ (Su)** A stalker automaton can phase in and out of the Astral Plane while moving, allowing it to travel quickly between two points. Once per round as part of a move action, a stalker automaton can teleport up to 15 feet as per _dimension door_. A stalker can continue to move and act immediately after teleporting. If the stalker is charging, it can teleport up to 30 feet with this ability and continue its charge from its new destination, so long as it has a clear path toward its target.
**Sprint (Ex)** Once per hour, a stalker automaton can move at 10 times its normal speed (500 feet) when it makes a charge.

##### Description

Stalker automatons house the minds of the greatest hunters of the Jistka Imperium, serving as the best scouts and assassins among the automatons. Unmatched at pursuing targets, they set out individually or in _[[items/Weapon Magic Abilities/Deadly|deadly]]_ groups to follow their quarry for days on end, using their construct forms to outlast even the hardiest of targets.

The bodies of stalker automatons were designed to emulate the various large cats that stalked the Jistka Imperium, such as aurumvoraxes, kamadans, and mountain lions. These creatures served as a basis for the strength and design of the bodies, but members of the Artificer Conclave took it upon themselves to improve upon what they found lacking in nature. A stalker automaton is typically 5 feet long and weighs 300 pounds, but the oldest of their kind remember the construction of larger stalker frames, including those that resemble creatures such as bears and drakes.

A stalker’s _automaton core_ uses a combination of illusion and transmutation magic to physically alter the makeup of its body to better _[[spells/Blend|blend]]_ into its surroundings, altering features like color and texture. Although the stalker’s frame consists mostly of metal, its planar-powered camouflage is capable of extraordinary adaptive feats, such as including creating the appearance of moss or leaves when appropriate. This effect is mostly an illusion, however, and those capable of seeing past such images can see the automaton for what it is.

A number of hunters jumped at the chance to become more animal-like in their new automaton bodies. The new bodies afforded these hunters enhanced instincts, which allowed them to connect with their quarries on a more primal level. While stalker automatons initially used their new bodies to hunt Jistka’s enemies, they quickly took to using their new skills for their own purposes, setting off on their own to seek out the hunts they longed for. Soon, stalker automatons were seen throughout the Inner Sea region, chasing after quarries that even the bravest monster hunters dared not approach.

The boldest stalkers took to hunting beyond the Material Plane and sought their next targets across the Great Beyond. These stalkers chase dangerous prey throughout the multiverse, hunting outsiders of all kinds, including elementals and genies as well as angels and demons. Most of these stalkers are content with just shadowing these more elusive targets, satisfied in the fact that they can trail them unnoticed for days or weeks. Only the most brazen or most foolish stalkers dare attack these creatures, especially on the creatures’ home planes. Rare are the stalkers that attack outsiders and remain intact, but a notable exception is one of the first stalkers, known simply as Mulvara the Quarry-bound. Rumors abound of her hunts, but the most consistent thread in these tales is her ability to consume part of the _[[spells/Quintessence|quintessence]]_ of her quarries, granting her untold powers.

In combat, stalker automatons are a subtle force unrivaled by even the most _[[items/Weapon Magic Abilities/Cunning|cunning]]_ rogues or _deadly_ assassins. Stalkers are capable of stepping between _[[items/Weapon Magic Abilities/Planar|planar]]_ boundaries and reaching the Astral Plane instantly. This ability allows them to appear between different parts of the battlefield in the _blink_ of an eye, not through typical _planar_ travel but instead utilizing a kind of _planar_ overlap similar in nature to _[[spells/Ethereal Jaunt|ethereal jaunt]]_.

While pursuing a target, a stalker automaton will first trail its quarry long enough to understand the creature’s tactics so that it can strike strategically at a later time. Due to their innate sense of honor, many stalkers prefer to make themselves known before an encounter or at least strike when the target is aware and ready. Stalkers see striking a creature while that target is at its strongest as the only way to prove their combat superiority. The automatons do understand their own limitations, however, and against targets they deem truly fearsome or powerful, they attack with every advantage possible. If it fails to overcome a target, or the target proves itself a worthy opponent, a stalker retreats, content with the outcome and leaving its opponent in peace.

Though stalker automatons typically live secluded lives, it is not uncommon for them to create tight-knit packs, especially after bonding during a successful combat or hunt. These packs take on group names that match their hunting style or the previous success such as Those of the Cliff and the Titan Slayers. The packs rarely have a true leader, instead rotating _[[feats/Leadership|leadership]]_ among its members. The current leader locates the next hunt and the pack follows. Once the hunt is complete, another member finds the next hunt she deems worthy.

Today, stalker automatons remain interspersed throughout the planes and the Inner Sea region, with most residing either in Axis or among the remnants of Jistkan ruins. Those within Axis tend to live more subdued lives, seeking out the inevitables and axiomites of the city to learn their ways, though most stalkers eventually grow disinterested in the outsiders’ rigid manners and make their own way in Axis. They often go on to serve as guides for those seeking information about the planes and their denizens, or even as teachers, sharing their hunting prowess with other skilled trackers.

The few stalker automatons that remain on Golarion seem intent on recovering as many remaining automaton cores as they can. The rarity of these artifacts makes for a hunt as worthy as any creature. These automatons tend to be more solitary in _[[universal monster rules/Fear|fear]]_ of other stalkers or master automatons seeking them out to claim their caches of cores. Stalker automatons also see themselves as the guardians of Jistkan ruins, attacking creatures that might stumble upon lost technology too powerful for the modern age or those few surviving creatures still housing remnants of the Night Plague.

One pack that makes its presence well known is Those That Sought the Beast. The especially powerful stalker automatons in this pack appear to have garnered some _[[spells/Spark|spark]]_ of divine might in their travels. They now scour Golarion in hopes of slaying the Spawn of Rovagug and welcome other hunters to join their cause.