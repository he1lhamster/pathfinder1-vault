---
cssclass: [monsters]
title1: Cerebric Cyst
desc_short: This floating, purple brain has occult sigils glowing on its surface and
  tentacles made of ectoplasm.
title2: Cerebric Cyst
CR: 7
sources:
- name: Occult Bestiary
  page: 13
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 3200
alignment: NE
size: Tiny
type: ooze
initiative:
  bonus: 6
senses:
  thoughtsense: 30
auras:
- name: brain static
  radius: 30
- name: mental static
  radius: 30
  DC: 19
AC:
  AC: 19
  touch: 19
  flat_footed: 14
  components:
    dex: 4
    dodge: 1
    insight: 2
    size: 2
HP:
  HP: 85
  long: 10d8+40
saves:
  fort: 9
  ref: 9
  will: 11
defensive_abilities:
- evasion
- prescience
immunities:
- ooze traits
speeds:
  base: 30
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 2 tentacles +13 (2d6 electricity plus empowering strike and psychic sting)
      entries:
      - - damage: 2d6
          type: electricity
        - effect: empowering strike
        - effect: psychic sting
      count: 2
      attack: tentacles
      bonus:
      - 13
  special:
  - empowering strike
  - psychic sting
space: 2.5
reach: 0
spell_like_abilities:
  entries:
  - superscripts:
    - OA
    name: enshroud thoughts
    source: default
    freq: Constant
  - name: charm monster
    source: default
    freq: At will
    DC: 18
  - name: dominate person
    source: default
    freq: At will
    DC: 19
  - superscripts:
    - OA
    name: mind thrust II
    source: default
    freq: At will
    DC: 16
  - superscripts:
    - OA
    name: synesthesia
    source: default
    freq: At will
    DC: 17
  - superscripts:
    - OA
    name: telekinetic projectile
    source: default
    freq: At will
  sources:
  - name: default
    CL: 10
    concentration: 14
psychic_magic:
  entries:
  - superscripts:
    - OA
    name: mind thrust III
    PE: 3
    DC: 17
  - superscripts:
    - OA
    name: synaptic pulse
    PE: 3
    DC: 17
  sources:
  - name: default
    CL: 10
    concentration: 14
  PE: 9
ability_scores:
  STR: 4
  DEX: 19
  CON: 18
  INT: 15
  WIS: 22
  CHA: 19
BAB: 7
CMB: 9
CMD: 22
CMD_other: can't be tripped
feats:
- name: Defensive Combat Training
- name: Dodge
- name: Great Fortitude
- name: Iron Will
- name: Weapon Finesse
skills:
  Bluff: 14
  Diplomacy: 6
  Fly: 20
  Perception: 16
  Sense Motive: 16
  Stealth: 15
languages:
- Aklo (can't speak)
- Common (can't speak)
- telepathy 100 ft.
ecology:
  environment: any ruins or underground
  organization: solitary, pair, flight (3-6), or colony (7-12)
  treasure_type: incidental
special_abilities:
  Brain Static (Su): While within 30 feet of a cerebric cyst, creatures take a -2
    penalty on all saves against the cerebric cyst's attacks, spells, and other abilities.
    This is a mindaffecting effect.
  Empowering Strike (Su): When a cerebric cyst hits a target creature with a tentacle
    attack, after resolving the damage it can, as a swift action, use one of its spell-like
    abilities without provoking attacks of opportunity.
  Prescience (Su): A cerebric cyst's limited precognitive ability grants it a +2 insight
    bonus on initiative checks, on Reflex saves, and to Armor Class. Cerebric cysts
    are never surprised or flat-footed.
  Psychic Sting (Su): Creatures hit by a cerebric cyst's tentacle must succeed at
    a DC 19 Fortitude saving throw or take 1d6 points of Intelligence damage. When
    a cerebric cyst deals Intelligence damage, it regains 1d6 hit points. This attack
    deals twice as much Intelligence damage and heals the cerebric cyst of twice as
    much damage if the victim can cast psychic spells (including by virtue of possessing
    the psychic magic universal monster ability) or has the Psychic Sensitivity feat.
    The save DC is Constitution-based.
desc_long: |-
  While a typical brain ooze is content with feeding on and subjugating the minds of lesser beings, cerebric cysts focus on a higher prize. Only the minds of psychic beings sate the vile and cruel hunger of these creatures. Cerebric cysts often manifest greater number of aggressive abilities than their brain ooze cousins, stunning and weakening their quarries' mental defenses before draining their victims' precious intellectual energy through their ectoplasmic tentacles.

  A cerebric cyst is willing to devour the power of non-psychic beings, but it gains only minor satisfaction from their mental energy. Psychic creatures, however, are a true delicacy, and cerebric cysts occasionally establish facades such as fake schools for gifted children in order to lure such pliable chattel to them and thus avoid the need for arduous hunts for psychic sensitives.

---

# Cerebric Cyst
This floating, purple brain has occult sigils glowing on its surface and tentacles made of ectoplasm.
**Source** Occult Bestiary pg. 13
**XP** 3,200

NE Tiny ooze
**Init** +6; **Senses** _[[universal monster rules/Thoughtsense|thoughtsense]]_ 30 ft., Perception +16
**Aura** brain static (30 ft.), mental static (30 ft., DC 19)

##### Defense

**AC** 19, touch 19, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 Dex, +1 dodge, +2 insight, +2 size)
**hp** 85 (10d8+40)
**Fort** +9, **Ref** +9, **Will** +11
**Defensive Abilities** evasion, prescience; **Immune** ooze traits

##### Offense
**Speed** 30 ft., fly 60 ft. (good)
**Melee** 2 tentacles +13 (2d6 electricity plus empowering strike and _[[classes/Psychic|psychic]]_ sting)
**Space** 2-1/2 ft., **Reach** 0 ft.
**Special Attacks** empowering strike, _psychic_ sting
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
Constant—_[[spells/Enshroud Thoughts|enshroud thoughts]]_
At will—_[[spells/Charm Monster|charm monster]]_ (DC 18), _[[spells/Dominate Person|dominate person]]_ (DC 19), _[[spells/Mind Thrust II|mind thrust II]]_ (DC 16), _[[spells/Synesthesia|synesthesia]]_ (DC 17), _[[spells/Telekinetic Projectile|telekinetic projectile]]_
**_[[universal monster rules/Psychic Magic|Psychic Magic]]_ **(CL 10th; concentration +14)
9 PE—_[[spells/Mind Thrust III|mind thrust III]]_ (3 PE, DC 17), _[[spells/Synaptic Pulse|synaptic pulse]]_ (3 PE, DC 17)

##### Statistics
**Str** 4, **Dex** 19, **Con** 18, **Int** 15, **Wis** 22, **Cha** 19
**Base Atk** +7; **CMB** +9; **CMD** 22 (can’t be tripped)
**Feats** _[[feats/Defensive Combat Training|Defensive Combat Training]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +14, Diplomacy +6, Fly +20, Perception +16, Sense Motive +16, Stealth +15
**Languages** Aklo (can’t speak), Common (can’t speak); _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any ruins or underground
**Organization** solitary, pair, _[[universal monster rules/Flight|flight]]_ (3–6), or colony (7–12)
**Treasure** incidental

### Special Abilities

**Brain Static (Su)** While within 30 feet of a _[[monsters/Cerebric Cyst|cerebric cyst]]_, creatures take a –2 penalty on all saves against the _cerebric cyst_’s attacks, spells, and other abilities. This is a mindaffecting effect.

**Empowering Strike (Su)** When a _cerebric cyst_ hits a target creature with a tentacle attack, after resolving the damage it can, as a swift action, use one of its _spell-like abilities_ without provoking attacks of opportunity.

**Prescience (Su)** A _cerebric cyst_’s limited precognitive ability grants it a +2 insight bonus on initiative checks, on Reflex saves, and to Armor Class. Cerebric cysts are never surprised or _flat-footed_.

**_Psychic_ Sting (Su)** Creatures hit by a _cerebric cyst_’s tentacle must succeed at a DC 19 Fortitude saving throw or take 1d6 points of Intelligence damage. When a _cerebric cyst_ deals Intelligence damage, it regains 1d6 hit points. This attack deals twice as much Intelligence damage and heals the _cerebric cyst_ of twice as much damage if the victim can cast _psychic_ spells (including by _[[spells/Virtue|virtue]]_ of possessing the _psychic magic_ universal monster ability) or has the _[[feats/Psychic Sensitivity|Psychic Sensitivity]]_ feat. The save DC is Constitution-based.

##### Description

While a typical _[[monsters/Brain Ooze|brain ooze]]_ is content with feeding on and subjugating the minds of lesser beings, cerebric cysts focus on a higher prize. Only the minds of _psychic_ beings sate the vile and _[[items/Weapon Magic Abilities/Cruel|cruel]]_ hunger of these creatures. Cerebric cysts often manifest greater number of aggressive abilities than their _brain ooze_ cousins, stunning and weakening their quarries’ mental defenses before draining their victims’ precious intellectual energy through their ectoplasmic tentacles.

A _cerebric cyst_ is willing to devour the power of non-psychic beings, but it gains only minor satisfaction from their mental energy. _Psychic_ creatures, however, are a true delicacy, and cerebric cysts occasionally establish facades such as fake schools for gifted children in order to lure such pliable chattel to them and thus avoid the need for arduous hunts for _psychic_ sensitives.