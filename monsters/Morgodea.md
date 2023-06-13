---
cssclass: [monsters]
title1: Morgodea
desc_short: Amid this hissing cloud of glistening cockroaches is a disheveled vagrant
  with wasplike stingers extending from its palms.
title2: Morgodea
CR: 4
sources:
- name: 'Pathfinder #99: Dance of the Damned'
  page: 86
  link: http://paizo.com/products/btpy9grk?Pathfinder-Adventure-Path-99-Dance-of-the-Damned
XP: 1200
alignment: CE
size: Medium
type: fey
initiative:
  bonus: 5
senses:
  darkvision: 60
  low-light vision: true
auras:
- name: cockroach cloud
  radius: 5
AC:
  AC: 19
  touch: 15
  flat_footed: 14
  components:
    dex: 5
    natural: 4
HP:
  HP: 33
  long: 6d6+12
saves:
  fort: 4
  ref: 10
  will: 6
immunities:
- mind-affecting effects
weaknesses:
- light sensitivity
speeds:
  base: 30
attacks:
  melee:
  - - text: claw +8 (1d6 plus grab)
      entries:
      - - damage: 1d6
        - effect: grab
      attack: claw
      bonus:
      - 8
    - text: 2 stings +7 (1d4 plus morgod jelly)
      entries:
      - - damage: 1d4
        - effect: morgod jelly
      count: 2
      attack: stings
      bonus:
      - 7
  special:
  - morgod jelly
  - sickening impulse (60ft, DC 15)
ability_scores:
  STR: 10
  DEX: 21
  CON: 15
  INT: 8
  WIS: 12
  CHA: 15
BAB: 3
CMB: 3
CMB_other: +7 to grapple
CMD: 18
feats:
- name: Multiattack
- name: Weapon Finesse
- name: Weapon Focus (stings)
skills:
  Bluff: 11
  Disguise: 15
  Knowledge (local): 8
  Perception: 8
  Sense Motive: 8
  Stealth: 12
  _racial_mods:
    Disguise:
      _: 4
languages:
- Aklo
- Common
special_qualities:
- cockroach empathy +8
ecology:
  environment: any urban
  organization: solitary, pair, or infestation (3-6)
  treasure_type: double
special_abilities:
  Cockroach Cloud (Su): As a swift action, a morgodea can open its layered hide and
    expel a brood of cockroaches into all adjacent squares. This cloud moves with
    the morgodea. Creatures other than morgodeas and cockroaches within the cloud
    at the beginning of their turns take 1d6 points of damage. Any creature damaged
    by the cockroach cloud must succeed at a DC 15 Fortitude save or be exposed to
    a dose of morgod jelly. Area-effect attacks that deal 10 or more points of damage
    to the morgodea destroy its cockroach cloud for 3 rounds, after which a new brood
    matures and the morgodea can unleash its cloud again. When a morgodea dies, its
    brood disperses.
  Cockroach Empathy (Ex): This ability functions as a druid's wild empathy ability,
    save that it works only on cockroaches. A morgodea gains a racial bonus on this
    check equal to its Hit Dice (+6 for most morgodeas). Vermin are normally mindless,
    but this empathic communication imparts a modicum of implanted intelligence in
    them, allowing the morgodea to train cockroaches and giant cockroaches and use
    them as guardians (although it does not grant them skills or feats). Cockroaches
    and giant cockroaches never attack a morgodea unless magically compelled to do
    so.
  Morgod Jelly (Ex): Morgodeas produce a pale, clear jelly from their bodies that
    acts as a powerful and addictive hallucinogenic (see the sidebar on page 87).
    Creatures unwillingly exposed to morgod jelly can resist its effects with a successful
    DC 15 Fortitude save. The save DC for a morgodea's jelly is Charisma-based.
  Sickening Impulse (Su): A morgodea can stir the morgod jelly in an addict's system.
    As a standard action, it can place an impulse into the mind of a single creature
    suffering from morgod jelly addiction within 60 feet. This functions as per the
    command spell, but the morgodea and its target do not need to hear or understand
    one another. Alternatively, the morgodea can inspire visions of insects crawling
    under the target's skin, sickening the target for 1d6 rounds. A successful DC
    15 Will save negates either effect. This is a mind-affecting compulsion effect.
    The save DC is Charisma-based.
desc_long: |-
  Morgodeas are sinister syntheses of fey and vermin who lurk in the filthy underworlds of cities. Compelled to corrupt and debase, these disgusting creatures deal in a pleasure that can plunge their victims into the depths addiction and madness. Morgodeas appear as human or elven vagrants covered in dirty rags. These “rags” are actually layered flaps of hide the morgodea can open to reveal a brood of cockroaches crawling amid its waxy, yellow flesh. Large pores in its body constantly weep a pale, thick jelly that sustains its nest of vermin and inspires euphoric visions in humanoids.

  In combat, a morgodea's cockroach brood erupts into a flesh-eating cloud to defend their master. The fey itself can extend a hidden chitinous pincer from its abdomen, and needlelike stings from the palm of each hand. It uses its massive claw to restrain victims while it injects them with its addictive venom again and again. A victim caught in this way is overwhelmed by the morgodea's druglike poison, and the prey's consequent hallucinations render its attacker indistinguishable in the teeming mass of hissing, gel-smeared insects, even as the morgodea holds it in place. A morgodea stands 5 to 6 feet tall and weighs around 200 pounds.

---

# Morgodea
Amid this hissing cloud of glistening cockroaches is a disheveled vagrant with wasplike stingers extending from its palms.
**Source** Pathfinder #99: Dance of the _[[feats/Damned|Damned]]_ pg. 86
**XP** 1,200
CE Medium fey
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +8
**Aura** cockroach cloud (5 ft.)

##### Defense

**AC** 19, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+5 Dex, +4 natural)
**hp** 33 (6d6+12)
**Fort** +4, **Ref** +10, **Will** +6
**Immune** mind-affecting effects
**Weaknesses** _[[universal monster rules/Light Sensitivity|light sensitivity]]_

##### Offense
**Speed** 30 ft.
**Melee** claw +8 (1d6 plus _[[universal monster rules/Grab|grab]]_), 2 stings +7 (1d4 plus morgod jelly)
**Special Attacks** morgod jelly, sickening impulse (60ft, DC 15)

##### Statistics
**Str** 10, **Dex** 21, **Con** 15, **Int** 8, **Wis** 12, **Cha** 15
**Base Atk** +3; **CMB** +3 (+7 to grapple); **CMD** 18
**Feats** _[[feats/Multiattack|Multiattack]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (stings)
**Skills** Bluff +11, Disguise +15, Knowledge (local) +8, Perception +8, Sense Motive +8, Stealth +12; **Racial Modifiers** +4 Disguise
**Languages** Aklo, Common
**SQ** cockroach _[[feats/Empathy|empathy]]_ +8

##### Ecology

**Environment** any urban
**Organization** solitary, pair, or infestation (3–6)
**Treasure** double

### Special Abilities

**Cockroach Cloud (Su)** As a swift action, a _[[monsters/Morgodea|morgodea]]_ can open its layered hide and expel a brood of cockroaches into all adjacent squares. This cloud moves with the _morgodea_. Creatures other than morgodeas and cockroaches within the cloud at the beginning of their turns take 1d6 points of damage. Any creature damaged by the cockroach cloud must succeed at a DC 15 Fortitude save or be exposed to a dose of morgod jelly. Area-effect attacks that deal 10 or more points of damage to the _morgodea_ destroy its cockroach cloud for 3 rounds, after which a new brood matures and the _morgodea_ can unleash its cloud again. When a _morgodea_ dies, its brood disperses.

**Cockroach _Empathy_ (Ex)** This ability functions as a _[[classes/Druid|druid]]_’s wild _empathy_ ability, save that it works only on cockroaches. A _morgodea_ gains a racial bonus on this check equal to its Hit Dice (+6 for most morgodeas). Vermin are normally mindless, but this empathic communication imparts a modicum of implanted intelligence in them, allowing the _morgodea_ to train cockroaches and giant cockroaches and use them as guardians (although it does not grant them skills or feats). Cockroaches and giant cockroaches never attack a _morgodea_ unless magically compelled to do so.

**Morgod Jelly (Ex)** Morgodeas produce a pale, clear jelly from their bodies that acts as a powerful and addictive hallucinogenic (see the sidebar on page 87). Creatures unwillingly exposed to morgod jelly can resist its effects with a successful DC 15 Fortitude save. The save DC for a _morgodea_’s jelly is Charisma-based.
**Sickening Impulse (Su)** A _morgodea_ can stir the morgod jelly in an addict’s system. As a standard action, it can place an impulse into the mind of a single creature suffering from morgod jelly addiction within 60 feet. This functions as per the _[[spells/Command|command]]_ spell, but the _morgodea_ and its target do not need to hear or understand one another. Alternatively, the _morgodea_ can inspire visions of insects crawling under the target’s skin, sickening the target for 1d6 rounds. A successful DC 15 Will save negates either effect. This is a mind-affecting compulsion effect. The save DC is Charisma-based.

##### Description

Morgodeas are sinister syntheses of fey and vermin who lurk in the filthy underworlds of cities. Compelled to corrupt and debase, these disgusting creatures deal in a pleasure that can plunge their victims into the depths addiction and madness. Morgodeas appear as human or elven vagrants covered in dirty rags. These “rags” are actually layered flaps of hide the _morgodea_ can open to reveal a brood of cockroaches crawling amid its waxy, yellow flesh. Large pores in its body constantly weep a pale, thick jelly that sustains its nest of vermin and inspires euphoric visions in humanoids.

In combat, a _morgodea_’s cockroach brood erupts into a flesh-eating cloud to defend their master. The fey itself can extend a hidden chitinous pincer from its abdomen, and needlelike stings from the palm of each hand. It uses its massive claw to restrain victims while it injects them with its addictive venom again and again. A victim caught in this way is overwhelmed by the _morgodea_’s druglike poison, and the prey’s consequent hallucinations render its attacker indistinguishable in the teeming mass of hissing, gel-smeared insects, even as the _morgodea_ holds it in place. A _morgodea_ stands 5 to 6 feet tall and weighs around 200 pounds.