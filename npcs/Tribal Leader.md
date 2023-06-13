---
cssclass: [monsters]
title1: Tribal Leader
title2: Tribal Leader
CR: 12
sources:
- name: NPC Codex
  page: 36
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Human
classes:
- bard 13
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 2
senses:
  see invisibility: true
AC:
  AC: 21
  touch: 13
  flat_footed: 18
  components:
    armor: 6
    dex: 2
    dodge: 1
    shield: 2
HP:
  HP: 78
  long: 13d8+16
saves:
  fort: 5
  ref: 10
  will: 8
  other: +4 vs. bardic performance, language-dependent, and sonic
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 spear +14/+9 (1d8+5/19-20/×3)
      entries:
      - - damage: 1d8+5
          crit_range: 19-20
          crit_multiplier: 3
      attack: +2 spear
      bonus:
      - 14
      - 9
  ranged:
  - - text: +2 spear +14/+9 (1d8+4/19-20/×3)
      entries:
      - - damage: 1d8+4
          crit_range: 19-20
          crit_multiplier: 3
      attack: +2 spear
      bonus:
      - 14
      - 9
  special:
  - bardic performance 32 rounds/day (swift action; countersong, dirge of doom, distraction,
    fascinate, inspire competence +4, inspire courage +3, inspire greatness, soothing
    performance, suggestion)
spells:
  entries:
  - name: mass suggestion
    source: Bard
    level: 5
    DC: 19
  - name: nightmare
    source: Bard
    level: 5
    DC: 19
  - name: cure critical wounds
    source: Bard
    level: 4
    DC: 18
  - name: hallucinatory terrain
    source: Bard
    level: 4
    DC: 18
  - name: speak with plants
    source: Bard
    level: 4
  - name: summon monster IV
    source: Bard
    level: 4
  - name: fear
    source: Bard
    level: 3
    DC: 17
  - name: haste
    source: Bard
    level: 3
    DC: 17
  - name: see invisibility
    source: Bard
    level: 3
  - name: slow
    source: Bard
    level: 3
    DC: 17
  - name: speak with animals
    source: Bard
    level: 3
  - name: cat's grace
    source: Bard
    level: 2
  - name: invisibility
    source: Bard
    level: 2
  - name: rage
    source: Bard
    level: 2
  - name: silence
    source: Bard
    level: 2
    DC: 16
  - name: tongues
    source: Bard
    level: 2
  - name: charm person
    source: Bard
    level: 1
    DC: 15
  - name: comprehend languages
    source: Bard
    level: 1
  - name: expeditious retreat
    source: Bard
    level: 1
  - name: grease
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 15
  - name: ventriloquism
    source: Bard
    level: 1
    DC: 15
  - name: dancing lights
    source: Bard
    level: 0
  - name: flare
    source: Bard
    level: 0
    DC: 14
  - name: ghost sound
    source: Bard
    level: 0
    DC: 14
  - name: light
    source: Bard
    level: 0
  - name: mage hand
    source: Bard
    level: 0
  - name: message
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 13
    concentration: 17
    slots:
      5: 1
      4: 4
      3: 5
      2: 6
      1: 6
      0: at-will
tactics:
  Before Combat: The bard casts expeditious retreat and see invisibility.
  During Combat: The bard uses hallucinatory terrain to befuddle and confuse enemies.
    To aid her side, she casts summon monster IV. She targets casters with silence
    and other combatants with slow, using her wand of magic missiles to aid in dealing
    damage.
ability_scores:
  STR: 14
  DEX: 14
  CON: 12
  INT: 10
  WIS: 10
  CHA: 19
BAB: 9
CMB: 11
CMD: 24
feats:
- name: Combat Reflexes
- name: Dodge
- name: Improved Critical (spear)
- name: Persuasive
- name: Point-Blank Shot
- name: Power Attack
- name: Vital Strike
- name: Weapon Focus (spear)
skills:
  Bluff: 16
  Diplomacy: 6
  Intimidate: 6
  Knowledge (arcane): 10
  Knowledge (dungeoneering): 10
  Knowledge (religion): 10
  Knowledge (geography): 15
  Knowledge (nature): 15
  Perception: 10
  Perform (dance): 20
  Perform (oratory): 20
  Perform (percussion): 20
  Sense Motive: 10
  Spellcraft: 10
  Stealth: 14
  Use Magic Device: 15
languages:
- Common
special_qualities:
- bardic knowledge +6
- jack-of-all-trades (use any skill)
- lore master 2/day
- versatile performance (oratory, percussion, dance)
gear:
  combat:
  - scrolls of bull's strength (2)
  - scroll of fog cloud
  - scroll of web
  - wand of magic missile (CL 5th, 50 charges)
  other:
  - +3 studded leather
  - +1 buckler
  - +2 spear
  - headband of alluring Charisma +2
  - 8 gp
desc_long: Tribal leaders use their abilities rather than brute strength to guide
  their tribes to victory.

---

# Tribal Leader

**Source** NPC Codex pg. 36
**XP** 19,200
Human _[[classes/Bard|bard]]_ 13

LE Medium humanoid (human)
**Init** +2; **Senses** _[[spells/See Invisibility|see invisibility]]_; Perception +10

##### Defense

**AC** 21, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+6 armor, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +2 _[[spells/Shield|shield]]_)
**hp** 78 (13d8+16)
**Fort** +5, **Ref** +10, **Will** +8; +4 vs. bardic performance, language-dependent, and sonic

##### Offense
**Speed** 30 ft.
**Melee** +2 _[[items/Weapon/Spear|spear]]_ +14/+9 (1d8+5/19–20/×3)
**Ranged** +2 _spear_ +14/+9 (1d8+4/19–20/×3)
**Special Attacks** bardic performance 32 rounds/day (swift action; countersong, dirge of _[[spells/Doom|doom]]_, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire competence +4, inspire courage +3, inspire greatness, soothing performance, _[[spells/Suggestion|suggestion]]_)
**_Bard_ Spells Known **(CL 13th; concentration +17)
5th (1/day)—mass _suggestion_ (DC 19), _[[spells/Nightmare|nightmare]]_ (DC 19)
4th (4/day)—_[[spells/Cure Critical Wounds|cure critical wounds]]_ (DC 18), _[[spells/Hallucinatory Terrain|hallucinatory terrain]]_ (DC 18), _[[spells/Speak with Plants|speak with plants]]_, _[[spells/Summon Monster IV|summon monster IV]]_
3rd (5/day)—_[[universal monster rules/Fear|fear]]_ (DC 17), _[[spells/Haste|haste]]_ (DC 17), _see invisibility_, _[[spells/Slow|slow]]_ (DC 17), _[[spells/Speak with Animals|speak with animals]]_
2nd (6/day)—cat’s _[[spells/Grace|grace]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Rage|rage]]_, _[[spells/Silence|silence]]_ (DC 16), _[[spells/Tongues|tongues]]_
1st (6/day)—_[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Grease|grease]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 15), _[[spells/Ventriloquism|ventriloquism]]_ (DC 15)
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Flare|flare]]_ (DC 14), _[[spells/Ghost Sound|ghost sound]]_ (DC 14), light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_

### Tactics

**Before Combat **The _bard_ casts _expeditious retreat_ and _see invisibility_.
**During Combat **The _bard_ uses _hallucinatory terrain_ to befuddle and confuse enemies. To aid her side, she casts _summon monster IV_. She targets casters with _silence_ and other combatants with _slow_, using her wand of magic missiles to aid in dealing damage.

##### Statistics
**Str** 14, **Dex** 14, **Con** 12, **Int** 10, **Wis** 10, **Cha** 19
**Base Atk** +9; **CMB** +11; **CMD** 24
**Feats** _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_spear_), _[[feats/Persuasive|Persuasive]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_spear_)
**Skills** Bluff +16, Diplomacy +6, Intimidate +6, Knowledge (arcane, dungeoneering, religion) +10, Knowledge (geography, nature) +15, Perception +10, Perform (dance, oratory, percussion) +20, Sense Motive +10, Spellcraft +10, Stealth +14, Use Magic Device +15
**Languages** Common
**SQ** bardic knowledge +6, jack-of-all-trades (use any skill), lore master 2/day, versatile performance (oratory, percussion, dance)
**Combat Gear** scrolls of bull’s strength (2), scroll of _[[spells/Fog Cloud|fog cloud]]_, scroll of web, wand of _[[spells/Magic Missile|magic missile]]_ (CL 5th, 50 charges); **Other Gear** +3 studded leather, +1 _[[items/Armor/Buckler|buckler]]_, +2 _spear_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring Charisma +2]]_, 8 gp

Tribal leaders use their abilities rather than brute strength to guide their tribes to victory.