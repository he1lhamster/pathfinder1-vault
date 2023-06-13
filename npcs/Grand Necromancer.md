---
cssclass: [monsters]
title1: Grand Necromancer
title2: Grand Necromancer
CR: 17
sources:
- name: NPC Codex
  page: 193
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 102400
race: Human
classes:
- necromancer 18
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 5
senses:
  see invisibility: true
AC:
  AC: 23
  touch: 16
  flat_footed: 22
  components:
    armor: 4
    deflection: 4
    dex: 1
    insight: 1
    natural: 3
HP:
  HP: 170
  long: 18d6+105
saves:
  fort: 14
  ref: 11
  will: 17
  other: +4 vs. mind-affecting
defensive_abilities:
- mind blank
- spell turning
resistances:
  cold: 20
  fire: 30
speeds:
  base: 30
attacks:
  melee:
  - - text: mwk silver dagger +9/+4 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: mwk silver dagger
      bonus:
      - 9
      - 4
  special:
  - channel negative energy (DC 19, 11/day)
spell_like_abilities:
  entries:
  - name: grave touch
    source: default
    freq: 11/day
    other: 9 rounds
  sources:
  - name: default
    CL: 18
    concentration: 26
spells:
  entries:
  - name: energy drain
    source: Necromancer
    level: 9
    DC: 29
  - name: time stop
    source: Necromancer
    level: 9
  - name: wail of the banshee
    source: Necromancer
    level: 9
    DC: 29
  - name: create greater undead
    source: Necromancer
    level: 8
  - name: horrid wilting
    source: Necromancer
    level: 8
    count: 3
    DC: 28
  - name: mind blank
    source: Necromancer
    level: 8
  - name: ethereal jaunt
    source: Necromancer
    level: 7
  - name: finger of death
    source: Necromancer
    level: 7
    DC: 27
  - name: quickened fireball
    source: Necromancer
    level: 7
    DC: 22
  - name: spell turning
    source: Necromancer
    level: 7
  - name: waves of exhaustion
    source: Necromancer
    level: 7
  - name: chain lightning
    source: Necromancer
    level: 6
    DC: 25
  - name: create undead
    source: Necromancer
    level: 6
  - name: disintegrate
    source: Necromancer
    level: 6
    DC: 24
  - name: eyebite
    source: Necromancer
    level: 6
    DC: 26
  - name: maximized vampiric touch
    source: Necromancer
    level: 6
    count: 2
  - name: cloudkill
    source: Necromancer
    level: 5
    DC: 23
  - name: quickened magic missile
    source: Necromancer
    level: 5
  - name: maximized scorching ray
    source: Necromancer
    level: 5
  - name: teleport
    source: Necromancer
    level: 5
  - name: wall of force
    source: Necromancer
    level: 5
  - name: waves of fatigue
    source: Necromancer
    level: 5
  - name: animate dead
    source: Necromancer
    level: 4
  - name: arcane eye
    source: Necromancer
    level: 4
  - name: bestow curse
    source: Necromancer
    level: 4
    count: 2
    DC: 24
  - name: dimension door
    source: Necromancer
    level: 4
  - name: fire shield
    source: Necromancer
    level: 4
  - name: maximized ray of enfeeblement
    source: Necromancer
    level: 4
  - name: blink
    source: Necromancer
    level: 3
  - name: dispel magic
    source: Necromancer
    level: 3
    count: 2
  - name: fireball
    source: Necromancer
    level: 3
    count: 2
    DC: 22
  - name: fly
    source: Necromancer
    level: 3
  - name: vampiric touch
    source: Necromancer
    level: 3
  - name: blindness/deafness
    source: Necromancer
    level: 2
    DC: 22
  - name: darkvision
    source: Necromancer
    level: 2
  - name: false life
    source: Necromancer
    level: 2
  - name: glitterdust
    source: Necromancer
    level: 2
    DC: 20
  - name: resist energy
    source: Necromancer
    level: 2
  - name: scorching ray
    source: Necromancer
    level: 2
  - name: see invisibility
    source: Necromancer
    level: 2
  - name: cause fear
    source: Necromancer
    level: 1
    DC: 21
  - name: expeditious retreat
    source: Necromancer
    level: 1
  - name: feather fall
    source: Necromancer
    level: 1
  - name: grease
    source: Necromancer
    level: 1
  - name: mage armor
    source: Necromancer
    level: 1
  - name: magic missile
    source: Necromancer
    level: 1
  - name: obscuring mist
    source: Necromancer
    level: 1
  - name: bleed
    source: Necromancer
    level: 0
    DC: 20
  - name: detect magic
    source: Necromancer
    level: 0
  - name: mage hand
    source: Necromancer
    level: 0
  - name: read magic
    source: Necromancer
    level: 0
  sources:
  - name: Necromancer
    type: prepared
    CL: 18
    concentration: 26
    slots:
      0: at-will
    opposition_schools:
    - enchantment
    - illusion
tactics:
  Before Combat: The wizard casts false life, mage armor, mind blank, resist energy
    (fire), see invisibility, and spell turning.
  During Combat: The wizard casts time stop and energy drain on the most dangerous-looking
    target, then thins out the ranks of his enemies with chain lightning.
  Base Statistics: Without false life, mage armor, mind blank, resist energy (fire),
    see invisibility, and spell turning, the wizard's statistics are AC 19, touch
    16, flat-footed 18; hp 155; Fort +14, Ref +11, Will +17; Defensive Abilities none;
    Resist cold 20.
ability_scores:
  STR: 8
  DEX: 12
  CON: 18
  INT: 26
  WIS: 14
  CHA: 10
BAB: 9
CMB: 8
CMD: 23
feats:
- name: Alertness
- name: Combat Casting
- name: Command Undead
- name: Craft Wondrous Item
- name: Extra Channel
- name: Forge Ring
- name: Greater Spell Focus (necromancy)
- name: Improved Channel
- name: Improved Initiative
- name: Maximize Spell
- name: Quicken Spell
- name: Scribe Scroll
- name: Spell Focus (evocation)
- name: Spell Focus (necromancy)
- name: Toughness
- name: Weapon Focus (ray)
skills:
  Fly: 22
  Heal: 20
  Intimidate: 16
  Knowledge (arcana): 29
  Knowledge (planes): 29
  Knowledge (religion): 29
  Knowledge (history): 21
  Knowledge (local): 21
  Perception: 24
  Sense Motive: 24
  Spellcraft: 29
  Stealth: 19
  Use Magic Device: 18
languages:
- Aklo
- Common
- Draconic
- Dwarven
- Elven
- Gnome
- Goblin
- Orc
- Undercommon
special_qualities:
- arcane bond (owl)
- life sight (30 feet, 18 rounds/day)
gear:
  combat:
  - potions of cure serious wounds (3)
  - scroll of iron body
  - scroll of spell turning
  - scroll of wall of force
  - wand of inflict moderate wounds (20 charges)
  - wand of invisibility (20 charges)
  other:
  - masterwork silver dagger
  - amulet of natural armor +3
  - belt of mighty constitution +4
  - clear spindle ioun stone
  - cloak of resistance +4
  - dusty rose prism ioun stone
  - headband of vast intelligence +6
  - restorative ointment
  - ring of major energy resistance (cold)
  - ring of protection +4
  - onyx gems (worth 2,000 gp)
  - spellbook
  - 8,973 gp
desc_long: These wizards are steeped in the evil of their profession.

---

# Grand Necromancer

**Source** NPC Codex pg. 193
**XP** 102,400
Human necromancer 18

NE Medium humanoid (human)
**Init** +5; **Senses** _[[spells/See Invisibility|see invisibility]]_; Perception +24

##### Defense

**AC** 23, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+4 armor, +4 _[[spells/Deflection|deflection]]_, +1 Dex, +1 insight, +3 natural)
**hp** 170 (18d6+105)
**Fort** +14, **Ref** +11, **Will** +17; +4 vs. mind-affecting
**Defensive Abilities** _[[spells/Mind Blank|mind blank]]_, _[[spells/Spell Turning|spell turning]]_; **Resist** cold 20, fire 30

##### Offense
**Speed** 30 ft.
**Melee** mwk silver _[[items/Weapon/Dagger|dagger]]_ +9/+4 (1d4–1/19–20)
**Special Attacks** channel negative energy (DC 19, 11/day)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +26)
11/day—grave touch (9 rounds)
**Necromancer Spells Prepared **(CL 18th; concentration +26)
9th—_[[universal monster rules/Energy Drain|energy drain]]_ (DC 29), _[[spells/Time Stop|time stop]]_, _[[spells/Wail of the Banshee|wail of the banshee]]_ (DC 29)
8th—_[[spells/Create Greater Undead|create greater undead]]_, _[[spells/Horrid Wilting|horrid wilting]]_ (3, DC 28), _mind blank_
7th—_[[spells/Ethereal Jaunt|ethereal jaunt]]_, _[[spells/Finger Of Death|finger of death]]_ (DC 27), quickened _[[spells/Fireball|fireball]]_ (DC 22), _spell turning_, _[[spells/Waves of Exhaustion|waves of exhaustion]]_
6th—_[[spells/Chain Lightning|chain lightning]]_ (DC 25), _[[spells/Create Undead|create undead]]_, _[[spells/Disintegrate|disintegrate]]_ (DC 24), _[[spells/Eyebite|eyebite]]_ (DC 26), maximized _[[spells/Vampiric Touch|vampiric touch]]_ (2)
5th—_[[spells/Cloudkill|cloudkill]]_ (DC 23), quickened _[[spells/Magic Missile|magic missile]]_, maximized _[[spells/Scorching Ray|scorching ray]]_, teleport, _[[spells/Wall Of Force|wall of force]]_, _[[spells/Waves of Fatigue|waves of fatigue]]_
4th—_[[spells/Animate Dead|animate dead]]_, _[[spells/Arcane Eye|arcane eye]]_, _[[spells/Bestow Curse|bestow curse]]_ (2, DC 24), _[[spells/Dimension Door|dimension door]]_, _[[spells/Fire Shield|fire shield]]_, maximized _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_
3rd—_[[spells/Blink|blink]]_, _[[spells/Dispel Magic|dispel magic]]_ (2), _fireball_ (2, DC 22), fly, _vampiric touch_
2nd—blindness/deafness (DC 22), _[[spells/Darkvision|darkvision]]_, _[[spells/False Life|false life]]_, _[[spells/Glitterdust|glitterdust]]_ (DC 20), _[[spells/Resist Energy|resist energy]]_, _scorching ray_, _see invisibility_
1st—_[[spells/Cause Fear|cause fear]]_ (DC 21), _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Grease|grease]]_, _[[spells/Mage Armor|mage armor]]_, _magic missile_, _[[spells/Obscuring Mist|obscuring mist]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 20), _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_
**Opposition Schools **enchantment, illusion

### Tactics

**Before Combat **The _[[classes/Wizard|wizard]]_ casts _false life_, _mage armor_, _mind blank_, _resist energy_ (fire), _see invisibility_, and _spell turning_.
**During Combat **The _wizard_ casts _time stop_ and _energy drain_ on the most dangerous-looking target, then thins out the ranks of his enemies with _chain lightning_.
**Base Statistics **Without _false life_, _mage armor_, _mind blank_, _resist energy_ (fire), _see invisibility_, and _spell turning_, the _wizard_’s statistics are **AC **19, touch 16, _flat-footed_ 18; **hp **155; **Fort **+14, **Ref **+11, **Will **+17; **Defensive Abilities **none; **Resist **cold 20.

##### Statistics
**Str** 8, **Dex** 12, **Con** 18, **Int** 26, **Wis** 14, **Cha** 10
**Base Atk** +9; **CMB** +8; **CMD** 23
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[spells/Command Undead|Command Undead]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Forge Ring|Forge Ring]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (necromancy), _[[feats/Improved Channel|Improved Channel]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Maximize Spell|Maximize Spell]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation, necromancy), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (ray)
**Skills** Fly +22, _[[spells/Heal|Heal]]_ +20, Intimidate +16, Knowledge (arcana, planes, religion) +29, Knowledge (history, local) +21, Perception +24, Sense Motive +24, Spellcraft +29, Stealth +19, Use Magic Device +18
**Languages** Aklo, Common, Draconic, Dwarven, Elven, Gnome, _[[monsters/Goblin|Goblin]]_, _[[monsters/Orc|Orc]]_, Undercommon
**SQ** arcane bond (owl), life sight (30 feet, 18 rounds/day)
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (3), scroll of _[[spells/Iron Body|iron body]]_, scroll of _spell turning_, scroll of _wall of force_, wand of _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_ (20 charges), wand of _[[spells/Invisibility|invisibility]]_ (20 charges); **Other Gear** _[[items/Weapon/Masterwork Silver Dagger|masterwork silver dagger]]_, _[[items/Wondrous Item/Amulet of Natural Armor +3|amulet of natural armor +3]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +4|belt of mighty constitution +4]]_, _[[items/Wondrous Item/Clear Spindle Ioun Stone|clear spindle ioun stone]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +4|cloak of _resistance_ +4]]_, _[[items/Wondrous Item/Dusty Rose Prism Ioun Stone|dusty rose prism ioun stone]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +6|headband of vast intelligence +6]]_, _[[items/Wondrous Item/Restorative Ointment|restorative ointment]]_, ring of major _[[items/Armor Magic Abilities/Energy Resistance|energy resistance]]_ (cold), _[[items/Ring/Ring of Protection +4|ring of protection +4]]_, onyx gems (worth 2,000 gp), _[[items/Mundane/Spellbook|spellbook]]_, 8,973 gp

These wizards are steeped in the evil of their profession.