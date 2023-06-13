---
cssclass: [monsters]
title1: Lich
desc_short: This armored undead human wields a heavy mace and wears the trappings
  of a devil-worshiper.
title2: Mythic Lich
CR: 17
MR: 7
sources:
- name: Mythic Adventures
  page: 206
  link: http://paizo.com/products/btpy8ywe?Pathfinder-Roleplaying-Game-Mythic-Adventures
XP: 102400
race: Human
classes:
- lich cleric of Asmodeus 13
alignment: LE
size: Medium
type: undead
subtypes:
- augmented humanoid
- human
- mythic
initiative:
  bonus: 13
senses:
  darkvision: 60
  spell perception: true
auras:
- name: fear
  radius: 60
  DC: 28
AC:
  AC: 36
  touch: 14
  flat_footed: 34
  components:
    armor: 7
    deflection: 2
    dex: 2
    natural: 15
HP:
  HP: 209
  long: 13d8+147
saves:
  fort: 16
  ref: 9
  will: 21
defensive_abilities:
- channel resistance +8
- creeping paralysis
DR:
- amount: 15
  weakness: bludgeoning and epic and magic
immunities:
- cold
- electricity
- undead traits
SR: 32
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 heavy mace +9/+4 (1d8)
      entries:
      - - damage: 1d8
      attack: +1 heavy mace
      bonus:
      - 9
      - 4
    - text: touch +3 (1d8+6 plus paralyzing touch)
      entries:
      - - damage: 1d8+6
        - effect: paralyzing touch
      attack: touch
      bonus:
      - 3
  special:
  - channel negative energy 10/day (DC 23, 7d6)
  - hand of the acolyte (11/day)
  - inspired spell
  - mythic power (7/day, surge +1d10)
  - mythic spells 2/day
  - paralyzing touch (DC 28)
  - scythe of evil (6 rounds, 2/day)
spell_like_abilities:
  entries:
  - name: touch of evil
    source: default
    freq: 11/day
    other: 6 rounds
  - name: dispelling touch
    source: default
    freq: 2/day
  sources:
  - name: default
    CL: 13
    concentration: 21
spells:
  entries:
  - is_domain_spell: true
    name: blasphemy
    source: Cleric
    level: 7
    DC: 25
  - name: destruction
    source: Cleric
    level: 7
    DC: 27
  - name: ethereal jaunt
    source: Cleric
    level: 7
  - is_domain_spell: true
    name: antimagic field
    source: Cleric
    level: 6
  - is_mythic_spell: true
    name: blade barrier
    source: Cleric
    level: 6
    DC: 24
  - is_mythic_spell: true
    name: harm
    source: Cleric
    level: 6
    count: 2
    DC: 26
  - is_domain_spell: true
    name: dispel good
    source: Cleric
    level: 5
  - is_mythic_spell: true
    name: flame strike
    source: Cleric
    level: 5
    DC: 23
  - name: greater command
    source: Cleric
    level: 5
    DC: 23
  - name: slay living
    source: Cleric
    level: 5
    count: 2
    DC: 25
  - is_mythic_spell: true
    name: chaos hammer
    source: Cleric
    level: 4
    DC: 22
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: poison
    source: Cleric
    level: 4
    DC: 24
  - name: spell immunity
    source: Cleric
    level: 4
  - is_mythic_spell: true
    is_domain_spell: true
    name: unholy blight
    source: Cleric
    level: 4
    count: 2
    DC: 22
  - name: bestow curse
    source: Cleric
    level: 3
    count: 2
    DC: 23
  - is_mythic_spell: true
    name: contagion
    source: Cleric
    level: 3
    DC: 23
  - is_domain_spell: true
    name: dispel magic
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: meld into stone
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: align weapon
    source: Cleric
    level: 2
    other: evil only
  - name: calm emotions
    source: Cleric
    level: 2
    DC: 20
  - name: darkness
    source: Cleric
    level: 2
  - name: desecrate
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 20
  - name: resist energy
    source: Cleric
    level: 2
  - is_mythic_spell: true
    name: spiritual weapon
    source: Cleric
    level: 2
  - name: bane
    source: Cleric
    level: 1
    DC: 19
  - name: cause fear
    source: Cleric
    level: 1
    DC: 21
  - name: deathwatch
    source: Cleric
    level: 1
  - name: entropic shield
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: identify
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
    count: 2
  - name: bleed
    source: Cleric
    level: 0
    DC: 20
  - name: detect magic
    source: Cleric
    level: 0
  - name: purify food and drink
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 13
    concentration: 21
    slots:
      0: at-will
    domains:
    - evil
    - magic
ability_scores:
  STR: 8
  DEX: 14
  CON:
  INT: 15
  WIS: 26
  CHA: 20
BAB: 9
CMB: 8
CMD: 22
feats:
- name: Combat Casting
- name: Craft Wondrous Item
- name: Extra Channel
- is_mythic: true
  name: Improved Channel
- is_mythic: true
  name: Improved Initiative
- name: Iron Will
- is_bonus: true
  name: Mythic Spell Lore
- is_mythic: true
  name: Spell Focus (necromancy)
- is_mythic: true
  name: Toughness
skills:
  Heal: 16
  Intimidate: 18
  Knowledge (arcana): 18
  Knowledge (religion): 18
  Perception: 29
  Sense Motive: 27
  Spellcraft: 26
  Stealth: 9
  _racial_mods:
    Perception:
      _: 8
    Sense Motive:
      _: 8
    Spellcraft:
      _: 8
    Stealth:
      _: 8
languages:
- Abyssal
- Common
special_qualities:
- mythic phylactery
- rejuvenation
ecology:
  environment: any
  organization: solitary
  treasure_type: NPC Gear
  treasure:
  - potions of invisibility [2]
  - +3 chain shirt
  - +1 heavy mace
  - amulet of natural armor +3
  - belt of incredible dexterity +2
  - cloak of resistance +3
  - headband of mental prowess +4 [Wis, Cha]
  - ring of protection +2
  - other treasure
desc_long: A mythic lich is an undead spellcaster who gave up standard mythic path
  abilities in favor of abilities that preserve her existence and enhance her unnatural
  power.

---

# Lich
Once fine robes hang in tatters from this withered corpse’s frame. A pale blue light shines from where its eyes should be.
**Source** Pathfinder RPG Bestiary pg. 188
**XP** 19,200
Human _[[monsters/Lich|lich]]_ necromancer 11

NE Medium undead (augmented humanoid)
**Init** +2; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., life sight; Perception +24
**Aura** _[[universal monster rules/Fear|fear]]_ (60-ft. radius, DC 18)

##### Defense

**AC** 23, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+4 armor, +2 _[[spells/Deflection|deflection]]_, +2 Dex, +5 natural)
**hp** 111 (11d6+55 plus 15 _[[spells/False Life|false life]]_)
**Fort** +6, **Ref** +7, **Will** +11
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 15/bludgeoning and magic; **Immune** cold, electricity, _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** touch +5 (1d8+5 plus paralyzing touch)
**Special Attacks** grave touch (9/day), paralyzing touch (DC 18), power over undead (9/day, DC 18)
**Spells Prepared **(CL 11th)
6th—_[[spells/Circle Of Death|circle of death]]_ (DC 22), _[[spells/Globe Of Invulnerability|globe of invulnerability]]_, maximized _[[spells/Fireball|fireball]]_ (DC 19)
5th—_[[spells/Cloudkill|cloudkill]]_ (DC 21), _[[spells/Cone of Cold|cone of cold]]_ (DC 21), quickened _[[spells/Magic Missile|magic missile]]_, _[[spells/Waves of Fatigue|waves of fatigue]]_
4th—_[[spells/Dimension Door|dimension door]]_, _[[spells/Enervation|enervation]]_, _[[spells/Fire Shield|fire shield]]_, _[[spells/Wall Of Ice|wall of ice]]_ (2)
3rd—_[[spells/Dispel Magic|dispel magic]]_ (2), _fireball_ (DC 19), _[[spells/Suggestion|suggestion]]_ (DC 19), _[[spells/Vampiric Touch|vampiric touch]]_ (2)
2nd—_[[spells/Darkness|darkness]]_, extended _[[spells/Mage Armor|mage armor]]_ (already cast), _false life_ (already cast), _[[spells/Scorching Ray|scorching ray]]_ (2), _[[spells/See Invisibility|see invisibility]]_, _[[spells/Spectral Hand|spectral hand]]_
1st—_magic missile_ (3), _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (2), _[[spells/Shield|shield]]_ (2)
0—_[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_
**Opposition Schools **illusion, transmutation

##### Statistics
**Str** 10, **Dex** 14, **Con** —, **Int** 22, **Wis** 14, **Cha** 16
**Base Atk** +5; **CMB** +5; **CMD** 25
**Feats** _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Defensive Combat Training|Defensive Combat Training]]_, _[[feats/Extend Spell|Extend Spell]]_, _[[feats/Improved Lightning Reflexes|Improved Lightning Reflexes]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Maximize Spell|Maximize Spell]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Scribe Scroll|Scribe Scroll]]_, _[[feats/Toughness|Toughness]]_
**Skills** Craft (alchemy) +20, Intimidate +17, Knowledge (arcana) +20, Knowledge (planes) +20, Linguistics +20, Perception +24, Sense Motive +24, Spellcraft +20, Stealth +24; **Racial Modifiers** +8 Perception, +8 Sense Motive, +8 Stealth
**Languages** Abyssal, Aklo, Aquan, Celestial, Common, Draconic, Dwarven, Elven, Giant, Gnome, _[[monsters/Goblin|Goblin]]_, Ignan, Infernal, _[[monsters/Orc|Orc]]_, Undercommon

##### Ecology

**Environment** any
**Organization** solitary
**Treasure** NPC gear (_[[items/Wondrous Item/Boots of Levitation|boots of levitation]]_, _[[items/Wondrous Item/Headband of Vast Intelligence +2|headband of vast intelligence +2]]_ [Perception], _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, potion of _[[spells/Invisibility|invisibility]]_, scroll of _[[spells/Dominate Person|dominate person]]_, scroll of teleport)

##### Description

Few creatures are more feared than the _lich_. The pinnacle of necromantic art, the _lich_ is a spellcaster who has chosen to shed his life as a method to cheat death by becoming undead. While many who reach such heights of power stop at nothing to achieve immortality, the idea of becoming a _lich_ is abhorrent to most creatures. The process involves the extraction of the spellcaster’s life-force and its _[[spells/Imprisonment|imprisonment]]_ in a specially prepared phylactery—the spellcaster gives up life, but in trapping life he also traps his death, and as long as his phylactery remains intact he can continue on in his research and work without _fear_ of the passage of time.

The quest to become a _lich_ is a lengthy one. While construction of the magical phylactery to contain the spellcaster’s soul is a critical component, a prospective _lich_ must also learn the secrets of transferring his soul into the receptacle and of preparing his body for the _[[spells/Transformation|transformation]]_ into undeath, neither of which are simple tasks. Further complicating the ritual is the fact that no two bodies or souls are exactly alike—a ritual that works for one spellcaster might simply kill another or drive him insane. The exact methods for each spellcaster’s _transformation_ are left to the GM’s discretion, but should involve expenditures of hundreds of thousands of gold pieces, numerous _[[items/Weapon Magic Abilities/Deadly|deadly]]_ adventures, and a large number of difficult skill checks over the course of months, years, or decades.