---
cssclass: [monsters]
title1: Acid Terror
title2: Acid Terror
CR: 12
sources:
- name: NPC Codex
  page: 213
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 19200
race: Human
classes:
- sorcerer 9
- dragon disciple 4
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 6
AC:
  AC: 24
  touch: 15
  flat_footed: 21
  components:
    armor: 4
    deflection: 2
    dex: 2
    dodge: 1
    natural: 5
HP:
  HP: 108
  long: 9d6+4d12+48
saves:
  fort: 9
  ref: 10
  will: 11
resistances:
  acid: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: 2 claws +10 (1d6+3 plus 1d6 acid)
      entries:
      - - damage: 1d6+3
        - damage: 1d6
          type: acid
      count: 2
      attack: claws
      bonus:
      - 10
    - text: bite +10 (1d6+4)
      entries:
      - - damage: 1d6+4
      attack: bite
      bonus:
      - 10
  - - text: quarterstaff +10/+5 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: quarterstaff
      bonus:
      - 10
      - 5
  special:
  - breath weapon (30-foot cone, 13d6 acid, DC 22, 2/day)
  - claws (2, 1d6+3 plus 1d6 acid, magic, 9 rounds/day)
  - dragon bite
spells:
  entries:
  - name: acid fog
    source: Sorcerer
    level: 6
  - name: form of the dragon I
    source: Sorcerer
    level: 6
  - name: cloudkill
    source: Sorcerer
    level: 5
    DC: 23
  - name: feeblemind
    source: Sorcerer
    level: 5
    DC: 22
  - name: spell resistance
    source: Sorcerer
    level: 5
  - name: black tentacles
    source: Sorcerer
    level: 4
  - name: confusion
    source: Sorcerer
    level: 4
    DC: 21
  - name: dimension door
    source: Sorcerer
    level: 4
  - name: fear
    source: Sorcerer
    level: 4
    DC: 20
  - name: displacement
    source: Sorcerer
    level: 3
  - name: fly
    source: Sorcerer
    level: 3
  - name: hold person
    source: Sorcerer
    level: 3
    DC: 20
  - name: stinking cloud
    source: Sorcerer
    level: 3
    DC: 21
  - name: suggestion
    source: Sorcerer
    level: 3
    DC: 20
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: glitterdust
    source: Sorcerer
    level: 2
    DC: 20
  - name: hideous laughter
    source: Sorcerer
    level: 2
    DC: 19
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: web
    source: Sorcerer
    level: 2
    DC: 20
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 18
  - name: color spray
    source: Sorcerer
    level: 1
    DC: 17
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: reduce person
    source: Sorcerer
    level: 1
    DC: 17
  - name: silent image
    source: Sorcerer
    level: 1
    DC: 17
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: daze
    source: Sorcerer
    level: 0
    DC: 17
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: open/close
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 12
    concentration: 18
    slots:
      6: 4
      5: 6
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
    bloodline: draconic (green)
tactics:
  Before Combat: As soon as she suspects combat is imminent, the dragon disciple casts
    mage armor and spell resistance.
  During Combat: The dragon disciple prefers to keep her distance, and starts combat
    by casting quickened web followed by acid fog. She then casts fly, black tentacles,
    acid arrow, feeblemind, and cloudkill, with judicious uses of Quickened Spell.
  Base Statistics: Without mage armor, the dragon disciple's statistics are AC 20,
    touch 15, flat-footed 17.
ability_scores:
  STR: 16
  DEX: 14
  CON: 15
  INT: 10
  WIS: 8
  CHA: 22
BAB: 7
CMB: 10
CMD: 25
feats:
- name: Combat Casting
- name: Dodge
- name: Eschew Materials
- name: Greater Spell Focus (conjuration)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Quicken Spell
- name: Spell Focus (conjuration)
- name: Spell Focus (enchantment)
- name: Toughness
skills:
  Climb: 4
  Fly: 6
  Intimidate: 19
  Knowledge (arcana): 8
  Linguistics: 1
  Perception: 12
  Spellcraft: 7
  Stealth: 9
languages:
- Common
- Draconic
special_qualities:
- blood of dragons
- bloodline arcana (acid spells deal +1 damage per die)
gear:
  combat:
  - potion of cure serious wounds
  - potion of delay poison
  - wand of detect thoughts (15 charges)
  other:
  - quarterstaff
  - amulet of natural armor +1
  - belt of mighty constitution +2
  - cloak of resistance +2
  - hat of disguise
  - headband of alluring charisma +2
  - ring of protection +2
  - 800 gp
desc_long: Cunning and manipulative, these dragon disciples trap their foes with schemes
  and spells before showering them with deadly acid.

---

# Acid Terror

**Source** NPC Codex pg. 213
**XP** 19,200
Human _[[classes/Sorcerer|sorcerer]]_ 9/dragon disciple 4

LE Medium humanoid (human)
**Init** +6; **Senses** Perception +12

##### Defense

**AC** 24, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 armor, +2 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +5 natural)
**hp** 108 (9d6+4d12+48)
**Fort** +9, **Ref** +10, **Will** +11
**Resist** acid 10

##### Offense
**Speed** 30 ft.
**Melee** 2 claws +10 (1d6+3 plus 1d6 acid), bite +10 (1d6+4) or _[[items/Weapon/Quarterstaff|quarterstaff]]_ +10/+5 (1d6+3)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-foot cone, 13d6 acid, DC 22, 2/day), claws (2, 1d6+3 plus 1d6 acid, magic, 9 rounds/day), dragon bite
**_Sorcerer_ Spells Known **(CL 12th; concentration +18)
6th (4/day)—_[[spells/Acid Fog|acid fog]]_, _[[spells/Form of the Dragon I|form of the dragon I]]_
5th (6/day)—_[[spells/Cloudkill|cloudkill]]_ (DC 23), _[[spells/Feeblemind|feeblemind]]_ (DC 22), _[[universal monster rules/Spell Resistance|spell resistance]]_
4th (7/day)—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Confusion|confusion]]_ (DC 21), _[[spells/Dimension Door|dimension door]]_, _[[universal monster rules/Fear|fear]]_ (DC 20)
3rd (7/day)—_[[spells/Displacement|displacement]]_, fly, _[[spells/Hold Person|hold person]]_ (DC 20), _[[spells/Stinking Cloud|stinking cloud]]_ (DC 21), _[[spells/Suggestion|suggestion]]_ (DC 20)
2nd (8/day)—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 20), _[[spells/Hideous Laughter|hideous laughter]]_ (DC 19), _[[spells/Invisibility|invisibility]]_, _[[spells/Resist Energy|resist energy]]_, web (DC 20)
1st (8/day)—_[[spells/Charm Person|charm person]]_ (DC 18), _[[spells/Color Spray|color spray]]_ (DC 17), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Reduce Person|reduce person]]_ (DC 17), _[[spells/Silent Image|silent image]]_ (DC 17)
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Daze|daze]]_ (DC 17), _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, open/close, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_
**Bloodline **draconic (green)

### Tactics

**Before Combat **As soon as she suspects combat is imminent, the dragon disciple casts _mage armor_ and _spell resistance_.
**During Combat **The dragon disciple prefers to keep her distance, and starts combat by casting quickened web followed by _acid fog_. She then casts fly, _black tentacles_, _acid arrow_, _feeblemind_, and _cloudkill_, with judicious uses of Quickened Spell.
**Base Statistics **Without _mage armor_, the dragon disciple’s statistics are **AC **20, touch 15, _flat-footed_ 17.

##### Statistics
**Str** 16, **Dex** 14, **Con** 15, **Int** 10, **Wis** 8, **Cha** 22
**Base Atk** +7; **CMB** +10; **CMD** 25
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (conjuration), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration, enchantment), _[[feats/Toughness|Toughness]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +4, Fly +6, Intimidate +19, Knowledge (arcana) +8, Linguistics +1, Perception +12, Spellcraft +7, Stealth +9
**Languages** Common, Draconic
**SQ** blood of dragons, bloodline arcana (acid spells deal +1 damage per die)
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, potion of _[[spells/Delay Poison|delay poison]]_, wand of _[[spells/Detect Thoughts|detect thoughts]]_ (15 charges); **Other Gear** _quarterstaff_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Hat of Disguise|hat of disguise]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 800 gp

_[[items/Weapon Magic Abilities/Cunning|Cunning]]_ and manipulative, these dragon disciples trap their foes with schemes and spells before showering them with _[[items/Weapon Magic Abilities/Deadly|deadly]]_ acid.