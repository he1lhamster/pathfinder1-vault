---
cssclass: [monsters]
title1: Baetriov
desc_short: Clad in the finest silks, this noblewoman has cheeks that are flush with
  vitality, though her eyes speak to great age and danger.
title2: Baetriov
CR: 8
sources:
- name: Taldor, the First Empire
  page: 56
  link: http://paizo.com/products/btpy9wzs?Pathfinder-Campaign-Setting-Taldor-the-First-Empire
XP: 4800
alignment: LE
size: Medium
type: undead
initiative:
  bonus: 8
senses:
  darkvision: 60
auras:
- name: hemophile
  radius: 30
AC:
  AC: 19
  touch: 18
  flat_footed: 15
  components:
    armor: 1
    dex: 4
    profane: 4
HP:
  HP: 102
  long: 12d8+48
  fast_healing: 5
saves:
  fort: 12
  ref: 12
  will: 13
defensive_abilities:
- channel resistance +4
DR:
- amount: 10
  weakness: good and piercing
immunities:
- undead traits
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +13 (1d4+3 plus bleed)
      entries:
      - - damage: 1d4+3
        - effect: bleed
      attack: dagger
      bonus:
      - 13
  - - text: 2 slams +13 (1d4+3)
      entries:
      - - damage: 1d4+3
      count: 2
      attack: slams
      bonus:
      - 13
  special:
  - sneak attack +3d6
spell_like_abilities:
  entries:
  - name: bleed
    source: default
    freq: At will
    DC: 14
  - name: blood biography
    source: default
    freq: At will
    DC: 16
  - name: bloodhound
    source: default
    freq: At will
  - name: pain strike
    source: default
    freq: At will
    DC: 19
  - name: charm person
    source: default
    freq: 3/day
    DC: 15
  - name: modify memory
    source: default
    freq: 3/day
    DC: 18
  - name: rage
    source: default
    freq: 3/day
    DC: 17
  sources:
  - name: default
    CL: 12
    concentration: 16
ability_scores:
  STR: 16
  DEX: 19
  CON:
  INT: 17
  WIS: 14
  CHA: 18
BAB: 9
CMB: 12
CMD: 26
feats:
- name: Ability Focus (pain strike)
- name: Dazzling Display
- is_bonus: true
  name: Deceitful
- name: Improved Initiative
- is_bonus: true
  name: Persuasive
- name: Shatter Defenses
- name: Weapon Focus (dagger)
- name: Weapon Focus (slam)
skills:
  Bluff: 18
  Craft (alchemy): 13
  Diplomacy: 18
  Disguise: 14
    when appearing to be alive: 24
  Intimidate: 21
  Knowledge (arcana): 11
  Knowledge (nobility): 11
  Perception: 15
  Sense Motive: 15
  Stealth: 13
languages:
- Common
- Elven
- Infernal
- Jistkan
special_qualities:
- blood well
- bloody bath
ecology:
  environment: any urban
  organization: solitary or cabal (2-6)
  treasure_type: double
  treasure:
  - padded armor
  - dagger
  - other treasure
special_abilities:
  Blood Well (Su): |-
    Every baetriov crafts a blood well, a bath or pool of magically fresh blood that preserves her false youth and immortality. So long as the well is empowered, a destroyed baetriov automatically re-forms in her blood well after 1d10 nights. Only destroying the pool prevents this return. A typical blood well has hardness 8 and 100 hp.

     The blood well must be refreshed by sacrificing humanoid creatures; a sacrificed humanoid empowers the blood well for a number of months equal to the victim's Hit Dice. If not refreshed again before this time expires, the blood well loses its magical properties and the baetriov no longer benefits from her bloody bath special ability until she can craft a new blood well, a process that requires the sacrifice of a vampire and a number of humanoids equal to the baetriov's Hit Dice (typically 12) under the new moon.
  Bloody Bath (Su): A baetriov can bathe in her blood well for 1 hour to gain a flush
    of false life for a number of days equal to her Hit Dice. This flush of life grants
    her immunity to spells that normally detect undead, a +10 circumstance bonus on
    Disguise checks to appear as a living creature, and a profane bonus to her AC
    and on saving throws equal to her Charisma modifier (already included in the statistics
    above).
  Hemophile (Su): Each attack that deals at least 1 point of piercing or slashing
    damage within this aura also deals 1d6 points of bleed damage. The baetriov can
    activate or deactivate this aura as a free action.
desc_long: Baetriovs are unique occult vampires who use ancient vile rituals to store
  their life force in a pool of blood, which must be periodically refreshed by human
  sacrifice. So long as their blood wells remain fresh and intact, baetriovs can remain
  forever young and handsome, gathering cults of personality to provide new victims.

---

# Baetriov
Clad in the finest silks, this noblewoman has cheeks that are flush with vitality, though her eyes speak to great age and danger.
**Source** Taldor, the First Empire pg. 56
**XP** 4,800

LE Medium undead
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +15
**Aura** hemophile (30 ft.)

##### Defense

**AC** 19, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 15 (+1 armor, +4 Dex, +4 profane)
**hp** 102 (12d8+48); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +12, **Ref** +12, **Will** +13
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 10/good and piercing; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +13 (1d4+3 plus _[[universal monster rules/Bleed|bleed]]_) or 2 slams +13 (1d4+3)
**Special Attacks** sneak attack +3d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +16)
At will—_bleed_ (DC 14), _[[spells/Blood Biography|blood biography]]_ (DC 16), _[[spells/Bloodhound|bloodhound]]_, _[[spells/Pain Strike|pain strike]]_ (DC 19)
3/day—_[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Modify Memory|modify memory]]_ (DC 18), _[[spells/Rage|rage]]_ (DC 17)

##### Statistics
**Str** 16, **Dex** 19, **Con** —, **Int** 17, **Wis** 14, **Cha** 18
**Base Atk** +9; **CMB** +12; **CMD** 26
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_pain strike_), _[[feats/Dazzling Display|Dazzling Display]]_, _[[feats/Deceitful|Deceitful]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Shatter Defenses|Shatter Defenses]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_dagger_, slam)
**Skills** Bluff +18, Craft (alchemy) +13, Diplomacy +18, Disguise +14 (+24 when appearing to be alive), Intimidate +21, Knowledge (arcana, nobility) +11, Perception +15, Sense Motive +15, Stealth +13
**Languages** Common, Elven, Infernal, Jistkan
**SQ** blood well, bloody bath

##### Ecology

**Environment** any urban
**Organization** solitary or cabal (2–6)
**Treasure** double (_[[items/Armor/Padded armor|padded armor]]_, _dagger_, other treasure)

### Special Abilities

**Blood Well (Su)** Every _[[monsters/Baetriov|baetriov]]_ crafts a blood well, a bath or pool of magically fresh blood that preserves her false youth and immortality. So long as the well is empowered, a destroyed _baetriov_ automatically re-forms in her blood well after 1d10 nights. Only destroying the pool prevents this return. A typical blood well has hardness 8 and 100 hp.

The blood well must be refreshed by sacrificing humanoid creatures; a sacrificed humanoid empowers the blood well for a number of months equal to the victim’s Hit Dice. If not refreshed again before this time expires, the blood well loses its magical properties and the _baetriov_ no longer benefits from her bloody bath special ability until she can craft a new blood well, a process that requires the _[[spells/Sacrifice|sacrifice]]_ of a _[[monsters/Vampire|vampire]]_ and a number of humanoids equal to the _baetriov_’s Hit Dice (typically 12) under the new moon.

**Bloody Bath (Su)** A _baetriov_ can bathe in her blood well for 1 hour to gain a flush of _[[spells/False Life|false life]]_ for a number of days equal to her Hit Dice. This flush of life grants her _[[universal monster rules/Immunity|immunity]]_ to spells that normally _[[spells/Detect Undead|detect undead]]_, a +10 circumstance bonus on Disguise checks to appear as a living creature, and a profane bonus to her AC and on saving throws equal to her Charisma modifier (already included in the statistics above).

**Hemophile (Su)** Each attack that deals at least 1 point of piercing or slashing damage within this aura also deals 1d6 points of _bleed_ damage. The _baetriov_ can activate or deactivate this aura as a free action.

##### Description

Baetriovs are unique occult vampires who use ancient vile rituals to store their life force in a pool of blood, which must be periodically refreshed by human _sacrifice_. So long as their blood wells remain fresh and intact, baetriovs can remain forever young and handsome, gathering cults of personality to provide new victims.