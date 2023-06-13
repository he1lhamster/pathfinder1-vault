---
cssclass: [monsters]
title1: Spellsword
title2: Spellsword
CR: 15
sources:
- name: NPC Codex
  page: 39
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 51200
race: Elf
classes:
- bard 16
alignment: N
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 21
  touch: 13
  flat_footed: 18
  components:
    armor: 8
    dex: 3
HP:
  HP: 91
  long: 16d8+16
saves:
  fort: 6
  ref: 13
  will: 10
  other: +2 vs. enchantments, +4 vs. bardic performance, language-dependent, and sonic
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 elven curve blade +18/+13/+8 (1d10+6/15-20)
      entries:
      - - damage: 1d10+6
          crit_range: 15-20
      attack: +2 elven curve blade
      bonus:
      - 18
      - 13
      - 8
  special:
  - bardic performance 39 rounds/day (swift action; countersong, dirge of doom, distraction,
    fascinate, frightening tune, inspire competence +5, inspire courage +3, inspire
    greatness, inspire heroics, soothing performance, suggestion)
spells:
  entries:
  - name: greater shout
    source: Bard
    level: 6
    DC: 21
  - name: project image
    source: Bard
    level: 6
    DC: 21
  - name: greater dispel magic
    source: Bard
    level: 5
  - name: mind fog
    source: Bard
    level: 5
    DC: 20
  - name: mirage arcana
    source: Bard
    level: 5
    DC: 20
  - name: shadow evocation
    source: Bard
    level: 5
    DC: 20
  - name: dimension door
    source: Bard
    level: 4
  - name: dominate person
    source: Bard
    level: 4
    DC: 19
  - name: freedom of movement
    source: Bard
    level: 4
  - name: greater invisibility
    source: Bard
    level: 4
  - name: shadow conjuration
    source: Bard
    level: 4
    DC: 19
  - name: charm monster
    source: Bard
    level: 3
    DC: 18
  - name: dispel magic
    source: Bard
    level: 3
  - name: haste
    source: Bard
    level: 3
    DC: 18
  - name: scrying
    source: Bard
    level: 3
    DC: 18
  - name: slow
    source: Bard
    level: 3
    DC: 18
  - name: alter self
    source: Bard
    level: 2
  - name: glitterdust
    source: Bard
    level: 2
    DC: 17
  - name: mirror image
    source: Bard
    level: 2
  - name: pyrotechnics
    source: Bard
    level: 2
    DC: 17
  - name: silence
    source: Bard
    level: 2
    DC: 17
  - name: suggestion
    source: Bard
    level: 2
    DC: 17
  - name: charm person
    source: Bard
    level: 1
    DC: 16
  - name: expeditious retreat
    source: Bard
    level: 1
  - name: grease
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 16
  - name: silent image
    source: Bard
    level: 1
    DC: 16
  - name: unseen servant
    source: Bard
    level: 1
  - name: dancing lights
    source: Bard
    level: 0
  - name: detect magic
    source: Bard
    level: 0
  - name: light
    source: Bard
    level: 0
  - name: mage hand
    source: Bard
    level: 0
  - name: read magic
    source: Bard
    level: 0
  - name: resistance
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 16
    concentration: 21
    slots:
      6: 1
      5: 4
      4: 5
      3: 6
      2: 6
      1: 7
      0: at-will
tactics:
  During Combat: The bard attacks with his wand of fireball and shadow evocation spells
    from a distance, then casts either greater invisibility or mirror image on himself
    before entering melee. He augments himself and allies with haste and his bardic
    performance abilities. He then makes melee attacks, stopping to cast spells when
    necessary.
ability_scores:
  STR: 16
  DEX: 16
  CON: 12
  INT: 10
  WIS: 10
  CHA: 20
BAB: 12
CMB: 15
CMB_other: +17 sunder
CMD: 28
CMD_other: 30 vs. sunder
feats:
- name: Arcane Strike
- name: Bleeding Critical
- name: Cleave
- name: Critical Focus
- name: Improved Critical (elven curve blade)
- name: Improved Sunder
- name: Power Attack
- name: Weapon Focus (elven curve blade)
skills:
  Knowledge (arcana): 12
  Knowledge (dungeoneering): 12
  Knowledge (local): 12
  Knowledge (nature): 12
  Knowledge (planes): 12
  Knowledge (religion): 12
  Perception: 15
  Perform (dance): 24
  Perform (oratory): 24
  Perform (string): 22
  Perform (wind): 22
  Spellcraft: 13
    to identify magic item properties: 15
  Stealth: 24
  Use Magic Device: 18
languages:
- Common
- Elven
special_qualities:
- bardic knowledge +8
- elven magic
- jack-of-all-trades (use any skill, all skills are class skills)
- lore master 2/day
- versatile performance (dance, oratory, string, wind)
- weapon familiarity
gear:
  combat:
  - scroll of teleport
  - wand of cure moderate wounds (50 charges)
  - wand of fireball (50 charges)
  other:
  - +2 shadow elven chain
  - +2 elven curve blade
  - belt of giant strength +4
  - headband of alluring charisma +2
  - 345 gp
desc_long: Spellswords make dangerous music with a mixture of swordplay and spellcasting.

---

# Spellsword

**Source** NPC Codex pg. 39
**XP** 51,200
Elf _[[classes/Bard|bard]]_ 16

N Medium humanoid (elf)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15

##### Defense

**AC** 21, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+8 armor, +3 Dex)
**hp** 91 (16d8+16)
**Fort** +6, **Ref** +13, **Will** +10; +2 vs. enchantments, +4 vs. bardic performance, language-dependent, and sonic
**Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** +2 _[[items/Weapon/Elven curve blade|elven curve blade]]_ +18/+13/+8 (1d10+6/15–20)
**Special Attacks** bardic performance 39 rounds/day (swift action; countersong, dirge of _[[spells/Doom|doom]]_, _[[universal monster rules/Distraction|distraction]]_, fascinate, frightening tune, inspire competence +5, inspire courage +3, inspire greatness, inspire heroics, soothing performance, _[[spells/Suggestion|suggestion]]_)
**_Bard_ Spells Known **(CL 16th; concentration +21)
6th (1/day)—greater _[[spells/Shout|shout]]_ (DC 21), _[[spells/Project Image|project image]]_ (DC 21)
5th (4/day)—greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Mind Fog|mind fog]]_ (DC 20), _[[spells/Mirage Arcana|mirage arcana]]_ (DC 20), _[[spells/Shadow Evocation|shadow evocation]]_ (DC 20)
4th (5/day)—_[[spells/Dimension Door|dimension door]]_, _[[spells/Dominate Person|dominate person]]_ (DC 19), _[[spells/Freedom of Movement|freedom of movement]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Shadow Conjuration|shadow conjuration]]_ (DC 19)
3rd (6/day)—_[[spells/Charm Monster|charm monster]]_ (DC 18), _dispel magic_, _[[spells/Haste|haste]]_ (DC 18), _[[spells/Scrying|scrying]]_ (DC 18), _[[spells/Slow|slow]]_ (DC 18)
2nd (6/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 17), _[[spells/Mirror Image|mirror image]]_, _[[spells/Pyrotechnics|pyrotechnics]]_ (DC 17), _[[spells/Silence|silence]]_ (DC 17), _suggestion_ (DC 17)
1st (7/day)—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Grease|grease]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 16), _[[spells/Silent Image|silent image]]_ (DC 16), _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

### Tactics

**During Combat **The _bard_ attacks with his wand of _[[spells/Fireball|fireball]]_ and _shadow evocation_ spells from a distance, then casts either greater _invisibility_ or _mirror image_ on himself before entering melee. He augments himself and allies with _haste_ and his bardic performance abilities. He then makes melee attacks, stopping to cast spells when necessary.

##### Statistics
**Str** 16, **Dex** 16, **Con** 12, **Int** 10, **Wis** 10, **Cha** 20
**Base Atk** +12; **CMB** +15 (+17 sunder); **CMD** 28 (30 vs. sunder)
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Cleave|Cleave]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Improved Critical|Improved Critical]]_ (_elven curve blade_), _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_elven curve blade_)
**Skills** Knowledge (arcana, dungeoneering, local, nature, planes, religion) +12, Perception +15, Perform (dance, oratory) +24, Perform (string, wind) +22, Spellcraft +13 (+15 to _[[spells/Identify|identify]]_ magic item properties), Stealth +24, Use Magic Device +18
**Languages** Common, Elven
**SQ** bardic knowledge +8, elven magic, jack-of-all-trades (use any skill, all skills are class skills), lore master 2/day, versatile performance (dance, oratory, string, wind), weapon familiarity
**Combat Gear** scroll of teleport, wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (50 charges), wand of _fireball_ (50 charges); **Other Gear** +2 _[[items/Armor Magic Abilities/Shadow|shadow]]_ _[[items/Armor/Elven Chain|elven chain]]_, +2 _elven curve blade_, _[[items/Wondrous Item/Belt of Giant Strength +4|belt of giant strength +4]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, 345 gp

Spellswords make dangerous music with a mixture of swordplay and spellcasting.