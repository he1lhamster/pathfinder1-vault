---
cssclass: [monsters]
title1: Arcane Experimenter
title2: Arcane Experimenter
CR: 13
sources:
- name: NPC Codex
  page: 19
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 25600
race: Gnome
classes:
- barbarian 14
alignment: CE
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 19
  touch: 12
  flat_footed: 16
  components:
    armor: 7
    dex: 3
    rage: -2
    size: 1
HP:
  HP: 191
  long: 14d12+95
saves:
  fort: 16
  ref: 8
  will: 9
  other: +2 vs. illusions, +4 vs. enchantments
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
- improved uncanny dodge
- indomitable will
- trap sense +4
DR:
- amount: 3
  weakness: '-'
immunities:
- frightened
- nauseated
- shaken
- sickened
speeds:
  base: 25
attacks:
  melee:
  - - text: +1 thundering gnome hooked hammer +21/+16/+11 (1d4+8/19-20/×4)
      entries:
      - - damage: 1d4+8
          crit_range: 19-20
          crit_multiplier: 4
      attack: +1 thundering gnome hooked hammer
      bonus:
      - 21
      - 16
      - 11
  - - text: +1 thundering gnome hooked hammer +19/+14/+9 (1d4+6/19-20/×4)
      entries:
      - - damage: 1d4+6
          crit_range: 19-20
          crit_multiplier: 4
      attack: +1 thundering gnome hooked hammer
      bonus:
      - 19
      - 14
      - 9
    - text: +1 gnome hooked hammer +19/+14 (1d6+6/19-20/×3)
      entries:
      - - damage: 1d6+6
          crit_range: 19-20
          crit_multiplier: 3
      attack: +1 gnome hooked hammer
      bonus:
      - 19
      - 14
    - text: bite +15 (1d3+2)
      entries:
      - - damage: 1d3+2
      attack: bite
      bonus:
      - 15
  ranged:
  - - text: mwk composite longbow +19/+14/+9 (1d6+5/×3)
      entries:
      - - damage: 1d6+5
          crit_multiplier: 3
      attack: mwk composite longbow
      bonus:
      - 19
      - 14
      - 9
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - greater rage (33 rounds/day)
  - rage powers (animal fury, clear mind, fearless rage, internal fortitude, mighty
    swing, moment of clarity, strength surge +14)
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: ghost sound
    source: default
    freq: 1/day
    DC: 11
  - name: prestidigitation
    source: default
    freq: 1/day
  - name: speak with animals
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 14
    concentration: 15
tactics:
  Before Combat: The barbarian uses her wand of shield before most battles, but also
    uses her wand of mirror image if she expects a difficult fight or a battle against
    a strong lone enemy.
  During Combat: The barbarian closes quickly to make full attacks with her hooked
    hammer, using the thundering pick end as her primary weapon and the hammer as
    her off-hand attack. If she has to charge or otherwise move between attacks, she
    makes a single two-handed Power Attack with the pick end. She uses moment of clarity
    to trigger a wand or scroll if the situation demands, such as in an encounter
    with a flying or invisible foe. She prefers to reserve her boots of speed for
    when she is already in melee, to facilitate full attacks or to close the distance
    on faster enemies.
  Base Statistics: When not raging, the barbarian's statistics are AC 21, touch 14,
    flat-footed 18; hp 149; Fort +13, Will +6; no bonus vs. enchantments; Immune -;
    Melee +1 thundering gnome hooked hammer +18/+13/+8 (1d4+4/19-20/×4) or +1 thundering
    gnome hooked hammer +16/+11/+6 (1d4+3/19-20/×4), +1 gnome hooked hammer +16/+11
    (1d6+3/19-20/×3); Ranged mwk composite longbow +19/+14/+9 (1d6+2/×3); Str 14,
    Con 16; CMB +15; CMD 28; Skills Climb +3.
ability_scores:
  STR: 20
  DEX: 17
  CON: 22
  INT: 8
  WIS: 12
  CHA: 12
BAB: 14
CMB: 18
CMD: 29
feats:
- name: Double Slice
- name: Improved Critical (gnome hooked hammer)
- name: Improved Two-Weapon Fighting
- name: Power Attack
- name: Skill Focus (Use Magic Device)
- name: Two-Weapon Fighting
- name: Two-Weapon Rend
skills:
  Acrobatics: 17
  Climb: 6
  Craft (alchemy): 5
  Knowledge (arcana): 0
  Perception: 20
  Spellcraft: 0
  Stealth: 5
  Survival: 5
  Use Magic Device: 18
languages:
- Common
- Gnome
- Sylvan
special_qualities:
- fast movement
gear:
  combat:
  - scroll of align weapon
  - scroll of cure light wounds
  - scroll of magic weapon
  - scroll of protection from good
  - scroll of true strike
  - wand of fly (10 charges)
  - wand of mirror image (10 charges)
  - wand of see invisibility (10 charges)
  - wand of shield (40 charges)
  - alchemical sliver arrows (10)
  - cold iron arrows (20)
  other:
  - +1 breastplate
  - +1 thundering/+1 gnome hooked hammer
  - masterwork composite longbow (+5 Str)
  - belt of giant strength +2
  - boots of speed
  - cloak of resistance +1
  - 8 gp
desc_long: An oddity among their kind, arcane experimenters use knowledge of magic
  to sow confusion on the battlefield.

---

# Arcane Experimenter

**Source** NPC Codex pg. 19
**XP** 25,600
Gnome _[[classes/Barbarian|barbarian]]_ 14
CE Small humanoid (gnome)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +20

##### Defense

**AC** 19, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 16 (+7 armor, +3 Dex, –2 _[[spells/Rage|rage]]_, +1 size)
**hp** 191 (14d12+95)
**Fort** +16, **Ref** +8, **Will** +9; +2 vs. illusions, +4 vs. enchantments
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 dodge bonus to AC vs. giants), improved uncanny _dodge_, indomitable will, trap sense +4; **DR** 3/—; **Immune** _[[conditions/Frightened|frightened]]_, _[[conditions/Nauseated|nauseated]]_, _[[conditions/Shaken|shaken]]_, _[[conditions/Sickened|sickened]]_

##### Offense
**Speed** 25 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Thundering|thundering]]_ _[[items/Weapon/Gnome hooked hammer|gnome hooked hammer]]_ +21/+16/+11 (1d4+8/19–20/×4) or +1 _thundering_ _gnome hooked hammer_ +19/+14/+9 (1d4+6/19–20/×4), +1 _gnome hooked hammer_ +19/+14 (1d6+6/19–20/×3), bite +15 (1d3+2)
**Ranged** mwk _[[items/Weapon/Composite longbow|composite longbow]]_ +19/+14/+9 (1d6+5/×3)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, greater _rage_ (33 rounds/day), _rage_ powers (animal fury, clear mind, fearless _rage_, internal fortitude, mighty swing, moment of _[[items/Weapon/Clarity|clarity]]_, strength surge +14)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 14th; concentration +15)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 11), _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_

### Tactics

**Before Combat **The _barbarian_ uses her wand of _[[spells/Shield|shield]]_ before most battles, but also uses her wand of _[[spells/Mirror Image|mirror image]]_ if she expects a difficult fight or a battle against a strong lone enemy.
**During Combat **The _barbarian_ closes quickly to make full attacks with her hooked _[[items/Mundane/Hammer|hammer]]_, using the _thundering_ pick end as her primary weapon and the _hammer_ as her off-hand attack. If she has to charge or otherwise move between attacks, she makes a single two-handed _[[feats/Power Attack|Power Attack]]_ with the pick end. She uses moment of _clarity_ to trigger a wand or scroll if the situation demands, such as in an encounter with a flying or _[[conditions/Invisible|invisible]]_ foe. She prefers to reserve her _[[items/Wondrous Item/Boots of Speed|boots of speed]]_ for when she is already in melee, to facilitate full attacks or to close the distance on faster enemies.
**Base Statistics **When not raging, the _barbarian_’s statistics are **AC **21, touch 14, _flat-footed_ 18; **hp **149; **Fort **+13, **Will **+6; no bonus vs. enchantments; **Immune **—; **Melee **+1 _thundering_ _gnome hooked hammer_ +18/+13/+8 (1d4+4/19–20/×4) or +1 _thundering_ _gnome hooked hammer_ +16/+11/+6 (1d4+3/19–20/×4), +1 _gnome hooked hammer_ +16/+11 (1d6+3/19–20/×3); **Ranged **mwk _composite longbow_ +19/+14/+9 (1d6+2/×3); **Str **14, **Con **16; **CMB **+15; **CMD **28; **Skills **_[[universal monster rules/Climb|Climb]]_ +3.

##### Statistics
**Str** 20, **Dex** 17, **Con** 22, **Int** 8, **Wis** 12, **Cha** 12
**Base Atk** +14; **CMB** +18; **CMD** 29
**Feats** _[[feats/Double Slice|Double Slice]]_, _[[feats/Improved Critical|Improved Critical]]_ (_gnome hooked hammer_), _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _Power Attack_, _[[feats/Skill Focus|Skill Focus]]_ (Use Magic Device), _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Two-Weapon Rend|Two-Weapon Rend]]_
**Skills** Acrobatics +17, _Climb_ +6, Craft (alchemy) +5, Knowledge (arcana) +0, Perception +20, Spellcraft +0, Stealth +5, Survival +5, Use Magic Device +18
**Languages** Common, Gnome, Sylvan
**SQ** fast movement
**Combat Gear** scroll of _[[spells/Align Weapon|align weapon]]_, scroll of _[[spells/Cure Light Wounds|cure light wounds]]_, scroll of _[[spells/Magic Weapon|magic weapon]]_, scroll of _[[spells/Protection From Good|protection from good]]_, scroll of _[[spells/True Strike|true strike]]_, wand of fly (10 charges), wand of _mirror image_ (10 charges), wand of _[[spells/See Invisibility|see invisibility]]_ (10 charges), wand of _shield_ (40 charges), alchemical sliver arrows (10), cold iron arrows (20); **Other Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 thundering/+1 _gnome hooked hammer_, masterwork _composite longbow_ (+5 Str), _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _boots of speed_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, 8 gp

An oddity among their kind, arcane experimenters use knowledge of magic to sow _[[spells/Confusion|confusion]]_ on the battlefield.