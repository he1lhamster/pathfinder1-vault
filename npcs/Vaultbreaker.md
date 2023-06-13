---
cssclass: [monsters]
title1: Vaultbreaker
title2: Vaultbreaker
CR: 16
sources:
- name: NPC Codex
  page: 206
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Human
classes:
- rogue 6
- transmuter 4
- arcane trickster 7
alignment: NE
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 5
AC:
  AC: 24
  touch: 18
  flat_footed: 18
  components:
    armor: 4
    deflection: 2
    dex: 5
    dodge: 1
    natural: 2
HP:
  HP: 109
  long: 6d8+4d6+7d6+40
saves:
  fort: 9
  ref: 19
  will: 13
defensive_abilities:
- evasion
- trap sense +2
- uncanny dodge
speeds:
  base: 40
attacks:
  melee:
  - - text: +1 frost rapier +15/+10 (1d6/18-20)
      entries:
      - - damage: 1d6
          crit_range: 18-20
      attack: +1 frost rapier
      bonus:
      - 15
      - 10
  ranged:
  - - text: mwk dagger +15 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: mwk dagger
      bonus:
      - 15
  special:
  - impromptu sneak attack 2/day
  - sneak attack +6d6
spell_like_abilities:
  entries:
  - name: telekinetic fist
    source: default
    freq: 8/day
  sources:
  - name: default
    CL: 11
    concentration: 16
spells:
  entries:
  - name: antimagic field
    source: Transmuter
    level: 6
  - name: disintegrate
    source: Transmuter
    level: 6
    DC: 22
  - name: passwall
    source: Transmuter
    level: 5
  - name: prying eyes
    source: Transmuter
    level: 5
  - name: teleport
    source: Transmuter
    level: 5
  - name: transmute rock to mud
    source: Transmuter
    level: 5
  - name: beast shape II
    source: Transmuter
    level: 4
  - name: charm monster
    source: Transmuter
    level: 4
    DC: 19
  - name: dimension door
    source: Transmuter
    level: 4
  - name: greater invisibility
    source: Transmuter
    level: 4
  - name: illusory wall
    source: Transmuter
    level: 4
    DC: 19
  - name: blink
    source: Transmuter
    level: 3
  - name: dispel magic
    source: Transmuter
    level: 3
  - name: fly
    source: Transmuter
    level: 3
  - name: slow
    source: Transmuter
    level: 3
    DC: 19
  - name: stinking cloud
    source: Transmuter
    level: 3
    DC: 18
  - name: water breathing
    source: Transmuter
    level: 3
  - name: flaming sphere
    source: Transmuter
    level: 2
    DC: 17
  - name: invisibility
    source: Transmuter
    level: 2
  - name: knock
    source: Transmuter
    level: 2
  - name: levitate
    source: Transmuter
    level: 2
  - name: mirror image
    source: Transmuter
    level: 2
  - name: spider climb
    source: Transmuter
    level: 2
  - name: comprehend languages
    source: Transmuter
    level: 1
  - name: detect secret doors
    source: Transmuter
    level: 1
  - name: expeditious retreat
    source: Transmuter
    level: 1
  - name: feather fall
    source: Transmuter
    level: 1
  - name: obscuring mist
    source: Transmuter
    level: 1
  - name: shield
    source: Transmuter
    level: 1
  - name: sleep
    source: Transmuter
    level: 1
    DC: 16
  - name: detect magic
    source: Transmuter
    level: 0
  - name: ghost sound
    source: Transmuter
    level: 0
  - name: mage hand
    source: Transmuter
    level: 0
  - name: open/close
    source: Transmuter
    level: 0
  sources:
  - name: Transmuter
    type: prepared
    CL: 11
    concentration: 16
    failure_chance: 10%
    slots:
      0: at-will
    opposition_schools:
    - evocation
    - necromancy
tactics:
  During Combat: The arcane trickster uses teleport, greater invisibility, blink,
    and fly to keep out of melee. If forced into melee, she uses Spring Attack and
    Vital Strike to make quick, devastating attacks before leaping away.
ability_scores:
  STR: 9
  DEX: 20
  CON: 14
  INT: 20
  WIS: 12
  CHA: 10
BAB: 9
CMB: 8
CMD: 26
feats:
- name: Arcane Strike
- name: Dodge
- name: Fleet (2)
- name: Lightning Reflexes
- name: Mobility
- name: Point-Blank Shot
- name: Scribe Scroll
- name: Spell Focus (transmutation)
- name: Spring Attack
- name: Vital Strike
- name: Weapon Finesse
skills:
  Acrobatics: 18
    when jumping: 22
  Appraise: 18
  Climb: 12
  Disable Device: 25
  Disguise: 8
  Escape Artist: 13
  Knowledge (arcana): 13
  Knowledge (geography): 13
  Knowledge (history): 13
  Knowledge (local): 13
  Knowledge (nature): 13
  Knowledge (nobility): 13
  Knowledge (planes): 13
  Knowledge (religion): 13
  Knowledge (dungeoneering): 18
  Knowledge (engineering): 18
  Perception: 21
  Sleight of Hand: 13
  Spellcraft: 18
  Stealth: 25
  Survival: 6
  Swim: 7
  Use Magic Device: 13
languages:
- Celestial
- Common
- Draconic
- Dwarven
- Elf
- Gnome
- Goblin
special_qualities:
- arcane bond (+1 frost rapier)
- physical enhancement +1 (Strength)
- ranged legerdemain
- rogue talents (finesse rogue, surprise attack, trap spotter)
- trapfinding +3
- tricky spells 4/day
gear:
  combat:
  - potions of cure serious wounds (2)
  - scrolls of dispel magic (3)
  other:
  - +2 leather armor
  - +1 frost rapier
  - masterwork daggers (5)
  - amulet of natural armor +2
  - belt of incredible dexterity +4
  - boots of speed
  - chime of opening
  - cloak of resistance +2
  - headband of vast intelligence +2
  - lens of detection
  - ring of protection +2
  - spell component pouch
  - spellbook
  - 167 gp
desc_long: Masters at breaking into treasure vaults, many arcane tricksters are more
  interested in the challenge of such break-ins than the riches they gain from them.

---

# Vaultbreaker

**Source** NPC Codex pg. 206
**XP** 76,800
Human _[[classes/Rogue|rogue]]_ 6/transmuter 4/arcane trickster 7

NE Medium humanoid (human)
**Init** +5; **Senses** Perception +21

##### Defense

**AC** 24, touch 18, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +2 _[[spells/Deflection|deflection]]_, +5 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural)
**hp** 109 (6d8+4d6+7d6+40)
**Fort** +9, **Ref** +19, **Will** +13
**Defensive Abilities** evasion, trap sense +2, uncanny _dodge_

##### Offense
**Speed** 40 ft.
**Melee** +1 frost _[[items/Weapon/Rapier|rapier]]_ +15/+10 (1d6/18–20)
**Ranged** mwk _[[items/Weapon/Dagger|dagger]]_ +15 (1d4–1/19–20)
**Special Attacks** impromptu sneak attack 2/day, sneak attack +6d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 11th; concentration +16)
8/day—telekinetic fist
**Transmuter Spells Prepared **(CL 11th; concentration +16; arcane spell failure 10%)
6th—_[[spells/Antimagic Field|antimagic field]]_, _[[spells/Disintegrate|disintegrate]]_ (DC 22)
5th—_[[spells/Passwall|passwall]]_, _[[spells/Prying Eyes|prying eyes]]_, teleport, _[[spells/Transmute Rock to Mud|transmute rock to mud]]_
4th—_[[spells/Beast Shape II|beast shape II]]_, _[[spells/Charm Monster|charm monster]]_ (DC 19), _[[spells/Dimension Door|dimension door]]_, greater _[[spells/Invisibility|invisibility]]_, _[[spells/Illusory Wall|illusory wall]]_ (DC 19)
3rd—_[[spells/Blink|blink]]_, _[[spells/Dispel Magic|dispel magic]]_, fly, _[[spells/Slow|slow]]_ (DC 19), _[[spells/Stinking Cloud|stinking cloud]]_ (DC 18), _[[universal monster rules/Water Breathing|water breathing]]_
2nd—_[[spells/Flaming Sphere|flaming sphere]]_ (DC 17), _invisibility_, _[[spells/Knock|knock]]_, _[[spells/Levitate|levitate]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Spider Climb|spider climb]]_
1st—_[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Detect Secret Doors|detect secret doors]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield|shield]]_, sleep (DC 16)
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Mage Hand|mage hand]]_, open/close
**Opposition Schools **evocation, necromancy

### Tactics

**During Combat **The arcane trickster uses _[[spells/Teleport, Greater|teleport, greater]]_ _invisibility_, _blink_, and fly to keep out of melee. If forced into melee, she uses _[[feats/Spring Attack|Spring Attack]]_ and _[[feats/Vital Strike|Vital Strike]]_ to make quick, devastating attacks before leaping away.

##### Statistics
**Str** 9, **Dex** 20, **Con** 14, **Int** 20, **Wis** 12, **Cha** 10
**Base Atk** +9; **CMB** +8; **CMD** 26
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _Dodge_, _[[feats/Fleet|Fleet]]_ (2), _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (transmutation), _Spring Attack_, _Vital Strike_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Acrobatics +18 (+22 when jumping), Appraise +18, _[[universal monster rules/Climb|Climb]]_ +12, Disable Device +25, Disguise +8, Escape Artist +13, Knowledge (arcana, geography, history, local, nature, nobility, planes, religion) +13, Knowledge (dungeoneering, engineering) +18, Perception +21, Sleight of Hand +13, Spellcraft +18, Stealth +25, Survival +6, Swim +7, Use Magic Device +13
**Languages** Celestial, Common, Draconic, Dwarven, Elf, Gnome, _[[monsters/Goblin|Goblin]]_
**SQ** arcane bond (+1 frost _rapier_), physical enhancement +1 (Strength), ranged legerdemain, _rogue_ talents (finesse _rogue_, surprise attack, trap spotter), trapfinding +3, tricky spells 4/day
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), scrolls of _dispel magic_ (3); **Other Gear** +2 _[[items/Armor/Leather armor|leather armor]]_, +1 frost _rapier_, masterwork daggers (5), _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Incredible Dexterity +4|belt of incredible dexterity +4]]_, _[[items/Wondrous Item/Boots of Speed|boots of speed]]_, _[[items/Wondrous Item/Chime of Opening|chime of opening]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +2|headband of vast intelligence +2]]_, _[[items/Wondrous Item/Lens of Detection|lens of detection]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, _[[items/Mundane/Spellbook|spellbook]]_, 167 gp

Masters at _[[items/Weapon Magic Abilities/Breaking|breaking]]_ into treasure vaults, many arcane tricksters are more interested in the challenge of such break-ins than the riches they gain from them.