---
cssclass: [monsters]
title1: Herecite, Herecite of Asmodeus
desc_short: A palpable sense of despair clings to the rotting frame of this decaying
  man. Tears of blood run from his eye sockets, yet his expression is one of unquenched
  rage.
title2: Herecite of Asmodeus
CR: 9
sources:
- name: 'Pathfinder #100: A Song of Silver'
  page: 116
  link: http://paizo.com/products/btpy9grm?Pathfinder-Adventure-Path-100-A-Song-of-Silver
- name: Bestiary 6
  page: 154
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
XP: 6400
alignment: LE
size: Medium
type: undead
initiative:
  bonus: 8
senses:
  darkvision: 60
  detect good: true
  see invisibility: true
auras:
- name: desecration
  radius: 30
AC:
  AC: 24
  touch: 19
  flat_footed: 20
  components:
    dex: 4
    natural: 5
    profane: 5
HP:
  HP: 138
  long: 12d8+84
saves:
  fort: 11
  ref: 10
  will: 11
defensive_abilities:
- channel resistance +6
- profane insight
DR:
- amount: 10
  weakness: good
immunities:
- undead traits
SR: 20 (24 vs. divine spells)
speeds:
  base: 40
attacks:
  melee:
  - - text: +2 unholy heavy mace +19/+14 (1d8+10/19-20 plus faith-stealing strike)
      entries:
      - - damage: 1d8+10
          crit_range: 19-20
        - effect: faith-stealing strike
      attack: +2 unholy heavy mace
      bonus:
      - 19
      - 14
    - text: slam +12 (1d8+5 plus faith-stealing strike)
      entries:
      - - damage: 1d8+5
        - effect: faith-stealing strike
      attack: slam
      bonus:
      - 12
  - - text: 2 slams +17 (1d8+8 plus faith-stealing strike)
      entries:
      - - damage: 1d8+8
        - effect: faith-stealing strike
      count: 2
      attack: slams
      bonus:
      - 17
  special:
  - faith-stealing strike
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: burning hands
    source: default
    freq: At will
    DC: 16
  - name: disguise self
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: 3/day
  - name: produce flame
    source: default
    freq: 3/day
  - name: unholy blight
    source: default
    freq: 3/day
    DC: 19
  - name: confusion
    source: default
    freq: 1/day
    DC: 19
  - name: fireball
    source: default
    freq: 1/day
    DC: 18
  - name: nondetection
    source: default
    freq: 1/day
  - name: wall of fire
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 10
    concentration: 15
ability_scores:
  STR: 22
  DEX: 19
  CON:
  INT: 14
  WIS: 9
  CHA: 21
BAB: 9
CMB: 15
CMD: 34
feats:
- name: Combat Casting
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Power Attack
- name: Skill Focus (Perception)
skills:
  Bluff: 17
  Intimidate: 20
  Knowledge (planes): 14
  Knowledge (religion): 17
  Perception: 20
  Sense Motive: 14
languages:
- Common
- Infernal
special_qualities:
- cabal
- herecite domains (Fire, Trickery)
- profane insight
- unleash heresy
ecology:
  environment: any
  organization: solitary or cabal (2-5)
  treasure_type: double
  treasure:
  - +2 heavy mace
  - other treasure
special_abilities:
  Cabal (Ex): |-
    Multiple herecites can form a cabal to gain increased magical abilities and defenses. A cabal consists of two to five herecites. The ritual to form a cabal (or to welcome new herecites into an existing cabal) requires 24 hours of worship, prayer, and vile sacrifice, after which point the herecites become bound to the area in which the ritual was performed (this area can be no larger than one 50-foot cube per herecite in the cabal, to a maximum of five 50-foot cubes for a cabal of five herecites). If any one member of a herecite cabal leaves this area, it and all other herecites in the cabal lose all of the shared abilities granted by their cabal and they must perform the ritual once again to regain these abilities.

     All herecites in a cabal gain the spell-like abilities granted by each individual herecite's domains (in the case of duplicate domains, no additional spelllike abilities are gained-most herecite cabals consist of herecites with individually different domains). All herecites in a cabal share one mind, can communicate telepathically, and gain a +4 bonus on initiative checks and Perception checks. If at least one herecite in a cabal disbelieves an illusion, all other herecites in the cabal are considered to disbelieve the illusion. If one herecite is aware of combatants, all other herecites in that cabal area also aware of those combatants, and if one member is injured or killed, all remaining herecites are aware of it. As long as the cabal exists, all herecites in the cabal gain fast healing 10.
  Desecration Aura (Su): A herecite's very existence is an embodiment of desecration,
    and as such it exudes a 30-foot-radius aura of desecration. It and all undead
    within this area gain a +2 profane bonus on attack rolls, damage rolls, and saving
    throws, and the DC to resist negative channeled energy in the area increases by
    6. The herecite itself gains 2 hit points per Hit Die (+24 hit points for most
    herecites). All of these benefits are calculated into the above stats, and while
    they do not stack with those granted by desecrate spells, neither do they vanish
    if the herecite enters an area under the effect of a consecrate spell.
  Faith-Stealing Strike (Su): A nonevil divine spellcaster struck by a herecite's
    slam attack or by its favored weapon must succeed at a DC 21 Will save or be unable
    to cast any divine spells for 1 round. Once a creature successfully saves, it
    is immune to further faith-stealing strikes from that particular herecite for
    24 hours. The save DC is Charisma-based.
  Herecite Domains: A herecite is associated with one evil god, and is always of the
    same alignment as that god. The herecite selects two domains granted by that god,
    gaining both domain's 1st-level spells as at-will spell-like abilities, the 2nd-level
    spells as 3/day spell-like abilities, and the 3rd- and 4th-level spells as 1/day
    spell-like abilities. Inappropriate spells granted by domains, or spells that
    duplicate the herecite's existing spell-like abilities, are replaced with inflict
    spells of the same level. For example, a herecite with access to Healing would
    swap out all four of its cure spells for the inflict versions, while a herecite
    with access to Glory would swap out bless weapon for inflict moderate wounds,
    searing light for inflict serious wounds, and holy smite for inflict critical
    wounds. The herecite above is a herecite of Asmodeus with the Fire and Trickery
    domains. These spell-like abilities are in addition to the herecite's base spell-like
    abilities (detect good, see invisibility, and unholy blight).
  Profane Insight (Su): A herecite adds its Charisma bonus (+5 for most herecites)
    to its AC as a profane bonus. It is proficient with the favored weapon of its
    associated deity, and if it wields its deity's favored weapon, that weapon gains
    the unholy weapon ability. Against divine spells, the herecite's SR increases
    by 4.
  Unleash Heresy (Su): When a herecite is destroyed, it explodes, dealing 3d6 negative
    energy damage to all creatures in a 30-foot radius (Reflex DC 21 half). Any nonevil
    creature damaged by this energy must also succeed at a DC 21 Will save or be affected
    by the herecite's faith-stealing strike. The save DC is Charisma-based.
desc_long: Herecites are a particularly blasphemous form of undead created via an
  obscure ritual of sacrifice, wherein a priest of an evil god offers up at least
  five worshipers of a nonevil deity to her own deity. All of the sacrifices must
  worship the same deity. Upon the death of the sacrificed worshipers, their souls
  and bodies seethe and surge with negative energy, then melt away only to reform
  into a single entity-a herecite. Even the herecite's appearance serves to support
  its heretical nature, for these foul creations always appear as undead versions
  of their prior god, even though now, in their new unlife, they are devoted worshipers
  of the god to whom they were sacrificed. Regardless of the size and shape of the
  worshipers sacrificed, or the mythological size of their prior deity, a herecite
  is a human-sized creature.

---

# Herecite, Herecite of Asmodeus
A palpable sense of despair clings to the rotting frame of this decaying man. Tears of blood run from his eye sockets, yet his expression is one of unquenched _[[spells/Rage|rage]]_.
**Source** Pathfinder #100: A Song of Silver pg. 116, Bestiary 6 pg. 154
**XP** 6,400

LE Medium undead
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +20
**Aura** desecration (30 ft.)

##### Defense

**AC** 24, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+4 Dex, +5 natural, +5 profane)
**hp** 138 (12d8+84)
**Fort** +11, **Ref** +10, **Will** +11
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +6, profane insight; **DR** 10/good; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 20 (24 vs. divine spells)

##### Offense
**Speed** 40 ft.
**Melee** +2 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Heavy mace|heavy mace]]_ +19/+14 (1d8+10/19–20 plus faith-stealing strike), slam +12 (1d8+5 plus faith-stealing strike) or 2 slams +17 (1d8+8 plus faith-stealing strike)
**Special Attacks** faith-stealing strike
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +15)
Constant—_detect good_, _see invisibility_
At will—_[[spells/Burning Hands|burning hands]]_ (DC 16), _[[spells/Disguise Self|disguise self]]_
3/day—_[[spells/Invisibility|invisibility]]_, _[[spells/Produce Flame|produce flame]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
1/day—_[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Fireball|fireball]]_ (DC 18), _[[spells/Nondetection|nondetection]]_, _[[spells/Wall Of Fire|wall of fire]]_

##### Statistics
**Str** 22, **Dex** 19, **Con** —, **Int** 14, **Wis** 9, **Cha** 21
**Base Atk** +9; **CMB** +15; **CMD** 34
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception)
**Skills** Bluff +17, Intimidate +20, Knowledge (planes) +14, Knowledge (religion) +17, Perception +20, Sense Motive +14
**Languages** Common, Infernal
**SQ** cabal, herecite domains (Fire, Trickery), profane insight, unleash heresy

##### Ecology

**Environment** any
**Organization** solitary or cabal (2–5)
**Treasure** double (+2 _heavy mace_, other treasure)

### Special Abilities

**Cabal (Ex)** Multiple herecites can form a cabal to gain increased magical abilities and defenses. A cabal consists of two to five herecites. The ritual to form a cabal (or to welcome new herecites into an existing cabal) requires 24 hours of worship, _[[spells/Prayer|prayer]]_, and vile _[[spells/Sacrifice|sacrifice]]_, after which point the herecites become bound to the area in which the ritual was performed (this area can be no larger than one 50-foot cube per herecite in the cabal, to a maximum of five 50-foot cubes for a cabal of five herecites). If any one member of a herecite cabal leaves this area, it and all other herecites in the cabal lose all of the shared abilities granted by their cabal and they must perform the ritual once again to regain these abilities.

All herecites in a cabal gain the _spell-like abilities_ granted by each individual herecite’s domains (in the case of duplicate domains, no additional spelllike abilities are gained—most herecite cabals consist of herecites with individually different domains). All herecites in a cabal share _[[feats/One Mind|one mind]]_, can communicate telepathically, and gain a +4 bonus on initiative checks and Perception checks. If at least one herecite in a cabal disbelieves an illusion, all other herecites in the cabal are considered to disbelieve the illusion. If one herecite is aware of combatants, all other herecites in that cabal area also aware of those combatants, and if one member is injured or killed, all remaining herecites are aware of it. As long as the cabal exists, all herecites in the cabal gain _[[universal monster rules/Fast Healing|fast healing]]_ 10.

**Desecration Aura (Su)** A herecite’s very existence is an embodiment of desecration, and as such it exudes a 30-foot-radius aura of desecration. It and all undead within this area gain a +2 profane bonus on attack rolls, damage rolls, and saving throws, and the DC to resist negative channeled energy in the area increases by 6. The herecite itself gains 2 hit points per Hit Die (+24 hit points for most herecites). All of these benefits are calculated into the above stats, and while they do not stack with those granted by _[[spells/Desecrate|desecrate]]_ spells, neither do they _[[spells/Vanish|vanish]]_ if the herecite enters an area under the effect of a _[[feats/Consecrate Spell|consecrate spell]]_.

**Faith-Stealing Strike (Su)** A nonevil divine spellcaster struck by a herecite’s slam attack or by its favored weapon must succeed at a DC 21 Will save or be unable to cast any divine spells for 1 round. Once a creature successfully saves, it is immune to further faith-stealing strikes from that particular herecite for 24 hours. The save DC is Charisma-based.

**Herecite Domains** A herecite is associated with one evil god, and is always of the same alignment as that god. The herecite selects two domains granted by that god, gaining both domain’s 1st-level spells as at-will _spell-like abilities_, the 2nd-level spells as 3/day _spell-like abilities_, and the 3rd- and 4th-level spells as 1/day _spell-like abilities_. Inappropriate spells granted by domains, or spells that duplicate the herecite’s existing _spell-like abilities_, are replaced with inflict spells of the same level. For example, a herecite with access to Healing would swap out all four of its cure spells for the inflict versions, while a herecite with access to Glory would swap out _[[spells/Bless Weapon|bless weapon]]_ for _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_, _[[spells/Searing Light|searing light]]_ for _[[spells/Inflict Serious Wounds|inflict serious wounds]]_, and _[[spells/Holy Smite|holy smite]]_ for _[[spells/Inflict Critical Wounds|inflict critical wounds]]_. The herecite above is a herecite of Asmodeus with the Fire and Trickery domains. These _spell-like abilities_ are in addition to the herecite’s base _spell-like abilities_ (_detect good_, _see invisibility_, and _unholy blight_).

**Profane Insight (Su)** A herecite adds its Charisma bonus (+5 for most herecites) to its AC as a profane bonus. It is proficient with the favored weapon of its associated deity, and if it wields its deity’s favored weapon, that weapon gains the _unholy_ weapon ability. Against divine spells, the herecite’s SR increases by 4.

**Unleash Heresy (Su)** When a herecite is destroyed, it explodes, dealing 3d6 negative energy damage to all creatures in a 30-foot radius (Reflex DC 21 half). Any nonevil creature damaged by this energy must also succeed at a DC 21 Will save or be affected by the herecite’s faith-stealing strike. The save DC is Charisma-based.

##### Description

Herecites are a particularly blasphemous form of undead created via an obscure ritual of _sacrifice_, wherein a priest of an evil god offers up at least five worshipers of a nonevil deity to her own deity. All of the sacrifices must worship the same deity. Upon the death of the sacrificed worshipers, their souls and bodies seethe and surge with negative energy, then melt away only to reform into a single entity—a herecite. Even the herecite’s appearance serves to support its _[[items/Weapon Magic Abilities/Heretical|heretical]]_ nature, for these foul creations always appear as undead versions of their prior god, even though now, in their new unlife, they are devoted worshipers of the god to whom they were sacrificed. Regardless of the size and shape of the worshipers sacrificed, or the mythological size of their prior deity, a herecite is a human-sized creature.