---
cssclass: [monsters]
title1: Emotion Ooze
desc_short: This viscous blob of brightly colored goo quivers and pulses in a curious
  manner.
title2: Emotion Ooze
CR: 6
sources:
- name: Bestiary 5
  page: 108
  link: http://paizo.com/products/btpy9g9x?Pathfinder-Roleplaying-Game-Bestiary-5
XP: 2400
alignment: N
size: Medium
type: ooze
initiative:
  bonus: -3
senses:
  blindsense: 120
auras:
- name: emotion
  DC: 20
AC:
  AC: 13
  touch: 13
  flat_footed: 13
  components:
    deflection: 6
    dex: -3
HP:
  HP: 76
  long: 9d8+36
saves:
  fort: 13
  ref: 6
  will: 11
defensive_abilities:
- amorphous
immunities:
- mind-affecting effects
- ooze traits
speeds:
  base: 20
  climb: 20
attacks:
  melee:
  - - text: slam +11 (1d8+7 plus emotional scarring)
      entries:
      - - damage: 1d8+7
        - effect: emotional scarring
      attack: slam
      bonus:
      - 11
  special:
  - compel emotion
  - emotional scarring
ability_scores:
  STR: 20
  DEX: 5
  CON: 18
  INT:
  WIS: 15
  CHA: 23
BAB: 6
CMB: 11
CMD: 16
skills:
  Climb: 13
  Perception: 2
special_qualities:
- compression
- emotional attunement
- empathic healing
ecology:
  environment: any
  organization: solitary, pair, conflict (3-12, often with different attuned emotions)
  treasure_type: incidental
special_abilities:
  Compel Emotion (Su): |-
    As a move action, an emotion ooze can release a pulse of psychic energy that causes intelligent creatures within 60 feet to be overwhelmed by the emotion ooze's attuned emotion (Will DC 20 negates). Each emotion has a special effect on affected creatures, which is described in the corresponding emotional attunement entry (see below). The effects of multiple emotion oozes attuned to the same emotion don't stack, but a creature can be under the effects of different emotions from different types of emotion oozes at the same time.

     A creature affected by compel emotion retains the chosen emotion for as long as it remains within 60 feet of the emotion ooze and for 1d4 minutes thereafter. An affected creature that takes a move action to try to control its emotions can attempt another DC 20 Will save. Success on this Will save removes the effect and grants the creature a +4 circumstance bonus on future saves against that emotion ooze's compel emotion ability for 24 hours. This is a mind-affecting emotion effect. The save DC is Charisma-based.
  Emotional Attunement (Su): |-
    Each emotion ooze is closely attuned to a single emotion. The type of emotion affects its physiology, altering its fundamental nature.

     Anger: An emotion ooze attuned to anger glows bright red. Its Strength score increases by 4, it gains Power Attack as a bonus feat, and it has fire resistance 10. A creature affected by an anger-attuned emotion ooze's compel emotion ability is compelled to take attacks of opportunity against its allies whenever those allies take actions that would provoke an attack of opportunity from a creature. These count against the number of attacks of opportunity the creature can take each round.

     Dedication: An emotion ooze attuned to dedication is a deep blue. Its Constitution score increases by 4, it gains Great Fortitude and Toughness as bonus feats, and its natural armor bonus to AC increases by 2. A creature affected by a dedication-attuned emotion ooze's compel emotion ability is unable to move away from an adjacent opponent unless it succeeds at a DC 20 Will save at the start of its turn. Success allows the creature to move away that round, but does not end the effect.

     Despair: An emotion ooze attuned to despair is a pale, listless gray. Its Constitution and Charisma scores increase by 2, and it has DR 10/magic and cold resistance 10. A creature affected by a despair-attuned emotion ooze's compel emotion ability takes a -4 morale penalty on attack rolls and damage rolls.

     Fear: An emotion ooze attuned to fear is light gray, flecked with darker gray motes swirling about its insides. Its Dexterity score increases by 4, it gains Improved Initiative and Lightning Reflexes as bonus feats, and it gains the evasion rogue class feature. A creature affected by a fearattuned emotion ooze's compel emotion ability gains the shaken condition.

     Hatred: An emotion ooze attuned to hatred is a deep black color, which pulsates violently when it attacks. Its Strength, Dexterity, and Constitution scores increase by 2, it has acid resistance 10, and its emotional scarring ability deals an additional 4d6 points of damage (instead of 3d6). A creature affected by a hatred-attuned emotion ooze's compel emotion ability takes a -4 penalty to AC, but gains a +1 morale bonus on attack rolls and damage rolls.

     Jealousy: An emotion ooze attuned to jealousy is a swirl of oily green, orange, and brownish red. Its Strength and Dexterity scores increase by 2, and it has DR 5/silver and SR 17. A creature affected by a jealousy-attuned emotion ooze's compel emotion ability must attempt saving throws to resist all spells cast on it, including harmless and beneficial spells.

     Zeal: An emotion ooze attuned to zeal is a bright orange color, and grows brighter when the ooze is feeding or has recently fed. Its Strength, Constitution, and Wisdom scores increase by 2, and it has DR 5/magic and electricity resistance 10. A creature affected by a zeal-attuned emotion ooze's compel emotion ability must succeed at a DC 20 Will save each round or repeat the same actions it took on the previous round. If it is unable to do so (such as if it made a full attack against an opponent that has moved away, or cast a spell that has been expended), it must take actions that mimic those taken in the previous round as closely as possible. Succeeding at this Will save allows the creature to act normally for 1 round, but does not free it from the emotion effect.
  Emotional Scarring (Ex): An emotion ooze's slam attack deals an additional 3d6 points
    of damage, which is mental damage like that from mind thrust I. This is a mind-affecting
    emotion effect.
  Empathic Healing (Su): An emotion ooze gains fast healing 5 as long as it is within
    60 feet of a creature that is affected by its compel emotion ability (or that
    is otherwise experiencing the emotion to which the ooze is attuned). Though an
    emotion ooze is otherwise immune to mind-affecting effects, it is healed by emotion
    effects that match its emotion, regaining a number of hit points equal to the
    caster level of the effect (or to the ooze's Hit Dice for abilities with no caster
    level). The ooze takes an equal amount of damage if it fails a saving throw against
    an effect that specifically counters its corresponding emotion (for instance,
    remove fear for fear or good hope for despair).
desc_long: |-
  Truly bizarre and alien creatures, emotion oozes are made of ectoplasm that has somehow been granted the spark of life. Though they can't be categorized as intelligent, emotion oozes have a unique emotional empathy, allowing them not only to respond and react to the emotions of nearby creatures, but also to psychically shape and alter the emotions of others.

   Though they are carnivorous, emotion oozes prefer to seek out victims with strong emotions, on which they also feed. As a part of their unnatural biology, they gain a physiological benefit from being exposed to strong emotions. Each emotion ooze is attuned to a specific emotion, and the cause of this connection is unclear. The most commonly accepted theory is that the oozes imprint on the first strong emotion that they are exposed to or that the emotion is imprinted in the ectoplasm, though others believe that the creatures have some control over this bond, and can even change the emotion they're attuned to given enough time. In addition to their coloration ref lecting their attuned emotions, emotion ooze takes on forms that befit the emotion to which they are tied, making it fairly easy for those with knowledge of the creatures to determine each one's particular emotional attunement on first glance.

   Creatures that encounter an emotion ooze find that it mimics their expressions and movements in an unnerving manner, sometimes even duplicating the facial features of the creature as it mimics a smile or growl. The ooze's reactions get more extreme when creatures around it express the type of emotion to which the ooze is attuned. The ooze begins to noticeably ripple, pulsing in a sympathetic rhythm and reshaping itself more rapidly than it does when it is on the search for emotional creatures. An anger-attuned ooze might form its pseudopods to look more like jagged spikes, and a despair ooze might reach out fitfully like a creature struggling to escape from a pool of quicksand.

   Most animals and unintelligent life forms find an emotion ooze's imitation and emotional echoes terrifying and flee as quickly as possible. Though some sentient creatures have this same reaction, others find the phenomenon fascinating, and attempt to either experiment with or capture emotion oozes, putting themselves within reach of the hungry oozes' grasp. These intelligent creatures are the most common victims of emotion ooze attacks.

   Pitched battles draw the attentions of emotion oozes attuned to anger, fear, hatred, or zeal. Such an ooze might join a nearby battle it senses so it can feed off the emotions generated there. The desire to continue causing and absorbing such strong feelings causes the ooze to try to prolong the battle, spreading out its attacks among multiple targets and paying little attention to creatures that aren't affected by its ability to compel emotion. In the end, the ooze's hunger might actually be its downfall.

   Emotion oozes often dwell in places where strong emotions were felt in the past, suggesting the creatures might have latent psychometric ability. Hatred oozes might live at the sites of massacres, zeal oozes in old temples or political offices, despair oozes in ancient prisons, and so on. If stuck in one place or deprived of emotional connections for a long time, an emotion ooze begins to lose its coloration, becoming a dull white, and eventually hardens and cracks into pieces.

   The typical emotion ooze has about the same volume as a human, but its composition makes it significantly lighter, weighing only around 50 pounds.

---

# Emotion Ooze
This viscous blob of brightly colored goo quivers and pulses in a curious manner.
**Source** Bestiary 5 pg. 108
**XP** 2,400

N Medium ooze
**Init** –3; **Senses** _[[universal monster rules/Blindsense|blindsense]]_ 120 ft.; Perception +2
**Aura** emotion (DC 20)

##### Defense

**AC** 13, touch 13, _[[conditions/Flat-Footed|flat-footed]]_ 13 (+6 _[[spells/Deflection|deflection]]_, –3 Dex)
**hp** 76 (9d8+36)
**Fort** +13, **Ref** +6, **Will** +11
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_; **Immune** mind-affecting effects, ooze traits

##### Offense
**Speed** 20 ft., _[[universal monster rules/Climb|climb]]_ 20 ft.
**Melee** slam +11 (1d8+7 plus emotional scarring)
**Special Attacks** compel emotion, emotional scarring

##### Statistics
**Str** 20, **Dex** 5, **Con** 18, **Int** —, **Wis** 15, **Cha** 23
**Base Atk** +6; **CMB** +11; **CMD** 16
**Skills** _Climb_ +13
**SQ** _[[universal monster rules/Compression|compression]]_, emotional attunement, empathic healing

##### Ecology

**Environment** any
**Organization** solitary, pair, conflict (3–12, often with different attuned emotions)
**Treasure** incidental

### Special Abilities

**Compel Emotion (Su)** As a move action, an _[[monsters/Emotion Ooze|emotion ooze]]_ can release a pulse of _[[classes/Psychic|psychic]]_ energy that causes intelligent creatures within 60 feet to be overwhelmed by the _emotion ooze_'s attuned emotion (Will DC 20 negates). Each emotion has a special effect on affected creatures, which is described in the corresponding emotional attunement entry (see below). The effects of multiple emotion oozes attuned to the same emotion don't stack, but a creature can be under the effects of different emotions from different types of emotion oozes at the same time.

A creature affected by compel emotion retains the chosen emotion for as long as it remains within 60 feet of the _emotion ooze_ and for 1d4 minutes thereafter. An affected creature that takes a move action to try to control its emotions can attempt another DC 20 Will save. Success on this Will save removes the effect and grants the creature a +4 circumstance bonus on future saves against that _emotion ooze_'s compel emotion ability for 24 hours. This is a mind-affecting emotion effect. The save DC is Charisma-based.

**Emotional Attunement (Su)** Each _emotion ooze_ is closely attuned to a single emotion. The type of emotion affects its physiology, altering its fundamental nature.

Anger: An _emotion ooze_ attuned to anger glows bright red. Its Strength score increases by 4, it gains _[[feats/Power Attack|Power Attack]]_ as a bonus feat, and it has fire _[[universal monster rules/Resistance|resistance]]_ 10. A creature affected by an anger-attuned _emotion ooze_'s compel emotion ability is compelled to take attacks of opportunity against its allies whenever those allies take actions that would provoke an attack of opportunity from a creature. These count against the number of attacks of opportunity the creature can take each round.

Dedication: An _emotion ooze_ attuned to dedication is a deep blue. Its Constitution score increases by 4, it gains _[[feats/Great Fortitude|Great Fortitude]]_ and _[[feats/Toughness|Toughness]]_ as bonus feats, and its natural armor bonus to AC increases by 2. A creature affected by a dedication-attuned _emotion ooze_'s compel emotion ability is unable to move away from an adjacent opponent unless it succeeds at a DC 20 Will save at the start of its turn. Success allows the creature to move away that round, but does not end the effect.

Despair: An _emotion ooze_ attuned to despair is a pale, listless _[[monsters/Gray|gray]]_. Its Constitution and Charisma scores increase by 2, and it has DR 10/magic and cold _resistance_ 10. A creature affected by a despair-attuned _emotion ooze_'s compel emotion ability takes a –4 morale penalty on attack rolls and damage rolls.

_[[universal monster rules/Fear|Fear]]_: An _emotion ooze_ attuned to _fear_ is light _gray_, flecked with darker _gray_ motes swirling about its insides. Its Dexterity score increases by 4, it gains _[[feats/Improved Initiative|Improved Initiative]]_ and _[[feats/Lightning Reflexes|Lightning Reflexes]]_ as bonus feats, and it gains the evasion _[[classes/Rogue|rogue]]_ class feature. A creature affected by a fearattuned _emotion ooze_'s compel emotion ability gains the _[[conditions/Shaken|shaken]]_ condition.

Hatred: An _emotion ooze_ attuned to hatred is a deep black color, which pulsates violently when it attacks. Its Strength, Dexterity, and Constitution scores increase by 2, it has acid _resistance_ 10, and its emotional scarring ability deals an additional 4d6 points of damage (instead of 3d6). A creature affected by a hatred-attuned _emotion ooze_'s compel emotion ability takes a –4 penalty to AC, but gains a +1 morale bonus on attack rolls and damage rolls.

Jealousy: An _emotion ooze_ attuned to jealousy is a swirl of oily green, orange, and brownish red. Its Strength and Dexterity scores increase by 2, and it has DR 5/silver and SR 17. A creature affected by a jealousy-attuned _emotion ooze_'s compel emotion ability must attempt saving throws to resist all spells cast on it, including harmless and beneficial spells.

Zeal: An _emotion ooze_ attuned to zeal is a bright orange color, and grows brighter when the ooze is feeding or has recently fed. Its Strength, Constitution, and Wisdom scores increase by 2, and it has DR 5/magic and electricity _resistance_ 10. A creature affected by a zeal-attuned _emotion ooze_'s compel emotion ability must succeed at a DC 20 Will save each round or repeat the same actions it took on the previous round. If it is unable to do so (such as if it made a full attack against an opponent that has moved away, or cast a spell that has been expended), it must take actions that _[[monsters/Mimic|mimic]]_ those taken in the previous round as closely as possible. Succeeding at this Will save allows the creature to act normally for 1 round, but does not free it from the emotion effect.

**Emotional Scarring (Ex)** An _emotion ooze_'s slam attack deals an additional 3d6 points of damage, which is mental damage like that from _[[spells/Mind Thrust I|mind thrust I]]_. This is a mind-affecting emotion effect.

**Empathic Healing (Su)** An _emotion ooze_ gains _[[universal monster rules/Fast Healing|fast healing]]_ 5 as long as it is within 60 feet of a creature that is affected by its compel emotion ability (or that is otherwise experiencing the emotion to which the ooze is attuned). Though an _emotion ooze_ is otherwise immune to mind-affecting effects, it is healed by emotion effects that match its emotion, regaining a number of hit points equal to the caster level of the effect (or to the ooze's Hit Dice for abilities with no caster level). The ooze takes an equal amount of damage if it fails a saving throw against an effect that specifically counters its corresponding emotion (for instance, _[[spells/Remove Fear|remove fear]]_ for _fear_ or _[[spells/Good Hope|good hope]]_ for despair).

##### Description

Truly bizarre and alien creatures, emotion oozes are made of ectoplasm that has somehow been granted the _[[spells/Spark|spark]]_ of life. Though they can’t be categorized as intelligent, emotion oozes have a unique emotional _[[feats/Empathy|empathy]]_, allowing them not only to respond and react to the emotions of nearby creatures, but also to psychically shape and alter the emotions of others.

Though they are carnivorous, emotion oozes prefer to seek out victims with strong emotions, on which they also feed. As a part of their unnatural biology, they gain a physiological benefit from being exposed to strong emotions. Each _emotion ooze_ is attuned to a specific emotion, and the cause of this connection is unclear. The most commonly accepted theory is that the oozes imprint on the first strong emotion that they are exposed to or that the emotion is imprinted in the ectoplasm, though others believe that the creatures have some control over this bond, and can even change the emotion they’re attuned to given enough time. In addition to their coloration ref lecting their attuned emotions, _emotion ooze_ takes on forms that befit the emotion to which they are tied, making it fairly easy for those with knowledge of the creatures to determine each one’s particular emotional attunement on first glance.

Creatures that encounter an _emotion ooze_ find that it mimics their expressions and movements in an unnerving manner, sometimes even duplicating the facial features of the creature as it mimics a smile or growl. The ooze’s reactions get more extreme when creatures around it express the type of emotion to which the ooze is attuned. The ooze begins to noticeably ripple, pulsing in a sympathetic rhythm and reshaping itself more rapidly than it does when it is on the search for emotional creatures. An anger-attuned ooze might form its pseudopods to look more like jagged spikes, and a despair ooze might reach out fitfully like a creature struggling to escape from a pool of quicksand.

Most animals and unintelligent life forms find an _emotion ooze_’s imitation and emotional echoes terrifying and flee as quickly as possible. Though some sentient creatures have this same reaction, others find the phenomenon fascinating, and attempt to either experiment with or capture emotion oozes, putting themselves within reach of the hungry oozes’ _[[spells/Grasp|grasp]]_. These intelligent creatures are the most common victims of _emotion ooze_ attacks.

Pitched battles draw the attentions of emotion oozes attuned to anger, _fear_, hatred, or zeal. Such an ooze might join a nearby battle it senses so it can feed off the emotions generated there. The desire to continue causing and absorbing such strong feelings causes the ooze to try to prolong the battle, spreading out its attacks among multiple targets and paying little attention to creatures that aren’t affected by its ability to compel emotion. In the end, the ooze’s hunger might actually be its downfall.

Emotion oozes often dwell in places where strong emotions were felt in the past, suggesting the creatures might have latent psychometric ability. Hatred oozes might live at the sites of massacres, zeal oozes in old temples or political offices, despair oozes in ancient prisons, and so on. If stuck in one place or deprived of emotional connections for a long time, an _emotion ooze_ begins to lose its coloration, becoming a dull white, and eventually hardens and cracks into pieces.

The typical _emotion ooze_ has about the same volume as a human, but its composition makes it significantly lighter, weighing only around 50 pounds.