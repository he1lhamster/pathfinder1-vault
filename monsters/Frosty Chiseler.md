---
cssclass: [monsters]
title1: Frosty Chiseler
is_3.5: true
desc_short: This twisted little gnome with white-blue skin and a wild, red-tinged
  beard snarls and prances madly about, clutching a hammer in one hand and a bloody
  chisel in the other. A closer look reveals its huge bushy beard is not made of hair,
  but of living scintillating icicles as sharp as dagger-points and frosted with blood-spray
  from its last kill. The beard dances as madly as he, wriggling like a nest of razored
  ice snakes undulating to their own sinister rhythm. One of the malingering degenerate's
  eyes is significantly larger than the other, pulsing and bloodshot, its pupil lolling
  about like a ship in a storm.
title2: Frosty Chiseler
CR: 4
sources:
- name: Carnival of Tears
  page: 31
  link: http://paizo.com/store/paizo/pathfinder/modules/35E/v5748btpy80op
alignment: CE
size: Small
type: fey
subtypes:
- cold
initiative:
  bonus: 6
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 21
  touch: 17
  flat_footed: 15
  components:
    natural: 4
    dex: 6
    size: 1
HP:
  HP: 39
  long: 6d6+18
saves:
  fort: 5
  ref: 11
  will: 6
immunities:
- cold
weaknesses:
- fire vulnerability
- sonic vulnerability
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk light hammer +11 (1d4+1 plus 1d6 cold)
      entries:
      - - damage: 1d4+1
        - damage: 1d6
          type: cold
      attack: mwk light hammer
      bonus:
      - 11
  - - text: mwk light hammer +9 (1d4+1 plus 1d6 cold)
      entries:
      - - damage: 1d4+1
        - damage: 1d6
          type: cold
      attack: mwk light hammer
      bonus:
      - 9
    - text: mwk carver's chisel +9 (1d3+1/x3 plus 1d6 cold)
      entries:
      - - damage: 1d3+1
          crit_multiplier: 3
        - damage: 1d6
          type: cold
      attack: mwk carver's chisel
      bonus:
      - 9
    - text: bristle-ice beard +3 (1d4+1 plus 1d6 cold)
      entries:
      - - damage: 1d4+1
        - damage: 1d6
          type: cold
      attack: bristle-ice beard
      bonus:
      - 3
  ranged:
  - - text: icicle shard +10 (1d3+1 plus 1d6 cold)
      entries:
      - - damage: 1d3+1
        - damage: 1d6
          type: cold
      attack: icicle shard
      bonus:
      - 10
  special:
  - bristle-ice beard
  - brittlebones curse
  - frosty grasp
spell_like_abilities:
  entries:
  - name: disguise self
    source: default
    freq: 3/day
  - name: ice shape
    source: default
    freq: 3/day
    other: as stone shape but affects ice instead
  - name: mirror image
    source: default
    freq: 1/day
  - name: wall of ice
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 10
ability_scores:
  STR: 12
  DEX: 22
  CON: 16
  INT: 11
  WIS: 13
  CHA: 12
BAB: 3
grapple_3.5: 0
feats:
- name: Dodge
- name: Two-Weapon Fighting
- name: Weapon Finesse
skills:
  Balance: 8
  Bluff: 7
  Diplomacy: 3
  Disguise: 9
    acting: 11
    with disguise self: 21
  Escape Artist: 14
  Hide: 15
  Intimidation: 3
  Jump: 8
  Listen: 6
  Move Silently: 13
  Spot: 6
  Tumble: 13
  Use Rope: 6
languages:
- Common
- Sylvan
special_qualities:
- frostwalker
gear:
  gear:
  - mwk carving hammer (light hammer) and carving chisel (punching dagger)
ecology:
  environment: any cold
  organization: solitary, pair, or work crew (2d8)
  treasure_type: standard
  advancement_3.5:
  - type: size
    HD_min: 7
    size: Small
    HD_max: 10
special_abilities:
  Bristle Ice Beard (Su): A frosty chiseler's razorsharp ice-tined beard sprouts and
    juts wildly from his face and is nearly as large as he is. The vicious icy growth
    poses a serious threat to anyone attacking the fey in melee. An adjacent attacker
    must make a DC 16 Reflex save or take 1d4 points of slashing and 1d6 points of
    cold damage when she lands a blow against the chiseler, as his flailing oversized
    beard tears at her and flash freezes her flesh. The chiseler can break off sharp
    shards of his beard and hurl them at distant foes.
  Brittlebones Curse (Su): Once per day, a frosty chiseler may target a foe within
    30 feet and mutter “skin like ice, bones like glass, crack and snap and fractious
    smash!” The target must make a DC 14 Will save or be affected by a terrible curse
    that causes her to turn as brittle at delicate crystalline ice. If she takes more
    than a single move action each round she takes 1d6 points of damage and 1 point
    of Dexterity and 1 point of Strength damage as bits of her break off and she begins
    to fall to pieces. A DC 14 Fortitude save halves the damage and negates the ability
    damage but must be made every round she exerts herself. In addition she takes
    double damage from bludgeoning and sonic attacks. The curse lasts for one day,
    but can be lifted by a remove curse or similar magic.
  Frostwalker (Su): Frosty chiselers take no penalties to movement on ice, no matter
    how slippery, and cannot be forced to make Balance checks or Reflex saves to avoid
    falling on icy terrain. They may Climb icy surfaces as if under the effect of
    a spider climb spell.
  Frosty Grasp (Su): A frosty chiseler's natural attacks, as well as any weapons he
    wields, deal an additional 1d6 points of cold damage.
desc_long: |-
  Frosty chiselers were once master craftsmen and artisans of the fey. Either under the perverted sway of the Witch Queen or consigned to prolonged exile from the verdant lands of their people, these artists found themselves changed by a creeping cold that spread from their hearts to envelope their entire beings. Now they are demented perversions who delight only in evil acts. They still pride themselves as artists and craftsmen of unparalleled skill, but now their favorite medium is a blend of ice and mortal flesh rendered in frosty blood, pulped entrails, and scooped-out eyes.

  Environment: Frosty chiselers infest the frozen hillsides on the outskirts of humanoid settlements or any other frigid locale where a steady stream of victims is available (an abandoned trading post in a well-traveled snowy mountain pass or a frozen river bed or lake where unsuspecting children frolic and skate the slick ice). A host of chiselers serve the Witch Queen in the still, blue recesses of her ice palace. There, they craft wonders and horrors beyond mortal comprehension out of blocks of ice and captive humanoids.

  Typical Physical Characteristics: Frosty chiselers resemble deformed gnomes with wildly enormous beards of a thousand jutting icicles. One of their eyes is always larger than the other and peers from their head like a child's ball, riddled with bloodshot tracery. The average chiseler stands only three feet tall but weighs a hefty 100 pounds.

---

# Frosty Chiseler
This twisted little gnome with white-blue skin and a wild, red-tinged beard snarls and prances madly about, clutching a _[[items/Mundane/Hammer|hammer]]_ in one hand and a bloody chisel in the other. A closer look reveals its huge bushy beard is not made of hair, but of living scintillating icicles as sharp as dagger-points and _[[items/Armor Magic Abilities/Frosted|frosted]]_ with blood-spray from its last kill. The beard dances as madly as he, wriggling like a nest of razored ice snakes undulating to their own sinister rhythm. One of the malingering degenerate’s eyes is significantly larger than the other, pulsing and bloodshot, its pupil lolling about like a ship in a storm.
**Source** Carnival of Tears pg. 31
CE Small fey (cold)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Listen +6, Spot +6

##### Defense

**AC** 21, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+4 natural, +6 Dex, +1 size)
**hp** 39 (6d6+18)
**Fort** +5, **Ref** +11, **Will** +6
**Immune** cold
**Weaknesses** fire _[[curses/Vulnerability|vulnerability]]_, sonic _vulnerability_

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Light hammer|light hammer]]_ +11 (1d4+1 plus 1d6 cold) or mwk _light hammer_ +9 (1d4+1 plus 1d6 cold) and mwk carver's chisel +9 (1d3+1/x3 plus 1d6 cold) and bristle-ice beard +3 (1d4+1 plus 1d6 cold)
**Ranged** icicle shard +10 (1d3+1 plus 1d6 cold)
**Special Attacks** bristle-ice beard, brittlebones curse, frosty _[[spells/Grasp|grasp]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th)
3/day - _[[spells/Disguise Self|disguise self]]_, ice shape (as _[[spells/Stone Shape|stone shape]]_ but affects ice instead)
1/day - _[[spells/Mirror Image|mirror image]]_, _[[spells/Wall Of Ice|wall of ice]]_

##### Statistics
**Str** 12, **Dex** 22, **Con** 16, **Int** 11, **Wis** 13, **Cha** 12
**Base Atk** +3; **Grapple** +0
**Feats** Dodge, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Balance +8, Bluff +7, Diplomacy +3, Disguise +9 (+11 acting, +21 with _disguise self_), Escape Artist +14, Hide +15, Intimidate +3, _[[spells/Jump|Jump]]_ +8, Listen +6, Move Silently +13, Spot +6, Tumble +13, Use Rope +6
**Languages** Common, Sylvan
**SQ** frostwalker
**Gear** mwk carving _hammer_ (_light hammer_) and carving chisel (_[[items/Weapon/Punching dagger|punching dagger]]_)

##### Ecology

**Environment** any cold
**Organization** solitary, pair, or work crew (2d8)
**Treasure** standard
**Advancement** 7-10 HD (Small)

### Special Abilities

**_[[spells/Bristle|Bristle]]_ Ice Beard (Su)** A _[[monsters/Frosty Chiseler|frosty chiseler]]_’s razorsharp ice-tined beard sprouts and juts wildly from his face and is nearly as large as he is. The _[[items/Weapon Magic Abilities/Vicious|vicious]]_ icy growth poses a serious threat to anyone attacking the fey in melee. An adjacent attacker must make a DC 16 Reflex save or take 1d4 points of slashing and 1d6 points of cold damage when she lands a blow against the chiseler, as his flailing oversized beard tears at her and flash freezes her flesh. The chiseler can break off sharp shards of his beard and hurl them at distant foes.

**Brittlebones Curse (Su)** Once per day, a _frosty chiseler_ may target a foe within 30 feet and mutter “skin like ice, bones like glass, crack and snap and fractious _[[feats/Smash|smash]]_!” The target must make a DC 14 Will save or be affected by a terrible curse that causes her to turn as brittle at delicate crystalline ice. If she takes more than a single move action each round she takes 1d6 points of damage and 1 point of Dexterity and 1 point of Strength damage as bits of her break off and she begins to fall to pieces. A DC 14 Fortitude save halves the damage and negates the ability damage but must be made every round she exerts herself. In addition she takes double damage from bludgeoning and sonic attacks. The curse lasts for one day, but can be lifted by a _[[spells/Remove Curse|remove curse]]_ or similar magic.

**Frostwalker (Su)** Frosty chiselers take no penalties to movement on ice, no matter how slippery, and cannot be forced to make Balance checks or Reflex saves to avoid falling on icy terrain. They may _[[universal monster rules/Climb|Climb]]_ icy surfaces as if under the effect of a _[[spells/Spider Climb|spider climb]]_ spell.

**Frosty _Grasp_ (Su)** A _frosty chiseler_’s _[[universal monster rules/Natural Attacks|natural attacks]]_, as well as any weapons he wields, deal an additional 1d6 points of cold damage.

##### Description

Frosty chiselers were once master craftsmen and artisans of the fey. Either under the perverted sway of the _[[classes/Witch|Witch]]_ Queen or consigned to prolonged exile from the verdant lands of their people, these artists found themselves changed by a _[[items/Armor Magic Abilities/Creeping|creeping]]_ cold that spread from their hearts to envelope their entire beings. Now they are demented perversions who delight only in evil acts. They still pride themselves as artists and craftsmen of unparalleled skill, but now their favorite _[[classes/Medium|medium]]_ is a _[[spells/Blend|blend]]_ of ice and mortal flesh rendered in frosty blood, pulped entrails, and scooped-out eyes.

**Environment**: Frosty chiselers infest the frozen hillsides on the outskirts of humanoid settlements or any other frigid locale where a steady stream of victims is available (an abandoned trading post in a well-traveled snowy mountain pass or a frozen river bed or lake where unsuspecting children frolic and skate the _[[items/Armor Magic Abilities/Slick|slick]]_ ice). A host of chiselers serve the _Witch_ Queen in the still, blue recesses of her ice palace. There, they craft wonders and horrors beyond mortal comprehension out of blocks of ice and captive humanoids.

**Typical Physical Characteristics**: Frosty chiselers resemble deformed gnomes with wildly enormous beards of a thousand jutting icicles. One of their eyes is always larger than the other and peers from their head like a child’s ball, riddled with bloodshot tracery. The average chiseler stands only three feet tall but weighs a hefty 100 pounds.