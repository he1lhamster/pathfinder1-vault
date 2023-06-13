---
cssclass: [monsters]
title1: Derro, Derro Brainwasher
desc_short: This pallid woman's clothing is adorned with leather straps, wicked barbs,
  and surgical tools. Her eyes twinkle with madness.
title2: Derro Brainwasher
CR: 5
sources:
- name: Inner Sea Monster Codex
  page: 24
  link: http://paizo.com/products/btpy9elc?Pathfinder-Campaign-Setting-Inner-Sea-Monster-Codex
XP: 1600
race: Derro
classes:
- bard 2 (Pathfinder RPG Bestiary 70)
alignment: CE
size: Small
type: humanoid
subtypes:
- derro
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 22
  touch: 16
  flat_footed: 17
  components:
    armor: 4
    dex: 4
    dodge: 1
    natural: 2
    size: 1
HP:
  HP: 39
  long: 3d8+2d8+17
  HD: 5
saves:
  fort: 4
  ref: 8
  will: 10
SR: 16
weaknesses:
- vulnerable to sunlight
speeds:
  base: 20
attacks:
  melee:
  - - text: aklys +4 (1d6)
      entries:
      - - damage: 1d6
      attack: aklys
      bonus:
      - 4
  ranged:
  - - text: repeating light crossbow +8 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: repeating light crossbow
      bonus:
      - 8
  - - text: aklys +8 (1d6)
      entries:
      - - damage: 1d6
      attack: aklys
      bonus:
      - 8
  special:
  - bardic performance 17 rounds/day (countersong, distraction, fascinate [DC 16],
    inspire courage +1)
  - sneak attack +1d6
spell_like_abilities:
  entries:
  - name: darkness
    source: default
    freq: At will
  - name: ghost sound
    source: default
    freq: At will
    DC: 15
  - name: daze
    source: default
    freq: 1/day
    DC: 15
  - name: sound burst
    source: default
    freq: 1/day
    DC: 17
  sources:
  - name: default
    CL: 3
    concentration: 8
spells:
  entries:
  - name: cause fear
    source: Bard
    level: 1
    DC: 16
  - superscripts:
    - APG
    name: memory lapse
    source: Bard
    level: 1
    DC: 16
  - name: sleep
    source: Bard
    level: 1
    DC: 16
  - name: detect magic
    source: Bard
    level: 0
  - name: flare
    source: Bard
    level: 0
    DC: 15
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
  sources:
  - name: Bard
    type: known
    CL: 2
    concentration: 7
    slots:
      1: 4
      0: at-will
ability_scores:
  STR: 11
  DEX: 19
  CON: 16
  INT: 12
  WIS: 7
  CHA: 20
BAB: 3
CMB: 2
CMD: 17
feats:
- name: Combat Casting
- name: Dodge
- name: Extra Performance
skills:
  Acrobatics: 8
    when jumping: 4
  Bluff: 12
  Disguise: 10
  Escape Artist: 7
  Knowledge (geography): 6
  Knowledge (local): 6
  Linguistics: 5
  Perception: 2
  Perform (oratory): 13
  Stealth: 12
  Use Magic Device: 11
languages:
- Aklo
- Common
- Undercommon
special_qualities:
- bardic knowledge +1
- madness
- poison use
- versatile performance (oratory)
gear:
  combat:
  - wand of charm person (15 charges)
  - wand of hold person (8 charges)
  - wand of modify memory (12 charges)
  - medium spider venom (5 doses)
  - striped toadstool (5 doses)
  other:
  - mwk chain shirt
  - aklys
  - repeating light crossbow with 20 mwk bolts
ecology:
  environment: any underground
desc_long: |-
  These sinister derros specialize in the skills needed to keep their underground civilization hidden from the surface world. Years of study and experimentation provide them with an unnatural understanding of how the humanoid mind works, especially the sections governing memory. Derro brainwashers program new memories into their targets and remove unwanted memories altogether; they edit away any evidence of their people and sow chaos within a subject's psyche, leaving the unfortunate soul jabbering and confused.

  Brainwashers typically venture aboveground to examine former test subjects when their memories of Nar-Voth visits threaten to return with unwelcome clarity. Instead of killing these leaks outright, the derro would rather protect their investment and try to recover these subjects, open them up to see what went wrong, and return them after appropriate repairs. Fortunately for the brainwashers, these former guests are generally so unhinged from their experience that they're unable to hide effectively. Most rave about white-eyed abductors, slobbering in seedy taverns where they quell the horrible visions with strong drink, or are locked away in asylums when they're caught violently preparing for their tormentors' return. Once the brainwashers locate their targets, they incapacitate the unfortunate victims, bring them back underground, and alter their memories of recent events using either magic or drastic surgery. They rarely come to the surface unprepared or alone, however, and their expeditions often return with new subjects as well as old ones.

---

# Derro, Derro Brainwasher
This pallid woman’s clothing is adorned with leather straps, wicked barbs, and surgical tools. Her eyes twinkle with madness.
**Source** Inner Sea Monster Codex pg. 24
**XP** 1,600
_[[monsters/Derro|Derro]]_ _[[classes/Bard|bard]]_ 2 (Pathfinder RPG Bestiary 70)
CE Small humanoid (_derro_)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +2

##### Defense

**AC** 22, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+4 armor, +4 Dex, +1 dodge, +2 natural, +1 size)
**hp** 39 (5 HD; 3d8+2d8+17)
**Fort** +4, **Ref** +8, **Will** +10
**SR** 16
**Weaknesses** vulnerable to sunlight

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Aklys|aklys]]_ +4 (1d6)
**Ranged** _[[items/Weapon/Repeating light crossbow|repeating light crossbow]]_ +8 (1d6/19–20) or _aklys_ +8 (1d6)
**Special Attacks** bardic performance 17 rounds/day (countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate [DC 16], inspire courage +1), sneak attack +1d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +8)
At will—_[[spells/Darkness|darkness]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 15)
1/day—_[[spells/Daze|daze]]_ (DC 15), _[[spells/Sound Burst|sound burst]]_ (DC 17)
**_Bard_ Spells Known **(CL 2nd; concentration +7)
1st (4/day)—_[[spells/Cause Fear|cause fear]]_ (DC 16), _[[spells/Memory Lapse|memory lapse]]_ (DC 16), sleep (DC 16)
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 15), _[[spells/Lullaby|lullaby]]_ (DC 15), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_

##### Statistics
**Str** 11, **Dex** 19, **Con** 16, **Int** 12, **Wis** 7, **Cha** 20
**Base Atk** +3; **CMB** +2; **CMD** 17
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Extra Performance|Extra Performance]]_
**Skills** Acrobatics +8 (+4 when jumping), Bluff +12, Disguise +10, Escape Artist +7, Knowledge (geography) +6, Knowledge (local) +6, Linguistics +5, Perception +2, Perform (oratory) +13, Stealth +12, Use Magic Device +11
**Languages** Aklo, Common, Undercommon
**SQ** bardic knowledge +1, madness, poison use, versatile performance (oratory)
**Combat Gear** wand of _[[spells/Charm Person|charm person]]_ (15 charges), wand of _[[spells/Hold Person|hold person]]_ (8 charges), wand of _[[spells/Modify Memory|modify memory]]_ (12 charges), _[[poisons/Medium Spider Venom|medium spider venom]]_ (5 doses), _[[poisons/Striped Toadstool|striped toadstool]]_ (5 doses); **Other Gear** mwk _[[items/Armor/Chain shirt|chain shirt]]_, _aklys_, _repeating light crossbow_ with 20 mwk bolts

##### Ecology

**Environment** any underground

##### Description

These sinister derros specialize in the skills needed to keep their underground civilization hidden from the surface world. Years of study and experimentation provide them with an unnatural understanding of how the humanoid mind works, especially the sections governing memory. _Derro_ brainwashers program new memories into their targets and remove unwanted memories altogether; they edit away any evidence of their people and sow chaos within a subject’s psyche, leaving the unfortunate soul jabbering and _[[conditions/Confused|confused]]_.

Brainwashers typically venture aboveground to examine former test subjects when their memories of Nar-Voth visits threaten to return with unwelcome _[[items/Weapon/Clarity|clarity]]_. Instead of killing these leaks outright, the _derro_ would rather protect their investment and try to recover these subjects, open them up to see what went wrong, and return them after appropriate repairs. Fortunately for the brainwashers, these former guests are generally so unhinged from their experience that they’re unable to hide effectively. Most rave about white-eyed abductors, slobbering in seedy taverns where they quell the horrible visions with strong drink, or are locked away in asylums when they’re caught violently preparing for their tormentors’ return. Once the brainwashers locate their targets, they incapacitate the unfortunate victims, bring them back underground, and alter their memories of recent events using either magic or drastic surgery. They rarely come to the surface unprepared or alone, however, and their expeditions often return with new subjects as well as old ones.