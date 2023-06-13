---
cssclass: [monsters]
title1: Death Master
title2: Death Master
CR: 16
sources:
- name: NPC Codex
  page: 230
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Half-elf
classes:
- cleric of Urgathoa 5
- evoker 5
- mystic theurge 7
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
- human
initiative:
  bonus: 4
senses:
  low-light vision: true
AC:
  AC: 28
  touch: 13
  flat_footed: 28
  components:
    armor: 12
    deflection: 3
    natural: 3
HP:
  HP: 182
  long: 5d8+5d6+7d6+100
saves:
  fort: 14
  ref: 7
  will: 20
  other: +2 vs. enchantments
immunities:
- charm monster
- fireball
- lightning bolt
- sleep
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 heavy mace +10/+5 (1d8+2)
      entries:
      - - damage: 1d8+2
      attack: +1 heavy mace
      bonus:
      - 10
      - 5
  special:
  - channel negative energy 4/day (DC 11, 3d6)
  - hand of the acolyte (8/day)
  - intense spells (+2 damage)
spell_like_abilities:
  entries:
  - name: bleeding touch
    source: default
    freq: 8/day
    other: 2 rounds
  - name: force missile
    source: evoker
    freq: 6/day
    other: 1d4+2
  sources:
  - name: default
    CL: 5
    concentration: 10
  - name: evoker
    CL: 5
    concentration: 8
spells:
  entries:
  - is_domain_spell: true
    name: antimagic field
    source: Cleric
    level: 6
  - name: heal
    source: Cleric
    level: 6
  - name: word of recall
    source: Cleric
    level: 6
  - name: flame strike
    source: Cleric
    level: 5
    count: 3
    DC: 20
  - is_domain_spell: true
    name: slay living
    source: Cleric
    level: 5
    DC: 20
  - name: wall of stone
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: death ward
    source: Cleric
    level: 4
  - name: dimensional anchor
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: spell immunity
    source: Cleric
    level: 4
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 19
  - name: contagion
    source: Cleric
    level: 3
    count: 2
    DC: 18
  - is_domain_spell: true
    name: dispel magic
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: prayer
    source: Cleric
    level: 3
  - name: summon monster III
    source: Cleric
    level: 3
  - name: cure moderate wounds
    source: Cleric
    level: 2
    count: 2
  - is_domain_spell: true
    name: death knell
    source: Cleric
    level: 2
    DC: 17
  - name: hold person
    source: Cleric
    level: 2
    DC: 17
  - name: silence
    source: Cleric
    level: 2
    DC: 17
  - name: spiritual weapon
    source: Cleric
    level: 2
  - is_domain_spell: true
    name: cause fear
    source: Cleric
    level: 1
    DC: 16
  - name: cure light wounds
    source: Cleric
    level: 1
    count: 3
  - name: deathwatch
    source: Cleric
    level: 1
  - name: entropic shield
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 15
  - name: detect poison
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  - name: stabilize
    source: Cleric
    level: 0
  - name: forceful hand
    source: Evoker
    level: 6
  - name: freezing sphere
    source: Evoker
    level: 6
    DC: 19
  - name: mislead
    source: Evoker
    level: 6
  - name: stilled dimension door
    source: Evoker
    level: 5
  - name: telekinesis
    source: Evoker
    level: 5
  - name: wall of force
    source: Evoker
    level: 5
    count: 2
  - name: black tentacles
    source: Evoker
    level: 4
  - name: fire shield
    source: Evoker
    level: 4
  - name: stilled fireball
    source: Evoker
    level: 4
  - name: greater invisibility
    source: Evoker
    level: 4
  - name: displacement
    source: Evoker
    level: 3
  - name: fireball
    source: Evoker
    level: 3
    DC: 16
  - name: fly
    source: Evoker
    level: 3
  - name: haste
    source: Evoker
    level: 3
  - name: invisibility sphere
    source: Evoker
    level: 3
  - name: lightning bolt
    source: Evoker
    level: 3
    DC: 16
  - name: false life
    source: Evoker
    level: 2
  - name: flaming sphere
    source: Evoker
    level: 2
    DC: 15
  - name: gust of wind
    source: Evoker
    level: 2
    DC: 15
  - name: invisibility
    source: Evoker
    level: 2
  - name: mirror image
    source: Evoker
    level: 2
  - name: misdirection
    source: Evoker
    level: 2
  - name: comprehend languages
    source: Evoker
    level: 1
  - name: expeditious retreat
    source: Evoker
    level: 1
  - name: feather fall
    source: Evoker
    level: 1
  - name: magic missile
    source: Evoker
    level: 1
    count: 2
  - name: unseen servant
    source: Evoker
    level: 1
  - name: dancing lights
    source: Evoker
    level: 0
  - name: detect magic
    source: Evoker
    level: 0
  - name: mage hand
    source: Evoker
    level: 0
  - name: read magic
    source: Evoker
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 12
    concentration: 17
    slots:
      0: at-will
    domains:
    - death
    - magic
  - name: Evoker
    type: prepared
    CL: 12
    concentration: 15
    failure_chance: 15%
    slots:
      0: at-will
    opposition_schools:
    - abjuration
    - enchantment
tactics:
  Before Combat: The mystic theurge casts deathwatch, false life, freedom of movement,
    and spell immunity.
  During Combat: The mystic theurge casts attack and slaying spells.
  Base Statistics: Without false life and spell immunity, the theurge's statistics
    are hp 168; Immune sleep.
ability_scores:
  STR: 12
  DEX: 10
  CON: 18
  INT: 16
  WIS: 20
  CHA: 8
BAB: 8
CMB: 9
CMD: 22
feats:
- name: Arcane Armor Mastery
- name: Arcane Armor Training
- name: Combat Casting
- name: Command Undead
- name: Craft Magic Arms and Armor
- name: Craft Wondrous Item
- name: Extra Channel
- name: Improved Initiative
- name: Scribe Scroll
- name: Skill Focus (Perception)
- name: Still Spell
- name: Toughness
skills:
  Heal: 13
  Intimidate: 9
  Knowledge (arcana): 16
  Knowledge (planes): 16
  Knowledge (dungeoneering): 11
  Knowledge (history): 11
  Knowledge (local): 11
  Knowledge (religion): 11
  Perception: 28
  Ride: 0
  Spellcraft: 16
languages:
- Abyssal
- Common
- Elven
- Infernal
- Undercommon
special_qualities:
- aura
- arcane bond (staff of swarming insects)
- combined spells (4th)
- elf blood
gear:
  combat:
  - staff of swarming insects
  other:
  - +3 mithral full plate
  - +1 heavy mace
  - amulet of natural armor +3
  - belt of mighty constitution +4
  - cloak of resistance +3
  - hat of disguise
  - headband of mental prowess +4 (Int, Wis)
  - ring of protection +3
  - 5,838 gp
desc_long: A death master slings a spell with each stride.

---

# Death Master

**Source** NPC Codex pg. 230
**XP** 76,800
Half-elf _[[classes/Cleric|cleric]]_ of Urgathoa 5/evoker 5/mystic theurge 7

NE Medium humanoid (elf, human)
**Init** +4; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +28

##### Defense

**AC** 28, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+12 armor, +3 _[[spells/Deflection|deflection]]_, +3 natural)
**hp** 182 (5d8+5d6+7d6+100)
**Fort** +14, **Ref** +7, **Will** +20; +2 vs. enchantments
**Immune** _[[spells/Charm Monster|charm monster]]_, _[[spells/Fireball|fireball]]_, _[[spells/Lightning Bolt|lightning bolt]]_, sleep

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Heavy mace|heavy mace]]_ +10/+5 (1d8+2)
**Special Attacks** channel negative energy 4/day (DC 11, 3d6), hand of the _[[npcs/Acolyte|acolyte]]_ (8/day), intense spells (+2 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 5th; concentration +10)
8/day—bleeding touch (2 rounds)
**Evoker _Spell-Like Abilities_ **(CL 5th; concentration +8)
6/day—force missile (1d4+2)
**_Cleric_ Spells Prepared **(CL 12th; concentration +17)
6th—_[[spells/Antimagic Field|antimagic field]]_, _[[spells/Heal|heal]]_, _[[spells/Word of Recall|word of recall]]_
5th—_[[spells/Flame Strike|flame strike]]_ (3, DC 20), _[[spells/Slay Living|slay living]]_ (DC 20), _[[spells/Wall Of Stone|wall of stone]]_
4th—_[[spells/Death Ward|death ward]]_, _[[spells/Dimensional Anchor|dimensional anchor]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Spell Immunity|spell immunity]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3rd—_[[spells/Contagion|contagion]]_ (2, DC 18), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Prayer|prayer]]_, _[[spells/Summon Monster III|summon monster III]]_
2nd—_[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), _[[spells/Death Knell|death knell]]_ (DC 17), _[[spells/Hold Person|hold person]]_ (DC 17), _[[spells/Silence|silence]]_ (DC 17), _[[spells/Spiritual Weapon|spiritual weapon]]_
1st—_[[spells/Cause Fear|cause fear]]_ (DC 16), _[[spells/Cure Light Wounds|cure light wounds]]_ (3), _[[spells/Deathwatch|deathwatch]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Obscuring Mist|obscuring mist]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Poison|detect poison]]_, _[[spells/Mending|mending]]_, stabilize
**D **Domain spell; **Domains **Death, Magic
**Evoker Spells Prepared **(CL 12th; concentration +15; 15% spell failure)
6th—_[[spells/Forceful Hand|forceful hand]]_, _[[spells/Freezing Sphere|freezing sphere]]_ (DC 19), _[[spells/Mislead|mislead]]_
5th—stilled _[[spells/Dimension Door|dimension door]]_, _[[spells/Telekinesis|telekinesis]]_, _[[spells/Wall Of Force|wall of force]]_ (2)
4th—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Fire Shield|fire shield]]_, stilled _fireball_, greater _[[spells/Invisibility|invisibility]]_
3rd—_[[spells/Displacement|displacement]]_, _fireball_ (DC 16), fly, _[[spells/Haste|haste]]_, _[[spells/Invisibility Sphere|invisibility sphere]]_, _lightning bolt_ (DC 16)
2nd—_[[spells/False Life|false life]]_, _[[spells/Flaming Sphere|flaming sphere]]_ (DC 15), _[[spells/Gust Of Wind|gust of wind]]_ (DC 15), _invisibility_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Misdirection|misdirection]]_
1st—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Magic Missile|magic missile]]_ (2), _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_
**Opposition Schools **abjuration, enchantment

### Tactics

**Before Combat **The mystic theurge casts _deathwatch_, _false life_, _freedom of movement_, and _spell immunity_.
**During Combat **The mystic theurge casts attack and slaying spells.
**Base Statistics **Without _false life_ and _spell immunity_, the theurge’s statistics are **hp **168; **Immune **sleep.

##### Statistics
**Str** 12, **Dex** 10, **Con** 18, **Int** 16, **Wis** 20, **Cha** 8
**Base Atk** +8; **CMB** +9; **CMD** 22
**Feats** _[[feats/Arcane Armor Mastery|Arcane Armor Mastery]]_, _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Still Spell|Still Spell]]_, _[[feats/Toughness|Toughness]]_
**Skills** _Heal_ +13, Intimidate +9, Knowledge (arcana, planes) +16, Knowledge (dungeoneering, history, local, religion) +11, Perception +28, Ride +0, Spellcraft +16
**Languages** Abyssal, Common, Elven, Infernal, Undercommon
**SQ** aura, arcane bond (_[[items/Staff/Staff of Swarming Insects|staff of swarming insects]]_), combined spells (4th), elf blood
**Combat Gear** _staff of swarming insects_; **Other Gear** +3 mithral _[[items/Armor/Full plate|full plate]]_, +1 _heavy mace_, _[[items/Wondrous Item/Amulet of Natural Armor +3|amulet of natural armor +3]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +4|belt of mighty constitution +4]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Hat of Disguise|hat of disguise]]_, _[[items/Wondrous Item/Headband of Mental Prowess +4|headband of mental prowess +4]]_ (Int, Wis), _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, 5,838 gp

A _[[npcs/Death Master|death master]]_ slings a spell with each stride.