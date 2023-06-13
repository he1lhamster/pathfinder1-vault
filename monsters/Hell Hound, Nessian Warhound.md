---
cssclass: [monsters]
title1: Hell Hound, Nessian Warhound
desc_short: This brawny hound is wreathed in flames, and its footsteps leave burning
  prints that sputter and smoke.
title2: Mythic Nessian Warhound
CR: 11
MR: 4
sources:
- name: Mythic Adventures
  page: 203
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 12800
alignment: LE
size: Large
type: outsider
subtypes:
- evil
- extraplanar
- fire
- lawful
- mythic
initiative:
  bonus: 6
senses:
  darkvision: 60
  scent: true
  see in darkness: true
AC:
  AC: 28
  touch: 11
  flat_footed: 26
  components:
    armor: 6
    dex: 2
    natural: 11
    size: -1
HP:
  HP: 166
  long: 12d10+100
saves:
  fort: 13
  ref: 10
  will: 6
DR:
- amount: 10
  weakness: epic
immunities:
- fire
weaknesses:
- vulnerable to cold
speeds:
  base: 40
attacks:
  melee:
  - - text: bite +22 (2d8+9/18-20 plus burn plus trip)
      entries:
      - - damage: 2d8+9
          crit_range: 18-20
        - effect: burn
        - effect: trip
      attack: bite
      bonus:
      - 22
    - text: 2 claws +20 (2d6+9 plus burn)
      entries:
      - - damage: 2d6+9
        - effect: burn
      count: 2
      attack: claws
      bonus:
      - 20
  special:
  - breath weapon (30-ft. cone, 10d6 fire plus clinging flames, Reflex DC 21 half,
    usable every 1d4 rounds)
  - burn (1d6, DC 21)
  - mythic power (4/day, surge +1d8)
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: dimension door
    source: default
    freq: 3/day
  - name: locate creature
    source: default
    freq: 3/day
  sources:
  - name: default
    CL: 12
    concentration: 10
ability_scores:
  STR: 29
  DEX: 15
  CON: 21
  INT: 4
  WIS: 14
  CHA: 6
BAB: 12
CMB: 22
CMD: 34
CMD_other: 38 vs. trip
feats:
- name: Alertness
- is_mythic: true
  name: Improved Critical (bite)
- name: Improved Initiative
- name: Skill Focus (Stealth)
- name: Skill Focus (Survival)
- is_mythic: true
  name: Weapon Focus (bite)
skills:
  Acrobatics: 15
    when jumping: 19
  Perception: 14
  Sense Motive: 4
  Stealth: 17
  Survival: 17
  _racial_mods:
    Stealth:
      _: 5
languages:
- Infernal
ecology:
  environment: any (Hell)
  organization: solitary, pair, or pack (3-6)
  treasure_type: standard
  treasure:
  - +2 chain shirt barding
desc_long: A mythic hell hound is a prince among the wolves of Hell, feral but still
  subservient to the archdevils. Allowed to run wild, they are the original creatures
  from which the “tamer” common hell hounds were made.

---

# Hell Hound, Nessian Warhound
This creature resembles a powerfully built _[[monsters/Wolf|wolf]]_ the size of a large draft _[[monsters/Horse|horse]]_, with ebony fur and _[[items/Weapon Magic Abilities/Burning|burning]]_, fiery red eyes.
**Source** Pathfinder RPG Bestiary pg. 173
**XP** 6,400

LE Large outsider (evil, extraplanar, fire, lawful)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Scent|scent]]_; Perception +12

##### Defense

**AC** 24, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+6 armor, +2 Dex, +7 natural, –1 size)
**hp** 126 (12d10+60)
**Fort** +13, **Ref** +10, **Will** +5
**Immune** fire
**Weaknesses** _[[curses/Vulnerability|vulnerability]]_ to cold

##### Offense
**Speed** 40 ft.
**Melee** bite +20 (2d6+12/19–20 plus 2d6 fire)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-ft. cone, once every 1d4 rounds, 10d6 fire damage, Reflex DC 21 half)

##### Statistics
**Str** 27, **Dex** 15, **Con** 21, **Int** 4, **Wis** 12, **Cha** 6
**Base Atk** +12; **CMB** +21; **CMD** 33 (37 vs. _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Improved Critical|Improved Critical]]_ (bite), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Skill Focus|Skill Focus]]_ (Stealth, Survival), _[[feats/Weapon Focus|Weapon Focus]]_ (bite)
**Skills** Acrobatics +16, Perception +12, Stealth +21, Survival +18; **Racial Modifiers** +5 Stealth
**Languages** Infernal

##### Ecology

**Environment** any (Hell)
**Organization** solitary, pair, or pack (3–6)
**Treasure** standard (+2 _[[items/Armor/Chain shirt|chain shirt]]_ barding)

##### Description

All are fitted with shirts of fire-scorched barding, and the loyal beasts obey their master perfectly.

They are fearsome, snarling horrors in combat.