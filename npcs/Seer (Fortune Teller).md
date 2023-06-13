---
cssclass: [monsters]
title1: Seer (Fortune Teller)
title2: Seer (Fortune Teller)
CR: 5
sources:
- name: GameMastery Guide
  page: 299
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 1600
race: Human
classes:
- bard 3
- sorcerer 3
alignment: CN
size: Medium
type: humanoid
initiative:
  bonus: 1
AC:
  AC: 11
  touch: 11
  flat_footed: 10
  components:
    dex: 1
HP:
  HP: 23
  long: 3d8+3d6
  HD: 6
saves:
  fort: 3
  ref: 6
  will: 8
  other: +4 vs. bardic performance, language-dependent, and sonic
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +2 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 2
  ranged:
  - - text: dagger +4 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 4
  special:
  - bardic performance 18 rounds/day (countersong, distraction, fascinate [DC 15],
    inspire competence +2, inspire courage +1)
spell_like_abilities:
  entries:
  - name: laughing touch
    source: default
    freq: 7/day
  sources:
  - name: default
    CL: 3
    concentration: 7
spells:
  entries:
  - name: cure light wounds
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 17
  - name: silent image
    source: Bard
    level: 1
    DC: 15
  - name: ventriloquism
    source: Bard
    level: 1
    DC: 15
  - name: ghost sound
    source: Bard
    level: 0
    DC: 14
  - name: know direction
    source: Bard
    level: 0
  - name: mage hand
    source: Bard
    level: 0
  - name: message
    source: Bard
    level: 0
  - name: read magic
    source: Bard
    level: 0
  - name: resistance
    source: Bard
    level: 0
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 15
  - name: entangle
    source: Sorcerer
    level: 1
    DC: 15
  - name: hypnotism
    source: Sorcerer
    level: 1
    DC: 17
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 16
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 3
    concentration: 7
    slots:
      1: 4
      0: at-will
  - name: Sorcerer
    type: known
    CL: 3
    concentration: 7
    slots:
      1: 6
      0: at-will
    bloodline: fey
ability_scores:
  STR: 8
  DEX: 13
  CON: 10
  INT: 14
  WIS: 12
  CHA: 18
BAB: 3
CMB: 2
CMD: 13
feats:
- name: Eschew Materials
- name: Extra Performance
- name: Magical Aptitude
- name: Skill Focus (Perform [act])
- name: Skill Focus (Sleight of Hand)
skills:
  Bluff: 16
  Diplomacy: 10
  Disguise: 16
  Intimidate: 10
  Knowledge (arcana): 7
  Knowledge (local): 7
  Knowledge (nature): 7
  Knowledge (planes): 7
  Knowledge (religion): 7
  Linguistics: 6
  Perception: 5
  Perform (act): 16
  Perform (oratory): 12
  Sense Motive: 10
  Sleight of Hand: 13
  Spellcraft: 10
  Use Magic Device: 15
languages:
- Aklo
- Common
- Draconic
- Sylvan
special_qualities:
- bardic knowledge +1
- bloodline arcana
- versatile performance (act)
- woodland stride
gear:
  combat:
  - scrolls of animate rope
  - comprehend languages (4)
  - erase
  - magic aura
  - magic mouth
  - wand of unseen servant (50 charges)
  - smokesticks (2)
  - thunderstones (2)
  other:
  - daggers (2)
  - cloak of resistance +1
  - non-magical crystal ball
  - tarot cards
  - augury focus
npc_boon: A fortune teller could advise PCs on the best ways to trick those in a particular
  community, granting them a +2 circumstance bonus on Bluff and Intimidate checks
  in that area for 1 week.
desc_long: ''

---

# Seer (Fortune Teller)

**Source** GameMastery Guide pg. 299
**XP** 1,600
Human _[[classes/Bard|bard]]_ 3/sorcerer 3

CN Medium humanoid
**Init** +1; **Senses** Perception +5

##### Defense

**AC** 11, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 10 (+1 Dex)
**hp** 23 (6 HD; 3d8+3d6)
**Fort** +3, **Ref** +6, **Will** +8; +4 vs. bardic performance, language-dependent, and sonic

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +2 (1d4–1/19–20)
**Ranged** _dagger_ +4 (1d4–1/19–20)
**Special Attacks** bardic performance 18 rounds/day (countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate [DC 15], inspire competence +2, inspire courage +1)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +7)
7/day—laughing touch
**_Bard_ Spells Known **(CL 3rd; concentration +7)
1st (4/day)—_[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 17), _[[spells/Silent Image|silent image]]_ (DC 15), _[[spells/Ventriloquism|ventriloquism]]_ (DC 15)
0 (at will)—_[[spells/Ghost Sound|ghost sound]]_ (DC 14), _[[spells/Know Direction|know direction]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known** (CL 3rd; concentration +7)
1st (6/day)—_[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Entangle|entangle]]_ (DC 15), _[[spells/Hypnotism|hypnotism]]_ (DC 17), _[[spells/Mage Armor|mage armor]]_
0 (at will)—_[[spells/Arcane Mark|arcane mark]]_, _[[spells/Daze|daze]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Prestidigitation|prestidigitation]]_
**Bloodline** fey

##### Statistics
**Str** 8, **Dex** 13, **Con** 10, **Int** 14, **Wis** 12, **Cha** 18
**Base Atk** +3; **CMB** +2; **CMD** 13
**Feats** _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extra Performance|Extra Performance]]_, _[[feats/Magical Aptitude|Magical Aptitude]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perform [act]), _Skill Focus_ (Sleight of Hand)
**Skills** Bluff +16, Diplomacy +10, Disguise +16, Intimidate +10, Knowledge (arcana) +7, Knowledge (local) +7, Knowledge (nature) +7, Knowledge (planes) +7, Knowledge (religion) +7, Linguistics +6, Perception +5, Perform (act) +16, Perform (oratory) +12, Sense Motive +10, Sleight of Hand +13, Spellcraft +10, Use Magic Device +15
**Languages** Aklo, Common, Draconic, Sylvan
**SQ** bardic knowledge +1, bloodline arcana, versatile performance (act), woodland stride
**Combat Gear** scrolls of _[[spells/Animate Rope|animate rope]]_, _[[spells/Comprehend Languages|comprehend languages]]_ (4), _[[spells/Erase|erase]]_, _[[spells/Magic Aura|magic aura]]_, _[[spells/Magic Mouth|magic mouth]]_, wand of _[[spells/Unseen Servant|unseen servant]]_ (50 charges), smokesticks (2), thunderstones (2); **Other Gear** daggers (2), _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, non-magical crystal ball, tarot _[[items/Mundane/Cards|cards]]_, _[[spells/Augury|augury]]_ focus

**Boon** A _[[feats/Fortune Teller|fortune teller]]_ could advise PCs on the best ways to trick those in a particular community, granting them a +2 circumstance bonus on Bluff and Intimidate checks in that area for 1 week.