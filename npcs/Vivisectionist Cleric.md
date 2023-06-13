---
cssclass: [monsters]
title1: Vivisectionist Cleric
title2: Vivisectionist Cleric
CR: 6
sources:
- name: NPC Codex
  page: 48
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 2400
race: Human
classes:
- cleric of Zon-Kuthon 7
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 0
AC:
  AC: 19
  touch: 10
  flat_footed: 19
  components:
    armor: 9
HP:
  HP: 56
  long: 7d8+21
saves:
  fort: 8
  ref: 3
  will: 9
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk spiked chain +7 (2d4+1)
      entries:
      - - damage: 2d4+1
      attack: mwk spiked chain
      bonus:
      - 7
  ranged:
  - - text: light crossbow +5 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 5
  special:
  - channel negative energy 5/day (DC 17, 4d6)
spell_like_abilities:
  entries:
  - name: bleeding touch
    source: default
    freq: 6/day
    other: 3 rounds
  - name: touch of darkness
    source: default
    freq: 6/day
    other: 3 rounds
  sources:
  - name: default
    CL: 7
    concentration: 10
spells:
  entries:
  - name: poison
    source: Cleric
    level: 4
    DC: 18
  - is_domain_spell: true
    name: shadow conjuration
    source: Cleric
    level: 4
    DC: 17
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 17
  - name: contagion
    source: Cleric
    level: 3
    DC: 17
  - is_domain_spell: true
    name: deeper darkness
    source: Cleric
    level: 3
  - name: dispel magic
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: blindness/deafness
    source: Cleric
    level: 2
    other: blindness only
    DC: 16
  - name: darkness
    source: Cleric
    level: 2
  - name: desecrate
    source: Cleric
    level: 2
  - name: eagle's splendor
    source: Cleric
    level: 2
  - name: silence
    source: Cleric
    level: 2
    DC: 15
  - is_domain_spell: true
    name: cause fear
    source: Cleric
    level: 1
    count: 2
    DC: 15
  - name: deathwatch
    source: Cleric
    level: 1
  - name: doom
    source: Cleric
    level: 1
    DC: 15
  - name: magic weapon
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 14
  - name: detect magic
    source: Cleric
    level: 0
  - name: light
    source: Cleric
    level: 0
  - name: resistance
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 7
    concentration: 10
    slots:
      0: at-will
    domains:
    - darkness
    - death
tactics:
  Before Combat: The cleric casts deathwatch.
  During Combat: The cleric casts magic weapon and shield of faith. If she has minions,
    she orders them to attack so she can use magic from a distance. She casts darkness
    to hide in and channels negative energy. If forced out of the darkness, she disables
    targets with bestow curse, blindness, and poison, then uses her spiked chain.
ability_scores:
  STR: 12
  DEX: 10
  CON: 14
  INT: 8
  WIS: 17
  CHA: 14
BAB: 5
CMB: 6
CMD: 16
feats:
- name: Blind-Fight
- name: Combat Casting
- name: Command Undead
- name: Heavy Armor Proficiency
- name: Improved Channel
- name: Spell Focus (necromancy)
skills:
  Heal: 9
  Knowledge (religion): 6
  Perception: 7
  Spellcraft: 5
languages:
- Common
special_qualities:
- aura
gear:
  combat:
  - potion of cure moderate wounds
  - flask of acid
  - smokesticks (2)
  other:
  - masterwork full plate
  - light crossbow with 20 bolts
  - masterwork spiked chain
  - cloak of resistance +1
  - unholy water
  - wooden unholy symbol
  - onyx gems (worth 350 gp)
  - silver dust for desecrate (worth 25 gp)
  - 114 gp
desc_long: The vivisectionist cleric serves the god of pain and darkness, and can
  keep victims alive for weeks.

---

# Vivisectionist Cleric

**Source** NPC Codex pg. 48
**XP** 2,400
Human _[[classes/Cleric|cleric]]_ of Zon-Kuthon 7

LE Medium humanoid (human)
**Init** +0; **Senses** Perception +7

##### Defense

**AC** 19, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+9 armor)
**hp** 56 (7d8+21)
**Fort** +8, **Ref** +3, **Will** +9

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Spiked chain|spiked chain]]_ +7 (2d4+1)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +5 (1d8/19–20)
**Special Attacks** channel negative energy 5/day (DC 17, 4d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +10)
6/day— bleeding touch (3 rounds), touch of _[[spells/Darkness|darkness]]_ (3 rounds)
**_Cleric_ Spells Prepared **(CL 7th; concentration +10)
4th—poison (DC 18), _[[items/Armor Magic Abilities/Shadow|shadow]]_ conjurationD (DC 17)
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 17), _[[spells/Contagion|contagion]]_ (DC 17), _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Dispel Magic|dispel magic]]_
2nd—blindness/deafnessD (blindness only, DC 16), _darkness_, _[[spells/Desecrate|desecrate]]_, _[[monsters/Eagle|eagle]]_’s splendor, _[[spells/Silence|silence]]_ (DC 15)
1st—cause fearD (2, DC 15), _[[spells/Deathwatch|deathwatch]]_, _[[spells/Doom|doom]]_ (DC 15), _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 14), _[[spells/Detect Magic|detect magic]]_, light, _[[universal monster rules/Resistance|resistance]]_
**D **Domain spell; **Domains **_Darkness_, Death

### Tactics

**Before Combat **The _cleric_ casts _deathwatch_.
**During Combat **The _cleric_ casts _magic weapon_ and _shield of faith_. If she has minions, she orders them to attack so she can use magic from a distance. She casts _darkness_ to hide in and channels negative energy. If forced out of the _darkness_, she disables targets with _bestow curse_, blindness, and poison, then uses her _spiked chain_.

##### Statistics
**Str** 12, **Dex** 10, **Con** 14, **Int** 8, **Wis** 17, **Cha** 14
**Base Atk** +5; **CMB** +6; **CMD** 16
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Heavy Armor Proficiency|Heavy Armor Proficiency]]_, _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Spell Focus|Spell Focus]]_ (necromancy)
**Skills** _[[spells/Heal|Heal]]_ +9, Knowledge (religion) +6, Perception +7, Spellcraft +5
**Languages** Common
**SQ** aura
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[items/Mundane/Flask|flask]]_ of acid, smokesticks (2); **Other Gear** masterwork _[[items/Armor/Full plate|full plate]]_, _light crossbow_ with 20 bolts, masterwork _spiked chain_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Weapon Magic Abilities/Unholy|unholy]]_ water, wooden _unholy_ symbol, onyx gems (worth 350 gp), silver dust for _desecrate_ (worth 25 gp), 114 gp

The _[[npcs/Vivisectionist Cleric|vivisectionist cleric]]_ serves the god of pain and _darkness_, and can keep victims alive for weeks.