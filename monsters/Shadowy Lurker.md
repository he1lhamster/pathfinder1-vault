---
cssclass: [monsters]
title1: Shadowy Lurker
is_3.5: true
desc_short: This umbral creature, resembling a gaunt, stunted elf trailing wisps of
  dark mist, grins evilly. Its large amber eyes grow hungrily.
title2: Shadowy Lurker
CR: 8
sources:
- name: Gallery of Evil
  page: 27
  link: http://paizo.com/store/paizo/pathfinder/modules/35E/v5748btpy804h
alignment: NE
size: Small
type: undead
subtypes:
- incorporeal
initiative:
  bonus: 5
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 19
  flat_footed: 14
  components:
    deflection: 3
    dex: 5
    size: 1
HP:
  HP: 32
  long: 5d12
  fast_healing: 5
  fast_healing_weakness: see below
saves:
  fort: 1
  ref: 6
  will: 6
immunities:
- incorporeal traits
- undead traits
speeds:
  fly: 40
attacks:
  melee:
  - - text: incorporeal touch +9 (1d6 Charisma drain)
      entries:
      - - damage: 1d6
          type: Charisma drain
      attack: incorporeal touch
      bonus:
      - 9
  special:
  - possession (DC 17)
space: 5
reach: 5
spell_like_abilities:
  entries:
  - name: ghost sound
    source: default
    freq: At will
    DC: 13
  - name: major image
    source: default
    freq: At will
    DC: 16
  - name: ventriloquism
    source: default
    freq: At will
    DC: 14
  sources:
  - name: default
    CL: 5
ability_scores:
  STR:
  DEX: 20
  CON:
  INT: 16
  WIS: 14
  CHA: 17
BAB: 2
grapple_3.5: '-'
feats:
- name: Flyby Attack
- name: Weapon Focus (incorporeal touch)
skills:
  Bluff: 8
  Concentration: 5
  Hide: 18
  Knowledge (arcana): 8
  Listen: 10
  Move Silently: 18
  Search: 10
  Spellcraft: 8
  Spot: 10
  _racial_mods:
    Listen:
      _: 2
    Search:
      _: 2
    Spot:
      _: 2
    Hide:
      _: 8
    Move Silently:
      _: 8
languages:
- Common
- Sylvan
special_qualities:
- dimensional step
- incorporeal
- painting dependent
ecology:
  environment: any land (usually urban)
  organization: solitary
  treasure_type: standard
  advancement_3.5:
  - type: size
    HD_min: 6
    size: Medium
    HD_max: 10
special_abilities:
  Charisma Drain (Ex): A shadowy lurker drains 1d6 Charisma points with each successful
    incorporeal slam attack.
  Dimensional Step (Su): As a free action, a shadowy lurker can move from one painting
    to another in a way similar to the dimension door spell, except no two paintings
    can be more than 30 feet apart from each other and from its bonded painting (see
    below). A shadowy lurker's dimensional step ability is suppressed in an antimagic
    field or by dimensional lock and dimensional anchor spells.
  Fast Healing (Su): A wounded shadowy lurker may retreat into its bonded painting
    and regain lost hit points at the rate of 5 hp per round.
  Painting Dependent (Ex): A shadowy lurker is bonded to a single masterwork quality
    painting. If the painting is ever destroyed, the shadowy lurker dies in 4d6 hours.
  Possession (Su): If a shadowy lurker drains an opponent to 0 Charisma, it immediately
    attempts to possess the target creature's body. The intended victim may attempt
    a DC 17 Will save to resist it. If successful, the creature becomes catatonic
    and cannot be targeted by the same shadowy lurker's possession ability for 24
    hours. If the opponent fails its Will save, its soul is forced into the shadowy
    lurker's bonded painting, which acts as the receptacle for the purposes of this
    ability, while the shadowy lurker takes over the creature's body. In all other
    ways, this ability duplicates the effects of a magic jar spell (CL 9th). The save
    DC is Charisma based and includes a +2 racial bonus.
desc_long: |-
  Shadowy lurkers were once the celebrated artisans of the First Elves of Golarion. They were unsurpassed in their skill with paint and brush, responsible for works of art so beautiful that lesser races wept at the sight of them.

  Dark powers already hateful of the elves grew increasingly jealous of the artisans and plotted their downfall. One of these evil creatures disguised itself as an ambassador from another world and came to them with claims that the artists of his world used colors and textures that made what the elven artisans produced look like charcoal sketches. The elves, puffed up with the hubris of generations of unrivaled artistry, were intrigued by these tales. The ambassador promised to take them on a visit to his home world, where they could see for themselves. He so thoroughly seduced the artisans that every one of them agreed to go.

  When the day came for their extraplanar trip, the ambassador opened a shimmering golden gate. The gate trapped them in the First World, the world of spirits and birthplace of fey, which stripped them of their bodies and forced them to wander in a colorless reflection of the physical world.

  Undeath made the artisans hateful and malicious, transforming them into stunted, shadowy versions of their former selves. In time they discovered portals back to their world. Ironically, these "portals" were in fact the paintings they had crafted so many centuries before, collected in galleries all across Golarion. Obsessed over their lost lives, the shadowy lurkers found their own works. The shadowy lurkers learned how to bond with their paintings and cross over into the Material Plane. Through their paintings they can even take control of nearby host bodies by sapping their victims' willpower. The artisans became so dependent on their connection to their bonded paintings that if these receptacles are ever destroyed, they perish. To protect their paintings, shadowy lurkers have learned tricks of illusion and can move from painting to painting to confuse their enemies.

  Environment: Shadowy lurkers follow their paintings and frequently appear in ancient galleries and vaults on the Material Plane. These paintings often have something slightly unsettling about them. Indeed, on a DC 30 Spot check, shadows in the painting appear a bit off and even seem to move around on their own.

  Typical Physical Characteristics: Shadowy lurkers resemble emaciated miniature elves with pinched, angry faces and large pale eyes that lack pupils. Their hands and feet trail wisps of shadow. A typical shadowy lurker is approximately 4 feet tall.

---

# Shadowy Lurker
This _[[items/Weapon Magic Abilities/Umbral|umbral]]_ creature, resembling a gaunt, stunted elf trailing wisps of dark mist, grins evilly. Its large amber eyes grow hungrily.
**Source** Gallery of Evil pg. 27

NE Small undead (_[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Listen +10, Spot +10

##### Defense

**AC** 19, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 deflection, +5 Dex, +1 size)
**hp** 32 (5d12); _[[universal monster rules/Fast Healing|fast healing]]_ 5 (see below)
**Fort** +1, **Ref** +6, **Will** +6
**Immune** _incorporeal_ traits, _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** fly 40 ft.
**Melee** _incorporeal_ touch +9 (1d6 Charisma drain)
**Space** 5 ft., **Reach** 5 ft.
**Special Attacks** _[[spells/Possession|possession]]_ (DC 17)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th)
At will - _[[spells/Ghost Sound|ghost sound]]_ (DC 13), _[[spells/Major Image|major image]]_ (DC 16), _[[spells/Ventriloquism|ventriloquism]]_ (DC 14)

##### Statistics
**Str** —, **Dex** 20, **Con** —, **Int** 16, **Wis** 14, **Cha** 17
**Base Atk** +2; **Grapple** —
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_incorporeal_ touch)
**Skills** Bluff +8, Concentration +5, Hide +18, Knowledge (arcana) +8, Listen +10, Move Silently +18, Search +10, Spellcraft +8, Spot +10; **Racial Modifiers** +2 Listen, +2 Search, +2 Spot, +8 Hide, +8 Move Silently
**Languages** Common, Sylvan
**SQ** dimensional step, _incorporeal_, painting dependent

##### Ecology

**Environment** any land (usually urban)
**Organization** solitary
**Treasure** standard
**Advancement** 6-10 HD (_[[classes/Medium|Medium]]_)

### Special Abilities

**Charisma Drain (Ex)** A _[[monsters/Shadowy Lurker|shadowy lurker]]_ drains 1d6 Charisma points with each successful _incorporeal_ slam attack.

**Dimensional Step (Su)** As a free action, a _shadowy lurker_ can move from one painting to another in a way similar to the _[[spells/Dimension Door|dimension door]]_ spell, except no two paintings can be more than 30 feet apart from each other and from its bonded painting (see below). A _shadowy lurker_'s dimensional step ability is suppressed in an _[[spells/Antimagic Field|antimagic field]]_ or by _[[spells/Dimensional Lock|dimensional lock]]_ and _[[spells/Dimensional Anchor|dimensional anchor]]_ spells.

**_Fast Healing_ (Su)** A wounded _shadowy lurker_ may retreat into its bonded painting and regain lost hit points at the rate of 5 hp per round.

**Painting Dependent (Ex)** A _shadowy lurker_ is bonded to a single masterwork quality painting. If the painting is ever destroyed, the _shadowy lurker_ dies in 4d6 hours.

**_Possession_ (Su)** If a _shadowy lurker_ drains an opponent to 0 Charisma, it immediately attempts to possess the target creature's body. The intended victim may attempt a DC 17 Will save to resist it. If successful, the creature becomes catatonic and cannot be targeted by the same _shadowy lurker_'s _possession_ ability for 24 hours. If the opponent fails its Will save, its soul is forced into the _shadowy lurker_'s bonded painting, which acts as the receptacle for the purposes of this ability, while the _shadowy lurker_ takes over the creature's body. In all other ways, this ability duplicates the effects of a _[[spells/Magic Jar|magic jar]]_ spell (CL 9th). The save DC is Charisma based and includes a +2 racial bonus.

##### Description

Shadowy lurkers were once the celebrated artisans of the First Elves of Golarion. They were unsurpassed in their skill with paint and brush, responsible for works of art so beautiful that lesser races wept at the sight of them.

Dark powers already hateful of the elves grew increasingly jealous of the artisans and plotted their downfall. One of these evil creatures disguised itself as an ambassador from another world and came to them with claims that the artists of his world used colors and textures that made what the elven artisans produced look like _[[items/Mundane/Charcoal|charcoal]]_ sketches. The elves, puffed up with the hubris of generations of unrivaled artistry, were intrigued by these tales. The ambassador promised to take them on a visit to his home world, where they could see for themselves. He so thoroughly seduced the artisans that every one of them agreed to go.

When the day came for their extraplanar _[[universal monster rules/Trip|trip]]_, the ambassador opened a shimmering golden _[[spells/Gate|gate]]_. The _gate_ trapped them in the First World, the world of spirits and birthplace of fey, which stripped them of their bodies and forced them to wander in a colorless reflection of the physical world.

Undeath made the artisans hateful and malicious, transforming them into stunted, shadowy versions of their former selves. In time they discovered portals back to their world. Ironically, these "portals" were in fact the paintings they had crafted so many centuries before, collected in galleries all across Golarion. Obsessed over their lost lives, the shadowy lurkers found their own works. The shadowy lurkers learned how to bond with their paintings and cross over into the Material Plane. Through their paintings they can even take control of nearby host bodies by _[[items/Weapon Magic Abilities/Sapping|sapping]]_ their victims' willpower. The artisans became so dependent on their connection to their bonded paintings that if these receptacles are ever destroyed, they perish. To protect their paintings, shadowy lurkers have learned tricks of illusion and can move from painting to painting to confuse their enemies.

**Environment**: Shadowy lurkers follow their paintings and frequently appear in ancient galleries and vaults on the Material Plane. These paintings often have something slightly unsettling about them. Indeed, on a DC 30 Spot check, shadows in the painting appear a bit off and even seem to move around on their own.

**Typical Physical Characteristics**: Shadowy lurkers resemble emaciated miniature elves with pinched, angry faces and large pale eyes that lack pupils. Their hands and feet trail wisps of _[[items/Armor Magic Abilities/Shadow|shadow]]_. A typical _shadowy lurker_ is approximately 4 feet tall.