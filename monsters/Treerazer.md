---
cssclass: [monsters]
title1: Treerazer
desc_short: The twenty-foot-tall winged saurian demon wields an acid-dripping axe.
  Two red eyes glow above a tooth-filled beak.
title2: Treerazer
CR: 25
sources:
- name: Inner Sea World Guide
  page: 314
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderChronicles/v5748btpy8ief
- name: 'Pathfinder #17: A Memory of Darkness'
  page: 88
  link: http://paizo.com/pathfinder/adventurePath/secondDarkness/v5748btpy86j6
XP: 1638400
alignment: CE
size: Huge
type: outsider
subtypes:
- demon
- native
initiative:
  bonus: 14
senses:
  darkvision: 60
  detect good: true
  detect law: true
  true seeing: true
auras:
- name: corruption
  radius: 120
- name: unholy aura
  DC: 25
AC:
  AC: 42
  touch: 22
  flat_footed: 32
  components:
    deflection: 4
    dex: 10
    natural: 20
    size: -2
HP:
  HP: 574
  long: 28d10+420
  regeneration: 15
  regeneration_weakness: good
saves:
  fort: 34
  ref: 23
  will: 27
defensive_abilities:
- freedom of movement
DR:
- amount: 15
  weakness: cold iron and good
immunities:
- death effects
- disease
- electricity
- mind-affecting effects
- poison
resistances:
  acid: 30
  cold: 30
  fire: 30
SR: 36
speeds:
  base: 60
  fly: 60
  fly_maneuverability: good
  swim: 40
attacks:
  melee:
  - - text: Blackaxe +44/+39/+34/+29 (4d6+24/19-20/x3 plus 1d6 acid)
      entries:
      - - damage: 4d6+24
          crit_range: 19-20
          crit_multiplier: 3
        - damage: 1d6
          type: acid
      attack: Blackaxe
      bonus:
      - 44
      - 39
      - 34
      - 29
    - text: bite +37 (2d6+6)
      entries:
      - - damage: 2d6+6
      attack: bite
      bonus:
      - 37
    - text: 2 wings +37 (1d8+6)
      entries:
      - - damage: 1d8+6
      count: 2
      attack: wings
      bonus:
      - 37
  special:
  - defoliation
space: 20
reach: 20
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect law
    source: default
    freq: Constant
  - name: freedom of movement
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
  - name: water breathing
    source: default
    freq: Constant
  - name: antiplant shell
    source: default
    freq: At will
  - name: contagion
    source: default
    freq: At will
    DC: 21
  - name: desecrate
    source: default
    freq: At will
  - name: greater dispel magic
    source: default
    freq: At will
  - name: greater teleport
    source: default
    freq: At will
    other: within Tanglebriar only
  - name: telekinesis
    source: default
    freq: At will
    DC: 22
  - name: unholy blight
    source: default
    freq: At will
    DC: 21
  - name: control plants
    source: default
    freq: 3/day
    DC: 25
  - name: quickened greater dispel magic
    source: default
    freq: 3/day
  - name: wall of thorns
    source: default
    freq: 3/day
  - name: horrid wilting
    source: default
    freq: 1/day
    DC: 25
  - name: summon demons
    source: default
    freq: 1/day
  - name: symbol of death
    source: default
    freq: 1/day
    DC: 25
  - name: time stop
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 27
ability_scores:
  STR: 36
  DEX: 30
  CON: 40
  INT: 21
  WIS: 24
  CHA: 25
BAB: 28
CMB: 43
CMD: 67
feats:
- name: Awesome Blow
- name: Combat Reflexes
- name: Critical Focus
- name: Flyby Attack
- name: Greater Vital Strike
- name: Improved Bull Rush
- name: Improved Critical (greataxe)
- name: Improved Initiative
- name: Improved Vital Strike
- name: Multiattack
- name: Power Attack
- name: Quicken Spell-Like Ability (greater dispel magic)
- name: Staggering Critical
- name: Vital Strike
skills:
  Acrobatics: 41
  Fly: 38
  Intimidate: 38
  Knowledge (arcana): 36
  Knowledge (nature): 36
  Knowledge (planes): 36
  Perception: 38
  Sense Motive: 38
  Spellcraft: 33
  Stealth: 33
  Swim: 49
languages:
- Abyssal
- Common
- Elven
- Sylvan
- telepathy 300 ft.
special_qualities:
- nascent demon lord traits
gear:
  gear:
  - Blackaxe (see page 299)
ecology:
  environment: Tanglebriar
  organization: solitary or group (Treerazor plus 1d4 nalfeshnees and 2d4 hezrous)
  treasure_type: triple
  treasure:
  - plus Blackaxe
special_abilities:
  Aura of Corruption (Su): Treerazer exudes an aura of corruption to a radius of 120
    feet. This aura causes plants to grow hideous, sprouting thorns, twisting, and
    becoming fungoid in nature. Creatures with woodland stride or freedom of movement
    can move through this fungal bloom with ease. Living creatures within Treerazer's
    aura of corruption must make a DC 39 Fortitude save each round or their flesh
    grows pasty and clammy as tendrils of diseased plant matter and fungal growth
    sprout from it. This condition persists as long as the creature remains within
    Treerazer's aura of corruption and for 1 minute thereafter. While suffering the
    effects of this aura, the living creature is treated as a plant for the purposes
    of spells and effects that harm or otherwise inconvenience plant creatures more
    than other creatures. The victim would thus be subject to antiplant shell, blight,
    and additional damage from horrid wilting or a plant bane weapon, and could be
    affected by control plants. The corruption does not otherwise impart plant traits
    to creatures. The save DC is Constitution-based.
  Defoliation (Su): As a standard action once every 1d4 rounds, Treerazer can exude
    a pulse of defoliating energy in a 30-foot-radius spread. This pulse appears as
    a wave of sickly green energy, and causes all plants and plant creatures in the
    area to blacken and wither. Such creatures take 20d10 points of damage and 1d8
    points of Strength drain, or half with a successful DC 39 Fortitude save. A plant
    that isn't a creature (such as a tree or a shrub) doesn't receive a save and immediately
    withers and dies. Treerazer can choose to exclude any number of plants in the
    area from this effect, and generally does so to preserve twisted and corrupted
    plants and fungus. The save DC is Constitution-based.
  Nascent Demon Lord Traits: A nascent demon lord is a powerful demon that has not
    yet made the full transition from unique demon to full demon lord of an Abyssal
    realm. Treerazer's current exile to the Material Plane prevents him from achieving
    full demon lord status. Yet he still possesses the typical nascent demon lord
    traits, which are similar to those possessed by a typical demon, only more potent,
    as summarized here.Immunity to death effects, electricity, charm and compulsion
    effects, and poison.Resistance to acid 30, cold 30, and fire 30.Summon (Sp) Once
    per day, nascent demon lords can summon any demon or combination of demons whose
    total combined CR is 20 or lower. This ability always works, and is equivalent
    to a 9th-level spell.Telepathy 300 ft.A nascent demon lord's natural weapons,
    as well as any weapon it wields, are treated as chaotic, epic, and evil for the
    purpose of resolving damage reduction.Nascent demon lords can grant spells to
    their worshipers. Granting spells does not require any specific action on the
    nascent demon lord's behalf. All nascent demon lords grant access to the domains
    of Chaos and Evil-in addition, they grant access to two other domains and a favored
    weapon that vary according to the nascent demon lord's themes and interests.
desc_long: |-
  Treerazer, the self-styled Lord of the Blasted Tarn, was once the favored minion and lieutenant (some even say child) of Cyth-V'sug, Demon Lord of Fungus and Parasites. After a failed attempt to wrest that crown away from Cyth-V'sug, Treerazer fled to the Material Plane. Cyth-V'sug was unable (or perhaps only unwilling) to pursue, but took steps to ensure that Treerazer would remain there by exiling him, transforming Treerazer into a native outsider and severing his bond to the Abyss-if the Lord of the Blasted Tarn is slain, his animus will not return to the Abyss and reform. Death, to Treerazer, is a permanent thing.

  Treerazer arrived on Golarion near the end of the Age of Darkness, and found the savaged planet much to his liking-so much so that the sting of exile was somewhat ameliorated. He spent many centuries wandering the remote corners of Golarion before finally coming upon the abandoned elven nation of Kyonin in 2497 ar. In the Sovyrian Stone, he found an artifact that he believed he could use to reinstate his Abyssal link and, perhaps, even uproot the entire nation and refocus the portal from Sovyrian to the Abyss, thereby reclaiming his position there and taking one more step toward revenge against Cyth-V'sug. Yet the elves sensed his tamperings and returned to confront the demon. A terrific battle resulted, and while the elves were able to drive Treerazer out of Iadara and into southern Kyonin, they were unable to slay him or force him out completely-they merely concentrated his power in a smaller region. Instead, the elves “walled off ” this region, a perverted realm known today as the Tanglebriar. Treerazer lurks at the Tanglebriar's heart to this day, the greatest bogeyman in elven mythology and a very real and constant threat to the nation's security.

  Treerazer begins most combats by casting time stop and raising an antiplant shell to prevent plant creatures (including creatures under the effect of his aura of corruption) from approaching. If he has time, he also creates walls of thorns and summons demons (usually four nalfeshnees and 12 hezrous). In melee, Treerazer gleefully takes up Blackaxe and makes full attacks against the closest foe, or Greater Vital Strikes if he's forced to move or charge. During the first 3 rounds of combat, he targets obvious spell effects with quickened greater dispel magic. If Treerazer is reduced to fewer than 150 hit points, he teleports back to his fortress, Witchbole, to recover and plan his revenge.

---

# Treerazer
The twenty-foot-tall winged _[[monsters/Saurian|saurian]]_ demon wields an acid-dripping axe. Two red eyes glow above a tooth-filled beak.
**Source** Inner Sea World Guide pg. 314, Pathfinder #17: A Memory of _[[spells/Darkness|Darkness]]_ pg. 88
**XP** 1,638,400
CE Huge outsider (demon, native)
**Init** +14; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Law|detect law]]_, _[[spells/True Seeing|true seeing]]_; Perception +38
**Aura** corruption (120 ft.), _[[spells/Unholy Aura|unholy aura]]_ (DC 25)

##### Defense

**AC** 42, touch 22, _[[conditions/Flat-Footed|flat-footed]]_ 32 (+4 deflection, +10 Dex, +20 natural, -2 size)
**hp** 574 (28d10+420); _[[universal monster rules/Regeneration|regeneration]]_ 15 (good)
**Fort** +34, **Ref** +23, **Will** +27
**Defensive Abilities** _[[spells/Freedom of Movement|freedom of movement]]_; **DR** 15/cold iron and good; **Immune** death effects, disease, electricity, mind-affecting effects, poison; **Resist** acid 30, cold 30, fire 30; **SR** 36

##### Offense
**Speed** 60 ft., fly 60 ft. (good), swim 40 ft.
**Melee** _[[items/Weapon/Blackaxe|Blackaxe]]_ +44/+39/+34/+29 (4d6+24/19-20/x3 plus 1d6 acid), bite +37 (2d6+6), 2 wings +37 (1d8+6)
**Space** 20 ft., **Reach** 20 ft.
**Special Attacks** defoliation
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +27)
Constant — _detect good_, _detect law_, _freedom of movement_, _true seeing_, _unholy aura_, _[[universal monster rules/Water Breathing|water breathing]]_
At will — _[[spells/Antiplant Shell|antiplant shell]]_, _[[spells/Contagion|contagion]]_ (DC 21), _[[spells/Desecrate|desecrate]]_, greater _[[spells/Dispel Magic, Greater|dispel magic, greater]]_ teleport (within Tanglebriar only), _[[spells/Telekinesis|telekinesis]]_ (DC 22), _[[spells/Unholy Blight|unholy blight]]_ (DC 21)
3/day — _[[spells/Control Plants|control plants]]_ (DC 25), quickened greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Wall Of Thorns|wall of thorns]]_
1/day — _[[spells/Horrid Wilting|horrid wilting]]_ (DC 25), _[[universal monster rules/Summon|summon]]_ demons, _[[spells/Symbol of Death|symbol of death]]_ (DC 25), _[[spells/Time Stop|time stop]]_

##### Statistics
**Str** 36, **Dex** 30, **Con** 40, **Int** 21, **Wis** 24, **Cha** 25
**Base Atk** +28; **CMB** +43; **CMD** 67
**Feats** _[[feats/Awesome Blow|Awesome Blow]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Greater Vital Strike|Greater Vital Strike]]_, _[[feats/Improved Bull Rush|Improved Bull Rush]]_, _[[feats/Improved Critical|Improved Critical]]_ (_[[items/Weapon/Greataxe|greataxe]]_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Multiattack|Multiattack]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (greater _dispel magic_), _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Vital Strike|Vital Strike]]_
**Skills** Acrobatics +41, Fly +38, Intimidate +38, Knowledge (arcana) +36, Knowledge (nature) +36, Knowledge (planes) +36, Perception +38, Sense Motive +38, Spellcraft +33, Stealth +33, Swim +49
**Languages** Abyssal, Common, Elven, Sylvan; _[[universal monster rules/Telepathy|telepathy]]_ 300 ft.
**SQ** nascent demon lord traits
**Gear** _Blackaxe_ (see page 299)

##### Ecology

**Environment** Tanglebriar
**Organization** solitary or group (Treerazor plus 1d4 nalfeshnees and 2d4 hezrous)
**Treasure** triple (plus _Blackaxe_)

### Special Abilities

**Aura of Corruption (Su)** _[[monsters/Treerazer|Treerazer]]_ exudes an aura of corruption to a radius of 120 feet. This aura causes plants to grow hideous, sprouting thorns, twisting, and becoming fungoid in nature. Creatures with woodland stride or _freedom of movement_ can move through this fungal bloom with ease. Living creatures within _Treerazer_’s aura of corruption must make a DC 39 Fortitude save each round or their flesh grows pasty and clammy as tendrils of diseased plant matter and fungal growth sprout from it. This condition persists as long as the creature remains within _Treerazer_’s aura of corruption and for 1 minute thereafter. While suffering the effects of this aura, the living creature is treated as a plant for the purposes of spells and effects that _[[spells/Harm|harm]]_ or otherwise inconvenience plant creatures more than other creatures. The victim would thus be subject to _antiplant shell_, _[[spells/Blight|blight]]_, and additional damage from _horrid wilting_ or a plant _[[spells/Bane|bane]]_ weapon, and could be affected by _control plants_. The corruption does not otherwise impart _[[universal monster rules/Plant Traits|plant traits]]_ to creatures. The save DC is Constitution-based.

**Defoliation (Su)** As a standard action once every 1d4 rounds, _Treerazer_ can exude a pulse of defoliating energy in a 30-foot-radius spread. This pulse appears as a wave of sickly green energy, and causes all plants and plant creatures in the area to blacken and wither. Such creatures take 20d10 points of damage and 1d8 points of Strength drain, or half with a successful DC 39 Fortitude save. A plant that isn’t a creature (such as a tree or a shrub) doesn’t receive a save and immediately withers and dies. _Treerazer_ can choose to exclude any number of plants in the area from this effect, and generally does so to _[[spells/Preserve|preserve]]_ twisted and corrupted plants and fungus. The save DC is Constitution-based.

**Nascent Demon Lord Traits** A nascent demon lord is a powerful demon that has not yet made the full transition from unique demon to full demon lord of an Abyssal realm. _Treerazer_’s current exile to the Material Plane prevents him from achieving full demon lord _[[spells/Status|status]]_. Yet he still possesses the typical nascent demon lord traits, which are similar to those possessed by a typical demon, only more _[[items/Weapon Magic Abilities/Potent|potent]]_, as summarized here.

* _[[universal monster rules/Immunity|Immunity]]_ to death effects, electricity, charm and compulsion effects, and poison.
* _[[universal monster rules/Resistance|Resistance]]_ to acid 30, cold 30, and fire 30.
* _Summon_ (Sp) Once per day, nascent demon lords can _summon_ any demon or combination of demons whose total combined CR is 20 or lower. This ability always works, and is equivalent to a 9th-level spell.
* _Telepathy_ 300 ft.
* A nascent demon lord’s natural weapons, as well as any weapon it wields, are treated as chaotic, epic, and evil for the purpose of resolving _[[universal monster rules/Damage Reduction|damage reduction]]_.
* Nascent demon lords can grant spells to their worshipers. Granting spells does not require any specific action on the nascent demon lord’s behalf. All nascent demon lords grant access to the domains of Chaos and Evil—in addition, they grant access to two other domains and a favored weapon that vary according to the nascent demon lord’s themes and interests.

##### Description

_Treerazer_, the self-styled Lord of the Blasted Tarn, was once the favored minion and lieutenant (some even say child) of Cyth-V’sug, Demon Lord of Fungus and Parasites. After a failed attempt to wrest that crown away from Cyth-V’sug, _Treerazer_ fled to the Material Plane. Cyth-V’sug was unable (or perhaps only unwilling) to pursue, but took steps to ensure that _Treerazer_ would remain there by exiling him, transforming _Treerazer_ into a native outsider and severing his bond to the Abyss—if the Lord of the Blasted Tarn is slain, his animus will not return to the Abyss and reform. Death, to _Treerazer_, is a permanent thing.

_Treerazer_ arrived on Golarion near the end of the Age of _Darkness_, and found the savaged planet much to his liking—so much so that the sting of exile was somewhat ameliorated. He spent many centuries wandering the remote corners of Golarion before finally coming upon the abandoned elven nation of Kyonin in 2497 ar. In the Sovyrian Stone, he found an artifact that he believed he could use to reinstate his Abyssal link and, perhaps, even uproot the entire nation and refocus the portal from Sovyrian to the Abyss, thereby reclaiming his position there and taking one more step toward revenge against Cyth-V’sug. Yet the elves sensed his tamperings and returned to confront the demon. A terrific battle resulted, and while the elves were able to drive _Treerazer_ out of Iadara and into southern Kyonin, they were unable to slay him or force him out completely—they merely concentrated his power in a smaller region. Instead, the elves “walled off ” this region, a perverted realm known today as the Tanglebriar. _Treerazer_ lurks at the Tanglebriar’s heart to this day, the greatest _[[monsters/Bogeyman|bogeyman]]_ in elven mythology and a very real and constant threat to the nation’s security.

_Treerazer_ begins most combats by casting _time stop_ and raising an _antiplant shell_ to prevent plant creatures (including creatures under the effect of his aura of corruption) from approaching. If he has time, he also creates walls of thorns and summons demons (usually four nalfeshnees and 12 hezrous). In melee, _Treerazer_ gleefully takes up _Blackaxe_ and makes full attacks against the closest foe, or Greater Vital Strikes if he’s forced to move or charge. During the first 3 rounds of combat, he targets obvious spell effects with quickened greater _dispel magic_. If _Treerazer_ is reduced to fewer than 150 hit points, he teleports back to his fortress, Witchbole, to recover and plan his revenge.