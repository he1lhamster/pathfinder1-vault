---
cssclass: [monsters]
title1: Chameleon
title2: Chameleon
CR: 10
sources:
- name: NPC Codex
  page: 34
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 9600
race: Half-orc
classes:
- bard 11
alignment: N
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 1
senses:
  darkvision: 60
AC:
  AC: 19
  touch: 13
  flat_footed: 17
  components:
    armor: 6
    deflection: 1
    dex: 1
    dodge: 1
HP:
  HP: 75
  long: 11d8+22
saves:
  fort: 4
  ref: 8
  will: 7
  other: +4 vs. bardic performance, language-dependent, and sonic
defensive_abilities:
- orc ferocity
speeds:
  base: 30
attacks:
  melee:
  - - text: +2 falchion +15/+10 (2d4+8/18-20)
      entries:
      - - damage: 2d4+8
          crit_range: 18-20
      attack: +2 falchion
      bonus:
      - 15
      - 10
  ranged:
  - - text: shortbow +9/+4 (1d6/×3)
      entries:
      - - damage: 1d6
          crit_multiplier: 3
      attack: shortbow
      bonus:
      - 9
      - 4
  special:
  - bardic performance 29 rounds/day (move action; countersong, dirge of doom, distraction,
    fascinate, inspire competence +4, inspire courage +3, inspire greatness, suggestion)
spells:
  entries:
  - name: dimension door
    source: Bard
    level: 4
  - name: freedom of movement
    source: Bard
    level: 4
  - name: greater invisibility
    source: Bard
    level: 4
  - name: gaseous form
    source: Bard
    level: 3
  - name: haste
    source: Bard
    level: 3
    DC: 18
  - name: see invisibility
    source: Bard
    level: 3
  - name: slow
    source: Bard
    level: 3
    DC: 18
  - name: alter self
    source: Bard
    level: 2
  - name: blindness/deafness
    source: Bard
    level: 2
    DC: 17
  - name: cure moderate wounds
    source: Bard
    level: 2
    DC: 17
  - name: detect thoughts
    source: Bard
    level: 2
    DC: 17
  - name: mirror image
    source: Bard
    level: 2
  - name: charm person
    source: Bard
    level: 1
    DC: 16
  - name: disguise self
    source: Bard
    level: 1
  - name: expeditious retreat
    source: Bard
    level: 1
  - name: feather fall
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 16
  - name: undetectable alignment
    source: Bard
    level: 1
  - name: daze
    source: Bard
    level: 0
    DC: 15
  - name: detect magic
    source: Bard
    level: 0
  - name: flare
    source: Bard
    level: 0
    DC: 15
  - name: mage hand
    source: Bard
    level: 0
  - name: open/close
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 11
    concentration: 16
    slots:
      4: 2
      3: 5
      2: 5
      1: 6
      0: at-will
tactics:
  Before Combat: The bard drinks her potion of bull's strength and potion of eagle's
    splendor.
  During Combat: The bard casts greater invisibility, then enters melee, using haste
    to augment her attacks or slow to hinder foes.
  Base Statistics: Without bull's strength and eagle's splendor, the bard's statistics
    are Bard Melee +2 falchion +13/+8 (2d4+5/18-20); Spells Known reduce spell DCs
    by 2; Str 14, Cha 17; CMB +10 (+12 sunder); CMD 23; Skills Climb +7, Intimidate
    +10, Perform (act) +17, Perform (dance) +17, Perform (oratory) +17.
ability_scores:
  STR: 18
  DEX: 13
  CON: 12
  INT: 10
  WIS: 10
  CHA: 17
BAB: 8
CMB: 12
CMB_other: +14 sunder
CMD: 25
feats:
- name: Arcane Strike
- name: Dazzling Display
- name: Dodge
- name: Improved Sunder
- name: Power Attack
- name: Weapon Focus (falchion)
skills:
  Climb: 9
  Intimidate: 12
  Knowledge (arcana): 9
  Knowledge (nobility): 9
  Knowledge (local): 12
  Perception: 9
  Perform (act): 19
  Perform (dance): 19
  Perform (oratory): 19
  Sense Motive: 6
  Spellcraft: 6
  Stealth: 13
languages:
- Common
- Orc
special_qualities:
- bardic knowledge +5
- jack-of-all-trades (use any skill)
- lore master 2/day
- orc blood
- versatile performance (act, dance, oratory)
- weapon familiarity
gear:
  combat:
  - potions of bull's strength (2)
  - potions of eagle's splendor (2)
  - potions of enlarge person (2)
  - potions of reduce person (2)
  other:
  - +2 chain shirt
  - +2 falchion
  - shortbow with 20 arrows
  - ring of protection +1
  - disguise kit
  - 295 gp
desc_long: Chameleons are more comfortable portraying other people than appearing
  in their own natural forms.

---

# Chameleon

**Source** NPC Codex pg. 34
**XP** 9,600
Half-orc _[[classes/Bard|bard]]_ 11

N Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +1; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +9

##### Defense

**AC** 19, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+6 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex, +1 _[[feats/Dodge|dodge]]_)
**hp** 75 (11d8+22)
**Fort** +4, **Ref** +8, **Will** +7; +4 vs. bardic performance, language-dependent, and sonic
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_

##### Offense
**Speed** 30 ft.
**Melee** +2 _[[items/Weapon/Falchion|falchion]]_ +15/+10 (2d4+8/18–20)
**Ranged** _[[items/Weapon/Shortbow|shortbow]]_ +9/+4 (1d6/×3)
**Special Attacks** bardic performance 29 rounds/day (move action; countersong, dirge of _[[spells/Doom|doom]]_, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire competence +4, inspire courage +3, inspire greatness, _[[spells/Suggestion|suggestion]]_)
**_Bard_ Spells Known **(CL 11th; concentration +16)
4th (2/day)—_[[spells/Dimension Door|dimension door]]_, _[[spells/Freedom of Movement|freedom of movement]]_, greater _[[spells/Invisibility|invisibility]]_
3rd (5/day)—_[[spells/Gaseous Form|gaseous form]]_, _[[spells/Haste|haste]]_ (DC 18), _[[spells/See Invisibility|see invisibility]]_, _[[spells/Slow|slow]]_ (DC 18)
2nd (5/day)—_[[spells/Alter Self|alter self]]_, blindness/deafness (DC 17), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (DC 17), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Mirror Image|mirror image]]_
1st (6/day)—_[[spells/Charm Person|charm person]]_ (DC 16), _[[spells/Disguise Self|disguise self]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 16), _[[spells/Undetectable Alignment|undetectable alignment]]_
0 (at will)—_[[spells/Daze|daze]]_ (DC 15), _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 15), _[[spells/Mage Hand|mage hand]]_, open/close, _[[spells/Prestidigitation|prestidigitation]]_

### Tactics

**Before Combat **The _bard_ drinks her potion of bull’s strength and potion of _[[monsters/Eagle|eagle]]_’s splendor.
**During Combat **The _bard_ casts greater _invisibility_, then enters melee, using _haste_ to augment her attacks or _slow_ to _[[feats/Hinder|hinder]]_ foes.
**Base Statistics **Without bull’s strength and _eagle_’s splendor, the _bard_’s statistics are **_Bard_ Melee** +2 _falchion_ +13/+8 (2d4+5/18–20); **Spells Known **reduce spell DCs by 2; **Str **14, **Cha **17; **CMB **+10 (+12 sunder); **CMD **23; **Skills **_[[universal monster rules/Climb|Climb]]_ +7, Intimidate +10, Perform (act) +17, Perform (dance) +17, Perform (oratory) +17.

##### Statistics
**Str** 18, **Dex** 13, **Con** 12, **Int** 10, **Wis** 10, **Cha** 17
**Base Atk** +8; **CMB** +12 (+14 sunder); **CMD** 25
**Feats** _[[feats/Arcane Strike|Arcane Strike]]_, _[[feats/Dazzling Display|Dazzling Display]]_, _Dodge_, _[[feats/Improved Sunder|Improved Sunder]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_falchion_)
**Skills** _Climb_ +9, Intimidate +12, Knowledge (arcana, nobility) +9, Knowledge (local) +12, Perception +9, Perform (act, dance, oratory) +19, Sense Motive +6, Spellcraft +6, Stealth +13
**Languages** Common, _Orc_
**SQ** bardic knowledge +5, jack-of-all-trades (use any skill), lore master 2/day, _orc_ blood, versatile performance (act, dance, oratory), weapon familiarity
**Combat Gear** potions of bull’s strength (2), potions of _eagle_’s splendor (2), potions of _[[spells/Enlarge Person|enlarge person]]_ (2), potions of _[[spells/Reduce Person|reduce person]]_ (2); **Other Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +2 _falchion_, _shortbow_ with 20 arrows, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, _[[items/Mundane/Disguise kit|disguise kit]]_, 295 gp

Chameleons are more comfortable portraying other people than appearing in their own natural forms.