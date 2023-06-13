---
cssclass: [monsters]
title1: Charnel Colossus
desc_short: This horror is composed of dozens, if not hundreds, of decomposing cadavers
  held together as an amalgamated whole.
title2: Charnel Colossus
CR: 19
sources:
- name: Inner Sea Bestiary
  page: 10
  link: http://paizo.com/products/btpy8v2x?Pathfinder-Campaign-Setting-Inner-Sea-Bestiary
XP: 204800
alignment: NE
size: Colossal
type: undead
initiative:
  bonus: 3
senses:
  darkvision: 60
  see invisibility: true
AC:
  AC: 29
  touch: 1
  flat_footed: 29
  components:
    dex: -1
    natural: 28
    size: -8
HP:
  HP: 345
  long: 30d8+210
saves:
  fort: 19
  ref: 11
  will: 32
defensive_abilities:
- amorphous
- channel resistance +4
DR:
- amount: 15
  weakness: magic and slashing
immunities:
- critical hits
- precision damage
- turning
- undead traits
SR: 30
speeds:
  base: 30
attacks:
  melee:
  - - text: 6 slams +26 (2d8+12/19-20 plus grab and mind feed)
      entries:
      - - damage: 2d8+12
          crit_range: 19-20
        - effect: grab
        - effect: mind feed
      count: 6
      attack: slams
      bonus:
      - 26
  - - text: 2 tendrils +21 (2d6+6 plus grab and pull)
      entries:
      - - damage: 2d6+6
        - effect: grab
        - effect: pull
      count: 2
      attack: tendrils
      bonus:
      - 21
  special:
  - voice of the ancients
space: 30
reach: 20
reach_other: 40 ft. with tendrils
spell_like_abilities:
  entries:
  - name: see invisibility
    source: default
    freq: Constant
  - name: augury
    source: default
    freq: At will
  - name: blindness/deafness
    source: default
    freq: At will
    DC: 20
  - name: doom
    source: default
    freq: At will
    DC: 18
  - name: bestow curse
    source: default
    freq: 3/day
    DC: 20
  - name: speak with dead
    source: default
    freq: 3/day
    DC: 20
  - name: unholy blight
    source: default
    freq: 3/day
    DC: 21
  - name: blasphemy
    source: default
    freq: 1/day
    DC: 24
  - name: horrid wilting
    source: default
    freq: 1/day
    DC: 25
  sources:
  - name: default
    CL: 18
    concentration: 25
ability_scores:
  STR: 34
  DEX: 9
  CON:
  INT: 18
  WIS: 36
  CHA: 25
BAB: 22
CMB: 42
CMB_other: +46 grapple
CMD: 51
CMD_other: can't be tripped
feats:
- name: Ability Focus (voice of the ancients)
- name: Alertness
- name: Blind- Fight
- name: Combat Reflexes
- name: Critical Focus
- name: Great Fortitude
- name: Improved Critical (slam)
- name: Improved Initiative
- name: Improved Iron Will
- name: Iron Will
- name: Lightning Reflexes
- name: Power Attack
- name: Staggering Critical
- name: Stand Still
- name: Stunning Critical
skills:
  Climb: 45
  Intimidate: 40
  Knowledge (arcana): 37
  Knowledge (history): 34
  Knowledge (religion): 37
  Perception: 50
  Sense Motive: 50
  Spellcraft: 37
languages:
- Common (or the most commonly spoken language of its corporate body)
special_qualities:
- corporate will
ecology:
  environment: any (Kalexcourt, Ustalav)
  organization: solitary
  treasure_type: standard
special_abilities:
  Corporate Will (Su): A charnel colossus is composed of the sentience of scores of
    creatures. Though they are able to work in concert as a cohesive whole, they are
    also able to separate their actions at will so as to not be impeded by the limitations
    of a single consciousness, effectively allowing them to focus on two things at
    once. As a result, the charnel colossus can use up to two spell-like abilities
    in the same round that it makes physical attacks or other fullfound actions. It
    also gains an additional spell attack per round. In addition, a charnel colossus
    is immune to being turned (though it can still take damage from channeled positive
    energy). While part of the creature's sentience may be affected by a turn attempt,
    there are enough unaffected intellects within to override the effect.
  Mind Feed (Su): When a charnel colossus succeeds at a grapple check with a slam
    attack, it can use its mind feed ability as a free action during each round in
    which the grapple is maintained. A victim of a mind feed attempt must succeed
    at a DC 38 Will save each round that the ability is used. On a failed save, the
    cadavers that make up the charnel colossus lock their mouths against the victim
    and begin to draw forth a part of her sentience to add to the collective. This
    action deals 1d6 points of Wisdom damage per round. If the victim's Wisdom score
    is reduced to 0, her soul and persona are wholly subsumed by the charnel colossus,
    and her body becomes bleached white and brittle and is incorporated into the creature's
    mass. The charnel colossus then has full access to all of the victim's memories
    (though not any special powers), and the victim can only be recovered and returned
    to life with a wish or miracle. If the charnel colossus has grappled multiple
    victims, it can attempt multiple mind feeds in a single round. The save DC is
    Wisdom-based.
  Voice of the Ancients (Su): |-
    A charnel colossus can, as a full-round action, cause its collective knowledge to be whispered into the minds of any sentient creature within 100 feet. These whispers riffle through the brain of any such creatures within range in a maddening susurrus. These individuals must succeed at a DC 34 Will save or be paralyzed and frozen in place as if by the hold monster spell. The victim may attempt a new save each round to try and break the effect.

    Regardless of whether or not the save is successful, the effect leaves an insidious seed implanted in the victim's mind. The day after the save is made, the victim must succeed at a new save or the seed takes root and creates the subconscious compulsion for the victim to return to the charnel colossus at some point in the future. When and how this occurs is up the GM. This compulsion can be removed with a remove curse spell or by destroying the charnel colossus that implanted the compulsion.

    This is a mind-affecting compulsion and cannot be negated by a silence spell because it is heard directly in the mind of the victim. Each time a creature is subjected to this attack, there is a 1% chance that some of the lost lore transmitted into her mind causes her to gain a permanent +2 bonus to Intelligence. This beneficial side effect can only occur to a creature once. When a charnel colossus uses this ability, it cannot use its spell-like abilities or take other actions in that round. The save DC is Charisma-based.
desc_long: |-
  Some dead don't rest easy because of the circumstances of their death or the horrific experiences they underwent in life. Their souls return to the world of the living demanding justice, revenge, or just wanton destruction. Some dead, however, never intended for their souls to leave. Instead they wished to preserve their knowledge, their culture, or some other aspect of their life in an undying form that could forever accumulate more of the same. In these instances, where lichdom is not sought as a viable option, and a multitude of individuals wish to take part, the result can be a charnel colossus.

  A charnel colossus is an amalgam of scores, even hundreds, of individuals who, upon death, chose to be interred under special ritual circumstances with others of like mind. This allowed them to feed their individual life experiences into an undying corporation of the collective whole. The resulting monstrosity would be like a living library-if it were living. The individual will of the deceased participants is subsumed in favor of a hive-like personality composed of all of the knowledge and experiences of the individual contributors. A few dominant or powerful members of this amalgam may give the resulting combined creature a general style of behavior, but no single constituent provides the creature with a true guiding force. Instead, the result is a pooling of the wisdom and experience of those who have been so interred-often over a period spanning hundreds of years-creating an abomination whose sole focus is the perpetuation of any such cultural traditions and the acquisition of more constituent parts to ever expand its breadth of experience. It is this guiding gluttony for further expansion of consciousness that ensures that even the most benign of traditions or experiential pools from which a charnel colossus is formed inevitably results in an all-consuming horror.

  The charnel colossus is a mass of the corpses that form its composition, often intermixed with earth, broken grave goods, and other burial materials if the decayed bodies alone are insufficient to fill out its massive size. This amorphous whole is collected within a membrane through which the individual corpses can still be seen and against which they often press as if seeking their freedom. But when a creature becomes trapped in the embrace of a colossus, the membrane proves to be permeable-the rotten, lipless mouths of those so interred are able to reach forth and feed upon the victim's own life experience. The colossus can also form two thin tendrils of this charnel stuff in order to lash out and draw prey into its embrace.

  As powerful, ever-hungering abominations, charnel colossi are thankfully few and far between. The only documented one currently known to exist is reported to be trapped beneath the ruins of Kalexcourt in northwestern Ustalav, in an ancient Kellid shamanistic burial site.

---

# Charnel Colossus
This horror is composed of dozens, if not hundreds, of decomposing cadavers held together as an amalgamated whole.
**Source** Inner Sea Bestiary pg. 10
**XP** 204,800

NE Colossal undead
**Init** +3; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/See Invisibility|see invisibility]]_; Perception +50

##### Defense

**AC** 29, touch 1, _[[conditions/Flat-Footed|flat-footed]]_ 29 (–1 Dex, +28 natural, –8 size)
**hp** 345 (30d8+210)
**Fort** +19, **Ref** +11, **Will** +32
**Defensive Abilities** _[[universal monster rules/Amorphous|amorphous]]_, _[[universal monster rules/Channel Resistance|channel resistance]]_ +4; **DR** 15/magic and slashing; **Immune** critical hits, precision damage, turning, _[[universal monster rules/Undead Traits|undead traits]]_; **SR** 30

##### Offense
**Speed** 30 ft.
**Melee** 6 slams +26 (2d8+12/19–20 plus _[[universal monster rules/Grab|grab]]_ and mind feed) or 2 tendrils +21 (2d6+6 plus _grab_ and _[[universal monster rules/Pull|pull]]_)
**Space** 30 ft., **Reach** 20 ft. (40 ft. with tendrils)
**Special Attacks** voice of the ancients
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 18th; concentration +25)
Constant—_see invisibility_
At will—_[[spells/Augury|augury]]_, blindness/deafness (DC 20), _[[spells/Doom|doom]]_ (DC 18)
3/day—_[[spells/Bestow Curse|bestow curse]]_ (DC 20), _[[spells/Speak with Dead|speak with dead]]_ (DC 20), _[[spells/Unholy Blight|unholy blight]]_ (DC 21)
1/day—_[[spells/Blasphemy|blasphemy]]_ (DC 24), _[[spells/Horrid Wilting|horrid wilting]]_ (DC 25)

##### Statistics
**Str** 34, **Dex** 9, **Con** —, **Int** 18, **Wis** 36, **Cha** 25
**Base Atk** +22; **CMB** +42 (+46 grapple); **CMD** 51 (can’t be tripped)
**Feats** _[[feats/Ability Focus|Ability Focus]]_ (voice of the ancients), _[[feats/Alertness|Alertness]]_, Blind- Fight, _[[feats/Combat Reflexes|Combat Reflexes]]_, _[[feats/Critical Focus|Critical Focus]]_, _[[feats/Great Fortitude|Great Fortitude]]_, _[[feats/Improved Critical|Improved Critical]]_ (slam), _[[feats/Improved Initiative|Improved Initiative]]_, _[[feats/Improved Iron Will|Improved Iron Will]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Lightning Reflexes|Lightning Reflexes]]_, _[[feats/Power Attack|Power Attack]]_, _[[feats/Staggering Critical|Staggering Critical]]_, _[[feats/Stand Still|Stand Still]]_, _[[feats/Stunning Critical|Stunning Critical]]_
**Skills** _[[universal monster rules/Climb|Climb]]_ +45, Intimidate +40, Knowledge (arcana) +37, Knowledge (history) +34, Knowledge (religion) +37, Perception +50, Sense Motive +50, Spellcraft +37
**Languages** Common (or the most commonly spoken language of its corporate body)
**SQ** corporate will

##### Ecology

**Environment** any (Kalexcourt, Ustalav)
**Organization** solitary
**Treasure** standard

### Special Abilities

**Corporate Will (Su)** A _[[monsters/Charnel Colossus|charnel colossus]]_ is composed of the sentience of scores of creatures. Though they are able to work in concert as a cohesive whole, they are also able to separate their actions at will so as to not be impeded by the limitations of a single consciousness, effectively allowing them to focus on two things at once. As a result, the _charnel colossus_ can use up to two _spell-like abilities_ in the same round that it makes physical attacks or other fullfound actions. It also gains an additional spell attack per round. In addition, a _charnel colossus_ is immune to being turned (though it can still take damage from channeled positive energy). While part of the creature’s sentience may be affected by a turn attempt, there are enough unaffected intellects within to override the effect.

**Mind Feed (Su) **When a _charnel colossus_ succeeds at a grapple check with a slam attack, it can use its mind feed ability as a free action during each round in which the grapple is maintained. A victim of a mind feed attempt must succeed at a DC 38 Will save each round that the ability is used. On a failed save, the cadavers that make up the _charnel colossus_ lock their mouths against the victim and begin to draw forth a part of her sentience to add to the collective. This action deals 1d6 points of Wisdom damage per round. If the victim’s Wisdom score is reduced to 0, her soul and persona are wholly subsumed by the _charnel colossus_, and her body becomes bleached white and brittle and is incorporated into the creature’s mass. The _charnel colossus_ then has full access to all of the victim’s memories (though not any special powers), and the victim can only be recovered and returned to life with a _[[spells/Wish|wish]]_ or _[[spells/Miracle|miracle]]_. If the _charnel colossus_ has _[[conditions/Grappled|grappled]]_ multiple victims, it can attempt multiple mind feeds in a single round. The save DC is Wisdom-based.

**Voice of the Ancients (Su)** A _charnel colossus_ can, as a full-round action, cause its collective knowledge to be whispered into the minds of any sentient creature within 100 feet. These whispers riffle through the brain of any such creatures within range in a maddening susurrus. These individuals must succeed at a DC 34 Will save or be _[[conditions/Paralyzed|paralyzed]]_ and frozen in place as if by the _[[spells/Hold Monster|hold monster]]_ spell. The victim may attempt a new save each round to try and break the effect.

Regardless of whether or not the save is successful, the effect leaves an insidious seed implanted in the victim’s mind. The day after the save is made, the victim must succeed at a new save or the seed takes _[[spells/Root|root]]_ and creates the subconscious compulsion for the victim to return to the _charnel colossus_ at some point in the future. When and how this occurs is up the GM. This compulsion can be removed with a _[[spells/Remove Curse|remove curse]]_ spell or by destroying the _charnel colossus_ that implanted the compulsion.

This is a mind-affecting compulsion and cannot be negated by a _[[spells/Silence|silence]]_ spell because it is heard directly in the mind of the victim. Each time a creature is subjected to this attack, there is a 1% chance that some of the lost lore transmitted into her mind causes her to gain a permanent +2 bonus to Intelligence. This beneficial side effect can only occur to a creature once. When a _charnel colossus_ uses this ability, it cannot use its _spell-like abilities_ or take other actions in that round. The save DC is Charisma-based.

##### Description

Some dead don’t rest easy because of the circumstances of their death or the horrific experiences they underwent in life. Their souls return to the world of the living demanding justice, revenge, or just wanton _[[spells/Destruction|destruction]]_. Some dead, however, never intended for their souls to leave. Instead they wished to _[[spells/Preserve|preserve]]_ their knowledge, their culture, or some other aspect of their life in an undying form that could forever accumulate more of the same. In these instances, where lichdom is not sought as a viable option, and a multitude of individuals _wish_ to take part, the result can be a _charnel colossus_.

A _charnel colossus_ is an amalgam of scores, even hundreds, of individuals who, upon death, chose to be interred under special ritual circumstances with others of like mind. This allowed them to feed their individual life experiences into an undying corporation of the collective whole. The resulting monstrosity would be like a living library—if it were living. The individual will of the deceased participants is subsumed in favor of a hive-like personality composed of all of the knowledge and experiences of the individual contributors. A few dominant or powerful members of this amalgam may give the resulting combined creature a general style of behavior, but no single constituent provides the creature with a true guiding force. Instead, the result is a pooling of the wisdom and experience of those who have been so interred—often over a period spanning hundreds of years—creating an abomination whose sole focus is the perpetuation of any such cultural traditions and the acquisition of more constituent parts to ever expand its _[[feats/Breadth of Experience|breadth of experience]]_. It is this guiding gluttony for further expansion of consciousness that ensures that even the most benign of traditions or experiential pools from which a _charnel colossus_ is formed inevitably results in an all-consuming horror.

The _charnel colossus_ is a mass of the corpses that form its composition, often intermixed with earth, _[[conditions/Broken|broken]]_ grave goods, and other burial materials if the decayed bodies alone are insufficient to fill out its massive size. This _amorphous_ whole is collected within a membrane through which the individual corpses can still be seen and against which they often press as if seeking their _[[spells/Freedom|freedom]]_. But when a creature becomes trapped in the embrace of a colossus, the membrane proves to be permeable—the rotten, lipless mouths of those so interred are able to reach forth and feed upon the victim’s own life experience. The colossus can also form two thin tendrils of this charnel stuff in order to lash out and draw prey into its embrace.

As powerful, ever-hungering abominations, charnel colossi are thankfully few and far between. The only documented one currently known to exist is reported to be trapped beneath the ruins of Kalexcourt in northwestern Ustalav, in an ancient Kellid shamanistic burial site.