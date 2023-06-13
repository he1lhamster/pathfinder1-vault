---
cssclass: [monsters]
title1: Fiery Dragonkin
title2: Fiery Dragonkin
CR: 16
sources:
- name: NPC Codex
  page: 174
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Dwarf
classes:
- sorcerer 17
alignment: CE
size: Medium
type: humanoid
subtypes:
- dwarf
initiative:
  bonus: 4
senses:
  darkvision: 60
AC:
  AC: 26
  touch: 14
  flat_footed: 26
  components:
    armor: 8
    deflection: 3
    insight: 1
    natural: 4
HP:
  HP: 147
  long: 17d6+85
saves:
  fort: 15
  ref: 9
  will: 14
  other: +2 vs. poison, spells, and spell-like abilities
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
DR:
- amount: 10
  weakness: adamantine
  max_absorb: 150
resistances:
  fire: 10
speeds:
  base: 20
  fly: 60
  fly_maneuverability: average
attacks:
  melee:
  - - text: mwk battleaxe +11/+6 (1d8+2/×3)
      entries:
      - - damage: 1d8+2
          crit_multiplier: 3
      attack: mwk battleaxe
      bonus:
      - 11
      - 6
  - - text: 2 claws +10 (1d6+2 plus 1d6 fire)
      entries:
      - - damage: 1d6+2
        - damage: 1d6
          type: fire
      count: 2
      attack: claws
      bonus:
      - 10
  ranged:
  - - text: mwk heavy crossbow +9 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: mwk heavy crossbow
      bonus:
      - 9
  special:
  - +1 on attack rolls against goblinoid and orc humanoids
  - breath weapon (30-foot cone, 17d6 fire, DC 23, 2/day)
  - claws (2, 1d4+2 plus 1d6 fire, treated as magic weapons, 8 rounds/day)
spells:
  entries:
  - name: form of the dragon III
    source: Sorcerer
    level: 8
  - name: greater shout
    source: Sorcerer
    level: 8
    DC: 25
  - name: incendiary cloud
    source: Sorcerer
    level: 8
    DC: 23
  - name: delayed blast fireball
    source: Sorcerer
    level: 7
    DC: 24
  - name: form of the dragon II
    source: Sorcerer
    level: 7
  - name: mass hold person
    source: Sorcerer
    level: 7
    DC: 22
  - name: reverse gravity
    source: Sorcerer
    level: 7
  - name: chain lightning
    source: Sorcerer
    level: 6
    DC: 23
  - name: flesh to stone
    source: Sorcerer
    level: 6
    DC: 21
  - name: form of the dragon I
    source: Sorcerer
    level: 6
  - name: transformation
    source: Sorcerer
    level: 6
  - name: cloudkill
    source: Sorcerer
    level: 5
    DC: 20
  - name: cone of cold
    source: Sorcerer
    level: 5
    DC: 22
  - name: spell resistance
    source: Sorcerer
    level: 5
  - name: telekinesis
    source: Sorcerer
    level: 5
  - name: wall of force
    source: Sorcerer
    level: 5
  - name: crushing despair
    source: Sorcerer
    level: 4
    DC: 19
  - name: fear
    source: Sorcerer
    level: 4
    DC: 19
  - name: fire shield
    source: Sorcerer
    level: 4
  - name: stoneskin
    source: Sorcerer
    level: 4
  - name: wall of fire
    source: Sorcerer
    level: 4
  - name: dispel magic
    source: Sorcerer
    level: 3
  - name: fireball
    source: Sorcerer
    level: 3
    DC: 20
  - name: fly
    source: Sorcerer
    level: 3
  - name: greater magic weapon
    source: Sorcerer
    level: 3
  - name: ray of exhaustion
    source: Sorcerer
    level: 3
    DC: 18
  - name: blur
    source: Sorcerer
    level: 2
  - name: flaming sphere
    source: Sorcerer
    level: 2
    DC: 19
  - name: invisibility
    source: Sorcerer
    level: 2
  - name: resist energy
    source: Sorcerer
    level: 2
    DC: 17
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: web
    source: Sorcerer
    level: 2
    DC: 17
  - name: burning hands
    source: Sorcerer
    level: 1
    DC: 18
  - name: expeditious retreat
    source: Sorcerer
    level: 1
  - name: mage armor
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: ventriloquism
    source: Sorcerer
    level: 1
    DC: 16
  - name: acid splash
    source: Sorcerer
    level: 0
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 15
  - name: dancing lights
    source: Sorcerer
    level: 0
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 17
  - name: mage hand
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
    DC: 15
  sources:
  - name: Sorcerer
    type: known
    CL: 17
    concentration: 22
    slots:
      8: 4
      7: 6
      6: 6
      5: 7
      4: 7
      3: 7
      2: 7
      1: 8
      0: at-will
    bloodline: draconic (red)
tactics:
  Before Combat: The sorcerer casts stoneskin.
  During Combat: The sorcerer casts mass hold person, then uses his breath weapon
    and area spells against his paralyzed foes. If forced into melee, he casts greater
    magic weapon on his battleaxe and transformation on himself.
  Base Statistics: Without stoneskin, the sorcerer's statistics are DR none.
ability_scores:
  STR: 14
  DEX: 10
  CON: 18
  INT: 12
  WIS: 10
  CHA: 20
BAB: 8
CMB: 10
CMD: 24
CMD_other: 28 vs. bull rush or trip
feats:
- name: Arcane Armor Mastery
- name: Arcane Armor Training
- name: Combat Casting
- name: Eschew Materials
- name: Great Fortitude
- name: Greater Spell Focus (evocation)
- name: Improved Initiative
- name: Light Armor Proficiency
- name: Medium Armor Proficiency
- name: Maximize Spell
- name: Quicken Spell
- name: Spell Focus (evocation)
skills:
  Appraise: 5
    to assess nonmagical metals or gemstones: 7
  Fly: 6
  Intimidate: 18
  Knowledge (arcana): 13
  Linguistics: 2
  Perception: 18
    to notice unusual stonework: 20
  Spellcraft: 13
languages:
- Common
- Draconic
- Dwarven
- Orc
special_qualities:
- bloodline arcana (fire spells deal +1 damage per die)
- wings
gear:
  combat:
  - potions of bull's strength (2)
  - potions of cure serious wounds (2)
  - wand of shield (20 charges)
  other:
  - +2 red dragonhide breastplate
  - masterwork battleaxe
  - masterwork heavy crossbow with 10 bolts
  - belt of mighty constitution +2
  - brooch of shielding
  - cloak of resistance +4
  - dusty rose prism ioun stone
  - headband of alluring charisma +4
  - ring of protection +3
  - diamond dust (worth 500 gp)
  - 6,240 gp
desc_long: The fiery dragonkin embodies all the greedy, violent, and territorial impulses
  of red dragons. Heedless of the lives they crush in their rise to glory, the dragonkin
  sorcerers are born conquerors, and see in their noble draconic blood an undeniable
  right to rule over lesser beings.

---

# Fiery Dragonkin

**Source** NPC Codex pg. 174
**XP** 76,800
Dwarf _[[classes/Sorcerer|sorcerer]]_ 17
CE Medium humanoid (dwarf)
**Init** +4; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +18

##### Defense

**AC** 26, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+8 armor, +3 _[[spells/Deflection|deflection]]_, +1 insight, +4 natural)
**hp** 147 (17d6+85)
**Fort** +15, **Ref** +9, **Will** +14; +2 vs. poison, spells, and _[[universal monster rules/Spell-Like Abilities|spell-like abilities]]_
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants); **DR** 10/adamantine (150 points); **Resist** fire 10

##### Offense
**Speed** 20 ft., fly 60 ft. (average)
**Melee** mwk _[[items/Weapon/Battleaxe|battleaxe]]_ +11/+6 (1d8+2/×3) or 2 claws +10 (1d6+2 plus 1d6 fire)
**Ranged** mwk _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +9 (1d10/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and _[[monsters/Orc|orc]]_ humanoids, _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-foot cone, 17d6 fire, DC 23, 2/day), claws (2, 1d4+2 plus 1d6 fire, treated as magic weapons, 8 rounds/day)
**_Sorcerer_ Spells Known **(CL 17th; concentration +22)
8th (4/day)—_[[spells/Form of the Dragon III|form of the dragon III]]_, greater _[[spells/Shout|shout]]_ (DC 25), _[[spells/Incendiary Cloud|incendiary cloud]]_ (DC 23)
7th (6/day)—_[[spells/Delayed Blast Fireball|delayed blast fireball]]_ (DC 24), _[[spells/Form of the Dragon II|form of the dragon II]]_, mass _[[spells/Hold Person|hold person]]_ (DC 22), _[[spells/Reverse Gravity|reverse gravity]]_
6th (6/day)—_[[spells/Chain Lightning|chain lightning]]_ (DC 23), _[[spells/Flesh to Stone|flesh to stone]]_ (DC 21), _[[spells/Form of the Dragon I|form of the dragon I]]_, _[[spells/Transformation|transformation]]_
5th (7/day)—_[[spells/Cloudkill|cloudkill]]_ (DC 20), _[[spells/Cone of Cold|cone of cold]]_ (DC 22), _[[universal monster rules/Spell Resistance|spell resistance]]_, _[[spells/Telekinesis|telekinesis]]_, _[[spells/Wall Of Force|wall of force]]_
4th (7/day)—_[[spells/Crushing Despair|crushing despair]]_ (DC 19), _[[universal monster rules/Fear|fear]]_ (DC 19), _[[spells/Fire Shield|fire shield]]_, _[[spells/Stoneskin|stoneskin]]_, _[[spells/Wall Of Fire|wall of fire]]_
3rd (7/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 20), fly, greater _[[spells/Magic Weapon|magic weapon]]_, _[[spells/Ray of Exhaustion|ray of exhaustion]]_ (DC 18)
2nd (7/day)—_[[spells/Blur|blur]]_, _[[spells/Flaming Sphere|flaming sphere]]_ (DC 19), _[[spells/Invisibility|invisibility]]_, _[[spells/Resist Energy|resist energy]]_ (DC 17), _[[spells/Scorching Ray|scorching ray]]_, web (DC 17)
1st (8/day)—_[[spells/Burning Hands|burning hands]]_ (DC 18), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 16)
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 15), _[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 17), _[[spells/Mage Hand|mage hand]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 15)
**Bloodline **draconic (red)

### Tactics

**Before Combat **The _sorcerer_ casts _stoneskin_.
**During Combat **The _sorcerer_ casts mass _hold person_, then uses his _breath weapon_ and area spells against his _[[conditions/Paralyzed|paralyzed]]_ foes. If forced into melee, he casts greater _magic weapon_ on his _battleaxe_ and _transformation_ on himself.
**Base Statistics **Without _stoneskin_, the _sorcerer_’s statistics are **DR **none.

##### Statistics
**Str** 14, **Dex** 10, **Con** 18, **Int** 12, **Wis** 10, **Cha** 20
**Base Atk** +8; **CMB** +10; **CMD** 24 (28 vs. bull rush or _[[universal monster rules/Trip|trip]]_)
**Feats** _[[feats/Arcane Armor Mastery|Arcane Armor Mastery]]_, _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (evocation), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Light Armor Proficiency|Light Armor Proficiency]]_, _[[feats/Medium Armor Proficiency|Medium Armor Proficiency]]_, _[[feats/Maximize Spell|Maximize Spell]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation)
**Skills** Appraise +5 (+7 to assess nonmagical metals or gemstones), Fly +6, Intimidate +18, Knowledge (arcana) +13, Linguistics +2, Perception +18 (+20 to notice unusual stonework), Spellcraft +13
**Languages** Common, Draconic, Dwarven, _Orc_
**SQ** bloodline arcana (fire spells deal +1 damage per die), wings
**Combat Gear** potions of bull’s strength (2), potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), wand of _shield_ (20 charges); **Other Gear** +2 red dragonhide _[[items/Armor/Breastplate|breastplate]]_, masterwork _battleaxe_, masterwork _heavy crossbow_ with 10 bolts, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Brooch of Shielding|brooch of shielding]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +4|cloak of _resistance_ +4]]_, _[[items/Wondrous Item/Dusty Rose Prism Ioun Stone|dusty rose prism ioun stone]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, diamond dust (worth 500 gp), 6,240 gp

The _[[npcs/Fiery Dragonkin|fiery dragonkin]]_ embodies all the greedy, violent, and territorial impulses of red dragons. Heedless of the lives they crush in their rise to glory, the _[[monsters/Dragonkin|dragonkin]]_ sorcerers are born conquerors, and see in their noble draconic blood an undeniable right to rule over lesser beings.