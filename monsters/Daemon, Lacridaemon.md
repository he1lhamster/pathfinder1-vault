---
cssclass: [monsters]
title1: Daemon, Lacridaemon
desc_short: The face of this gray-skinned humanoid stretches in a manic grin,even
  though it weeps steaming tears. Frost crusts its flesh.
title2: Lacridaemon
CR: 3
sources:
- name: Bestiary 6
  page: 71
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
- name: 'Book of the Damned - Volume 3: Horsemen of the Apocalypse'
  page: 48
  link: http://paizo.com/products/btpy8odg?Pathfinder-Campaign-Setting-Book-of-the-Damned-Volume-3-Horsemen-of-the-Apocalypse
XP: 800
alignment: NE
size: Medium
type: outsider
subtypes:
- daemon
- evil
- extraplanar
initiative:
  bonus: 7
senses:
  darkvision: 60
  detect good: true
  detect magic: true
auras:
- name: weeping
  radius: 100
AC:
  AC: 15
  touch: 13
  flat_footed: 12
  components:
    dex: 3
    natural: 2
HP:
  HP: 30
  long: 4d10+8
saves:
  fort: 6
  ref: 4
  will: 5
DR:
- amount: 5
  weakness: good or silver
immunities:
- acid
- cold
- death effects
- disease,poison
resistances:
  electricity: 10
  fire: 10
SR: 14
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +5 (1d4+1 plus 1d4 cold and poison)
      entries:
      - - damage: 1d4+1
        - damage: 1d4
          type: cold
        - effect: poison
      attack: bite
      bonus:
      - 5
    - text: 2 claws +6(1d4+1 plus 1d4 cold)
      entries:
      - - damage: 1d4+1
        - damage: 1d4
          type: cold
      count: 2
      attack: claws
      bonus:
      - 6
  special:
  - poisonous tears
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: detect magic
    source: default
    freq: Constant
  - name: pass without trace
    source: default
    freq: Constant
  - name: overwhelming grief
    source: default
    freq: 3/day
    DC: 15
  - name: teleport
    source: default
    freq: 3/day
    other: self plus 50 lbs. of objects only
  - name: hold person
    source: default
    freq: 1/day
    DC: 14
  - name: invisibility
    source: default
    freq: 1/day
  - name: snare
    source: default
    freq: 1/day
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: lacridaemon
      amount: 1
      chance: 50%
  sources:
  - name: default
    CL: 4
    concentration: 5
ability_scores:
  STR: 12
  DEX: 17
  CON: 14
  INT: 11
  WIS: 13
  CHA: 12
BAB: 4
CMB: 5
CMD: 18
feats:
- name: Improved Initiative
- name: Weapon Focus (claw)
skills:
  Acrobatics: 10
  Bluff: 8
  Climb: 8
  Perception: 8
  Sense Motive: 8
  Stealth: 10
languages:
- Abyssal
- Draconic
- Infernal
- telepathy100 ft.
ecology:
  environment: any (Abaddon)
  organization: solitary, pair, or lurk (3-6)
  treasure_type: standard
special_abilities:
  Poisonous Tears (Su): |-
    A lacridaemon's tears are poisonous to other creatures. As a swift action that provokes attacks of opportunity, a lacridaemon can coat both of its claws with its tears, giving its next attack the possibility of poisoning its victim. In order to use this ability, a lacridaemon must attack with its claws on the same round it applies its tears; after that time, the tears lose their potency. A lacridaemon's bite attack is always treated as having its poisonous tears applied to it. The save DC is Constitution-based. 

    Lacridaemon Poison: Bite-injury; save Fortitude DC 14; frequency 1/round for 6 rounds; effect 1 Wis damage plus staggered for 1 round; cure 2 consecutive saves.
  Weeping Aura (Su): A lacridaemon is surrounded by the muffled sounds of a crying
    child. These whimpers sound as if they're coming from all directions at once,
    disorienting those within 100 feet of the lacridaemon. Any creature that enters
    this area must succeed at a DC 13 Will saving throw or take a -5 penalty on Survival
    checks to avoid becoming lost for 24 hours. A lacridaemon can suppress or reactivate
    its aura as a free action, and the effects from multiple lacridaemon auras stack
    (up to a maximum penalty of -20). This aura is a sonic mind-affecting effect.
    The save DC is Charisma-based.
desc_long: |-
  Among the least powerful of all daemons, lacridaemons personify death by neglect or exposure to the elements, such as that suffered by those who become lost in the wilderness and die far from help, or unfortunates who become trapped in an enclosed space (like a collapsed mine) and are left alone to slowly expire. Lacridaemons' despair is in stark contrast to their savage nature. If they're given any opportunity, they viciously lash out, furiously attacking their mortal victims. 

  In death, lacridaemons continue to suffer just as their mortal incarnations did in their last days of life, consumed by feelings of abandonment, self-pity, and a gnawing sense of loneliness. They often spawn from the souls of evil mortals who died alone and abandoned-exiled criminals, reclusive and corrupt nobles, or those who died from intense exposure to the natural elements (whether the blistering heat of the desert or the ravaging cold of the arctic), such as by freezing to death or dying of thirst. 

  A lacridaemon stands just under 6 feet tall but weighs only 90 pounds.

---

# Daemon, Lacridaemon
The face of this gray-skinned humanoid stretches in a manic grin,

even though it weeps _[[items/Armor Magic Abilities/Steaming|steaming]]_ tears. Frost crusts its flesh.
**Source** Bestiary 6 pg. 71, _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ - Volume 3: Horsemen of the Apocalypse pg. 48
**XP** 800

NE Medium outsider (daemon, evil, extraplanar)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_, _[[spells/Detect Magic|detect magic]]_;

Perception +8
**Aura** _[[items/Armor Magic Abilities/Weeping|weeping]]_ (100 ft.)

##### Defense

**AC** 15, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+3 Dex, +2 natural)
**hp** 30 (4d10+8)
**Fort** +6, **Ref** +4, **Will** +5
**DR** 5/good or silver; **Immune** acid, cold, death effects, disease,

poison; **Resist** electricity 10, fire 10; **SR** 14

##### Offense
**Speed** 40 ft.
**Melee** bite +5 (1d4+1 plus 1d4 cold and poison), 2 claws +6

(1d4+1 plus 1d4 cold)
**Special Attacks** poisonous tears
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +5)
Constant—_detect good_, _detect magic_, _[[spells/Pass without Trace|pass without trace]]_ 
3/day—_[[spells/Overwhelming Grief|overwhelming grief]]_ (DC 15), teleport (self plus 50 lbs. of objects only) 
1/day—_[[spells/Hold Person|hold person]]_ (DC 14), _[[spells/Invisibility|invisibility]]_, _[[spells/Snare|snare]]_, _[[universal monster rules/Summon|summon]]_ (level 3, 1 lacridaemon 50%)

##### Statistics
**Str** 12, **Dex** 17, **Con** 14, **Int** 11, **Wis** 13, **Cha** 12
**Base Atk** +4; **CMB** +5; **CMD** 18
**Feats** _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Acrobatics +10, Bluff +8,

_[[universal monster rules/Climb|Climb]]_ +8, Perception +8, Sense Motive +8,

Stealth +10
**Languages** Abyssal, Draconic, Infernal; _[[universal monster rules/Telepathy|telepathy]]_

100 ft.

##### Ecology

**Environment** any (Abaddon)
**Organization** solitary, pair, or lurk (3–6)
**Treasure** standard

### Special Abilities

**Poisonous Tears (Su)** A lacridaemon’s tears are poisonous to other creatures. As a swift action that provokes attacks of opportunity, a lacridaemon can coat both of its claws with its tears, giving its next attack the possibility of _[[items/Armor Magic Abilities/Poisoning|poisoning]]_ its victim. In order to use this ability, a lacridaemon must attack with its claws on the same round it applies its tears; after that time, the tears lose their potency. A lacridaemon’s bite attack is always treated as having its poisonous tears applied to it. The save DC is Constitution-based.

Lacridaemon Poison: Bite—injury; save Fortitude DC 14; frequency 1/round for 6 rounds; effect 1 Wis damage plus _[[conditions/Staggered|staggered]]_ for 1 round; cure 2 consecutive saves.

**_Weeping_ Aura (Su)** A lacridaemon is surrounded by the muffled sounds of a crying child. These whimpers sound as if they’re coming from all directions at once, disorienting those within 100 feet of the lacridaemon. Any creature that enters this area must succeed at a DC 13 Will saving throw or take a –5 penalty on Survival checks to avoid becoming lost for 24 hours. A lacridaemon can suppress or reactivate its aura as a free action, and the effects from multiple lacridaemon auras stack (up to a maximum penalty of –20). This aura is a sonic mind-affecting effect. The save DC is Charisma-based.

##### Description

Among the least powerful of all daemons, lacridaemons personify death by neglect or exposure to the elements, such as that suffered by those who become lost in the wilderness and die far from help, or unfortunates who become trapped in an enclosed space (like a collapsed mine) and are left alone to slowly expire. Lacridaemons’ despair is in stark contrast to their savage nature. If they’re given any opportunity, they viciously lash out, furiously attacking their mortal victims.

In death, lacridaemons continue to suffer just as their mortal incarnations did in their last days of life, consumed by feelings of abandonment, self-pity, and a gnawing sense of loneliness. They often spawn from the souls of evil mortals who died alone and abandoned—exiled criminals, reclusive and corrupt nobles, or those who died from intense exposure to the natural elements (whether the blistering _[[universal monster rules/Heat|heat]]_ of the desert or the ravaging cold of the arctic), such as by freezing to death or _[[conditions/Dying|dying]]_ of thirst.

A lacridaemon stands just under 6 feet tall but weighs only 90 pounds.