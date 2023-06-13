---
cssclass: [monsters]
title1: Kyton, Cantor
desc_short: All the skin has been scraped from this childlike humanoid's frame, revealing
  cords of gray musculature. Its eyes burn with a red glow.
title2: Cantor
CR: 9
sources:
- name: Occult Bestiary
  page: 30
  link: http://paizo.com/products/btpy9g21?Pathfinder-Campaign-Setting-Occult-Bestiary
XP: 6400
alignment: LE
size: Small
type: outsider
subtypes:
- evil
- extraplanar
- kyton
- lawful
initiative:
  bonus: 9
senses:
  darkvision: 60
AC:
  AC: 24
  touch: 16
  flat_footed: 19
  components:
    dex: 5
    natural: 8
    size: 1
HP:
  HP: 105
  long: 10d10+50
  regeneration: 5
  regeneration_weakness: good spells and weapons, silver weapons
saves:
  fort: 12
  ref: 10
  will: 12
DR:
- amount: 10
  weakness: silver
immunities:
- cold
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +16 (1d3+2 plus grab and lingering touch)
      entries:
      - - damage: 1d3+2
        - effect: grab
        - effect: lingering touch
      count: 2
      attack: claws
      bonus:
      - 16
    - text: bite +16 (1d4+2)
      entries:
      - - damage: 1d4+2
      attack: bite
      bonus:
      - 16
  special:
  - lingering touch
  - oneiric invasion
  - unnerving gaze (DC 18)
spell_like_abilities:
  entries:
  - superscripts:
    - OA
    name: ego whip I
    source: default
    freq: 3/day
    DC: 16
  - name: nightmare
    source: default
    freq: 3/day
    DC: 18
  - superscripts:
    - OA
    name: paranoia
    source: default
    freq: 3/day
    DC: 15
  - superscripts:
    - OA
    name: shadow body
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 9
    concentration: 12
ability_scores:
  STR: 14
  DEX: 21
  CON: 20
  INT: 13
  WIS: 21
  CHA: 16
BAB: 10
CMB: 11
CMB_other: +15 grapple
CMD: 26
feats:
- name: Combat Reflexes
- name: Improved Initiative
- name: Lightning Reflexes
- name: Run
- name: Weapon Finesse
skills:
  Acrobatics: 18
  Bluff: 16
  Climb: 15
  Intimidate: 16
  Knowledge (arcana): 14
  Perception: 18
  Stealth: 22
languages:
- Common
- Infernal
- telepathy 100 ft.
ecology:
  environment: any (Plane of Shadow)
  organization: solitary, pair, or expedition (3-6)
  treasure_type: standard
special_abilities:
  Lingering Touch (Su): |-
    The touch of a cantor is supernaturally toxic, lingering in its victim's mind like a poison. Any creature damaged by a cantor must succeed at a Will saving throw or vividly feel the pain of the kyton's claws. The memory is so real, the victim continues to take damage. Multiple attacks increase the DC of this effect, as with any other poison. Any form of magical healing or spells like psychic surgeryOA end this effect immediately, but remove poison has no effect. Creatures that are immune to mind-affecting effects are immune to this ability.

    Lingering Touch: Claw-injury; save Will DC 20; frequency 1/round for 10 rounds; effect 1d3 damage; cure 2 consecutive saves. The save DC is Wisdom-based.
  Oneiric Invasion (Su): Once per minute, a cantor can unleash a soundless scream.
    All foes within 30 feet must succeed at a DC 20 Will saving throw or be affected
    as per the spell oneiric horrorOA. Those who fail believe the cantor has grown
    even more terrifying and is making a direct assault against them. At the same
    moment, the cantor becomes invisible, as per improved invisibility. This invisibility
    lasts for as long as at least one creature is affected by the cantor's oneiric
    horror effect. If no creature fails its saving throw, the cantor remains visible.
    Those who succeed at their saving throws are immune to the same cantor's oneiric
    invasion for 24 hours. Creatures that are immune to mind-affecting effects are
    immune to this ability. The save DC is Wisdom-based.
  Unnerving Gaze (Su): Those who fail their saves are telepathically wracked by agonizing
    pain that imposes a -4 penalty on their attack rolls, skill checks, and ability
    checks. This penalty lasts for 1d4 rounds. This is a mind-affecting fear effect.
    The save DC is Charisma-based.
desc_long: |-
  Few can imagine what atrocities bring kyton cantors into being. Like all kytons, cantors arise in pain, but theirs is of a more deliberate sort. Just as its skin is stripped away, a cantor's consciousness is shattered and reforged, making it a weapon against reality and a scalpel to excise sanity. Among their brethren, cantors serve as scouts, guides to more brutish kytons, and, along with their teeming brethren, throng the ruined halls of Shadow Plane fortresses.

  A cantor stands a mere 3 feet tall and weighs less than 50 pounds.

---

# Kyton, Cantor
All the skin has been scraped from this _[[feats/Childlike|childlike]]_ humanoid’s frame, revealing cords of _[[monsters/Gray|gray]]_ musculature. Its eyes _[[universal monster rules/Burn|burn]]_ with a red glow.
**Source** Occult Bestiary pg. 30
**XP** 6,400

LE Small outsider (evil, extraplanar, _[[monsters/Kyton|kyton]]_, lawful)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +18

##### Defense

**AC** 24, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+5 Dex, +8 natural, +1 size)
**hp** 105 (10d10+50); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good spells and weapons, silver weapons)
**Fort** +12, **Ref** +10, **Will** +12
**DR** 10/silver; **Immune** cold

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +16 (1d3+2 plus _[[universal monster rules/Grab|grab]]_ and lingering touch), bite +16 (1d4+2)
**Special Attacks** lingering touch, oneiric invasion, unnerving _[[universal monster rules/Gaze|gaze]]_ (DC 18)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +12)
3/day—_[[spells/Ego _[[items/Weapon/Whip|Whip]]_ I|ego _whip_ I]]_ (DC 16), _[[spells/Nightmare|nightmare]]_ (DC 18), _[[spells/Paranoia|paranoia]]_ (DC 15)
1/day—_[[spells/Shadow Body|shadow body]]_

##### Statistics
**Str** 14, **Dex** 21, **Con** 20, **Int** 13, **Wis** 21, **Cha** 16
**Base Atk** +10; **CMB** +11 (+15 grapple); **CMD** 26
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, Run, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +18, Bluff +16, _[[universal monster rules/Climb|Climb]]_ +15, Intimidate +16, Knowledge (arcana) +14, Perception +18, Stealth +22
**Languages** Common, Infernal; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.

##### Ecology

**Environment** any (Plane of _[[items/Armor Magic Abilities/Shadow|Shadow]]_)
**Organization** solitary, pair, or expedition (3–6)
**Treasure** standard

### Special Abilities

**Lingering Touch (Su)** The touch of a cantor is supernaturally _[[items/Weapon Magic Abilities/Toxic|toxic]]_, lingering in its victim’s mind like a poison. Any creature damaged by a cantor must succeed at a Will saving throw or vividly feel the pain of the _kyton_’s claws. The memory is so real, the victim continues to take damage. Multiple attacks increase the DC of this effect, as with any other poison. Any form of magical healing or spells like _[[spells/Psychic Surgery|psychic surgery]]_ end this effect immediately, but remove poison has no effect. Creatures that are immune to mind-affecting effects are immune to this ability.

Lingering Touch: Claw—injury; save Will DC 20; frequency 1/round for 10 rounds; effect 1d3 damage; cure 2 consecutive saves. The save DC is Wisdom-based.

**Oneiric Invasion (Su)** Once per minute, a cantor can unleash a soundless scream. All foes within 30 feet must succeed at a DC 20 Will saving throw or be affected as per the spell _[[spells/Oneiric Horror|oneiric horror]]_. Those who fail believe the cantor has grown even more terrifying and is making a direct assault against them. At the same moment, the cantor becomes _[[conditions/Invisible|invisible]]_, as per improved _[[spells/Invisibility|invisibility]]_. This _invisibility_ lasts for as long as at least one creature is affected by the cantor’s _oneiric horror_ effect. If no creature fails its saving throw, the cantor remains visible. Those who succeed at their saving throws are immune to the same cantor’s oneiric invasion for 24 hours. Creatures that are immune to mind-affecting effects are immune to this ability. The save DC is Wisdom-based.

**Unnerving _Gaze_ (Su)** Those who fail their saves are telepathically wracked by agonizing pain that imposes a –4 penalty on their attack rolls, skill checks, and ability checks. This penalty lasts for 1d4 rounds. This is a mind-affecting _[[universal monster rules/Fear|fear]]_ effect. The save DC is Charisma-based.

##### Description

Few can imagine what atrocities bring _kyton_ cantors into being. Like all kytons, cantors arise in pain, but theirs is of a more deliberate sort. Just as its skin is stripped away, a cantor’s consciousness is shattered and reforged, making it a weapon against reality and a scalpel to excise sanity. Among their brethren, cantors serve as scouts, guides to more brutish kytons, and, along with their teeming brethren, throng the ruined halls of _Shadow_ Plane fortresses.

A cantor stands a mere 3 feet tall and weighs less than 50 pounds.