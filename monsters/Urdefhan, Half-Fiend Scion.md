---
cssclass: [monsters]
title1: Urdefhan, Half-Fiend Scion
desc_short: The scent of death pours from this disheveled woman. Leather straps dotted
  with iron buckles bind her lean form.
title2: Half-Fiend Scion
CR: 15
sources:
- name: Inner Sea Monster Codex
  page: 63
  link: http://paizo.com/products/btpy9elc?Pathfinder-Campaign-Setting-Inner-Sea-Monster-Codex
XP: 51200
race: Half-fiend
classes:
- urdefhan warpriest of Szuriel 12 (Pathfinder RPG Bestiary 171, Pathfinder RPG Bestiary
  2 276, Pathfinder RPG Advanced Class Guide 60)
alignment: NE
size: Medium
type: outsider
subtypes:
- native
initiative:
  bonus: 7
senses:
  darkvision: 120
AC:
  AC: 23
  touch: 12
  flat_footed: 21
  components:
    armor: 8
    dex: 2
    natural: 3
HP:
  HP: 157
  long: 12d8+3d10+87
  HD: 15
saves:
  fort: 15
  ref: 12
  will: 16
defensive_abilities:
- sacred armor (+2, 12 minutes/day)
DR:
- amount: 10
  weakness: magic
- amount: 5
  weakness: good or silver
immunities:
- death effects
- disease
- fear
- level drain
- poison
resistances:
  acid: 10
  cold: 10
  electricity: 10
  fire: 10
SR: 26
speeds:
  base: 20
  fly: 45
  fly_maneuverability: good
attacks:
  melee:
  - - text: +1 vicious rhoka sword +20/+15/+10 (1d10+7/18-20 plus 2d6)
      entries:
      - - damage: 1d10+7
          crit_range: 18-20
        - damage: 2d6
      attack: +1 vicious rhoka sword
      bonus:
      - 20
      - 15
      - 10
    - text: bite +13 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: bite
      bonus:
      - 13
    - text: claw +13 (1d4+3)
      entries:
      - - damage: 1d4+3
      attack: claw
      bonus:
      - 13
  - - text: mwk silver light mace +19/+14/+9 (1d6+6)
      entries:
      - - damage: 1d6+6
      attack: mwk silver light mace
      bonus:
      - 19
      - 14
      - 9
    - text: bite +13 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: bite
      bonus:
      - 13
    - text: claw +13 (1d4+3)
      entries:
      - - damage: 1d4+3
      attack: claw
      bonus:
      - 13
  special:
  - blessings 9/day
  - blood drain (1 Con)
  - channel negative energy 6/day (DC 23, 4d6)
  - fervor 13/day (4d6)
  - sacred weapon (+3 1d10, 12 rounds/day)
  - smite good
  - Strength damage
spell_like_abilities:
  entries:
  - name: feather fall
    source: default
    freq: At will
  - name: align weapon
    source: default
    freq: 3/day
  - name: darkness
    source: default
    freq: 3/day
  - name: death knell
    source: default
    freq: 3/day
    DC: 17
  - name: poison
    source: default
    freq: 3/day
  - name: ray of enfeeblement
    source: default
    freq: 3/day
    DC: 17
  - name: unholy aura
    source: default
    freq: 3/day
  - name: blasphemy
    source: default
    freq: 1/day
  - name: contagion
    source: default
    freq: 1/day
  - name: desecrate
    source: default
    freq: 1/day
  - name: horrid wilting
    source: default
    freq: 1/day
  - name: unhallow
    source: default
    freq: 1/day
  - name: unholy blight
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 3
    concentration: 9
spells:
  entries:
  - name: dismissal
    source: Warpriest
    level: 4
    DC: 21
  - name: divine power
    source: Warpriest
    level: 4
  - name: inflict critical wounds
    source: Warpriest
    level: 4
    DC: 21
  - name: summon monster IV
    source: Warpriest
    level: 4
  - name: bestow curse
    source: Warpriest
    level: 3
    DC: 20
  - name: contagion
    source: Warpriest
    level: 3
    DC: 20
  - name: deeper darkness
    source: Warpriest
    level: 3
  - name: magic circle against good
    source: Warpriest
    level: 3
  - name: protection from energy
    source: Warpriest
    level: 3
  - name: summon monster III
    source: Warpriest
    level: 3
  - name: augury
    source: Warpriest
    level: 2
  - name: bull's strength
    source: Warpriest
    level: 2
  - name: enthrall
    source: Warpriest
    level: 2
    DC: 19
  - name: lesser restoration
    source: Warpriest
    level: 2
  - name: spiritual weapon
    source: Warpriest
    level: 2
  - name: summon monster II
    source: Warpriest
    level: 2
    count: 2
  - name: bless
    source: Warpriest
    level: 1
  - name: cause fear
    source: Warpriest
    level: 1
    DC: 18
  - name: command
    source: Warpriest
    level: 1
    DC: 18
  - name: divine favor
    source: Warpriest
    level: 1
  - name: shield of faith
    source: Warpriest
    level: 1
  - name: summon monster I
    source: Warpriest
    level: 1
    count: 2
  - name: bleed
    source: Warpriest
    level: 0
    DC: 17
  - name: detect magic
    source: Warpriest
    level: 0
  - name: guidance
    source: Warpriest
    level: 0
  - name: read magic
    source: Warpriest
    level: 0
  - name: resistance
    source: Warpriest
    level: 0
  sources:
  - name: Warpriest
    type: prepared
    CL: 12
    concentration: 19
    slots:
      0: at-will
ability_scores:
  STR: 23
  DEX: 16
  CON: 19
  INT: 14
  WIS: 24
  CHA: 22
BAB: 12
CMB: 18
CMD: 31
feats:
- name: Augment Summoning
- name: Combat Casting
- name: Improved Initiative
- name: Improved Vital Strike
- name: Lightning Reflexes
- name: Power Attack
- name: Siphoning Blade
- name: Spell Focus (conjuration)
- name: Step Up
- name: Toughness
- name: Vital Strike
- name: Voracious Blade
- name: Weapon Focus (rhoka sword)
skills:
  Acrobatics: -1
    when jumping: -5
  Bluff: 14
  Fly: 7
  Intimidate: 19
  Knowledge (dungeoneering): 7
  Knowledge (planes): 17
  Knowledge (religion): 17
  Perception: 20
  Sense Motive: 16
  Spellcraft: 16
languages:
- Aklo
- Elven
- Infernal
- Orvian
- Undercommon
special_qualities:
- 'blessings (evil: battle companion, unholy strike; war: battle lust, war mind)'
- daemonic pact
gear:
  combat:
  - potion of barkskin (CL 9th)
  - potion of bear's endurance
  - potion of cat's grace
  - potion of haste
  other:
  - +2 glamered chainmail
  - +1 vicious rhoka sword
  - mwk silver light mace
  - belt of giant strength +2
  - cloak of resistance +3
  - headband of inspired wisdom +2
  - incense of meditation
  - ring of protection +2
  - iron unholy symbol
ecology:
  environment: any land (Abaddon)
desc_long: Urdefhans never forget who created them, and they spend their lives awaiting
  the day they will be destroyed and returned to Abaddon for an eternity of torment.
  Their frequent interactions with daemons occasionally spawns reality-warping half-blood
  children who rise to positions of great power in urdefhan society-if they manage
  to survive.

---

# Urdefhan, Half-Fiend Scion
The _[[universal monster rules/Scent|scent]]_ of death pours from this disheveled woman. Leather straps dotted with iron buckles bind her lean form.
**Source** Inner Sea Monster Codex pg. 63
**XP** 51,200
Half-fiend _[[monsters/Urdefhan|urdefhan]]_ _[[classes/Warpriest|warpriest]]_ of Szuriel 12 (Pathfinder RPG Bestiary 171, Pathfinder RPG Bestiary 2 276, Pathfinder RPG Advanced Class Guide 60)

NE Medium outsider (native)
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +20

##### Defense

**AC** 23, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 21 (+8 armor, +2 Dex, +3 natural)
**hp** 157 (15 HD; 12d8+3d10+87)
**Fort** +15, **Ref** +12, **Will** +16
**Defensive Abilities** _[[items/Weapon Magic Abilities/Sacred|sacred]]_ armor (+2, 12 minutes/day); **DR** 10/magic, 5/good or silver; **Immune** death effects, disease, _[[universal monster rules/Fear|fear]]_, level drain, poison; **Resist** acid 10, cold 10, electricity 10, fire 10; **SR** 26

##### Offense
**Speed** 20 ft., fly 45 ft. (good)
**Melee** +1 _[[items/Weapon Magic Abilities/Vicious|vicious]]_ _[[items/Weapon/Rhoka sword|rhoka sword]]_ +20/+15/+10 (1d10+7/18–20 plus 2d6), bite +13 (1d6+3), claw +13 (1d4+3) or mwk silver _[[items/Weapon/Light mace|light mace]]_ +19/+14/+9 (1d6+6), bite +13 (1d6+3), claw +13 (1d4+3)
**Special Attacks** blessings 9/day, _[[universal monster rules/Blood Drain|blood drain]]_ (1 Con), channel negative energy 6/day (DC 23, 4d6), fervor 13/day (4d6), _sacred_ weapon (+3 1d10, 12 rounds/day), smite good, Strength damage
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd; concentration +9)
At will—_[[spells/Feather Fall|feather fall]]_
3/day—_[[spells/Align Weapon|align weapon]]_, _[[spells/Darkness|darkness]]_, _[[spells/Death Knell|death knell]]_ (DC 17), poison, _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 17), _[[spells/Unholy Aura|unholy aura]]_
1/day—_[[spells/Blasphemy|blasphemy]]_, _[[spells/Contagion|contagion]]_, _[[spells/Desecrate|desecrate]]_, _[[spells/Horrid Wilting|horrid wilting]]_, _[[spells/Unhallow|unhallow]]_, _[[spells/Unholy Blight|unholy blight]]_
**_Warpriest_ Spells Prepared **(CL 12th; concentration +19)
4th—_[[spells/Dismissal|dismissal]]_ (DC 21), _[[spells/Divine Power|divine power]]_, _[[spells/Inflict Critical Wounds|inflict critical wounds]]_ (DC 21), _[[spells/Summon Monster IV|summon monster IV]]_
3rd—_[[spells/Bestow Curse|bestow curse]]_ (DC 20), _contagion_ (DC 20), _[[spells/Deeper Darkness|deeper darkness]]_, _[[spells/Magic Circle against Good|magic circle against good]]_, _[[spells/Protection from Energy|protection from energy]]_, _[[spells/Summon Monster III|summon monster III]]_
2nd—_[[spells/Augury|augury]]_, bull’s strength, _[[spells/Enthrall|enthrall]]_ (DC 19), lesser _[[spells/Restoration|restoration]]_, _[[spells/Spiritual Weapon|spiritual weapon]]_, _[[spells/Summon Monster II|summon monster II]]_ (2)
1st—_[[spells/Bless|bless]]_, _[[spells/Cause Fear|cause fear]]_ (DC 18), _[[spells/Command|command]]_ (DC 18), _[[spells/Divine Favor|divine favor]]_, _[[spells/Shield Of Faith|shield of faith]]_, _[[spells/Summon Monster I|summon monster I]]_ (2)
0 (at will)—_[[universal monster rules/Bleed|bleed]]_ (DC 17), _[[spells/Detect Magic|detect magic]]_, _[[spells/Guidance|guidance]]_, _[[spells/Read Magic|read magic]]_, _[[universal monster rules/Resistance|resistance]]_

##### Statistics
**Str** 23, **Dex** 16, **Con** 19, **Int** 14, **Wis** 24, **Cha** 22
**Base Atk** +12; **CMB** +18; **CMD** 31
**Feats** _[[feats/Augment Summoning|Augment Summoning]]_, _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Siphoning Blade|Siphoning Blade]]_, _[[feats/Spell Focus|Spell Focus]]_ (conjuration), _[[feats/Step Up|Step Up]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Voracious Blade|Voracious Blade]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_rhoka sword_)
**Skills** Acrobatics –1 (–5 when jumping), Bluff +14, Fly +7, Intimidate +19, Knowledge (dungeoneering) +7, Knowledge (planes) +17, Knowledge (religion) +17, Perception +20, Sense Motive +16, Spellcraft +16
**Languages** Aklo, Elven, Infernal, Orvian, Undercommon
**SQ** blessings (evil: battle companion, _[[items/Weapon Magic Abilities/Unholy|unholy]]_ strike; war: battle lust, war mind), daemonic pact
**Combat Gear** potion of _[[spells/Barkskin|barkskin]]_ (CL 9th), potion of bear’s _[[feats/Endurance|endurance]]_, potion of cat’s _[[spells/Grace|grace]]_, potion of _[[spells/Haste|haste]]_; **Other Gear** +2 _[[items/Weapon Magic Abilities/Glamered|glamered]]_ _[[items/Armor/Chainmail|chainmail]]_, +1 _vicious_ _rhoka sword_, mwk silver _light mace_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, _[[items/Wondrous Item/Cloak of _Resistance_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _[[items/Wondrous Item/Incense of Meditation|incense of meditation]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, iron _unholy_ symbol

##### Ecology

**Environment** any land (Abaddon)

##### Description

Urdefhans never forget who created them, and they spend their lives awaiting the day they will be destroyed and returned to Abaddon for an eternity of torment. Their frequent interactions with daemons occasionally spawns reality-warping half-blood children who rise to positions of great power in _urdefhan_ society—if they manage to survive.