---
cssclass: [monsters]
title1: Galundari, the Scourge of Heaven
desc_short: This towering, burning demon wears black, spiky armor and carries two
  weapons-a jagged sword and a whip of flames.
title2: Galundari, the Scourge of Heaven
CR: 25
sources:
- name: Demons Revisited
  page: 14
  link: http://paizo.com/products/btpy8yvo?Pathfinder-Campaign-Setting-Demons-Revisited
XP: 1638400
race: Male
classes:
- balor lord fighter 5 (Pathfinder RPG Bestiary 59)
alignment: CE
size: Large
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 6
senses:
  darkvision: 60
  true seeing: true
auras:
- name: flaming body
- name: unholy aura
  DC: 27
AC:
  AC: 44
  touch: 17
  flat_footed: 40
  components:
    armor: 11
    deflection: 4
    dex: 4
    natural: 16
    size: -1
HP:
  HP: 542
  long: 25d10+405
  HD: 25
saves:
  fort: 35
  ref: 19
  will: 24
  will_other: +1 vs. fear
defensive_abilities:
- bravery +1
DR:
- amount: 15
  weakness: epic, cold iron, and good
immunities:
- electricity
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 31
speeds:
  base: 40
  fly: 90
  fly_maneuverability: good
attacks:
  melee:
  - - text: +5 vorpal good outsider-bane flaming burst unholy longsword +44/+39/+34/+29
        (2d6+23/19-20 plus 1d6 fire)
      entries:
      - - damage: 2d6+23
          crit_range: 19-20
        - damage: 1d6
          type: fire
      attack: +5 vorpal good outsider-bane flaming burst unholy longsword
      bonus:
      - 44
      - 39
      - 34
      - 29
    - text: +5 vorpal good outsider-bane flaming burst unholy whip +42/+37/+32 (1d4+12
        plus 1d6 fire and entangle)
      entries:
      - - damage: 1d4+12
        - damage: 1d6
          type: fire
        - effect: entangle
      attack: +5 vorpal good outsider-bane flaming burst unholy whip
      bonus:
      - 42
      - 37
      - 32
  ranged:
  - - text: +5 unholy good outsider-bane flaming burst composite longbow +35/+30/+25/+20
        (2d6+20/×3)
      entries:
      - - damage: 2d6+20
          crit_multiplier: 3
      attack: +5 unholy good outsider-bane flaming burst composite longbow
      bonus:
      - 35
      - 30
      - 25
      - 20
  special:
  - Abyssal rift
  - angelslayer
  - weapon training (heavy blades +1)
space: 10
reach: 10
reach_other: 20 ft. with whip
spell_like_abilities:
  entries:
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 27
  - name: dominate monster
    source: default
    freq: At will
    DC: 28
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: power word stun
    source: default
    freq: At will
  - name: telekinesis
    source: default
    freq: At will
    DC: 24
  - name: quickened telekinesis
    source: default
    freq: 3/day
    DC: 24
  - name: blasphemy
    source: default
    freq: 1/day
    DC: 26
  - name: fire storm
    source: default
    freq: 1/day
    DC: 27
  - name: implosion
    source: default
    freq: 1/day
    DC: 28
  - name: summon
    source: default
    freq: 1/day
    level: 9
    summons:
    - name: any one CR 19
    - name: lower demon
      chance: 100%
  sources:
  - name: default
    CL: 20
    concentration: 29
ability_scores:
  STR: 40
  DEX: 23
  CON: 40
  INT: 26
  WIS: 24
  CHA: 29
BAB: 25
CMB: 41
CMD: 61
feats:
- name: Craft Magic Arms and Armor
- name: Craft Wondrous Item
- name: Critical Focus
- name: Greater Two-Weapon Fighting
- name: Improved Two- Weapon Fighting
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Master Craftsman
- name: Power Attack
- name: Quicken Spell-Like Ability (telekinesis)
- name: Staggering Critical
- name: Toughness
- name: Two-Weapon Fighting
- name: Vital Strike
- name: Weapon Focus (longsword)
- name: Weapon Specialization (longsword)
skills:
  Acrobatics: 32
    when jumping: 36
  Bluff: 37
  Craft (weaponsmith): 38
  Diplomacy: 37
  Fly: 34
  Intimidate: 37
  Knowledge (history): 28
  Knowledge (nobility): 28
  Knowledge (planes): 31
  Knowledge (religion): 31
  Perception: 43
  Sense Motive: 35
  Stealth: 28
  Use Magic Device: 37
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
special_qualities:
- armor training 1
- death throes
- vorpal strike
- whip mastery
gear:
  gear:
  - +5 adamantine spiked heavy fortification breastplate
  - +3 good outsider-bane flaming burst unholy longsword
  - +4 good outsider-bane flaming burst unholy whip
  - +5 good outsider-bane flaming burst unholy composite longbow (20 greater good
    outsider slaying arrows, 10 greater human slaying arrows, and 30 cold iron arrows)
  - efficient quiver
  - ring of freedom of movement
  - ring of spell turning
special_abilities:
  Abyssal Rift (Su): The first time Galundari slays a creature in a round (but no
    more than once per round), a rift tears open between the plane he currently occupies
    and the Abyss. The slain creature must immediately make a DC 29 Will save or his
    body and gear are drawn through the rift, transported to Galundari's trophy room
    in his palace on the Abyss. Regardless of whether the creature's body is drawn
    through the rift, the rift immediately slams shut a moment after it forms, creating
    a 20-foot-radius burst of chaotic energy that staggers all non-demons in the area
    of effect for 1d10 rounds-a DC 29 Fortitude save reduces the staggering effect
    to 1 round. If Galundari slays multiple creatures simultaneously, the body targeted
    by the rift is determined randomly. If the body targeted by the rift was a good
    outsider, all creatures (including the dead creature in danger of being pulled
    through the rift) take a -2 penalty on all saving throws against that specific
    Abyssal rift. This is a teleportation effect. The save DC is Charisma-based.
desc_long: |-
  Few balor lords have achieved the notoriety and power of Galundari, even though it has been centuries since the balor lord was lost to the Nemesis Well and longer still since he was imprisoned in the artifact that now bears his name. Indeed, it was this notoriety that compelled Nex to seek the balor's aid, over 56 centuries ago, in the creation of the Lens of Galundari (Pathfinder Campaign Setting: Artifacts & Legends 30)-a magical lens akin to others that powered the wizard's demon ships, but that would be much more potent than its lesser copies. Nex lured Galundari into the lens with lies and false promises, and the balor has remained trapped within the lens ever since.

  When Pathfinder Durvin Gest threw the Lens of Galundari into the Nemesis Well in 4332 ar, many believed that the time of the mighty balor lord had passed forever. Yet Galundari still lives, and even now the last few of his still-loyal minions toil in far corners of the Great Beyond and elsewhere in the universe, seeking the location of the far side of the Nemesis Well so that their master may be released. In his time, Galundari was even more powerful than the creature presented above, but over the centuries of imprisonment within the lens, he has lost all of his mythic power. What remains is still a formidable foe, and the Scourge of Heaven is one of the few of his kind to possess multiple unique balor lord powers. Galundari earned his appellation for his countless successful raids against the fortresses of Heaven itself. Some demonologists maintain that Nex was only able to deceive Galundari with the hidden aid of a vengeful solar, and that in trapping the Scourge of Heaven he pried strange and impossible favors from Heaven itself.

  Galundari requires the sacrifice of nothing less than a planetar (minimum CR of 18) when conjured-the murder of the planetar must be performed by the conjurer in Galundari's presence, and the angel must be conscious when the murder is performed. It's a DC 35 check to research Galundari, but as long as he remains imprisoned in the Lens of Galundari (itself still lost in the Nemesis Well), he cannot be conjured at all. Assuming the balor lord can be freed, his skill at creating magical armor, weapons, and wondrous items is as significant as his skill in combat.

---

# Galundari, the Scourge of Heaven
This towering, _[[items/Weapon Magic Abilities/Burning|burning]]_ demon wears black, spiky armor and carries two weapons—a jagged sword and a _[[items/Weapon/Whip|whip]]_ of flames.
**Source** Demons Revisited pg. 14
**XP** 1,638,400
Male balor lord _[[classes/Fighter|fighter]]_ 5 (Pathfinder RPG Bestiary 59)
CE Large outsider (chaotic, demon, evil, extraplanar)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +43
**Aura** _[[items/Weapon Magic Abilities/Flaming|flaming]]_ body, _[[spells/Unholy Aura|unholy aura]]_ (DC 27)

##### Defense

**AC** 44, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 40 (+11 armor, +4 deflection, +4 Dex, +16 natural, –1 size)
**hp** 542 (25 HD; 25d10+405)
**Fort** +35, **Ref** +19, **Will** +24 (+1 vs. _[[universal monster rules/Fear|fear]]_)
**Defensive Abilities** bravery +1; **DR** 15/epic, cold iron, and good; **Immune** electricity, fire, poison; **Resist** acid 10, cold 10; **SR** 31

##### Offense
**Speed** 40 ft., fly 90 ft. (good)
**Melee** +5 _[[items/Weapon Magic Abilities/Vorpal|vorpal]]_ good outsider-bane _[[items/Weapon Magic Abilities/Flaming Burst|flaming burst]]_ _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Longsword|longsword]]_ +44/+39/+34/+29 (2d6+23/19–20 plus 1d6 fire), +5 _vorpal_ good outsider-bane _flaming burst_ _unholy_ _whip_ +42/+37/+32 (1d4+12 plus 1d6 fire and _[[spells/Entangle|entangle]]_)
**Ranged** +5 _unholy_ good outsider-bane _flaming burst_ _[[items/Weapon/Composite longbow|composite longbow]]_ +35/+30/+25/+20 (2d6+20/×3)
**Space** 10 ft., **Reach** 10 ft. (20 ft. with _whip_)
**Special Attacks** Abyssal rift, angelslayer, weapon _[[items/Weapon Magic Abilities/Training|training]]_ (heavy blades +1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +29)
Constant—_true seeing_, _unholy aura_ (DC 27)
At will—_[[spells/Dominate Monster|dominate monster]]_ (DC 28), greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (self plus 50 lbs. of objects only), _[[spells/Power Word Stun|power word stun]]_, _[[spells/Telekinesis|telekinesis]]_ (DC 24)
3/day—quickened _telekinesis_ (DC 24)
1/day—_[[spells/Blasphemy|blasphemy]]_ (DC 26), _[[spells/Fire Storm|fire storm]]_ (DC 27), _[[spells/Implosion|implosion]]_ (DC 28), _[[universal monster rules/Summon|summon]]_ (level 9, any one CR 19 or lower demon 100%)

##### Statistics
**Str** 40, **Dex** 23, **Con** 40, **Int** 26, **Wis** 24, **Cha** 29
**Base Atk** +25; **CMB** +41; **CMD** 61
**Feats** _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Greater Two-Weapon Fighting|Greater Two-Weapon Fighting]]_, Improved Two- Weapon Fighting, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Master Craftsman|Master Craftsman]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (_telekinesis_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_longsword_), _[[feats/Weapon Specialization|Weapon Specialization]]_ (_longsword_)
**Skills** Acrobatics +32 (+36 when jumping), Bluff +37, Craft (weaponsmith) +38, Diplomacy +37, Fly +34, Intimidate +37, Knowledge (history) +28, Knowledge (nobility) +28, Knowledge (planes) +31, Knowledge (religion) +31, Perception +43, Sense Motive +35, Stealth +28, Use Magic Device +37
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** armor _training_ 1, death throes, _vorpal_ strike, _[[feats/Whip Mastery|whip mastery]]_
**Gear** +5 adamantine spiked heavy _[[universal monster rules/Fortification|fortification]]_ _[[items/Armor/Breastplate|breastplate]]_, +3 good outsider-bane _flaming burst_ _unholy_ _longsword_, +4 good outsider-bane _flaming burst_ _unholy_ _whip_, +5 good outsider-bane _flaming burst_ _unholy_ _composite longbow_ (20 greater good outsider slaying arrows, 10 greater human slaying arrows, and 30 cold iron arrows), _[[items/Wondrous Item/Efficient Quiver|efficient quiver]]_, _[[items/Ring/Ring of _[[spells/Freedom|Freedom]]_ of Movement|ring of _freedom_ of movement]]_, _[[items/Ring/Ring of Spell Turning|ring of spell turning]]_

### Special Abilities

**Abyssal Rift (Su)** The first time Galundari slays a creature in a round (but no more than once per round), a rift tears open between the plane he currently occupies and the Abyss. The slain creature must immediately make a DC 29 Will save or his body and gear are drawn through the rift, transported to Galundari’s trophy room in his palace on the Abyss. Regardless of whether the creature’s body is drawn through the rift, the rift immediately slams shut a moment after it forms, creating a 20-foot-radius burst of chaotic energy that staggers all non-demons in the area of effect for 1d10 rounds—a DC 29 Fortitude save reduces the staggering effect to 1 round. If Galundari slays multiple creatures simultaneously, the body targeted by the rift is determined randomly. If the body targeted by the rift was a good outsider, all creatures (including the dead creature in danger of being pulled through the rift) take a –2 penalty on all saving throws against that specific Abyssal rift. This is a teleportation effect. The save DC is Charisma-based.

##### Description

Few balor lords have achieved the notoriety and power of Galundari, even though it has been centuries since the balor lord was lost to the _[[feats/Nemesis|Nemesis]]_ Well and longer still since he was imprisoned in the artifact that now bears his name. Indeed, it was this notoriety that compelled Nex to seek the balor’s aid, over 56 centuries ago, in the creation of the _[[items/Wondrous Item/Lens of Galundari|Lens of Galundari]]_ (Pathfinder Campaign Setting: Artifacts &_[[items/Mundane/Amp|amp]]_; Legends 30)—a magical lens akin to others that powered the _[[classes/Wizard|wizard]]_’s demon ships, but that would be much more _[[items/Weapon Magic Abilities/Potent|potent]]_ than its lesser copies. Nex lured Galundari into the lens with lies and false promises, and the balor has remained trapped within the lens ever since.

When Pathfinder Durvin Gest threw the _Lens of Galundari_ into the _Nemesis_ Well in 4332 ar, many believed that the time of the mighty balor lord had passed forever. Yet Galundari still lives, and even now the last few of his still-loyal minions toil in far corners of the Great Beyond and elsewhere in the universe, seeking the location of the far side of the _Nemesis_ Well so that their master may be released. In his time, Galundari was even more powerful than the creature presented above, but over the centuries of _[[spells/Imprisonment|imprisonment]]_ within the lens, he has lost all of his mythic power. What remains is still a formidable foe, and the Scourge of Heaven is one of the few of his kind to possess multiple unique balor lord powers. Galundari earned his appellation for his countless successful raids against the fortresses of Heaven itself. Some demonologists maintain that Nex was only able to deceive Galundari with the hidden aid of a vengeful solar, and that in trapping the Scourge of Heaven he pried strange and impossible favors from Heaven itself.

Galundari requires the _[[spells/Sacrifice|sacrifice]]_ of nothing less than a planetar (minimum CR of 18) when conjured—the murder of the planetar must be performed by the conjurer in Galundari’s presence, and the angel must be conscious when the murder is performed. It’s a DC 35 check to research Galundari, but as long as he remains imprisoned in the _Lens of Galundari_ (itself still lost in the _Nemesis_ Well), he cannot be conjured at all. Assuming the balor lord can be freed, his skill at creating magical armor, weapons, and wondrous items is as significant as his skill in combat.