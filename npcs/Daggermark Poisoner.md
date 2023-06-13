---
cssclass: [monsters]
title1: Daggermark Poisoner
title2: Daggermark Poisoner
CR: 7
sources:
- name: Inner Sea NPC Codex
  page: 17
  link: http://paizo.com/products/btpy92lj?Pathfinder-Campaign-Setting-Inner-Sea-NPC-Codex
XP: 3200
race: Gnome
classes:
- rogue (poisoner) 5
- Daggermark poisoner 3
alignment: LE
size: Small
type: humanoid
subtypes:
- gnome
initiative:
  bonus: 7
senses:
  low-light vision: true
AC:
  AC: 21
  touch: 15
  flat_footed: 17
  other: +4 dodge vs. giants
  components:
    armor: 5
    dex: 3
    dodge: 1
    shield: 1
    size: 1
HP:
  HP: 60
  long: 5d8+3d8+21
  HD: 8
saves:
  fort: 6
  ref: 9
  will: 2
  other: +2 vs. illusions, +2 vs. poison
defensive_abilities:
- evasion
- poison resistance +2
- uncanny dodge
speeds:
  base: 20
attacks:
  melee:
  - - text: +1 rapier +11 (1d4+2/18-20 plus poison)
      entries:
      - - damage: 1d4+2
          crit_range: 18-20
        - effect: poison
      attack: +1 rapier
      bonus:
      - 11
  ranged:
  - - text: dagger +9 (1d3+1/19-20 plus poison)
      entries:
      - - damage: 1d3+1
          crit_range: 19-20
        - effect: poison
      attack: dagger
      bonus:
      - 9
  special:
  - +1 on attack rolls against goblinoid and reptilian humanoids
  - poison use
  - sneak attack +3d6
spell_like_abilities:
  entries:
  - name: detect poison
    source: default
    freq: At will
    paren_text: range 5 feet, swift action
  - name: dancing lights
    source: gnome
    freq: 1/day
  - name: ghost sound
    source: gnome
    freq: 1/day
    DC: 11
  - name: prestidigitation
    source: gnome
    freq: 1/day
  - name: speak with animals
    source: gnome
    freq: 1/day
  sources:
  - name: default
    CL: 3
  - name: gnome
    CL: 8
ability_scores:
  STR: 12
  DEX: 16
  CON: 14
  INT: 14
  WIS: 8
  CHA: 12
BAB: 5
CMB: 5
CMD: 19
feats:
- name: Combat Expertise
- name: Dodge
- name: Improved Feint
- name: Improved Initiative
- name: Weapon Finesse
- name: Weapon Focus (rapier)
skills:
  Acrobatics: 14
    when jumping: 10
  Bluff: 12
  Craft (alchemy): 15
    when dealing with poison: 19
  Craft (traps): 10
    with poisonous traps: 13
  Disable Device: 9
    with poisonous traps: 12
  Disguise: 7
  Heal: 3
    when dealing with poison: 4
  Knowledge (local): 10
  Perception: 12
    to locate traps: 15
  Sense Motive: 7
  Sleight of Hand: 14
  Stealth: 18
languages:
- Common
- Elven
- Gnome
- Hallit
- Sylvan
special_qualities:
- combine poison 3/day
- master poisoner
- quick poisoning
- rogue talents (combat trick, finesse rogue)
- toxic apothecary +1
- toxic manufactory
- trapster
gear:
  combat:
  - potions of invisibility (2)
  - antitoxin (2)
  - bloodroot (1 dose)
  - drow poison (4 doses)
  - Large scorpion venom (2 doses)
  - Medium spider venom (2 doses)
  - purple worm poison (1 dose)
  - sassone leaf residue (2 doses)
  - shadow essence (2 doses)
  other:
  - +1 mithral chain shirt
  - mwk buckler
  - +1 rapier
  - daggers (12)
  - cloak of resistance +1
  - alchemist's lab
  - mwk thieves' tools
  - 224 gp
special_abilities:
  Combine Poison (Ex): Three times per day, the Daggermark poisoner can combine two
    different poisons without reducing their efficacy, and apply them to the same
    weapon, object, or trap. A creature exposed to the poisons must save against both.
  Master Poisoner (Ex): The Daggermark poisoner's levels in the Daggermark poisoner
    prestige class stack with her rogue levels when determining her bonus on Craft
    (alchemy) checks dealing with poison granted by this ability.
  Quick Poisoning (Ex): The Daggermark poisoner can poison a weapon as a move action.
    She can create poisons with the Craft (alchemy) skill in half the normal amount
    of time.
  Toxic Apothecary (Ex and Sp): The Daggermark poisoner can use detect poison at will
    (range 5 feet) as a swift action. She gains a bonus equal to half her Daggermark
    poisoner level on Heal checks dealing with poison, and on a successful check she
    adds this bonus to the saving throw bonus she provides her patient against the
    treated poison.
  Toxic Manufactory (Ex): When creating poisons or antitoxins, the Daggermark poisoner
    can create a number of doses equal to her Intelligence modifier at one time (minimum
    1). These additional doses do not increase the time required, but do increase
    the raw material cost accordingly. In addition, she uses the item's gp value as
    its sp value when determining progress made with her Craft (alchemy) checks.
  Trapster (Ex): The Daggermark poisoner adds her class level on Perception skill
    checks made to locate traps and on Craft and Disable Device checks regarding poisonous
    traps. She also adds a +1 bonus on attack rolls, save DCs, and Perception and
    Disable Device DCs for poisoned traps she creates.
desc_long: Poison is widely used throughout the Inner Sea and across Golarion, but
  the Daggermark Poisoners' Guild produces artists of toxins. The guild is closely
  allied with the Daggermark Assassins' Guild, and it's rumored that the founder killed
  the last king of Daggermark.

---

# Daggermark Poisoner

**Source** Inner Sea NPC Codex pg. 17
**XP** 3,200
Gnome _[[classes/Rogue|rogue]]_ (poisoner) 5/Daggermark poisoner 3

LE Small humanoid (gnome)
**Init** +7; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +12

##### Defense

**AC** 21, touch 15, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 armor, +3 Dex, +1 dodge, +1 _[[spells/Shield|shield]]_, +1 size); +4 _dodge_ vs. giants
**hp** 60 (8 HD; 5d8+3d8+21)
**Fort** +6, **Ref** +9, **Will** +2; +2 vs. illusions, +2 vs. poison
**Defensive Abilities** evasion, poison _[[universal monster rules/Resistance|resistance]]_ +2, uncanny _dodge_

##### Offense
**Speed** 20 ft.
**Melee** +1 _[[items/Weapon/Rapier|rapier]]_ +11 (1d4+2/18–20 plus poison)
**Ranged** _[[items/Weapon/Dagger|dagger]]_ +9 (1d3+1/19–20 plus poison)
**Special Attacks** +1 on attack rolls against goblinoid and reptilian humanoids, poison use, sneak attack +3d6
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 3rd)
At will—_[[spells/Detect Poison|detect poison]]_ (range 5 feet, swift action)
 **Gnome _Spell-Like Abilities_** (CL 8th)
 1/day—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 11), _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Speak with Animals|speak with animals]]_

##### Statistics
**Str** 12, **Dex** 16, **Con** 14, **Int** 14, **Wis** 8, **Cha** 12
**Base Atk** +5; **CMB** +5; **CMD** 19
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _Dodge_, _[[feats/Improved Feint|Improved Feint]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_rapier_)
**Skills** Acrobatics +14 (+10 when jumping), Bluff +12, Craft (alchemy) +15 (+19 when dealing with poison), Craft (traps) +10 (+13 with poisonous traps), Disable Device +9 (+12 with poisonous traps), Disguise +7, _[[spells/Heal|Heal]]_ +3 (+4 when dealing with poison), Knowledge (local) +10, Perception +12 (+15 to locate traps), Sense Motive +7, Sleight of Hand +14, Stealth +18
**Languages** Common, Elven, Gnome, Hallit, Sylvan
**SQ** combine poison 3/day, master poisoner, quick _[[items/Armor Magic Abilities/Poisoning|poisoning]]_, _rogue_ talents (combat trick, finesse _rogue_), _[[items/Weapon Magic Abilities/Toxic|toxic]]_ apothecary +1, _toxic_ manufactory, trapster
**Combat Gear** potions of _[[spells/Invisibility|invisibility]]_ (2), _[[items/Mundane/Antitoxin|antitoxin]]_ (2), _[[poisons/Bloodroot|bloodroot]]_ (1 dose), _[[poisons/Drow poison|drow poison]]_ (4 doses), _[[poisons/Large Scorpion Venom|Large scorpion venom]]_ (2 doses), _[[poisons/Medium Spider Venom|Medium spider venom]]_ (2 doses), _[[poisons/Purple Worm Poison|purple worm poison]]_ (1 dose), sassone leaf residue (2 doses), _[[poisons/Shadow Essence|shadow essence]]_ (2 doses); **Other Gear** +1 mithral _[[items/Armor/Chain shirt|chain shirt]]_, mwk _[[items/Armor/Buckler|buckler]]_, +1 _rapier_, daggers (12), _[[items/Wondrous Item/Cloak of _Resistance_ +1|cloak of _resistance_ +1]]_, _[[classes/Alchemist|alchemist]]_’s lab, mwk thieves’ tools, 224 gp

### Special Abilities

**Combine Poison (Ex)** Three times per day, the _[[npcs/Daggermark Poisoner|Daggermark poisoner]]_ can combine two different poisons without reducing their efficacy, and apply them to the same weapon, object, or trap. A creature exposed to the poisons must save against both.

**Master Poisoner (Ex)** The _Daggermark poisoner_’s levels in the _Daggermark poisoner_ prestige class stack with her _rogue_ levels when determining her bonus on Craft (alchemy) checks dealing with poison granted by this ability.

**Quick _Poisoning_ (Ex)** The _Daggermark poisoner_ can poison a weapon as a move action. She can create poisons with the Craft (alchemy) skill in half the normal amount of time.

**_Toxic_ Apothecary (Ex and Sp)** The _Daggermark poisoner_ can use _detect poison_ at will (range 5 feet) as a swift action. She gains a bonus equal to half her _Daggermark poisoner_ level on _Heal_ checks dealing with poison, and on a successful check she adds this bonus to the saving throw bonus she provides her patient against the treated poison.

**_Toxic_ Manufactory (Ex)** When creating poisons or antitoxins, the _Daggermark poisoner_ can create a number of doses equal to her Intelligence modifier at one time (minimum 1). These additional doses do not increase the time required, but do increase the raw material cost accordingly. In addition, she uses the item’s gp value as its sp value when determining progress made with her Craft (alchemy) checks.

**Trapster (Ex)** The _Daggermark poisoner_ adds her class level on Perception skill checks made to locate traps and on Craft and Disable Device checks regarding poisonous traps. She also adds a +1 bonus on attack rolls, save DCs, and Perception and Disable Device DCs for poisoned traps she creates.

Poison is widely used throughout the Inner Sea and across Golarion, but the Daggermark Poisoners’ Guild produces artists of toxins. The guild is closely allied with the Daggermark Assassins’ Guild, and it’s rumored that the founder killed the last _[[npcs/King|king]]_ of Daggermark.