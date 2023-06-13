---
cssclass: [monsters]
title1: Fighting School (Master)
title2: Fighting School (Master)
CR: 14
sources:
- name: GameMastery Guide
  page: 275
  link: http://paizo.com/pathfinderRPG/v5748btpy8ffn
XP: 38400
race: Human
classes:
- monk 15
alignment: LN
size: Medium
type: humanoid
initiative:
  bonus: 3
AC:
  AC: 25
  touch: 24
  flat_footed: 22
  components:
    armor: 1
    deflection: 1
    dex: 3
    monk: 5
    wis: 5
HP:
  HP: 112
  long: 15d8+45
saves:
  fort: 12
  ref: 13
  will: 15
  other: +2 vs. enchantment
defensive_abilities:
- improved evasion
immunities:
- disease
- poison
SR: 25
speeds:
  base: 80
attacks:
  melee:
  - - text: unarmed +15/+10/+5 (2d10+3/19-20 plus 1d6 electricity)
      entries:
      - - damage: 2d10+3
          crit_range: 19-20
        - damage: 1d6
          type: electricity
      attack: unarmed
      bonus:
      - 15
      - 10
      - 5
  - - text: unarmed flurry of blows +17/+17/+12/+12/+7/+7 (2d10+3/19-20 plus 1d6 electricity)
      entries:
      - - damage: 2d10+3
          crit_range: 19-20
        - damage: 1d6
          type: electricity
      attack: unarmed flurry of blows
      bonus:
      - 17
      - 17
      - 12
      - 12
      - 7
      - 7
  - - text: kama +14/+9/+4 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: kama
      bonus:
      - 14
      - 9
      - 4
  - - text: kama flurry of blows +16/+16/+11/+11/+6/+6 (1d6+3)
      entries:
      - - damage: 1d6+3
      attack: kama flurry of blows
      bonus:
      - 16
      - 16
      - 11
      - 11
      - 6
      - 6
  ranged:
  - - text: +1 sling +15 (1d4+4)
      entries:
      - - damage: 1d4+4
      attack: +1 sling
      bonus:
      - 15
  special:
  - flurry of blows
  - quivering palm (DC 22)
  - stunning fist (16/day, DC 22, fatigued, sickened, staggered)
ability_scores:
  STR: 17
  DEX: 16
  CON: 14
  INT: 10
  WIS: 20
  CHA: 8
BAB: 11
CMB: 18
CMB_other: +22 to trip
CMD: 38
CMD_other: 40 vs. trip
feats:
- name: Gorgon's Fist
- name: Greater Trip
- name: Improved Critical (unarmed strike)
- name: Improved Trip
- name: Improved Unarmed Strike
- name: Improved Vital Strike
- name: Lunge
- name: Medusa's Wrath
- name: Power Attack
- name: Scorpion Style
- name: Skill Focus (Acrobatics)
- name: Snatch Arrows
- name: Spring Attack
- name: Stunning Fist
- name: Vital Strike
- name: Weapon Focus (unarmed strike)
skills:
  Acrobatics: 25
    jump: 60
  Climb: 10
  Escape Artist: 10
  Heal: 10
  Knowledge (history): 5
  Knowledge (religion): 5
  Perception: 23
  Profession (gardener): 10
  Sense Motive: 20
  Stealth: 20
  Survival: 6
  Swim: 10
languages:
- Common
special_qualities:
- abundant step
- fast movement
- high jump
- ki pool (12 points, lawful, magic)
- maneuver training
- slow fall 70 ft.
- wholeness of body
gear:
  combat:
  - oil of align weapon (2)
  - potion of cure light wounds (2)
  other:
  - kama
  - +1 sling with 10 bullets
  - amulet of mighty fists (shock)
  - belt of physical perfection +2
  - bracers of armor +1
  - cloak of resistance +1
  - headband of inspired wisdom +2
  - monk's robe
  - ring of protection +1
npc_boon: Masters can lend their own and their school's reputation to the PCs, granting
  a +2 bonus for 1 month on Leadership checks to attract followers or to attract a
  monk cohort.
desc_long: Masters are the undisputed champions of unarmed combat, able to focus their
  inner strength into a single devastating blow or a barrage of attacks that leave
  their enemies dazed and reeling. A master can be a unique arena champion or an emissary
  from a distant empire. Masters may travel with a cohort of 10 battle monks from
  their academy (CR 16).

---

# Fighting School (Master)

**Source** GameMastery Guide pg. 275
**XP** 38,400
Human _[[classes/Monk|monk]]_ 15

LN Medium humanoid
**Init** +3; **Senses** Perception +23

##### Defense

**AC** 25, touch 24, _[[conditions/Flat-Footed|flat-footed]]_ 22 (+1 armor, +1 _[[spells/Deflection|deflection]]_, +3 Dex, +5 _monk_, +5 Wis)
**hp** 112 (15d8+45)
**Fort** +12, **Ref** +13, **Will** +15; +2 vs. enchantment
**Defensive Abilities** improved evasion; **Immune** disease, poison; **SR** 25

##### Offense
**Speed** 80 ft.
**Melee** unarmed +15/+10/+5 (2d10+3/19–20 plus 1d6 electricity) or unarmed flurry of blows +17/+17/+12/+12/+7/+7 (2d10+3/19–20 plus 1d6 electricity) or _[[items/Weapon/Kama|kama]]_ +14/+9/+4 (1d6+3) or _kama_ flurry of blows +16/+16/+11/+11/+6/+6 (1d6+3)
**Ranged** +1 _[[items/Weapon/Sling|sling]]_ +15 (1d4+4)
**Special Attacks** flurry of blows, quivering palm (DC 22), _[[feats/Stunning Fist|stunning fist]]_ (16/day, DC 22, _[[conditions/Fatigued|fatigued]]_, _[[conditions/Sickened|sickened]]_, _[[conditions/Staggered|staggered]]_)

##### Statistics
**Str** 17, **Dex** 16, **Con** 14, **Int** 10, **Wis** 20, **Cha** 8
**Base Atk** +11; **CMB** +18 (+22 to _[[universal monster rules/Trip|trip]]_); **CMD** 38 (40 vs. _trip_)
**Feats** _[[monsters/Gorgon|Gorgon]]_’s Fist, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Critical|Improved Critical]]_ (unarmed strike), _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Improved Unarmed Strike|Improved Unarmed Strike]]_, _[[feats/Improved Vital Strike|Improved Vital Strike]]_, _[[feats/Lunge|Lunge]]_, _[[monsters/Medusa|Medusa]]_’s Wrath, _[[feats/Power Attack|Power Attack]]_, _[[feats/Scorpion Style|Scorpion Style]]_, _[[feats/Skill Focus|Skill Focus]]_ (Acrobatics), _[[feats/Snatch Arrows|Snatch Arrows]]_, _[[feats/Spring Attack|Spring Attack]]_, _Stunning Fist_, _[[feats/Vital Strike|Vital Strike]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (unarmed strike)
**Skills** Acrobatics +25 (+60 _[[spells/Jump|jump]]_), _[[universal monster rules/Climb|Climb]]_ +10, Escape Artist +10, _[[spells/Heal|Heal]]_ +10, Knowledge (history) +5, Knowledge (religion) +5, Perception +23, Profession (gardener) +10, Sense Motive +20, Stealth +20, Survival +6, Swim +10
**Languages** Common
**SQ** abundant step, fast movement, high _jump_, ki pool (12 points, lawful, magic), maneuver _[[items/Weapon Magic Abilities/Training|training]]_, _[[spells/Slow|slow]]_ fall 70 ft., wholeness of body
**Combat Gear** oil of _[[spells/Align Weapon|align weapon]]_ (2), potion of _[[spells/Cure Light Wounds|cure light wounds]]_ (2); **Other Gear** _kama_, +1 _sling_ with 10 bullets, amulet of mighty fists (_[[items/Weapon Magic Abilities/Shock|shock]]_), _[[items/Wondrous Item/Belt of Physical Perfection +2|belt of physical perfection +2]]_, _[[items/Wondrous Item/Bracers of Armor +1|bracers of armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of _[[items/Weapon Magic Abilities/Inspired|Inspired]]_ Wisdom +2|headband of _inspired_ wisdom +2]]_, _monk_’s robe, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_

**Boon** Masters can lend their own and their school’s reputation to the PCs, granting a +2 bonus for 1 month on _[[feats/Leadership|Leadership]]_ checks to attract followers or to attract a _monk_ cohort.

Masters are the undisputed champions of unarmed combat, able to focus their inner strength into a single devastating blow or a barrage of attacks that leave their enemies _[[conditions/Dazed|dazed]]_ and reeling. A master can be a unique arena _[[items/Armor Magic Abilities/Champion|champion]]_ or an emissary from a distant empire. Masters may travel with a cohort of 10 battle monks from their academy (CR 16).