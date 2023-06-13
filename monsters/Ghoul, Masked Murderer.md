---
cssclass: [monsters]
title1: Ghoul, Masked Murderer
title2: Masked Murderer
CR: 8
sources:
- name: Monster Codex
  page: 85
  link: http://paizo.com/products/btpy9926?Pathfinder-Roleplaying-Game-Monster-Codex
XP: 4800
race: Ghoul
classes:
- bard (dirge bard) 8 (Pathfinder RPG Ultimate Magic 26)
alignment: CE
size: Medium
type: undead
initiative:
  bonus: 7
senses:
  darkvision: 60
AC:
  AC: 20
  touch: 13
  flat_footed: 17
  components:
    armor: 5
    dex: 3
    natural: 2
HP:
  HP: 113
  long: 10d8+68
saves:
  fort: 8
  ref: 9
  will: 11
  other: +4 vs. necromantic effects
defensive_abilities:
- channel resistance +2
immunities:
- undead traits
speeds:
  base: 30
attacks:
  melee:
  - - text: bite +10 (1d6+2 plus disease and paralysis)
      entries:
      - - damage: 1d6+2
        - effect: disease
        - effect: paralysis
      attack: bite
      bonus:
      - 10
    - text: 2 claws +11 (1d6+2 plus paralysis)
      entries:
      - - damage: 1d6+2
        - effect: paralysis
      count: 2
      attack: claws
      bonus:
      - 11
  ranged:
  - - text: mwk composite shortbow +11/+6 (1d6+2/×3)
      entries:
      - - damage: 1d6+2
          crit_multiplier: 3
      attack: mwk composite shortbow
      bonus:
      - 11
      - 6
  special:
  - bardic performance 24 rounds/day (move action; countersong, dirge of doom [DC
    20], distraction, fascinate [DC 20], inspire competence +3, inspire courage +2,
    suggestion [DC 20])
  - disease (DC 17)
  - paralysis (1d4+1 rounds, DC 19, elves are immune to this effect)
spells:
  entries:
  - name: confusion
    source: Bard
    level: 3
    DC: 19
  - name: crushing despair
    source: Bard
    level: 3
    DC: 19
  - name: glibness
    source: Bard
    level: 3
  - superscripts:
    - UM
    name: allegro
    source: Bard
    level: 2
  - name: fleshy facade
    source: Bard
    level: 2
    DC: 18
  - name: inflict moderate wounds
    source: Bard
    level: 2
    DC: 18
  - name: mirror image
    source: Bard
    level: 2
  - name: disguise self
    source: Bard
    level: 1
  - name: expeditious retreat
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 17
  - name: ray of enfeeblement
    source: Bard
    level: 1
    DC: 17
  - name: silent image
    source: Bard
    level: 1
    DC: 17
  - name: detect magic
    source: Bard
    level: 0
  - name: ghost sound
    source: Bard
    level: 0
    DC: 16
  - name: mage hand
    source: Bard
    level: 0
  - name: message
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
    DC: 16
  - name: summon instrument
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 8
    concentration: 14
    slots:
      3: 3
      2: 6
      1: 6
      0: at-will
tactics:
  Before Combat: This furtive killer disguises herself as a human while stalking her
    targets. If at all possible, she avoids conflict, though her hunger sometimes
    gets the best of her.
  During Combat: If her presence is detected, the murderer begins combat by casting
    confusion. She then starts a bardic performance (typically dirge of doom). Before
    she actually enters melee, she casts allegro to gain additional attacks.
ability_scores:
  STR: 15
  DEX: 17
  CON:
  INT: 17
  WIS: 14
  CHA: 22
BAB: 7
CMB: 9
CMD: 22
feats:
- name: Ability Focus (paralysis)
- name: Combat Casting
- name: Improved Initiative
- name: Weapon Finesse
- name: Weapon Focus (claw)
skills:
  Bluff: 19
  Diplomacy: 19
  Disguise: 19
  Intimidate: 19
  Knowledge (arcana): 16
  Knowledge (local): 20
  Knowledge (religion): 15
    to identify undead creatures and their abilities: 19
  Perception: 15
  Perform (oratory): 14
  Perform (percussion): 19
  _racial_mods:
    Knowledge (religion):
      to identify undead creatures and their abilities: 4
languages:
- Common
- Dwarven
- Elven
- Undercommon
special_qualities:
- bardic knowledge +4
- haunting refrain (+4 to demoralize, -2 penalty on saves against bard's fear effects)
- secrets of the grave
gear:
  combat:
  - +1 thundering arrows (4)
  - potion of invisibility
  - scroll of hold person
  - wand of inflict light wounds (50 charges)
  other:
  - +1 chain shirt
  - mwk composite shortbow with 10 arrows
  - headband of alluring charisma +2
  - disguise kit
  - 10 gp
ecology:
  environment: any land
desc_long: |-
  The masked murderer uses deception to get closer to her human prey, mingling among them without arousing their suspicion until it is too late for them to escape her clutches. Magic, particularly the fleshy facade spell, allows her to craft her deceptive appearance, and she knows how to disguise herself using mundane means so that she can at least hide her gruesomeness long enough to get to safety if her magic fails her.

   Charm and lies pave the murderer's way through society. Typically, she begins small, making friends with low-class workers or farmers in taverns and alleyways, then luring them away to kill and devour them. This is rarely enough for a masked murderer, though, and in time she makes connections among the elite. This could be to satisfy her ego, but more often she wants to dine on the finer morsels of spoiled elites rather than the tough flesh of hard laborers.

   Unfortunately for ghouls, spending so much time among the living serves only to highlight the life they traded away for the unending hunger of their undead existence. Many masked murderers find themselves conf licted as a result, envying the vibrant lives of their prey. In the end, however, a masked murderer's ghoulish hunger always overwhelms any other emotion she might feel, and she hunts her prey with as much ravenous fervor as any other ghoul, if not more.

---

# Ghoul, Masked Murderer

**Source** Monster Codex pg. 85
**XP** 4,800
_[[monsters/Ghoul|Ghoul]]_ _[[classes/Bard|bard]]_ (dirge _bard_) 8 (Pathfinder RPG Ultimate Magic 26)
CE Medium undead
**Init** +7; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft.; Perception +15

##### Defense

**AC** 20, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 17 (+5 armor, +3 Dex, +2 natural)
**hp** 113 (10d8+68)
**Fort** +8, **Ref** +9, **Will** +11; +4 vs. necromantic effects
**Defensive Abilities** _[[universal monster rules/Channel Resistance|channel resistance]]_ +2; **Immune** _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** 30 ft.
**Melee** bite +10 (1d6+2 plus disease and _[[universal monster rules/Paralysis|paralysis]]_), 2 claws +11 (1d6+2 plus _paralysis_)
**Ranged** mwk _[[items/Weapon/Composite shortbow|composite shortbow]]_ +11/+6 (1d6+2/×3)
**Special Attacks** bardic performance 24 rounds/day (move action; countersong, dirge of _[[spells/Doom|doom]]_ [DC 20], _[[universal monster rules/Distraction|distraction]]_, fascinate [DC 20], inspire competence +3, inspire courage +2, _[[spells/Suggestion|suggestion]]_ [DC 20]), disease (DC 17), _paralysis_ (1d4+1 rounds, DC 19, elves are immune to this effect)
**_Bard_ Spells Known **(CL 8th; concentration +14)
3rd (3/day)—_[[spells/Confusion|confusion]]_ (DC 19), _[[spells/Crushing Despair|crushing despair]]_ (DC 19), _[[spells/Glibness|glibness]]_
2nd (6/day)—_[[spells/Allegro|allegro]]_, _[[spells/Fleshy Facade|fleshy facade]]_ (DC 18), _[[spells/Inflict Moderate Wounds|inflict moderate wounds]]_ (DC 18), _[[spells/Mirror Image|mirror image]]_
1st (6/day)—_[[spells/Disguise Self|disguise self]]_, _[[spells/Expeditious Retreat|expeditious retreat]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 17), _[[spells/Ray Of Enfeeblement|ray of enfeeblement]]_ (DC 17), _[[spells/Silent Image|silent image]]_ (DC 17)
0 (at will)—_[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 16), _[[spells/Mage Hand|mage hand]]_, _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_ (DC 16), _[[spells/Summon Instrument|summon instrument]]_

### Tactics

**Before Combat** This furtive killer disguises herself as a human while _[[items/Weapon Magic Abilities/Stalking|stalking]]_ her targets. If at all possible, she avoids conflict, though her hunger sometimes gets the best of her.
 **During Combat** If her presence is detected, the murderer begins combat by casting _confusion_. She then starts a bardic performance (typically dirge of _doom_). Before she actually enters melee, she casts _allegro_ to gain additional attacks.

##### Statistics
**Str** 15, **Dex** 17, **Con** —, **Int** 17, **Wis** 14, **Cha** 22
**Base Atk** +7; **CMB** +9; **CMD** 22
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (_paralysis_), _[[feats/Combat Casting|Combat Casting]]_, _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Weapon Finesse|Weapon Finesse]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (claw)
**Skills** Bluff +19, Diplomacy +19, Disguise +19, Intimidate +19, Knowledge (arcana) +16, Knowledge (local) +20, Knowledge (religion) +15 (+19 to _[[spells/Identify|identify]]_ undead creatures and their abilities), Perception +15, Perform (oratory) +14, Perform (percussion) +19; **Racial Modifiers** +4 Knowledge (religion) to _identify_ undead creatures and their abilities
**Languages** Common, Dwarven, Elven, Undercommon
**SQ** bardic knowledge +4, haunting refrain (+4 to demoralize, –2 penalty on saves against _bard_’s _[[universal monster rules/Fear|fear]]_ effects), secrets of the grave
**Combat Gear** +1 _[[items/Weapon Magic Abilities/Thundering|thundering]]_ arrows (4), potion of _[[spells/Invisibility|invisibility]]_, scroll of _[[spells/Hold Person|hold person]]_, wand of _[[spells/Inflict Light Wounds|inflict light wounds]]_ (50 charges); **Other Gear** +1 _[[items/Armor/Chain shirt|chain shirt]]_, mwk _composite shortbow_ with 10 arrows, _[[items/Wondrous Item/Headband of Alluring Charisma +2|headband of alluring charisma +2]]_, _[[items/Mundane/Disguise kit|disguise kit]]_, 10 gp

##### Ecology

**Environment** any land

##### Description

The masked murderer uses deception to get closer to her human prey, mingling among them without arousing their suspicion until it is too late for them to escape her clutches. Magic, particularly the _fleshy facade_ spell, allows her to craft her _[[items/Weapon Magic Abilities/Deceptive|deceptive]]_ appearance, and she knows how to disguise herself using mundane means so that she can at least hide her gruesomeness long enough to get to safety if her magic fails her.

Charm and lies pave the murderer’s way through society. Typically, she begins small, making friends with low-class workers or farmers in taverns and alleyways, then luring them away to kill and devour them. This is rarely enough for a masked murderer, though, and in time she makes connections among the elite. This could be to satisfy her ego, but more often she wants to dine on the finer morsels of spoiled elites rather than the tough flesh of hard laborers.

Unfortunately for ghouls, spending so much time among the living serves only to highlight the life they traded away for the unending hunger of their undead existence. Many masked murderers find themselves conf licted as a result, envying the vibrant lives of their prey. In the end, however, a masked murderer’s ghoulish hunger always overwhelms any other emotion she might feel, and she hunts her prey with as much _[[curses/Ravenous|ravenous]]_ fervor as any other _ghoul_, if not more.