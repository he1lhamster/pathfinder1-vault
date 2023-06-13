---
cssclass: [monsters]
title1: Automaton, Familiar Automaton
desc_short: This small construct resembles a house cat. It bears elaborate markings,
  and the core in its head glows with a warm light.
title2: Familiar Automaton
CR: 2
sources:
- name: Construct Handbook
  page: 24
  link: https://paizo.com/products/btq01vam
XP: 600
alignment: LN
size: Tiny
type: construct
subtypes:
- automaton
- extraplanar
initiative:
  bonus: 6
senses:
  darkvision: 120
  low-light vision: true
AC:
  AC: 14
  touch: 12
  flat_footed: 12
  components:
    dex: 2
    natural: 2
HP:
  HP: 15
  long: 3d10
  fast_healing: 2
saves:
  fort: 1
  ref: 3
  will: 1
DR:
- amount: 5
  weakness: adamantine
immunities:
- construct traits
- electricity
resistances:
  cold: 10
  sonic: 10
weaknesses:
- vulnerable mind
speeds:
  base: 20
  climb: 30
attacks:
  melee:
  - - text: bite +5 (1d3-1 plus disease)
      entries:
      - - damage: 1d3-1
        - effect: disease
      attack: bite
      bonus:
      - 5
    - text: 2 claws +5 (1d2-1)
      entries:
      - - damage: 1d2-1
      count: 2
      attack: claws
      bonus:
      - 5
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - name: detect magic
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: magic missile
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 1/week
    other: self plus 5 lbs. of objects only
  sources:
  - name: default
    CL: 3
    concentration: 4
ability_scores:
  STR: 8
  DEX: 15
  CON:
  INT: 14
  WIS: 10
  CHA: 14
BAB: 3
CMB: 0
CMD: 12
feats:
- name: Improved Initiative
- name: Weapon Finesse
skills:
  Climb: 7
  Diplomacy: 7
  Knowledge (any one): 8
  Perception: 6
  Spellcraft: 7
  Stealth: 8
  Use Magic Device: 7
languages:
- Common
- telepathy (touch)
special_qualities:
- automaton core
- intelligent construct
ecology:
  environment: any (Axis)
  organization: solitary
  treasure_type: none
special_abilities:
  Disease (Ex): 'Arcane fever: Bite-injury; save Fort DC 13; onset 1d3 days; frequency
    1/day; effect 1d3 Dex damage and 1d3 Int damage; cure 2 consecutive saves. The
    save DC is Constitution-based and includes a +2 racial bonus.'
desc_long: |-
  Familiar automatons were the most common of the automatons created within the Jistkan Imperium. The Artificer Conclave found itself overwhelmed with requests to join the group from hundreds of individuals they deemed unworthy of the more powerful automaton frames. Rather than turn these individuals away and risk the ire of so many Jistkans, the Conclave decided instead to transplant the majority of these individuals into familiar automatons. These familiars also served as a way for the Conclave to test new technologies and perfect the creation of automaton cores.

   All interested citizens were accepted to become familiar automatons so long as they could afford their automaton frame and the automaton core, though some were granted free of charge in order to allow further experimentation. As these automatons served as prototypes for a number of different technologies, most of the first few generations of familiars quickly failed and left their cores stranded without a body. The majority of these stranded cores were hidden away or used as parts in further research. Thanks to breakthroughs made with the aid of these cores, future generations of automatons were more stable and had the potential to remain intact indefinitely. A few existing accounts of automaton core creation reference some cores activating before their creation was complete, seemingly activated by the will of an individual lost from an early generation, though no records corroborate these notes.

   The Artificer Conclave experimented with a number of different forms and frames for the familiar automatons. The design of these forms had aesthetics in mind more than function, which led to the construction of especially elaborate familiars. Eventually, they settled on common animal shapes such as birds, dogs, and snakes, though cats quickly became one of the favorites. Wealthy individuals occasionally requested automaton frames modeled after rare creatures such as faerie dragons, imps, or lantern archons. This trend served the Conclave well, as they could charge high prices for more extravagant frames and then use the income they generated to fund the research and construction of more powerful automatons.

   A familiar automaton is usually the same size and twice the weight of the creature after which it is modeled. For the most part, nonfeline familiar automatons use the same statistics as the cat-based familiar automaton presented here, but more powerful familiar automatons may have additional abilities better suited for their more unique frames. On rare occasions, a familiar automaton bears spells engraved in markings on its body-usually signature spells of ancient mages, engraved on their forms by request. Some mages today keep these automatons as their personal familiars. A 7th-level lawful spellcaster with the Improved Familiar feat can select a familiar automaton as a familiar. These familiars serve well due to their innate ability to understand magic and magical items.

   Although most familiar automatons housed lowerranking citizens and worker-artificers, a number of these familiars housed more notable individuals. A number of judge-artificers and priest-artificers intentionally chose to become familiars rather than taking any of the more powerful automaton forms. The reasons for this varied from humility to a desire to escape from the conflict in which the Jistka Imperium was embroiled. Regardless of the reason, these high familiars, as they came to be known, each had their own powerful abilities. Some high familiars of note include the Judge Lord Valmen, who took on the form of an arbiter inevitable, and Urthilan the Star Priestess, who took a frame resembling a cassisian angel.

   Familiar automatons were not designed for combat but nevertheless feature a number of abilities to assist in fights. The most notable ability is the strange disease that each familiar automaton carries. What was originally a flaw of a familiar's automaton core eventually became a standard feature. Each of these cores leaks a minimal amount of energy that manifests as a disease known as arcane fever, technically a form of radiation sickness brought on by exposure to this planar energy. In a true twist of irony, the disease seems to be most potent against wizards, as they quickly forget how to prepare their spells as they slip further into the symptoms of the potent fever.

   Most familiar automatons do not bother searching for new automaton cores. The nature of a familiar automaton's body generally allows for any core to take dominance of the frame and discard the previous mentality; as such, most familiars tend to stay as far away from other cores as possible, content with their existing nature and unwilling to subject their frames to a new psyche. A rare few familiars have learned to maintain their minds across multiple cores, however, and these often work with other automatons to collect more cores, a practice that allows the familiar to live on far longer than it could on its own.

   As they were the most numerous automatons at the fall of the Jistka Imperium, familiar automatons are the most common variety found throughout Golarion. A familiar automaton's intelligence usually allows it to avoid detection when it likes, though scholars all over the world report sightings of these automatons in a variety of forms. The technological nature of Numeria allows familiar automatons to hide in plain sight, where onlookers believe the constructs to be curiosities or projects of local tinkerers-though a spellcaster who doesn't want to be forcibly separated from her familiar would be careful to keep a familiar automaton out of the eye of the Technic League.

   While most familiar automatons remain on Golarion, a sizable number reside elsewhere throughout the Great Beyond. The city of Axis houses quite a few familiar automatons, relaxing in peace as they go unnoticed among the strange citizens of the Eternal City. They tend to serve as messengers between the city's denizens, especially other automatons, an exception to most who tend to avoid others of their kind. Among champion automatons, familiars serve as chroniclers, recording great battles and sharing them with other champions; among stalkers, familiars usually act as solving to solve feuds or overseeing two hunters staging contests of skill where the familiar automaton serves as an impartial judge.

   The Boneyard also contains a surprising number of familiar automatons. Here, the constructs walk among the souls awaiting judgment, serving as temporary companions for petitioners. The nature of a petitioner's memory means that the petitioner usually does not recognize a familiar automaton but still retains a strong association with a beloved pet from its former life. This association provides comfort for especially distressed petitioners. Thanks to their ability to ease wary souls, a few catrina psychopomps establish friendships with familiar automatons, the two working in tandem to make the wait for judgment as painless as possible.

---

# Automaton, Familiar Automaton
This small construct resembles a house cat. It bears elaborate markings, and the core in its head glows with a warm light.
**Source** Construct Handbook pg. 24
**XP** 600

LN Tiny construct (automaton, extraplanar)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +6

##### Defense

**AC** 14, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+2 Dex, +2 natural)
**hp** 15 (3d10); _[[universal monster rules/Fast Healing|fast healing]]_ 2
**Fort** +1, **Ref** +3, **Will** +1
**DR** 5/adamantine; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_, electricity; **Resist** cold 10, sonic 10
**Weaknesses** vulnerable mind

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 30 ft.
**Melee** bite +5 (1d3-1 plus disease), 2 claws +5 (1d2-1)
**Space** 2-1/2 ft., **Reach** 0 ft.
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +4)
At will—_[[spells/Detect Magic|detect magic]]_, _[[spells/Invisibility|invisibility]]_ (self only)
3/day—_[[spells/Magic Missile|magic missile]]_
1/week—_[[spells/Plane Shift|plane shift]]_ (self plus 5 lbs. of objects only)

##### Statistics
**Str** 8, **Dex** 15, **Con** —, **Int** 14, **Wis** 10, **Cha** 14
**Base Atk** +3; **CMB** +0; **CMD** 12
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** _Climb_ +7, Diplomacy +7, Knowledge (any one) +8, Perception +6, Spellcraft +7, Stealth +8, Use Magic Device +7
**Languages** Common; _[[universal monster rules/Telepathy|telepathy]]_ (touch)
**SQ** _[[items/Wondrous Item/Automaton Core|automaton core]]_, intelligent construct

##### Ecology

**Environment** any (Axis)
**Organization** solitary
**Treasure** none

### Special Abilities

**Disease (Ex)** Arcane fever: Bite—injury; save Fort DC 13; onset 1d3 days; frequency 1/day; effect 1d3 Dex damage and 1d3 Int damage; cure 2 consecutive saves. The save DC is Constitution-based and includes a +2 racial bonus.

##### Description

Familiar automatons were the most common of the automatons created within the Jistkan Imperium. The Artificer Conclave found itself overwhelmed with requests to join the group from hundreds of individuals they deemed unworthy of the more powerful automaton frames. Rather than turn these individuals away and risk the ire of so many Jistkans, the Conclave decided instead to transplant the majority of these individuals into familiar automatons. These familiars also served as a way for the Conclave to test new technologies and perfect the creation of automaton cores.

All interested citizens were accepted to become familiar automatons so long as they could afford their automaton frame and the _automaton core_, though some were granted free of charge in order to allow further experimentation. As these automatons served as prototypes for a number of different technologies, most of the first few generations of familiars quickly failed and left their cores stranded without a body. The majority of these stranded cores were hidden away or used as parts in further research. Thanks to breakthroughs made with the aid of these cores, future generations of automatons were more _[[conditions/Stable|stable]]_ and had the potential to remain intact indefinitely. A few existing accounts of _automaton core_ creation reference some cores activating before their creation was complete, seemingly activated by the will of an individual lost from an early generation, though no records corroborate these notes.

The Artificer Conclave experimented with a number of different forms and frames for the familiar automatons. The design of these forms had aesthetics in mind more than function, which led to the construction of especially elaborate familiars. Eventually, they settled on common _[[spells/Animal Shapes|animal shapes]]_ such as birds, dogs, and snakes, though cats quickly became one of the favorites. Wealthy individuals occasionally requested automaton frames modeled after rare creatures such as faerie dragons, imps, or lantern archons. This trend served the Conclave well, as they could charge high prices for more extravagant frames and then use the income they generated to fund the research and construction of more powerful automatons.

A familiar automaton is usually the same size and twice the weight of the creature after which it is modeled. For the most part, nonfeline familiar automatons use the same statistics as the cat-based familiar automaton presented here, but more powerful familiar automatons may have additional abilities better suited for their more unique frames. On rare occasions, a familiar automaton bears spells engraved in markings on its body—usually signature spells of ancient mages, engraved on their forms by request. Some mages today keep these automatons as their personal familiars. A 7th-level lawful spellcaster with the _[[feats/Improved Familiar|Improved Familiar]]_ feat can select a familiar automaton as a familiar. These familiars serve well due to their innate ability to understand magic and magical items.

Although most familiar automatons housed lowerranking citizens and worker-artificers, a number of these familiars housed more notable individuals. A number of judge-artificers and priest-artificers intentionally chose to become familiars rather than taking any of the more powerful automaton forms. The reasons for this varied from humility to a desire to escape from the conflict in which the Jistka Imperium was embroiled. Regardless of the reason, these high familiars, as they came to be known, each had their own powerful abilities. Some high familiars of note include the Judge Lord Valmen, who took on the form of an arbiter inevitable, and Urthilan the Star Priestess, who took a frame resembling a cassisian angel.

Familiar automatons were not designed for combat but nevertheless feature a number of abilities to assist in fights. The most notable ability is the strange disease that each familiar automaton carries. What was originally a flaw of a familiar’s _automaton core_ eventually became a standard feature. Each of these cores leaks a minimal amount of energy that manifests as a disease known as arcane fever, technically a form of radiation sickness brought on by exposure to this _[[items/Weapon Magic Abilities/Planar|planar]]_ energy. In a true twist of irony, the disease seems to be most _[[items/Weapon Magic Abilities/Potent|potent]]_ against wizards, as they quickly forget how to prepare their spells as they slip further into the symptoms of the _potent_ fever.

Most familiar automatons do not bother searching for new automaton cores. The nature of a familiar automaton’s body generally allows for any core to take dominance of the frame and discard the previous mentality; as such, most familiars tend to stay as far away from other cores as possible, content with their existing nature and unwilling to subject their frames to a new psyche. A rare few familiars have learned to maintain their minds across multiple cores, however, and these often work with other automatons to collect more cores, a practice that allows the familiar to live on far longer than it could on its own.

As they were the most numerous automatons at the fall of the Jistka Imperium, familiar automatons are the most common variety found throughout Golarion. A familiar automaton’s intelligence usually allows it to avoid detection when it likes, though scholars all over the world report sightings of these automatons in a variety of forms. The technological nature of Numeria allows familiar automatons to hide in plain sight, where onlookers believe the constructs to be curiosities or projects of local tinkerers—though a spellcaster who doesn’t want to be forcibly separated from her familiar would be careful to keep a familiar automaton out of the eye of the Technic League.

While most familiar automatons remain on Golarion, a sizable number reside elsewhere throughout the Great Beyond. The city of Axis houses quite a few familiar automatons, relaxing in peace as they _[[feats/Go Unnoticed|go unnoticed]]_ among the strange citizens of the Eternal City. They tend to serve as messengers between the city’s denizens, especially other automatons, an exception to most who tend to avoid others of their kind. Among _[[items/Armor Magic Abilities/Champion|champion]]_ automatons, familiars serve as chroniclers, recording great battles and sharing them with other champions; among stalkers, familiars usually act as solving to solve feuds or overseeing two hunters staging contests of skill where the familiar automaton serves as an impartial judge.

The Boneyard also contains a surprising number of familiar automatons. Here, the constructs walk among the souls awaiting judgment, serving as temporary companions for petitioners. The nature of a _[[monsters/Petitioner|petitioner]]_’s memory means that the _petitioner_ usually does not recognize a familiar automaton but still retains a strong association with a beloved pet from its former life. This association provides _[[items/Armor Magic Abilities/Comfort|comfort]]_ for especially distressed petitioners. Thanks to their ability to ease wary souls, a few catrina psychopomps establish friendships with familiar automatons, the two working in tandem to make the wait for judgment as painless as possible.