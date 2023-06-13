---
cssclass: [monsters]
title1: Blackscale Sorcerer
title2: Blackscale Sorcerer
CR: 9
sources:
- name: NPC Codex
  page: 167
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 6400
race: Half-orc
classes:
- sorcerer 10
alignment: CE
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 5
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 12
  flat_footed: 18
  components:
    armor: 4
    deflection: 1
    dex: 1
    natural: 3
HP:
  HP: 82
  long: 10d6+45
saves:
  fort: 8
  ref: 5
  will: 7
defensive_abilities:
- orc ferocity
DR:
- amount: 10
  weakness: adamantine
resistances:
  acid: 10
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk greataxe +8 (1d12+3/×3)
      entries:
      - - damage: 1d12+3
          crit_multiplier: 3
      attack: mwk greataxe
      bonus:
      - 8
  - - text: 2 claws +7 (1d6+2)
      entries:
      - - damage: 1d6+2
      count: 2
      attack: claws
      bonus:
      - 7
  special:
  - breath weapon (60-foot line, 10d6 acid, DC 20, 1/day)
  - claws (2, 1d6+2, treated as magic weapons, 7 rounds/day)
spells:
  entries:
  - name: cloudkill
    source: Sorcerer
    level: 5
    DC: 20
  - name: fear
    source: Sorcerer
    level: 4
    DC: 19
  - name: shout
    source: Sorcerer
    level: 4
    DC: 21
  - name: stoneskin
    source: Sorcerer
    level: 4
  - name: fireball
    source: Sorcerer
    level: 3
    DC: 20
  - name: fly
    source: Sorcerer
    level: 3
  - name: rage
    source: Sorcerer
    level: 3
  - name: stinking cloud
    source: Sorcerer
    level: 3
    DC: 18
  - name: acid arrow
    source: Sorcerer
    level: 2
  - name: bull's strength
    source: Sorcerer
    level: 2
  - name: false life
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 18
  - name: endure elements
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
  - name: shield
    source: Sorcerer
    level: 1
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: arcane mark
    source: Sorcerer
    level: 0
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 15
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 17
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: resistance
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 15
  sources:
  - name: Sorcerer
    type: known
    CL: 10
    concentration: 15
    slots:
      5: 4
      4: 6
      3: 7
      2: 7
      1: 8
      0: at-will
    bloodline: draconic (black)
tactics:
  Before Combat: The sorcerer casts false life, mage armor, and stoneskin on himself.
  During Combat: The sorcerer casts fly on the first round of combat along with a
    quickened magic missile. He maneuvers so he can catch as many opponents as possible
    with his breath weapon. If pressed into melee, he casts bull's strength and rage,
    then attacks with his greataxe or claws.
  Base Statistics: Without false life, mage armor, and stoneskin, the sorcerer's statistics
    are AC 15, touch 12, flat-footed 14; hp 67; DR -.
ability_scores:
  STR: 14
  DEX: 12
  CON: 14
  INT: 10
  WIS: 8
  CHA: 20
BAB: 5
CMB: 7
CMD: 19
feats:
- name: Combat Casting
- name: Eschew Materials
- name: Great Fortitude
- name: Greater Spell Focus (evocation)
- name: Improved Initiative
- name: Quicken Spell
- name: Spell Focus (evocation)
skills:
  Fly: 9
  Intimidate: 15
  Linguistics: 1
  Perception: 7
  Spellcraft: 7
languages:
- Common
- Draconic
- Orc
special_qualities:
- bloodline arcana (acid spells deal +1 damage per die)
- orc blood
- weapon familiarity
gear:
  combat:
  - potion of cure serious wounds
  - wand of acid arrow (15 charges)
  other:
  - masterwork greataxe
  - amulet of natural armor +1
  - cloak of resistance +1
  - headband of alluring charisma +2
  - ring of protection +1
  - signet ring
  - diamond dust (worth 500 gp)
  - 825 gp
desc_long: The blackscale sorcerer channels the powers of corruption and sloth.

---

# Blackscale Sorcerer

**Source** NPC Codex pg. 167
**XP** 6,400
Half-orc _[[classes/Sorcerer|sorcerer]]_ 10
CE Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +7

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +3 natural)
**hp** 82 (10d6+45)
**Fort** +8, **Ref** +5, **Will** +7
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_; **DR** 10/adamantine; **Resist** acid 10

##### Offense
**Speed** 30 ft.
**Melee** mwk _[[items/Weapon/Greataxe|greataxe]]_ +8 (1d12+3/×3) or 2 claws +7 (1d6+2)
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-foot line, 10d6 acid, DC 20, 1/day), claws (2, 1d6+2, treated as magic weapons, 7 rounds/day)
**_Sorcerer_ Spells Known **(CL 10th; concentration +15)
5th (4/day)—_[[spells/Cloudkill|cloudkill]]_ (DC 20)
4th (6/day)—_[[universal monster rules/Fear|fear]]_ (DC 19), _[[spells/Shout|shout]]_ (DC 21), _[[spells/Stoneskin|stoneskin]]_
3rd (7/day)—_[[spells/Fireball|fireball]]_ (DC 20), fly, _[[spells/Rage|rage]]_, _[[spells/Stinking Cloud|stinking cloud]]_ (DC 18)
2nd (7/day)—_[[spells/Acid Arrow|acid arrow]]_, bull’s strength, _[[spells/False Life|false life]]_, _[[spells/Resist Energy|resist energy]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (8/day)—_[[spells/Burning Hands|burning hands]]_ (DC 18), _[[spells/Endure Elements|endure elements]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 16), _[[spells/Shield|shield]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[spells/Arcane Mark|arcane mark]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 17), _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 15)
**Bloodline **draconic (black)

### Tactics

**Before Combat **The _sorcerer_ casts _false life_, _mage armor_, and _stoneskin_ on himself.
**During Combat **The _sorcerer_ casts fly on the first round of combat along with a quickened _magic missile_. He maneuvers so he can catch as many opponents as possible with his _breath weapon_. If pressed into melee, he casts bull’s strength and _rage_, then attacks with his _greataxe_ or claws.
**Base Statistics **Without _false life_, _mage armor_, and _stoneskin_, the _sorcerer_’s statistics are **AC **15, touch 12, _flat-footed_ 14; **hp **67; **DR **—.

##### Statistics
**Str** 14, **Dex** 12, **Con** 14, **Int** 10, **Wis** 8, **Cha** 20
**Base Atk** +5; **CMB** +7; **CMD** 19
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation)
**Skills** Fly +9, Intimidate +15, Linguistics +1, Perception +7, Spellcraft +7
**Languages** Common, Draconic, _Orc_
**SQ** bloodline arcana (acid spells deal +1 damage per die), _orc_ blood, weapon familiarity
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, wand of _acid arrow_ (15 charges); **Other Gear** masterwork _greataxe_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Signet ring|signet ring]]_, diamond dust (worth 500 gp), 825 gp

The _[[npcs/Blackscale Sorcerer|blackscale sorcerer]]_ channels the powers of corruption and sloth.