---
cssclass: [monsters]
title1: Giant Hunter
title2: Giant Hunter
CR: 14
sources:
- name: NPC Codex
  page: 122
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 38400
race: Gnome
classes:
- paladin 15
alignment: LG
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 4
senses:
  low-light vision: true
auras:
- name: courage
  radius: 10
- name: faith
  radius: 10
- name: justice
  radius: 10
- name: resolve
  radius: 10
AC:
  AC: 24
  touch: 13
  flat_footed: 24
  components:
    armor: 10
    deflection: 2
    natural: 1
    size: 1
HP:
  HP: 137
  long: 15d10+50
saves:
  fort: 16
  ref: 10
  will: 15
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
immunities:
- charm
- disease
- fear
speeds:
  base: 15
attacks:
  melee:
  - - text: +1 shock gnome hooked hammer +22/+17/+12 (1d6+7/×3 plus 1d6 electricity)
      entries:
      - - damage: 1d6+7
          crit_multiplier: 3
        - damage: 1d6
          type: electricity
      attack: +1 shock gnome hooked hammer
      bonus:
      - 22
      - 17
      - 12
  - - text: mwk gnome hooked hammer +22/+17/+12 (1d4+6/×4)
      entries:
      - - damage: 1d4+6
          crit_multiplier: 4
      attack: mwk gnome hooked hammer
      bonus:
      - 22
      - 17
      - 12
  ranged:
  - - text: +1 light crossbow +17 (1d6+1/19-20)
      entries:
      - - damage: 1d6+1
          crit_range: 19-20
      attack: +1 light crossbow
      bonus:
      - 17
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - channel positive energy (DC 20, 8d6)
  - smite evil 5/day (+3 attack and AC, +15 damage)
spell_like_abilities:
  entries:
  - name: detect evil
    source: default
    freq: At will
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
  sources:
  - name: default
    CL: 15
    concentration: 18
spells:
  entries:
  - name: holy sword
    source: Paladin
    level: 4
  - name: daylight
    source: Paladin
    level: 3
  - name: prayer
    source: Paladin
    level: 3
    count: 2
  - name: resist energy
    source: Paladin
    level: 2
    count: 2
  - name: shield other
    source: Paladin
    level: 2
  - name: bless
    source: Paladin
    level: 1
  - name: divine favor
    source: Paladin
    level: 1
    count: 2
  - name: endure elements
    source: Paladin
    level: 1
  sources:
  - name: Paladin
    type: prepared
    CL: 12
    concentration: 15
tactics:
  During Combat: The paladin uses divine bond to give her weapon a mix of the defending,
    flaming, and holy special abilities.
ability_scores:
  STR: 18
  DEX: 10
  CON: 15
  INT: 8
  WIS: 12
  CHA: 16
BAB: 15
CMB: 18
CMD: 30
feats:
- name: Bleeding Critical
- name: Critical Focus
- name: Extra Lay on Hands
- name: Improved Initiative
- name: Power Attack
- name: Toughness
- name: Vital Strike
- name: Weapon Focus (gnome hooked hammer)
skills:
  Knowledge (dungeoneering): 4
  Knowledge (local): 4
  Perception: 13
  Stealth: 8
languages:
- Common
- Gnome
- Sylvan
special_qualities:
- aura
- code of conduct
- divine bond (weapon +4, 3/day)
- lay on hands (7d6, 12/day)
- mercies (cursed, diseased, nauseated, sickened, stunned)
gear:
  combat:
  - potions of haste (2)
  other:
  - +2 shadow half-plate
  - +1 light crossbow with 20 bolts
  - +1 shock/masterwork gnome hooked hammer
  - amulet of natural armor +1
  - belt of giant strength +2
  - boots of striding and springing
  - cloak of resistance +2
  - ring of protection +2
  - 543 gp
desc_long: This paladin's lifelong mission is to eradicate evil giants.

---

# Giant Hunter

**Source** NPC Codex pg. 122
**XP** 38,400
Gnome _[[classes/Paladin|paladin]]_ 15

LG Small humanoid (gnome)
**Init** +4; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +13
**Aura** courage (10 ft.), faith (10 ft.), justice (10 ft.), resolve (10 ft.)

##### Defense

**AC** 24, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+10 armor, +2 deflection, +1 natural, +1 size)
**hp** 137 (15d10+50)
**Fort** +16, **Ref** +10, **Will** +15; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants); **Immune** charm, disease, _[[universal monster rules/Fear|fear]]_

##### Offense
**Speed** 15 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Shock|shock]]_ _[[items/Weapon/Gnome hooked hammer|gnome hooked hammer]]_ +22/+17/+12 (1d6+7/×3 plus 1d6 electricity) or mwk _gnome hooked hammer_ +22/+17/+12 (1d4+6/×4)
**Ranged** +1 _[[items/Weapon/Light crossbow|light crossbow]]_ +17 (1d6+1/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, channel positive energy (DC 20, 8d6), smite evil 5/day (+3 attack and AC, +15 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +18)
At will—_[[spells/Detect Evil|detect evil]]_
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
**_Paladin_ Spells Prepared **(CL 12th; concentration +15)
4th—_[[spells/Holy Sword|holy sword]]_
3rd—_[[spells/Daylight|daylight]]_, _[[spells/Prayer|prayer]]_ (2)
2nd—_[[spells/Resist Energy|resist energy]]_ (2), _[[spells/Shield Other|shield other]]_
1st—_[[spells/Bless|bless]]_, _[[spells/Divine Favor|divine favor]]_ (2), _[[spells/Endure Elements|endure elements]]_

### Tactics

**During Combat **The _paladin_ uses divine bond to give her weapon a mix of the _[[items/Weapon Magic Abilities/Defending|defending]]_, _[[items/Weapon Magic Abilities/Flaming|flaming]]_, and holy special abilities.

##### Statistics
**Str** 18, **Dex** 10, **Con** 15, **Int** 8, **Wis** 12, **Cha** 16
**Base Atk** +15; **CMB** +18; **CMD** 30
**Feats** _[[feats/Bleeding Critical|Bleeding Critical]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Extra Lay On Hands|Extra Lay on Hands]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_gnome hooked hammer_)
**Skills** Knowledge (dungeoneering, local) +4, Perception +13, Stealth +8
**Languages** Common, Gnome, Sylvan
**SQ** aura, code of conduct, divine bond (weapon +4, 3/day), lay on hands (7d6, 12/day), mercies (cursed, diseased, _[[conditions/Nauseated|nauseated]]_, _[[conditions/Sickened|sickened]]_, _[[conditions/Stunned|stunned]]_)
**Combat Gear** potions of _[[spells/Haste|haste]]_ (2); **Other Gear** +2 _[[items/Armor Magic Abilities/Shadow|shadow]]_ _[[items/Armor/Half-plate|half-plate]]_, +1 _light crossbow_ with 20 bolts, +1 shock/masterwork _gnome hooked hammer_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Boots of Striding and Springing|boots of striding and springing]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +2|cloak of _resistance_ +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 543 gp

This _paladin_’s lifelong mission is to eradicate evil giants.