---
cssclass: [monsters]
title1: Lich, Forsaken Lich
desc_short: This horribly withered creature moves in jerks and twitches as if constantly
  wracked with pain. Waves of shadow undulate through the creature's body, emerging
  like appendages from just beneath its dry, stretched skin.
title2: Forsaken Lich
CR: 12
sources:
- name: 'Pathfinder #48: Shadows of Gallowspire'
  page: 82
  link: http://paizo.com/store/games/roleplayingGames/p/pathfinderRPG/paizo/pathfinderAdventurePath/carrionCrown/v5748btpy8mgb
XP: 19200
race: Human
classes:
- lich cleric of Urgathoa 11
alignment: NE
size: Medium
type: undead
subtypes:
- augmented humanoid
initiative:
  bonus: 0
senses:
  darkvision: 60
auras:
- name: delusory aura
  radius: 100
AC:
  AC: 21
  touch: 11
  flat_footed: 21
  components:
    armor: 7
    deflection: 1
    natural: 3
HP:
  HP: 97
  long: 11d8+44
saves:
  fort: 7
  ref: 3
  will: 12
defensive_abilities:
- channel resistance +4
- soul shield
- spell storm
DR:
- amount: 15
  weakness: bludgeoning and magic
immunities:
- cold
- electricity
- undead traits
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 scythe +15/+10 (2d4+8/19-20/×4)
      entries:
      - - damage: 2d4+8
          crit_range: 19-20
          crit_multiplier: 4
      attack: +1 scythe
      bonus:
      - 15
      - 10
  special:
  - channel negative energy 9/day (DC 19, 6d6)
  - disembodied strike (1d8+5); hand of the acolyte (8/day)
  - soul lash (DC 19; 5d6)
spells:
  entries:
  - name: antilife shell
    source: Cleric
    level: 6
  - is_domain_spell: true
    name: create undead
    source: Cleric
    level: 6
  - name: flame strike
    source: Cleric
    level: 5
    DC: 20
  - is_domain_spell: true
    name: slay living
    source: Cleric
    level: 5
  - name: symbol of pain
    source: Cleric
    level: 5
    DC: 20
  - name: unhallow
    source: Cleric
    level: 5
  - name: divine power
    source: Cleric
    level: 4
  - name: freedom of movement
    source: Cleric
    level: 4
  - is_domain_spell: true
    name: imbue with spell ability
    source: Cleric
    level: 4
  - name: spell immunity
    source: Cleric
    level: 4
  - name: unholy blight
    source: Cleric
    level: 4
    DC: 19
  - is_domain_spell: true
    name: animate dead
    source: Cleric
    level: 3
  - name: bestow curse
    source: Cleric
    level: 3
    DC: 18
  - name: dispel magic
    source: Cleric
    level: 3
  - name: glyph of warding
    source: Cleric
    level: 3
    DC: 18
  - name: invisibility purge
    source: Cleric
    level: 3
  - name: protection from energy
    source: Cleric
    level: 3
  - is_domain_spell: true
    name: death knell
    source: Cleric
    level: 2
  - name: desecrate
    source: Cleric
    level: 2
  - name: gentle repose
    source: Cleric
    level: 2
  - name: hold person
    source: Cleric
    level: 2
    DC: 17
  - name: resist energy
    source: Cleric
    level: 2
  - name: silence
    source: Cleric
    level: 2
    DC: 17
  - is_domain_spell: true
    name: cause fear
    source: Cleric
    level: 1
    DC: 16
  - name: command
    source: Cleric
    level: 1
    DC: 16
  - name: entropic shield
    source: Cleric
    level: 1
  - name: deathwatch
    source: Cleric
    level: 1
  - name: doom
    source: Cleric
    level: 1
    DC: 16
  - name: protection from good
    source: Cleric
    level: 1
  - name: shield of faith
    source: Cleric
    level: 1
  - name: bleed
    source: Cleric
    level: 0
  - name: detect magic
    source: Cleric
    level: 0
  - name: guidance
    source: Cleric
    level: 0
  - name: read magic
    source: Cleric
    level: 0
  sources:
  - name: Cleric
    type: prepared
    CL: 11
    concentration: 16
    slots:
      0: at-will
    domains:
    - death
    - magic
ability_scores:
  STR: 20
  DEX: 10
  CON:
  INT: 13
  WIS: 21
  CHA: 18
BAB: 8
CMB: 13
CMD: 24
feats:
- name: Combat Expertise
- name: Craft Wondrous Item
- name: Extra Channel
- name: Improved Critical (scythe)
- name: Improved Trip
- name: Selective Channeling
- name: Weapon Focus (scythe)
skills:
  Knowledge (arcana): 15
  Knowledge (religion): 15
  Perception: 20
  Sense Motive: 19
  Spellcraft: 15
languages:
- Common
- Necril
special_qualities:
- death's embrace
gear:
  gear:
  - +1 breastplate
  - +1 scythe
  - ring of protection +1
desc_long: |-
  The means of attaining lichdom are extremely personal for mortal spellcasters, fraught with misinformation and peril. The smallest miscalculation in the potion of lichdom's formula or most minute flaw in one's phylactery can interrupt the process that infuses one's mortal soul with overwhelming arcane and negative energies. Other times, an inexperienced wizard attempts the transformation, or erroneously consumes a formula produced for another spellcaster, instantly dying from the backlash of potent forces or condemning himself to a terminal but far more terrible end.

  In these sorrowful cases, the process traps the soul of the would-be lich outside a phylactery that will not accept it and a body that has rejected it. The potent arcane forces tampered with by the lich's failed creation also find themselves unleashed but uncontrolled, surrounding the newly formed abomination, empowering it but also slowly consuming its essence.

  This creature, known as a forsaken lich, is granted the undeath it sought in life, but in a terrifyingly temporary fashion. For the miscalculations of its ambitions, the creature's once-vibrant body shrivels and decays like that of a lich, but becomes a lifeless shell manipulated by the malicious soul and unchecked magical storm that envelop it, forces that control the corpse's actions almost like a marionette. Yet this doom is temporary for nearly all who attempt this foul transition. With the soul unbound from the body and both spirit and corpse exposed to destructive arcane tides, both are slowly eroded. After 1d10 days, the forsaken lich's body and soul are both consumed like a lit candle, eventually reduced physically to ashes, and spiritually to nothing-its essence utterly annihilated, scoured from existence for all time.

---

# Lich, Forsaken Lich
This horribly withered creature moves in jerks and twitches as if constantly wracked with pain. Waves of _[[items/Armor Magic Abilities/Shadow|shadow]]_ undulate through the creature’s body, emerging like appendages from just beneath its dry, stretched skin.
**Source** Pathfinder #48: Shadows of Gallowspire pg. 82
**XP** 19,200
Human _[[monsters/Lich|lich]]_ _[[classes/Cleric|cleric]]_ of Urgathoa 11

NE Medium undead (augmented humanoid)
**Init** +0; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +20
**Aura** delusory aura (100 ft.)

##### Defense

**AC** 21, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+7 armor, +1 _[[spells/Deflection|deflection]]_, +3 natural)
**hp** 97 (11d8+44)
**Fort** +7, **Ref** +3, **Will** +12
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +4, soul _[[spells/Shield|shield]]_, spell storm; **DR** 15/bludgeoning and magic; **Immune** cold, electricity, _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Scythe|scythe]]_ +15/+10 (2d4+8/19–20/×4)
**Special Attacks** channel negative energy 9/day (DC 19, 6d6), disembodied strike (1d8+5); hand of the _[[npcs/Acolyte|acolyte]]_ (8/day), soul lash (DC 19; 5d6)
**_Cleric_ Spells Prepared **(CL 11th; concentration +16)
6th—_[[spells/Antilife Shell|antilife shell]]_, _[[spells/Create Undead|create undead]]_
5th—_[[spells/Flame Strike|flame strike]]_ (DC 20), _[[spells/Slay Living|slay living]]_, _[[spells/Symbol of Pain|symbol of pain]]_ (DC 20), _[[spells/Unhallow|unhallow]]_
4th—_[[spells/Divine Power|divine power]]_, _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Imbue with Spell Ability|imbue with spell ability]]_, _[[spells/Spell Immunity|spell immunity]]_, _[[spells/Unholy Blight|unholy blight]]_ (DC 19)
3rd—_[[spells/Animate Dead|animate dead]]_, _[[spells/Bestow Curse|bestow curse]]_ (DC 18), _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Glyph Of Warding|glyph of warding]]_ (DC 18), _[[spells/Invisibility Purge|invisibility purge]]_, _[[spells/Protection from Energy|protection from energy]]_
2nd—_[[spells/Death Knell|death knell]]_, _[[spells/Desecrate|desecrate]]_, _[[spells/Gentle Repose|gentle repose]]_, _[[spells/Hold Person|hold person]]_ (DC 17), _[[spells/Resist Energy|resist energy]]_, _[[spells/Silence|silence]]_ (DC 17)
1st—_[[spells/Cause Fear|cause fear]]_ (DC 16), _[[spells/Command|command]]_ (DC 16), _[[spells/Entropic Shield|entropic shield]]_, _[[spells/Deathwatch|deathwatch]]_, _[[spells/Doom|doom]]_ (DC 16), _[[spells/Protection From Good|protection from good]]_, _[[spells/Shield Of Faith|shield of faith]]_
0 (at will)—_[[universal monster rules/Bleed|bleed]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_
**D** Domain spell; **Domains **Death, Magic

##### Statistics
**Str** 20, **Dex** 10, **Con** —, **Int** 13, **Wis** 21, **Cha** 18
**Base Atk** +8; **CMB** +13; **CMD** 24
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Craft Wondrous Item|Craft Wondrous Item]]_, _[[feats/Extra Channel|Extra Channel]]_, _[[feats/Improved Critical|Improved Critical]]_ (_scythe_), _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Selective Channeling|Selective Channeling]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scythe_)
**Skills** Knowledge (arcana) +15, Knowledge (religion) +15, Perception +16, Sense Motive +19, Spellcraft +15
**Languages** Common, Necril
**SQ** death’s embrace
**Gear** +1 _[[items/Armor/Breastplate|breastplate]]_, +1 _scythe_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_

##### Description

The means of attaining lichdom are extremely personal for mortal spellcasters, fraught with misinformation and peril. The smallest miscalculation in the potion of lichdom's formula or most minute flaw in one's phylactery can interrupt the process that infuses one's mortal soul with overwhelming arcane and negative energies. Other times, an inexperienced _[[classes/Wizard|wizard]]_ attempts the _[[spells/Transformation|transformation]]_, or erroneously consumes a formula produced for another spellcaster, instantly _[[conditions/Dying|dying]]_ from the backlash of _[[items/Weapon Magic Abilities/Potent|potent]]_ forces or condemning himself to a terminal but far more terrible end.

In these sorrowful cases, the process traps the soul of the would-be _lich_ outside a phylactery that will not accept it and a body that has rejected it. The _potent_ arcane forces tampered with by the _lich_'s failed creation also find themselves unleashed but uncontrolled, surrounding the newly formed abomination, empowering it but also slowly consuming its essence.

This creature, known as a forsaken _lich_, is granted the undeath it sought in life, but in a terrifyingly temporary fashion. For the miscalculations of its ambitions, the creature's once-vibrant body shrivels and decays like that of a _lich_, but becomes a lifeless shell manipulated by the malicious soul and unchecked magical storm that envelop it, forces that control the corpse's actions almost like a marionette. Yet this _doom_ is temporary for nearly all who attempt this foul transition. With the soul _[[items/Armor Magic Abilities/Unbound|unbound]]_ from the body and both spirit and corpse exposed to destructive arcane tides, both are slowly eroded. After 1d10 days, the forsaken _lich_'s body and soul are both consumed like a lit _[[items/Mundane/Candle|candle]]_, eventually reduced physically to ashes, and spiritually to nothing—its essence utterly annihilated, scoured from existence for all time.