---
cssclass: [monsters]
title1: Poludnica
desc_short: 'A haze of heat shimmers around this beautiful woman. The glare of the
  sun gleams from her radiant skin. '
title2: Poludnica
CR: 10
sources:
- name: "Pathfinder #72: The Witch Queen's Revenge"
  page: 88
  link: http://paizo.com/products/btpy8yv7?Pathfinder-Adventure-Path-72-The-Witch-Queen-s-Revenge
XP: 9600
alignment: CN
size: Medium
type: fey
initiative:
  bonus: 5
senses:
  low-light vision: true
auras:
- name: sunstroke haze
  radius: 10
  DC: 21
AC:
  AC: 24
  touch: 20
  flat_footed: 18
  components:
    armor: 4
    deflection: 4
    dex: 5
    dodge: 1
HP:
  HP: 119
  long: 14d6+70
saves:
  fort: 11
  ref: 14
  will: 11
DR:
- amount: 10
  weakness: cold iron
immunities:
- blindness
- exhaustion
- fatigue
- fire
SR: 21
weaknesses:
- darkness powerlessness
speeds:
  base: 30
attacks:
  melee:
  - - text: +1 scythe +15/+10 (2d4+10 plus 1d6 fire and 1d2 Con damage/×4)
      entries:
      - - damage: 2d4+10
          crit_multiplier: 4
        - damage: 1d6
          type: fire
          crit_multiplier: 4
        - damage: 1d2
          type: Con damage
          crit_multiplier: 4
      attack: +1 scythe
      bonus:
      - 15
      - 10
  special:
  - searing weapons
spell_like_abilities:
  entries:
  - name: pass without trace
    source: default
    freq: Constant
  - name: daylight
    source: default
    freq: At will
  - name: plant growth
    source: default
    freq: At will
    other: enrichment only
  - name: touch of fatigue
    source: default
    freq: At will
    DC: 14
  - name: blur
    source: default
    freq: 3/day
  - name: dimension door
    source: default
    freq: 3/day
  - name: rainbow pattern
    source: default
    freq: 3/day
    DC: 18
  - name: searing light
    source: default
    freq: 3/day
  - name: sunbeam
    source: default
    freq: 1/day
    DC: 21
  - name: waves of fatigue
    source: default
    freq: 1/day
  sources:
  - name: default
    CL: 10
    concentration: 14
ability_scores:
  STR: 22
  DEX: 20
  CON: 21
  INT: 10
  WIS: 15
  CHA: 19
BAB: 7
CMB: 13
CMD: 33
feats:
- name: Cleave
- name: Combat Reflexes
- name: Dodge
- name: Great Fortitude
- name: Power Attack
- name: Stand Still
- name: Weapon Focus (scythe)
skills:
  Bluff: 12
  Diplomacy: 13
  Intimidate: 9
  Knowledge (local): 17
  Perception: 19
  Sense Motive: 15
  Spellcraft: 10
  Stealth: 20
  Survival: 10
languages:
- Common
- Sylvan
special_qualities:
- grace
- tied to day
ecology:
  environment: temperate plains
  organization: solitary
  treasure_type: standard
  treasure:
  - +1 scythe
  - mithral chain shirt
  - other treasure
special_abilities:
  Darkness Powerlessness (Su): As long as a poludnica is within an area of magical
    darkness, her sunstroke haze aura does not function. She also becomes staggered
    and cannot use any of her spell-like abilities.
  Grace (Su): A poludnica adds her Charisma modifier as a deflection bonus to her
    Armor Class.
  Searing Weapons (Su): Any weapon a poludnica wields becomes incredibly hot and conducts
    and amplifies her ability to cause fatigue by reducing the target's ability to
    resist the effects. In melee combat, such a weapon deals an additional 1d6 points
    of fire damage plus 1d2 points of Constitution damage. The Constitution damage
    is negated with a successful DC 21 Fortitude save. The weapon cools rapidly if
    it leaves her grasp, losing these additional abilities immediately.
  Sunstroke Haze (Su): A poludnica radiates oppressive heat in a 10-foot radius. Any
    creature that starts its turn within this area must succeed at a DC 21 Fortitude
    save or take 1d6 points of nonlethal damage and become fatigued. A fatigued creature
    that fails a second saving throw becomes exhausted. The fatigued or exhausted
    condition lasts for as long as the nonlethal damage goes unhealed. A poludnica
    can activate or suppress this ability as a free action and the save DC is Charisma-based.
  Tied to Day (Su): A poludnica's connection to the sun tethers her to the Material
    Plane. During daylight hours (from dawn to sunset), her abilities are as shown
    above whether she can actually see the sun or not. During the nighttime hours
    (from sunset to dawn), a poludnica shifts to the Ethereal Plane (as ethereal jaunt).
    This is automatic, involuntary, and causes a poludnica great distress. While on
    the Ethereal Plane, a poludnica is affected by her darkness powerlessness and
    is nearly helpless. This curse cannot be dispelled or removed by anything short
    of divine interaction.
desc_long: |-
  Driven by an obsession that few can fully comprehend, poludnicas are bitter creatures of light, heat, and envy. Although they are surprisingly strong and deadly combatants, these scythe-wielding women resort to violence only when guile and trickery have failed. They are lonely creatures that seek the company of mortals by luring farm workers and children away from their families so that they can brief ly enjoy a feeble simulation of family life. In the rural farming communities where her kind is most commonly found, a poludnica might also be known as Cornwife, Lady Midday, or Mother Noon. She might even be mistaken for a vengeful or beneficent ghost depending on how she presents herself. 

  Averaging 6 feet tall and weighing approximately 170 pounds, poludnicas could easily be mistaken for strapping farm girls if it were not for their radiance. Their maximum life expectancy has not been documented and it is commonly believed that poludnicas are effectively immortal unless they suffer some deadly mishap. It has been theorized that permanently keeping a poludnica in magically darkened conditions would eventually lead to her death, but no scholars have so far attempted to prove this hypothesis.

---

# Poludnica
A haze of _[[universal monster rules/Heat|heat]]_ shimmers around this beautiful woman. The glare
of the sun gleams from her _[[items/Armor Magic Abilities/Radiant|radiant]]_ skin.

**Source** Pathfinder #72: The _[[classes/Witch|Witch]]_ Queen's Revenge pg. 88
**XP** 9,600

CN Medium fey
**Init** +5; **Senses** _[[universal monster rules/Low-Light Vision|low-light vision]]_; Perception +19
**Aura** sunstroke haze (10 ft., DC 21)

##### Defense

**AC** 24, touch 20, _[[conditions/Flat-Footed|flat-footed]]_ 18 (+4 armor, +4 _[[spells/Deflection|deflection]]_, +5 Dex,
+1 _[[feats/Dodge|dodge]]_)
**hp** 119 (14d6+70)
**Fort** +11, **Ref** +14, **Will** +11
**DR** 10/cold iron; **Immune** blindness, exhaustion, fatigue, fire; **SR** 21
**Weaknesses** _[[spells/Darkness|darkness]]_ powerlessness

##### Offense
**Speed** 30 ft.
**Melee** +1 _[[items/Weapon/Scythe|scythe]]_ +15/+10 (2d4+10 plus 1d6 fire and 1d2 Con
damage/×4)
**Special Attacks** searing weapons
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 10th; concentration +14)
Constant—_[[spells/Pass without Trace|pass without trace]]_
At will—_[[spells/Daylight|daylight]]_, _[[spells/Plant Growth|plant growth]]_ (enrichment only), touch of
fatigue (DC 14)
3/day—_[[spells/Blur|blur]]_, _[[spells/Dimension Door|dimension door]]_, _[[spells/Rainbow Pattern|rainbow pattern]]_ (DC 18),
_[[spells/Searing Light|searing light]]_
1/day—_[[spells/Sunbeam|sunbeam]]_ (DC 21), _[[spells/Waves of Fatigue|waves of fatigue]]_

##### Statistics
**Str** 22, **Dex** 20, **Con** 21, **Int** 10, **Wis** 15, **Cha** 19
**Base Atk** +7; **CMB** +13; **CMD** 33
**Feats** _[[feats/Cleave|Cleave]]_, _[[feats/Combat Reflexes|Combat Reflexes]]_, _Dodge_, _[[feats/Great Fortitude|Great Fortitude]]_, Power
Attack, _[[feats/Stand Still|Stand Still]]_, _[[feats/Weapon Focus|Weapon Focus]]_ (_scythe_)
**Skills** Bluff +12, Diplomacy +13, Intimidate +9, Knowledge
(local) +17, Perception +19, Sense Motive +15, Spellcraft +10,
Stealth +20, Survival +10
**Languages** Common, Sylvan
**SQ** _[[spells/Grace|grace]]_, tied to day

##### Ecology

**Environment** temperate plains
**Organization** solitary
**Treasure** standard (+1 _scythe_, mithral _[[items/Armor/Chain shirt|chain shirt]]_, other treasure)

### Special Abilities

**_Darkness_ Powerlessness (Su)** As long as a _[[monsters/Poludnica|poludnica]]_ is within
an area of magical _darkness_, her sunstroke haze aura does
not function. She also becomes _[[conditions/Staggered|staggered]]_ and cannot use
any of her _spell-like abilities_.

**_Grace_ (Su)** A _poludnica_ adds her Charisma modifier as a
_deflection_ bonus to her Armor Class.
**Searing Weapons (Su)** Any weapon a _poludnica_ wields becomes
incredibly hot and conducts and amplifies her ability to cause
fatigue by reducing the target’s ability to resist the effects.
In melee combat, such a weapon deals an additional 1d6
points of fire damage plus 1d2 points of Constitution damage.
The Constitution damage is negated with a successful DC 21
Fortitude save. The weapon cools rapidly if it leaves her _[[spells/Grasp|grasp]]_,
losing these additional abilities immediately.
**Sunstroke Haze (Su)** A _poludnica_ radiates oppressive _heat_
in a 10-foot radius. Any creature that starts its turn within
this area must succeed at a DC 21 Fortitude save or take
 1d6 points of nonlethal damage and become _[[conditions/Fatigued|fatigued]]_. A
_fatigued_ creature that fails a second saving throw becomes
_[[conditions/Exhausted|exhausted]]_. The _fatigued_ or _exhausted_ condition lasts for as
long as the nonlethal damage goes unhealed. A _poludnica_
can activate or suppress this ability as a free action and the
save DC is Charisma-based.

**Tied to Day (Su)** A _poludnica_’s connection to the sun tethers
her to the Material Plane. During _daylight_ hours (from dawn
to sunset), her abilities are as shown above whether she can
actually see the sun or not. During the nighttime hours (from
sunset to dawn), a _poludnica_ shifts to the Ethereal Plane (as
_[[spells/Ethereal Jaunt|ethereal jaunt]]_). This is automatic, involuntary, and causes
a _poludnica_ great distress. While on the Ethereal Plane, a
_poludnica_ is affected by her _darkness_ powerlessness and is
nearly _[[conditions/Helpless|helpless]]_. This curse cannot be dispelled or removed
by anything short of divine interaction.

##### Description

Driven by an obsession that few can fully comprehend,
poludnicas are _[[items/Armor Magic Abilities/Bitter|bitter]]_ creatures of light, _heat_, and envy.
Although they are surprisingly strong and _[[items/Weapon Magic Abilities/Deadly|deadly]]_
combatants, these scythe-wielding women resort to
violence only when guile and trickery have failed. They
are lonely creatures that seek the company of mortals
by luring farm workers and children away from their
families so that they can brief ly enjoy a feeble simulation
of family life. In the rural farming communities where her
kind is most commonly found, a _poludnica_ might also be
known as Cornwife, Lady Midday, or Mother Noon. She
might even be mistaken for a vengeful or beneficent _[[monsters/Ghost|ghost]]_
depending on how she presents herself.

Averaging 6 feet tall and weighing approximately 170
pounds, poludnicas could easily be mistaken for strapping
farm girls if it were not for their _[[items/Weapon/Radiance|radiance]]_. Their maximum
life expectancy has not been documented and it is commonly
believed that poludnicas are effectively immortal unless
they suffer some _deadly_ mishap. It has been theorized that
permanently keeping a _poludnica_ in magically darkened
conditions would eventually lead to her death, but no
scholars have so far attempted to prove this hypothesis.