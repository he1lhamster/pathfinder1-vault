---
cssclass: [monsters]
title1: Demon, Lilitu
desc_short: While this seductive woman has goat horns, goat hooves, and aserpentine
  tail, her eyeless face is her most disturbing feature.
title2: Lilitu
CR: 17
sources:
- name: Bestiary 6
  page: 84
  link: http://paizo.com/products/btpy9oge?Pathfinder-Roleplaying-Game-Bestiary-6-Hardcover
- name: The Worldwound
  page: 48
  link: http://paizo.com/products/btpy8yvk?Pathfinder-Campaign-Setting-The-Worldwound
XP: 102400
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar,shapechanger
initiative:
  bonus: 9
senses:
  darkvision: 60
  true seeing: true
auras:
- name: unholy aura
  DC: 26
AC:
  AC: 34
  touch: 24
  flat_footed: 28
  components:
    deflection: 4
    dex: 5
    dodge,+10 natural: 1
    profane: 4
HP:
  HP: 263
  long: 17d10+170
saves:
  fort: 19
  ref: 23
  will: 20
defensive_abilities:
- evasion
- profane grace
DR:
- amount: 10
  weakness: cold iron andgood
immunities:
- electricity
- poison
resistances:
  acid: 10
  cold: 10
  fire: 10
SR: 28
speeds:
  base: 60
  fly: 60
  fly_maneuverability: good
attacks:
  melee:
  - - text: 4 claws +25 (2d8+8/19-20)
      entries:
      - - damage: 2d8+8
          crit_range: 19-20
      count: 4
      attack: claws
      bonus:
      - 25
    - text: tail slap +20 touch (1d6+4plus branding)
      entries:
      - - damage: 1d6+4
          type: plus branding
      attack: tail slap
      bonus:
      - 20
      touch: true
  special:
  - create husk
  - husk link
  - profane pact
  - swift claws
spell_like_abilities:
  entries:
  - name: fly
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: true seeing
    source: default
    freq: Constant
  - name: unholy aura
    source: default
    freq: Constant
    DC: 26
  - name: charm monster
    source: default
    freq: At will
    DC: 22
  - name: detect thoughts
    source: default
    freq: At will
    DC: 20
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: suggestion
    source: default
    freq: At will
    DC: 21
  - name: telekinesis
    source: default
    freq: At will
    DC: 23
  - name: quickened charm monster
    source: default
    freq: 3/day
    DC: 22
  - name: persistent image
    source: default
    freq: 3/day
    DC: 23
  - name: seeming
    source: default
    freq: 3/day
    DC: 23
  - name: demand
    source: default
    freq: 1/day
    DC: 26
  - name: dominate monster
    source: default
    freq: 1/day
    DC: 27
  - name: project image
    source: default
    freq: 1/day
    DC: 25
  - name: summon
    source: default
    freq: 1/day
    level: 5
    summons:
    - name: lilitu
      amount: 1
      chance: 20%
    - name: glabrezus
      amount: 1d2
      chance: 40%
    - name: vrocks
      amount: 1d6
      chance: 50%
  - name: binding
    source: default
    freq: 1/week
    DC: 26
  - name: wish
    source: default
    freq: 1/week
    other: granted to a mortal humanoid only
  sources:
  - name: default
    CL: 17
    concentration: 25
ability_scores:
  STR: 27
  DEX: 20
  CON: 30
  INT: 21
  WIS: 23
  CHA: 26
BAB: 17
CMB: 25
CMD: 49
feats:
- name: Critical Focus
- name: Deceitful
- name: Dodge
- name: Improved Critical (claw)
- name: Mobility
- name: Power Attack
- name: Quicken Spell-Like Ability (charmmonster)
- name: Spring Attack
- name: Staggering Critical
skills:
  Acrobatics: 25
  Bluff: 40
  Diplomacy: 28
  Disguise: 29
  Fly: 37
  Intimidate: 25
  Knowledge (local): 25
  Knowledge (nobility): 25
  Knowledge (religion): 22
  Perception: 34
  Sense Motive: 26
  _racial_mods:
    Bluff:
      _: 8
    Perception:
      _: 8
languages:
- Abyssal
- Celestial
- Draconic
- telepathy 100 ft.
- tongues
special_qualities:
- change shape (Small or Medium humanoid; alter self),profane wishcraft
ecology:
  environment: any (Abyss)
  organization: solitary, pair, gathering (3-5), or cult (1 lilitu and6-12 succubi)
  treasure_type: double
special_abilities:
  Branding (Su): |-
    Each time a lilitu damages a living creature with her tail slap, the wound leaves an angry and permanent red brand. The creature struck becomes staggered for 1 round from the pain. A successful DC 26 Will save negates the staggered condition and reduces the duration of the brand from permanent to 1 hour. The save DC is Charisma-based. Removing brands is difficult-each casting of restoration, dispel chaos, or dispel evil removes one brand. Heal removes 1d4+4 brands. Greater restoration removes a number of brands equal to the spell's caster level. Miracle and wish can each remove all brands at once. The number of brands a creature gains in this manner has a cumulative series of effects, as listed below. 

    1-3 Brands: The lilitu can affect the branded creature with its create husk, husk link, and profane pact abilities. 

    4-6 Brands: The branded creature takes a -2 penalty on all Will saves made against a lilitu's spells, spell-like abilities, and supernatural abilities. The branded creature's aura now radiates chaos and evil. 

    7-9 Brands: The branded creature's Wisdom score is reduced by 4. A chaotic evil creature is immune to this effect. 

    10 or More Brands: The penalties to the creature's Will saves and Wisdom score that are listed above double. In addition, the branded creature automatically fails all Will saves made against a lilitu's spells, spell-like abilities, and supernatural abilities. A chaotic evil creature is immune to this effect.
  Create Husk (Su): Once per day as a swift action, when a lilitu deals enough damage
    with a weapon, spell, or spell-like ability to kill a branded Small or Medium
    humanoid within 30 feet, she can instead opt to transform that slain humanoid
    into a husk. The targeted creature can attempt a DC 26 Fortitude save to negate
    this effect, allowing it to die normally. A humanoid transformed into a husk withers
    away into an immobile and desiccated corpse, but does not actually die-in this
    state, the creature remains aware of its surroundings but can take no actions
    at all. A husk is essentially treated as an object with hardness 15 and 60 hit
    points; it weighs 10% of the original creature's weight. If a husk is destroyed,
    the effect ends and the body dies. This is a curse effect- removing this curse
    restores the victim to life at a number of negative hit points equal to the creature's
    Constitution - 1; a husk restored to life in this way has 1 round to stabilize
    or be healed before it dies. A lilitu can maintain a number of husks simultaneously
    equal to her Charisma bonus (8 husks for the typical lilitu); if she creates more
    husks than she can maintain, a previously created husk (chosen by the lilitu)
    is released and immediately dies. Lilitus hide their husk collections in very
    safe places. The save DC is Charisma-based.
  Husk Link (Su): By spending a minute in blasphemous contact with a husk she created,
    a lilitu can establish a supernatural link to that husk. As long as she and that
    husk remain on the same plane, divination spells reveal the linked husk's alignment
    to be the same as the lilitu's alignment (chaotic evil). The link allows a lilitu
    to use her change shape ability to assume a husk's original form, gaining a +20
    bonus on Disguise checks to impersonate that person. If a lilitu with an active
    husk link takes enough damage to be slain, the husk takes the killing blow's damage
    instead and is destroyed, instantly severing the active husk link; if the lilitu
    is disguised in the husk's original form, she instantly reverts to her true form.
  Profane Grace (Su): A lilitu gains a +4 profane bonus to AC and on Initiative checks
    and Reflex saves.
  Profane Pact (Su): Once per day as a full-round action, a lilitu can forge a profane
    pact with a willing humanoid creature bearing at least one lilitu brand by touching
    the creature for 1 full round. A single creature can have no more than one profane
    pact with a lilitu at any time. This functions identically to a succubus's profane
    gift ability (Pathfinder RPG Bestiary 68), save that it grants a +4 profane bonus
    to an ability score of the humanoid's choice and it does not grant a telepathic
    link to the target.
  Profane Wishcraft (Su): A creature that accepts a wish from a lilitu immediately
    becomes chaotic evil unless it succeeds at a DC 26 Will save. A creature that
    becomes chaotic evil in this way gains the benefits of a good hope spell for 24
    hours, followed by the effects of crushing despair for 1d6 days (these spell effects
    function at CL 17th). The save DC is Charisma-based.
  Swift Claws (Ex): When a lilitu makes a full attack, she can attack twice with each
    of her claws, for a total of four attacks in that round.
desc_long: |-
  Lilitus are subversive and hidden horrors, demons who work subtly in their constant quest to destroy and devastate. Whereas most demons prefer to rend and destroy, the lilitu is more akin to the succubus-she prefers to do her work in humanoid form to infect society with sin from within. Lilitus enjoy few things more than leading mortals into all manner of sinful acts, in the hope that when the mortal perishes, its soul will fuel the Abyss. Despite some superficial similarities to succubi, lilitus are not solely concerned with the sin of lust. The exact nature of sin that a lilitu tempts a mortal into committing varies, for these demons are adept at reading mortal desires and secrets, quickly discerning which sins a specific target can be convinced to perform. 

  Lilitus have numerous tools at their disposal for the encouragement of sin, but they much prefer their humanoid victims to commit sins of their own free will. As such, lilitus generally use their abilities to deceive and beguile mortals rather than forcing them to execute heinous acts. A son convinced to kill for his mother (the disguised lilitu) to rectify a grave injustice elicits far more delight than compelling a mind-controlled humanoid to do such a deed. 

  In her true form, a lilitu appears as an eyeless, horned, snake-tailed-but otherwise beautiful-human woman. Despite her lack of eyes, a lilitu can see with ease. A lilitu forms from the soul of a mortal who lured others of its kind to commit sins. 

  Lilitus are more likely than other demons to devote their work to a specific demon lord, yet they do not generally view such devotion as true servitude. It's simply convenient to have a specific demigod in mind when seeking to corrupt a mortal's faith and to convince such fallen souls to shift their own allegiance from a prior deity to the lilitu's chosen demon lord. When a lilitu chooses to ally herself with a demon lord, she takes on certain physical characteristics that reflect that demon lord's personality or appearance. For example, a lilitu that serves Dagon, the demon lord of deformity, sea monsters, and the sea might bear scaly skin like that of a fish, webbed fingers and toes, and finlike ridges on her head instead of the more typical goat's horns. A lilitu that serves Pazuzu, on the other hand, might have vestigial feathery wings on her back and bird's talons instead of hooves for feet. These appearance changes are cosmetic only and never impact the lilitu's options for natural attacks. Of course, the demon's ability to change shape or assume the form of a captured husk allows the demon to disguise her true form at will. Lilitus who serve specific demon lords in this manner often have class levels. A lilitu typically focuses on class roles such as bards, rogues, swashbucklers, or any other agility- and deception-based classes. 

  Lilitus typically stand 6 to 6-1/2 feet tall and weigh 130 to 150 pounds.

---

# Demon, Lilitu
While this seductive woman has goat horns, goat hooves, and a

serpentine tail, her eyeless face is her most disturbing feature.
**Source** Bestiary 6 pg. 84, The Worldwound pg. 48
**XP** 102,400
CE Medium outsider (chaotic, demon, evil, extraplanar,

shapechanger)
**Init** +9; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/True Seeing|true seeing]]_; Perception +34
**Aura** _[[spells/Unholy Aura|unholy aura]]_ (DC 26)

##### Defense

**AC** 34, touch 24, _[[conditions/Flat-Footed|flat-footed]]_ 28 (+4 _[[spells/Deflection|deflection]]_, +5 Dex, +1 _[[feats/Dodge|dodge]]_,

+10 natural, +4 profane)
**hp** 263 (17d10+170)
**Fort** +19, **Ref** +23, **Will** +20
**Defensive Abilities** evasion, profane _[[spells/Grace|grace]]_; **DR** 10/cold iron and

good; **Immune** electricity, poison; **Resist** acid 10, cold 10,

fire 10; **SR** 28

##### Offense
**Speed** 60 ft., fly 60 ft. (good)
**Melee** 4 claws +25 (2d8+8/19–20), tail slap +20 touch (1d6+4

plus branding)
**Special Attacks** create husk, husk link, profane pact, swift claws
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 17th; concentration +25)
Constant—fly, _[[spells/Tongues|tongues]]_, _true seeing_, _unholy aura_ (DC 26) 
At will—_[[spells/Charm Monster|charm monster]]_ (DC 22), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 20), greater teleport (self plus 50 lbs. of objects only), _[[spells/Suggestion|suggestion]]_ (DC 21), _[[spells/Telekinesis|telekinesis]]_ (DC 23) 
3/day—quickened _charm monster_ (DC 22), _[[spells/Persistent Image|persistent image]]_ (DC 23), _[[spells/Seeming|seeming]]_ (DC 23) 
1/day—_[[spells/Demand|demand]]_ (DC 26), _[[spells/Dominate Monster|dominate monster]]_ (DC 27), _[[spells/Project Image|project image]]_ (DC 25), _[[universal monster rules/Summon|summon]]_ (level 5, 1 lilitu 20%, 1d2 glabrezus 40%, or 1d6 vrocks 50%) 
1/week—_[[spells/Binding|binding]]_ (DC 26), _[[spells/Wish|wish]]_ (granted to a mortal humanoid only)

##### Statistics
**Str** 27, **Dex** 20, **Con** 30, **Int** 21, **Wis** 23, **Cha** 26
**Base Atk** +17; **CMB** +25; **CMD** 49
**Feats** _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Deceitful|Deceitful]]_, _Dodge_, _[[feats/Improved Critical|Improved Critical]]_ (claw), _[[feats/Mobility|Mobility]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Quicken Spell-Like Ability|Quicken Spell-Like Ability]]_ (charm

monster), _[[feats/Spring Attack|Spring Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_
**Skills** Acrobatics +25, Bluff +40, Diplomacy +28, Disguise +29,

Fly +37, Intimidate +25, Knowledge (local, nobility) +25,

Knowledge (religion) +22, Perception +34, Sense Motive +26;

Racial Modifiers +8 Bluff, +8 Perception
**Languages** Abyssal, Celestial, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.; _tongues_
**SQ** _[[universal monster rules/Change Shape|change shape]]_ (Small or _Medium_ humanoid; _[[spells/Alter Self|alter self]]_),

profane wishcraft

##### Ecology

**Environment** any (Abyss)
**Organization** solitary, pair, gathering (3–5), or cult (1 lilitu and

6–12 succubi)
**Treasure** double

### Special Abilities

**Branding (Su)** Each time a lilitu damages a living creature with her tail slap, the wound leaves an angry and permanent red _[[spells/Brand|brand]]_. The creature struck becomes _[[conditions/Staggered|staggered]]_ for 1 round from the pain. A successful DC 26 Will save negates the _staggered_ condition and reduces the duration of the _brand_ from permanent to 1 hour. The save DC is Charisma-based. Removing brands is difficult—each casting of _[[spells/Restoration|restoration]]_, _[[spells/Dispel Chaos|dispel chaos]]_, or _[[spells/Dispel Evil|dispel evil]]_ removes one _brand_. _[[spells/Heal|Heal]]_ removes 1d4+4 brands. Greater _restoration_ removes a number of brands equal to the spell’s caster level. _[[spells/Miracle|Miracle]]_ and _wish_ can each remove all brands at once. The number of brands a creature gains in this manner has a cumulative series of effects, as listed below.

1–3 Brands: The lilitu can affect the branded creature with its create husk, husk link, and profane pact abilities.

4–6 Brands: The branded creature takes a –2 penalty on all Will saves made against a lilitu’s spells, _spell-like abilities_, and supernatural abilities. The branded creature’s aura now radiates chaos and evil.

7–9 Brands: The branded creature’s Wisdom score is reduced by 4. A chaotic evil creature is immune to this effect.

10 or More Brands: The penalties to the creature’s Will saves and Wisdom score that are listed above double. In addition, the branded creature automatically fails all Will saves made against a lilitu’s spells, _spell-like abilities_, and supernatural abilities. A chaotic evil creature is immune to this effect.

**Create Husk (Su)** Once per day as a swift action, when a lilitu deals enough damage with a weapon, spell, or spell-like ability to kill a branded Small or _Medium_ humanoid within 30 feet, she can instead opt to transform that slain humanoid into a husk. The targeted creature can attempt a DC 26 Fortitude save to negate this effect, allowing it to die normally. A humanoid transformed into a husk withers away into an immobile and desiccated corpse, but does not actually die—in this state, the creature remains aware of its surroundings but can take no actions at all. A husk is essentially treated as an object with hardness 15 and 60 hit points; it weighs 10% of the original creature’s weight. If a husk is destroyed, the effect ends and the body dies. This is a curse effect— removing this curse restores the victim to life at a number of negative hit points equal to the creature’s Constitution – 1; a husk restored to life in this way has 1 round to stabilize or be healed before it dies. A lilitu can maintain a number of husks simultaneously equal to her Charisma bonus (8 husks for the typical lilitu); if she creates more husks than she can maintain, a previously created husk (chosen by the lilitu) is released and immediately dies. Lilitus hide their husk collections in very safe places. The save DC is Charisma-based.

**Husk Link (Su)** By spending a minute in blasphemous contact with a husk she created, a lilitu can establish a supernatural link to that husk. As long as she and that husk remain on the same plane, _[[spells/Divination|divination]]_ spells reveal the linked husk’s alignment to be the same as the lilitu’s alignment (chaotic evil). The link allows a lilitu to use her _change shape_ ability to assume a husk’s original form, gaining a +20 bonus on Disguise checks to impersonate that person. If a lilitu with an active husk link takes enough damage to be slain, the husk takes the killing blow’s damage instead and is destroyed, instantly severing the active husk link; if the lilitu is disguised in the husk’s original form, she instantly reverts to her _[[spells/True Form|true form]]_.

**Profane _Grace_ (Su)** A lilitu gains a +4 profane bonus to AC and on Initiative checks and Reflex saves.

**Profane Pact (Su)** Once per day as a full-round action, a lilitu can forge a profane pact with a willing humanoid creature bearing at least one lilitu _brand_ by touching the creature for 1 full round. A single creature can have no more than one profane pact with a lilitu at any time. This functions identically to a succubus’s profane gift ability (Pathfinder RPG Bestiary 68), save that it grants a +4 profane bonus to an ability score of the humanoid’s choice and it does not grant a _[[feats/Telepathic Link|telepathic link]]_ to the target.

**Profane Wishcraft (Su)** A creature that accepts a _wish_ from a lilitu immediately becomes chaotic evil unless it succeeds at a DC 26 Will save. A creature that becomes chaotic evil in this way gains the benefits of a _[[spells/Good Hope|good hope]]_ spell for 24 hours, followed by the effects of _[[spells/Crushing Despair|crushing despair]]_ for 1d6 days (these spell effects function at CL 17th). The save DC is Charisma-based.
**Swift Claws (Ex)** When a lilitu makes a full attack, she can attack twice with each of her claws, for a total of four attacks in that round.

##### Description

Lilitus are subversive and hidden horrors, demons who work subtly in their constant quest to destroy and devastate. Whereas most demons prefer to _[[universal monster rules/Rend|rend]]_ and destroy, the lilitu is more akin to the succubus—she prefers to do her work in humanoid form to infect society with sin from within. Lilitus enjoy few things more than leading mortals into all manner of sinful acts, in the hope that when the mortal perishes, its soul will fuel the Abyss. Despite some superficial similarities to succubi, lilitus are not solely concerned with the sin of lust. The exact nature of sin that a lilitu tempts a mortal into committing varies, for these demons are adept at reading mortal desires and secrets, quickly discerning which sins a specific target can be convinced to perform.

Lilitus have numerous tools at their disposal for the encouragement of sin, but they much prefer their humanoid victims to commit sins of their own free will. As such, lilitus generally use their abilities to deceive and beguile mortals rather than forcing them to execute heinous acts. A son convinced to kill for his mother (the disguised lilitu) to rectify a grave injustice elicits far more delight than compelling a mind-controlled humanoid to do such a deed.

In her _true form_, a lilitu appears as an eyeless, horned, snake-tailed—but otherwise beautiful—human woman. Despite her lack of eyes, a lilitu can see with ease. A lilitu forms from the soul of a mortal who lured others of its kind to commit sins.

Lilitus are more likely than other demons to devote their work to a specific demon lord, yet they do not generally view such devotion as true servitude. It’s simply convenient to have a specific demigod in mind when seeking to corrupt a mortal’s faith and to convince such _[[monsters/Fallen|fallen]]_ souls to shift their own allegiance from a prior deity to the lilitu’s chosen demon lord. When a lilitu chooses to ally herself with a demon lord, she takes on certain physical characteristics that reflect that demon lord’s personality or appearance. For example, a lilitu that serves Dagon, the demon lord of deformity, sea monsters, and the sea might bear scaly skin like that of a fish, webbed fingers and toes, and finlike ridges on her head instead of the more typical goat’s horns. A lilitu that serves Pazuzu, on the other hand, might have vestigial feathery wings on her back and bird’s talons instead of hooves for feet. These appearance changes are cosmetic only and never _[[items/Weapon Magic Abilities/Impact|impact]]_ the lilitu’s options for _[[universal monster rules/Natural Attacks|natural attacks]]_. Of course, the demon’s ability to _change shape_ or assume the form of a captured husk allows the demon to disguise her _true form_ at will. Lilitus who serve specific demon lords in this manner often have class levels. A lilitu typically focuses on class roles such as bards, rogues, swashbucklers, or any other agility- and deception-based classes.

Lilitus typically stand 6 to 6-1/2 feet tall and weigh 130 to 150 pounds.