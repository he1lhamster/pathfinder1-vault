---
cssclass: [monsters]
title1: Razmiran Priest
title2: Razmiran Priest
CR: 9
sources:
- name: Inner Sea NPC Codex
  page: 46
  link: http://paizo.com/products/btpy92lj?Pathfinder-Campaign-Setting-Inner-Sea-NPC-Codex
XP: 6400
race: Human
classes:
- sorcerer 6
- Razmiran priest 4
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 2
AC:
  AC: 12
  touch: 12
  flat_footed: 10
  components:
    dex: 2
HP:
  HP: 61
  long: 6d6+4d8+20
  HD: 10
saves:
  fort: 6
  ref: 6
  will: 8
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk heavy mace +6/+1 (1d8-1)
      entries:
      - - damage: 1d8-1
      attack: mwk heavy mace
      bonus:
      - 6
      - 1
  special:
  - false channel (2d6, 8/day)
  - staff of order (4 rounds, 1/day)
spell_like_abilities:
  entries:
  - name: touch of law
    source: default
    freq: 8/day
  - name: touch of destiny
    source: bloodline
    freq: 8/day
    other: '+3'
  sources:
  - name: default
    CL: 9
    concentration: 14
  - name: bloodline
    CL: 9
    concentration: 14
spells:
  entries:
  - name: confusion
    source: Sorcerer
    level: 4
    DC: 19
  - name: enervation
    source: Sorcerer
    level: 4
  - name: lightning bolt
    source: Sorcerer
    level: 3
    DC: 18
  - name: ray of exhaustion
    source: Sorcerer
    level: 3
    DC: 18
  - name: suggestion
    source: Sorcerer
    level: 3
    DC: 18
  - name: bless
    source: Sorcerer
    level: 2
  - name: blindness/deafness
    source: Sorcerer
    level: 2
    DC: 17
  - name: blur
    source: Sorcerer
    level: 2
  - name: cure light wounds
    source: Sorcerer
    level: 2
  - name: detect thoughts
    source: Sorcerer
    level: 2
    DC: 17
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: alarm
    source: Sorcerer
    level: 1
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 16
  - name: disguise self
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 16
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 15
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: ray of fatigue
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 9
    concentration: 14
    slots:
      4: 5
      3: 7
      2: 7
      1: 8
      0: at-will
    bloodline: destined
ability_scores:
  STR: 8
  DEX: 14
  CON: 14
  INT: 12
  WIS: 10
  CHA: 20
BAB: 6
CMB: 5
CMD: 17
feats:
- name: Combat Casting
- name: Empower Spell
- name: Eschew Materials
- name: False Casting
- name: Magical Aptitude
- name: Silent Spell
- name: Weapon Focus (ray)
skills:
  Bluff: 21
  Diplomacy: 12
  Intimidate: 18
  Knowledge (history): 5
  Knowledge (religion): 10
  Perception: 10
  Sense Motive: 7
  Sleight of Hand: 3
  Spellcraft: 10
  Use Magic Device: 25
languages:
- Common
- Hallit
special_qualities:
- bloodline arcana (gain luck bonus on saves when casting personalrange spells)
- domain of Razmir (Law domain)
- fated (+1)
- first ritual
- master of lies
gear:
  combat:
  - scroll of prayer
  - scroll of shield (CL 3rd)
  - scroll of spiritual weapon (CL 6th)
  - wand of cure light wounds (15 charges)
  - wand of shield of faith (CL 6th, 21 charges)
  other:
  - mwk heavy mace
  - circlet of persuasion
  - cloak of resistance +1
  - headband of alluring charisma +2
  - iron holy symbol of Razmir (worth 5 gp)
  - 73 gp
desc_long: 'Razmiran priests serve the same role as the clergy of most religions:
  spreading their faith and punishing heresy. Razmir's priests are quick to unleash
  their power on any who deny his divinity, or worse, who actually have evidence that
  would expose his ruse. Though they are primarily isolated in the nation of Razmiran
  itself, priests of the Living God have begun travelling throughout Avistan, particularly
  the nations on Lake Encarthan, with increasing regularity, leading some to believe
  that Razmir has some sinister plan in the works beyond simply converting more followers
  into the fold through intimidation and force.'

---

# Razmiran Priest

**Source** Inner Sea NPC Codex pg. 46
**XP** 6,400
Human _[[classes/Sorcerer|sorcerer]]_ 6/Razmiran priest 4

LE Medium humanoid (human)
**Init** +2; **Senses** Perception +10

##### Defense

**AC** 12, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 10 (+2 Dex)
**hp** 61 (10 HD; 6d6+4d8+20)
**Fort** +6, **Ref** +6, **Will** +8

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Heavy mace|heavy mace]]_ +6/+1 (1d8–1)
**Special Attacks** false channel* (2d6, 8/day), staff of order (4 rounds, 1/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 9th; concentration +14)
8/day—touch of law
**Bloodline _Spell-Like Abilities_** (CL 9th; concentration +14)
8/day—touch of destiny (+3)
**_Sorcerer_ Spells Known **(CL 9th; concentration +14)
4th (5/day)—_[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Enervation|enervation]]_
3rd (7/day)—_[[spells/Lightning Bolt|lightning bolt]]_ (DC 18), _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 18), _[[spells/Suggestion|suggestion]]_ (DC 18)
2nd (7/day)—_[[spells/Bless|bless]]_, blindness/deafness (DC 17), _[[spells/Blur|blur]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Invisibility|invisibility]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (8/day)—_[[spells/Alarm|alarm]]_, _[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Disguise Self|disguise self]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 16)
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 15), light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Prestidigitation|prestidigitation]]_, ray of fatigue, _[[spells/Read Magic|read magic]]_
**Bloodline** destined

##### Statistics
**Str** 8, **Dex** 14, **Con** 14, **Int** 12, **Wis** 10, **Cha** 20
**Base Atk** +6; **CMB** +5; **CMD** 17
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/False Casting|False Casting]]_, _[[feats/Magical Aptitude|Magical Aptitude]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (ray)
**Skills** Bluff +21, Diplomacy +12, Intimidate +18, Knowledge (history) +5, Knowledge (religion) +10, Perception +10, Sense Motive +7, Sleight of Hand +3, Spellcraft +10, Use Magic Device +25
**Languages** Common, Hallit
**SQ** bloodline arcana (gain luck bonus on saves when casting personalrange spells), domain of Razmir* (Law domain), fated (+1), first ritual*, master of lies*
**Combat Gear** scroll of _[[spells/Prayer|prayer]]_, scroll of _[[spells/Shield|shield]]_ (CL 3rd), scroll of _[[spells/Spiritual Weapon|spiritual weapon]]_ (CL 6th), wand of _cure light wounds_ (15 charges), wand of _[[spells/Shield Of Faith|shield of faith]]_ (CL 6th, 21 charges); **Other Gear** mwk _heavy mace_, _[[items/Wondrous Item/Circlet of Persuasion|circlet of persuasion]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, iron holy symbol of Razmir (worth 5 gp), 73 gp

Razmiran priests serve the same role as the clergy of most religions: spreading their faith and punishing heresy. Razmir’s priests are quick to unleash their power on any who deny his divinity, or worse, who actually have evidence that would expose his ruse. Though they are primarily isolated in the nation of Razmiran itself, priests of the Living God have begun travelling throughout Avistan, particularly the nations on Lake Encarthan, with increasing regularity, leading some to believe that Razmir has some sinister plan in the works beyond simply converting more followers into the fold through intimidation and force.