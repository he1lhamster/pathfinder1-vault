---
cssclass: [monsters]
title1: Ghoul, Ghoul Commander
title2: Ghoul Commander
CR: 8
sources:
- name: Monster Codex
  page: 84
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 4800
race: Ghoul
classes:
- antipaladin 7 (Pathfinder RPG Advanced Player's Guide 118)
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 3
senses:
  darkvision: 60
auras:
- name: cowardice
  radius: 10
AC:
  AC: 21
  touch: 13
  flat_footed: 18
  components:
    armor: 6
    dex: 3
    natural: 2
HP:
  HP: 99
  long: 2d8+7d10+52
  HD: 9
saves:
  fort: 13
  ref: 9
  will: 15
defensive_abilities:
- channel resistance +2
immunities:
- disease
- undead traits
speeds:
  base: 20
attacks:
  melee:
  - - text: mwk greataxe +15/+10 (1d12+7/19-20/×3)
      entries:
      - - damage: 1d12+7
          crit_range: 19-20
          crit_multiplier: 3
      attack: mwk greataxe
      bonus:
      - 15
      - 10
    - text: bite +8 (1d6+2 plus disease and paralysis)
      entries:
      - - damage: 1d6+2
        - effect: disease
        - effect: paralysis
      attack: bite
      bonus:
      - 8
  - - text: bite +13 (1d6+5 plus disease and paralysis)
      entries:
      - - damage: 1d6+5
        - effect: disease
        - effect: paralysis
      attack: bite
      bonus:
      - 13
    - text: 2 claws +13 (1d6+5 plus paralysis)
      entries:
      - - damage: 1d6+5
        - effect: paralysis
      count: 2
      attack: claws
      bonus:
      - 13
  ranged:
  - - text: mwk composite shortbow +12/+7 (1d6+5/×3)
      entries:
      - - damage: 1d6+5
          crit_multiplier: 3
      attack: mwk composite shortbow
      bonus:
      - 12
      - 7
  special:
  - channel negative energy (DC 17, 4d6)
  - disease (DC 15)
  - paralysis (1d4+1 rounds, DC 15, elves are immune to this effect)
  - smite good 3/day (+4 attack and AC, +7 damage)
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: At will
  sources:
  - name: default
    CL: 7
    concentration: 11
spells:
  entries:
  - name: desecrate
    source: Antipaladin
    level: 2
  - name: disguise self
    source: Antipaladin
    level: 1
  - name: inflict light wounds
    source: Antipaladin
    level: 1
    DC: 15
  sources:
  - name: Antipaladin
    type: prepared
    CL: 4
    concentration: 8
tactics:
  Before Combat: The ghoul commander is usually accompanied by a fiendish dire boar
    mount. If he is defending an area, he casts desecrate on the area (these bonuses
    are not included in his statistics).
  During Combat: The commander begins combat by charging in on his boar. He prefers
    to attack with his greataxe.
ability_scores:
  STR: 20
  DEX: 17
  CON:
  INT: 13
  WIS: 16
  CHA: 18
BAB: 8
CMB: 13
CMD: 26
feats:
- name: Cleave
- name: Improved Critical (greataxe)
- name: Power Attack
- name: Toughness
- name: Weapon Focus (greataxe)
skills:
  Bluff: 11
  Intimidate: 16
  Perception: 15
  Ride: 12
languages:
- Common
- Undercommon
special_qualities:
- cruelties (fatigued, staggered)
- fiendish boon (fiendish dire boar servant)
- touch of corruption 7/day (3d6)
gear:
  combat:
  - scroll of inflict serious wounds
  other:
  - mwk breastplate
  - mwk composite shortbow with 20 arrows
  - mwk greataxe
  - belt of giant strength +2
  - 79 gp
ecology:
  environment: any land
desc_long: ''

---

# Ghoul, Ghoul Commander

**Source** Monster Codex pg. 84
**XP** 4,800
_[[monsters/Ghoul|Ghoul]]_ _[[classes/Antipaladin|antipaladin]]_ 7 (Pathfinder RPG Advanced Player’s Guide 118)
CE Medium undead
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +15
**Aura** cowardice (10 ft.)

##### Defense

**AC** 21, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+6 armor, +3 Dex, +2 natural)
**hp** 99 (9 HD; 2d8+7d10+52)
**Fort** +13, **Ref** +9, **Will** +15
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2; **Immune** disease, _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 20 ft.
**Melee** mwk _[[items/Weapon/Greataxe|greataxe]]_ +15/+10 (1d12+7/19–20/×3), bite +8 (1d6+2 plus disease and _[[universal monster rules/Paralysis|paralysis]]_) or bite +13 (1d6+5 plus disease and _paralysis_), 2 claws +13 (1d6+5 plus _paralysis_)
**Ranged** mwk _[[items/Weapon/Composite shortbow|composite shortbow]]_ +12/+7 (1d6+5/×3)
**Special Attacks** channel negative energy (DC 17, 4d6), disease (DC 15), _paralysis_ (1d4+1 rounds, DC 15, elves are immune to this effect), smite good 3/day (+4 attack and AC, +7 damage)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +11)
At will—_[[spells/Detect Good|detect good]]_
**_Antipaladin_ Spells Prepared **(CL 4th; concentration +8)
2nd—_[[spells/Desecrate|desecrate]]_
1st—_[[spells/Disguise Self|disguise self]]_, _[[spells/Inflict Light Wounds|inflict light wounds]]_ (DC 15)

### Tactics

**Before Combat** The _ghoul_ commander is usually accompanied by a fiendish dire _[[monsters/Boar|boar]]_ _[[spells/Mount|mount]]_. If he is _[[items/Weapon Magic Abilities/Defending|defending]]_ an area, he casts _desecrate_ on the area (these bonuses are not included in his statistics).
 **During Combat** The commander begins combat by charging in on his _boar_. He prefers to attack with his _greataxe_.

##### Statistics
**Str** 20, **Dex** 17, **Con** —, **Int** 13, **Wis** 16, **Cha** 18
**Base Atk** +8; **CMB** +13; **CMD** 26
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Improved Critical|Improved Critical]]_ (_greataxe_), _[[feats/Power Attack|Power Attack]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_greataxe_)
**Skills** Bluff +11, Intimidate +16, Perception +15, Ride +12
**Languages** Common, Undercommon
**SQ** cruelties (_[[conditions/Fatigued|fatigued]]_, _[[conditions/Staggered|staggered]]_), fiendish boon (fiendish dire _boar_ servant), touch of corruption 7/day (3d6)
**Combat Gear** scroll of _[[spells/Inflict Serious Wounds|inflict serious wounds]]_; **Other Gear** mwk _[[items/Armor/Breastplate|breastplate]]_, mwk _composite shortbow_ with 20 arrows, mwk _greataxe_, _[[items/Wondrous Item/Belt of Giant Strength +2|belt of giant strength +2]]_, 79 gp

##### Ecology

**Environment** any land

##### Description

## Fiendish Dire _Boar_ Servant

**hp** 42 (Pathfinder RPG Bestiary 36, 294)

When ghouls marshal themselves into organized groups, it is _ghoul_ commanders who shoulder the responsibility of _[[feats/Leadership|leadership]]_ and _[[spells/Command|command]]_. In “civilized” _ghoul_ cities and nations, _ghoul_ commanders serve as an elite _[[npcs/Officer|officer]]_ class, directing and commanding units of more common ghouls in military maneuvers and on excursions. While they receive their orders from ghouls higher up the chain of _command_, _ghoul_ commanders are responsible for translating those orders into concrete tactics, and enjoy great autonomy on the battlefield—so long as their strategies succeed, at least.