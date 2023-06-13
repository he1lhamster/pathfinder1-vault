---
cssclass: [monsters]
title1: Svartalfar
desc_short: This hairless, black-skinned elf like creature has an expressionless face
  and wields an eerie ebon sword.
title2: Svartalfar
CR: 8
sources:
- name: Bestiary 4
  page: 256
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 4800
alignment: LE
size: Medium
type: fey
subtypes:
- extraplanar
initiative:
  bonus: 5
senses:
  darkvision: 120
  low-light vision: true
AC:
  AC: 20
  touch: 15
  flat_footed: 15
  components:
    dex: 5
    natural: 5
HP:
  HP: 84
  long: 13d6+39
saves:
  fort: 6
  ref: 13
  will: 12
DR:
- amount: 10
  weakness: cold iron
resistances:
  cold: 10
  electricity: 10
SR: 19
weaknesses:
- light blindness
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 longsword +9/+6 (1d8+4/19-20)
      entries:
      - - damage: 1d8+4
          crit_range: 19-20
      attack: +1 longsword
      bonus:
      - 9
      - 6
  special:
  - bane
  - quickened spell strike
  - sneak attack +3d6
spell_like_abilities:
  entries:
  - name: chill touch
    source: default
    freq: At will
    DC: 16
  - superscripts:
    - UM
    name: corrosive touch
    source: default
    freq: At will
  - superscripts:
    - UM
    name: frigid touch
    source: default
    freq: 3/day
  - superscripts:
    - UM
    name: shadow step
    source: default
    freq: 3/day
  - superscripts:
    - APG
    name: vanish
    source: default
    freq: 3/day
  - superscripts:
    - UM
    name: force punch
    source: default
    freq: 1/day
    DC: 18
  - name: greater invisibility
    source: default
    freq: 1/day
  - name: ray of exhaustion
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 13
    concentration: 18
ability_scores:
  STR: 12
  DEX: 21
  CON: 17
  INT: 18
  WIS: 14
  CHA: 21
BAB: 6
CMB: 11
CMD: 22
feats:
- name: Agile Maneuvers
- name: Combat Casting
- name: Iron Will
- name: Skill Focus (Stealth)
- name: Stealthy
- name: Vital Strike
- name: Weapon Focus (longsword)
skills:
  Acrobatics: 21
    when jumping: 25
  Bluff: 21
  Escape Artist: 25
  Intimidate: 18
  Knowledge (nature): 20
  Knowledge (planes): 17
  Perception: 18
  Sense Motive: 18
  Sleight of Hand: 21
  Stealth: 31
  _racial_mods:
    Acrobatics:
      when jumping: 4
languages:
- Aklo
- Common
- Elven
- Sylvan
ecology:
  environment: any (Shadow Plane)
  organization: solitary, pair, cabal (3-12), or clan (10-30)
  treasure_type: NPC Gear
  treasure:
  - +1 longsword
  - other treasure
special_abilities:
  Bane (Su): Once per day as a swift action, a svartalfar can imbue one of its weapons
    with the bane weapon special ability. It must select one creature type (and subtype,
    if choosing humanoid or outsider) when it uses this ability. This lasts for 1
    hour. This ability only functions while the svartalfar wields the weapon.
  Quickened Spell Strike (Su): 'Three times per day as a free action after hitting
    with a melee weapon, a svartalfar can cast and deliver one of the following of
    its spell-like abilities through the weapon: chill touch, corrosive touch, force
    punch, frigid touch, or ray of exhaustion. If the attack is a critical hit and
    the spell-like ability deals damage, it deals double damage.'
desc_long: |-
  The ancestors of the svartalfars were exiled from their primordial home for grave crimes that no fey will speak of. Fleeing to the Shadow Plane, they formed assassin clans, and now they hire their services to any who pay them. Their payment must be in secrets, bits of occult science, and obscure information to add to their huge, dark libraries in underground warrens hidden away on the Shadow Plane. Svartalfars are extremely interested in knowledge about the realm of the fey. Many fear the svartalfars are searching for a way to finally take their revenge upon those who expelled them.

  These cold, calculating killers are not swayed by whimsy or deeper passions. They pride themselves on their pitilessness and inability to be bribed or dissuaded from ending a target's life once they've been contracted to do so. Once an assassination is paid for, it's the duty of all the svartalfars of a clan or cabal to make sure it gets done. If a clan or cabal fails, another one will finish the job.

  Svartalfars seem to feel no love or real friendship. All of their actions are committed for practical reasons-political gain, procreation, or relieving boredom. Focused and utterly unyielding, they are considered by many to be the perfect killers, and their tenacity and mastery over magic and shadows are a death sentence for anyone who has been marked as their quarry.

---

# Svartalfar
This hairless, black-skinned elf like creature has an expressionless face and wields an eerie ebon sword.
**Source** Bestiary 4 pg. 256
**XP** 4,800

LE Medium fey (extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +18

##### Defense

**AC** 20, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+5 Dex, +5 natural)
**hp** 84 (13d6+39)
**Fort** +6, **Ref** +13, **Will** +12
**DR** 10/cold iron; **Resist** cold 10, electricity 10; **SR** 19
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 40 ft.
**Melee** +1 _[[items/Weapon/Longsword|longsword]]_ +9/+6 (1d8+4/19–20)
**Special Attacks** _[[spells/Bane|bane]]_, quickened spell strike, sneak attack +3d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +18)
At will—_[[spells/Chill Touch|chill touch]]_ (DC 16), _[[spells/Corrosive Touch|corrosive touch]]_
3/day—_[[spells/Frigid Touch|frigid touch]]_, _[[spells/Shadow Step|shadow step]]_, _[[spells/Vanish|vanish]]_
1/day—_[[spells/Force Punch|force punch]]_ (DC 18), greater _[[spells/Invisibility|invisibility]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 18)

##### Statistics
**Str** 12, **Dex** 21, **Con** 17, **Int** 18, **Wis** 14, **Cha** 21
**Base Atk** +6; **CMB** +11; **CMD** 22
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth), _[[feats/Stealthy|Stealthy]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_longsword_)
**Skills** Acrobatics +21 (+25 when jumping), Bluff +21, Escape Artist +25, Intimidate +18, Knowledge (nature) +20, Knowledge (planes) +17, Perception +18, Sense Motive +18, Sleight of Hand +21, Stealth +31; **Racial Modifiers** +4 Acrobatics when jumping
**Languages** Aklo, Common, Elven, Sylvan

##### Ecology

**Environment** any (_[[items/Armor Magic Abilities/Shadow|Shadow]]_ Plane)
**Organization** solitary, pair, cabal (3–12), or clan (10–30)
**Treasure** NPC gear (+1 _longsword_, other treasure)

### Special Abilities

**_Bane_ (Su)** Once per day as a swift action, a _[[monsters/Svartalfar|svartalfar]]_ can imbue one of its weapons with the _bane_ weapon special ability. It must select one creature type (and subtype, if choosing humanoid or outsider) when it uses this ability. This lasts for 1 hour. This ability only functions while the _svartalfar_ wields the weapon.

**Quickened Spell Strike (Su)** Three times per day as a free action after hitting with a melee weapon, a _svartalfar_ can cast and deliver one of the following of its _spell-like abilities_ through the weapon: _chill touch_, _corrosive touch_, _force punch_, _frigid touch_, or _ray of exhaustion_. If the attack is a critical hit and the spell-like ability deals damage, it deals double damage.

##### Description

The ancestors of the svartalfars were exiled from their primordial home for grave crimes that no fey will speak of. Fleeing to the _Shadow_ Plane, they formed assassin clans, and now they hire their services to any who pay them. Their payment must be in secrets, bits of occult science, and obscure information to add to their huge, dark libraries in underground warrens hidden away on the _Shadow_ Plane. Svartalfars are extremely interested in knowledge about the realm of the fey. Many _[[universal monster rules/Fear|fear]]_ the svartalfars are searching for a way to finally take their revenge upon those who expelled them.

These cold, calculating killers are not swayed by whimsy or deeper passions. They pride themselves on their pitilessness and inability to be bribed or dissuaded from ending a target’s life once they’ve been contracted to do so. Once an assassination is paid for, it’s the duty of all the svartalfars of a clan or cabal to make sure it gets done. If a clan or cabal fails, another one will finish the job.

Svartalfars seem to feel no love or real friendship. All of their actions are committed for practical reasons—political gain, procreation, or relieving boredom. Focused and utterly unyielding, they are considered by many to be the perfect killers, and their tenacity and mastery over magic and shadows are a death sentence for anyone who has been marked as their quarry.