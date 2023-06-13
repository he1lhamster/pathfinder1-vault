---
cssclass: [monsters]
title1: Ayandamahla, the Crimson Lotus
desc_short: This pale woman is as beautiful as she is menacing-her smile promises
  endless bliss, yet her weapons and fangs drip with blood.
title2: Ayandamahla, the Crimson Lotus
CR: 24
sources:
- name: Demons Revisited
  page: 56
  link: http://paizo.com/products/btpy8yvo?Pathfinder-Campaign-Setting-Demons-Revisited
XP: 1228800
race: Female
classes:
- succubus bard 20 (Pathfinder RPG Bestiary 68)
alignment: CE
size: Medium
type: outsider
subtypes:
- chaotic
- demon
- evil
- extraplanar
initiative:
  bonus: 5
senses:
  darkvision: 60
  detect good: true
AC:
  AC: 41
  touch: 21
  flat_footed: 35
  components:
    armor: 9
    deflection: 5
    dex: 5
    dodge: 1
    natural: 10
    shield: 1
HP:
  HP: 490
  long: 8d10+20d8+356
  HD: 28
saves:
  fort: 24
  ref: 28
  will: 26
  other: +4 vs. bardic performance, language-dependent, and sonic
DR:
- amount: 10
  weakness: cold iron or good
immunities:
- electricity
- fire
- poison
resistances:
  acid: 10
  cold: 10
SR: 18
speeds:
  base: 30
  fly: 50
  fly_maneuverability: average
attacks:
  melee:
  - - text: +5 speed wounding rapier +31/+31/+26/+21/+16 (1d6+10/18-20)
      entries:
      - - damage: 1d6+10
          crit_range: 18-20
      attack: +5 speed wounding rapier
      bonus:
      - 31
      - 31
      - 26
      - 21
      - 16
    - text: +5 wounding unholy whip +31/+26/+21 (1d3+10)
      entries:
      - - damage: 1d3+10
      attack: +5 wounding unholy whip
      bonus:
      - 31
      - 26
      - 21
  special:
  - bardic performance 56 rounds/day (swift action, countersong, deadly performance,
    dirge of doom, distraction, fascinate, frightening tune, inspire competence +6,
    inspire courage +4, inspire greatness, inspire heroics, mass suggestion, soothing
    performance, suggestion)
  - energy drain
  - profane gift
spell_like_abilities:
  entries:
  - name: detect good
    source: default
    freq: Constant
  - name: tongues
    source: default
    freq: Constant
  - name: charm monster
    source: default
    freq: At will
    DC: 28
  - name: detect thoughts
    source: default
    freq: At will
    DC: 26
  - name: ethereal jaunt
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: greater teleport
    source: default
    freq: At will
    other: self plus 50 lbs. of objects only
  - name: suggestion
    source: default
    freq: At will
    DC: 27
  - name: dominate person
    source: default
    freq: 1/day
    DC: 29
  - name: summon
    source: default
    freq: 1/day
    level: 3
    summons:
    - name: babau
      amount: 1
      chance: 50%
  sources:
  - name: default
    CL: 12
    concentration: 26
spells:
  entries:
  - name: mass charm monster
    source: Bard
    level: 6
    DC: 30
  - name: geas/quest
    source: Bard
    level: 6
  - name: irresistible dance
    source: Bard
    level: 6
  - name: project image
    source: Bard
    level: 6
    DC: 30
  - name: veil
    source: Bard
    level: 6
    DC: 30
  - name: mind fog
    source: Bard
    level: 5
    DC: 29
  - name: nightmare
    source: Bard
    level: 5
    DC: 29
  - name: persistent image
    source: Bard
    level: 5
    DC: 29
  - name: song of discord
    source: Bard
    level: 5
    DC: 29
  - name: mass suggestion
    source: Bard
    level: 5
    DC: 29
  - name: cure critical wounds
    source: Bard
    level: 4
  - name: dominate person
    source: Bard
    level: 4
    DC: 28
  - name: freedom of movement
    source: Bard
    level: 4
  - name: invisibility
    source: Bard
    level: 4
  - name: modify memory
    source: Bard
    level: 4
    DC: 28
  - name: zone of silence
    source: Bard
    level: 4
  - name: confusion
    source: Bard
    level: 3
    DC: 27
  - name: cure serious wounds
    source: Bard
    level: 3
  - name: dispel magic
    source: Bard
    level: 3
  - name: displacement
    source: Bard
    level: 3
  - name: major image
    source: Bard
    level: 3
    DC: 27
  - name: scrying
    source: Bard
    level: 3
    DC: 27
  - name: blindness/deafness
    source: Bard
    level: 2
    DC: 26
  - name: cure moderate wounds
    source: Bard
    level: 2
  - name: hold person
    source: Bard
    level: 2
    DC: 26
  - name: mirror image
    source: Bard
    level: 2
  - name: misdirection
    source: Bard
    level: 2
  - name: sound burst
    source: Bard
    level: 2
    DC: 26
  - name: animate rope
    source: Bard
    level: 1
  - name: cure light wounds
    source: Bard
    level: 1
  - name: feather fall
    source: Bard
    level: 1
  - name: hideous laughter
    source: Bard
    level: 1
    DC: 25
  - name: silent image
    source: Bard
    level: 1
    DC: 25
  - name: undetectable alignment
    source: Bard
    level: 1
  - name: dancing lights
    source: Bard
    level: 0
  - name: detect magic
    source: Bard
    level: 0
  - name: ghost sound
    source: Bard
    level: 0
    DC: 24
  - name: message
    source: Bard
    level: 0
  - name: prestidigitation
    source: Bard
    level: 0
  - name: summon instrument
    source: Bard
    level: 0
  sources:
  - name: Bard
    type: known
    CL: 20
    concentration: 34
    slots:
      6: 8
      5: 8
      4: 8
      3: 8
      2: 9
      1: 9
      0: at-will
ability_scores:
  STR: 20
  DEX: 20
  CON: 32
  INT: 20
  WIS: 12
  CHA: 38
BAB: 23
CMB: 28
CMD: 49
feats:
- name: Combat Expertise
- name: Craft Magic Arms and Armor
- name: Dodge
- name: Double Slice
- name: Greater Two-Weapon Fighting
- name: Improved Two-Weapon Fighting
- superscripts:
  - UC
  name: Improved Whip Mastery
- name: Iron Will
- name: Quicken Spell
- superscripts:
  - UM
  name: Spellsong
- name: Toughness
- name: Two-Weapon Defense
- name: Two-Weapon Fighting
- superscripts:
  - UC
  name: Whip Mastery
skills:
  Acrobatics: 45
  Bluff: 45
  Diplomacy: 45
  Disguise: 45
  Fly: 45
  Intimidate: 31
  Knowledge (arcana): 32
  Knowledge (local): 32
  Knowledge (nobility): 32
  Knowledge (planes): 32
  Knowledge (religion): 32
  Perception: 40
  Perform (act): 45
  Perform (dance): 45
  Perform (oratory): 45
  Perform (sing): 45
  Perform (string): 45
  Sense Motive: 45
  Stealth: 36
  Use Magic Device: 45
languages:
- Abyssal
- Celestial
- Common
- Draconic
- telepathy 100 ft.
special_qualities:
- bardic knowledge +10
- change shape (alter self, Small or Medium humanoid)
- jack-of-all-trades (use any skill, all skills are class skills, take 10 on any skill)
- lore master 3/day
- versatile performance (act, dance, oratory, sing, string)
gear:
  gear:
  - +5 mithral chain shirt
  - +5 speed wounding rapier
  - +5 wounding unholy whip
  - amulet of natural armor +3
  - belt of physical might +6 (Str, Con)
  - cloak of resistance +5
  - headband of alluring charisma +6
  - ring of protection +5
  - strand of prayer beads (standard)
  - statuette of herself worth 3,400 gp (for project image)
  - 3,479 gp
desc_long: |-
  Ayandamahla was first conjured by Runelord Sorshen on the evening she and the other runelords were to meet to discuss the removal of King Xin from power. Sorshen expected treachery at the hands of her fellow runelords, and promised Ayandamahla a week of freedom among her subjects in the nation of Eurythnia if the succubus would promise to aid her in the event of betrayal by one of the other rulers of Thassilon. As it worked out, the only betrayal that night was that of the runelords against Xin himself, but Sorshen did not renege on her promise to the Crimson Lotus. Thus began a relationship that would last the rest of Thassilon's existence-Ayandamahla would not only serve numerous times as Sorshen's spy, assassin, messenger, champion, executioner, and lover, but would also aid her in her research into the nature of blood and its relationship to eternal life. Sorshen also made Ayandamahla the warden of the Lady's Light, an immense tower Sorshen had erected at the westernmost edge of her realm.

  When Sorshen learned that the end of Thassilon was nigh, she betrayed Ayandamahla-knowing that the succubus would not deign to remain as the protector of the Lady's Light once the runelord retreated into her secret vaults to wait out Earthfall, she worked a powerful binding spell to ensure that Ayandamahla would remain within the Light until Sorshen returned. The Crimson Lotus was enraged, both at Sorshen and at herself for being duped. She watched from atop the Lady's Light as Earthfall ended the world she'd helped build, used her magic and that of the Lady's Light to protect the statue from the earthquakes and tsunami that would have otherwise destroyed it, then retreated into the Light to wait out eternity. As it turned out, eternity was much shorter than the succubus expected it to be. When she discovered a flaw in Sorshen's binding spell, she managed to shift the magic to one of her alu-demon daughters and escaped back to the Abyss.

  In the 10,000 years since her service to Sorshen ended in betrayal, Ayandamahla never again forged as prosperous an alliance as that with the runelord. Instead, she has used mortals increasingly as her own tools, attended to duties for her own mistress, Zura, as needed, and has worked to perfect her skills at seduction, subversion, and slaughter the entire time. Throughout it all, the deadly creature has kept one eye on Varisia, watching patiently for any signs of Sorshen's return to the region. Even today, more powerful than ever before, Ayandamahla doubts she could match the runelord in power-but if Sorshen rises once again, the succubus plans to be there to have her revenge.

---

# Ayandamahla, the Crimson Lotus
This pale woman is as beautiful as she is _[[items/Weapon Magic Abilities/Menacing|menacing]]_—her smile promises endless bliss, yet her weapons and fangs drip with blood.
**Source** Demons Revisited pg. 56
**XP** 1,228,800
Female succubus _[[classes/Bard|bard]]_ 20 (Pathfinder RPG Bestiary 68)
CE Medium outsider (chaotic, demon, evil, extraplanar)
**Init** +5; **Senses** _[[spells/Darkvision|darkvision]]_ 60 ft., _[[spells/Detect Good|detect good]]_; Perception +40

##### Defense

**AC** 41, touch 21, _[[conditions/Flat-Footed|flat-footed]]_ 35 (+9 armor, +5 _[[spells/Deflection|deflection]]_, +5 Dex, +1 _[[feats/Dodge|dodge]]_, +10 natural, +1 _[[spells/Shield|shield]]_)
**hp** 490 (28 HD; 8d10+20d8+356)
**Fort** +24, **Ref** +28, **Will** +26; +4 vs. bardic performance, language-dependent, and sonic
**DR** 10/cold iron or good; **Immune** electricity, fire, poison; **Resist** acid 10, cold 10; **SR** 18

##### Offense
**Speed** 30 ft., fly 50 ft. (average)
**Melee** +5 speed _[[items/Weapon Magic Abilities/Wounding|wounding]]_ _[[items/Weapon/Rapier|rapier]]_ +31/+31/+26/+21/+16 (1d6+10/18–20), +5 _wounding_ _[[items/Weapon Magic Abilities/Unholy|unholy]]_ _[[items/Weapon/Whip|whip]]_ +31/+26/+21 (1d3+10)
**Special Attacks** bardic performance 56 rounds/day (swift action, countersong, _[[items/Weapon Magic Abilities/Deadly|deadly]]_ performance, dirge of _[[spells/Doom|doom]]_, _[[universal monster rules/Distraction|distraction]]_, fascinate, frightening tune, inspire competence +6, inspire courage +4, inspire greatness, inspire heroics, mass _[[spells/Suggestion|suggestion]]_, soothing performance, _suggestion_), _[[universal monster rules/Energy Drain|energy drain]]_, profane gift
**_[[universal monster rules/Spell-Like Abilities|Spell-Like Abilities]]_** (CL 12th; concentration +26)
Constant—_detect good_, _[[spells/Tongues|tongues]]_
At will—_[[spells/Charm Monster|charm monster]]_ (DC 28), _[[spells/Detect Thoughts|detect thoughts]]_ (DC 26), _[[spells/Ethereal Jaunt|ethereal jaunt]]_ (self plus 50 lbs. of objects only), greater teleport (self plus 50 lbs. of objects only), _suggestion_ (DC 27)
1/day—_[[spells/Dominate Person|dominate person]]_ (DC 29), _[[universal monster rules/Summon|summon]]_ (level 3, 1 babau 50%)
**_Bard_ Spells Known **(CL 20th; concentration +34)
6th (8/day)—mass _charm monster_ (DC 30), geas/quest, _[[spells/Irresistible Dance|irresistible dance]]_, _[[spells/Project Image|project image]]_ (DC 30), _[[spells/Veil|veil]]_ (DC 30)
5th (8/day)—_[[spells/Mind Fog|mind fog]]_ (DC 29), _[[spells/Nightmare|nightmare]]_ (DC 29), _[[spells/Persistent Image|persistent image]]_ (DC 29), _[[spells/Song of Discord|song of discord]]_ (DC 29), mass _suggestion_ (DC 29)
4th (8/day)—_[[spells/Cure Critical Wounds|cure critical wounds]]_, _dominate person_ (DC 28), _[[spells/Freedom of Movement|freedom of movement]]_, _[[spells/Invisibility|invisibility]]_, _[[spells/Modify Memory|modify memory]]_ (DC 28), _[[spells/Zone of Silence|zone of silence]]_
3rd (8/day)—_[[spells/Confusion|confusion]]_ (DC 27), _[[spells/Cure Serious Wounds|cure serious wounds]]_, _[[spells/Dispel Magic|dispel magic]]_, _[[spells/Displacement|displacement]]_, _[[spells/Major Image|major image]]_ (DC 27), _[[spells/Scrying|scrying]]_ (DC 27)
2nd (9/day)—blindness/deafness (DC 26), _[[spells/Cure Moderate Wounds|cure moderate wounds]]_, _[[spells/Hold Person|hold person]]_ (DC 26), _[[spells/Mirror Image|mirror image]]_, _[[spells/Misdirection|misdirection]]_, _[[spells/Sound Burst|sound burst]]_ (DC 26)
1st (9/day)—_[[spells/Animate Rope|animate rope]]_, _[[spells/Cure Light Wounds|cure light wounds]]_, _[[spells/Feather Fall|feather fall]]_, _[[spells/Hideous Laughter|hideous laughter]]_ (DC 25), _[[spells/Silent Image|silent image]]_ (DC 25), _[[spells/Undetectable Alignment|undetectable alignment]]_
0 (at will)—_[[spells/Dancing Lights|dancing lights]]_, _[[spells/Detect Magic|detect magic]]_, _[[spells/Ghost Sound|ghost sound]]_ (DC 24), _[[spells/Message|message]]_, _[[spells/Prestidigitation|prestidigitation]]_, _[[spells/Summon Instrument|summon instrument]]_

##### Statistics
**Str** 20, **Dex** 20, **Con** 32, **Int** 20, **Wis** 12, **Cha** 38
**Base Atk** +23; **CMB** +28; **CMD** 49
**Feats** _[[feats/Combat Expertise|Combat Expertise]]_, _[[feats/Craft Magic Arms and Armor|Craft Magic Arms and Armor]]_, _Dodge_, _[[feats/Double Slice|Double Slice]]_, _[[feats/Greater Two-Weapon Fighting|Greater Two-Weapon Fighting]]_, _[[feats/Improved Two-Weapon Fighting|Improved Two-Weapon Fighting]]_, _[[feats/Improved _Whip_ Mastery|Improved _Whip_ Mastery]]_, _[[feats/Iron Will|Iron Will]]_, _[[feats/Quicken Spell|Quicken Spell]]_, _[[feats/Spellsong|Spellsong]]_, _[[feats/Toughness|Toughness]]_, _[[feats/Two-Weapon Defense|Two-Weapon Defense]]_, _[[feats/Two-Weapon Fighting|Two-Weapon Fighting]]_, _[[feats/Whip Mastery|Whip Mastery]]_
**Skills** Acrobatics +45, Bluff +45, Diplomacy +45, Disguise +45, Fly +45, Intimidate +31, Knowledge (arcana) +32, Knowledge (local) +32, Knowledge (nobility) +32, Knowledge (planes) +32, Knowledge (religion) +32, Perception +40, Perform (act) +45, Perform (dance) +45, Perform (oratory) +45, Perform (sing) +45, Perform (string) +45, Sense Motive +45, Stealth +36, Use Magic Device +45
**Languages** Abyssal, Celestial, Common, Draconic; _[[universal monster rules/Telepathy|telepathy]]_ 100 ft.
**SQ** bardic knowledge +10, _[[universal monster rules/Change Shape|change shape]]_ (_[[spells/Alter Self|alter self]]_, Small or _Medium_ humanoid), jack-of-all-trades (use any skill, all skills are class skills, take 10 on any skill), lore master 3/day, versatile performance (act, dance, oratory, sing, string)
**Gear** +5 mithral _[[items/Armor/Chain shirt|chain shirt]]_, +5 speed _wounding_ _rapier_, +5 _wounding_ _unholy_ _whip_, _[[items/Wondrous Item/Amulet of Natural Armor +3|amulet of natural armor +3]]_, _[[items/Wondrous Item/Belt of Physical Might +6|belt of physical might +6]]_ (Str, Con), _[[items/Wondrous Item/Cloak of _[[universal monster rules/Resistance|Resistance]]_ +5|cloak of _resistance_ +5]]_, _[[items/Wondrous Item/Headband of Alluring Charisma +6|headband of alluring charisma +6]]_, _[[items/Ring/Ring of Protection +5|ring of protection +5]]_, strand of _[[spells/Prayer|prayer]]_ beads (standard), statuette of herself worth 3,400 gp (for _project image_), 3,479 gp

##### Description

Ayandamahla was first conjured by Runelord Sorshen on the evening she and the other runelords were to meet to discuss the removal of _[[npcs/King|King]]_ Xin from power. Sorshen expected treachery at the hands of her fellow runelords, and promised Ayandamahla a week of _[[spells/Freedom|freedom]]_ among her subjects in the nation of Eurythnia if the succubus would promise to aid her in the event of betrayal by one of the other rulers of Thassilon. As it worked out, the only betrayal that night was that of the runelords against Xin himself, but Sorshen did not renege on her promise to the Crimson Lotus. Thus began a relationship that would last the rest of Thassilon’s existence—Ayandamahla would not only serve numerous times as Sorshen’s spy, assassin, messenger, _[[items/Armor Magic Abilities/Champion|champion]]_, executioner, and lover, but would also aid her in her research into the nature of blood and its relationship to eternal life. Sorshen also made Ayandamahla the warden of the Lady’s Light, an immense tower Sorshen had erected at the westernmost edge of her realm.

When Sorshen learned that the end of Thassilon was nigh, she _[[feats/Betrayed|betrayed]]_ Ayandamahla—knowing that the succubus would not deign to remain as the protector of the Lady’s Light once the runelord retreated into her secret vaults to wait out Earthfall, she worked a powerful _[[spells/Binding|binding]]_ spell to ensure that Ayandamahla would remain within the Light until Sorshen returned. The Crimson Lotus was enraged, both at Sorshen and at herself for being duped. She watched from atop the Lady’s Light as Earthfall ended the world she’d helped build, used her magic and that of the Lady’s Light to protect the _[[spells/Statue|statue]]_ from the earthquakes and _[[spells/Tsunami|tsunami]]_ that would have otherwise destroyed it, then retreated into the Light to wait out eternity. As it turned out, eternity was much shorter than the succubus expected it to be. When she discovered a flaw in Sorshen’s _binding_ spell, she managed to shift the magic to one of her alu-demon daughters and escaped back to the Abyss.

In the 10,000 years since her service to Sorshen ended in betrayal, Ayandamahla never again forged as prosperous an alliance as that with the runelord. Instead, she has used mortals increasingly as her own tools, attended to duties for her own mistress, Zura, as needed, and has worked to perfect her skills at seduction, subversion, and slaughter the entire time. Throughout it all, the _deadly_ creature has kept one eye on Varisia, watching patiently for any signs of Sorshen’s return to the region. Even today, more powerful than ever before, Ayandamahla doubts she could match the runelord in power—but if Sorshen rises once again, the succubus plans to be there to have her revenge.