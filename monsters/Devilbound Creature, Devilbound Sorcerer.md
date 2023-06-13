---
cssclass: [monsters]
title1: Devilbound Creature, Devilbound Sorcerer
desc_short: This elegant and mysterious woman has a sinister air of dark power around
  her, like a protective ward.
title2: Devilbound Sorcerer
CR: 13
sources:
- name: Bestiary 4
  page: 56
  link: http://paizo.com/products/btpy91ds?Pathfinder-Roleplaying-Game-Bestiary-4
XP: 25600
race: Female
classes:
- pit fiend-bound human sorcerer 13
alignment: LE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 4
senses:
  darkvision: 60
  see in darkness: true
AC:
  AC: 21
  touch: 10
  flat_footed: 21
  components:
    armor: 4
    natural: 7
HP:
  HP: 121
  long: 13d6+73
  regeneration: 5
  regeneration_weakness: good spells, good weapons
saves:
  fort: 13
  ref: 7
  will: 12
  other: +4 vs. poison
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 130
resistances:
  cold: 20
  fire: 30
weaknesses:
- contract bound
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +5/+0 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 5
      - 0
spell_like_abilities:
  entries:
  - name: quickened fireball
    source: default
    freq: 3/day
    DC: 20
  - name: invisibility
    source: default
    freq: 3/day
  - name: blasphemy
    source: default
    freq: 1/day
    DC: 24
  - name: summon
    source: default
    freq: 1/day
    level: 7
    summons:
    - name: lemure
      amount: 1
    - name: bearded devil
      amount: 1
    - name: erinyes
      amount: 1
      chance: 100%
  - name: elemental ray
    source: bloodline
    freq: 10/day
    other: 1d6+6 cold
  - name: elemental blast
    source: bloodline
    freq: 1/day
    other: 13d6 cold
    DC: 23
  sources:
  - name: default
    CL: 13
    concentration: 20
  - name: bloodline
    CL: 13
    concentration: 20
spells:
  entries:
  - name: acid fog
    source: Sorcerer
    level: 6
  - name: elemental body III
    source: Sorcerer
    level: 6
  - name: summon monster VI
    source: Sorcerer
    level: 6
  - name: cloudkill
    source: Sorcerer
    level: 5
    DC: 23
  - name: elemental body II
    source: Sorcerer
    level: 5
  - name: summon monster V
    source: Sorcerer
    level: 5
  - name: teleport
    source: Sorcerer
    level: 5
  - name: charm monster
    source: Sorcerer
    level: 4
    DC: 22
  - name: confusion
    source: Sorcerer
    level: 4
    DC: 22
  - name: elemental body I
    source: Sorcerer
    level: 4
  - name: fear
    source: Sorcerer
    level: 4
    DC: 21
  - name: stoneskin
    source: Sorcerer
    level: 4
    other: already cast
  - name: displacement
    source: Sorcerer
    level: 3
  - name: hold person
    source: Sorcerer
    level: 3
    DC: 21
  - name: protection from energy
    source: Sorcerer
    level: 3
  - name: stinking cloud
    source: Sorcerer
    level: 3
    DC: 21
  - name: summon monster III
    source: Sorcerer
    level: 3
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: darkness
    source: Sorcerer
    level: 2
  - name: detect thoughts
    source: Sorcerer
    level: 2
    DC: 19
  - name: glitterdust
    source: Sorcerer
    level: 2
    DC: 20
  - name: scorching ray
    source: Sorcerer
    level: 2
    other: cold
  - name: web
    source: Sorcerer
    level: 2
    DC: 20
  - name: burning hands
    source: Sorcerer
    level: 1
    other: cold
    DC: 18
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 19
  - name: disguise self
    source: Sorcerer
    level: 1
  - name: feather fall
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
    other: already cast
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: ghost sound
    source: Sorcerer
    level: 0
    DC: 17
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: mending
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: prestidigitation
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  sources:
  - name: Sorcerer
    type: known
    CL: 13
    concentration: 20
    slots:
      6: 5
      5: 7
      4: 6
      3: 8
      2: 8
      1: 7
      0: at-will
    bloodline: elemental (water)
ability_scores:
  STR: 8
  DEX: 10
  CON: 18
  INT: 15
  WIS: 12
  CHA: 24
BAB: 6
CMB: 5
CMD: 15
feats:
- superscripts:
  - APG
  name: Arcane Shield
- name: Augment Summoning
- name: Combat Casting
- name: Craft Wondrous Item
- name: Empower Spell
- name: Eschew Materials
- name: Great Fortitude
- name: Improved Initiative
- name: Spell Focus (conjuration)
- name: Spell Focus (enchantment)
- superscripts:
  - APG
  name: Superior Summoning
skills:
  Diplomacy: 13
  Intimidate: 17
  Knowledge (arcana): 18
  Knowledge (planes): 18
  Perception: 14
  Sense Motive: 14
languages:
- Common
- Draconic
- Infernal
special_qualities:
- bloodline arcana (change energy damage spells to cold)
ecology:
  environment: any urban
  organization: solitary
  treasure_type: NPC Gear
  treasure:
  - dagger
  - amulet of natural armor +3
  - belt of mighty constitution +2
  - cloak of resistance +3
  - headband of alluring charisma +4
  - brooch of shielding [50 points]
  - potion of cure serious wounds
  - wand of false life [10 charges]
  - diamond dust [250 gp]
  - other treasure
desc_long: A devilbound creature has made a bargain with a devil, promising a service
  and its soul in exchange for infernal power. The specif ic service depends on the
  devil's type and motivations, but always furthers the interests of Hell.

---

# Devilbound Creature, Devilbound Sorcerer
This elegant and mysterious woman has a sinister air of dark power around her, like a protective ward.
**Source** Bestiary 4 pg. 56
**XP** 25,600
Female pit fiend-bound human _[[classes/Sorcerer|sorcerer]]_ 13

LE Medium humanoid (human)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/See in Darkness|see in darkness]]_; Perception +14

##### Defense

**AC** 21, touch 10, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 armor, +7 natural)
**hp** 121 (13d6+73); _[[universal monster rules/Regeneration|regeneration]]_ 5 (good spells, good weapons)
**Fort** +13, **Ref** +7, **Will** +12; +4 vs. poison
**DR** 10/adamantine (130 points); **Resist** cold 20, fire 30
**Weaknesses** contract bound

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +5/+0 (1d4–1/19–20)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 13th; concentration +20)
3/day—quickened _[[spells/Fireball|fireball]]_ (DC 20), _[[spells/Invisibility|invisibility]]_
 1/day—_[[spells/Blasphemy|blasphemy]]_ (DC 24), _[[universal monster rules/Summon|summon]]_ (level 7, 1 lemure, 1 bearded devil, or 1 erinyes 100%)
 **Bloodline _Spell-Like Abilities_** (CL 13th; concentration +20)
 10/day—elemental ray (1d6+6 cold)
 1/day—elemental blast (13d6 cold, DC 23)
**_Sorcerer_ Spells Known **(CL 13th; concentration +20)
6th (5/day)—_[[spells/Acid Fog|acid fog]]_, _[[spells/Elemental Body III|elemental body III]]_, _[[spells/Summon Monster VI|summon monster VI]]_
5th (7/day)—_[[spells/Cloudkill|cloudkill]]_ (DC 23), _[[spells/Elemental Body II|elemental body II]]_, _[[spells/Summon Monster V|summon monster V]]_, teleport
4th (6/day)—_[[spells/Charm Monster|charm monster]]_ (DC 22), _[[spells/Confusion|confusion]]_ (DC 22), _[[spells/Elemental Body I|elemental body I]]_, _[[universal monster rules/Fear|fear]]_ (DC 21), _[[spells/Stoneskin|stoneskin]]_ (already cast)
3rd (8/day)—_[[spells/Displacement|displacement]]_, _[[spells/Hold Person|hold person]]_ (DC 21), _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Stinking Cloud|stinking cloud]]_ (DC 21), _[[spells/Summon Monster III|summon monster III]]_
2nd (8/day)—_[[spells/Acid Arrow|acid arrow]]_, _[[spells/Darkness|darkness]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 19), _[[spells/Glitterdust|glitterdust]]_ (DC 20), _[[spells/Scorching Ray|scorching ray]]_ (cold), web (DC 20)
1st (7/day)—_[[spells/Burning Hands|burning hands]]_ (cold) (DC 18), _[[spells/Charm Person|charm person]]_ (DC 19), _[[spells/Disguise Self|disguise self]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Mage Armor|mage armor]]_ (already cast), _[[spells/Magic Missile|magic missile]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Arcane Mark|arcane mark]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 17), _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Read Magic|read magic]]_
**Bloodline **elemental (water)

##### Statistics
**Str** 8, **Dex** 10, **Con** 18, **Int** 15, **Wis** 12, **Cha** 24
**Base Atk** +6; **CMB** +5; **CMD** 15
**Feats** _[[feats/Arcane Shield|Arcane Shield]]_, _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _Spell Focus_ (enchantment), _[[feats/Superior Summoning|Superior Summoning]]_
**Skills** Diplomacy +13, Intimidate +17, Knowledge (arcana) +18, Knowledge (planes) +18, Perception +14, Sense Motive +14
**Languages** Common, Draconic, Infernal
**SQ** bloodline arcana (change energy damage spells to cold)

##### Ecology

**Environment** any urban
**Organization** solitary
**Treasure** NPC gear (_dagger_, _[[items/Wondrous Item/Amulet of Natural Armor +3|amulet of natural armor +3]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Wondrous Item/Brooch of Shielding|brooch of shielding]]_ [50 points], potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, wand of _[[spells/False Life|false life]]_ [10 charges], diamond dust [250 gp], other treasure)

##### Description

A devilbound creature has made a bargain with a devil, promising a service and its soul in exchange for infernal power. The specif ic service depends on the devil’s type and motivations, but always furthers the interests of Hell.