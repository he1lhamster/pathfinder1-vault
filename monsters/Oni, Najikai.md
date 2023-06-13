---
cssclass: [monsters]
title1: Oni, Najikai
desc_short: This scaly-skinned humanoid has long venomous fangs, claws, and unblinking
  reptilian eyes.
title2: Najikai
CR: 8
sources:
- name: Book of the Damned
  page: 250
  link: http://paizo.com/products/btpy9tok
XP: 4800
alignment: LE
size: Large
type: outsider
subtypes:
- native
- oni
- reptilian
- shapechanger
initiative:
  bonus: 9
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 22
  touch: 15
  flat_footed: 16
  components:
    dex: 5
    dodge: 1
    natural: 7
    size: -1
HP:
  HP: 105
  long: 10d10+50
  regeneration: 5
  regeneration_weakness: cold, fire
saves:
  fort: 8
  ref: 12
  will: 11
immunities:
- acid
- poison
SR: 19
weaknesses:
- vulnerable to cold
speeds:
  base: 40
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 spiked chain +15/+10 (2d6+8)
      entries:
      - - damage: 2d6+8
      attack: +1 spiked chain
      bonus:
      - 15
      - 10
    - text: bite +9 (1d6+2 plus poison)
      entries:
      - - damage: 1d6+2
        - effect: poison
      attack: bite
      bonus:
      - 9
  special:
  - ripping spikes
  - sudden shed
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: command
    source: default
    freq: At will
    DC: 14
  - name: darkness
    source: default
    freq: At will
  - name: invisibility
    source: default
    freq: At will
    other: self only
  - name: charm monster
    source: default
    freq: 3/day
    DC: 17
  - name: cloudkill
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 8
    concentration: 11
ability_scores:
  STR: 20
  DEX: 20
  CON: 20
  INT: 18
  WIS: 19
  CHA: 17
BAB: 10
CMB: 16
CMD: 32
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Dodge
- name: Improved Initiative
- name: Mobility
skills:
  Bluff: 16
  Disguise: 13
  Fly: 24
  Knowledge (arcana): 17
  Knowledge (local): 17
  Perception: 17
  Sense Motive: 17
  Spellcraft: 17
  Stealth: 14
  Use Magic Device: 16
languages:
- Common
- Draconic
- Nagaji
special_qualities:
- change shape (nagaji
- alter self
ecology:
  environment: warm forests or mountains
  organization: solitary, pair, or band (3-8)
  treasure_type: standard
  treasure:
  - +1 spike chain
  - other treasure
special_abilities:
  Poison (Ex): Bite or spit-injury or contact; save Fort DC 20; frequency 1/round
    for 6 rounds; effect 1d2 Str damage; cure 2 consecutive saves. The save DC is
    Constitution-based.
  Ripping Spikes (Su): The second time in a round it hits the same foe with a spiked
    chain attack (but no more than once per round), the najikai deals 1d4 points of
    bleed damage.
  Sudden Shed (Su): Once per day as a swift action while in nagaji form, a najikai
    can slough its skin to the ground and revert to its hideous true self. Any creature
    within 30 feet that can see the oni must succeed at a DC 18 Will save or be nauseated
    for 1d4 rounds at this sight. A creature that successfully saves is only staggered
    for 1 round. This is a mind-affecting, vision-based effect. The save DC is Charisma-based.
desc_long: Like all oni, najikai crave power and luxury. A najikai will often infiltrate
  a nagaji settlement, posing as a mighty warrior and easily cowing the people, with
  the ultimate goal of replacing the settlement's naga ruler. The oni gets the naga's
  attention with shows of strength and cunning, soon earning the najikai a position
  of direct service to the ruler. The oni pretends deference, but destroys the naga
  the instant its defenses slip, replacing it as a tyrant over the now-disgraced nagaji
  who failed their leader.

---

# Oni, Najikai
This scaly-skinned humanoid has long venomous fangs, claws, and unblinking reptilian eyes.
**Source** _[[items/Wondrous Item/Book of the Damned|Book of the Damned]]_ pg. 250
**XP** 4,800

LE Large outsider (native, oni, reptilian, shapechanger)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +17

##### Defense

**AC** 22, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+5 Dex, +1 dodge, +7 natural, -1 size)
**hp** 105 (10d10+50); _[[universal monster rules/Regeneration|regeneration]]_ 5 (cold, fire)
**Fort** +8, **Ref** +12, **Will** +11
**Immune** acid, poison; **SR** 19
**Weaknesses** vulnerable to cold

##### Offense
**Speed** 40 ft., fly 60 ft. (good)
**Melee** +1 _[[items/Weapon/Spiked chain|spiked chain]]_ +15/+10 (2d6+8), bite +9 (1d6+2 plus poison)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** ripping spikes, sudden shed
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +11)
Constant—fly
 At will—_[[spells/Command|command]]_ (DC 14), _[[spells/Darkness|darkness]]_, _[[spells/Invisibility|invisibility]]_ (self only)
 3/day—_[[spells/Charm Monster|charm monster]]_ (DC 17)
 1/day—_[[spells/Cloudkill|cloudkill]]_ (DC 18)

##### Statistics
**Str** 20, **Dex** 20, **Con** 20, **Int** 18, **Wis** 19, **Cha** 17
**Base Atk** +10; **CMB** +16; **CMD** 32
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_
**Skills** Bluff +16, Disguise +13, Fly +24, Knowledge (arcana, local) +17, Perception +17, Sense Motive +17, Spellcraft +17, Stealth +14, Use Magic Device +16
**Languages** Common, Draconic, _[[monsters/Nagaji|Nagaji]]_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (_nagaji_, _[[spells/Alter Self|alter self]]_

##### Ecology

**Environment** warm forests or mountains
**Organization** solitary, pair, or band (3-8)
**Treasure** standard (+1 spike chain, other treasure)

### Special Abilities

**Poison (Ex)** Bite or spit—injury or contact; save Fort DC 20; frequency 1/round for 6 rounds; effect 1d2 Str damage; cure 2 consecutive saves. The save DC is Constitution-based.

**Ripping Spikes (Su)** The second time in a round it hits the same foe with a _spiked chain_ attack (but no more than once per round), the najikai deals 1d4 points of _[[universal monster rules/Bleed|bleed]]_ damage.
**Sudden Shed (Su)** Once per day as a swift action while in _nagaji_ form, a najikai can _[[spells/Slough|slough]]_ its skin to the ground and revert to its hideous true self. Any creature within 30 feet that can see the oni must succeed at a DC 18 Will save or be _[[conditions/Nauseated|nauseated]]_ for 1d4 rounds at this sight. A creature that successfully saves is only _[[conditions/Staggered|staggered]]_ for 1 round. This is a mind-affecting, vision-based effect. The save DC is Charisma-based.

##### Description

Like all _[[monsters/Oni, Najikai|oni, najikai]]_ crave power and luxury. A najikai will often infiltrate a _nagaji_ settlement, posing as a mighty warrior and easily cowing the people, with the ultimate goal of replacing the settlement’s naga ruler. The oni gets the naga’s attention with shows of strength and _[[items/Weapon Magic Abilities/Cunning|cunning]]_, soon earning the najikai a position of direct service to the ruler. The oni pretends deference, but destroys the naga the instant its defenses slip, replacing it as a tyrant over the now-disgraced _nagaji_ who failed their leader.