---
cssclass: [monsters]
title1: Trickster Mage
title2: Trickster Mage
CR: 7
sources:
- name: NPC Codex
  page: 165
  link: http://paizo.com/products/btpy8v3a?Pathfinder-Roleplaying-Game-NPC-Codex
XP: 3200
race: Gnome
classes:
- sorcerer 8
alignment: CE
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 2
senses:
  low-light vision: true
AC:
  AC: 16
  touch: 14
  flat_footed: 13
  components:
    armor: 2
    dex: 2
    dodge: 1
    size: 1
HP:
  HP: 46
  long: 8d6+16
saves:
  fort: 3
  ref: 4
  will: 10
  other: +2 vs. illusions
defensive_abilities:
- defensive training (+4 dodge bonus to AC vs. giants)
speeds:
  base: 20
attacks:
  melee:
  - - text: sickle +3 (1d4-2)
      entries:
      - - damage: 1d4-2
      attack: sickle
      bonus:
      - 3
  ranged:
  - - text: mwk light crossbow +8 (1d6/19-20)
      entries:
      - - damage: 1d6
          crit_range: 19-20
      attack: mwk light crossbow
      bonus:
      - 8
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
spell_like_abilities:
  entries:
  - name: dancing lights
    source: default
    freq: 1/day
  - name: ghost sound
    source: default
    freq: 1/day
    DC: 15
  - name: prestidigitation
    source: default
    freq: 1/day
  - name: speak with animals
    source: default
    freq: 1/day
  - name: laughing touch
    source: default
    freq: 7/day
  sources:
  - name: default
    CL: 8
    concentration: 12
spells:
  entries:
  - name: phantasmal killer
    source: Sorcerer
    level: 4
    DC: 21
  - name: deep slumber
    source: Sorcerer
    level: 3
    DC: 19
  - name: major image
    source: Sorcerer
    level: 3
    DC: 20
  - name: suggestion
    source: Sorcerer
    level: 3
    DC: 19
  - name: hideous laughter
    source: Sorcerer
    level: 2
    DC: 18
  - name: hypnotic pattern
    source: Sorcerer
    level: 2
    DC: 19
  - name: mirror image
    source: Sorcerer
    level: 2
  - name: scorching ray
    source: Sorcerer
    level: 2
  - name: charm person
    source: Sorcerer
    level: 1
    DC: 15
  - name: color spray
    source: Sorcerer
    level: 1
    DC: 18
  - name: entangle
    source: Sorcerer
    level: 1
    DC: 15
  - name: magic missile
    source: Sorcerer
    level: 1
  - name: shield
    source: Sorcerer
    level: 1
  - name: ventriloquism
    source: Sorcerer
    level: 1
    DC: 18
  - name: daze
    source: Sorcerer
    level: 0
    DC: 16
  - name: detect magic
    source: Sorcerer
    level: 0
  - name: flare
    source: Sorcerer
    level: 0
    DC: 14
  - name: mage hand
    source: Sorcerer
    level: 0
  - name: message
    source: Sorcerer
    level: 0
  - name: ray of frost
    source: Sorcerer
    level: 0
  - name: read magic
    source: Sorcerer
    level: 0
  - name: touch of fatigue
    source: Sorcerer
    level: 0
    DC: 14
  sources:
  - name: Sorcerer
    type: known
    CL: 8
    concentration: 12
    slots:
      4: 4
      3: 6
      2: 7
      1: 7
      0: at-will
    bloodline: fey
tactics:
  During Combat: The sorcerer casts mirror image, then attempts to control or humiliate
    opponents with charm person, hideous laughter, suggestion, or his wand of grease.
ability_scores:
  STR: 6
  DEX: 14
  CON: 12
  INT: 12
  WIS: 14
  CHA: 18
BAB: 4
CMB: 1
CMD: 14
feats:
- name: Dodge
- name: Eschew Materials
- name: Greater Spell Focus (illusion)
- name: Iron Will
- name: Mobility
- name: Spell Focus (illusion)
skills:
  Bluff: 12
  Knowledge (arcana): 8
  Knowledge (nature): 5
  Perception: 10
  Spellcraft: 8
  Use Magic Device: 11
languages:
- Common
- Elven
- Gnome
- Sylvan
special_qualities:
- bloodline arcana (+2 DC for compulsion spells)
- gnome magic
- woodland stride
gear:
  combat:
  - potion of cure moderate wounds
  - screaming bolts (3)
  - wand of grease (20 charges)
  - wand of invisibility (21 charges)
  other:
  - masterwork light crossbow with 10 bolts
  - sickle
  - bracers of armor +2
  - book of pressed fairy wings
  - 168 gp
desc_long: The trickster mage thinks everyone deserves to be the butt of his jokes,
  even if they don't want to be.

---

# Trickster Mage

**Source** NPC Codex pg. 165
**XP** 3,200
Gnome _[[classes/Sorcerer|sorcerer]]_ 8
CE Small humanoid (gnome)
**Init** +2; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +10

##### Defense

**AC** 16, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+2 armor, +2 Dex, +1 dodge, +1 size)
**hp** 46 (8d6+16)
**Fort** +3, **Ref** +4, **Will** +10; +2 vs. illusions
**Defensive Abilities** defensive _[[items/Weapon Magic Abilities/Training|training]]_ (+4 _dodge_ bonus to AC vs. giants)

##### Offense
**Speed** 20 ft.
**Melee** _[[items/Weapon/Sickle|sickle]]_ +3 (1d4–2)
**Ranged** mwk _[[items/Weapon/Light crossbow|light crossbow]]_ +8 (1d6/19–20)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 8th; concentration +12)
1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 15), _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_
7/day—laughing touch
**_Sorcerer_ Spells Known **(CL 8th; concentration +12)
4th (4/day)—_[[spells/Phantasmal Killer|phantasmal killer]]_ (DC 21)
3rd (6/day)—_[[spells/Deep Slumber|deep slumber]]_ (DC 19), _[[spells/Major Image|major image]]_ (DC 20), _[[spells/Suggestion|suggestion]]_ (DC 19)
2nd (7/day)—_[[spells/Hideous Laughter|hideous laughter]]_ (DC 18), _[[spells/Hypnotic Pattern|hypnotic pattern]]_ (DC 19), _[[spells/Mirror Image|mirror image]]_, _[[spells/Scorching Ray|scorching ray]]_
1st (7/day)—_[[spells/Charm Person|charm person]]_ (DC 15), _[[spells/Color Spray|color spray]]_ (DC 18), _[[spells/Entangle|entangle]]_ (DC 15), _[[spells/Magic Missile|magic missile]]_, _[[spells/Shield|shield]]_, _[[spells/Ventriloquism|ventriloquism]]_ (DC 18)
0 (at will)—_[[spells/Daze|daze]]_ (DC 16), _[[spells/Detect Magic|detect magic]]_, _[[spells/Flare|flare]]_ (DC 14), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Ray of Frost|ray of frost]]_, _[[spells/Read Magic|read magic]]_, _[[spells/Touch of Fatigue|touch of fatigue]]_ (DC 14)
**Bloodline **fey

### Tactics

**During Combat **The _sorcerer_ casts _mirror image_, then attempts to control or humiliate opponents with _charm person_, _hideous laughter_, _suggestion_, or his wand of _[[spells/Grease|grease]]_.

##### Statistics
**Str** 6, **Dex** 14, **Con** 12, **Int** 12, **Wis** 14, **Cha** 18
**Base Atk** +4; **CMB** +1; **CMD** 14
**Feats** _Dodge_, _[[feats/Eschew Materials|Eschew Materials]]_, _[[feats/Greater Spell Focus|Greater Spell Focus]]_ (illusion), _[[feats/Iron Will|Iron Will]]_, _[[feats/Mobility|Mobility]]_, _[[feats/Spell Focus|Spell Focus]]_ (illusion)
**Skills** Bluff +12, Knowledge (arcana) +8, Knowledge (nature) +5, Perception +10, Spellcraft +8, Use Magic Device +11
**Languages** Common, Elven, Gnome, Sylvan
**SQ** bloodline arcana (+2 DC for compulsion spells), gnome magic, woodland stride
**Combat Gear** potion of _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, screaming bolts (3), wand of _grease_ (20 charges), wand of _[[spells/Invisibility|invisibility]]_ (21 charges); **Other Gear** masterwork _light crossbow_ with 10 bolts, _sickle_, _[[items/Wondrous Item/Bracers of Armor +2|bracers of armor +2]]_, book of pressed fairy wings, 168 gp

The _[[npcs/Trickster Mage|trickster mage]]_ thinks everyone deserves to be the butt of his jokes, even if they don’t want to be.