---
cssclass: [monsters]
title1: Chaos Arrow
title2: Chaos Arrow
CR: 19
sources:
- name: NPC Codex
  page: 203
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 204800
race: Gnome
classes:
- rogue 6
- sorcerer 4
- arcane archer 10
alignment: CE
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 11
senses:
  low-light vision: true
  see invisibility: true
AC:
  AC: 31
  touch: 21
  flat_footed: 24
  components:
    armor: 7
    deflection: 3
    dex: 6
    dodge: 1
    natural: 3
    size: 1
HP:
  HP: 140
  long: 6d8+4d6+10d10+40
saves:
  fort: 13
  ref: 21
  will: 13
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
- evasion
- trap sense +2
- uncanny dodge
speeds:
  base: 20
attacks:
  melee:
  - - text: dagger +17/+12/+7/+2 (1d3/19-20)
      entries:
      - - damage: 1d3
          crit_range: 19-20
      attack: dagger
      bonus:
      - 17
      - 12
      - 7
      - 2
  ranged:
  - - text: +2 frost shock shortbow +27/+22/+17/+12 (1d4+2/×3 plus 1d6 cold and 1d6
        electricity)
      entries:
      - - damage: 1d4+2
          crit_multiplier: 3
        - damage: 1d6
          type: cold
        - damage: 1d6
          type: electricity
      attack: +2 frost shock shortbow
      bonus:
      - 27
      - 22
      - 17
      - 12
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - arrow of death
  - enhance arrows (aligned, distance, elemental, elemental burst, magic)
  - imbue arrow
  - phase arrow (3/day)
  - seeker arrow (4/day)
  - sneak attack +3d6
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: ghost sound
    source: default
    freq: 1/day
  - name: prestidigitation
    source: default
    freq: 1/day
  - name: speak with animals
    source: default
    freq: 1/day
  - name: laughing touch
    source: bloodline
    freq: 7/day
  sources:
  - name: default
    CL: 20
    concentration: 24
  - name: bloodline
    CL: 11
    concentration: 15
spells:
  entries:
  - name: cloudkill
    source: Sorcerer
    level: 5
    DC: 19
  - name: teleport
    source: Sorcerer
    level: 5
  - name: confusion
    source: Sorcerer
    level: 4
    DC: 20
  - name: greater invisibility
    source: Sorcerer
    level: 4
  - name: shout
    source: Sorcerer
    level: 4
    DC: 18
  - name: explosive runes
    source: Sorcerer
    level: 3
  - name: haste
    source: Sorcerer
    level: 3
  - name: heroism
    source: Sorcerer
    level: 3
  - name: stinking cloud
    source: Sorcerer
    level: 3
    DC: 17
  - name: darkvision
    source: Sorcerer
    level: 2
  - name: glitterdust
    source: Sorcerer
    level: 2
    DC: 16
  - name: rope trick
    source: Sorcerer
    level: 2
  - name: see invisibility
    source: Sorcerer
    level: 2
  - name: web
    source: Sorcerer
    level: 2
    DC: 16
  - name: color spray
    source: Sorcerer
    level: 1
    DC: 16
  - name: entangle
    source: Sorcerer
    level: 1
    DC: 15
  - name: expeditious retreat
    source: Sorcerer
    level: 1
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: reduce person
    source: Sorcerer
    level: 1
    DC: 15
  - name: true strike
    source: Sorcerer
    level: 1
  - name: bleed
    source: Sorcerer
    level: 0
    DC: 14
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 14
  - name: light
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: prestidigitation
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
    CL: 11
    concentration: 15
    failure_chance: 10%
    slots:
      5: 4
      4: 7
      3: 7
      2: 7
      1: 7
      0: at-will
    bloodline: fey
tactics:
  Before Combat: The arcane archer casts see invisibility and haste. She prepares
    flaming burst arrows as her enhance arrows ability.
  During Combat: A arcane archer uses imbue arrows to fire off cloudkill, stinking
    cloud, and entangle from a distance.
  Base Statistics: Without see invisibility, the arcane archer's statistics are Senses
    low-light vision; Perception +26.
ability_scores:
  STR: 10
  DEX: 24
  CON: 14
  INT: 10
  WIS: 13
  CHA: 18
BAB: 16
CMB: 15
CMD: 36
feats:
- name: Deadly Aim
- name: Dodge
- name: Eschew Materials
- name: Improved Initiative
- name: Mobility
- name: Pinpoint Targeting
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
- name: Shot on the Run
- name: Vital Strike
- name: Weapon Focus (shortbow)
skills:
  Bluff: 27
  Craft (bows): 8
  Disguise: 13
  Knowledge (local): 8
  Knowledge (nature): 8
  Perception: 26
  Spellcraft: 8
  Stealth: 34
  Swim: 8
  Use Magic Device: 12
languages:
- Common
- Gnome
special_qualities:
- bloodline arcana (+2 DC for compulsion spells)
- rogue talents (bleeding attack +3, combat trick, surprise attack)
- trapfinding +3
- woodland stride
gear:
  combat:
  - +1 dwarf-bane arrows (10)
  - +1 elf-bane arrows (10)
  - +1 human-bane arrows (10)
  - +1 holy arrows (5)
  - +1 unholy arrows (5)
  - dust of illusion
  - potions of cure serious wounds (3)
  other:
  - +3 mithral chain shirt
  - +2 frost shock shortbow with 20 arrows
  - daggers (3)
  - amulet of natural armor +3
  - belt of physical might +4 (Dex, Con)
  - cloak of resistance +3
  - deck of illusions
  - efficient quiver
  - hat of disguise
  - headband of alluring charisma +2
  - ring of protection +3
  - rope of climbing
  - 621 gp
desc_long: Often whimsical in their destruction, chaos arrows roam the world playing
  the cruelest pranks for their own twisted amusement.

---

# Chaos Arrow

**Source** NPC Codex pg. 203
**XP** 204,800
Gnome _[[classes/Rogue|rogue]]_ 6/sorcerer 4/arcane archer 10
CE Small humanoid (gnome)
**Init** +11; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +26

##### Defense

**AC** 31, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+7 armor, +3 deflection, +6 Dex, +1 _[[feats/Dodge|dodge]]_, +3 natural, +1 size)
**hp** 140 (6d8+4d6+10d10+40)
**Fort** +13, **Ref** +21, **Will** +13; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants), evasion, trap sense +2, uncanny _dodge_

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +17/+12/+7/+2 (1d3/19–20)
**Ranged** +2 frost _[[items/Weapon Magic Abilities/Shock|shock]]_ _[[items/Weapon/Shortbow|shortbow]]_ +27/+22/+17/+12 (1d4+2/×3 plus 1d6 cold and 1d6 electricity)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, arrow of death, enhance arrows (aligned, distance, elemental, elemental burst, magic), imbue arrow, _[[items/Ammunition/Phase Arrow|phase arrow]]_ (3/day), seeker arrow (4/day), sneak attack +3d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +24)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
**Bloodline _Spell-Like Abilities_ **(CL 11th; concentration +15)
 7/day—laughing touch
**_[[classes/Sorcerer|Sorcerer]]_ Spells Known **(CL 11th; concentration +15; arcane spell failure 10%)
5th (4/day)—_[[spells/Cloudkill|cloudkill]]_ (DC 19), teleport
4th (7/day)—_[[spells/Confusion|confusion]]_ (DC 20), greater _[[spells/Invisibility|invisibility]]_, _[[spells/Shout|shout]]_ (DC 18)
3rd (7/day)—_[[spells/Explosive Runes|explosive runes]]_, _[[spells/Haste|haste]]_, _[[spells/Heroism|heroism]]_, _[[spells/Stinking Cloud|stinking cloud]]_ (DC 17)
2nd (7/day)—_[[spells/Darkvision|darkvision]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 16), _[[spells/Rope Trick|rope trick]]_, _see invisibility_, web (DC 16)
1st (7/day)—_[[spells/Color Spray|color spray]]_ (DC 16), _[[spells/Entangle|entangle]]_ (DC 15), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Magic Missile|magic missile]]_, _[[spells/Reduce Person|reduce person]]_ (DC 15), _[[spells/True Strike|true strike]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 14), _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 14), light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _prestidigitation_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_
**Bloodline **fey

### Tactics

**Before Combat **The arcane archer casts _see invisibility_ and _haste_. She prepares _[[items/Weapon Magic Abilities/Flaming Burst|flaming burst]]_ arrows as her enhance arrows ability.
**During Combat **A arcane archer uses imbue arrows to fire off _cloudkill_, _stinking cloud_, and _entangle_ from a distance.
**Base Statistics **Without _see invisibility_, the arcane archer’s statistics are **Senses **_low-light vision_; Perception +26.

##### Statistics
**Str** 10, **Dex** 24, **Con** 14, **Int** 10, **Wis** 13, **Cha** 18
**Base Atk** +16; **CMB** +15; **CMD** 36
**Feats** _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Pinpoint Targeting|Pinpoint Targeting]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_, _[[feats/Shot on the Run|Shot on the Run]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_shortbow_)
**Skills** Bluff +27, Craft (bows) +8, Disguise +13, Knowledge (local, nature) +8, Perception +26, Spellcraft +8, Stealth +34, Swim +8, Use Magic Device +12
**Languages** Common, Gnome
**SQ** bloodline arcana (+2 DC for compulsion spells), _rogue_ talents (bleeding attack +3, combat trick, surprise attack), trapfinding +3, woodland stride
**Combat Gear** +1 dwarf-bane arrows (10), +1 elf-bane arrows (10), +1 human-bane arrows (10), +1 holy arrows (5), +1 _[[items/Weapon Magic Abilities/Unholy|unholy]]_ arrows (5), _[[items/Wondrous Item/Dust of Illusion|dust of illusion]]_, potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (3); **Other Gear** +3 mithral _[[items/Armor/Chain shirt|chain shirt]]_, +2 frost _shock_ _shortbow_ with 20 arrows, daggers (3), _[[items/Wondrous Item/Amulet of Natural Armor +3|amulet of natural armor +3]]_, _[[items/Wondrous Item/Belt of Physical Might +4|belt of physical might +4]]_ (Dex, Con), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Deck of Illusions|deck of illusions]]_, _[[items/Wondrous Item/Efficient Quiver|efficient quiver]]_, _[[items/Wondrous Item/Hat of Disguise|hat of disguise]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, _[[items/Wondrous Item/Rope of Climbing|rope of climbing]]_, 621 gp

Often whimsical in their _[[spells/Destruction|destruction]]_, chaos arrows roam the world playing the cruelest pranks for their own twisted amusement.