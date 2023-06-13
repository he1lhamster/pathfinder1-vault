---
cssclass: [monsters]
title1: Impundulu
desc_short: A dark shadow moves rapidly across the ground. In the skies high above,
  silhouetted by the sun, a monstrous, black-feathered avian creature circles. Slowly,
  a supernatural wind begins to swirl about the creature, and crackling sparks erupt
  from its body. Screeching wildly, it descends as if falling from the sky, its blood-f
  lecked wings tipped with cruel curved hooks, and its protruding lower beak scalloped
  with vicious, jagged barbs.
title2: Impundulu
CR: 11
sources:
- name: 'Pathfinder #40: Vaults of Madness'
  page: 80
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/serpentsSkull/v5748btpy8i1u
XP: 12800
alignment: NE
size: Medium
type: outsider
subtypes:
- evil
- extraplanar
- shapechanger
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 25
  touch: 15
  flat_footed: 20
  components:
    dex: 5
    natural: 10
HP:
  HP: 133
  long: 14d10+56
saves:
  fort: 13
  ref: 14
  will: 10
DR:
- amount: 10
  weakness: magic and cold iron
immunities:
- electricity
resistances:
  cold: 10
  fire: 10
SR: 22
speeds:
  base: 20
  base_other: 30 ft. in humanoid form
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: bite +19 (1d6+4 plus 1d6 bleed and 1d6 electricity)
      entries:
      - - damage: 1d6+4
        - damage: 1d6
          type: bleed
        - damage: 1d6
          type: electricity
      attack: bite
      bonus:
      - 19
    - text: 2 talons +19 (1d4+4 plus 1d6 electricity and grab)
      entries:
      - - damage: 1d4+4
        - damage: 1d6
          type: electricity
        - effect: grab
      count: 2
      attack: talons
      bonus:
      - 19
    - text: 2 hook +13 (1d4+2 plus 1d6 electricity)
      entries:
      - - damage: 1d4+2
        - damage: 1d6
          type: electricity
      count: 2
      attack: hook
      bonus:
      - 13
  special:
  - bleed (1d6)
  - breath weapon (60-ft. line, 8d6 electricity, Reflex DC 21 half, usable every 1d4
    rounds)
  - electrical discharge
spell_like_abilities:
  entries:
  - name: call lightning
    source: default
    freq: 3/day
  - name: charm person
    source: default
    freq: 3/day
  - name: gust of wind
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 14
    concentration: 19
ability_scores:
  STR: 18
  DEX: 21
  CON: 19
  INT: 15
  WIS: 18
  CHA: 20
BAB: 14
CMB: 18
CMB_other: +22 grapple
CMD: 33
feats:
- name: Flyby Attack
- name: Hover
- name: Improved Initiative
- name: Iron Will
- name: Vital Strike
- name: Weapon Focus (bite)
- name: Weapon Focus (talons)
skills:
  Bluff: 22
  Diplomacy: 19
  Fly: 9
  Intimidate: 15
  Knowledge (arcana): 12
  Knowledge (nature): 12
  Knowledge (planes): 12
  Perception: 21
  Sense Motive: 21
  Spellcraft: 19
  Stealth: 22
languages:
- Abyssal
- Common
- Fey
- Infernal
- Polyglot
- speak with animals
- telepathy 100 ft.
special_qualities:
- change shape (one humanoid)
- shaman form
ecology:
  environment: temperate or warm forest
  organization: solitary, pair, or flock (2d6)
  treasure_type: standard
  treasure:
  - and impundulu fat
  - see sidebar
special_abilities:
  Blood Drain (Ex): If it grapples a foe, an impundulu drains blood at the end of
    its turn, dealing Constitution damage.
  Electrical Discharge (Su): An impundulu builds substantial electrical charges in
    its body-electrical charges visibly crackle about its form. If the impundulu hits
    a creature with two talons in the same round, this charge releases into that creature,
    dealing 4d6 points of electricity damage (this damage is in addition to the electricity
    damage from its talon attacks). The target may attempt a DC 21 Fortitude save
    for half damage. If one or both of the talon attacks is a critical hit, the jolt
    is so potent that the target is stunned for 1d4 rounds (creatures that are immune
    to electricity are immune to this stunning effect). The save DC is Constitution-based.
    Once the creature releases this charge, it cannot use this ability again for 1d4
    rounds while it waits for the energy to build again (though this energy buildup
    does not affect the electrical damage from its regular talon attacks).
  Familiar Service: A mortal of 7th level or higher with the Improved Familiar feat
    can summon an impundulu to serve as her familiar; an impundulu familiar appears
    as a birdlike imp or quasit, has the normal statistics of an imp or quasit, and
    loses all of its own abilities except its subtypes, alignment, and damage reduction.
    If its master is slain, the impundulu seizes its former master's soul, retreats
    to a hidden place, and consumes the soul, after which it metamorphoses over the
    next 24 hours into its natural form, regains all of its normal abilities, and
    becomes free; most aging masters pass on their impundulu familiars to younger
    family members rather than let the creatures turn on them.
  Shaman Form (Su): An impundulu using its change shape special quality can take on
    one specific humanoid form as if it had the change shape ability. This form usually
    resembles that of a jungle shaman, except it has claw-like fingernails and its
    feet end in talons. In this form, it cannot fly or use its breath weapon, electrical
    discharge, or hook attacks. An impundulu can remain in this form indefinitely.
    Its natural form is its bird form. If killed, it reverts to its true form.
  Witchcraft: 'An impundulu serving as a witch's familiar gives its master additional
    spells known, just like a witch's patron. The master must choose from one of the
    following patron themes when binding the impundulu, and this choice cannot be
    changed without dismissing and re-summoning the impundulu: Agility, Elements,
    or Transformation. These patron spells known are in addition to any granted by
    the witch's actual patron.'
desc_long: The tribesfolk of southern Garund tell tales of a ruthless winged shapeshifter,
  a bloodthirsty demon and hunter of men. They call this being impundulu, a name that
  loosely translates to “lightning-bird” after its savage avian form. Legend describes
  this creature as a huge, stork-like bird that rides upon fierce storms and whose
  dark feathers crackle with lightning. It is believed that an evil shaman summoned
  the first impundulu and that using an ancient, taboo ritual, the two formed a blood
  pact. The shaman offered the impundulu the ability to wear his mortal f lesh in
  exchange for mastery over the demon's significant occult powers. As soon as the
  impundulu seized control of the shaman's body, it broke the pact- however, the ancient
  ritual bound the fiend to the mortal form, and even after the shaman perished, it
  could not shed its f lesh. Thus despite its own immortality, the impundulu became
  forever tied to the realm of mortals. For this reason, it is said, the creature
  continues to forge pacts with mortal spellcasters in the hope that one day it will
  unbind the secrets of its cursed existence.

---

# Impundulu
A dark _[[items/Armor Magic Abilities/Shadow|shadow]]_ moves rapidly across the ground. In the skies high above, silhouetted by the sun, a monstrous, black-feathered avian creature circles. Slowly, a supernatural wind begins to swirl about the creature, and crackling sparks erupt from its body. Screeching wildly, it descends as if falling from the sky, its blood-f lecked wings tipped with _[[items/Weapon Magic Abilities/Cruel|cruel]]_ curved hooks, and its protruding lower beak scalloped with _[[items/Weapon Magic Abilities/Vicious|vicious]]_, jagged barbs.
**Source** Pathfinder #40: Vaults of Madness pg. 80
**XP** 12,800

NE Medium outsider (evil, extraplanar, shapechanger)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +21

##### Defense

**AC** 25, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+5 Dex, +10 natural)
**hp** 133 (14d10+56)
**Fort** +13, **Ref** +14, **Will** +10
**DR** 10/magic and cold iron; **Immune** electricity; **Resist** cold 10, fire 10; **SR** 22

##### Offense
**Speed** 20 ft. (30 ft. in humanoid form), fly 60 ft. (good)
**Melee** bite +19 (1d6+4 plus 1d6 _[[universal monster rules/Bleed|bleed]]_ and 1d6 electricity), 2 talons +19 (1d4+4 plus 1d6 electricity and _[[universal monster rules/Grab|grab]]_), 2 hook +13 (1d4+2 plus 1d6 electricity)
**Special Attacks** _bleed_ (1d6), _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. line, 8d6 electricity, Reflex DC 21 half, usable every 1d4 rounds), electrical _[[spells/Discharge|discharge]]_
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +19)
3/day - _[[spells/Call Lightning|call lightning]]_, _[[spells/Charm Person|charm person]]_, _[[spells/Gust Of Wind|gust of wind]]_

##### Statistics
**Str** 18, **Dex** 21, **Con** 19, **Int** 15, **Wis** 18, **Cha** 20
**Base Atk** +14; **CMB** +18 (+22 grapple); **CMD** 33
**Feats** _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite), _Weapon Focus_ (talons)
**Skills** Bluff +22, Diplomacy +19, Fly +9, Intimidate +15, Knowledge (arcana) +12, Knowledge (nature) +12, Knowledge (planes) +12, Perception +21, Sense Motive +21, Spellcraft +19, Stealth +22
**Languages** Abyssal, Common, Fey, Infernal, Polyglot; _[[spells/Speak with Animals|speak with animals]]_, _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (one humanoid), _[[classes/Shaman|shaman]]_ form

##### Ecology

**Environment** temperate or warm forest
**Organization** solitary, pair, or flock (2d6)
**Treasure** standard (and _[[monsters/Impundulu|impundulu]]_ fat, see sidebar)

### Special Abilities

**_[[universal monster rules/Blood Drain|Blood Drain]]_ (Ex)** If it grapples a foe, an _impundulu_ drains blood at the end of its turn, dealing Constitution damage.

**Electrical _Discharge_ (Su)** An _impundulu_ builds substantial electrical charges in its body—electrical charges visibly crackle about its form. If the _impundulu_ hits a creature with two talons in the same round, this charge releases into that creature, dealing 4d6 points of electricity damage (this damage is in addition to the electricity damage from its talon attacks). The target may attempt a DC 21 Fortitude save for half damage. If one or both of the talon attacks is a critical hit, the _[[spells/Jolt|jolt]]_ is so _[[items/Weapon Magic Abilities/Potent|potent]]_ that the target is _[[conditions/Stunned|stunned]]_ for 1d4 rounds (creatures that are immune to electricity are immune to this stunning effect). The save DC is Constitution-based. Once the creature releases this charge, it cannot use this ability again for 1d4 rounds while it waits for the energy to build again (though this energy buildup does not affect the electrical damage from its regular talon attacks).

**Familiar Service** A mortal of 7th level or higher with the _[[feats/Improved Familiar|Improved Familiar]]_ feat can _[[universal monster rules/Summon|summon]]_ an _impundulu_ to serve as her familiar; an _impundulu_ familiar appears as a birdlike imp or quasit, has the normal statistics of an imp or quasit, and loses all of its own abilities except its subtypes, alignment, and _[[universal monster rules/Damage Reduction|damage reduction]]_. If its master is slain, the _impundulu_ seizes its former master’s soul, retreats to a hidden place, and consumes the soul, after which it metamorphoses over the next 24 hours into its natural form, regains all of its normal abilities, and becomes free; most aging masters pass on their _impundulu_ familiars to younger family members rather than let the creatures turn on them.
**_Shaman_ Form (Su)** An _impundulu_ using its _change shape_ special quality can take on one specific humanoid form as if it had the _change shape_ ability. This form usually resembles that of a jungle _shaman_, except it has claw-like fingernails and its feet end in talons. In this form, it cannot fly or use its _breath weapon_, electrical _discharge_, or hook attacks. An _impundulu_ can remain in this form indefinitely. Its natural form is its bird form. If killed, it reverts to its _[[spells/True Form|true form]]_.

**Witchcraft** An _impundulu_ serving as a _[[classes/Witch|witch]]_’s familiar gives its master additional spells known, just like a _witch_’s patron. The master must choose from one of the following patron themes when _[[spells/Binding|binding]]_ the _impundulu_, and this choice cannot be changed without dismissing and re-summoning the _impundulu_: Agility, Elements, or _[[spells/Transformation|Transformation]]_. These patron spells known are in addition to any granted by the _witch_’s actual patron.

##### Description

The tribesfolk of southern Garund tell tales of a ruthless winged shapeshifter, a _[[items/Armor Magic Abilities/Bloodthirsty|bloodthirsty]]_ demon and _[[classes/Hunter|hunter]]_ of men. They call this being _impundulu_, a name that loosely translates to “lightning-bird” after its savage avian form. Legend describes this creature as a huge, stork-like bird that rides upon fierce storms and whose dark feathers crackle with lightning. It is believed that an evil _shaman_ summoned the first _impundulu_ and that using an ancient, taboo ritual, the two formed a blood pact. The _shaman_ offered the _impundulu_ the ability to wear his mortal f lesh in exchange for mastery over the demon’s significant occult powers. As soon as the _impundulu_ seized control of the _shaman_’s body, it broke the pact— however, the ancient ritual bound the fiend to the mortal form, and even after the _shaman_ perished, it could not shed its f lesh. Thus despite its own immortality, the _impundulu_ became forever tied to the realm of mortals. For this reason, it is said, the creature continues to forge pacts with mortal spellcasters in the hope that one day it will unbind the secrets of its cursed existence.