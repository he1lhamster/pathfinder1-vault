---
cssclass: [monsters]
title1: Demon-Blooded Sorcerer
title2: Demon-Blooded Sorcerer
CR: 17
sources:
- name: NPC Codex
  page: 175
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 102400
race: Half-orc
classes:
- sorcerer 18
alignment: CE
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 6
senses:
  darkvision: 60
AC:
  AC: 22
  touch: 13
  flat_footed: 19
  components:
    armor: 5
    dex: 2
    dodge: 1
    natural: 4
HP:
  HP: 152
  long: 18d6+87
saves:
  fort: 11
  ref: 9
  will: 13
  other: +4 vs. poison
defensive_abilities:
- orc ferocity
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
resistances:
  electricity: 10
speeds:
  base: 30
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: 2 claws +12 (1d6+3 plus 1d6 fire)
      entries:
      - - damage: 1d6+3
        - damage: 1d6
          type: fire
      count: 2
      attack: claws
      bonus:
      - 12
  - - text: +1 flaming greataxe +13/+8 (1d12+5/×3 plus 1d6 fire)
      entries:
      - - damage: 1d12+5
          crit_multiplier: 3
        - damage: 1d6
          type: fire
      attack: +1 flaming greataxe
      bonus:
      - 13
      - 8
  special:
  - claws (2, 1d6+7 plus 1d6 fire, treated as magic weapons, 7 rounds/day)
spells:
  entries:
  - name: meteor swarm
    source: Sorcerer
    level: 9
  - name: incendiary cloud
    source: Sorcerer
    level: 8
    DC: 27
  - name: summon monster VIII
    source: Sorcerer
    level: 8
  - name: unholy aura
    source: Sorcerer
    level: 8
  - name: delayed blast fireball
    source: Sorcerer
    level: 7
    DC: 24
  - name: greater teleport
    source: Sorcerer
    level: 7
  - name: power word blind
    source: Sorcerer
    level: 7
  - name: reverse gravity
    source: Sorcerer
    level: 7
  - name: acid fog
    source: Sorcerer
    level: 6
  - name: chain lightning
    source: Sorcerer
    level: 6
    DC: 23
  - name: transformation
    source: Sorcerer
    level: 6
  - name: true seeing
    source: Sorcerer
    level: 6
  - name: cloudkill
    source: Sorcerer
    level: 5
    DC: 24
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 22
  - name: dismissal
    source: Sorcerer
    level: 5
    DC: 22
  - name: feeblemind
    source: Sorcerer
    level: 5
    DC: 22
  - name: summon monster V
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
  - name: phantasmal killer
    source: Sorcerer
    level: 4
    DC: 21
  - name: stoneskin
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: fly
    source: Sorcerer
    level: 3
  - name: gaseous form
    source: Sorcerer
    level: 3
  - name: rage
    source: Sorcerer
    level: 3
  - name: slow
    source: Sorcerer
    level: 3
    DC: 20
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: bull's strength
    source: Sorcerer
    level: 2
  - name: darkness
    source: Sorcerer
    level: 2
  - name: false life
    source: Sorcerer
    level: 2
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 18
  - name: cause fear
    source: Sorcerer
    level: 1
    DC: 18
  - name: enlarge person
    source: Sorcerer
    level: 1
    DC: 18
  - name: grease
    source: Sorcerer
    level: 1
  - name: ray of enfeeblement
    source: Sorcerer
    level: 1
    DC: 18
  - name: shield
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 17
  - name: daze
    source: Sorcerer
    level: 0
    DC: 17
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
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
    CL: 18
    concentration: 25
    slots:
      9: 3
      8: 5
      7: 7
      6: 7
      5: 7
      4: 7
      3: 8
      2: 8
      1: 8
      0: at-will
    bloodline: abyssal
tactics:
  Before Combat: The sorcerer casts false life and stoneskin.
  During Combat: The sorcerer casts summon monster VIII to summon a hezrou, then alternates
    between casting area damage spells and summoning other demons. If he knows he
    is fighting good-aligned opponents, he casts unholy aura.
  Base Statistics: Without false life and stoneskin, the sorcerer's statistics are
    hp 137; DR none.
ability_scores:
  STR: 16
  DEX: 14
  CON: 14
  INT: 8
  WIS: 12
  CHA: 24
BAB: 9
CMB: 12
CMD: 25
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Dodge
- name: Empower Spell
- name: Eschew Materials
- name: Extend Spell
- name: Great Fortitude
- name: Greater Spell Focus (conjuration)
- name: Improved Initiative
- name: Quicken Spell
- name: Spell Focus (conjuration)
- name: Toughness
skills:
  Fly: 6
  Intimidate: 14
  Knowledge (arcana): 3
  Knowledge (planes): 5
  Linguistics: 0
  Perception: 10
  Spellcraft: 3
languages:
- Abyssal
- Common
- Orc
special_qualities:
- added summonings
- bloodline arcana (summoned creatures gain DR 9/good)
- orc blood
- strength of the Abyss
- weapon familiarity
gear:
  combat:
  - potions of cure serious wounds (2)
  - potion of haste
  - scroll of greater dispel magic
  - wand of shield (20 charges)
  other:
  - +1 flaming greataxe
  - amulet of natural armor +4
  - bracers of armor +5
  - cloak of resistance +1
  - headband of alluring charisma +4
  - ring of counterspells
  - diamond dust (worth 500 gp)
  - eye ointment for true seeing (worth 500 gp)
  - 4,480 gp
desc_long: The demon-blooded sorcerer is a powerful mortal servant of the Abyss.

---

# Demon-Blooded Sorcerer

**Source** NPC Codex pg. 175
**XP** 102,400
Half-orc _[[classes/Sorcerer|sorcerer]]_ 18
CE Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +6; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +10

##### Defense

**AC** 22, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 19 (+5 armor, +2 Dex, +1 _[[feats/Dodge|dodge]]_, +4 natural)
**hp** 152 (18d6+87)
**Fort** +11, **Ref** +9, **Will** +13; +4 vs. poison
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_; **DR** 10/adamantine (150 points); **Resist** electricity 10

##### Offense
**Speed** 30 ft., fly 60 ft. (average)
**Melee** 2 claws +12 (1d6+3 plus 1d6 fire) or +1 _[[items/Weapon Magic Abilities/Flaming|flaming]]_ _[[items/Weapon/Greataxe|greataxe]]_ +13/+8 (1d12+5/×3 plus 1d6 fire)
**Special Attacks** claws (2, 1d6+7 plus 1d6 fire, treated as magic weapons, 7 rounds/day)
**_Sorcerer_ Spells Known **(CL 18th; concentration +25)
9th (3/day)—_[[spells/Meteor Swarm|meteor swarm]]_
8th (5/day)—_[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 27), _[[spells/Summon Monster VIII|summon monster VIII]]_, _[[spells/Unholy Aura|unholy aura]]_
7th (7/day)—_[[spells/Delayed Blast Fireball|delayed blast fireball]]_ (DC 24), greater teleport, _[[spells/Power Word Blind|power word blind]]_, _[[spells/Reverse Gravity|reverse gravity]]_
6th (7/day)—_[[spells/Acid Fog|acid fog]]_, _[[spells/Chain Lightning|chain lightning]]_ (DC 23), _[[spells/Transformation|transformation]]_, _[[spells/True Seeing|true seeing]]_
5th (7/day)—_[[spells/Cloudkill|cloudkill]]_ (DC 24), _[[spells/Cone of Cold|cone of cold]]_ (DC 22), _[[spells/Dismissal|dismissal]]_ (DC 22), _[[spells/Feeblemind|feeblemind]]_ (DC 22), _[[spells/Summon Monster V|summon monster V]]_
4th (7/day)—_[[spells/Black Tentacles|black tentacles]]_, _[[spells/Confusion|confusion]]_ (DC 21), _[[spells/Dimension Door|dimension door]]_, _[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 21), _[[spells/Stoneskin|stoneskin]]_
3rd (8/day)—_[[spells/Dispel Magic|dispel magic]]_, fly, _[[spells/Gaseous Form|gaseous form]]_, _[[spells/Rage|rage]]_, _[[spells/Slow|slow]]_ (DC 20)
2nd (8/day)—_[[spells/Acid Arrow|acid arrow]]_, bull’s strength, _[[spells/Darkness|darkness]]_, _[[spells/False Life|false life]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (8/day)—_[[spells/Burning Hands|burning hands]]_ (DC 18), _[[spells/Cause Fear|cause fear]]_ (DC 18), _[[spells/Enlarge Person|enlarge person]]_ (DC 18), _[[spells/Grease|grease]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 18), _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 17), _[[spells/Daze|daze]]_ (DC 17), _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_
**Bloodline** abyssal

### Tactics

**Before Combat **The _sorcerer_ casts _false life_ and _stoneskin_.
**During Combat **The _sorcerer_ casts _summon monster VIII_ to _[[universal monster rules/Summon|summon]]_ a hezrou, then alternates between casting area damage spells and summoning other demons. If he knows he is fighting good-aligned opponents, he casts _unholy aura_.
**Base Statistics **Without _false life_ and _stoneskin_, the _sorcerer_’s statistics are **hp **137; **DR **none.

##### Statistics
**Str** 16, **Dex** 14, **Con** 14, **Int** 8, **Wis** 12, **Cha** 24
**Base Atk** +9; **CMB** +12; **CMD** 25
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _Dodge_, _[[feats/Empower Spell|Empower Spell]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (conjuration), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _[[feats/Toughness|Toughness]]_
**Skills** Fly +6, Intimidate +14, Knowledge (arcana) +3, Knowledge (planes) +5, Linguistics +0, Perception +10, Spellcraft +3
**Languages** Abyssal, Common, _Orc_
**SQ** added summonings, bloodline arcana (summoned creatures gain DR 9/good), _orc_ blood, strength of the Abyss, weapon familiarity
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), potion of _[[spells/Haste|haste]]_, scroll of greater _dispel magic_, wand of _shield_ (20 charges); **Other Gear** +1 _flaming_ _greataxe_, _[[items/Wondrous Item/Amulet of Natural Armor +4|amulet of natural armor +4]]_, _[[items/Wondrous Item/Bracers of Armor +5|bracers of armor +5]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Ring/Ring of Counterspells|ring of counterspells]]_, diamond dust (worth 500 gp), eye ointment for _true seeing_ (worth 500 gp), 4,480 gp

The _[[npcs/Demon-Blooded Sorcerer|demon-blooded sorcerer]]_ is a powerful mortal servant of the Abyss.