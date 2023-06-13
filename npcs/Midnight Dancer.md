---
cssclass: [monsters]
title1: Midnight Dancer
title2: Midnight Dancer
CR: 12
sources:
- name: NPC Codex
  page: 237
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Half-orc
classes:
- bard 9
- shadowdancer 4
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 2
senses:
  darkvision: 90
  see invisibility: true
AC:
  AC: 20
  touch: 14
  flat_footed: 17
  components:
    armor: 5
    deflection: 1
    dex: 2
    dodge: 1
    natural: 1
HP:
  HP: 71
  long: 9d8+4d8+9
saves:
  fort: 4
  ref: 12
  will: 8
  other: +4 vs. bardic performance, language-dependent, and sonic
defensive_abilities:
- evasion
- orc ferocity
- uncanny dodge
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 dagger +12/+7 (1d4+3/19-20)
      entries:
      - - damage: 1d4+3
          crit_range: 19-20
      attack: +1 dagger
      bonus:
      - 12
      - 7
  ranged:
  - - text: +1 light crossbow +12 (1d8+1/19-20)
      entries:
      - - damage: 1d8+1
          crit_range: 19-20
      attack: +1 light crossbow
      bonus:
      - 12
  special:
  - bardic performance 24 rounds/day (move action; countersong, dirge of doom, distraction,
    fascinate, inspire competence +3, inspire courage +2, inspire greatness, suggestion)
spell_like_abilities:
  entries:
  - name: shadow illusion
    source: default
    freq: 2/day
    DC: 15
  - name: shadow call
    source: default
    freq: 1/day
    DC: 18
  sources:
  - name: default
    CL: 4
    concentration: 8
spells:
  entries:
  - name: cure serious wounds
    source: Bard
    level: 3
  - name: deep slumber
    source: Bard
    level: 3
    DC: 18
  - name: gaseous form
    source: Bard
    level: 3
  - name: see invisibility
    source: Bard
    level: 3
  - name: darkness
    source: Bard
    level: 2
  - name: invisibility
    source: Bard
    level: 2
  - name: silence
    source: Bard
    level: 2
    DC: 16
  - name: suggestion
    source: Bard
    level: 2
    DC: 17
  - name: cure light wounds
    source: Bard
    level: 1
  - name: lesser confusion
    source: Bard
    level: 1
    DC: 16
  - name: remove fear
    source: Bard
    level: 1
  - name: silent image
    source: Bard
    level: 1
    DC: 15
  - name: sleep
    source: Bard
    level: 1
    DC: 16
  - name: daze
    source: Bard
    level: 0
    DC: 15
  - name: ghost sound
    source: Bard
    level: 0
    DC: 14
  - name: lullaby
    source: Bard
    level: 0
    DC: 15
  - name: mage hand
    source: Bard
    level: 0
  - name: message
    source: Bard
    level: 0
  - name: open/close
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 9
    concentration: 13
    slots:
      3: 4
      2: 5
      1: 6
      0: at-will
tactics:
  Before Combat: The shadowdancer casts see invisibility.
  During Combat: Keeping to the shadows at the edge of battle, the shadowdancer supports
    allies and uses crossbow shots and debilitating spells against enemies.
  Base Statistics: Without see invisibility, the shadowdancer's statistics are Senses
    darkvision 90 ft.
ability_scores:
  STR: 14
  DEX: 14
  CON: 10
  INT: 15
  WIS: 8
  CHA: 18
BAB: 9
CMB: 11
CMD: 25
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Dodge
- name: Iron Will
- name: Lightning Reflexes
- name: Mobility
- name: Spell Focus (enchantment)
skills:
  Acrobatics: 15
  Climb: 10
  Disable Device: 12
  Disguise: 10
  Intimidate: 6
  Knowledge (dungeoneering): 19
  Knowledge (local): 14
  Perception: 15
  Perform (act): 15
  Perform (dance): 14
  Sleight of Hand: 10
  Stealth: 23
  Swim: 7
  Use Magic Device: 17
languages:
- Common
- Goblin
- Orc
special_qualities:
- bardic knowledge +4
- hide in plain sight
- lore master 1/day
- orc blood
- rogue talent (fast stealth)
- shadow jump (40 feet/day)
- summon shadow
- versatile performance (act, dance)
- weapon familiarity
gear:
  combat:
  - +1 human-bane bolts (5)
  - +1 undead-bane bolts (5)
  other:
  - +3 leather armor
  - +1 dagger
  - +1 light crossbow with 20 bolts
  - dagger
  - amulet of natural armor +1
  - cloak of elvenkind
  - headband of alluring charisma +2
  - ring of protection +1
  - 1,038 gp
desc_long: These bards grant support though a subtle dance of shadows.

---

# Midnight Dancer

**Source** NPC Codex pg. 237
**XP** 19,200
Half-orc _[[classes/Bard|bard]]_ 9/shadowdancer 4

NE Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 90 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +15

##### Defense

**AC** 20, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 armor, +1 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +1 natural)
**hp** 71 (9d8+4d8+9)
**Fort** +4, **Ref** +12, **Will** +8; +4 vs. bardic performance, language-dependent, and sonic
**Defensive Abilities** evasion, _orc_ _[[universal monster rules/Ferocity|ferocity]]_, uncanny _dodge_

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Dagger|dagger]]_ +12/+7 (1d4+3/19–20)
**Ranged** +1 _[[items/Weapon/Light crossbow|light crossbow]]_ +12 (1d8+1/19–20)
**Special Attacks** bardic performance 24 rounds/day (move action; countersong, dirge of _[[spells/Doom|doom]]_, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire competence +3, inspire courage +2, inspire greatness, _[[spells/Suggestion|suggestion]]_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +8)
2/day—_[[items/Armor Magic Abilities/Shadow|shadow]]_ illusion (DC 15)
1/day—_shadow_ call (DC 18)
**_Bard_ Spells Known **(CL 9th; concentration +13)
3rd (4/day)—_[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Deep Slumber|deep slumber]]_ (DC 18), _[[spells/Gaseous Form|gaseous form]]_, _see invisibility_
2nd (5/day)—_[[spells/Darkness|darkness]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Silence|silence]]_ (DC 16), _suggestion_ (DC 17)
1st (6/day)—_[[spells/Cure Light Wounds|cure light wounds]]_, lesser _[[spells/Confusion|confusion]]_ (DC 16), _[[spells/Remove Fear|remove fear]]_, _[[spells/Silent Image|silent image]]_ (DC 15), sleep (DC 16)
0 (at will)—_[[spells/Daze|daze]]_ (DC 15), _[[spells/Ghost Sound|ghost sound]]_ (DC 14), _[[spells/Lullaby|lullaby]]_ (DC 15), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, open/close

### Tactics

**Before Combat **The shadowdancer casts _see invisibility_.
**During Combat **Keeping to the shadows at the edge of battle, the shadowdancer supports allies and uses crossbow shots and _[[items/Weapon Magic Abilities/Debilitating|debilitating]]_ spells against enemies.
**Base Statistics **Without _see invisibility_, the shadowdancer’s statistics are **Senses **_darkvision_ 90 ft.

##### Statistics
**Str** 14, **Dex** 14, **Con** 10, **Int** 15, **Wis** 8, **Cha** 18
**Base Atk** +9; **CMB** +11; **CMD** 25
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment)
**Skills** Acrobatics +15, _[[universal monster rules/Climb|Climb]]_ +10, Disable Device +12, Disguise +10, Intimidate +6, Knowledge (dungeoneering) +19, Knowledge (local) +14, Perception +15, Perform (act) +15, Perform (dance) +14, Sleight of Hand +10, Stealth +23, Swim +7, Use Magic Device +17
**Languages** Common, _[[monsters/Goblin|Goblin]]_, _Orc_
**SQ** bardic knowledge +4, hide in plain sight, lore master 1/day, _orc_ blood, _[[classes/Rogue|rogue]]_ talent (fast stealth), _shadow_ _[[spells/Jump|jump]]_ (40 feet/day), _[[universal monster rules/Summon|summon]]_ _shadow_, versatile performance (act, dance), weapon familiarity
**Combat Gear** +1 human-bane bolts (5), +1 undead-bane bolts (5); **Other Gear** +3 _[[items/Armor/Leather armor|leather armor]]_, +1 _dagger_, +1 _light crossbow_ with 20 bolts, _dagger_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of Elvenkind|cloak of elvenkind]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, 1,038 gp

These bards grant support though a subtle dance of shadows.