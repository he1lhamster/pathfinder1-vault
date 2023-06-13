---
cssclass: [monsters]
title1: Seeded Creature, Seeded Lamia
desc_short: This creature's lower body is that of a decaying lion, while its upper
  torso is that of a woman with ropey fungus for hair. A web of grotesque fibers sprouts
  from its body.
title2: Seeded Lamia
CR: 7
sources:
- name: 'Pathfinder #113: What Grows Within'
  page: 90
  link: http://paizo.com/products/btpy9qcl?Pathfinder-Adventure-Path-113-What-Grows-Within
XP: 3200
alignment: NE
size: Large
type: undead
subtypes:
- augmented monstrous humanoid
initiative:
  bonus: 3
senses:
  darkvision: 60
  low-light vision: true
AC:
  AC: 22
  touch: 13
  flat_footed: 18
  components:
    dex: 3
    dodge: 1
    natural: 9
    size: -1
HP:
  HP: 67
  long: 9d8+27
  fast_healing: 5
saves:
  fort: 8
  ref: 9
  will: 12
  other: +4 vs. mind-affecting effects
defensive_abilities:
- channel resistance +4
DR:
- amount: 5
  weakness: bludgeoning or slashing
resistances:
  cold: 10
  electricity: 10
weaknesses:
- transformed
speeds:
  base: 60
  climb: 60
attacks:
  melee:
  - - text: +1 dagger +15/+10 (1d4+7/19-20)
      entries:
      - - damage: 1d4+7
          crit_range: 19-20
      attack: +1 dagger
      bonus:
      - 15
      - 10
    - text: +9 touch (1d4 Wisdom drain plus seedborne consumption)
      entries:
      - - damage: 1d4
          type: Wisdom drain
        - effect: seedborne consumption
      attack: touch
      bonus:
      - 9
      touch: true
    - text: 2 claws +9 (1d4+3 plus seedborne consumption)
      entries:
      - - damage: 1d4+3
        - effect: seedborne consumption
      count: 2
      attack: claws
      bonus:
      - 9
    - text: 2 tendrils +9 (1d8+3 plus grab and seedborne consumption)
      entries:
      - - damage: 1d8+3
        - effect: grab
        - effect: seedborne consumption
      count: 2
      attack: tendrils
      bonus:
      - 9
  special:
  - death burst
  - entrapping tendrils
  - seedborne consumption (DC 17)
  - insidious mind
  - Wisdom drain
space: 10
reach: 5
reach_other: 10 ft. with tendrils
spell_like_abilities:
  entries:
  - name: disguise self
    source: default
    freq: At will
  - name: ventriloquism
    source: default
    freq: At will
    DC: 14
  - name: charm monster
    source: default
    freq: 3/day
    DC: 17
  - name: major image
    source: default
    freq: 3/day
    DC: 16
  - name: mirror image
    source: default
    freq: 3/day
  - name: suggestion
    source: default
    freq: 3/day
    DC: 16
  - name: deep slumber
    source: default
    freq: 1/day
    DC: 16
  sources:
  - name: default
    CL: 9
    concentration: 12
ability_scores:
  STR: 22
  DEX: 16
  CON:
  INT: 12
  WIS: 18
  CHA: 16
BAB: 9
CMB: 16
CMD: 30
CMD_other: 34 vs. trip
feats:
- name: Dodge
- name: Great Fortitude
- name: Iron Will
- name: Mobility
- name: Spring Attack
skills:
  Acrobatics: 3
    when jumping: 15
  Bluff: 11
  Climb: 14
  Diplomacy: 6
  Disguise: 8
  Intimidate: 12
  Knowledge (religion): 4
  Perception: 16
  Stealth: 15
  Survival: 13
  _racial_mods:
    Bluff:
      _: 4
    Stealth:
      _: 4
languages:
- Abyssal
- Common
- telepathy 100 ft. (seeded creatures only)
special_qualities:
- undersized weapons
ecology:
  environment: temperate deserts
  organization: solitary, pair, or cult (3-12)
  treasure_type: double
  treasure:
  - +1 dagger
  - other treasure
special_abilities:
  Undersized Weapons (Ex): Although a lamia is Large, its upper torso is the same
    size as that of a Medium humanoid. As a result, lamias wield weapons as if they
    were one size category smaller than their actual size.
  Wisdom Drain (Su): A lamia drains 1d4 points of Wisdom each time it hits with its
    melee touch attack (unlike with other kinds of ability drain attacks, a lamia
    doesn't regain hit points when it uses its Wisdom drain). Lamias try to use this
    power early in an encounter to make foes more susceptible to charm monster and
    suggestion.
desc_long: |-
  Though the Great Old One Xhamen-Dor lies halfdormant where its bloated body crashed millennia ago, virtually nothing can prevent it from seeking new hosts to infect. The most common means by which one might contract this infestation is through nightmares that brush against Xhamen-Dor's influence in the Dimension of Dreams, after which the Inmost Blot can track victims and infest their thoughts, slowly and painfully driving them mad. Less common is direct exposure to one of the Great Old One's vine-choked thralls: the seeded.

  Xhamen-Dor feeds upon a victim's force of personality, and as a result, only a select few who meet its inscrutable criteria are even able to contract the seedborne consumption disease that turns one into a seeded. Those infected first become sickly and withdrawn. Weeks later, the germinating evil within begins sending fibrous feelers throughout the victim's body. When the host finally slips into a catatonic coma, these fibers quickly digest the organs and portions of the flesh before animating the corpse from within like a puppet. Most victims maintain painful recollections of their former lives, yet they are driven to hear and obey the commands of Xhamen-Dor and find new victims to spread their plague.

---

# Seeded Creature, Seeded Lamia
This creature’s lower body is that of a decaying _[[monsters/Lion|lion]]_, while its upper torso is that of a woman with ropey fungus for hair. A web of grotesque fibers sprouts from its body.
**Source** Pathfinder #113: _[[spells/What Grows Within|What Grows Within]]_ pg. 90
**XP** 3,200

NE Large undead (augmented monstrous humanoid)
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +16

##### Defense

**AC** 22, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+3 Dex, +1 dodge, +9 natural, –1 size)
**hp** 67 (9d8+27); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +8, **Ref** +9, **Will** +12; +4 vs. mind-affecting effects
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 5/bludgeoning or slashing; **Resist** cold 10, electricity 10
**Weaknesses** transformed

##### Offense
**Speed** 60 ft., _[[universal monster rules/Climb|climb]]_ 60 ft.
**Melee** +1 _[[items/Weapon/Dagger|dagger]]_ +15/+10 (1d4+7/19–20), +9 touch (1d4 Wisdom drain plus seedborne _[[feats/Consumption|consumption]]_), 2 claws +9 (1d4+3 plus seedborne _consumption_), 2 tendrils +9 (1d8+3 plus _[[universal monster rules/Grab|grab]]_ and seedborne _consumption_)
**Space** 10 ft., **Reach** 5 ft. (10 ft. with tendrils)
**Special Attacks** death burst, entrapping tendrils, seedborne _consumption_ (DC 17), insidious mind, Wisdom drain
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +12)
At will—_[[spells/Disguise Self|disguise self]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 14)
3/day—_[[spells/Charm Monster|charm monster]]_ (DC 17), _[[spells/Major Image|major image]]_ (DC 16), _[[spells/Mirror Image|mirror image]]_, _[[spells/Suggestion|suggestion]]_ (DC 16)
1/day—_[[spells/Deep Slumber|deep slumber]]_ (DC 16)

##### Statistics
**Str** 22, **Dex** 16, **Con** —, **Int** 12, **Wis** 18, **Cha** 16
**Base Atk** +9; **CMB** +16; **CMD** 30 (34 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spring Attack|Spring Attack]]_
**Skills** Acrobatics +3 (+15 when jumping), Bluff +11, _Climb_ +14, Diplomacy +6, Disguise +8, Intimidate +12, Knowledge (religion) +4, Perception +16, Stealth +15, Survival +13; **Racial Modifiers** +4 Bluff, +4 Stealth
**Languages** Abyssal, Common; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft. (seeded creatures only)
**SQ** _[[universal monster rules/Undersized Weapons|undersized weapons]]_

##### Ecology

**Environment** temperate deserts
**Organization** solitary, pair, or cult (3–12)
**Treasure** double (+1 _dagger_, other treasure)

### Special Abilities

**_Undersized Weapons_ (Ex)** Although a _[[monsters/Lamia|lamia]]_ is Large, its upper torso is the same size as that of a _[[classes/Medium|Medium]]_ humanoid. As a result, lamias wield weapons as if they were one size category smaller than their actual size.

**Wisdom Drain (Su)** A _lamia_ drains 1d4 points of Wisdom each time it hits with its melee touch attack (unlike with other kinds of ability drain attacks, a _lamia_ doesn’t regain hit points when it uses its Wisdom drain). Lamias try to use this power early in an encounter to make foes more susceptible to _charm monster_ and _suggestion_.

##### Description

Though the Great Old One Xhamen-Dor lies halfdormant where its bloated body crashed millennia ago, virtually nothing can prevent it from seeking new hosts to infect. The most common means by which one might contract this infestation is through nightmares that brush against Xhamen-Dor’s influence in the Dimension of Dreams, after which the Inmost _[[spells/Blot|Blot]]_ can track victims and infest their thoughts, slowly and painfully driving them mad. Less common is direct exposure to one of the Great Old One’s vine-choked thralls: the seeded.

Xhamen-Dor feeds upon a victim’s force of personality, and as a result, only a select few who meet its inscrutable criteria are even able to contract the seedborne _consumption_ disease that turns one into a seeded. Those infected first become sickly and withdrawn. Weeks later, the germinating evil within begins _[[spells/Sending|sending]]_ fibrous feelers throughout the victim’s body. When the host finally slips into a catatonic coma, these fibers quickly digest the organs and portions of the flesh before animating the corpse from within like a puppet. Most victims maintain painful recollections of their former lives, yet they are driven to hear and obey the commands of Xhamen-Dor and find new victims to spread their plague.