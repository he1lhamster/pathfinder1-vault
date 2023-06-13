---
cssclass: [monsters]
title1: Adventurer (Battle Mage)
title2: Adventurer (Battle Mage)
CR: 5
sources:
- name: GameMastery Guide
  page: 256
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 1600
race: Human
classes:
- evoker 6
alignment: N
size: Medium
type: humanoid
initiative:
  bonus: 6
AC:
  AC: 16
  touch: 12
  flat_footed: 14
  components:
    mage armor: 4
    dex: 2
HP:
  HP: 33
  long: 6d6+12
saves:
  fort: 3
  ref: 4
  will: 5
speeds:
  base: 30
attacks:
  melee:
  - - text: dagger +2 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 2
  - - text: wand of shocking grasp +2 touch (1d6 electricity)
      entries:
      - - damage: 1d6
          type: electricity
      attack: wand of shocking grasp
      bonus:
      - 2
      touch: true
  ranged:
  - - text: dagger +5 (1d4-1/19-20)
      entries:
      - - damage: 1d4-1
          crit_range: 19-20
      attack: dagger
      bonus:
      - 5
  special:
  - intense spells +3
spells:
  entries:
  - name: dispel magic
    source: Wizard
    level: 3
  - name: fly
    source: Wizard
    level: 3
  - name: haste
    source: Wizard
    level: 3
  - name: fireball
    source: Wizard
    level: 3
    count: 2
    DC: 17
  - name: flaming sphere
    source: Wizard
    level: 2
    DC: 16
  - name: glitterdust
    source: Wizard
    level: 2
    DC: 15
  - name: mirror image
    source: Wizard
    level: 2
  - name: protection from arrows
    source: Wizard
    level: 2
  - name: scorching ray
    source: Wizard
    level: 2
    DC: 16
  - name: burning hands
    source: Wizard
    level: 1
    DC: 15
  - name: color spray
    source: Wizard
    level: 1
    DC: 14
  - name: expeditious retreat
    source: Wizard
    level: 1
  - name: mage armor
    source: Wizard
    level: 1
  - name: shocking grasp
    source: Wizard
    level: 1
  - name: dancing lights
    source: Wizard
    level: 0
  - name: detect magic
    source: Wizard
    level: 0
  - name: light
    source: Wizard
    level: 0
  - name: message
    source: Wizard
    level: 0
  sources:
  - name: Wizard
    type: prepared
    CL: 6
    concentration: 9
    slots:
      0: at-will
    opposition_schools:
    - enchantment
    - necromancy
ability_scores:
  STR: 9
  DEX: 14
  CON: 12
  INT: 17
  WIS: 10
  CHA: 13
BAB: 3
CMB: 2
CMD: 17
feats:
- name: Combat Casting
- name: Craft Wand
- name: Defensive Combat Training
- name: Improved Initiative
- name: Scribe Scroll
- name: Spell Focus (evocation)
skills:
  Craft (Armor): 10
  Craft (Weapons): 10
  Fly: 11
  Knowledge (arcana): 12
  Knowledge (engineering): 7
  Knowledge (geography): 7
  Knowledge (history): 7
  Perception: 6
  Ride: 6
  Spellcraft: 12
languages:
- Common
- Draconic
- Elven
- Giant
special_qualities:
- arcane bond (wand)
gear:
  combat:
  - scrolls of fly (2)
  - invisibility (2)
  - minor image (2)
  - wand of magic missile (CL 5, 50 charges, arcane bond item)
  - wand of shocking grasp (50 charges)
  - tanglefoot bags (3)
  other:
  - daggers (2)
  - 20 gp
npc_boon: A battle mage can create scrolls at a 10% discount.
desc_long: A battle mage is always ready for a fight. She knows that the one who strikes
  first strikes best. Never lacking in firepower, her versatility on the battlefield
  is always appreciated. Battle mages make excellent military fire support and magical
  bodyguards. They can be found alone, guarding a traveling merchant (CR 7) or guide
  (CR 8) or adventuring with a medium or minstrel, monster hunter or gladiator, and
  tomb raider (CR 9). A squad of four battle mages (CR 9) might be attached to an
  army.

---

# Adventurer (Battle Mage)

**Source** GameMastery Guide pg. 256
**XP** 1,600
Human evoker 6

N Medium humanoid
**Init** +6; **Senses** Perception +6

##### Defense

**AC** 16, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+4 _[[spells/Mage Armor|mage armor]]_, +2 Dex)
**hp** 33 (6d6+12)
**Fort** +3, **Ref** +4, **Will** +5

##### Offense
**Speed** 30 ft.
**Melee** _[[items/Weapon/Dagger|dagger]]_ +2 (1d4–1/19–20) or wand of _[[spells/Shocking Grasp|shocking grasp]]_ +2 touch (1d6 electricity)
**Ranged** _dagger_ +5 (1d4–1/19–20)
**Special Attacks** intense spells +3
**_[[classes/Wizard|Wizard]]_ Spells Prepared **(CL 6th; concentration +9)
3rd—_[[spells/Dispel Magic|dispel magic]]_, fly, _[[spells/Haste|haste]]_, _[[spells/Fireball|fireball]]_ (2) (DC 17)
2nd—_[[spells/Flaming Sphere|flaming sphere]]_ (DC 16), _[[spells/Glitterdust|glitterdust]]_ (DC 15), _[[spells/Mirror Image|mirror image]]_, _[[spells/Protection From Arrows|protection from arrows]]_, _[[spells/Scorching Ray|scorching ray]]_ (DC 16)
1st—_[[spells/Burning Hands|burning hands]]_ (DC 15), _[[spells/Color Spray|color spray]]_ (DC 14), _[[spells/Expeditious Retreat|expeditious retreat]]_, _mage armor_, _shocking grasp_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Message|message]]_
**Prohibited Schools** enchantment, necromancy

##### Statistics
**Str** 9, **Dex** 14, **Con** 12, **Int** 17, **Wis** 10, **Cha** 13
**Base Atk** +3; **CMB** +2; **CMD** 17
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Craft Wand|Craft Wand]]_, _[[feats/Defensive Combat Training|Defensive Combat Training]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Spell Focus|Spell Focus]]_ (evocation)
**Skills** Craft (Armor) +10, Craft (Weapons) +10, Fly +11, Knowledge (arcana) +12, Knowledge (engineering) +7, Knowledge (geography) +7, Knowledge (history) +7, Perception +6, Ride +6, Spellcraft +12
**Languages** Common, Draconic, Elven, Giant
**SQ** arcane bond (wand)
**Combat Gear** scrolls of fly (2), _[[spells/Invisibility|invisibility]]_ (2), _[[spells/Minor Image|minor image]]_ (2), wand of _[[spells/Magic Missile|magic missile]]_ (CL 5, 50 charges, arcane bond item), wand of _shocking grasp_ (50 charges), tanglefoot bags (3); **Other Gear** daggers (2), 20 gp

**Boon** A _[[npcs/Battle Mage|battle mage]]_ can create scrolls at a 10% discount.

A _battle mage_ is always ready for a fight. She knows that the one who strikes first strikes best. Never lacking in firepower, her versatility on the battlefield is always appreciated. Battle mages make excellent military fire support and magical bodyguards. They can be found alone, _[[items/Armor Magic Abilities/Guarding|guarding]]_ a traveling merchant (CR 7) or guide (CR 8) or adventuring with a _medium_ or minstrel, monster _[[classes/Hunter|hunter]]_ or gladiator, and tomb raider (CR 9). A squad of four battle mages (CR 9) might be attached to an army.