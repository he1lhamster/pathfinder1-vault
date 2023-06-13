---
cssclass: [monsters]
title1: Egregore
desc_short: Within a swirl of light, a clump of brains wrapped in arcs of light pulses
  and throbs. The impression of an open eye floats before it.
title2: Egregore
CR: 10
sources:
- name: Bestiary 5
  page: 104
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 9600
alignment: N
size: Large
type: aberration
initiative:
  bonus: 7
senses:
  darkvision: 60
  lifesense: true
auras:
- name: mental static
  radius: 30
  DC: 22
AC:
  AC: 27
  touch: 13
  flat_footed: 23
  components:
    armor: 4
    dex: 3
    dodge: 1
    natural: 6
    shield: 4
    size: -1
HP:
  HP: 123
  long: 13d8+65
  fast_healing: 5
saves:
  fort: 10
  ref: 9
  will: 15
defensive_abilities:
- amorphous
DR:
- amount: 5
  weakness: '-'
SR: 21
speeds:
  base: 30
  fly: 40
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: 4 light tentacles +14 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 4
      attack: light tentacles
      bonus:
      - 14
  special:
  - hypnotic oscillation
  - light tentacles
space: 10
reach: 10
psychic_magic:
  entries:
  - name: heal
    PE: 6
  - name: mass bear's endurance
    PE: 6
  - name: mass bull's strength
    PE: 6
  sources:
  - name: default
    CL: 13
    concentration: 19
  PE: 24
spell_like_abilities:
  entries:
  - name: mage armor
    source: default
    freq: Constant
  - name: mental barrier I
    source: default
    freq: Constant
  - name: cure moderate wounds
    source: default
    freq: At will
  sources:
  - name: default
    CL: 13
    concentration: 19
ability_scores:
  STR: 22
  DEX: 17
  CON: 18
  INT: 19
  WIS: 20
  CHA: 23
BAB: 9
CMB: 16
CMD: 30
feats:
- name: Combat Reflexes
- name: Dodge
- name: Great Fortitude
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Toughness
skills:
  Bluff: 19
  Escape Artist: 19
  Fly: 25
  Intimidate: 22
  Knowledge (arcana): 20
  Perception: 21
  Sense Motive: 18
  Spellcraft: 20
languages:
- Abyssal
- Celestial
- Common
- Infernal
- telepathy 100 ft.
special_qualities:
- cult mind
- psychic conduit
ecology:
  environment: any
  organization: cult (1 plus 13-20 cultists)
  treasure_type: standard
special_abilities:
  Cult Mind (Su): |-
    An egregore is created by the combined will of a number of cult members equal to its Hit Dice (minimum 13), and can have a maximum number of members in its cult mind equal to its Hit Dice. Each member must be an intelligent, living creature. These cultists pour their collective psychic consciousness into the collaborative creation of the egregore, granting each member a number of advantages. Creating an egregore involves a ritual lasting 1 day and costing 1,000 gp per Hit Die of the egregore. New creatures can be added to the cult mind only if previous members die or depart (see below). Adding a new member to the cult mind requires a ritual lasting 1 day and costing 1,000 gp. All the other members who are still a part of the cult mind must be present during this ritual or it fails.

     As long as a member of the cult mind is within 1 mile of the egregore, the egregore can use any of its spell-like abilities on that member, regardless of the spell's range. If a member of the cult mind is targeted by a mind-affecting spell, the egregore can attempt a Will save as well, and the cult member uses the better of the two results. If the cult member still fails, another member of the cult mind can choose to be affected instead.

     In addition, the members of the cult mind share a limited form of telepathy: they are able to send and receive simple messages and emotions, much like the empathic link between a wizard and his familiar.

     If a member of the cult mind is slain or travels more than 1 mile from the egregore, its link to the cult mind is severed, and every other member must succeed at a DC 20 Will save or be sickened for 1 round. If the number of members in the cult mind drops below half of the number of Hit Dice possessed by the egregore, the egregore must succeed at a DC 20 Will save or suffer from confusion. The egregore can attempt a new save at the start of each round to regain its senses. As long as the remaining number of members is less than half the egregore's Hit Dice, the egregore must attempt a new save each time a member of its cult mind is slain or leaves the cult mind. If the last member of the cult is slain or leaves the cult mind, the egregore dissipates harmlessly in 1d4 rounds.
  Hypnotic Oscillation (Sp): As a standard action, an egregore can weave a hypnotic
    pattern using its bands of light in a 10-foot radius around itself. Members of
    its cult mind are immune and don't count towards the spell's Hit Die limit, but
    otherwise this ability functions as the spell.
  Light Tentacles (Su): An egregore produces bands of light powered by its concentrated
    mental energy. It can cause these bands to become solid and lash out as tentacles.
    These tentacles follow all the normal rules for tentacles, except that they function
    as though they had the brilliant energy weapon special ability.
  Psychic Conduit (Ex): Any member of a cult mind can channel any psychic spells it
    casts through the egregore, as long as the cultist is within 30 feet of the egregore.
    If a cultist casts spells in this way, treat the egregore as if it were the spellcaster
    for purposes of the spell's range, point of origin, and other functions that depend
    on the caster's location. The creature casting the spell still provokes any attacks
    of opportunity or other negative consequences of casting a spell. The egregore
    takes 1d6 points of slashing damage per level of spell cast through it in this
    way as the energy cuts its way out of the creature, though its damage reduction
    applies. (A 0-level spell channeled through the egregore deals no damage to it.)
desc_long: |-
  When an especially powerful psychic leads a community of like-minded individuals, that group can pool its collective will together to create an egregore. The egregore is a powerful defender and a focal point for the psychic talents of every member of the group, granting them access to additional magical powers and a communal link.

   Though egregores' appearances vary, they typically have a core that resembles a mass of brains, discernible by practitioners of phrenology (Pathfinder RPG Occult Adventures 196) as bearing characteristics of the brains of those who make up its cult mind. This core projects an image that ref lects the ideals for which the egregore was formed-an unblinking eye to represent vigilance, a heraldic shield for protection, or some other stylized emblem to ref lect the goals of the group. From this bizarre hovering mass emerges a number of pulsating arcs of light that move in a strange unison, forming an almost mesmerizing pattern with their cadence.

   The synchronized synaptic pulses that emit from the egregore's cranial core manifest as elegant arcs of light leaping from one brain-shape to another in a rhythmic dance. The egregore can divert an arc outward, transforming it into a semi-solid band of light it can use to strike its foes. These bands normally pass through objects, but by concentrating more fully, the egregore can transform an arc into an even more solid form capable of manipulating objects.

   Typically, the sort of cult that creates an egregore is formed of a small association of individuals under the guidance of a strong-willed psychic leader, who directs the weaker-minded followers in a ritual that combines their latent psychic energy into the creation of a powerful entity to support the goals of the organization.

   The egregore itself is a totally separate creature, akin to the eidolons of summoners, though it seems to be a genuine living being of the Material Plane and not a true outsider. Creating an egregore requires a cult of 13-one leader and a dozen followers. Larger cults are capable of creating more powerful egregores, with stories circulating of doomsday cults with hundreds of members working together to create an abomination, but subsequently losing control and facing annihilation from their own creation. The egregore exists only as long as the cult that created it, fading back into the psychic ether from which it spawned once the cult is no more.

   An egregore is 12 feet across, though the bands of light that extend out from it cause it to fluctuate between an effective size of 13 feet to 15 feet. It weighs only 300 pounds despite its vast size. The brains that make up the egregore's body aren't constructed like human brains, and are far less dense; they seem to take the form of brains only because of the conceptual link they represent. Likewise, the egregore's staring eye and bands of light are more metaphorical than physical.

---

# Egregore
Within a swirl of light, a clump of brains wrapped in arcs of light pulses and throbs. The impression of an open eye floats before it.
**Source** Bestiary 5 pg. 104
**XP** 9,600

N Large aberration
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Lifesense|lifesense]]_; Perception +21
**Aura** mental static (30 ft., DC 22)

##### Defense

**AC** 27, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 23 (+4 armor, +3 Dex, +1 dodge, +6 natural, +4 _[[spells/Shield|shield]]_, –1 size)
**hp** 123 (13d8+65), _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +10, **Ref** +9, **Will** +15
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_; **DR** 5/—; **SR** 21

##### Offense
**Speed** 30 ft., fly 40 ft. (perfect)
**Melee** 4 light tentacles +14 (1d8+6)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** hypnotic oscillation, light tentacles
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_** (CL 13th; concentration +19)
24 PE—_[[spells/Heal|heal]]_ (6 PE), mass bear’s _[[feats/Endurance|endurance]]_ (6 PE), mass bull’s strength (6 PE)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +19)
Constant—_[[spells/Mage Armor|mage armor]]_, _[[spells/Mental Barrier I|mental barrier I]]_
At will—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_

##### Statistics
**Str** 22, **Dex** 17, **Con** 18, **Int** 19, **Wis** 20, **Cha** 23
**Base Atk** +9; **CMB** +16; **CMD** 30
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Toughness|Toughness]]_
**Skills** Bluff +19, Escape Artist +19, Fly +25, Intimidate +22, Knowledge (arcana) +20, Perception +21, Sense Motive +18, Spellcraft +20
**Languages** Abyssal, Celestial, Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** cult mind, _[[classes/Psychic|psychic]]_ conduit

##### Ecology

**Environment** any
**Organization** cult (1 plus 13–20 cultists)
**Treasure** standard

### Special Abilities

**Cult Mind (Su)** An _[[monsters/Egregore|egregore]]_ is created by the combined will of a number of cult members equal to its Hit Dice (minimum 13), and can have a maximum number of members in its cult mind equal to its Hit Dice. Each member must be an intelligent, living creature. These cultists pour their collective _psychic_ consciousness into the collaborative creation of the _egregore_, granting each member a number of advantages. Creating an _egregore_ involves a ritual lasting 1 day and costing 1,000 gp per Hit Die of the _egregore_. New creatures can be added to the cult mind only if previous members die or depart (see below). Adding a new member to the cult mind requires a ritual lasting 1 day and costing 1,000 gp. All the other members who are still a part of the cult mind must be present during this ritual or it fails.

As long as a member of the cult mind is within 1 mile of the _egregore_, the _egregore_ can use any of its _spell-like abilities_ on that member, regardless of the spell’s range. If a member of the cult mind is targeted by a mind-affecting spell, the _egregore_ can attempt a Will save as well, and the cult member uses the better of the two results. If the cult member still fails, another member of the cult mind can choose to be affected instead.

In addition, the members of the cult mind share a limited form of _telepathy_: they are able to send and receive simple messages and emotions, much like the empathic link between a _[[classes/Wizard|wizard]]_ and his familiar.

If a member of the cult mind is slain or travels more than 1 mile from the _egregore_, its link to the cult mind is severed, and every other member must succeed at a DC 20 Will save or be _[[conditions/Sickened|sickened]]_ for 1 round. If the number of members in the cult mind drops below half of the number of Hit Dice possessed by the _egregore_, the _egregore_ must succeed at a DC 20 Will save or suffer from _[[spells/Confusion|confusion]]_. The _egregore_ can attempt a new save at the start of each round to regain its senses. As long as the remaining number of members is less than half the _egregore_’s Hit Dice, the _egregore_ must attempt a new save each time a member of its cult mind is slain or leaves the cult mind. If the last member of the cult is slain or leaves the cult mind, the _egregore_ dissipates harmlessly in 1d4 rounds.

**Hypnotic Oscillation (Sp)** As a standard action, an _egregore_ can weave a _[[spells/Hypnotic Pattern|hypnotic pattern]]_ using its bands of light in a 10-foot radius around itself. Members of its cult mind are immune and don’t count towards the spell’s Hit Die limit, but otherwise this ability functions as the spell.

**Light Tentacles (Su)** An _egregore_ produces bands of light powered by its concentrated mental energy. It can cause these bands to become solid and lash out as tentacles. These tentacles follow all the normal rules for tentacles, except that they function as though they had the _[[items/Weapon Magic Abilities/Brilliant Energy|brilliant energy]]_ weapon special ability.

**_Psychic_ Conduit (Ex)** Any member of a cult mind can channel any _psychic_ spells it casts through the _egregore_, as long as the _[[npcs/Cultist|cultist]]_ is within 30 feet of the _egregore_. If a _cultist_ casts spells in this way, treat the _egregore_ as if it were the spellcaster for purposes of the spell’s range, point of origin, and other functions that depend on the caster’s location. The creature casting the spell still provokes any attacks of opportunity or other negative consequences of casting a spell. The _egregore_ takes 1d6 points of slashing damage per level of spell cast through it in this way as the energy cuts its way out of the creature, though its _[[universal monster rules/Damage Reduction|damage reduction]]_ applies. (A 0-level spell channeled through the _egregore_ deals no damage to it.)

##### Description

When an especially powerful _psychic_ leads a community of like-minded individuals, that group can pool its collective will together to create an _egregore_. The _egregore_ is a powerful defender and a focal point for the _psychic_ talents of every member of the group, granting them access to additional magical powers and a communal link.

Though egregores’ appearances vary, they typically have a core that resembles a mass of brains, discernible by practitioners of phrenology (Pathfinder RPG Occult Adventures 196) as bearing characteristics of the brains of those who make up its cult mind. This core projects an image that ref lects the ideals for which the _egregore_ was formed—an unblinking eye to represent vigilance, a heraldic _shield_ for protection, or some other stylized emblem to ref lect the goals of the group. From this bizarre hovering mass emerges a number of pulsating arcs of light that move in a strange unison, forming an almost mesmerizing pattern with their cadence.

The synchronized synaptic pulses that emit from the _egregore_’s cranial core manifest as elegant arcs of light leaping from one brain-shape to another in a rhythmic dance. The _egregore_ can divert an arc outward, transforming it into a semi-solid band of light it can use to strike its foes. These bands normally pass through objects, but by concentrating more fully, the _egregore_ can transform an arc into an even more solid form capable of manipulating objects.

Typically, the sort of cult that creates an _egregore_ is formed of a small association of individuals under the _[[spells/Guidance|guidance]]_ of a strong-willed _psychic_ leader, who directs the weaker-minded followers in a ritual that combines their latent _psychic_ energy into the creation of a powerful entity to support the goals of the organization.

The _egregore_ itself is a totally separate creature, akin to the eidolons of summoners, though it seems to be a genuine living being of the Material Plane and not a true outsider. Creating an _egregore_ requires a cult of 13—one leader and a dozen followers. Larger cults are capable of creating more powerful egregores, with stories circulating of doomsday cults with hundreds of members working together to create an abomination, but subsequently losing control and facing annihilation from their own creation. The _egregore_ exists only as long as the cult that created it, fading back into the _psychic_ ether from which it spawned once the cult is no more.

An _egregore_ is 12 feet across, though the bands of light that extend out from it cause it to fluctuate between an effective size of 13 feet to 15 feet. It weighs only 300 pounds despite its vast size. The brains that make up the _egregore_’s body aren’t constructed like human brains, and are far less dense; they seem to take the form of brains only because of the conceptual link they represent. Likewise, the _egregore_’s staring eye and bands of light are more metaphorical than physical.