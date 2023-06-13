---
cssclass: [monsters]
title1: Vampire
desc_short: This aristocratic figure could easily pass for human if not for the grave-pale
  skin, red eyes, and long fangs.
title2: Mythic Vampire
CR: 10
MR: 4
sources:
- name: Mythic Adventures
  page: 220
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 9600
race: Human
classes:
- vampire fighter 7
alignment: NE
size: Medium
type: undead
subtypes:
- augmented humanoid
- human
- mythic
initiative:
  bonus: 12
senses:
  darkvision: 60
AC:
  AC: 29
  touch: 16
  flat_footed: 24
  components:
    armor: 3
    deflection: 1
    dex: 4
    dodge: 1
    natural: 10
HP:
  HP: 117
  long: 7d10+74
  fast_healing: 5
saves:
  fort: 11
  ref: 10
  will: 4
  will_other: +2 vs. fear
defensive_abilities:
- bravery +2
DR:
- amount: 10
  weakness: epic and magic and silver
immunities:
- undead traits
resistances:
  cold: 10
  electricity: 10
weaknesses:
- vampire weaknesses
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 longsword +19/+14 (1d8+12/19-20 plus energy drain)
      entries:
      - - damage: 1d8+12
          crit_range: 19-20
        - effect: energy drain
      attack: +1 longsword
      bonus:
      - 19
      - 14
    - text: slam +15 (1d4+4 plus energy drain)
      entries:
      - - damage: 1d4+4
        - effect: energy drain
      attack: slam
      bonus:
      - 15
  ranged:
  - - text: mwk light crossbow +12 (1d8/19-20)
      entries:
      - - damage: 1d8
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 12
  special:
  - blood drain
  - children of the night (ghouls or shadows)
  - create spawn
  - dominate (DC 17)
  - energy drain (2 levels, DC 17)
  - mythic power (4/day, surge +1d8)
  - negative energy focus
  - scabrous claws
  - weapon training (heavy blades +1)
ability_scores:
  STR: 26
  DEX: 18
  CON:
  INT: 14
  WIS: 10
  CHA: 19
BAB: 7
CMB: 15
CMD: 31
feats:
- is_bonus: true
  name: Alertness
- is_bonus: true
  name: Combat Reflexes
- name: Deceitful
- is_mythic: true
  name: Disruptive
- is_bonus: true
  name: Dodge
- name: Greater Weapon Focus (longsword)
- is_mythic: true
  is_bonus: true
  name: Improved Initiative
- is_bonus: true
  name: Lightning Reflexes
- name: Mobility
- name: Power Attack
- name: Quick Draw
- is_bonus: true
  name: Toughness
- name: Vital Strike
- name: Weapon Focus (longsword)
- name: Weapon Specialization (longsword)
skills:
  Bluff: 21
  Climb: 14
  Disguise: 6
  Intimidate: 14
  Perception: 17
  Ride: 8
  Sense Motive: 17
  Stealth: 15
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
    Sense Motive:
      _: 8
    Stealth:
      _: 8
languages:
- Common
- Draconic
- Undercommon
special_qualities:
- armor training 2
- change shape (dire bat or wolf, beast shape II)
- gaseous form
- overcome weakness (garlic, sunlight)
- shadowless
- spider climb
ecology:
  environment: any
  organization: solitary or family (vampire plus 2-8 spawn)
  treasure_type: NPC Gear
  treasure:
  - potion of inflict serious wounds
  - +1 bolts (10)
  - +1 leather armor
  - +1 longsword
  - mwk light crossbow
  - cloak of resistance +2
  - ring of protection +1
  - other treasure
desc_long: A mythic vampire has ties to the earliest of its kind, being either one
  of the first vampires or the offspring of such ancient creatures.

---

# Vampire
This alluring, raven-haired beauty casually wipes a trickle of blood from a pale cheek, then smiles to reveal needle-sharp fangs.
**Source** Pathfinder RPG Bestiary pg. 270
**XP** 6,400
Female human _[[monsters/Vampire|vampire]]_ _[[classes/Sorcerer|sorcerer]]_ 8
CE Medium undead (augmented humanoid)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +13

##### Defense

**AC** 23, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+2 _[[spells/Deflection|deflection]]_, +4 Dex, +1 _[[feats/Dodge|dodge]]_, +6 natural)
**hp** 102 (8d6+72); _[[universal monster rules/Fast Healing|fast healing]]_ 5
**Fort** +13, **Ref** +11, **Will** +12
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 10/magic and silver; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_; **Resist** cold 10, electricity 10
**Weaknesses** _vampire_ weaknesses

##### Offense
**Speed** 30 ft.
**Melee** slam +8 (1d4+4 plus _[[universal monster rules/Energy Drain|energy drain]]_)
**Special Attacks** _[[universal monster rules/Blood Drain|blood drain]]_, children of the night, create spawn, dominate (DC 22), _energy drain_ (2 levels, DC 22)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th, +7 touch)
11/day—grave touch
**_Sorcerer_ Spells Known **(CL 8th, +8 ranged touch)
4th (5/day)—greater _[[spells/Invisibility|invisibility]]_
3rd (5/day)—_[[spells/Dispel Magic|dispel magic]]_, _[[spells/Fireball|fireball]]_ (DC 21), _[[spells/Vampiric Touch|vampiric touch]]_
2nd (8/day)—_[[spells/False Life|false life]]_, _invisibility_, _[[spells/Scorching Ray|scorching ray]]_, web (DC 20)
1st (8/day)—_[[spells/Burning Hands|burning hands]]_ (DC 19), _[[spells/Chill Touch|chill touch]]_ (DC 19), _[[spells/Disguise Self|disguise self]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Mage Armor|mage armor]]_, _[[spells/Magic Missile|magic missile]]_
0—_[[spells/Acid Splash|acid splash]]_, _[[spells/Detect Magic|detect magic]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _[[spells/Message|message]]_, open/close, _[[spells/Read Magic|read magic]]_
**Bloodline **undead

##### Statistics
**Str** 16, **Dex** 18, **Con** —, **Int** 14, **Wis** 16, **Cha** 26
**Base Atk** +4; **CMB** +7; **CMD** 24
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Blind-Fight|Blind-Fight]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Silent Spell|Silent Spell]]_, _[[feats/Still Spell|Still Spell]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_
**Skills** Bluff +27, Knowledge (arcana) +13, Knowledge (religion) +10, Perception +21, Sense Motive +13, Spellcraft +13, Stealth +12, Use Magic Device +19; **Racial Modifiers** +8 Bluff, +8 Perception, +8 Sense Motive, +8 Stealth
**Languages** Abyssal, Common, Draconic
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (dire bat or _[[monsters/Wolf|wolf]]_, _[[spells/Beast Shape II|beast shape II]]_), _[[spells/Gaseous Form|gaseous form]]_, shadowless, _[[spells/Spider Climb|spider climb]]_

##### Ecology

**Environment** any
**Organization** solitary or family (_vampire_ plus 2–8 spawn)
**Treasure** NPC gear (_[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_)

##### Description

Vampires are undead humanoid creatures that feed on the blood of the living. They look much as they did in life, often becoming more attractive, though some have a hardened, feral look instead.