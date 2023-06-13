---
cssclass: [monsters]
title1: Moxix
desc_short: This strange, four-armed fiend appears to be constructed completely out
  of stone. Dried blood stains its body.
title2: Moxix
CR: 20
sources:
- name: Inner Sea Bestiary
  page: 32
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 307200
alignment: CE
size: Gargantuan
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 3
senses:
  blindsense: 60
  darkvision: 60
  see invisibility: true
auras:
- name: hopedrinker
  radius: 60
AC:
  AC: 34
  touch: 9
  flat_footed: 31
  components:
    dex: 3
    natural: 25
    size: -4
HP:
  HP: 379
  long: 23d10+253
saves:
  fort: 24
  ref: 10
  will: 22
defensive_abilities:
- gush
DR:
- amount: 15
  weakness: adamantine and good
immunities:
- electricity
- poison
resistances:
  acid: 20
  cold: 20
  fire: 20
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +29 (2d8+10/19-20)
      entries:
      - - damage: 2d8+10
          crit_range: 19-20
      attack: bite
      bonus:
      - 29
    - text: gore +29 (2d8+10)
      entries:
      - - damage: 2d8+10
      attack: gore
      bonus:
      - 29
    - text: 4 slams +29 (2d6+10/19-20 plus grab)
      entries:
      - - damage: 2d6+10
          crit_range: 19-20
        - effect: grab
      count: 4
      attack: slams
      bonus:
      - 29
  special:
  - breath weapon (60-ft. cone, 16d6 acid damage plus disease, Reflex DC 32 halves,
    usable every 1d4 rounds)
  - constrict (2d6+10)
  - rend (2 slams, 2d6+15)
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: mind blank
    source: default
    freq: Constant
  - name: see invisibility
    source: default
    freq: Constant
  - name: crushing despair
    source: default
    freq: At will
    DC: 21
  - name: detect magic
    source: default
    freq: At will
  - name: dispel magic
    source: default
    freq: At will
  - name: eyebite
    source: default
    freq: At will
    DC: 23
  - name: protection from good
    source: default
    freq: At will
  - name: stone shape
    source: default
    freq: At will
  - name: create undead
    source: default
    freq: 3/day
  - name: feeblemind
    source: default
    freq: 3/day
    DC: 22
  - name: insanity
    source: default
    freq: 3/day
    DC: 24
  - name: quickened mind fog
    source: default
    freq: 3/day
    DC: 22
  - name: phantasmal killer
    source: default
    freq: 3/day
    DC: 21
  - name: song of discord
    source: default
    freq: 3/day
    DC: 22
  - name: symbol of pain
    source: default
    freq: 3/day
    DC: 22
  - name: desecrate
    source: default
    freq: 1/day
  - name: greater teleport
    source: default
    freq: 1/day
    other: self plus 50 lbs. of objects only
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: any 1 CR 19
    - name: lower demon
      chance: 100%
  - name: symbol of insanity
    source: default
    freq: 1/day
    DC: 25
  - name: weird
    source: default
    freq: 1/day
    DC: 26
  sources:
  - name: default
    CL: 23
    concentration: 30
ability_scores:
  STR: 30
  DEX: 17
  CON: 32
  INT: 15
  WIS: 24
  CHA: 25
BAB: 23
CMB: 37
CMB_other: +41 grapple
CMD: 50
feats:
- name: Bleeding Critical
- name: Blind-Fight
- name: Cleave
- name: Combat Reflexes
- name: Critical Focus
- superscripts:
  - APG
  name: Dazing Assault
- name: Improved Critical (bite)
- name: Improved Critical (slam)
- name: Iron Will
- name: Power Attack
- name: Quicken Spell-Like Ability (mind fog)
- name: Vital Strike
skills:
  Bluff: 33
  Climb: 28
  Diplomacy: 25
  Intimidate: 33
  Knowledge (planes): 28
  Knowledge (religion): 21
  Perception: 33
  Sense Motive: 33
  Spellcraft: 25
languages:
- Abyssal
- Aklo
- Common
- telepathy 300 ft.
ecology:
  environment: warm jungles (Yoha's Graveyard)
  organization: solitary
  treasure_type: double
special_abilities:
  Breath Weapon (Su): |-
    Moxix can exhale a cone of acidic fog laced with a terrible disease. Any creature damaged by the acid of his breath weapon must succeed at a DC 28 Fortitude save or contract this disease. A humanoid afflicted with this disease must attempt a new Will save each day. If the humanoid fails, it attacks and attempts to eat the weakest humanoid nearby. If the save is successful, it resists this impulse. A humanoid who dies or is killed while afflicted rises as a ghast at the next midnight. The save DC is Charisma-based.

    Moxix's Delectation: Inhaled; save Fortitude DC 28; onset 1 day; frequency 1/day; effect 1d4 Con and 1d4 Wis damage; cure 2 consecutive saves.
  Gush (Ex): Anytime Moxix takes more than 50 points of weapon damage in a round,
    blood and pus spews forth from the wound. The blood is extremely slippery and
    sprays out in a 20-foot radius, coating all creatures and surfaces in the area.
    Any creatures in the area must succeed at a DC 28 Reflex save or drop any items
    they are holding. A saving throw must be made each round that the creature attempts
    to use or pick up an item it previously dropped. In addition, the area coated
    in the gushing blood is difficult to move about in, and creatures moving through
    the area must succeed at a DC 15 Acrobatics check or fall prone.
  Hopedrinker (Su): Moxix emits an aura that drains hope from all within 60 feet.
    All morale bonuses are suppressed within this aura, regardless of their source.
    In addition, spells and spell-like abilities granting a morale bonus are affected
    as dispel magic used to counterspell (caster level 23rd) every round at the beginning
    of Moxix's turn. A successful dispel check negates the entire effect (not just
    the morale bonus) and grants Moxix temporary hit points equal to the spell's level
    (to a maximum of 100). These temporary hit points last 1 hour.
  Mindshatter (Su): If a creature fails its save against Moxix's eyebite spell-like
    ability, as a standard action before the end of his turn he may unravel the target's
    mind and spirit. This acts as greater dispel magic (caster level 23rd) against
    effects that protect against mind-affecting or necromantic effects and automatically
    affects the target as enervation and touch of idiocy (duration 24 hours).
desc_long: |-
  Moxix, the Drinker of Human Hopes, is a unique demon bound to the mysterious isle called Yoha's Graveyard in the Shackles. Appearing as an eldritch four-armed statue of weathered gray stone, Moxix has a single emerald eye centered in his horrible face. A nest of twisted horns rests atop his head, and his fangf illed maw is perpetually stained with blood. Those courageous explorers traveling to his seemingly idyllic isle are driven mad by strange visions and dreams, or by inscrutable but disturbing carvings, idols, and glyphs that litter the island. Even if they withstand the island's maddening magic, adventurers in search of legendary lost riches may confront Moxix himself and be scourged of mind, body, and soul. Moxix's baleful presence and malevolent awareness leer from every crudely carved icon, relief, and idol bearing his likeness, bringing with them a tinge of insanity and a ravenous hunger for human flesh. Ghosts and pentagram-branded cannibals and lunatics are all that remain of ill-fated expeditions to Yoha's Graveyard. 

  Moxix found his first worshipers among the terrible cyclopes of Ghol-Gan as their civilization fell into ruin. As the one-eyed giants slipped more and more into depravity and violence, they began worshiping foul, otherworldly creatures their brothers and sisters brought up from the vaults of the Darklands after their exposure to the serpentfolk's wicked ways. Among the dozens of fiendish icons was Moxix, who came into inf luence among the cyclopes as their practice of sacrifice and cannibalism increased. It was at this time Moxix became known as the Drinker of Human Hopes. The ancient Ghol-Gan cyclopes fed him hundreds of captured humans, most of whom were of Azlanti descent. In one instance early in his time among the Ghol-Gan cyclopes, Moxix's followers captured an entire Azlanti embassy and fed them to the strange demon one by one while their companions watched in horror. Some say the sacrifices' spirits still inhabit the region, their wailing cries drifting through the hills and jungles of the haunted island.

  As his reign of blood began to spread from its base in southern Ghol-Gan, a raging contingent of rival cyclopes from elsewhere in the failing empire raided the demon-worshiping clan dedicated to Moxix, bringing both brute strength and the magic of powerful shamans and oracles to bear against it. The battle raged for 2 days, and in the end an oracle sacrificed her life in a final ploy to destroy Moxix. However, the oracle only succeeded in binding him to the high mountain peak that would one day become the island known as Yoha's Graveyard.

  To this very day, Moxix remains trapped in his island domain, ever eager to draw creatures to the ziggurat he calls home. There he delights in turning people to cannibalism, destruction, and insanity. Obscuring and disease-laden mists swirl around the island, keeping its lands hidden and protected from trespassers. Once per year, however, on the first full moon after the rainy season, the mists part for a single night. Some explorers have mounted expeditions to Moxix's island during these events, but as of yet, no one has returned the same person she used to be; all bear the mark of insanity Moxix stamps on their being.

---

# Moxix
This strange, four-armed fiend appears to be constructed completely out of stone. Dried blood stains its body.
**Source** Inner Sea Bestiary pg. 32
**XP** 307,200
CE Gargantuan outsider (chaotic, demon, evil, extraplanar)
**Init** +3; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 60 ft., _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +33
**Aura** hopedrinker (60 ft.)

##### Defense

**AC** 34, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 31 (+3 Dex, +25 natural, –4 size)
**hp** 379 (23d10+253)
**Fort** +24, **Ref** +10, **Will** +22
**Defensive Abilities** gush; **DR** 15/adamantine and good; **Immune** electricity, poison; **Resist** acid 20, cold 20, fire 20

##### Offense
**Speed** 40 ft.
**Melee** bite +29 (2d8+10/19–20), gore +29 (2d8+10), 4 slams +29 (2d6+10/19–20 plus _[[universal monster rules/Grab|grab]]_)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. cone, 16d6 acid damage plus disease, Reflex DC 32 halves, usable every 1d4 rounds), _[[universal monster rules/Constrict|constrict]]_ (2d6+10), _[[universal monster rules/Rend|rend]]_ (2 slams, 2d6+15)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 23rd; concentration +30)
Constant—_[[spells/Mind Blank|mind blank]]_, _see invisibility_
At will—_[[spells/Crushing Despair|crushing despair]]_ (DC 21), _[[spells/Detect Magic|detect magic]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Eyebite|eyebite]]_ (DC 23), _[[spells/Protection From Good|protection from good]]_, _[[spells/Stone Shape|stone shape]]_
3/day—_[[spells/Create Undead|create undead]]_, _[[spells/Feeblemind|feeblemind]]_ (DC 22), _[[spells/Insanity|insanity]]_ (DC 24), quickened _[[spells/Mind Fog|mind fog]]_ (DC 22), _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 21), _[[spells/Song of Discord|song of discord]]_ (DC 22), _[[spells/Symbol of Pain|symbol of pain]]_ (DC 22)
1/day—_[[spells/Desecrate|desecrate]]_, greater teleport (self plus 50 lbs. of objects only), _[[universal monster rules/Summon|summon]]_ (level 9, any 1 CR 19 or lower demon 100%), _[[spells/Symbol of Insanity|symbol of insanity]]_ (DC 25), _[[spells/Weird|weird]]_ (DC 26)

##### Statistics
**Str** 30, **Dex** 17, **Con** 32, **Int** 15, **Wis** 24, **Cha** 25
**Base Atk** +23; **CMB** +37 (+41 grapple); **CMD** 50
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Dazing Assault|Dazing Assault]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _Improved Critical_ (slam), _[[feats/Iron Will|Iron Will]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_mind fog_), _[[feats/Vital Strike|Vital Strike]]_
**Skills** Bluff +33, _[[universal monster rules/Climb|Climb]]_ +28, Diplomacy +25, Intimidate +33, Knowledge (planes) +28, Knowledge (religion) +21, Perception +33, Sense Motive +33, Spellcraft +25
**Languages** Abyssal, Aklo, Common; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.

##### Ecology

**Environment** warm jungles (Yoha’s Graveyard)
**Organization** solitary
**Treasure** double

### Special Abilities

**_Breath Weapon_ (Su) **_[[monsters/Moxix|Moxix]]_ can exhale a cone of acidic fog laced with a terrible disease. Any creature damaged by the acid of his _breath weapon_ must succeed at a DC 28 Fortitude save or contract this disease. A humanoid afflicted with this disease must attempt a new Will save each day. If the humanoid fails, it attacks and attempts to eat the weakest humanoid nearby. If the save is successful, it resists this impulse. A humanoid who dies or is killed while afflicted rises as a ghast at the next midnight. The save DC is Charisma-based.

_Moxix_’s Delectation: Inhaled; save Fortitude DC 28; onset 1 day; frequency 1/day; effect 1d4 Con and 1d4 Wis damage; cure 2 consecutive saves.

**Gush (Ex)** Anytime _Moxix_ takes more than 50 points of weapon damage in a round, blood and pus spews forth from the wound. The blood is extremely slippery and sprays out in a 20-foot radius, coating all creatures and surfaces in the area. Any creatures in the area must succeed at a DC 28 Reflex save or drop any items they are holding. A saving throw must be made each round that the creature attempts to use or pick up an item it previously dropped. In addition, the area coated in the gushing blood is difficult to move about in, and creatures moving through the area must succeed at a DC 15 Acrobatics check or fall _[[conditions/Prone|prone]]_.

**Hopedrinker (Su) **_Moxix_ emits an aura that drains hope from all within 60 feet. All morale bonuses are suppressed within this aura, regardless of their source. In addition, spells and _spell-like abilities_ granting a morale bonus are affected as _dispel magic_ used to counterspell (caster level 23rd) every round at the beginning of _Moxix_’s turn. A successful dispel check negates the entire effect (not just the morale bonus) and grants _Moxix_ temporary hit points equal to the spell’s level (to a maximum of 100). These temporary hit points last 1 hour.

**Mindshatter (Su)** If a creature fails its save against _Moxix_’s _eyebite_ spell-like ability, as a standard action before the end of his turn he may unravel the target’s mind and spirit. This acts as greater _dispel magic_ (caster level 23rd) against effects that protect against mind-affecting or necromantic effects and automatically affects the target as _[[spells/Enervation|enervation]]_ and _[[spells/Touch of Idiocy|touch of idiocy]]_ (duration 24 hours).

##### Description

_Moxix_, the Drinker of Human Hopes, is a unique demon bound to the mysterious isle _[[items/Weapon Magic Abilities/Called|called]]_ Yoha’s Graveyard in the Shackles. Appearing as an eldritch four-armed _[[spells/Statue|statue]]_ of weathered _[[monsters/Gray|gray]]_ stone, _Moxix_ has a single emerald eye centered in his horrible face. A nest of twisted horns rests atop his head, and his fangf illed maw is perpetually stained with blood. Those _[[items/Weapon Magic Abilities/Courageous|courageous]]_ explorers traveling to his seemingly idyllic isle are driven mad by strange visions and dreams, or by inscrutable but disturbing carvings, idols, and glyphs that litter the island. Even if they withstand the island’s maddening magic, adventurers in search of legendary lost riches may confront _Moxix_ himself and be scourged of mind, body, and soul. _Moxix_’s baleful presence and _[[items/Armor Magic Abilities/Malevolent|malevolent]]_ awareness leer from every crudely carved icon, relief, and idol bearing his likeness, bringing with them a tinge of _insanity_ and a _[[curses/Ravenous|ravenous]]_ hunger for human flesh. Ghosts and pentagram-branded cannibals and lunatics are all that remain of ill-fated expeditions to Yoha’s Graveyard.

_Moxix_ found his first worshipers among the terrible cyclopes of Ghol-Gan as their civilization fell into ruin. As the one-eyed giants slipped more and more into depravity and violence, they began worshiping foul, otherworldly creatures their brothers and sisters brought up from the vaults of the Darklands after their exposure to the _[[monsters/Serpentfolk|serpentfolk]]_’s wicked ways. Among the dozens of fiendish icons was _Moxix_, who came into inf luence among the cyclopes as their practice of _[[spells/Sacrifice|sacrifice]]_ and cannibalism increased. It was at this time _Moxix_ became known as the Drinker of Human Hopes. The ancient Ghol-Gan cyclopes fed him hundreds of captured humans, most of whom were of Azlanti descent. In one instance early in his time among the Ghol-Gan cyclopes, _Moxix_’s followers captured an entire Azlanti embassy and fed them to the strange demon one by one while their companions watched in horror. Some say the sacrifices’ spirits still inhabit the region, their wailing cries drifting through the hills and jungles of the haunted island.

As his reign of blood began to spread from its base in southern Ghol-Gan, a raging contingent of _[[feats/Rival|rival]]_ cyclopes from elsewhere in the failing empire raided the demon-worshiping clan dedicated to _Moxix_, bringing both brute strength and the magic of powerful shamans and oracles to bear against it. The battle raged for 2 days, and in the end an _[[classes/Oracle|oracle]]_ sacrificed her life in a final ploy to destroy _Moxix_. However, the _oracle_ only succeeded in _[[spells/Binding|binding]]_ him to the high mountain peak that would one day become the island known as Yoha’s Graveyard.

To this very day, _Moxix_ remains trapped in his island domain, ever eager to draw creatures to the ziggurat he calls home. There he delights in turning people to cannibalism, _[[spells/Destruction|destruction]]_, and _insanity_. Obscuring and disease-laden mists swirl around the island, keeping its lands hidden and protected from trespassers. Once per year, however, on the first full moon after the rainy season, the mists part for a single night. Some explorers have mounted expeditions to _Moxix_’s island during these events, but as of yet, no one has returned the same person she used to be; all bear the mark of _insanity_ _Moxix_ stamps on their being.