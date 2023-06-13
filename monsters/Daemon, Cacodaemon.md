---
cssclass: [monsters]
title1: Daemon, Cacodaemon
desc_short: 'An ever-gnashing maw, filled with row after row of mismatched teeth,
  dominates this frightful creature's orb-like body. '
title2: Cacodaemon
CR: 2
sources:
- name: Bestiary 2
  page: 64
  link: http://paizo.com/pathfinderRPG/v5748btpy8hif
XP: 600
alignment: NE
size: Tiny
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 4
senses:
  darkvision: 60
  detect good: true
  detect magic: true
AC:
  AC: 16
  touch: 12
  flat_footed: 16
  components:
    natural: 4
    size: 2
HP:
  HP: 19
  long: 3d10+3
  fast_healing: 2
saves:
  fort: 2
  ref: 5
  will: 4
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
  base: 5
  fly: 50
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: bite +6 (1d4+1 plus disease)
      entries:
      - - damage: 1d4+1
        - effect: disease
      attack: bite
      bonus:
      - 6
  special:
  - soul lock
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: lesser confusion
    source: default
    freq: 3/day
    DC: 12
  - name: commune
    source: default
    freq: 1/week
    CL: 12
    other: six questions
  sources:
  - name: default
    CL: 6
    concentration: 7
ability_scores:
  STR: 12
  DEX: 11
  CON: 13
  INT: 8
  WIS: 13
  CHA: 12
BAB: 3
CMB: 1
CMD: 12
feats:
- name: Improved Initiative
- name: Lightning Reflexes
skills:
  Bluff: 7
  Fly: 18
  Knowledge (planes): 5
  Perception: 7
  Stealth: 14
languages:
- Abyssal
- Common
- Infernal
- telepathy 100 ft.
special_qualities:
- 'change shape (2 of the following forms: lizard, octopus, Small scorpion, venomous
  snake, polymorph)'
ecology:
  environment: any (Abaddon)
  organization: solitary or swarm (2-10)
  treasure_type: standard
special_abilities:
  Disease (Su): 'Cacodaemonia: Bite-injury; save Fort DC 12; onset 1 day; frequency
    1/day; effect 1d2 Wis damage, cure 2 consecutive saves. In addition to the normal
    effects of the disease, as long as a victim is infected, the cacodaemon can telepathically
    communicate with the creature over any distance (as long as they remain on the
    same plane).'
  Soul Lock (Su): Once per day as a full-round action, a cacodaemon can ingest the
    spirit of any sentient creature that has died within the last minute. This causes
    a soul gem to grow inside of the cacodaemon's gut, which it can regurgitate as
    a standard action. A soul gem is a fine-sized object with 1 hit point and hardness
    2. Destroying a soul gem frees the soul within, though it does not return the
    deceased creature to life. This is a death effect. Any attempt to resurrect a
    body whose soul is trapped in a soul gem requires a DC 12 caster level check.
    Failure results in the spell having no effect, while success shatters the victim's
    soul gem and returns the creature to life as normal. If the soul gem rests in
    an unholy location, such as that created by the spell unhallow, the DC of this
    caster level check increases by +2. The caster level check DC is Charisma-based.
desc_long: |-
  Any evil outsider can, as a standard action, ingest a soul gem. Doing so frees the soul within, but condemns it to one of the lower planes (though the soul can be returned to life as normal). The outsider gains fast healing 2 for a number of rounds equal to its Hit Dice. 

  The least of daemonkind, cacodaemons spawn from eddies of angry, violent, and demented souls amid the mists of Abaddon. Dim-witted but utterly evil, they endlessly seek to cause pain and indulge their hunger for mortal souls. Many more powerful fiends keep cacodaemons as pets, if only to be able to harvest the tiny creatures' soul gems. A 7th-level spellcaster can gain a cacodaemon as a familiar if she has the Improved Familiar feat.

---

# Daemon, Cacodaemon
An ever-gnashing maw, filled with row after row of mismatched teeth, dominates this frightful creature’s orb-like body.

**Source** Bestiary 2 pg. 64
**XP** 600

NE Tiny outsider (daemon, evil, extraplanar)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_; Perception +7

##### Defense

**AC** 16, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+4 natural, +2 size)
**hp** 19 (3d10+3); _[[universal monster rules/Fast Healing|fast healing]]_ 2
**Fort** +2, **Ref** +5, **Will** +4
**DR** 5/good or silver; **Immune** acid, death effects, disease, poison; **Resist** cold 10, electricity 10, fire 10

##### Offense
**Speed** 5 ft., fly 50 ft. (perfect)
**Melee** bite +6 (1d4+1 plus disease)
**Space** 2-1/2 ft., **Reach** 0 ft.
**Special Attacks** soul lock
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 6th; concentration +7)
Constant—_detect good_, _detect magic_
At will—_[[spells/Invisibility|invisibility]]_ (self only)
3/day—lesser _[[spells/Confusion|confusion]]_ (DC 12)
1/week—_[[spells/Commune|commune]]_ (CL 12th, six questions)

##### Statistics
**Str** 12, **Dex** 11, **Con** 13, **Int** 8, **Wis** 13, **Cha** 12
**Base Atk** +3; **CMB** +1; **CMD** 12
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_
**Skills** Bluff +7, Fly +18, Knowledge (planes) +5, Perception +7, Stealth +14
**Languages** Abyssal, Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (2 of the following forms: lizard, _[[monsters/Octopus|octopus]]_, Small scorpion, venomous snake, _[[spells/Polymorph|polymorph]]_)

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary or swarm (2–10)
**Treasure** standard

### Special Abilities

**Disease (Su)** Cacodaemonia: Bite—injury; save Fort DC 12; onset 1 day; frequency 1/day; effect 1d2 Wis damage, cure 2 consecutive saves. In addition to the normal effects of the disease, as long as a victim is infected, the cacodaemon can telepathically communicate with the creature over any distance (as long as they remain on the same plane).
**Soul Lock (Su)** Once per day as a full-round action, a cacodaemon can ingest the spirit of any sentient creature that has died within the last minute. This causes a soul gem to grow inside of the cacodaemon’s gut, which it can regurgitate as a standard action. A soul gem is a fine-sized object with 1 hit point and hardness 2. Destroying a soul gem frees the soul within, though it does not return the deceased creature to life. This is a death effect. Any attempt to resurrect a body whose soul is trapped in a soul gem requires a DC 12 caster level check. Failure results in the spell having no effect, while success shatters the victim’s soul gem and returns the creature to life as normal. If the soul gem rests in an _[[items/Weapon Magic Abilities/Unholy|unholy]]_ location, such as that created by the spell _[[spells/Unhallow|unhallow]]_, the DC of this caster level check increases by +2. The caster level check DC is Charisma-based.

##### Description

Any evil outsider can, as a standard action, ingest a soul gem. Doing so frees the soul within, but condemns it to one of the lower planes (though the soul can be returned to life as normal). The outsider gains _fast healing_ 2 for a number of rounds equal to its Hit Dice.

The least of daemonkind, cacodaemons spawn from eddies of angry, violent, and demented souls amid the mists of Abaddon. Dim-witted but utterly evil, they endlessly seek to cause pain and indulge their hunger for mortal souls. Many more powerful fiends keep cacodaemons as pets, if only to be able to harvest the tiny creatures’ soul gems. A 7th-level spellcaster can gain a cacodaemon as a familiar if she has the _[[feats/Improved Familiar|Improved Familiar]]_ feat.