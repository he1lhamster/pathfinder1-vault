---
cssclass: [monsters]
title1: Devil, Salikotal
desc_short: On lean limbs the color of spilt blood creeps a being of sinister grace.
  Eyes like embers and a sneer full of needle-thin teeth gleam from an unmistakably
  fiendish visage. A pair of crimson wings sprout from the back of the hairless humanoid
  form, fluttering silently like an assassin's cloak, while in one hand it clutches
  the twisted, dagger-like horn of some infernal terror.
title2: Salikotal
CR: 7
sources:
- name: 'Pathfinder #26: The Sixfold Trial'
  page: 82
  link: http://paizo.com/pathfinder/adventurePath/councilOfThieves/v5748btpy89vw
XP: 3200
alignment: LE
size: Medium
type: outsider
subtypes:
- devil
- evil
- extraplanar
- lawful
initiative:
  bonus: 10
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 23
  touch: 17
  flat_footed: 16
  components:
    dex: 6
    dodge: 1
    natural: 6
HP:
  HP: 76
  long: 9d10+27
saves:
  fort: 9
  ref: 12
  will: 7
DR:
- amount: 5
  weakness: good
immunities:
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 18
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 dagger +14/+9 (1d4+5/17-20)
      entries:
      - - damage: 1d4+5
          crit_range: 17-20
      attack: +1 dagger
      bonus:
      - 14
      - 9
    - text: tail +8 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: tail
      bonus:
      - 8
  - - text: 2 claws +13 (1d4+4)
      entries:
      - - damage: 1d4+4
      count: 2
      attack: claws
      bonus:
      - 13
    - text: tail +8 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: tail
      bonus:
      - 8
  ranged:
  - - text: +1 dagger +16 (1d4+5/17-20)
      entries:
      - - damage: 1d4+5
          crit_range: 17-20
      attack: +1 dagger
      bonus:
      - 16
  special:
  - contract killer
  - sneak attack +3d6
  - suicide
  - vengeance
spell_like_abilities:
  entries:
  - name: spider climb
    source: default
    freq: Always active
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 pounds of objects only
  - name: locate creature
    source: default
    freq: At will
  - name: knock
    source: default
    freq: At will
  - name: blur
    source: default
    freq: 3/day
    other: self only
  - name: darkness
    source: default
    freq: 3/day
  - name: dimension door
    source: default
    freq: 3/day
  - name: dispel magic
    source: default
    freq: 3/day
  - name: silence
    source: default
    freq: 3/day
    DC: 16
  - name: suggestion
    source: default
    freq: 3/day
    DC: 17
  - name: mislead
    source: default
    freq: 1/day
    DC: 20
  - name: passwall
    source: default
    freq: 1/day
  - name: statue
    source: default
    freq: 1/day
    other: self only
  - name: summon devil
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: imps
      amount: 4
      chance: 35%
  sources:
  - name: default
    CL: 9
ability_scores:
  STR: 18
  DEX: 22
  CON: 17
  INT: 15
  WIS: 19
  CHA: 18
BAB: 9
CMB: 13
CMD: 30
feats:
- name: Dodge
- name: Improved Critical (dagger)
- name: Improved Initiative
- name: Mobility
- name: Wind Stance
skills:
  Acrobatics: 15
  Disable Device: 18
  Disguise: 16
  Escape Artist: 18
  Knowledge (local): 11
  Sense Motive: 16
  Sleight of Hand: 18
  Stealth: 18
  Perception: 4
languages:
- Celestial
- Common
- Infernal
- telepathy 100 ft.
gear:
  gear:
  - +1 dagger
ecology:
  environment: any (Hell)
  organization: solitary or team (2-8)
  treasure_type: standard
  treasure:
  - +1 dagger
  - other treasure
special_abilities:
  Contract Killer (Su): A salikotal gains a +2 bonus on attack and damage rolls when
    attacking a specific individual it has marked for death. At the beginning of each
    day, it determines an individual to serve as its target and which one of its three
    vengeances it may make use of that day. It may not change this target or ability
    until the next day. The target may be any specific creature the salikotal knows
    of, even if it has not seen its target before. This target is treated as being
    known to a salikotal for the purposes of using its locate creature ability, even
    if the devil has never seen its victim before.
  Sneak Attack (Ex): Anytime a salikotal's opponent is denied his Dexterity bonus
    to AC, or if a salikotal flanks his opponent, he deals an extra 3d6 points of
    damage. This ability is just like the rogue's sneak attack and subject to the
    same limitations.
  Suicide (Su): As a standard action, a salikotal may target itself with a coup de
    grace attack. If the salikotal reduces itself to fewer than 0 hit points-or fails
    to do so but still fails the associated Fortitude save (DC = 10 + damage dealt)-the
    salikotal erupts in a burst of destructive energy. Any creature within 15 feet
    of a salikotal that commits suicide is damaged by a blast of metal shards and
    needle-like scales, taking 6d6 points of damage (DC 17, save for half ). The save
    DC is Constitution-based. Upon using this ability, a salikotal is permanently
    destroyed. This effect only takes place if a salikotal willingly ends its own
    life, not if it is killed by outside effects.
  Vengeance (Su): |-
    While seeking a victim a salikotal prepares itself daily, honing its will to effectively slaughter its intended quarry. On a given day, chosen as part of its contract killer ability, a salikotal may gain the benefit of any one of the following powers, either the one it feels will most aid it or whichever one its summoner requests. Only one of these abilities is active on a given day, and it only comes into effect when a salikotal kills its intended target with a coup de grace. These executions only function on living creatures.

    Fideicide: The victim's soul is immediately shunted to a infernal prison on Erebus, the third layer of Hell. The soul can be returned to life, but upon casting the spell, the spellcaster attempting the resurrection takes an amount of fire damage equal to 1d6 × the victim's number of Hit Dice, and must make an immediate concentration check (DC 10 + damage delt + spell level) or lose the spell.

    Necrocide: After 1d4 rounds, the victim's body animates as a zombie under the salikotal's control. The devil may permanently grant control of the zombie to any sentient creature as a free action.

    Omnicide: The victim's body is utterly destroyed, disintegrating without a trace. Its clothing and possessions remain unharmed. Only spells that do not require a portion of the corpse may return the victim to life.
desc_long: |-
  Prince-killers and assassins of souls, salikotals serve as the bloody chisels by which the lords of Hell subtly shape the mortal world to their whims. Soaring through the night on silent wings, these murderous devils care nothing for life or reason, knowing only a single, murderous goal. Cloaked by shadow and silence, few ever glimpse the sharp features of a salikotal, for Hell's death-dealers reveal themselves only amid the haze of fading life.

  Lean, deft hunters, salikotals move like terrible predatory birds, each taloned step measured, cautious, and full of deadly intent. Protected by an armor of sharp, thin scales, these agile devils universally stand 5 feet, 4 inches tall, and weigh 85 pounds, their barbed frames supporting the breadth of their 8-foot-wide, bat-like wings. They have full control over their slender tails, nimbly manipulating objects and even wielding deadly, Hell-forged blades in these dexterous, prehensile appendages.

---

# Devil, Salikotal
On lean limbs the color of spilt blood creeps a being of sinister _[[spells/Grace|grace]]_. Eyes like embers and a sneer full of needle-thin teeth gleam from an unmistakably fiendish visage. A pair of crimson wings sprout from the back of the hairless humanoid form, fluttering silently like an assassin’s cloak, while in one hand it clutches the twisted, dagger-like horn of some infernal terror.
**Source** Pathfinder #26: The Sixfold Trial pg. 82
**XP** 3,200

LE Medium outsider (devil, evil, extraplanar, lawful)
**Init** +10; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +4

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+6 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 76 (9d10+27)
**Fort** +9, **Ref** +12, **Will** +7
**DR** 5/good; **Immune** fire, poison; **Resist** acid 10, cold 10; **SR** 18

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** +1 _[[items/Weapon/Dagger|dagger]]_ +14/+9 (1d4+5/17-20), tail +8 (1d4+2) or 2 claws +13 (1d4+4), tail +8 (1d4+2)
**Ranged** +1 _dagger_ +16 (1d4+5/17-20)
**Special Attacks** _[[npcs/Contract Killer|contract killer]]_, sneak attack +3d6, suicide, _[[feats/Vengeance|vengeance]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th)
Always active — _[[spells/Spider Climb|spider climb]]_
At will — greater teleport (self plus 50 pounds of objects only), _[[spells/Locate Creature|locate creature]]_, _[[spells/Knock|knock]]_
3/day — _[[spells/Blur|blur]]_ (self only), _[[spells/Darkness|darkness]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Silence|silence]]_ (DC 16), _[[spells/Suggestion|suggestion]]_ (DC 17)
1/day — _[[spells/Mislead|mislead]]_ (DC 20), _[[spells/Passwall|passwall]]_, _[[spells/Statue|statue]]_ (self only), _[[universal monster rules/Summon|summon]]_ devil (level 3, 4 imps, 35%)

##### Statistics
**Str** 18, **Dex** 22, **Con** 17, **Int** 15, **Wis** 19, **Cha** 18
**Base Atk** +9; **CMB** +13; **CMD** 30
**Feats** _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_dagger_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Wind Stance|Wind Stance]]_
**Skills** Acrobatics +15, Disable Device +18, Disguise +16, Escape Artist +18, Knowledge (local) +11, Sense Motive +16, Sleight of Hand +18, Stealth +18
**Languages** Celestial, Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**Gear** +1 _dagger_

##### Ecology

**Environment** any (Hell)
**Organization** solitary or team (2-8)
**Treasure** standard (+1 _dagger_, other treasure)

### Special Abilities

**_Contract Killer_ (Su)** A salikotal gains a +2 bonus on attack and damage rolls when attacking a specific individual it has marked for death. At the beginning of each day, it determines an individual to serve as its target and which one of its three vengeances it may make use of that day. It may not change this target or ability until the next day. The target may be any specific creature the salikotal knows of, even if it has not seen its target before. This target is treated as being known to a salikotal for the purposes of using its _locate creature_ ability, even if the devil has never seen its victim before.
**Sneak Attack (Ex)** Anytime a salikotal’s opponent is denied his Dexterity bonus to AC, or if a salikotal flanks his opponent, he deals an extra 3d6 points of damage. This ability is just like the _[[classes/Rogue|rogue]]_’s sneak attack and subject to the same limitations.
**Suicide (Su)** As a standard action, a salikotal may target itself with a coup de _grace_ attack. If the salikotal reduces itself to fewer than 0 hit points—or fails to do so but still fails the associated Fortitude save (DC = 10 + damage dealt)—the salikotal erupts in a burst of destructive energy. Any creature within 15 feet of a salikotal that commits suicide is damaged by a blast of metal shards and needle-like scales, taking 6d6 points of damage (DC 17, save for half ). The save DC is Constitution-based. Upon using this ability, a salikotal is permanently destroyed. This effect only takes place if a salikotal willingly ends its own life, not if it is killed by outside effects.

**_Vengeance_ (Su)** While seeking a victim a salikotal prepares itself daily, honing its will to effectively slaughter its intended quarry. On a given day, chosen as part of its _contract killer_ ability, a salikotal may gain the benefit of any one of the following powers, either the one it feels will most aid it or whichever one its _[[classes/Summoner|summoner]]_ requests. Only one of these abilities is active on a given day, and it only comes into effect when a salikotal kills its intended target with a coup de _grace_. These executions only function on living creatures.

Fideicide: The victim’s soul is immediately shunted to a infernal prison on Erebus, the third layer of Hell. The soul can be returned to life, but upon casting the spell, the spellcaster attempting the _[[spells/Resurrection|resurrection]]_ takes an amount of fire damage equal to 1d6 × the victim’s number of Hit Dice, and must make an immediate concentration check (DC 10 + damage delt + spell level) or lose the spell.

Necrocide: After 1d4 rounds, the victim’s body animates as a zombie under the salikotal’s control. The devil may permanently grant control of the zombie to any sentient creature as a free action.

Omnicide: The victim’s body is utterly destroyed, disintegrating without a trace. Its clothing and possessions remain unharmed. Only spells that do not require a portion of the corpse may return the victim to life.

##### Description

Prince-killers and assassins of souls, salikotals serve as the bloody chisels by which the lords of Hell subtly shape the mortal world to their whims. Soaring through the night on silent wings, these murderous devils care nothing for life or reason, knowing only a single, murderous goal. Cloaked by _[[items/Armor Magic Abilities/Shadow|shadow]]_ and _silence_, few ever glimpse the sharp features of a salikotal, for Hell’s death-dealers reveal themselves only amid the haze of fading life.

Lean, deft hunters, salikotals move like terrible predatory birds, each taloned step measured, cautious, and full of _[[items/Weapon Magic Abilities/Deadly|deadly]]_ intent. Protected by an armor of sharp, thin scales, these _[[items/Weapon Magic Abilities/Agile|agile]]_ devils universally stand 5 feet, 4 inches tall, and weigh 85 pounds, their barbed frames supporting the breadth of their 8-foot-wide, bat-like wings. They have full control over their slender tails, nimbly manipulating objects and even wielding _deadly_, Hell-forged blades in these dexterous, _[[items/Weapon Magic Abilities/Prehensile|prehensile]]_ appendages.