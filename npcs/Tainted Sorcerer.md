---
cssclass: [monsters]
title1: Tainted Sorcerer
title2: Tainted Sorcerer
CR: 3
sources:
- name: NPC Codex
  page: 161
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 800
race: Gnome
classes:
- sorcerer 4
alignment: CE
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 1
senses:
  low-light vision: true
AC:
  AC: 13
  touch: 12
  flat_footed: 12
  components:
    armor: 1
    dex: 1
    size: 1
HP:
  HP: 28
  long: 4d6+12
saves:
  fort: 3
  ref: 2
  will: 6
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk spear +5 (1d6+1/×3)
      entries:
      - - damage: 1d6+1
          crit_multiplier: 3
      attack: mwk spear
      bonus:
      - 5
  ranged:
  - - text: light crossbow +4 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: light crossbow
      bonus:
      - 4
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - long limbs (+5 ft.)
spell_like_abilities:
  entries:
  - name: acidic ray
    source: default
    freq: 7/day
    other: 1d6+2 acid
  - name: dancing lights
    source: default
    freq: 1/day
  - name: ghost sound
    source: default
    freq: 1/day
    DC: 15
  - name: prestidigitation
    source: default
    freq: 1/day
  - name: speak with animals
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 4
    concentration: 8
spells:
  entries:
  - name: alter self
    source: Sorcerer
    level: 2
  - name: enlarge person
    source: Sorcerer
    level: 1
    DC: 16
  - name: reduce person
    source: Sorcerer
    level: 1
    DC: 16
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
    DC: 14
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 14
  sources:
  - name: Sorcerer
    type: known
    CL: 4
    concentration: 8
    slots:
      2: 4
      1: 7
      0: at-will
    bloodline: aberrant
tactics:
  During Combat: The sorcerer casts shield, targets approaching enemies with acidic
    ray, then uses her long limbs ability to deliver touch spells. In melee, she casts
    enlarge person on herself and attacks with her spear.
ability_scores:
  STR: 12
  DEX: 13
  CON: 14
  INT: 8
  WIS: 10
  CHA: 18
BAB: 2
CMB: 2
CMD: 13
feats:
- name: Eschew Materials
- name: Iron Will
- name: Spell Focus (transmutation)
skills:
  Bluff: 8
  Craft (alchemy): 5
  Disguise: 5
  Perception: 2
  Use Magic Device: 8
languages:
- Common
- Gnome
- Sylvan
special_qualities:
- bloodline arcana (+50% duration on polymorph spells)
- gnome magic
gear:
  combat:
  - potion of spider climb
  - scrolls of cat's grace (2)
  - scroll of slow
  - acid
  - tanglefoot bag
  other:
  - light crossbow with 10 bolts
  - masterwork spear
  - bracers of armor +1
  - collection of dolls' heads
  - 28 gp
desc_long: The tainted sorcerer's mind and body have been warped by alien or extraplanar
  magic.

---

# Tainted Sorcerer

**Source** NPC Codex pg. 161
**XP** 800
Gnome _[[classes/Sorcerer|sorcerer]]_ 4
CE Small humanoid (gnome)
**Init** +1; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +2

##### Defense

**AC** 13, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 12 (+1 armor, +1 Dex, +1 size)
**hp** 28 (4d6+12)
**Fort** +3, **Ref** +2, **Will** +6; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 dodge bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Spear|spear]]_ +5 (1d6+1/×3)
**Ranged** _[[items/Weapon/Light crossbow|light crossbow]]_ +4 (1d6/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, long limbs (+5 ft.)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +8)
7/day—acidic ray (1d6+2 acid)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
**_Sorcerer_ Spells Known **(CL 4th; concentration +8)
2nd (4/day)—_[[spells/Alter Self|alter self]]_
1st (7/day)—_[[spells/Enlarge Person|enlarge person]]_ (DC 16), _[[spells/Reduce Person|reduce person]]_ (DC 16), _[[spells/Shield|shield]]_, _[[spells/Shocking Grasp|shocking grasp]]_
0 (at will)—_[[spells/Acid Splash|acid splash]]_, _[[universal monster rules/Bleed|bleed]]_ (DC 14), _[[spells/Detect Magic|detect magic]]_, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 14)
**Bloodline **aberrant

### Tactics

**During Combat **The _sorcerer_ casts _shield_, targets approaching enemies with acidic ray, then uses her long limbs ability to deliver touch spells. In melee, she casts _enlarge person_ on herself and attacks with her _spear_.

##### Statistics
**Str** 12, **Dex** 13, **Con** 14, **Int** 8, **Wis** 10, **Cha** 18
**Base Atk** +2; **CMB** +2; **CMD** 13
**Feats** _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Spell Focus|Spell Focus]]_ (transmutation)
**Skills** Bluff +8, Craft (alchemy) +5, Disguise +5, Perception +2, Use Magic Device +8
**Languages** Common, Gnome, Sylvan
**SQ** bloodline arcana (+50% duration on _[[spells/Polymorph|polymorph]]_ spells), gnome magic
**Combat Gear** potion of _[[spells/Spider Climb|spider climb]]_, scrolls of cat’s _[[spells/Grace|grace]]_ (2), scroll of _[[spells/Slow|slow]]_, acid, _[[items/Mundane/Tanglefoot bag|tanglefoot bag]]_; **Other Gear** _light crossbow_ with 10 bolts, masterwork _spear_, _[[items/Wondrous Item/Bracers of Armor +1|bracers of armor +1]]_, collection of dolls’ heads, 28 gp

The _[[npcs/Tainted Sorcerer|tainted sorcerer]]_’s mind and body have been warped by alien or extraplanar magic.