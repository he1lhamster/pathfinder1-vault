---
cssclass: [monsters]
title1: Automaton, Sharpshooter Automaton
desc_short: This construct resembles a humanoid with a large crossbow built into its
  arm. It floats with no apparent mechanism.
title2: Sharpshooter Automaton
CR: 15
sources:
- name: Construct Handbook
  page: 28
  link: https://paizo.com/products/btq01vam
XP: 51200
alignment: LN
size: Medium
type: construct
subtypes:
- automaton
- extraplanar
initiative:
  bonus: 9
senses:
  darkvision: 120
  low-light vision: true
  see invisibility: true
AC:
  AC: 29
  touch: 14
  flat_footed: 25
  components:
    dex: 4
    natural: 15
HP:
  HP: 130
  long: 20d10+20
  fast_healing: 10
saves:
  fort: 6
  ref: 14
  will: 10
defensive_abilities:
- all-around vision
- sharpshooter's sense
DR:
- amount: 15
  weakness: adamantine
immunities:
- construct traits
- electricity
resistances:
  cold: 10
  sonic: 10
SR: 26
weaknesses:
- vulnerable mind
speeds:
  fly: 100
  fly_maneuverability: perfect
attacks:
  melee:
  - - text: slam +24 (1d8+6)
      entries:
      - - damage: 1d8+6
      attack: slam
      bonus:
      - 24
  ranged:
  - - text: automated crossbow +25/+20/+15/+10 (2d8+6/17-20 plus 1d6 fire)
      entries:
      - - damage: 2d8+6
          crit_range: 17-20
        - damage: 1d6
          type: fire
      attack: automated crossbow
      bonus:
      - 25
      - 20
      - 15
      - 10
  special:
  - arcane propulsion
  - bolt volley
  - energy beam
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - name: hold person
    source: default
    freq: At will
    DC: 16
  - name: mirror image
    source: default
    freq: At will
  - name: web
    source: default
    freq: At will
    DC: 16
  - name: chain lightning
    source: default
    freq: 3/day
    DC: 20
  - name: wall of force
    source: default
    freq: 3/day
  - name: plane shift
    source: default
    freq: 1/day
    other: self plus 50 lbs. of objects only
  - name: reverse gravity
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 20
    concentration: 24
ability_scores:
  STR: 18
  DEX: 20
  CON:
  INT: 17
  WIS: 19
  CHA: 18
BAB: 20
CMB: 24
CMD: 40
feats:
- name: Far Shot
- name: Hover
- name: Improved Critical (automated crossbow)
- name: Improved Initiative
- name: Improved Precise Shot
- name: Manyshot
- name: Pinpoint Targeting
- name: Point-Blank Shot
- name: Precise Shot
- name: Rapid Shot
skills:
  Diplomacy: 27
  Fly: 36
  Intimidate: 27
  Knowledge (geography): 26
  Knowledge (local): 26
  Perception: 27
  Spellcraft: 26
languages:
- Abyssal
- Celestial
- Common
- telepathy 100 ft.
special_qualities:
- automaton core
- intelligent construct
ecology:
  environment: any (Axis)
  organization: solitary or pair
  treasure:
  - automated crossbow
special_abilities:
  Arcane Propulsion (Su): A sharpshooter automaton flies using arcane energy that
    radiates out from itself. A creature that ends its turn adjacent to a sharpshooter
    automaton takes 2d8 points of fire damage.
  Automated Crossbow (Ex): A sharpshooter automaton's automated crossbow is treated
    as a Large +2 flaming heavy crossbow. The powerful weapon is treated as a siege
    weapon for the purposes of wind effects, wind wall, and similar effects. While
    the crossbow is built into the automaton, the automaton adds its Strength bonus
    as a bonus on damage rolls and reloads as a free action.
  Bolt Volley (Ex): As a standard action, a sharpshooter automaton can fire a spray
    of arrows that covers a 30-foot-radius area. If it uses a full-round action, the
    size of the area increases to a 50-foot radius. It makes a single attack roll
    against all creatures in the area using its highest base attack bonus at a -4
    penalty. Each creature struck takes 6d8 points of damage plus 1d6 points of fire
    damage. The sharpshooter automaton can use this attack once every 1d4 rounds as
    it must regenerate its ammunition, but it can continue to use its automated crossbow
    as normal during this time.
  Energy Beam (Ex): A sharpshooter automaton can focus the energy in its core to make
    a ranged touch attack against a creature within 120 feet as a standard action.
    The beam deals 15d6 points of damage on a hit; half of this damage is fire damage
    and half is force damage. Upon striking its target, the energy beam explodes in
    a 10-foot-radius burst. Creatures in the explosion area, including the original
    target, take 10d6 points of fire damage (Reflex DC 24 half). The sharpshooter
    automaton can use its energy beam once every 1d4 rounds. The save DC is Wisdom-based.
  Sharpshooter's Sense (Ex): A sharpshooter automaton's core is instilled with a knack
    for combat awareness, granting it all-around vision. Additionally, it adds its
    Wisdom modifier as a bonus on Reflex saves.
desc_long: |-
  Sharpshooter automatons contain the minds of the best archers and crossbow specialists known throughout the Jistka Imperium, who competed in tournaments to earn the right to an automaton body. They served as the artillery of the automatons, attacking enemies with such precision and at such a great distance that many targets fell long before they were aware of an imminent attack.

   Efficiency was the key of the sharpshooter automaton's design. Their frames are just large enough to house the components necessary to power the construct alongside their magical weapons. Though the frames followed a similar pattern of design across these automatons, many sharpshooters chose to embellish their forms with intricate runic patterns or fearsome designs reminiscent of tattoos. A sharpshooter automaton is typically 4 feet tall and weighs 215 pounds. The largest sharpshooter automatons, however, housed extremely large ranged weapons or even siege weapons, such as ballistae capable of destroying a keep's walls.

   A sharpshooter automaton's automaton core directs a considerable amount of its power to the arcane propulsion that allows the construct to fly. This energy appears invisible to the naked eye, but creatures capable of detecting magical auras perceive it as something resembling a magical flame. This propulsion constantly releases excess energy capable of burning creatures too close to the sharpshooter.

   The technology that fuels a sharpshooter's flight similarly powers its weapon. The crossbow built into most sharpshooters siphons planar energy from the automaton core and reconstitutes it to create the large bolts its weapon requires. These bolts allow a sharpshooter automaton to fire enormous volleys without ever lacking ammunition. Once a bolt leaves the automaton's reserve, it becomes relatively unstable, however, and generally dissipates in minutes, returning to the parts of the Great Beyond from which it was drawn.

   Although most sharpshooter automatons use crossbows as their weapon of choice, archers of all kinds volunteered to become the new constructs, as the automaton's expert construction allowed for perfection of an archer's skill. The first sharpshooter automatons took to the skies in early combat, raining death on their enemies, but they soon found that sandstorms and other magical protections rendered an aerial approach ineffective. In time, they eventually learned to overcome such defenses, but as a whole they were too few to shift battles in favor of the Jistka Imperium. Among the most notable of these heroes was Khimar of the High Watch, whose volleys were said to resemble torrential downpours.

   Since the fall of Jistka, the sharpshooter automatons scattered to the winds, intent on finding their own purpose in a world without a land or people they could call their own. Even with their planar abilities, some sharpshooter automatons remained on Golarion. Leveraging the freedom granted by their flight, these automatons can be found around the world, seemingly as wanderers. A number of them act as itinerant saviors, slaying large creatures on the verge of attacking villages or rescuing travelers caught in tough spots. Occasional tales crop up among travelers claiming that they were saved from peril by a rain of bolts, but that when they returned to the site of the rescue hours later, they found nothing. Other sharpshooter automatons keep watch in the skies, hovering thousands of feet in the air over important structures and locations throughout Golarion. While the locations appear random to a modern observer, most of these are places important to the individual automaton or of significance in Jistkan history, such as locations mentioned in the Poleiheira.

   Now, besides those few on the Material Plane, most sharpshooter automatons reside in Axis with others of their kind. However, a few visit the Maelstrom on a regular basis, pushed toward the chaotic uncertainty of these planar depths by some sort of melancholy. These automatons tend to avoid other creatures and keep to themselves, and most proteans know that even in that chaotic realm, the constructs remain quite powerful, and thus keep their distance. Although the automatons in the Maelstrom are few, they are generally quite familiar with their favored region of the plane, and their powerful sight allows them to keep track of the chaos for miles in every direction. Most notable among these self-exiled sharpshooter automatons is Alvara the All-Seer. Those who know of her claim that the millennia through which she has stayed in the Maelstrom allows her to accurately understand and even predict the nature of the chaotic seas in which she resides.

---

# Automaton, Sharpshooter Automaton
This construct resembles a humanoid with a large crossbow built into its arm. It floats with no apparent mechanism.
**Source** Construct Handbook pg. 28
**XP** 51,200

LN Medium construct (automaton, extraplanar)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 120 ft., _[[universal monster rules/Low-Light Vision|low-light vision]]_, _[[spells/See Invisibility|see invisibility]]_; Perception +27

##### Defense

**AC** 29, touch 14, _[[conditions/Flat-Footed|flat-footed]]_ 25 (+4 Dex, +15 natural)
**hp** 130 (20d10+20); _[[universal monster rules/Fast Healing|fast healing]]_ 10
**Fort** +6, **Ref** +14, **Will** +10
**Defensive Abilities** _[[universal monster rules/All-Around Vision|all-around vision]]_, sharpshooter's sense; **DR** 15/adamantine; **Immune** _[[universal monster rules/Construct Traits|construct traits]]_, electricity; **Resist** cold 10, sonic 10; **SR** 26
**Weaknesses** vulnerable mind

##### Offense
**Speed** fly 100 ft. (perfect)
**Melee** slam +24 (1d8+6)
**Ranged** automated crossbow +25/+20/+15/+10 (2d8+6/17-20 plus 1d6 fire)
**Special Attacks** arcane propulsion, bolt volley, energy beam
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 20th; concentration +24)
Constant—_see invisibility_ 
At will—_[[spells/Hold Person|hold person]]_ (DC 16), _[[spells/Mirror Image|mirror image]]_, web (DC 16) 
3/day—_[[spells/Chain Lightning|chain lightning]]_ (DC 20), _[[spells/Wall Of Force|wall of force]]_ 
1/day—_[[spells/Plane Shift|plane shift]]_ (self plus 50 lbs. of objects only), _[[spells/Reverse Gravity|reverse gravity]]_

##### Statistics
**Str** 18, **Dex** 20, **Con** —, **Int** 17, **Wis** 19, **Cha** 18
**Base Atk** +20; **CMB** +24; **CMD** 40
**Feats** _[[feats/Far Shot|Far Shot]]_, _[[feats/Hover|Hover]]_, _[[feats/Improved Critical|Improved Critical]]_ (automated crossbow), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Precise Shot|Improved Precise Shot]]_, _[[feats/Manyshot|Manyshot]]_, _[[feats/Pinpoint Targeting|Pinpoint Targeting]]_, _[[feats/Point-Blank Shot|Point-Blank Shot]]_, _[[feats/Precise Shot|Precise Shot]]_, _[[feats/Rapid Shot|Rapid Shot]]_
**Skills** Diplomacy +27, Fly +36, Intimidate +27, Knowledge (geography) +26, Knowledge (local) +26, Perception +27, Spellcraft +26
**Languages** Abyssal, Celestial, Common; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** _[[items/Wondrous Item/Automaton Core|automaton core]]_, intelligent construct

##### Ecology

**Environment** any (Axis)
**Organization** solitary or pair
**Treasure** automated crossbow

### Special Abilities

**Arcane Propulsion (Su)** A sharpshooter automaton flies using arcane energy that radiates out from itself. A creature that ends its turn adjacent to a sharpshooter automaton takes 2d8 points of fire damage.

**Automated Crossbow (Ex)** A sharpshooter automaton’s automated crossbow is treated as a Large +2 _[[items/Weapon Magic Abilities/Flaming|flaming]]_ _[[items/Weapon/Heavy crossbow|heavy crossbow]]_. The powerful weapon is treated as a siege weapon for the purposes of wind effects, _[[spells/Wind Wall|wind wall]]_, and similar effects. While the crossbow is built into the automaton, the automaton adds its Strength bonus as a bonus on damage rolls and reloads as a free action.

**Bolt Volley (Ex)** As a standard action, a sharpshooter automaton can fire a spray of arrows that covers a 30-foot-radius area. If it uses a full-round action, the size of the area increases to a 50-foot radius. It makes a single attack roll against all creatures in the area using its highest base attack bonus at a –4 penalty. Each creature struck takes 6d8 points of damage plus 1d6 points of fire damage. The sharpshooter automaton can use this attack once every 1d4 rounds as it must _[[spells/Regenerate|regenerate]]_ its ammunition, but it can continue to use its automated crossbow as normal during this time.

**Energy Beam (Ex)** A sharpshooter automaton can focus the energy in its core to make a ranged touch attack against a creature within 120 feet as a standard action. The beam deals 15d6 points of damage on a hit; half of this damage is fire damage and half is force damage. Upon striking its target, the energy beam explodes in a 10-foot-radius burst. Creatures in the explosion area, including the original target, take 10d6 points of fire damage (Reflex DC 24 half). The sharpshooter automaton can use its energy beam once every 1d4 rounds. The save DC is Wisdom-based.
**Sharpshooter’s Sense (Ex)** A sharpshooter automaton’s core is instilled with a knack for combat awareness, granting it _all-around vision_. Additionally, it adds its Wisdom modifier as a bonus on Reflex saves.

##### Description

Sharpshooter automatons contain the minds of the best archers and crossbow specialists known throughout the Jistka Imperium, who competed in tournaments to earn the right to an automaton body. They served as the artillery of the automatons, attacking enemies with such precision and at such a great distance that many targets fell long before they were aware of an imminent attack.

Efficiency was the key of the sharpshooter automaton’s design. Their frames are just large enough to house the components necessary to power the construct alongside their magical weapons. Though the frames followed a similar pattern of design across these automatons, many sharpshooters chose to embellish their forms with intricate runic patterns or fearsome designs reminiscent of tattoos. A sharpshooter automaton is typically 4 feet tall and weighs 215 pounds. The largest sharpshooter automatons, however, housed extremely large ranged weapons or even siege weapons, such as ballistae capable of destroying a keep’s walls.

A sharpshooter automaton’s _automaton core_ directs a considerable amount of its power to the arcane propulsion that allows the construct to fly. This energy appears _[[conditions/Invisible|invisible]]_ to the naked eye, but creatures capable of detecting magical auras perceive it as something resembling a magical flame. This propulsion constantly releases excess energy capable of _[[items/Weapon Magic Abilities/Burning|burning]]_ creatures too close to the sharpshooter.

The technology that fuels a sharpshooter’s _[[universal monster rules/Flight|flight]]_ similarly powers its weapon. The crossbow built into most sharpshooters siphons _[[items/Weapon Magic Abilities/Planar|planar]]_ energy from the _automaton core_ and reconstitutes it to create the large bolts its weapon requires. These bolts allow a sharpshooter automaton to fire enormous volleys without ever lacking ammunition. Once a bolt leaves the automaton’s reserve, it becomes relatively unstable, however, and generally dissipates in minutes, returning to the parts of the Great Beyond from which it was drawn.

Although most sharpshooter automatons use crossbows as their weapon of choice, archers of all kinds volunteered to become the new constructs, as the automaton’s expert construction allowed for perfection of an archer’s skill. The first sharpshooter automatons took to the skies in early combat, raining death on their enemies, but they soon found that sandstorms and other magical protections rendered an aerial approach ineffective. In time, they eventually learned to overcome such defenses, but as a whole they were too few to shift battles in favor of the Jistka Imperium. Among the most notable of these heroes was Khimar of the High Watch, whose volleys were said to resemble torrential downpours.

Since the fall of Jistka, the sharpshooter automatons scattered to the winds, intent on finding their own purpose in a world without a land or people they could call their own. Even with their _planar_ abilities, some sharpshooter automatons remained on Golarion. _[[items/Weapon Magic Abilities/Leveraging|Leveraging]]_ the _[[spells/Freedom|freedom]]_ granted by their _flight_, these automatons can be found around the world, seemingly as wanderers. A number of them act as itinerant saviors, slaying large creatures on the verge of attacking villages or rescuing travelers caught in tough spots. Occasional tales crop up among travelers claiming that they were saved from peril by a rain of bolts, but that when they returned to the site of the rescue hours later, they found nothing. Other sharpshooter automatons _[[spells/Keep Watch|keep watch]]_ in the skies, hovering thousands of feet in the air over important structures and locations throughout Golarion. While the locations appear random to a modern observer, most of these are places important to the individual automaton or of significance in Jistkan history, such as locations mentioned in the Poleiheira.

Now, besides those few on the Material Plane, most sharpshooter automatons reside in Axis with others of their kind. However, a few visit the Maelstrom on a regular basis, pushed toward the chaotic _[[feats/Uncertainty|uncertainty]]_ of these _planar_ depths by some sort of melancholy. These automatons tend to avoid other creatures and keep to themselves, and most proteans know that even in that chaotic realm, the constructs remain quite powerful, and thus keep their distance. Although the automatons in the Maelstrom are few, they are generally quite familiar with their favored region of the plane, and their powerful sight allows them to keep track of the chaos for miles in every direction. Most notable among these self-exiled sharpshooter automatons is Alvara the All-Seer. Those who know of her claim that the millennia through which she has stayed in the Maelstrom allows her to accurately understand and even predict the nature of the chaotic seas in which she resides.