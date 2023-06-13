---
cssclass: [monsters]
title1: Ugothokra
desc_short: This partially mechanical, partially organic spider moves with a skittering
  lurch. A single crystalline eye glares from its hideous face.
title2: Ugothokra
CR: 7
sources:
- name: 'Pathfinder #88: Valley of the Brain Collectors'
  page: 88
  link: http://paizo.com/products/btpy99sg?Pathfinder-Adventure-Path-88-Valley-of-the-Brain-Collectors
XP: 3200
alignment: CE
size: Small
type: aberration
initiative:
  bonus: 9
senses:
  darkvision: 60
AC:
  AC: 20
  touch: 17
  flat_footed: 14
  components:
    dex: 5
    dodge: 1
    natural: 3
    size: 1
HP:
  HP: 85
  long: 10d8+40
saves:
  fort: 7
  ref: 8
  will: 10
defensive_abilities:
- infected blood
immunities:
- cold
- disease
- poison
resistances:
  acid: 5
  electricity: 5
speeds:
  base: 50
  climb: 50
attacks:
  melee:
  - - text: bite +9 (1d4+1 plus poison)
      entries:
      - - damage: 1d4+1
        - effect: poison
      attack: bite
      bonus:
      - 9
  ranged:
  - - text: 6 flechette spray +13 (1d4+1 plus viral infection)
      entries:
      - - damage: 1d4+1
        - effect: viral infection
      count: 6
      attack: flechette spray
      bonus:
      - 13
  special:
  - combined arms
ability_scores:
  STR: 13
  DEX: 20
  CON: 18
  INT: 10
  WIS: 17
  CHA: 13
BAB: 7
CMB: 7
CMD: 23
CMD_other: 35 vs. trip
feats:
- name: Dodge
- name: Improved Initiative
- name: Mobility
- name: Point-Blank Shot
- name: Shot on the Run
skills:
  Acrobatics: 18
    when jumping: 26
  Climb: 30
  Perception: 16
  Stealth: 22
  _racial_mods:
    Climb:
      _: 8
languages:
- Aklo (can't speak)
special_qualities:
- expert climber
- no breath
ecology:
  environment: any
  organization: solitary, pair, or pack (3-12)
  treasure_type: incidental
special_abilities:
  Combined Arms (Ex): When taking a full-attack action, an ugothokra can attack with
    its bite and its flechette spray attacks simultaneously. It does not provoke attacks
    of opportunity with its flechette spray attacks when using combined arms.
  Expert Climber (Ex): An ugothokra's feet allow it to climb any surface, no matter
    how slick or sheer. In effect, an ugothokra is treated as constantly being under
    the effects of spider climb, though this is effect is natural rather than magical.
  Flechette Spray (Ex): An ugothokra can fire bursts of calcified bone and horn from
    the vents along its abdomen. All six vents can fire as part of a full-attack action,
    or it can fire one vent as a standard action. This attack has a range increment
    of 50 feet. An ugothokra generates the “ammunition” it uses for this attack internally
    by feeding on organic material, and effectively has an unlimited supply of flechette
    material at any one time, but an ugothokra that is currently starving can't use
    this attack until at least 1 hour after feeding.
  Infected Blood (Ex): A creature that damages an ugothokra with a slashing or piercing
    melee weapon (regardless of how often the ugothokra is damaged) must succeed at
    a DC 20 Reflex saving throw at the end of its turn or be sprayed by the ugothokra's
    infected blood. A creature that damages an ugothokra with a slashing or piercing
    natural weapon automatically fails this saving throw. On a failed saving throw,
    the creature is exposed to a random viral infection (see below), but gains a +4
    bonus on the Fortitude save to resist contracting whatever disease it is exposed
    to. Unlike when a victim contracts an infection from an ugothokra's flechette
    spray, diseases caught via contact with the monster's blood have normal onset
    times as determined by the disease in question. The Reflex save is Dexterity-based.
  Poison (Ex): Bite-injury; save Fort DC 19; frequency 1/round for 6 rounds; effect
    1d4 Con plus sickened for 1 round; cure 2 consecutive saves.
  Viral Infection (Su): |-
    An ugothokra's body is infested with numerous potent and highly infectious diseases engineered by their Dominion creators to cause highly specific conditions in those they infect. An ugothokra's blood carries these diseases, and while the creature can transmit random infections by means of contact with its blood, the most efficient method of transmission is via its flechette spray. Most ugothokras carry the following three contagions in their systems, and they can decide which one to inflict on a target as part of the act of firing a flechette spray-it can even inflict different diseases with different sprays in the same round if it so chooses. Some ugothokras carry additional viral infections that are tailored by their Dominion creators for incredibly specialized tasks. A creature exposed to any of these viral infections can resist the infection with a successful DC 19 Fortitude save, but on a failed save, the effect occurs immediately and the onset time is ignored. Contracting an infection via the ugothokra's blood is not as efficient and uses the listed onset time. The most common viral infections available to an ugothokra are listed below.

    Aklo Submission: Disease-injury or contact; save Fort DC 19; onset 1 day; frequency 1/day; effect 1d2 Wisdom drain (can't drain Wisdom below 0) plus susceptibility to Aklo; cure 2 consecutive saves. As long as a creature is infected with this disease (even if the creature isn't currently suffering any Wisdom drain from the disease), it becomes unusually compliant and responsive to commands issued to it in Aklo. Any Bluff, Diplomacy, or Intimidate check attempted against the character while speaking in Aklo gains a +4 bonus. Furthermore, as a full-round action, any creature can issue a command to the victim in Aklo to attempt to affect the victim with a suggestion effect (effective CL 5th, regardless of the commander's level)-the victim can resist this suggestion with a successful DC 14 Will save. Once a victim of Aklo submission succeeds at a Will save to resist such a suggestion, it can't be further affected in this way by any Aklo-speaking creature for 24 hours.

    Flesh Ripen Fever: Disease-injury or contact; save Fort DC 19; onset 1d4 days; frequency 1/day; effect 1d3 Con damage plus stench; cure 2 consecutive saves. A character suffering from flesh ripen fever exudes a nauseating stench as his skin decays and sloughs off, leaving behind reeking pits of stinking flesh. The victim is automatically sickened by its own smell, as are all creatures within a 10-foot radius. A successful DC 14 Fortitude save allows a creature to ignore the sickening effect for 24 hours-the victim of flesh ripen fever doesn't get such a saving throw to avoid being sickened. This stench is a poison effect that doesn't affect creatures associated with the Dominion of the Black.

    Implant Rejection Syndrome: Disease-injury or contact; save Fort DC 19; onset 1d4 days; frequency 1/day; effect 1d2 Con drain plus 1d2 Int drain plus implant rejection; cure 2 consecutive saves. This insidious sickness is particularly devastating to creatures with cybernetic implants. Such creatures take a -2 penalty on all saving throws attempted to resist this disease. Further, each time a saving throw to resist its effect is attempted and failed, the creature takes 2d6 points of damage and loses the use of one randomly selected cybernetic implant for 24 hours.
desc_long: |-
  One of many artificially engineered species grown and molded in Dominion of the Black labs, ugothokras were designed specifically to spread contagions through organic enemy ranks. Immune to disease, ugothokras have small bodies that are capable of hosting a limitless number of contagions within their blood.

  Ugothokras are incapable of reproduction, and when additional ones are required by the Dominion of the Black, replacements are constructed from organic and cybernetic components. The construction facilities typically operate within the organic walls of Dominion installations, the little beasts crawling out from birthing tubes protruding from their semi-organic incubators. These incubators are of widely varying size and capacity. Smaller versions, possessing no more than two birthing tubes, can produce an ugothokra every hour if provided the proper nutrients (typically curdled flesh harvested from victims of flesh ripen fever), fed to it through the living walls in which the incubator is nestled. Significantly larger incubators with dozens of birthing tubes have been reported, their size limited only by the resources needed to create more offspring.

  A newborn ugothokra is completely autonomous and fully functional. While ugothokras can't fly, their immunity to cold and the fact that they don't breathe make them ideal bioweapons for use against enemy vessels in space-often, a Dominion ship's exterior swarms with ugothokras, and as they near an enemy ship, dozens of the tenacious aberrations drop off to cling to the enemy's hull. The creatures skitter along surfaces, searching for points of entry so they can infect the vessel's crew and spread their sickness. Often, these entry points are created for them via battle damage from other Dominion weaponry. Many Dominion ships have had great success at using ugothokras to spread Aklo submission among enemy crews, allowing the Dominion to order their victims to power down and submit. Those that manage to resist still typically fall under the grinding legs and mouth parts of swarms of ugothokras.

  Rumors of variant ugothokras abound, including swarms or larger varieties, and those possessing even more potent and deadly diseases. Given the prodigious industry of the Dominion of the Black, such rumors hardly seem far fetched.

  An ugothokra stands only about 2 1/2 feet tall, with a leg span approaching 6 feet. Most weigh around 150 pounds.

---

# Ugothokra
This partially mechanical, partially organic spider moves with a skittering lurch. A single crystalline eye glares from its hideous face.
**Source** Pathfinder #88: Valley of the Brain Collectors pg. 88
**XP** 3,200
CE Small aberration
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +16

##### Defense

**AC** 20, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+5 Dex, +1 dodge, +3 natural, +1 size)
**hp** 85 (10d8+40)
**Fort** +7, **Ref** +8, **Will** +10
**Defensive Abilities** infected blood; **Immune** cold, disease, poison; **Resist** acid 5, electricity 5

##### Offense
**Speed** 50 ft., _[[universal monster rules/Climb|climb]]_ 50 ft.
**Melee** bite +9 (1d4+1 plus poison)
**Ranged** 6 flechette spray +13 (1d4+1 plus viral infection)
**Special Attacks** combined arms

##### Statistics
**Str** 13, **Dex** 20, **Con** 18, **Int** 10, **Wis** 17, **Cha** 13
**Base Atk** +7; **CMB** +7; **CMD** 23 (35 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Shot on the Run|Shot on the Run]]_
**Skills** Acrobatics +18 (+26 when jumping), _Climb_ +30, Perception +16, Stealth +22; **Racial Modifiers** +8 _Climb_
**Languages** Aklo (can’t speak)
**SQ** expert climber, _[[universal monster rules/No Breath|no breath]]_

##### Ecology

**Environment** any
**Organization** solitary, pair, or pack (3–12)
**Treasure** incidental

### Special Abilities

**Combined Arms (Ex)** When taking a full-attack action, an _[[monsters/Ugothokra|ugothokra]]_ can attack with its bite and its flechette spray attacks simultaneously. It does not provoke attacks of opportunity with its flechette spray attacks when using combined arms.

**Expert Climber (Ex)** An _ugothokra_’s feet allow it to _climb_ any surface, no matter how _[[items/Armor Magic Abilities/Slick|slick]]_ or sheer. In effect, an _ugothokra_ is treated as constantly being under the effects of _[[spells/Spider Climb|spider climb]]_, though this is effect is natural rather than magical.

**Flechette Spray (Ex)** An _ugothokra_ can fire bursts of calcified bone and horn from the vents along its abdomen. All six vents can fire as part of a full-attack action, or it can fire one vent as a standard action. This attack has a range increment of 50 feet. An _ugothokra_ generates the “ammunition” it uses for this attack internally by feeding on organic material, and effectively has an unlimited supply of flechette material at any one time, but an _ugothokra_ that is currently starving can’t use this attack until at least 1 hour after feeding.

**Infected Blood (Ex)** A creature that damages an _ugothokra_ with a slashing or piercing melee weapon (regardless of how often the _ugothokra_ is damaged) must succeed at a DC 20 Reflex saving throw at the end of its turn or be sprayed by the _ugothokra_’s infected blood. A creature that damages an _ugothokra_ with a slashing or piercing natural weapon automatically fails this saving throw. On a failed saving throw, the creature is exposed to a random viral infection (see below), but gains a +4 bonus on the Fortitude save to resist contracting whatever disease it is exposed to. Unlike when a victim contracts an infection from an _ugothokra_’s flechette spray, diseases caught via contact with the monster’s blood have normal onset times as determined by the disease in question. The Reflex save is Dexterity-based.

**Poison (Ex)** Bite—injury; save Fort DC 19; frequency 1/round for 6 rounds; effect 1d4 Con plus _[[conditions/Sickened|sickened]]_ for 1 round; cure 2 consecutive saves.

**Viral Infection (Su)** An _ugothokra_’s body is infested with numerous _[[items/Weapon Magic Abilities/Potent|potent]]_ and highly infectious diseases engineered by their Dominion creators to cause highly specific conditions in those they infect. An _ugothokra_’s blood carries these diseases, and while the creature can transmit random infections by means of contact with its blood, the most efficient method of transmission is via its flechette spray. Most ugothokras carry the following three contagions in their systems, and they can decide which one to inflict on a target as part of the act of firing a flechette spray—it can even inflict different diseases with different sprays in the same round if it so chooses. Some ugothokras carry additional viral infections that are tailored by their Dominion creators for incredibly specialized tasks. A creature exposed to any of these viral infections can resist the infection with a successful DC 19 Fortitude save, but on a failed save, the effect occurs immediately and the onset time is ignored. Contracting an infection via the _ugothokra_’s blood is not as efficient and uses the listed onset time. The most common viral infections available to an _ugothokra_ are listed below.

Aklo Submission: Disease—injury or contact; save Fort DC 19; onset 1 day; frequency 1/day; effect 1d2 Wisdom drain (can’t drain Wisdom below 0) plus susceptibility to Aklo; cure 2 consecutive saves. As long as a creature is infected with this disease (even if the creature isn’t currently suffering any Wisdom drain from the disease), it becomes unusually compliant and responsive to commands issued to it in Aklo. Any Bluff, Diplomacy, or Intimidate check attempted against the character while speaking in Aklo gains a +4 bonus. Furthermore, as a full-round action, any creature can issue a _[[spells/Command|command]]_ to the victim in Aklo to attempt to affect the victim with a _[[spells/Suggestion|suggestion]]_ effect (effective CL 5th, regardless of the commander’s level)—the victim can resist this _suggestion_ with a successful DC 14 Will save. Once a victim of Aklo submission succeeds at a Will save to resist such a _suggestion_, it can’t be further affected in this way by any Aklo-speaking creature for 24 hours.

Flesh Ripen Fever: Disease—injury or contact; save Fort DC 19; onset 1d4 days; frequency 1/day; effect 1d3 Con damage plus _[[universal monster rules/Stench|stench]]_; cure 2 consecutive saves. A character suffering from flesh ripen fever exudes a nauseating _stench_ as his skin decays and sloughs off, leaving behind reeking pits of stinking flesh. The victim is automatically _sickened_ by its own smell, as are all creatures within a 10-foot radius. A successful DC 14 Fortitude save allows a creature to ignore the sickening effect for 24 hours—the victim of flesh ripen fever doesn’t get such a saving throw to avoid being _sickened_. This _stench_ is a poison effect that doesn’t affect creatures associated with the Dominion of the Black.

Implant Rejection Syndrome: Disease—injury or contact; save Fort DC 19; onset 1d4 days; frequency 1/day; effect 1d2 Con drain plus 1d2 Int drain plus implant rejection; cure 2 consecutive saves. This insidious sickness is particularly devastating to creatures with cybernetic implants. Such creatures take a –2 penalty on all saving throws attempted to resist this disease. Further, each time a saving throw to resist its effect is attempted and failed, the creature takes 2d6 points of damage and loses the use of one randomly selected cybernetic implant for 24 hours.

##### Description

One of many artificially engineered species grown and molded in Dominion of the Black labs, ugothokras were designed specifically to spread contagions through organic enemy ranks. Immune to disease, ugothokras have small bodies that are capable of hosting a limitless number of contagions within their blood.

Ugothokras are incapable of reproduction, and when additional ones are required by the Dominion of the Black, replacements are constructed from organic and cybernetic components. The construction facilities typically operate within the organic walls of Dominion installations, the little beasts crawling out from birthing tubes protruding from their semi-organic incubators. These incubators are of widely varying size and capacity. Smaller versions, possessing no more than two birthing tubes, can produce an _ugothokra_ every hour if provided the proper nutrients (typically curdled flesh harvested from victims of flesh ripen fever), fed to it through the living walls in which the incubator is nestled. Significantly larger incubators with dozens of birthing tubes have been reported, their size limited only by the resources needed to create more offspring.

A newborn _ugothokra_ is completely autonomous and fully functional. While ugothokras can’t fly, their _[[universal monster rules/Immunity|immunity]]_ to cold and the fact that they don’t breathe make them ideal bioweapons for use against enemy vessels in space—often, a Dominion ship’s exterior swarms with ugothokras, and as they near an enemy ship, dozens of the tenacious aberrations drop off to cling to the enemy’s hull. The creatures skitter along surfaces, searching for points of entry so they can infect the vessel’s crew and spread their sickness. Often, these entry points are created for them via battle damage from other Dominion weaponry. Many Dominion ships have had great success at using ugothokras to spread Aklo submission among enemy crews, allowing the Dominion to order their victims to power down and submit. Those that manage to resist still typically fall under the _[[items/Armor Magic Abilities/Grinding|grinding]]_ legs and mouth parts of swarms of ugothokras.

Rumors of variant ugothokras abound, including swarms or larger varieties, and those possessing even more _potent_ and _[[items/Weapon Magic Abilities/Deadly|deadly]]_ diseases. Given the prodigious industry of the Dominion of the Black, such rumors hardly seem far fetched.

An _ugothokra_ stands only about 2 1/2 feet tall, with a leg span approaching 6 feet. Most weigh around 150 pounds.