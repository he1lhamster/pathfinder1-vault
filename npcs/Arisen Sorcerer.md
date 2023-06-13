---
cssclass: [monsters]
title1: Arisen Sorcerer
title2: Arisen Sorcerer
CR: 19
sources:
- name: NPC Codex
  page: 177
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 204800
race: Human
classes:
- sorcerer 20
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 6
AC:
  AC: 30
  touch: 17
  flat_footed: 27
  components:
    armor: 4
    deflection: 4
    dex: 2
    dodge: 1
    natural: 9
HP:
  HP: 217
  long: 20d6+145
saves:
  fort: 16
  ref: 11
  will: 18
  other: +4 morale bonus vs. undead spells and spell-like abilities
DR:
- amount: 5
  weakness: '-'
immunities:
- cold
- nonlethal damage
- paralysis
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: quarterstaff +9/+4 (1d6-1)
      entries:
      - - damage: 1d6-1
      attack: quarterstaff
      bonus:
      - 9
      - 4
spell_like_abilities:
  entries:
  - name: grave touch
    source: default
    freq: 11/day
    other: 10 rounds
  - name: grasp of the dead
    source: default
    freq: 3/day
    other: 20d6 slashing
    DC: 28
  - name: incorporeal form
    source: default
    freq: 1/day
    other: 20 rounds
  sources:
  - name: default
    CL: 20
    concentration: 28
spells:
  entries:
  - name: energy drain
    source: Sorcerer
    level: 9
    DC: 29
  - name: imprisonment
    source: Sorcerer
    level: 9
    DC: 27
  - name: power word kill
    source: Sorcerer
    level: 9
  - name: wail of the banshee
    source: Sorcerer
    level: 9
    DC: 29
  - name: create greater undead
    source: Sorcerer
    level: 8
  - name: horrid wilting
    source: Sorcerer
    level: 8
    DC: 28
  - name: polar ray
    source: Sorcerer
    level: 8
  - name: protection from spells
    source: Sorcerer
    level: 8
  - name: finger of death
    source: Sorcerer
    level: 7
    DC: 27
  - name: mass hold person
    source: Sorcerer
    level: 7
    DC: 25
  - name: prismatic spray
    source: Sorcerer
    level: 7
  - name: waves of exhaustion
    source: Sorcerer
    level: 7
  - name: circle of death
    source: Sorcerer
    level: 6
    DC: 26
  - name: create undead
    source: Sorcerer
    level: 6
  - name: flesh to stone
    source: Sorcerer
    level: 6
    DC: 24
  - name: undeath to death
    source: Sorcerer
    level: 6
    DC: 26
  - name: cloudkill
    source: Sorcerer
    level: 5
    DC: 23
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 23
  - name: dominate person
    source: Sorcerer
    level: 5
    DC: 23
  - name: teleport
    source: Sorcerer
    level: 5
  - name: waves of fatigue
    source: Sorcerer
    level: 5
  - name: animate dead
    source: Sorcerer
    level: 4
  - name: contagion
    source: Sorcerer
    level: 4
    DC: 24
  - name: crushing despair
    source: Sorcerer
    level: 4
    DC: 22
  - name: solid fog
    source: Sorcerer
    level: 4
  - name: wall of ice
    source: Sorcerer
    level: 4
    DC: 22
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: fireball
    source: Sorcerer
    level: 3
    DC: 21
  - name: gaseous form
    source: Sorcerer
    level: 3
  - name: ray of exhaustion
    source: Sorcerer
    level: 3
    DC: 23
  - name: vampiric touch
    source: Sorcerer
    level: 3
  - name: blindness/deafness
    source: Sorcerer
    level: 2
    DC: 22
  - name: false life
    source: Sorcerer
    level: 2
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: spectral hand
    source: Sorcerer
    level: 2
  - name: chill touch
    source: Sorcerer
    level: 1
    DC: 21
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 21
  - name: shield
    source: Sorcerer
    level: 1
  - name: shocking grasp
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 20
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: disrupt undead
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 18
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 20
  sources:
  - name: Sorcerer
    type: known
    CL: 20
    concentration: 28
    slots:
      9: 6
      8: 7
      7: 7
      6: 7
      5: 7
      4: 8
      3: 8
      2: 8
      1: 8
      0: at-will
    bloodline: undead
tactics:
  Before Combat: The sorcerer casts false life and mage armor.
  During Combat: The sorcerer casts energy drain, power word kill, and wail of the
    banshee. She may deter opponents with solid fog, waves of exhaustion, or her grasp
    of the dead ability.
  Base Statistics: Without false life and mage armor, the sorcerer's statistics are
    AC 26, touch 17, flat-footed 23; hp 202.
ability_scores:
  STR: 8
  DEX: 14
  CON: 20
  INT: 10
  WIS: 12
  CHA: 27
BAB: 10
CMB: 9
CMD: 26
feats:
- name: Blind-Fight
- name: Combat Casting
- name: Dodge
- name: Empower Spell
- name: Eschew Materials
- name: Great Fortitude
- name: Greater Spell Focus (necromancy)
- name: Improved Initiative
- name: Iron Will
- name: Mobility
- name: Quicken Spell
- name: Silent Spell
- name: Spell Focus (necromancy)
- name: Still Spell
- name: Toughness
skills:
  Fly: 10
  Intimidate: 21
  Knowledge (arcana): 13
  Knowledge (religion): 13
  Perception: 16
  Spellcraft: 13
  Use Magic Device: 21
languages:
- Common
special_qualities:
- bloodline arcana (corporeal undead affected by humanoid-affecting spells)
- one of us
gear:
  combat:
  - scrolls of darkvision (2)
  - scrolls of fly (2)
  - scroll of see invisibility
  - wand of cure moderate wounds (25 charges)
  other:
  - quarterstaff
  - amulet of natural armor +4
  - belt of mighty constitution +6
  - cloak of resistance +3
  - headband of alluring charisma +6
  - ring of protection +4
  - robe of bones
  - diamonds for protection from spells (worth 1,500 gp)
  - onyx gems (worth 2,000 gp)
  - 4,650 gp
desc_long: There is no description for this NPC.

---

# Arisen Sorcerer

**Source** NPC Codex pg. 177
**XP** 204,800
Human _[[classes/Sorcerer|sorcerer]]_ 20

LE Medium humanoid (human)
**Init** +6; **Senses** Perception +16

##### Defense

**AC** 30, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+4 armor, +4 _[[spells/Deflection|deflection]]_, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +9 natural)
**hp** 217 (20d6+145)
**Fort** +16, **Ref** +11, **Will** +18; +4 morale bonus vs. undead spells and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**DR** 5/—; **Immune** cold, nonlethal damage, _[[universal monster rules/Paralysis|paralysis]]_, sleep

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Quarterstaff|quarterstaff]]_ +9/+4 (1d6–1)
**_Spell-Like Abilities_** (CL 20th; concentration +28)
11/day—grave touch (10 rounds)
3/day—_[[spells/Grasp|grasp]]_ of the dead (20d6 slashing, DC 28)
1/day—_[[universal monster rules/Incorporeal|incorporeal]]_ form (20 rounds)
**_Sorcerer_ Spells Known **(CL 20th; concentration +28)
9th (6/day)—_[[universal monster rules/Energy Drain|energy drain]]_ (DC 29), _[[spells/Imprisonment|imprisonment]]_ (DC 27), _[[spells/Power Word Kill|power word kill]]_, _[[spells/Wail of the Banshee|wail of the banshee]]_ (DC 29)
8th (7/day)—_[[spells/Create Greater Undead|create greater undead]]_, _[[spells/Horrid Wilting|horrid wilting]]_ (DC 28), _[[spells/Polar Ray|polar ray]]_, _[[spells/Protection from Spells|protection from spells]]_
7th (7/day)—_[[spells/Finger Of Death|finger of death]]_ (DC 27), mass _[[spells/Hold Person|hold person]]_ (DC 25), _[[spells/Prismatic Spray|prismatic spray]]_, _[[spells/Waves of Exhaustion|waves of exhaustion]]_
6th (7/day)—_[[spells/Circle Of Death|circle of death]]_ (DC 26), _[[spells/Create Undead|create undead]]_, _[[spells/Flesh to Stone|flesh to stone]]_ (DC 24), _[[spells/Undeath to Death|undeath to death]]_ (DC 26)
5th (7/day)—_[[spells/Cloudkill|cloudkill]]_ (DC 23), _[[spells/Cone of Cold|cone of cold]]_ (DC 23), _[[spells/Dominate Person|dominate person]]_ (DC 23), teleport, _[[spells/Waves of Fatigue|waves of fatigue]]_
4th (8/day)—_[[spells/Animate Dead|animate dead]]_, _[[spells/Contagion|contagion]]_ (DC 24), _[[spells/Crushing Despair|crushing despair]]_ (DC 22), _[[spells/Solid Fog|solid fog]]_, _[[spells/Wall Of Ice|wall of ice]]_ (DC 22)
3rd (8/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 21), _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 23), _[[spells/Vampiric Touch|vampiric touch]]_
2nd (8/day)—blindness/deafness (DC 22), _[[spells/False Life|false life]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Scorching Ray|scorching ray]]_, _[[spells/Spectral Hand|spectral hand]]_
1st (8/day)—_[[spells/Chill Touch|chill touch]]_ (DC 21), _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 21), _[[spells/Shield|shield]]_, _[[spells/Shocking Grasp|shocking grasp]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 20), _[[spells/Detect Magic|detect magic]]_, _[[spells/Disrupt Undead|disrupt undead]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 18), _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 20)
**Bloodline **undead

### Tactics

**Before Combat **The _sorcerer_ casts _false life_ and _mage armor_.
**During Combat **The _sorcerer_ casts _energy drain_, _power word kill_, and _wail of the banshee_. She may deter opponents with _solid fog_, _waves of exhaustion_, or her _grasp_ of the dead ability.
**Base Statistics **Without _false life_ and _mage armor_, the _sorcerer_’s statistics are **AC **26, touch 17, _flat-footed_ 23; **hp **202.

##### Statistics
**Str** 8, **Dex** 14, **Con** 20, **Int** 10, **Wis** 12, **Cha** 27
**Base Atk** +10; **CMB** +9; **CMD** 26
**Feats** _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (necromancy), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (necromancy), _[[feats/Still Spell|Still Spell]]_, _[[feats/Toughness|Toughness]]_
**Skills** Fly +10, Intimidate +21, Knowledge (arcana, religion) +13, Perception +16, Spellcraft +13, Use Magic Device +21
**Languages** Common
**SQ** bloodline arcana (corporeal undead affected by humanoid-affecting spells), one of us
**Combat Gear** scrolls of _[[spells/Darkvision|darkvision]]_ (2), scrolls of fly (2), scroll of _[[spells/See Invisibility|see invisibility]]_, wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (25 charges); **Other Gear** _quarterstaff_, _[[items/Wondrous Item/Amulet of Natural Armor +4|amulet of natural armor +4]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +6|belt of mighty constitution +6]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +6|headband of alluring charisma +6]]_, _[[items/Ring/Ring of Protection +4|ring of protection +4]]_, _[[items/Wondrous Item/Robe of Bones|robe of bones]]_, diamonds for _protection from spells_ (worth 1,500 gp), onyx gems (worth 2,000 gp), 4,650 gp

There is no description for this NPC.