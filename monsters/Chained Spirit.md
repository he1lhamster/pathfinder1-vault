---
cssclass: [monsters]
title1: Chained Spirit
desc_short: This humanoid figure's body fades into mist below the hips, while its
  upper, ghostly torso is bound in lengths of writhing chains.
title2: Chained Spirit
CR: 14
sources:
- name: Curse of the Crimson Throne (PFRPG)
  page: 468
  link: http://paizo.com/products/btpy9nme?Pathfinder-Adventure-Path-Curse-of-the-Crimson-Throne
- name: 'Pathfinder #11: Skeletons of Scarwall'
  page: 78
  link: http://paizo.com/pathfinder/adventurePath/curseOfTheCrimsonThrone/v5748btpy83yw
XP: 38400
alignment: LE
size: Medium
type: undead
subtypes:
- incorporeal
initiative:
  bonus: 8
senses:
  darkvision: 60
  spectral sight: true
  spiritsense: true
AC:
  AC: 30
  touch: 30
  flat_footed: 26
  components:
    deflection: 8
    dex: 4
    profane: 8
HP:
  HP: 200
  long: 16d8+128
  fast_healing: 20
saves:
  fort: 13
  ref: 11
  will: 17
defensive_abilities:
- incorporeal
- spirit anchor
immunities:
- positive energy
- undead traits
speeds:
  fly: 60
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: incorporeal touch +17 (1d6 Charisma drain)
      entries:
      - - damage: 1d6
          type: Charisma drain
      attack: incorporeal touch
      bonus:
      - 17
    - text: 4 chains +23 (2d4+7/19-20 plus 1 Charisma drain)
      entries:
      - - damage: 2d4+7
          crit_range: 19-20
        - damage: '1'
          type: Charisma drain
      count: 4
      attack: chains
      bonus:
      - 23
  special:
  - 5 ft. (30 ft. with chains)
space: 5
reach: 5
reach_other: 30 ft. with chains
ability_scores:
  STR:
  DEX: 19
  CON:
  INT: 15
  WIS: 20
  CHA: 27
BAB: 12
CMB: 16
CMD: 42
feats:
- name: Combat Expertise
- name: Combat Reflexes
- name: Improved Critical (chain)
- name: Improved Initiative
- name: Iron Will
- name: Lightning Reflexes
- name: Skill Focus (Perception)
- name: Weapon Focus (incorporeal touch)
skills:
  Bluff: 24
  Diplomacy: 24
  Fly: 31
  Knowledge (history): 18
  Perception: 30
  Stealth: 23
languages:
- Common
- Necril
special_qualities:
- spectral bindings
ecology:
  environment: any
  organization: solitary plus up to 4 spirit anchors
  treasure_type: standard
special_abilities:
  Chain Spirit (Su): As a standard action once per day, a chained spirit can attempt
    to chain any evil-aligned corporeal creature with an Intelligence score of 3 or
    higher that it can detect via spiritsense; it need not have line of sight or line
    of effect to such a creature. The targeted evil creature to must succeed at a
    DC 25 Will save or take 1d8 points of Charisma drain. On each successful attack,
    the chained spirit gains 5 temporary hit points. Any creature targeted by this
    ability is immediately aware of some malevolence attempting to take control of
    it. If a creature's Charisma score is drained to 0 by this attack, its fate depends
    on its Hit Dice. If the victim has half the Hit Dice or fewer of the chained spirit
    (8 Hit Dice for most chained spirits), it is slain by the attack. If the victim
    has more than 8 Hit Dice, it becomes a spirit anchor linked to the chained spirit
    (see below). Even though a chained spirit can use this ability once per day, it
    can create only one spirit anchor per week. In addition, a chained spirit can
    use this ability only if it currently has three or fewer spirit anchors, and it
    can never have more than four spirit anchors. A creature with more than half the
    chained spirit's Hit Dice whose Charisma score is drained to 0 by this attack
    and who doesn't become a spirit anchor is merely driven unconscious, as per normal
    for catastrophic Charisma drain. The save DC is Charisma-based.
  '': Numerous chains extend from a chained spirit. A number of these (one for every
    spirit anchor currently tethered to the chained spirit) are corporeal and can
    make melee attacks. These corporeal chains are treated as evil, magical, ghost
    touch weapons and deal bludgeoning damage in addition to Charisma drain. Each
    chain is treated as if wielded one-handed by a creature with a Strength score
    of 25. A sundered chain automatically reforms 1 round later.
  Charisma Drain (Su): Any creature hit by a chained spirit's chains or incorporeal
    touch attack must succeed at a DC 25 Will save or take Charisma drain (1 point
    if struck by a chain, or 1d6 points if struck by a touch attack). The save DC
    is Charisma-based.
  Create Spawn (Su): Any humanoid slain by a chained spirit becomes a spectre in 1d4
    rounds. These spawn are under the command of the chained spirit that created them
    and remain enslaved until its death. They don't have any of the abilities they
    had in life.
  Spectral Bindings (Su): 'A chained spirit is extremely mobile, with only one major
    hindrance: no matter how far it moves on its turn, as long as it has at least
    one spirit anchor, it automatically returns to its starting place when its turn
    ends. This immediate return does not count as an action and does not provoke attacks
    of opportunity, as the spirit simply reappears back in its original position.
    In essence, the chained spirit is eternally confined to a single square throughout
    its existence except the distance it can travel in a single round before returning
    to its starting position. If another creature occupies the space it has left,
    that creature is shunted to the closest available square. If a solid object occupies
    its starting square, the spirit's incorporeal nature allows it to return regardless.
    Even a force effect cannot thwart it as it simply reappears within the square,
    though if that square is surrounded by a force effect with no exit, the chained
    spirit is effectively trapped. Spectral Sight (Su) A chained spirit can see and
    hear through the senses of any of its spirit anchors whenever it wishes, just
    as if it were using both effects of clairaudience/clairvoyance.'
  Spiritsense (Su): A chained spirit can detect both the living and the undead. It
    can detect living creatures within 100 feet, just as if it had blindsight. It
    can also sense the dead, as per detect undead, to a range of 500 feet.
desc_long: |-
  A chained spirit is the tormented soul of one who was charged, cursed, or honor-bound to guard a certain place or object, only to be slain in the course of such duty. Such a dishonored spirit returns as a misty approximation of its living form, except now burdened by loops of constricting chains and inescapable locks, all representing its bonds of duty. Reaching out with these chains, these tormented undead claim allies, binding other unwilling sentinels to the same charge with which they are eternally cursed.

   Among the rarest known manifestations of undead, the chained spirit can exist only in an area of extreme misery combined with a potent source of necromantic energy. In the case of Scarwall, the castle's history of violence, combined with the vengeful attention of Zon-Kuthon, made the castle the perfect cradle for the generation of a chained spirit. Others may well exist on Golarion, or could yet come to manifest, but at this point, the chained spirit of Scarwall may be the only one of its kind.

---

# Chained Spirit
This humanoid figure’s body fades into mist below the hips, while its upper, ghostly torso is bound in lengths of writhing chains.
**Source** Curse of the Crimson Throne (PFRPG) pg. 468, Pathfinder #11: Skeletons of Scarwall pg. 78
**XP** 38,400

LE Medium undead (_[[universal monster rules/Incorporeal|incorporeal]]_)
**Init** +8; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., spectral sight, spiritsense; Perception +30

##### Defense

**AC** 30, touch 30, _[[conditions/Flat-Footed|flat-footed]]_ 26 (+8 _[[spells/Deflection|deflection]]_, +4 Dex, +8 profane)
**hp** 200 (16d8+128); _[[universal monster rules/Fast Healing|fast healing]]_ 20
**Fort** +13, **Ref** +11, **Will** +17
**Defensive Abilities** _incorporeal_, spirit anchor; **Immune** positive energy, _[[universal monster rules/Undead Traits|undead traits]]_

##### Offense
**Speed** fly 60 ft. (perfect)
**Melee** _incorporeal_ touch +17 (1d6 Charisma drain), 4 chains +23 (2d4+7/19–20 plus 1 Charisma drain)
**Space** 5 ft., **Reach** 5 ft. (30 ft. with chains)
**Special Attacks** 5 ft. (30 ft. with chains)

##### Statistics
**Str** —, **Dex** 19, **Con** —, **Int** 15, **Wis** 20, **Cha** 27
**Base Atk** +12; **CMB** +16; **CMD** 42
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Improved Critical|Improved Critical]]_ (chain), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Skill Focus|Skill Focus]]_ (Perception), _[[feats/Weapon Focus|Weapon Focus]]_ (_incorporeal_ touch)
**Skills** Bluff +24, Diplomacy +24, Fly +31, Knowledge (history) +18, Perception +30, Stealth +23
**Languages** Common, Necril
**SQ** spectral bindings

##### Ecology

**Environment** any
**Organization** solitary plus up to 4 spirit anchors
**Treasure** standard

### Special Abilities

**Chain Spirit (Su)** As a standard action once per day, a _[[monsters/Chained Spirit|chained spirit]]_ can attempt to chain any evil-aligned corporeal creature with an Intelligence score of 3 or higher that it can detect via spiritsense; it need not have line of sight or line of effect to such a creature. The targeted evil creature to must succeed at a DC 25 Will save or take 1d8 points of Charisma drain. On each successful attack, the _chained spirit_ gains 5 temporary hit points. Any creature targeted by this ability is immediately aware of some malevolence attempting to take control of it. If a creature’s Charisma score is drained to 0 by this attack, its fate depends on its Hit Dice. If the victim has half the Hit Dice or fewer of the _chained spirit_ (8 Hit Dice for most chained spirits), it is slain by the attack. If the victim has more than 8 Hit Dice, it becomes a spirit anchor linked to the _chained spirit_ (see below). Even though a _chained spirit_ can use this ability once per day, it can create only one spirit anchor per week. In addition, a _chained spirit_ can use this ability only if it currently has three or fewer spirit anchors, and it can never have more than four spirit anchors. A creature with more than half the _chained spirit_’s Hit Dice whose Charisma score is drained to 0 by this attack and who doesn’t become a spirit anchor is merely driven _[[conditions/Unconscious|unconscious]]_, as per normal for catastrophic Charisma drain. The save DC is Charisma-based.

Numerous chains extend from a _chained spirit_. A number of these (one for every spirit anchor currently tethered to the _chained spirit_) are corporeal and can make melee attacks. These corporeal chains are treated as evil, magical, _[[items/Weapon Magic Abilities/Ghost Touch|ghost touch]]_ weapons and deal bludgeoning damage in addition to Charisma drain. Each chain is treated as if wielded one-handed by a creature with a Strength score of 25. A sundered chain automatically reforms 1 round later.

**Charisma Drain (Su)** Any creature hit by a _chained spirit_’s chains or _incorporeal_ touch attack must succeed at a DC 25 Will save or take Charisma drain (1 point if struck by a chain, or 1d6 points if struck by a touch attack). The save DC is Charisma-based.

**Create Spawn (Su)** Any humanoid slain by a _chained spirit_ becomes a _[[monsters/Spectre|spectre]]_ in 1d4 rounds. These spawn are under the _[[spells/Command|command]]_ of the _chained spirit_ that created them and remain enslaved until its death. They don’t have any of the abilities they had in life.
**Spectral Bindings (Su)** A _chained spirit_ is extremely mobile, with only one major hindrance: no matter how far it moves on its turn, as long as it has at least one spirit anchor, it automatically returns to its starting place when its turn ends. This immediate return does not count as an action and does not provoke attacks of opportunity, as the spirit simply reappears back in its original position. In essence, the _chained spirit_ is eternally confined to a single square throughout its existence except the distance it can travel in a single round before returning to its starting position. If another creature occupies the space it has left, that creature is shunted to the closest available square. If a solid object occupies its starting square, the spirit’s _incorporeal_ nature allows it to return regardless. Even a force effect cannot thwart it as it simply reappears within the square, though if that square is surrounded by a force effect with no exit, the _chained spirit_ is effectively trapped. Spectral Sight (Su) A _chained spirit_ can see and hear through the senses of any of its spirit anchors whenever it wishes, just as if it were using both effects of clairaudience/clairvoyance.
**Spiritsense (Su)** A _chained spirit_ can detect both the living and the undead. It can detect living creatures within 100 feet, just as if it had _[[universal monster rules/Blindsight|blindsight]]_. It can also sense the dead, as per _[[spells/Detect Undead|detect undead]]_, to a range of 500 feet.

##### Description

A _chained spirit_ is the tormented soul of one who was charged, cursed, or honor-bound to _[[npcs/Guard|guard]]_ a certain place or object, only to be slain in the course of such duty. Such a dishonored spirit returns as a misty approximation of its living form, except now burdened by loops of constricting chains and inescapable locks, all representing its bonds of duty. Reaching out with these chains, these tormented undead claim allies, _[[spells/Binding|binding]]_ other unwilling sentinels to the same charge with which they are eternally cursed.

Among the rarest known manifestations of undead, the _chained spirit_ can exist only in an area of extreme misery combined with a _[[items/Weapon Magic Abilities/Potent|potent]]_ source of necromantic energy. In the case of Scarwall, the castle’s history of violence, combined with the vengeful attention of Zon-Kuthon, made the castle the perfect cradle for the generation of a _chained spirit_. Others may well exist on Golarion, or could yet come to manifest, but at this point, the _chained spirit_ of Scarwall may be the only one of its kind.