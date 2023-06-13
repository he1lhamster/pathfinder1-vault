---
cssclass: [monsters]
title1: Couatl, Xiuh Couatl
desc_short: Wreathed in flame, this winged serpent sports brightly colored feathers
  sparking with electricity.
title2: Xiuh Couatl
CR: 12
sources:
- name: 'Pathfinder #106: For Queen and Empire'
  page: 86
  link: http://paizo.com/products/btpy9l3b?Pathfinder-Adventure-Path-106-For-Queen-Empire
XP: 19200
alignment: NG
size: Large
type: outsider
subtypes:
- native
initiative:
  bonus: 9
senses:
  detect chaos/evil/good/law: true
  darkvision: 60
  thoughtsense: 60
AC:
  AC: 29
  touch: 14
  flat_footed: 24
  components:
    dex: 5
    natural: 15
    size: -1
HP:
  HP: 157
  long: 15d10+75
saves:
  fort: 14
  ref: 10
  will: 16
immunities:
- electricity
- fire
SR: 23
speeds:
  base: 30
  fly: 80
  fly_maneuverability: average
attacks:
  melee:
  - - text: bite +22 (2d6+12 plus burn, grab, and poison)
      entries:
      - - damage: 2d6+12
        - effect: burn
        - effect: grab
        - effect: poison
      attack: bite
      bonus:
      - 22
  special:
  - breath weapon (60-ft. line, 6d6 fire and 6d6 electricity, Reflex DC 22 half, usable
    every 1d6 rounds)
  - burn (1d6 fire, DC 22)
  - constrict (2d6+12)
  - poison
space: 10
reach: 10
spell_like_abilities:
  entries:
  - name: detect chaos/evil/good/law
    source: default
    freq: Constant
  - name: detect thoughts
    source: default
    freq: At will
    DC: 18
  - name: invisibility
    source: default
    freq: At will
  - name: plane shift
    source: default
    freq: At will
    DC: 23
  - name: atonement
    source: default
    freq: 1/week
  sources:
  - name: default
    CL: 15
    concentration: 21
spells:
  entries:
  - name: greater arcane sight
    source: Psychic
    level: 7
  - name: vision
    source: Psychic
    level: 7
  - name: greater dispel magic
    source: Psychic
    level: 6
  - name: legend lore
    source: Psychic
    level: 6
  - name: veil
    source: Psychic
    level: 6
    DC: 22
  - name: commune with nature
    source: Psychic
    level: 5
  - name: mind thrust V
    source: Psychic
    level: 5
    DC: 21
  - name: psychic crush I
    source: Psychic
    level: 5
    DC: 21
  - name: wall of force
    source: Psychic
    level: 5
  - name: divination
    source: Psychic
    level: 4
  - name: dream
    source: Psychic
    level: 4
  - name: locate creature
    source: Psychic
    level: 4
  - name: sending
    source: Psychic
    level: 4
  - name: clairaudience/clairvoyance
    source: Psychic
    level: 3
  - name: deep slumber
    source: Psychic
    level: 3
    DC: 20
  - name: dispel magic
    source: Psychic
    level: 3
  - name: haste
    source: Psychic
    level: 3
  - name: anticipate thoughts
    source: Psychic
    level: 2
    DC: 18
  - name: augury
    source: Psychic
    level: 2
  - name: aversion
    source: Psychic
    level: 2
    DC: 18
  - name: demand offering
    source: Psychic
    level: 2
    DC: 18
  - name: scare
    source: Psychic
    level: 2
    DC: 19
  - name: anticipate peril
    source: Psychic
    level: 1
    DC: 17
  - name: charm person
    source: Psychic
    level: 1
    DC: 18
  - name: forbid action
    source: Psychic
    level: 1
    DC: 18
  - name: mindlink
    source: Psychic
    level: 1
  - name: sleep
    source: Psychic
    level: 1
    DC: 18
  - name: bleed
    source: Psychic
    level: 0
    DC: 17
  - name: detect magic
    source: Psychic
    level: 0
  - name: detect poison
    source: Psychic
    level: 0
  - name: ghost sound
    source: Psychic
    level: 0
    DC: 17
  - name: know direction
    source: Psychic
    level: 0
  - name: light
    source: Psychic
    level: 0
  - name: mage hand
    source: Psychic
    level: 0
  - name: read magic
    source: Psychic
    level: 0
  - name: stabilize
    source: Psychic
    level: 0
  sources:
  - name: Psychic
    type: known
    CL: 15
    concentration: 21
    slots:
      7: 4
      6: 7
      5: 7
      4: 7
      3: 7
      2: 8
      1: 8
      0: at-will
ability_scores:
  STR: 26
  DEX: 20
  CON: 20
  INT: 23
  WIS: 25
  CHA: 23
BAB: 15
CMB: 24
CMB_other: +28 grapple
CMD: 39
CMD_other: can't be tripped
feats:
- name: Alertness
- name: Flyby Attack
- name: Hover
- name: Improved Initiative
- name: Persuasive
- name: Power Attack
- name: Quicken Spell
- name: Wingover
skills:
  Acrobatics: 20
  Diplomacy: 28
  Fly: 21
  Intimidate: 8
  Knowledge (arcana): 13
  Knowledge (geography): 14
  Knowledge (history): 24
  Knowledge (local): 24
  Knowledge (religion): 24
  Perception: 29
  Sense Motive: 29
  Spellcraft: 21
  Survival: 22
  Use Magic Device: 21
languages:
- Celestial
- Common
- Draconic
- telepathy 100 ft.
special_qualities:
- instrument of retribution
ecology:
  environment: any mountain
  organization: solitary or pair
  treasure_type: standard
special_abilities:
  Instrument of Retribution (Su): As a full-round action, a xiuh couatl can transform
    into any simple or martial weapon. The weapon is always a +2 flaming shock weapon
    and can be sized for any creature. The xiuh couatl is limited to only light or
    one-handed weapons if sized for a Gargantuan creature or light weapons if sized
    for a Colossal creature. In weapon form, the xiuh couatl gains hardness equal
    to that of a weapon of its type and retains its type, senses, hit points, saving
    throws, and telepathy. A xiuh couatl can return to its normal form as an immediate
    action.
  Poison (Ex): Bite-injury; save Fort DC 22; frequency 1/minute for 10 minutes; effect
    1d6 Str; cure 2 consecutive saves.
  Psychic Spells: A xiuh couatl casts spells as a 15th-level psychic (Pathfinder RPG
    Occult Adventures 60).
desc_long: Xiuh couatls are a fierce variety of couatl commonly associated with vengeance
  and retribution. They seek out vile creatures, offering one final opportunity at
  redemption. Those who do not accept this offer or cannot be redeemed face the xiuh
  couatl's fearsome and absolute punishment. In cases where its might alone is not
  enough, a xiuh couatl offers its assistance to a powerful, righteous figure to mete
  out justice on its behalf. The winged serpents glow with an intense plume of flames,
  draped in arcing electricity. Their feathers range in color from bright crimson
  to deep violet, encompassing the shades of the setting sun. A typical xiuh couatl
  is 20 feet long with a wingspan of 25 feet. It weighs 4,500 pounds.

---

# Couatl, Xiuh Couatl
Wreathed in flame, this winged serpent sports brightly colored feathers sparking with electricity.
**Source** Pathfinder #106: For Queen and Empire pg. 86
**XP** 19,200

NG Large outsider (native)
**Init** +9; **Senses** detect chaos/evil/good/law, _[[spells/Darkvision|darkvision]]_ 60 ft., _[[universal monster rules/Thoughtsense|thoughtsense]]_ 60 ft.; Perception +29

##### Defense

**AC** 29, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+5 Dex, +15 natural, –1 size)
**hp** 157 (15d10+75)
**Fort** +14, **Ref** +10, **Will** +16
**Immune** electricity, fire; **SR** 23

##### Offense
**Speed** 30 ft., fly 80 ft. (average)
**Melee** bite +22 (2d6+12 plus _[[universal monster rules/Burn|burn]]_, _[[universal monster rules/Grab|grab]]_, and poison)
**Space** 10 ft., **Reach** 10 ft.
**Special Attacks** _[[universal monster rules/Breath Weapon|breath weapon]]_ (60-ft. line, 6d6 fire and 6d6 electricity, Reflex DC 22 half, usable every 1d6 rounds), _burn_ (1d6 fire, DC 22), _[[universal monster rules/Constrict|constrict]]_ (2d6+12), poison
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 15th; concentration +21)
Constant—detect chaos/evil/good/law
At will—_[[spells/Detect Thoughts|detect thoughts]]_ (DC 18), _[[spells/Invisibility|invisibility]]_, _[[spells/Plane Shift|plane shift]]_ (DC 23)
1/week—_[[spells/Atonement|atonement]]_
**_[[classes/Psychic|Psychic]]_ Spells Known **(CL 15th; concentration +21)
7th (4/day)—greater _[[spells/Arcane Sight|arcane sight]]_, _[[spells/Vision|vision]]_
6th (7/day)—greater _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Legend Lore|legend lore]]_, _[[spells/Veil|veil]]_ (DC 22)
5th (7/day)—_[[spells/Commune with Nature|commune with nature]]_, _[[spells/Mind Thrust V|mind thrust V]]_ (DC 21), _[[spells/Psychic Crush I|psychic crush I]]_ (DC 21), _[[spells/Wall Of Force|wall of force]]_
4th (7/day)—_[[spells/Divination|divination]]_, _[[spells/Dream|dream]]_, _[[spells/Locate Creature|locate creature]]_, _[[spells/Sending|sending]]_
3rd (7/day)—clairaudience/clairvoyance, _[[spells/Deep Slumber|deep slumber]]_ (DC 20), _dispel magic_, _[[spells/Haste|haste]]_
2nd (8/day)—_[[spells/Anticipate Thoughts|anticipate thoughts]]_ (DC 18), _[[spells/Augury|augury]]_, _[[spells/Aversion|aversion]]_ (DC 18), _[[spells/Demand Offering|demand offering]]_ (DC 18), _[[spells/Scare|scare]]_ (DC 19)
1st (8/day)—_[[spells/Anticipate Peril|anticipate peril]]_ (DC 17), _[[spells/Charm Person|charm person]]_ (DC 18), _[[spells/Forbid Action|forbid action]]_ (DC 18), _[[spells/Mindlink|mindlink]]_, sleep (DC 18)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 17), _[[spells/Detect Magic|detect magic]]_, _[[spells/Detect Poison|detect poison]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 17), _[[spells/Know Direction|know direction]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_, stabilize

##### Statistics
**Str** 26, **Dex** 20, **Con** 20, **Int** 23, **Wis** 25, **Cha** 23
**Base Atk** +15; **CMB** +24 (+28 grapple); **CMD** 39 (can’t be tripped)
**Feats** _[[feats/Alertness|Alertness]]_, _[[feats/Flyby Attack|Flyby Attack]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Persuasive|Persuasive]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Wingover|Wingover]]_
**Skills** Acrobatics +20, Diplomacy +28, Fly +21, Intimidate +8, Knowledge (arcana) +13, Knowledge (geography) +14, Knowledge (history) +24, Knowledge (local) +24, Knowledge (religion) +24, Perception +29, Sense Motive +29, Spellcraft +21, Survival +22, Use Magic Device +21
**Languages** Celestial, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** instrument of _[[spells/Retribution|retribution]]_

##### Ecology

**Environment** any mountain
**Organization** solitary or pair
**Treasure** standard

### Special Abilities

**Instrument of _Retribution_ (Su)** As a full-round action, a xiuh _[[monsters/Couatl|couatl]]_ can transform into any simple or martial weapon. The weapon is always a +2 _[[items/Weapon Magic Abilities/Flaming|flaming]]_ _[[items/Weapon Magic Abilities/Shock|shock]]_ weapon and can be sized for any creature. The xiuh _couatl_ is limited to only light or one-handed weapons if sized for a Gargantuan creature or light weapons if sized for a Colossal creature. In weapon form, the xiuh _couatl_ gains hardness equal to that of a weapon of its type and retains its type, senses, hit points, saving throws, and _telepathy_. A xiuh _couatl_ can return to its normal form as an immediate action.

**Poison (Ex)** Bite—injury; save Fort DC 22; frequency 1/minute for 10 minutes; effect 1d6 Str; cure 2 consecutive saves.

**_Psychic_ Spells** A xiuh _couatl_ casts spells as a 15th-level _psychic_ (Pathfinder RPG Occult Adventures 60).

##### Description

Xiuh couatls are a fierce variety of _couatl_ commonly associated with _[[feats/Vengeance|vengeance]]_ and _retribution_. They seek out vile creatures, offering one final opportunity at _[[feats/Redemption|redemption]]_. Those who do not accept this offer or cannot be _[[items/Weapon Magic Abilities/Redeemed|redeemed]]_ face the xiuh _couatl_’s fearsome and absolute punishment. In cases where its might alone is not enough, a xiuh _couatl_ offers its assistance to a powerful, _[[items/Armor Magic Abilities/Righteous|righteous]]_ figure to mete out justice on its behalf. The winged serpents glow with an intense plume of flames, draped in arcing electricity. Their feathers range in color from bright crimson to deep violet, encompassing the _[[spells/Shades|shades]]_ of the setting sun. A typical xiuh _couatl_ is 20 feet long with a wingspan of 25 feet. It weighs 4,500 pounds.