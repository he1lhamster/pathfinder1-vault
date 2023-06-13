---
cssclass: [monsters]
title1: Harrower
title2: Harrower
CR: 9
sources:
- name: Inner Sea NPC Codex
  page: 29
  link: http://paizo.com/products/btpy92lj?Pathfinder-Campaign-Setting-Inner-Sea-NPC-Codex
XP: 6400
race: Human
classes:
- bard 7
- harrower 3
alignment: CG
size: Medium
type: humanoid
subtypes:
- human
initiative:
  bonus: 1
AC:
  AC: 15
  touch: 12
  flat_footed: 14
  components:
    armor: 3
    deflection: 1
    dex: 1
HP:
  HP: 62
  long: 7d8+3d6+17
  HD: 10
saves:
  fort: 4
  ref: 8
  will: 10
  will_other: +1 vs. enchantments
  other: +4 vs. bardic performance, language-dependent, and sonic
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 dagger +6/+1 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: +1 dagger
      bonus:
      - 6
      - 1
  ranged:
  - - text: +1 dagger +8 (1d4/19-20)
      entries:
      - - damage: 1d4
          crit_range: 19-20
      attack: +1 dagger
      bonus:
      - 8
  special:
  - bardic performance 20 rounds/day (move action, countersong, distraction, fascinate,
    inspire competence +3, inspire courage +2, move action, suggestion)
  - harrow casting 3/day
spells:
  entries:
  - name: legend lore
    source: Bard
    level: 4
  - name: shout
    source: Bard
    level: 4
    DC: 18
  - name: clairaudience/clairvoyance
    source: Bard
    level: 3
  - name: good hope
    source: Bard
    level: 3
  - name: remove curse
    source: Bard
    level: 3
  - name: scrying
    source: Bard
    level: 3
    DC: 18
  - name: alter self
    source: Bard
    level: 2
  - name: calm emotions
    source: Bard
    level: 2
    DC: 16
  - name: detect thoughts
    source: Bard
    level: 2
    DC: 17
  - name: locate object
    source: Bard
    level: 2
  - name: hold person
    source: Bard
    level: 2
    DC: 16
  - superscripts:
    - UM
    name: anticipate peril
    source: Bard
    level: 1
    DC: 16
  - name: comprehend languages
    source: Bard
    level: 1
  - superscripts:
    - UM
    name: ear-piercing scream
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 15
  - name: remove fear
    source: Bard
    level: 1
  - name: detect magic
    source: Bard
    level: 0
  - name: ghost sound
    source: Bard
    level: 0
    DC: 14
  - name: know direction
    source: Bard
    level: 0
  - name: light
    source: Bard
    level: 0
  - name: mage hand
    source: Bard
    level: 0
  - name: read magic
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 10
    concentration: 14
    slots:
      4: 2
      3: 4
      2: 5
      1: 6
      0: at-will
ability_scores:
  STR: 8
  DEX: 12
  CON: 10
  INT: 13
  WIS: 14
  CHA: 19
BAB: 6
CMB: 5
CMD: 17
feats:
- name: Diviner's Delving
- name: Fortune Teller
- name: Harrowed
- name: Skill Focus (Perform [oratory])
- name: Spell Focus (divination)
- name: Toughness
skills:
  Appraise: 9
  Bluff: 12
  Disguise: 12
  Intimidate: 10
  Knowledge (arcana): 12
  Knowledge (history): 10
  Knowledge (local): 10
  Knowledge (nobility): 10
  Perform (dance): 12
  Perform (oratory): 23
  Sleight of Hand: 9
  Spellcraft: 14
  Stealth: 9
  Use Magic Device: 8
  Perception: 2
languages:
- Common
- Varisian
special_qualities:
- bardic knowledge +3
- blessing of the harrow 1/day
- lore master 1/day
- versatile performance (dance, oratory)
- tower of intelligence
- tower of strength
gear:
  combat:
  - potions of cat's grace (3)
  - potions of cure moderate wounds (2)
  - potion of protection from evil
  - scroll of confusion
  - scroll of eagle's splendor
  - wand of cure light wounds (40 charges)
  - wand of magic missile (50 charges)
  - wand of sound burst (17 charges)
  - feather token (whip)
  other:
  - +1 leather armor
  - +1 dagger
  - cloak of resistance +1
  - ring of protection +1
  - seer's tea
  - Harrow deck
  - spell component pouch
  - 28 gp
special_abilities:
  Blessing of the Harrow (Su): 'Once per day, a harrower may spend 10 minutes to perform
    a harrowing for himself and all allies within 20 feet to gain an insight bonus
    that lasts 24 hours based upon the suit with the most cards showing after the
    reading. In the case of a tie, the harrower chooses one suit. Strength: +1 on
    attack rolls; Dexterity: +1 to AC; Constitution: +1 on all skill checks; Intelligence:
    +1 on all skill checks; Wisdom: +1 on all saving throws; Charisma: +1 on all caster
    level and concentration checks.'
  Harrow Casting (Su): As he casts a spell, the harrower can draw three cards from
    his Harrow deck. This adds both a somatic component (if the spell does not already
    have one) and a focus component (the Harrow deck) to the spell, but does not increase
    the spell's casting time. Each card the harrower draws of the Intelligence or
    Strength suits grants the benefit of the tower of intelligence or tower of strength
    abilities, respectively. Each card the harrower draws that exactly matches his
    alignment counts as two cards of that suit. Cards drawn from the other four suits
    provide no benefits. A spell cannot be affected by both Harrow casting and a metamagic
    feat.
desc_long: Far from mere fortune tellers, harrowers use their mystical powers to advise
  their clans, bring doom upon their foes, and uphold the ancient and mysterious traditions
  of the Varisian wanderers.

---

# Harrower

**Source** Inner Sea NPC Codex pg. 29
**XP** 6,400
Human _[[classes/Bard|bard]]_ 7/harrower 3

CG Medium humanoid (human)
**Init** +1; **Senses** Perception +2

##### Defense

**AC** 15, touch 12, _[[conditions/Flat-Footed|flat-footed]]_ 14 (+3 armor, +1 _[[spells/Deflection|deflection]]_, +1 Dex)
**hp** 62 (10 HD; 7d8+3d6+17)
**Fort** +4, **Ref** +8, **Will** +10 (+1 vs. enchantments); +4 vs. bardic performance, language-dependent, and sonic

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Dagger|dagger]]_ +6/+1 (1d4/19–20)
**Ranged** +1 _dagger_ +8 (1d4/19–20)
**Special Attacks** bardic performance 20 rounds/day (move action, countersong, _[[universal monster rules/Distraction|distraction]]_, fascinate, inspire competence +3, inspire courage +2, move action, _[[spells/Suggestion|suggestion]]_), harrow casting 3/day
**_Bard_ Spells Known **(CL 10th; concentration +14)
4th (2/day)—_[[spells/Legend Lore|legend lore]]_, _[[spells/Shout|shout]]_ (DC 18)
3rd (4/day)—clairaudience/clairvoyance, _[[spells/Good Hope|good hope]]_, _[[spells/Remove Curse|remove curse]]_, _[[spells/Scrying|scrying]]_ (DC 18)
2nd (5/day)—_[[spells/Alter Self|alter self]]_, _[[spells/Calm Emotions|calm emotions]]_ (DC 16), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 17), _[[spells/Locate Object|locate object]]_, _[[spells/Hold Person|hold person]]_ (DC 16)
1st (6/day)—_[[spells/Anticipate Peril|anticipate peril]]_ (DC 16), _[[spells/Comprehend Languages|comprehend languages]]_, _[[spells/Ear-Piercing Scream|ear-piercing scream]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 15), _[[spells/Remove Fear|remove fear]]_
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 14), _[[spells/Know Direction|know direction]]_, light, _[[spells/Mage Hand|mage hand]]_, _[[spells/Read Magic|read magic]]_

##### Statistics
**Str** 8, **Dex** 12, **Con** 10, **Int** 13, **Wis** 14, **Cha** 19
**Base Atk** +6; **CMB** +5; **CMD** 17
**Feats** _[[feats/Diviner's Delving|Diviner's Delving]]_, _[[feats/Fortune Teller|Fortune Teller]]_, _[[feats/Harrowed|Harrowed]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perform [oratory]), _[[feats/Spell Focus|Spell Focus]]_ (_[[spells/Divination|divination]]_), _[[feats/Toughness|Toughness]]_
**Skills** Appraise +9, Bluff +12, Disguise +12, Intimidate +10, Knowledge (arcana) +12, Knowledge (history) +10, Knowledge (local) +10, Knowledge (nobility) +10, Perform (dance) +12, Perform (oratory) +23, Sleight of Hand +9, Spellcraft +14, Stealth +9, Use Magic Device +8
**Languages** Common, Varisian
**SQ** bardic knowledge +3, blessing of the harrow 1/day, lore master 1/day, versatile performance (dance, oratory), tower of intelligence*, tower of strength*
**Combat Gear** potions of cat’s _[[spells/Grace|grace]]_ (3), potions of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_ (2), potion of _[[spells/Protection From Evil|protection from evil]]_, scroll of _[[spells/Confusion|confusion]]_, scroll of _[[monsters/Eagle|eagle]]_’s splendor, wand of _[[spells/Cure Light Wounds|cure light wounds]]_ (40 charges), wand of _[[spells/Magic Missile|magic missile]]_ (50 charges), wand of _[[spells/Sound Burst|sound burst]]_ (17 charges), feather token (_[[items/Weapon/Whip|whip]]_); **Other Gear** +1 _[[items/Armor/Leather armor|leather armor]]_, +1 _dagger_, _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +1|cloak of _resistance_ +1]]_, _[[items/Ring/Ring of Protection +1|ring of protection +1]]_, seer’s tea, _[[items/Mundane/Harrow deck|Harrow deck]]_, _[[items/Mundane/Spell component pouch|spell component pouch]]_, 28 gp

### Special Abilities

**Blessing of the Harrow (Su)** Once per day, a _[[npcs/Harrower|harrower]]_ may spend 10 minutes to perform a _[[spells/Harrowing|harrowing]]_ for himself and all allies within 20 feet to gain an insight bonus that lasts 24 hours based upon the suit with the most _[[items/Mundane/Cards|cards]]_ showing after the reading. In the case of a tie, the _harrower_ chooses one suit. Strength: +1 on attack rolls; Dexterity: +1 to AC; Constitution: +1 on all skill checks; Intelligence: +1 on all skill checks; Wisdom: +1 on all saving throws; Charisma: +1 on all caster level and concentration checks.

**Harrow Casting (Su)** As he casts a spell, the _harrower_ can draw three _cards_ from his _Harrow deck_. This adds both a somatic component (if the spell does not already have one) and a focus component (the _Harrow deck_) to the spell, but does not increase the spell’s casting time. Each card the _harrower_ draws of the Intelligence or Strength suits grants the benefit of the tower of intelligence or tower of strength abilities, respectively. Each card the _harrower_ draws that exactly matches his alignment counts as two _cards_ of that suit. _Cards_ drawn from the other four suits provide no benefits. A spell cannot be affected by both Harrow casting and a metamagic feat.

Far from mere fortune tellers, harrowers use their mystical powers to advise their clans, bring _[[spells/Doom|doom]]_ upon their foes, and uphold the ancient and mysterious traditions of the Varisian wanderers.