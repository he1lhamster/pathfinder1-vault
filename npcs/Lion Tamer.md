---
cssclass: [monsters]
title1: Lion Tamer
title2: Lion Tamer
CR: 14
sources:
- name: NPC Codex
  page: 38
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 38400
race: Gnome
classes:
- bard 15
alignment: CN
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 3
senses:
  low-light vision: true
AC:
  AC: 23
  touch: 16
  flat_footed: 20
  components:
    armor: 6
    deflection: 2
    dex: 3
    natural: 1
    size: 1
HP:
  HP: 86
  long: 15d8+15
saves:
  fort: 6
  ref: 13
  will: 10
  other: +2 vs. illusions, +4 vs. bardic performance, language-dependent, and sonic
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 shock whip +17/+12/+7 (1d2+1 nonlethal plus 1d6 electricity)
      entries:
      - - damage: 1d2+1
          type: nonlethal
        - damage: 1d6
          type: electricity
      attack: +1 shock whip
      bonus:
      - 17
      - 12
      - 7
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - bardic performance 38 rounds/day (swift action; countersong, dirge of doom, distraction,
    fascinate, frightening tune, inspire competence +5, inspire courage +3, inspire
    greatness, inspire heroics, soothing performance, suggestion)
space: 5
reach: 5
reach_other: 10 ft. with whip
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: ghost sound
    source: default
    freq: 1/day
  - name: prestidigitation
    source: default
    freq: 1/day
  - name: speak with animals
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 4
    concentration: 8
spells:
  entries:
  - name: greater heroism
    source: Bard
    level: 5
  - name: mass suggestion
    source: Bard
    level: 5
    DC: 21
  - name: mislead
    source: Bard
    level: 5
  - name: summon monster V
    source: Bard
    level: 5
  - name: cure critical wounds
    source: Bard
    level: 4
    DC: 20
  - name: dominate person
    source: Bard
    level: 4
    DC: 20
  - name: greater invisibility
    source: Bard
    level: 4
  - name: summon monster IV
    source: Bard
    level: 4
  - name: charm monster
    source: Bard
    level: 3
    DC: 19
  - name: glibness
    source: Bard
    level: 3
  - name: haste
    source: Bard
    level: 3
    DC: 19
  - name: speak with animals
    source: Bard
    level: 3
  - name: summon monster III
    source: Bard
    level: 3
  - name: animal trance
    source: Bard
    level: 2
    DC: 18
  - name: cat's grace
    source: Bard
    level: 2
  - name: mirror image
    source: Bard
    level: 2
  - name: pyrotechnics
    source: Bard
    level: 2
    DC: 18
  - name: rage
    source: Bard
    level: 2
  - name: summon monster II
    source: Bard
    level: 2
  - name: animate rope
    source: Bard
    level: 1
  - name: charm person
    source: Bard
    level: 1
    DC: 17
  - name: disguise self
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 17
  - name: summon monster I
    source: Bard
    level: 1
  - name: ventriloquism
    source: Bard
    level: 1
    DC: 18
  - name: dancing lights
    source: Bard
    level: 0
  - name: daze
    source: Bard
    level: 0
    DC: 16
  - name: flare
    source: Bard
    level: 0
    DC: 16
  - name: mage hand
    source: Bard
    level: 0
  - name: mending
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 15
    concentration: 21
    slots:
      5: 4
      4: 5
      3: 6
      2: 7
      1: 7
      0: at-will
tactics:
  During Combat: The bard casts greater invisibility on himself, and sends forth summoned
    creatures and trained lions.
ability_scores:
  STR: 10
  DEX: 16
  CON: 10
  INT: 13
  WIS: 10
  CHA: 22
BAB: 11
CMB: 13
CMB_other: +17 disarm or trip
CMD: 25
CMD_other: 27 vs. disarm or trip
feats:
- name: Agile Maneuvers
- name: Combat Expertise
- name: Greater Disarm
- name: Greater Trip
- name: Improved Disarm
- name: Improved Trip
- name: Weapon Finesse
- name: Weapon Focus (whip)
skills:
  Knowledge (arcana): 13
  Knowledge (local): 15
  Knowledge (nature): 15
  Perception: 15
  Perform (comedy): 24
  Perform (dance): 24
  Perform (oratory): 24
  Perform (wind): 24
  Profession (showman): 4
  Stealth: 24
  Use Magic Device: 18
languages:
- Common
- Gnome
- Sylvan
special_qualities:
- bardic knowledge +7
- jack-of-all-trades (use any skill)
- lore master 2/day
- versatile performance (comedy, dance, oratory, wind)
- weapon familiarity
gear:
  combat:
  - potion of invisibility
  - scroll of bull's strength
  - scroll of cat's grace
  - wand of cure moderate wounds (50 charges)
  other:
  - +2 chain shirt
  - +1 shock whip
  - amulet of natural armor +1
  - cloak of resistance +1
  - headband of alluring charisma +4
  - ring of protection +2
  - trained lion
  - 349 gp
desc_long: These bards tame and control wild animals.

---

# Lion Tamer

**Source** NPC Codex pg. 38
**XP** 38,400
Gnome _[[classes/Bard|bard]]_ 15

CN Small humanoid (gnome)
**Init** +3; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +15

##### Defense

**AC** 23, touch 16, _[[conditions/Flat-Footed|flat-footed]]_ 20 (+6 armor, +2 deflection, +3 Dex, +1 natural, +1 size)
**hp** 86 (15d8+15)
**Fort** +6, **Ref** +13, **Will** +10; +2 vs. illusions, +4 vs. bardic performance, language-dependent, and sonic
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _[[feats/Dodge|dodge]]_ bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon Magic Abilities/Shock|shock]]_ _[[items/Weapon/Whip|whip]]_ +17/+12/+7 (1d2+1 nonlethal plus 1d6 electricity)
**Space** 5 ft., **Reach** 5 ft. (10 ft. with _whip_)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, bardic performance 38 rounds/day (swift action; countersong, dirge of _[[spells/Doom|doom]]_, _[[universal monster rules/Distraction|distraction]]_, fascinate, frightening tune, inspire competence +5, inspire courage +3, inspire greatness, inspire heroics, soothing performance, _[[spells/Suggestion|suggestion]]_)
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 4th; concentration +8)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
**_Bard_ Spells Known **(CL 15th; concentration +21)
5th (4/day)—greater _[[spells/Heroism|heroism]]_, mass _suggestion_ (DC 21), _[[spells/Mislead|mislead]]_, _[[spells/Summon Monster V|summon monster V]]_
4th (5/day)—_[[spells/Cure Critical Wounds|cure critical wounds]]_ (DC 20), _[[spells/Dominate Person|dominate person]]_ (DC 20), greater _[[spells/Invisibility|invisibility]]_, _[[spells/Summon Monster IV|summon monster IV]]_
3rd (6/day)—_[[spells/Charm Monster|charm monster]]_ (DC 19), _[[spells/Glibness|glibness]]_, _[[spells/Haste|haste]]_ (DC 19), _speak with animals_, _[[spells/Summon Monster III|summon monster III]]_
2nd (7/day)—_[[spells/Animal Trance|animal trance]]_ (DC 18), cat’s _[[spells/Grace|grace]]_, _[[spells/Mirror Image|mirror image]]_, _[[spells/Pyrotechnics|pyrotechnics]]_ (DC 18), _[[spells/Rage|rage]]_, _[[spells/Summon Monster II|summon monster II]]_
1st (7/day)—_[[spells/Animate Rope|animate rope]]_, _[[spells/Charm Person|charm person]]_ (DC 17), _[[spells/Disguise Self|disguise self]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 17), _[[spells/Summon Monster I|summon monster I]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 18)
0 (at will)—_dancing lights_, _[[spells/Daze|daze]]_ (DC 16), _[[spells/Flare|flare]]_ (DC 16), _[[spells/Mage Hand|mage hand]]_, _[[spells/Mending|mending]]_, _prestidigitation_

### Tactics

**During Combat **The _bard_ casts greater _invisibility_ on himself, and sends forth summoned creatures and trained lions.

##### Statistics
**Str** 10, **Dex** 16, **Con** 10, **Int** 13, **Wis** 10, **Cha** 22
**Base Atk** +11; **CMB** +13 (+17 disarm or _[[universal monster rules/Trip|trip]]_); **CMD** 25 (27 vs. disarm or _trip_)
**Feats** _[[feats/Agile Maneuvers|Agile Maneuvers]]_, _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Greater Disarm|Greater Disarm]]_, _[[feats/Greater Trip|Greater Trip]]_, _[[feats/Improved Disarm|Improved Disarm]]_, _[[feats/Improved Trip|Improved Trip]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_whip_)
**Skills** Knowledge (arcana) +13, Knowledge (local, nature) +15, Perception +15, Perform (comedy, dance, oratory, wind) +24, Profession (showman) +4, Stealth +24, Use Magic Device +18
**Languages** Common, Gnome, Sylvan
**SQ** bardic knowledge +7, jack-of-all-trades (use any skill), lore master 2/day, versatile performance (comedy, dance, oratory, wind), weapon familiarity
**Combat Gear** potion of _invisibility_, scroll of bull’s strength, scroll of cat’s _grace_, wand of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (50 charges); **Other Gear** +2 _[[items/Armor/Chain shirt|chain shirt]]_, +1 _shock_ _whip_, _[[items/Wondrous Item/Amulet of Natural Armor +1|amulet of natural armor +1]]_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +4|headband of alluring charisma +4]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, trained _[[monsters/Lion|lion]]_, 349 gp

These bards tame and control wild animals.