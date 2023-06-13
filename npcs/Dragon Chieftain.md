---
cssclass: [monsters]
title1: Dragon Chieftain
title2: Dragon Chieftain
CR: 16
sources:
- name: NPC Codex
  page: 214
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 76800
race: Half-orc
classes:
- bard 10
- dragon disciple 7
alignment: CE
size: Medium
type: humanoid
subtypes:
- human
- orc
initiative:
  bonus: 3
senses:
  blindsense: 30
  darkvision: 60
AC:
  AC: 27
  touch: 12
  flat_footed: 27
  components:
    armor: 9
    deflection: 2
    dex: -1
    insight: 1
    natural: 6
HP:
  HP: 189
  long: 10d8+7d12+95
saves:
  fort: 16
  ref: 11
  will: 14
  other: +4 vs. bardic performance, language-dependent, and sonic
defensive_abilities:
- orc ferocity
resistances:
  fire: 5
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +19 (1d6+9 plus 1d6 fire)
      entries:
      - - damage: 1d6+9
        - damage: 1d6
          type: fire
      attack: bite
      bonus:
      - 19
    - text: 2 claws +19 (1d6+6)
      entries:
      - - damage: 1d6+6
      count: 2
      attack: claws
      bonus:
      - 19
  - - text: +1 heavy mace +19/+14/+9 (1d8+10)
      entries:
      - - damage: 1d8+10
      attack: +1 heavy mace
      bonus:
      - 19
      - 14
      - 9
  special:
  - bardic performance 26 rounds/day (move action; countersong, dirge of doom, distraction,
    fascinate, inspire competence +3, inspire courage +2, inspire greatness, suggestion)
  - breath weapon (30-foot cone, 7d6 fire, DC 17, 1/day)
  - claws (2, 1d6+6, magic, 7 rounds/day)
  - dragon bite
spell_like_abilities:
  entries:
  - name: form of the dragon I
    source: default
    freq: 1/day
    other: red dragon only
  sources:
  - name: default
    CL: 7
    concentration: 11
spells:
  entries:
  - name: greater heroism
    source: Bard
    level: 5
  - name: mass cure light wounds
    source: Bard
    level: 5
  - name: shadow walk
    source: Bard
    level: 5
    DC: 19
  - name: song of discord
    source: Bard
    level: 5
    DC: 20
  - name: cure critical wounds
    source: Bard
    level: 4
  - name: dominate person
    source: Bard
    level: 4
    DC: 19
  - name: neutralize poison
    source: Bard
    level: 4
  - name: shout
    source: Bard
    level: 4
    DC: 18
  - name: clairaudience/clairvoyance
    source: Bard
    level: 3
  - name: fear
    source: Bard
    level: 3
    DC: 17
  - name: haste
    source: Bard
    level: 3
  - name: invisibility sphere
    source: Bard
    level: 3
  - name: phantom steed
    source: Bard
    level: 3
  - name: blur
    source: Bard
    level: 2
  - name: cure moderate wounds
    source: Bard
    level: 2
  - name: detect thoughts
    source: Bard
    level: 2
    DC: 16
  - name: silence
    source: Bard
    level: 2
    DC: 16
  - name: summon swarm
    source: Bard
    level: 2
  - name: whispering wind
    source: Bard
    level: 2
  - name: charm person
    source: Bard
    level: 1
    DC: 16
  - name: cure light wounds
    source: Bard
    level: 1
  - name: expeditious retreat
    source: Bard
    level: 1
  - name: feather fall
    source: Bard
    level: 1
  - name: remove fear
    source: Bard
    level: 1
  - name: unseen servant
    source: Bard
    level: 1
  - name: dancing lights
    source: Bard
    level: 0
  - name: detect magic
    source: Bard
    level: 0
  - name: flare
    source: Bard
    level: 0
    DC: 14
  - name: mage hand
    source: Bard
    level: 0
  - name: message
    source: Bard
    level: 0
  - name: resistance
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 15
    concentration: 19
    slots:
      5: 3
      4: 5
      3: 6
      2: 6
      1: 6
      0: at-will
tactics:
  During Combat: The dragon disciple casts greater heroism and haste, then uses dominate
    person and charm person to create allies among his enemies. In melee, he uses
    his breath weapon and Dazzling Display.
ability_scores:
  STR: 22
  DEX: 8
  CON: 18
  INT: 12
  WIS: 10
  CHA: 18
BAB: 12
CMB: 18
CMD: 30
feats:
- name: Arcane Armor Mastery
- name: Arcane Armor Training
- name: Combat Casting
- name: Dazzling Display
- name: Great Fortitude
- name: Improved Initiative
- name: Power Attack
- name: Spell Focus (enchantment)
- name: Toughness
- name: Weapon Focus (bite)
- name: Weapon Focus (claws)
skills:
  Climb: 12
  Intimidate: 6
  Knowledge (arcana): 14
  Knowledge (dungeoneering): 14
  Knowledge (geography): 10
  Knowledge (history): 10
  Knowledge (local): 10
  Knowledge (nature): 10
  Knowledge (religion): 10
  Linguistics: 5
  Perception: 18
  Perform (oratory): 17
  Perform (percussion): 17
  Perform (sing): 17
  Ride: 2
  Spellcraft: 9
  Stealth: 10
  Swim: 9
languages:
- Common
- Draconic
- Goblin
- Orc
special_qualities:
- bardic knowledge +5
- blood of dragons
- jack-of-all-trades (use any skill)
- lore master 1/day
- orc blood
- versatile performance (oratory, percussion, sing)
- weapon familiarity
gear:
  combat:
  - potions of cure serious wounds (2)
  - potion of eagle's splendor
  other:
  - +5 hide armor
  - +1 heavy mace
  - amulet of natural armor +2
  - belt of physical might +2 (Str, Con)
  - cloak of resistance +3
  - dusty rose prism ioun stone
  - headband of alluring charisma +2
  - ring of protection +2
  - 1,723 gp
desc_long: These half-orcs become chieftains of savage tribes by brutally and publicly
  assassinating the former chieftains.

---

# Dragon Chieftain

**Source** NPC Codex pg. 214
**XP** 76,800
Half-orc _[[classes/Bard|bard]]_ 10/dragon disciple 7
CE Medium humanoid (human, _[[monsters/Orc|orc]]_)
**Init** +3; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 30 ft., _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +18

##### Defense

**AC** 27, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 27 (+9 armor, +2 _[[spells/Deflection|deflection]]_, –1 Dex, +1 insight, +6 natural)
**hp** 189 (10d8+7d12+95)
**Fort** +16, **Ref** +11, **Will** +14; +4 vs. bardic performance, language-dependent, and sonic
**Defensive Abilities** _orc_ _[[universal monster rules/Ferocity|ferocity]]_; **Resist** fire 5

##### Offense
**Speed** 30 ft.
**Melee** bite +19 (1d6+9 plus 1d6 fire), 2 claws +19 (1d6+6) or +1 _[[items/Weapon/Heavy mace|heavy mace]]_ +19/+14/+9 (1d8+10)
**Special Attacks** bardic performance 26 rounds/day (move action; countersong, dirge of _[[spells/Doom|doom]]_, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire competence +3, inspire courage +2, inspire greatness, _[[spells/Suggestion|suggestion]]_), _[[universal monster rules/Breath Weapon|breath weapon]]_ (30-foot cone, 7d6 fire, DC 17, 1/day), claws (2, 1d6+6, magic, 7 rounds/day), dragon bite
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 7th; concentration +11)
1/day—_[[spells/Form of the Dragon I|form of the dragon I]]_ (red dragon only)
**_Bard_ Spells Known **(CL 15th; concentration +19)
5th (3/day)—greater _[[spells/Heroism|heroism]]_, mass _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Shadow Walk|shadow walk]]_ (DC 19), _[[spells/Song of Discord|song of discord]]_ (DC 20)
4th (5/day)—_[[spells/Cure Critical Wounds|cure critical wounds]]_, _[[spells/Dominate Person|dominate person]]_ (DC 19), _[[spells/Neutralize Poison|neutralize poison]]_, _[[spells/Shout|shout]]_ (DC 18)
3rd (6/day)—clairaudience/clairvoyance, _[[universal monster rules/Fear|fear]]_ (DC 17), _[[spells/Haste|haste]]_, _[[spells/Invisibility Sphere|invisibility sphere]]_, _[[spells/Phantom Steed|phantom steed]]_
2nd (6/day)—_[[spells/Blur|blur]]_, _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Detect Thoughts|detect thoughts]]_ (DC 16), _[[spells/Silence|silence]]_ (DC 16), _[[spells/Summon Swarm|summon swarm]]_, _[[spells/Whispering Wind|whispering wind]]_
1st (6/day)—_[[spells/Charm Person|charm person]]_ (DC 16), _cure light wounds_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Remove Fear|remove fear]]_, _[[spells/Unseen Servant|unseen servant]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 14), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[universal monster rules/Resistance|resistance]]_

### Tactics

**During Combat **The dragon disciple casts greater _heroism_ and _haste_, then uses _dominate person_ and _charm person_ to create allies among his enemies. In melee, he uses his _breath weapon_ and _[[feats/Dazzling Display|Dazzling Display]]_.

##### Statistics
**Str** 22, **Dex** 8, **Con** 18, **Int** 12, **Wis** 10, **Cha** 18
**Base Atk** +12; **CMB** +18; **CMD** 30
**Feats** _[[feats/Arcane Armor Mastery|Arcane Armor Mastery]]_, _[[feats/Arcane Armor Training|Arcane Armor Training]]_, _[[feats/Combat Casting|Combat Casting]]_, _Dazzling Display_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Spell Focus|Spell Focus]]_ (enchantment), _[[feats/Toughness|Toughness]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (bite, claws)
**Skills** _[[universal monster rules/Climb|Climb]]_ +12, Intimidate +6, Knowledge (arcana, dungeoneering) +14, Knowledge (geography, history, local, nature, religion) +10, Linguistics +5, Perception +18, Perform (oratory, percussion, sing) +17, Ride +2, Spellcraft +9, Stealth +10, Swim +9
**Languages** Common, Draconic, _[[monsters/Goblin|Goblin]]_, _Orc_
**SQ** bardic knowledge +5, blood of dragons, jack-of-all-trades (use any skill), lore master 1/day, _orc_ blood, versatile performance (oratory, percussion, sing), weapon familiarity
**Combat Gear** potions of _[[spells/Cure Serious Wounds|cure serious wounds]]_ (2), potion of _[[monsters/Eagle|eagle]]_’s splendor; **Other Gear** +5 _[[items/Armor/Hide armor|hide armor]]_, +1 _heavy mace_, _[[items/Wondrous Item/Amulet of Natural Armor +2|amulet of natural armor +2]]_, _[[items/Wondrous Item/Belt of Physical Might +2|belt of physical might +2]]_ (Str, Con), _[[items/Wondrous Item/Cloak of _Resistance_ +3|cloak of _resistance_ +3]]_, _[[items/Wondrous Item/Dusty Rose Prism Ioun Stone|dusty rose prism ioun stone]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Ring/Ring of Protection +2|ring of protection +2]]_, 1,723 gp

These half-orcs become chieftains of savage tribes by brutally and publicly assassinating the former chieftains.