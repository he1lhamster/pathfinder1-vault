---
cssclass: [monsters]
title1: Shadow Cleric
title2: Shadow Cleric
CR: 17
sources:
- name: NPC Codex
  page: 59
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 102400
race: Elf
classes:
- cleric of Norgorber 18
alignment: NE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 26
  touch: 17
  flat_footed: 22
  components:
    armor: 7
    deflection: 3
    dex: 3
    dodge: 1
    natural: 2
HP:
  HP: 129
  long: 18d8+45
saves:
  fort: 17
  ref: 13
  will: 21
  other: +2 vs. enchantments
immunities:
- sleep
speeds:
  base: 30
attacks:
  melee:
  - - text: +4 short sword +21/+16/+11 (1d6+5/17-20)
      entries:
      - - damage: 1d6+5
          crit_range: 17-20
      attack: +4 short sword
      bonus:
      - 21
      - 16
      - 11
  ranged:
  - - text: +4 seeking light crossbow +20/+15/+10 (1d8+4/19-20)
      entries:
      - - damage: 1d8+4
          crit_range: 19-20
      attack: +4 seeking light crossbow
      bonus:
      - 20
      - 15
      - 10
  special:
  - channel negative energy 2/day (DC 18, 9d6)
spell_like_abilities:
  entries:
  - name: bleeding touch
    source: default
    freq: 9/day
    other: 9 rounds
  - name: copycat
    source: default
    freq: 9/day
    other: 18 rounds
  - name: master's illusion
    source: default
    freq: At will
    other: 18 rounds/day
    DC: 27
  sources:
  - name: default
    CL: 18
    concentration: 24
spells:
  entries:
  - name: energy drain
    source: Cleric
    level: 9
    DC: 25
  - name: implosion
    source: Cleric
    level: 9
    DC: 25
  - is_domain_spell: true
    name: time stop
    source: Cleric
    level: 9
  - name: antimagic field
    source: Cleric
    level: 8
  - name: discern location
    source: Cleric
    level: 8
  - name: greater spell immunity
    source: Cleric
    level: 8
  - is_domain_spell: true
    name: mass invisibility
    source: Cleric
    level: 8
  - name: blasphemy
    source: Cleric
    level: 7
    count: 2
    DC: 23
  - name: ethereal jaunt
    source: Cleric
    level: 7
  - is_domain_spell: true
    name: screen
    source: Cleric
    level: 7
  - name: blade barrier
    source: Cleric
    level: 6
    DC: 22
  - name: harm
    source: Cleric
    level: 6
    DC: 22
  - name: heal
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: mislead
    source: Cleric
    level: 6
  - name: wind walk
    source: Cleric
    level: 6
  - name: word of recall
    source: Cleric
    level: 6
  - name: dispel good
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: false vision
    source: Cleric
    level: 5
  - name: insect plague
    source: Cleric
    level: 5
  - name: slay living
    source: Cleric
    level: 5
    count: 2
    DC: 21
  - name: spell resistance
    source: Cleric
    level: 5
  - is_domain_spell: true
    name: confusion
    source: Cleric
    level: 4
    DC: 20
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - name: greater magic weapon
    source: Cleric
    level: 4
    count: 2
  - name: neutralize poison
    source: Cleric
    level: 4
  - name: deeper darkness
    source: Cleric
    level: 3
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: magic vestment
    source: Cleric
    level: 3
  - name: meld with stone
    source: Cleric
    level: 3
  - name: poison
    source: Cleric
    level: 3
    DC: 19
  - is_domain_spell: true
    name: nondetection
    source: Cleric
    level: 3
  - name: darkness
    source: Cleric
    level: 2
  - name: delay poison
    source: Cleric
    level: 2
    DC: 18
  - name: hold person
    source: Cleric
    level: 2
    DC: 18
  - is_domain_spell: true
    name: invisibility
    source: Cleric
    level: 2
  - name: silence
    source: Cleric
    level: 2
    count: 2
    DC: 18
  - name: undetectable alignment
    source: Cleric
    level: 2
  - name: cause fear
    source: Cleric
    level: 1
    DC: 17
  - name: comprehend languages
    source: Cleric
    level: 1
  - is_domain_spell: true
    name: disguise self
    source: Cleric
    level: 1
  - name: divine favor
    source: Cleric
    level: 1
  - name: entropic shield
    source: Cleric
    level: 1
  - name: obscuring mist
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
    DC: 16
  - name: detect magic
    source: Cleric
    level: 0
  - name: detect poison
    source: Cleric
    level: 0
  - name: mending
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 18
    concentration: 24
    slots:
      0: at-will
    domains:
    - death
    - trickery
tactics:
  Before Combat: The cleric casts delay poison, greater magic weapon (on her sword
    and crossbow), freedom of movement, greater spell immunity, magic vestment, and
    undetectable alignment.
  During Combat: The cleric uses magic to turn invisible or hinder vision, then makes
    hit-and-run attacks.
  Base Statistics: Without greater magic weapon and magic vestment, the cleric's statistics
    are AC 23, touch 17, flat-footed 19; Melee +1 short sword +18/+13/+8 (1d6+2/17-20);
    Ranged +1 seeking light crossbow +17/+12/+7 (1d8+1/19-20).
ability_scores:
  STR: 12
  DEX: 16
  CON: 14
  INT: 12
  WIS: 22
  CHA: 8
BAB: 13
CMB: 14
CMD: 31
feats:
- name: Combat Casting
- name: Combat Reflexes
- name: Deadly Aim
- name: Dodge
- name: Improved Critical (short sword)
- name: Rapid Reload
- name: Vital Strike
- name: Weapon Finesse
- name: Weapon Focus (short sword)
skills:
  Bluff: 11
  Diplomacy: 11
  Disguise: 11
  Knowledge (religion): 13
  Perception: 8
  Sense Motive: 18
  Stealth: 24
languages:
- Common
- Elven
- Orc
special_qualities:
- aura
- death's embrace
- elven magic
- weapon familiarity
gear:
  combat:
  - wand of invisibility (10 charges)
  other:
  - +1 seeking light crossbow with 20 bolts
  - +1 shadow studded leather
  - +1 short sword
  - amulet of natural armor +2
  - belt of mighty constitution +2
  - boots of speed
  - cloak of resistance +4
  - headband of inspired wisdom +4
  - ring of protection +3
  - wooden unholy symbol
  - eye ointment for true seeing (worth 250 gp)
  - 4,254 gp
desc_long: A shadow cleric strikes like death from the darkness.

---

# Shadow Cleric

**Source** NPC Codex pg. 59
**XP** 102,400
Elf _[[classes/Cleric|cleric]]_ of Norgorber 18

NE Medium humanoid (elf)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +8

##### Defense

**AC** 26, touch 17, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+7 armor, +3 _[[spells/Deflection|deflection]]_, +3 Dex, +1 _[[feats/Dodge|dodge]]_, +2 natural)
**hp** 129 (18d8+45)
**Fort** +17, **Ref** +13, **Will** +21; +2 vs. enchantments
**Immune** sleep

##### Offense
**Speed** 30 ft.
**Melee** +4 _[[items/Weapon/Short sword|short sword]]_ +21/+16/+11 (1d6+5/17–20)
**Ranged** +4 seeking _[[items/Weapon/Light crossbow|light crossbow]]_ +20/+15/+10 (1d8+4/19–20)
**Special Attacks** channel negative energy 2/day (DC 18, 9d6)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +24)
9/day—bleeding touch (9 rounds), copycat (18 rounds)
At will—master’s illusion (18 rounds/day, DC 27)
**_Cleric_ Spells Prepared **(CL 18th; concentration +24)
9th—_[[universal monster rules/Energy Drain|energy drain]]_ (DC 25), _[[spells/Implosion|implosion]]_ (DC 25), _[[spells/Time Stop|time stop]]_
8th—_[[spells/Antimagic Field|antimagic field]]_, _[[spells/Discern Location|discern location]]_, greater _[[spells/Spell Immunity|spell immunity]]_, mass _[[spells/Invisibility|invisibility]]_
7th—_[[spells/Blasphemy|blasphemy]]_ (2, DC 23), _[[spells/Ethereal Jaunt|ethereal jaunt]]_, screen
6th—_[[spells/Blade Barrier|blade barrier]]_ (DC 22), _[[spells/Harm|harm]]_ (DC 22), _[[spells/Heal|heal]]_, _[[spells/Mislead|mislead]]_, _[[spells/Wind Walk|wind walk]]_, _[[spells/Word of Recall|word of recall]]_
5th—_[[spells/Dispel Good|dispel good]]_, _[[spells/False Vision|false vision]]_, _[[spells/Insect Plague|insect plague]]_, _[[spells/Slay Living|slay living]]_ (2, DC 21), _[[universal monster rules/Spell Resistance|spell resistance]]_
4th—_[[spells/Confusion|confusion]]_ (DC 20), _[[spells/Divine Power|divine power]]_, _[[spells/Freedom of Movement|freedom of movement]]_, greater _[[spells/Magic Weapon|magic weapon]]_ (2), _[[spells/Neutralize Poison|neutralize poison]]_
3rd—_[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Magic Vestment|magic vestment]]_, meld with stone, poison (DC 19), _[[spells/Nondetection|nondetection]]_
2nd—_[[spells/Darkness|darkness]]_, _[[spells/Delay Poison|delay poison]]_ (DC 18), _[[spells/Hold Person|hold person]]_ (DC 18), _invisibility_, _[[spells/Silence|silence]]_ (2, DC 18), _[[spells/Undetectable Alignment|undetectable alignment]]_
1st—_[[spells/Cause Fear|cause fear]]_ (DC 17), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Disguise Self|disguise self]]_, _[[spells/Divine Favor|divine favor]]_, _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Obscuring Mist|obscuring mist]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Mending|mending]]_
**D **Domain spell; **Domains **Death, Trickery

### Tactics

**Before Combat **The _cleric_ casts _delay poison_, greater _magic weapon_ (on her sword and crossbow), _freedom of movement_, greater _spell immunity_, _magic vestment_, and _undetectable alignment_.
**During Combat **The _cleric_ uses magic to turn _[[conditions/Invisible|invisible]]_ or _[[feats/Hinder|hinder]]_ _[[spells/Vision|vision]]_, then makes hit-and-run attacks.
**Base Statistics **Without greater _magic weapon_ and _magic vestment_, the _cleric_'s statistics are **AC **23, touch 17, _flat-footed_ 19; **Melee** +1 _short sword_ +18/+13/+8 (1d6+2/17–20); **Ranged **+1 seeking _light crossbow_ +17/+12/+7 (1d8+1/19–20).

##### Statistics
**Str** 12, **Dex** 16, **Con** 14, **Int** 12, **Wis** 22, **Cha** 8
**Base Atk** +13; **CMB** +14; **CMD** 31
**Feats** _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Deadly Aim|Deadly Aim]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (_short sword_), _[[feats/Rapid Reload|Rapid Reload]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_short sword_)
**Skills** Bluff +11, Diplomacy +11, Disguise +11, Knowledge (religion) +13, Perception +8, Sense Motive +18, Stealth +24
**Languages** Common, Elven, _[[monsters/Orc|Orc]]_
**SQ** aura, death’s embrace, elven magic, weapon familiarity
**Combat Gear** wand of _invisibility_ (10 charges); **Other Gear** +1 seeking _light crossbow_ with 20 bolts, +1 _[[items/Armor Magic Abilities/Shadow|shadow]]_ studded leather, +1 _short sword_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Mighty Constitution +2|belt of mighty constitution +2]]_, _[[items/Wondrous Item/Boots of Speed|boots of speed]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +4|cloak of _resistance_ +4]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +4|headband of _inspired_ wisdom +4]]_, _[[items/Ring/Ring of Protection +3|ring of protection +3]]_, wooden _[[items/Weapon Magic Abilities/Unholy|unholy]]_ symbol, eye ointment for _[[spells/True Seeing|true seeing]]_ (worth 250 gp), 4,254 gp

A _[[npcs/Shadow Cleric|shadow cleric]]_ strikes like death from the _darkness_.