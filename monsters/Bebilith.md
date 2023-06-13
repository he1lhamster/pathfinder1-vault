---
cssclass: [monsters]
title1: Bebilith
desc_short: A spider the size of an elephant, this dark blue arachnid rears up on
  its six hind legs to raise its barbed and razor-edged front claws.
title2: Bebilith
CR: 10
sources:
- name: Pathfinder RPG Bestiary
  page: 32
  link: http://paizo.com/products/btpy8auu?Pathfinder-Roleplaying-Game-Bestiary
XP: 9600
alignment: CE
size: Huge
type: outsider
subtypes:
- chaotic
- evil
- extraplanar
initiative:
  bonus: 5
senses:
  darkvision: 60
  scent: true
AC:
  AC: 22
  touch: 9
  flat_footed: 21
  components:
    dex: 1
    natural: 13
    size: -2
HP:
  HP: 150
  long: 12d10+84
saves:
  fort: 15
  ref: 11
  will: 7
DR:
- amount: 10
  weakness: good
speeds:
  base: 40
  climb: 20
attacks:
  melee:
  - - text: bite +19 (2d6+9 plus rot)
      entries:
      - - damage: 2d6+9
        - effect: rot
      attack: bite
      bonus:
      - 19
    - text: 2 claws +19 (2d4+9/19-20)
      entries:
      - - damage: 2d4+9
          crit_range: 19-20
      count: 2
      attack: claws
      bonus:
      - 19
  special:
  - dismantle armor
  - penetrating strike
  - web (+11 ranged, DC 23, 12 hp)
space: 15
reach: 15
spell_like_abilities:
  entries:
  - name: plane shift
    source: default
    freq: At will
    other: bebilith only
  sources:
  - name: default
    CL: 12
ability_scores:
  STR: 28
  DEX: 12
  CON: 24
  INT: 11
  WIS: 13
  CHA: 13
BAB: 12
CMB: 23
CMD: 34
CMD_other: 46 vs. trip
feats:
- name: Cleave
- name: Improved Critical (claws)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
skills:
  Acrobatics: 16
  Climb: 32
  Perception: 16
  Sense Motive: 16
  Stealth: 16
  Survival: 16
  _racial_mods:
    Stealth:
      _: 8
languages:
- Abyssal (cannot speak)
- telepathy 100 ft.
ecology:
  environment: any (the Abyss)
  organization: solitary or band (2-6)
  treasure_type: standard
special_abilities:
  Dismantle Armor (Ex): If a bebilith hits a foe with both claw attacks, it can attempt
    to peel away the target's armor and shield as a free action by making a CMB check.
    If the bebilith is successful, the target's armor and shield are torn from his
    body and dismantled, falling to the ground. Armor subjected to this attack loses
    half its hit points and gains the broken condition if the target fails a DC 25
    Reflex save. The save DC is Strength-based.
  Penetrating Strike (Su): A bebilith's natural weapons are treated as chaotic and
    magical for the purposes of penetrating damage reduction. Against creatures with
    the demon type, its natural weapons are also treated as cold iron and good.
  Rot (Su): A bebilith's bite causes a horrible withering and weakening of the flesh,
    resulting in a hideous melting and foul rotting effect. This catastrophic withering
    begins on the round the creature is bitten and continues for another 4 rounds
    thereafter, for 5 rounds of withering in all. Each round the rot persists, the
    target must succeed on a DC 23 Fortitude save or take 2 points of Constitution
    damage. If the target makes two consecutive saving throws in a row, the effect
    is cured. Heal can also halt the rot effect. The save DC is Constitution-based.
desc_long: |-
  The Abyss is a terrible place, yet even in this horrific realm there exist predators and wild beasts that prey upon the demonic horde-the bebilith being the most notorious, a creature evolved to hunt and slay demons.

  Far more intelligent than its verminous shape would suggest, it is perhaps a blessing that the bebilith is such a focused and devoted hunter of demons, for had these dangerous outsiders more of a mind to conquer and expand empires, their ability to plane shift would make them a menace indeed. Although, as an outsider, the bebilith has no biological need to eat, it does enjoy the sensation of chewing on demonic flesh.

---

# Bebilith
A spider the size of an _[[monsters/Elephant|elephant]]_, this dark blue arachnid rears up on its six hind legs to raise its barbed and razor-edged front claws.
**Source** Pathfinder RPG Bestiary pg. 32
**XP** 9,600
CE Huge outsider (chaotic, evil, extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +16

##### Defense

**AC** 22, touch 9, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+1 Dex, +13 natural, –2 size)
**hp** 150 (12d10+84)
**Fort** +15, **Ref** +11, **Will** +7
**DR** 10/good

##### Offense
**Speed** 40 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** bite +19 (2d6+9 plus rot) and 2 claws +19 (2d4+9/19–20)
**Space** 15 ft., **Reach** 15 ft.
**Special Attacks** dismantle armor, _[[feats/Penetrating Strike|penetrating strike]]_, web (+11 ranged, DC 23, 12 hp)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th)
At will—_[[spells/Plane Shift|plane shift]]_ (_[[monsters/Bebilith|bebilith]]_ only)

##### Statistics
**Str** 28, **Dex** 12, **Con** 24, **Int** 11, **Wis** 13, **Cha** 13
**Base Atk** +12; **CMB** +23; **CMD** 34 (46 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (claws), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_
**Skills** Acrobatics +16, _Climb_ +32, Perception +16, Sense Motive +16, Stealth +16, Survival +16; **Racial Modifiers** +8 Stealth
**Languages** Abyssal (cannot speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (the Abyss)
**Organization** solitary or band (2–6)
**Treasure** standard

### Special Abilities

**Dismantle Armor (Ex) **If a _bebilith_ hits a foe with both claw attacks, it can attempt to peel away the target’s armor and _[[spells/Shield|shield]]_ as a free action by making a CMB check. If the _bebilith_ is successful, the target’s armor and _shield_ are torn from his body and dismantled, falling to the ground. Armor subjected to this attack loses half its hit points and gains the _[[conditions/Broken|broken]]_ condition if the target fails a DC 25 Reflex save. The save DC is Strength-based.

**_Penetrating Strike_ (Su)** A _bebilith_’s natural weapons are treated as chaotic and magical for the purposes of penetrating _[[universal monster rules/Damage Reduction|damage reduction]]_. Against creatures with the demon type, its natural weapons are also treated as cold iron and good.

**Rot (Su) **A _bebilith_’s bite causes a horrible withering and weakening of the flesh, resulting in a hideous melting and foul rotting effect. This catastrophic withering begins on the round the creature is bitten and continues for another 4 rounds thereafter, for 5 rounds of withering in all. Each round the rot persists, the target must succeed on a DC 23 Fortitude save or take 2 points of Constitution damage. If the target makes two consecutive saving throws in a row, the effect is cured. _[[spells/Heal|Heal]]_ can also halt the rot effect. The save DC is Constitution-based.

##### Description

The Abyss is a terrible place, yet even in this horrific realm there exist predators and wild beasts that prey upon the demonic horde—the _bebilith_ being the most notorious, a creature evolved to hunt and slay demons.

Far more intelligent than its verminous shape would suggest, it is perhaps a blessing that the _bebilith_ is such a focused and devoted _[[classes/Hunter|hunter]]_ of demons, for had these dangerous outsiders more of a mind to conquer and expand empires, their ability to _plane shift_ would make them a menace indeed. Although, as an outsider, the _bebilith_ has no biological need to eat, it does enjoy the sensation of chewing on demonic flesh.