---
cssclass: [monsters]
title1: Drow, Drow Demonic Champion
title2: Drow Demonic Champion
CR: 9
sources:
- name: Monster Codex
  page: 37
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 6400
race: Drow
classes:
- antipaladin 10 (Pathfinder RPG Advanced Player's Guide 118)
alignment: CE
size: Medium
type: humanoid
subtypes:
- elf
initiative:
  bonus: 5
senses:
  darkvision: 120
auras:
- name: cowardice
  radius: 10
- name: despair
  radius: 10
AC:
  AC: 25
  touch: 11
  flat_footed: 24
  components:
    armor: 10
    dex: 1
    shield: 4
HP:
  HP: 79
  long: 10d10+20
saves:
  fort: 11
  ref: 7
  will: 9
  other: +2 vs. enchantments
immunities:
- sleep
- disease
SR: 16
weaknesses:
- light blindness
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 scimitar +16/+11 (1d6+5/15-20)
      entries:
      - - damage: 1d6+5
          crit_range: 15-20
      attack: +1 scimitar
      bonus:
      - 16
      - 11
  ranged:
  - - text: heavy crossbow +12 (1d10/19-20)
      entries:
      - - damage: 1d10
          crit_range: 19-20
      attack: heavy crossbow
      bonus:
      - 12
  special:
  - channel negative energy (DC 18, 5d6)
  - smite good 4/day (+3 attack and AC, +10 damage)
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: darkness
    source: default
    freq: 1/day
  - name: faerie fire
    source: default
    freq: 1/day
  - name: Like Abilities
    source: default
    freq: Antipaladin Spell
    CL: 10
    other: concentration +13
  - name: detect good
    source: default
    freq: At will
  sources:
  - name: default
    CL: 10
    concentration: 3
spells:
  entries:
  - superscripts:
    - UC
    name: litany of sight
    source: Antipaladin
    level: 3
  - name: invisibility
    source: Antipaladin
    level: 2
  - name: silence
    source: Antipaladin
    level: 2
    DC: 15
  - superscripts:
    - UC
    name: litany of sloth
    source: Antipaladin
    level: 1
  - superscripts:
    - UM
    name: murderous command
    source: Antipaladin
    level: 1
    DC: 14
  - name: protection from good
    source: Antipaladin
    level: 1
  sources:
  - name: Antipaladin
    type: prepared
    CL: 7
    concentration: 10
tactics:
  Before Combat: The demonic champion casts invisibility and protection from good
    on herself, then uses her scroll of defile armor on her full plate. She prefers
    to use her fiendish boon ability to grant her scimitar the anarchic, flaming,
    unholy, or vicious weapon special ability.
  During Combat: The demonic champion uses smite good and Channel Smite with her scimitar
    attacks to harm foes, or uses her cruelties and touch of corruption to disable
    opponents. She casts silence to interfere with spellcasters employing ranged spells
    against her.
ability_scores:
  STR: 18
  DEX: 12
  CON: 12
  INT: 12
  WIS: 8
  CHA: 16
BAB: 10
CMB: 14
CMD: 25
feats:
- name: Channel Smite
- name: Improved Critical (scimitar)
- name: Improved Initiative
- name: Shield Focus
- name: Weapon Focus (scimitar)
skills:
  Acrobatics: 0
  Climb: 3
  Intimidate: 11
  Perception: 11
  Stealth: 8
languages:
- Elven
- Undercommon
special_qualities:
- cruelties (dazed, nauseated, sickened, staggered)
- fiendish boon (weapon +2, 2/day)
- poison use
- touch of corruption 8/day (5d6)
gear:
  combat:
  - potion of cure serious wounds
  - potion of delay poison
  - potion of haste
  - scroll of defile armor
  - scroll of invisibility
  - acid (2)
  - alchemist's fire (2)
  - antitoxin
  other:
  - +1 full plate
  - +1 heavy steel shield
  - +1 scimitar
  - heavy crossbow with 10 mwk bolts
  - belt of giant strength +2
  - 69 gp
ecology:
  environment: underground
desc_long: A demonic champion has been tested by the powers of the Abyss and emerged
  stronger for it. Her soul is scarred by centuries of depraved acts, and she is irredeemable
  in her evil-something she is happy to prove. Demonic champions enjoy many creature
  comforts within drow society thanks to the spoils they claim in war, but their bloodlust
  motivates them to repeatedly return to battle.

---

# Drow, Drow Demonic Champion

**Source** Monster Codex pg. 37
**XP** 6,400
_[[monsters/Drow|Drow]]_ _[[classes/Antipaladin|antipaladin]]_ 10 (Pathfinder RPG Advanced Player’s Guide 118)
CE Medium humanoid (elf)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft.; Perception +11
**Aura** cowardice (10 ft.), despair (10 ft.)

##### Defense

**AC** 25, touch 11, _[[conditions/Flat-Footed|flat-footed]]_ 24 (+10 armor, +1 Dex, +4 _[[spells/Shield|shield]]_)
**hp** 79 (10d10+20)
**Fort** +11, **Ref** +7, **Will** +9; +2 vs. enchantments
**Immune** sleep, disease; **SR** 16
**Weaknesses** _[[universal monster rules/Light Blindness|light blindness]]_

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Scimitar|scimitar]]_ +16/+11 (1d6+5/15–20)
**Ranged** _[[items/Weapon/Heavy crossbow|heavy crossbow]]_ +12 (1d10/19–20)
**Special Attacks** channel negative energy (DC 18, 5d6), smite good 4/day (+3 attack and AC, +10 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +3)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Darkness|darkness]]_, _[[spells/Faerie Fire|faerie fire]]_
_Antipaladin_ _Spell-Like Abilities_ (CL 10th; concentration +13)
At will—_[[spells/Detect Good|detect good]]_
**_Antipaladin_ Spells Prepared **(CL 7th; concentration +10)
3rd—_[[spells/Litany of Sight|litany of sight]]_
2nd—_[[spells/Invisibility|invisibility]]_, _[[spells/Silence|silence]]_ (DC 15)
1st—_[[spells/Litany of Sloth|litany of sloth]]_, _[[spells/Murderous Command|murderous command]]_ (DC 14), _[[spells/Protection From Good|protection from good]]_

### Tactics

**Before Combat** The demonic _[[items/Armor Magic Abilities/Champion|champion]]_ casts _invisibility_ and _protection from good_ on herself, then uses her scroll of _[[spells/Defile Armor|defile armor]]_ on her _[[items/Armor/Full plate|full plate]]_. She prefers to use her fiendish boon ability to grant her _scimitar_ the _[[items/Weapon Magic Abilities/Anarchic|anarchic]]_, _[[items/Weapon Magic Abilities/Flaming|flaming]]_, _[[items/Weapon Magic Abilities/Unholy|unholy]]_, or _[[items/Weapon Magic Abilities/Vicious|vicious]]_ weapon special ability.
 **During Combat** The demonic _champion_ uses smite good and _[[feats/Channel Smite|Channel Smite]]_ with her _scimitar_ attacks to _[[spells/Harm|harm]]_ foes, or uses her cruelties and touch of corruption to disable opponents. She casts _silence_ to interfere with spellcasters employing ranged spells against her.

##### Statistics
**Str** 18, **Dex** 12, **Con** 12, **Int** 12, **Wis** 8, **Cha** 16
**Base Atk** +10; **CMB** +14; **CMD** 25
**Feats** _Channel Smite_, _[[feats/Improved Critical|Improved Critical]]_ (_scimitar_), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Shield Focus|Shield Focus]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scimitar_)
**Skills** Acrobatics +0, _[[universal monster rules/Climb|Climb]]_ +3, Intimidate +11, Perception +11, Stealth +8
**Languages** Elven, Undercommon
**SQ** cruelties (_[[conditions/Dazed|dazed]]_, _[[conditions/Nauseated|nauseated]]_, _[[conditions/Sickened|sickened]]_, _[[conditions/Staggered|staggered]]_), fiendish boon (weapon +2, 2/day), poison use, touch of corruption 8/day (5d6)
**Combat Gear** potion of _[[spells/Cure Serious Wounds|cure serious wounds]]_, potion of _[[spells/Delay Poison|delay poison]]_, potion of _[[spells/Haste|haste]]_, scroll of _defile armor_, scroll of _invisibility_, acid (2), _[[classes/Alchemist|alchemist]]_’s fire (2), _[[items/Mundane/Antitoxin|antitoxin]]_; **Other Gear** +1 _full plate_, +1 _[[items/Shield/Heavy steel shield|heavy steel shield]]_, +1 _scimitar_, _heavy crossbow_ with 10 mwk bolts, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, 69 gp

##### Ecology

**Environment** underground

##### Description

A demonic _champion_ has been tested by the powers of the Abyss and emerged stronger for it. Her soul is scarred by centuries of depraved acts, and she is irredeemable in her evil—something she is happy to prove. Demonic champions enjoy many creature comforts within _drow_ society thanks to the spoils they claim in war, but their bloodlust motivates them to repeatedly return to battle.