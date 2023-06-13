---
cssclass: [monsters]
title1: Shaorhaz, Glutton of the Green
desc_short: This four-armed nightmare stands with an elegance that seems out of place,
  given its demonic visage. Huge black wings fan behind its back, and flickering black
  blades burn in its hands.
title2: Shaorhaz, Glutton of the Green
CR: 23
sources:
- name: Demons Revisited
  page: 44
  link: http://paizo.com/products/btpy8yvo?Pathfinder-Campaign-Setting-Demons-Revisited
XP: 819200
race: Male
classes:
- vrolikai inquisitor of Cyth-V'sug 9 (Pathfinder RPG Bestiary 2 81)
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 21
senses:
  darkvision: 120
  low-light vision: true
  true seeing: true
AC:
  AC: 42
  touch: 13
  flat_footed: 38
  components:
    armor: 10
    dex: 3
    dodge: 1
    natural: 19
    size: -1
HP:
  HP: 489
  long: 19d10+9d8+345
  HD: 28
saves:
  fort: 24
  ref: 22
  will: 26
defensive_abilities:
- freedom of movement
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- death effects
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 30
speeds:
  base: 30
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: +1 black flame knife +39/+34/+29/+24 (1d6+15/17-20 plus energy drain)
      entries:
      - - damage: 1d6+15
          crit_range: 17-20
        - effect: energy drain
      attack: +1 black flame knife
      bonus:
      - 39
      - 34
      - 29
      - 24
    - text: 3 +1 black flame knives +39 (1d6+8 plus energy drain)
      entries:
      - - damage: 1d6+8
        - effect: energy drain
      count: 3
      attack: +1 black flame knives
      bonus:
      - 39
    - text: bite +36 (1d8+7)
      entries:
      - - damage: 1d8+7
      attack: bite
      bonus:
      - 36
    - text: sting +36 (1d6+7 plus madness)
      entries:
      - - damage: 1d6+7
        - effect: madness
      attack: sting
      bonus:
      - 36
  special:
  - bane (9 rounds/day)
  - black flame knives
  - death-stealing gaze (DC 28)
  - madness (DC 28)
  - multiweapon mastery
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: deeper darkness
    source: default
    freq: At will
  - name: enervation
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: telekinesis
    source: default
    freq: At will
    DC: 24
  - name: quickened enervation
    source: default
    freq: 3/day
  - name: regenerate
    source: default
    freq: 3/day
  - name: silence
    source: default
    freq: 3/day
    DC: 21
  - name: vampiric touch
    source: default
    freq: 3/day
  - name: mass hold monster
    source: default
    freq: 1/day
    DC: 28
  - name: summon
    source: default
    freq: 1/day
    level: 6
    summons:
    - name: marilith
      amount: 1
      chance: 50%
    - name: glabrezus
      amount: 1d4
      chance: 75%
  - name: symbol of death
    source: default
    freq: 1/day
    DC: 27
  - name: detect alignment
    source: inquisitor
    freq: At will
  - name: discern lies
    source: inquisitor
    freq: 9 rounds/day
  sources:
  - name: default
    CL: 19
    concentration: 28
  - name: inquisitor
    CL: 9
    concentration: 18
spells:
  entries:
  - name: cure serious wounds
    source: Inquisitor
    level: 3
  - name: dimensional anchor
    source: Inquisitor
    level: 3
  - name: seek thoughts
    source: Inquisitor
    level: 3
    DC: 22
  - name: speak with dead
    source: Inquisitor
    level: 3
    DC: 22
  - name: barkskin
    source: Inquisitor
    level: 2
  - name: death knell
    source: Inquisitor
    level: 2
    DC: 21
  - name: detect thoughts
    source: Inquisitor
    level: 2
    DC: 21
  - name: spiritual weapon
    source: Inquisitor
    level: 2
  - name: command
    source: Inquisitor
    level: 1
    DC: 20
  - name: cure light wounds
    source: Inquisitor
    level: 1
  - name: divine favor
    source: Inquisitor
    level: 1
  - name: protection from good
    source: Inquisitor
    level: 1
  - name: shield of faith
    source: Inquisitor
    level: 1
  - name: acid splash
    source: Inquisitor
    level: 0
  - name: brand
    source: Inquisitor
    level: 0
    DC: 19
  - name: bleed
    source: Inquisitor
    level: 0
    DC: 19
  - name: detect magic
    source: Inquisitor
    level: 0
  - name: disrupt undead
    source: Inquisitor
    level: 0
  - name: read magic
    source: Inquisitor
    level: 0
  sources:
  - name: Inquisitor
    type: known
    CL: 9
    concentration: 18
    slots:
      3: 5
      2: 6
      1: 8
      0: at-will
    domains:
    - decay
ability_scores:
  STR: 38
  DEX: 27
  CON: 34
  INT: 22
  WIS: 28
  CHA: 28
BAB: 25
CMB: 40
CMD: 59
feats:
- name: Combat Expertise
- name: Critical Focus
- name: Dodge
- name: Flyby Attack
- name: Greater Vital Strike
- name: Improved Critical (black flame knife)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Mobility
- name: Multiattack
- name: Outflank
- name: Power Attack
- name: Precise Strike
- name: Quicken Spell-Like Ability (enervation)
- name: Staggering Critical
- name: Swap Places
- name: Vital Strike
skills:
  Acrobatics: 36
  Fly: 42
  Intimidate: 44
  Knowledge (dungeoneering): 37
  Knowledge (nature): 37
  Knowledge (planes): 37
  Knowledge (religion): 37
  Linguistics: 10
  Perception: 44
  Sense Motive: 44
  Spellcraft: 37
  Stealth: 37
    in shadowy areas: 45
  Use Magic Device: 37
  _racial_mods:
    Perception:
      _: 8
    Stealth:
      in shadowy areas: 8
languages:
- Abyssal
- Aklo
- Celestial
- Draconic
- Druidic
- Sylvan
- telepathy 100 ft.
special_qualities:
- cunning initiative
- judgment (2, 3/day)
- monster lore +9
- solo tactics
- stern gaze
- track +4
gear:
  gear:
  - +4 ghost touch shadow undead-controlling breastplate
  - belt of giant strength +6
  - ring of earth elemental command
  - ring of freedom of movement
desc_long: |-
  Even before he was recruited by Deskari to raze the Green Faith from Sarkoris, the vrolikai Shaorhaz had a long tradition of antipathy toward the druidic faith. When Shaorhaz first came to the Material Plane to grow, he had the misfortune of appearing in the small village of Rookhill in southeastern Ustalav. At first, Shaorhaz met little opposition from the villagers, and he fed with impunity. But then a cabal of druids came to Rookhill's aid, and Shaorhaz found his hunting grounds increasingly well guarded and dangerous. Stubborn to a fault, the nabasu refused to move on to easier hunting grounds elsewhere, and time and time again, he clashed with the druids. With each attempt to kill them, though, the druids grew more and more adept at fighting the nabasu, and with each dawn, it seemed that the very wilderness in which he had enjoyed hiding for so many months was turning against him. When the nabasu was nearly slain by the druids' treant ally, he made a desperate attempt to assassinate their leader. This foolish assault earned the nabasu nothing more than the loss of his accumulated growth, as the druid sacrificed his life to return the spiritual energies the demon had fed upon to the land. Only then did Shaorhaz flee Ustalav, teleporting to another wilderness to start over. It took the demon 10 times as long as he'd hoped to finally achieve apotheosis and transform to a vrolikai, and in that time, his hatred of the druidic faith only grew.

  Today, Shaorhaz rules over the ruins of the Forest of Stones in what was once northern Sarkoris. This region, known today as the Stonewilds, was once sacred to the Green Faith, but now the only druids who remain are the warped and twisted undead abominations known as siabraes, for when it became clear that Shaorhaz had won the battle, the last few druids turned again to sacrifice to defeat the demon. Yet this time, the tactic did not work. This time, Shaorhaz was prepared, and the vile energies he commanded ref lected back upon the druids, turning them into the very things they detested most. Since then, Shaorhaz has spent the majority of his time within his palace, Greengrave, searching for a way to feed not on more mortal souls but upon the very soul of Golarion itself.

  Shaorhaz prefers offerings of druids, especially those of the Green Faith. He often promises to let these offerings live if they can reveal to him something of the druidic faith that he has not already confirmed for himself-those druids foolish enough to take the demon at his word get the deaths they deserve. It's a DC 33 check to research the Glutton of the Green.

---

# Shaorhaz, Glutton of the Green
This four-armed _[[spells/Nightmare|nightmare]]_ stands with an elegance that seems out of place, given its demonic visage. Huge black wings fan behind its back, and flickering black blades _[[universal monster rules/Burn|burn]]_ in its hands.
**Source** Demons Revisited pg. 44
**XP** 819,200
Male vrolikai _[[classes/Inquisitor|inquisitor]]_ of Cyth-V’sug 9 (Pathfinder RPG Bestiary 2 81)
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +21; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/True Seeing|true seeing]]_; Perception +44

##### Defense

**AC** 42, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 38 (+10 armor, +3 Dex, +1 dodge, +19 natural, –1 size)
**hp** 489 (28 HD; 19d10+9d8+345)
**Fort** +24, **Ref** +22, **Will** +26
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 15/cold iron and good; **Immune** death effects, electricity, poison; **Resist** acid 10, cold 10, fire 10; **SR** 30

##### Offense
**Speed** 30 ft., fly 60 ft. (perfect)
**Melee** +1 black flame knife +39/+34/+29/+24 (1d6+15/17–20 plus _[[universal monster rules/Energy Drain|energy drain]]_), 3 +1 black flame knives +39 (1d6+8 plus _energy drain_), bite +36 (1d8+7), sting +36 (1d6+7 plus madness)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[spells/Bane|bane]]_ (9 rounds/day), black flame knives, death-stealing _[[universal monster rules/Gaze|gaze]]_ (DC 28), madness (DC 28), _[[universal monster rules/Multiweapon Mastery|multiweapon mastery]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 19th; concentration +28)
Constant—_true seeing_
At will—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Enervation|enervation]]_, greater teleport (self plus 50 lbs. of objects only), _[[spells/Telekinesis|telekinesis]]_ (DC 24)
3/day—quickened _enervation_, _[[spells/Regenerate|regenerate]]_, _[[spells/Silence|silence]]_ (DC 21), _[[spells/Vampiric Touch|vampiric touch]]_
1/day—mass _[[spells/Hold Monster|hold monster]]_ (DC 28), _[[universal monster rules/Summon|summon]]_ (level 6, 1 marilith 50% or 1d4 glabrezus 75%), _[[spells/Symbol of Death|symbol of death]]_ (DC 27)
**_Inquisitor_ _Spell-Like Abilities_ **(CL 9th; concentration +18)
At will—detect alignment
9 rounds/day—_[[spells/Discern Lies|discern lies]]_
**_Inquisitor_ Spells Known **(CL 9th; concentration +18)
3rd (5/day)—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Seek Thoughts|seek thoughts]]_ (DC 22), _[[spells/Speak with Dead|speak with dead]]_ (DC 22)
2nd (6/day)—_[[spells/Barkskin|barkskin]]_, _[[spells/Death Knell|death knell]]_ (DC 21), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 21), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st (8/day)—_[[spells/Command|command]]_ (DC 20), _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Protection From Good|protection from good]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Brand|brand]]_ (DC 19), _[[universal monster rules/Bleed|bleed]]_ (DC 19), _[[spells/Detect Magic|detect magic]]_, _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Read Magic|read magic]]_
**Domain **Decay

##### Statistics
**Str** 38, **Dex** 27, **Con** 34, **Int** 22, **Wis** 28, **Cha** 28
**Base Atk** +25; **CMB** +40; **CMD** 59
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Critical Focus|Critical Focus]]_, _Dodge_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Critical|Improved Critical]]_ (black flame knife), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Outflank|Outflank]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Precise Strike|Precise Strike]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_enervation_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Swap Places|Swap Places]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +36, Fly +42, Intimidate +44, Knowledge (dungeoneering) +37, Knowledge (nature) +37, Knowledge (planes) +37, Knowledge (religion) +37, Linguistics +10, Perception +44, Sense Motive +44, Spellcraft +37, Stealth +37 (+45 in shadowy areas), Use Magic Device +37; **Racial Modifiers** +8 Perception, +8 Stealth in shadowy areas
**Languages** Abyssal, Aklo, Celestial, Draconic, Druidic, Sylvan; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[items/Weapon Magic Abilities/Cunning|cunning]]_ initiative, judgment (2, 3/day), monster lore +9, solo tactics, stern _gaze_, track +4
**Gear** +4 _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ _[[items/Armor Magic Abilities/Shadow|shadow]]_ undead-controlling _[[items/Armor/Breastplate|breastplate]]_, _[[items/Wondrous Item/Belt of Giant Strength +6|belt of giant strength +6]]_, ring of earth elemental _command_, _[[items/Ring/Ring of _[[spells/Freedom|Freedom]]_ of Movement|ring of _freedom_ of movement]]_

##### Description

Even before he was recruited by Deskari to raze the Green Faith from Sarkoris, the vrolikai Shaorhaz had a long tradition of _[[spells/Antipathy|antipathy]]_ toward the druidic faith. When Shaorhaz first came to the Material Plane to grow, he had the misfortune of appearing in the small village of Rookhill in southeastern Ustalav. At first, Shaorhaz met little opposition from the villagers, and he fed with impunity. But then a cabal of druids came to Rookhill’s aid, and Shaorhaz found his hunting grounds increasingly well guarded and dangerous. Stubborn to a fault, the nabasu refused to move on to easier hunting grounds elsewhere, and time and time again, he clashed with the druids. With each attempt to kill them, though, the druids grew more and more adept at fighting the nabasu, and with each dawn, it seemed that the very wilderness in which he had enjoyed hiding for so many months was turning against him. When the nabasu was nearly slain by the druids’ _[[monsters/Treant|treant]]_ ally, he made a desperate attempt to assassinate their leader. This foolish assault earned the nabasu nothing more than the loss of his accumulated growth, as the _[[classes/Druid|druid]]_ sacrificed his life to return the spiritual energies the demon had fed upon to the land. Only then did Shaorhaz flee Ustalav, teleporting to another wilderness to start over. It took the demon 10 times as long as he’d hoped to finally achieve _[[feats/Apotheosis|apotheosis]]_ and transform to a vrolikai, and in that time, his hatred of the druidic faith only grew.

Today, Shaorhaz rules over the ruins of the Forest of Stones in what was once northern Sarkoris. This region, known today as the Stonewilds, was once _[[items/Weapon Magic Abilities/Sacred|sacred]]_ to the Green Faith, but now the only druids who remain are the warped and twisted undead abominations known as siabraes, for when it became clear that Shaorhaz had won the battle, the last few druids turned again to _[[spells/Sacrifice|sacrifice]]_ to defeat the demon. Yet this time, the tactic did not work. This time, Shaorhaz was prepared, and the vile energies he commanded ref lected back upon the druids, turning them into the very things they detested most. Since then, Shaorhaz has spent the majority of his time within his palace, Greengrave, searching for a way to feed not on more mortal souls but upon the very soul of Golarion itself.

Shaorhaz prefers offerings of druids, especially those of the Green Faith. He often promises to let these offerings live if they can reveal to him something of the druidic faith that he has not already confirmed for himself—those druids foolish enough to take the demon at his word get the deaths they deserve. It’s a DC 33 check to research the Glutton of the Green.