---
cssclass: [monsters]
title1: Failed Prophet
desc_short: A spider-webbing network of fine golden veins covers the body of this
  skinless, stony-eyed humanoid.
title2: Failed Prophet
CR: 11
sources:
- name: Druma, Profit and Prophecy
  page: 60
  link: https://paizo.com/products/btq01zow
XP: 12800
race: Human
classes:
- failed prophet mesmerist 10
alignment: LE
size: Medium
type: construct
subtypes:
- augmented humanoid
initiative:
  bonus: 8
senses:
  darkvision: 60
  silver scent: true
AC:
  AC: 24
  touch: 14
  flat_footed: 20
  components:
    armor: 5
    dex: 4
    natural: 5
HP:
  HP: 88
  long: 10d8+40
  fast_healing: 10
saves:
  fort: 3
  ref: 11
  will: 13
  other: +4 vs. mind-affecting
defensive_abilities:
- revel in wealth
DR:
- amount: 10
  weakness: bludgeoning and magic
immunities:
- cold
- construct traits (except mind-affecting effects)
- electricity
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +12 (1d6+5 plus greedy grab)
      entries:
      - - damage: 1d6+5
        - effect: greedy grab
      count: 2
      attack: claws
      bonus:
      - 12
  - - text: greedy grab +12 touch
      entries: []
      attack: greedy grab
      bonus:
      - 12
      touch: true
  ranged:
  - - text: earth blast +11 (5d6+10)
      entries:
      - - damage: 5d6+10
      attack: earth blast
      bonus:
      - 11
  - - text: metal blast +11 (10d6+15)
      entries:
      - - damage: 10d6+15
      attack: metal blast
      bonus:
      - 11
  special:
  - aurokinesis (kinetic blast-earth blast [5d6+10], metal blast [10d6+15]; burn [3
    points/round, maximum 8]; infusions-impale, kinetic blade, magnetic infusion,
    rare-metal infusion; kinetic blast; gather power)
  - bold stare (disorientation, timidity)
  - greedy grab (1,000 gp)
  - hypnotic stare (-3)
  - manifold tricks (3)
  - mental potency (+2)
  - mesmerist tricks 10/day (astounding avoidance, compel alacrity, false flanker,
    levitation buffer, mesmeric mirror, spectral smoke)
  - painful stare (+7 or +4d6+7)
space: 5
reach: 10
spells:
  entries:
  - name: enervation
    source: Mesmerist
    level: 4
  - name: hold monster
    source: Mesmerist
    level: 4
    DC: 19
  - name: bestow curse
    source: Mesmerist
    level: 3
    DC: 18
  - name: confusion
    source: Mesmerist
    level: 3
    DC: 18
  - name: dispel magic
    source: Mesmerist
    level: 3
  - name: ray of exhaustion
    source: Mesmerist
    level: 3
    DC: 18
  - name: blindness/deafness
    source: Mesmerist
    level: 2
    DC: 17
  - name: detect thoughts
    source: Mesmerist
    level: 2
    DC: 17
  - name: false life
    source: Mesmerist
    level: 2
  - name: glitterdust
    source: Mesmerist
    level: 2
    DC: 17
  - name: mirror image
    source: Mesmerist
    level: 2
  - name: beguiling gift
    source: Mesmerist
    level: 1
    DC: 16
  - name: comprehend languages
    source: Mesmerist
    level: 1
  - name: ill omen
    source: Mesmerist
    level: 1
  - name: ray of enfeeblement
    source: Mesmerist
    level: 1
    DC: 16
  - name: vanish
    source: Mesmerist
    level: 1
    DC: 16
  - name: detect magic
    source: Mesmerist
    level: 0
  - name: detect psychic significance
    source: Mesmerist
    level: 0
  - name: ghost sound
    source: Mesmerist
    level: 0
    DC: 15
  - name: mage hand
    source: Mesmerist
    level: 0
  - name: open/close
    source: Mesmerist
    level: 0
    DC: 15
  - name: prestidigitation
    source: Mesmerist
    level: 0
  sources:
  - name: Mesmerist
    type: known
    CL: 10
    concentration: 15
    slots:
      4: 2
      3: 4
      2: 5
      1: 7
      0: at-will
ability_scores:
  STR: 20
  DEX: 18
  CON:
  INT: 14
  WIS: 12
  CHA: 20
BAB: 7
CMB: 12
CMB_other: +16 greedy grab
CMD: 26
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Intense Pain
- name: Intimidating Glance
- name: Point-Blank Shot
- name: Toughness
skills:
  Appraise: 19
  Bluff: 23
  Diplomacy: 18
  Intimidate: 18
  Knowledge (arcana): 14
  Knowledge (religion): 14
  Perception: 18
  Sense Motive: 18
  Stealth: 20
  Use Magic Device: 18
  _racial_mods:
    Appraise:
      _: 4
    Knowledge (arcana):
      _: 4
    Knowledge (religion):
      _: 4
    Perception:
      _: 4
    Sense Motive:
      _: 4
    Stealth:
      _: 4
languages:
- Common
- Dwarven
special_qualities:
- consummate liar +5
- personal vault
- plutophage
- touch treatment 8/day (greater)
ecology:
  environment: any underground or urban
  organization: solitary
  treasure_type: double
  treasure:
  - +1 chain shirt
  - headband of alluring charisma +2
  - other treasure
desc_long: |-
  When a Kalistocrat performs the final rites to create her idealized afterlife, the likelihood of success depends on how stringently she adhered to Kalistrade's teachings and how much wealth she sacrificed to serve as an occult anchor for her will. It's not always apparent which prophets succeed, and mere weeks after death, the mindscapes of those prophets who failed begin to collapse. For most, their souls become untethered and join the River of Souls, but others cling tenaciously to their failed dream, and their consciousness escapes into and animates their gold-veined bodies.

   Some of these so-called failed prophets eventually slip out of their shells and accept Pharasma's judgment. Others refuse to accept their own failure and attempt to perform the ritual again after accumulating far more wealth than before. These failed prophets often break out of their mausoleums to hunt down the wealthy and steal their treasure-or worse, dismantle the precious bodies of other Kalistocrats for scrap, sending the mindscapes of their onetime allies hurtling to the Astral Plane to be torn apart by predators or astral weather.

---

# Failed Prophet
A spider-webbing network of fine golden veins covers the body of this skinless, stony-eyed humanoid.
**Source** Druma, Profit and Prophecy pg. 60
**XP** 12,800
Human _[[monsters/Failed Prophet|failed prophet]]_ _[[classes/Mesmerist|mesmerist]]_ 10

LE Medium construct (augmented humanoid)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., silver _[[universal monster rules/Scent|scent]]_; Perception +18

##### Defense

**AC** 24, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+5 armor, +4 Dex, +5 natural)
**hp** 88 (10d8+40); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +3, **Ref** +11, **Will** +13; +4 vs. mind-affecting
**Defensive Abilities** revel in wealth; **DR** 10/bludgeoning and magic; **Immune** cold, _[[universal monster rules/Construct Traits|construct traits]]_ (except mind-affecting effects), electricity

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +12 (1d6+5 plus greedy _[[universal monster rules/Grab|grab]]_) or greedy _grab_ +12 touch
**Ranged** earth blast +11 (5d6+10) or metal blast +11 (10d6+15)
**Space** 5 ft., **Reach** 10 ft.
**Special Attacks** aurokinesis (kinetic blast—earth blast [5d6+10], metal blast [10d6+15]; _[[universal monster rules/Burn|burn]]_ [3 points/round, maximum 8]; infusions—impale, kinetic blade, magnetic infusion, rare-metal infusion; kinetic blast; gather power), bold stare (disorientation, timidity), greedy _grab_ (1,000 gp), hypnotic stare (–3), manifold tricks (3), mental potency (+2), _mesmerist_ tricks 10/day (astounding avoidance, compel alacrity, false flanker, levitation buffer, mesmeric _[[items/Mundane/Mirror|mirror]]_, spectral smoke), painful stare (+7 or +4d6+7)
**_Mesmerist_ Spells Known** (CL 10th; concentration +15)
4th (2/day)—_[[spells/Enervation|enervation]]_, _[[spells/Hold Monster|hold monster]]_ (DC 19) 
3rd (4/day)—_[[spells/Bestow Curse|bestow curse]]_ (DC 18), _[[spells/Confusion|confusion]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 18) 
2nd (5/day)—blindness/deafness (DC 17), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/False Life|false life]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 17), _[[spells/Mirror Image|mirror image]]_ 
1st (7/day)—_[[spells/Beguiling Gift|beguiling gift]]_ (DC 16), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Ill Omen|ill omen]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 16), _[[spells/Vanish|vanish]]_ (DC 16) 
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Detect _[[classes/Psychic|Psychic]]_ Significance|detect _psychic_ significance]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Mage Hand|mage hand]]_, open/close (DC 15), _[[spells/Prestidigitation|prestidigitation]]_

##### Statistics
**Str** 20, **Dex** 18, **Con** —, **Int** 14, **Wis** 12, **Cha** 20
**Base Atk** 7; **CMB** +12 (+16 greedy _grab_); **CMD** 26
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Intense Pain|Intense Pain]]_, _[[feats/Intimidating Glance|Intimidating Glance]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Toughness|Toughness]]_
**Skills** Appraise +19, Bluff +23, Diplomacy +18, Intimidate +18, Knowledge (arcana) +14, Knowledge (religion) +14, Perception +18, Sense Motive +18, Stealth +20, Use Magic Device +18; **Racial Modifiers** +4 Appraise, +4 Knowledge (arcana), +4 Knowledge (religion), +4 Perception, +4 Sense Motive, +4 Stealth
**Languages** Common, Dwarven
**SQ** consummate liar +5, personal vault, plutophage, touch treatment 8/day (greater)

##### Ecology

**Environment** any underground or urban
**Organization** solitary
**Treasure** double (+1 _[[items/Armor/Chain shirt|chain shirt]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, other treasure)

##### Description

When a Kalistocrat performs the final rites to create her idealized afterlife, the likelihood of success depends on how stringently she adhered to Kalistrade’s teachings and how much wealth she sacrificed to serve as an occult anchor for her will. It’s not always apparent which prophets succeed, and mere weeks after death, the mindscapes of those prophets who failed begin to collapse. For most, their souls become untethered and join the River of Souls, but others cling tenaciously to their failed _[[spells/Dream|dream]]_, and their consciousness escapes into and animates their gold-veined bodies.

Some of these so-called failed prophets eventually slip out of their shells and accept Pharasma’s judgment. Others refuse to accept their own failure and attempt to perform the ritual again after accumulating far more wealth than before. These failed prophets often break out of their mausoleums to hunt down the wealthy and steal their treasure—or worse, dismantle the precious bodies of other Kalistocrats for scrap, _[[spells/Sending|sending]]_ the mindscapes of their onetime allies hurtling to the Astral Plane to be torn apart by predators or astral weather.