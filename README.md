# PokemonTypeScorer
This project was inspired by GameFreak's Pokemon games that debuted in the 90s. If you haven't played them, I highly recommend that you do. Anyway, I grew up playing these games and still do to this day. The idea for this program spawned from a question I constantly asked myself: what is the best Pokemon type in this game? So this program is an attempt to rate all Pokemon types based on a given generation. I had written something similar in Java a while ago and wanted to learn Python so I translated the code.

**PS:** My favorite type is Normal. Snorlax and Slacking FTW! Misdreavus is a close second.

## Installation
Just download the source code and you're good. It is worth noting that you'll need some programming experience to get the most out of this. All I've done here is set up the logistical framework that you can build upon.
The program does rely on the `json` and `tkinter` modules, which I believe come standard with Python. If not, they'll likely be made available with the `pip install` command.

This was written in Python 3.6.8 and I don't intend on making it compatible with Python 2. 

## Usage
You'll find a Python script titled `main.py` that is set up to print out the ratings. You are welcome to change the weight functions in `main.py` and/or change the `rate(self, *args, **kwargs)` function which can be found in `matchupManager.py`.

You can also execute the `matchupView.py` file for a much easier matchup viewing experience. Though, there is still much to be desired. 
`matchupView.py` can be launched from the command line for slightly more flexibility.

## Generation VII Results
In case you don't want to download the source code to just see my results (worst to best) for Generation VII, here they are: 

|Type Name|Rating|
|:--------|-----:|
|Bug|0.0|
|Poison|0.13534589453489448|
|Ice|0.1675727395782371|
|Normal|0.18581613739112593|
|Bug_Ice|0.19340807956021275|
|Bug_Grass|0.19401434775285537|
|Psychic|0.23092726548555081|
|Grass|0.23592486709074448|
|Flying|0.2433922735767783|
|Fairy_Ice|0.26344418630536226|
|Bug_Flying|0.28964275646361726|
|Ice_Rock|0.2991219872902185|
|Normal_Poison|0.3021838901933353|
|Bug_Poison|0.3076260242218763|
|Flying_Ice|0.32161747754503706|
|Flying_Normal|0.3223155554396681|
|Fairy|0.32324416714399706|
|Bug_Normal|0.32412279208961314|
|Bug_Fighting|0.3314608743238214|
|Dragon|0.33474720672706343|
|Grass_Ice|0.3353007107395297|
|Fighting|0.33824834227591066|
|Bug_Fairy|0.3431438458870419|
|Ghost_Psychic|0.3494097811537979|
|Rock|0.35332411735970926|
|Flying_Psychic|0.3606816898428299|
|Ice_Normal|0.36756255694067064|
|Ice_Psychic|0.3791189434223902|
|Bug_Dragon|0.3829485518720854|
|Dragon_Ice|0.3872917322417113|
|Bug_Rock|0.3885478681135296|
|Fire|0.38987905227188024|
|Bug_Psychic|0.3899763296019668|
|Normal_Psychic|0.3937403084227054|
|Poison_Rock|0.3968275809309078|
|Flying_Poison|0.3992027479975183|
|Fire_Ice|0.4037174836048766|
|Ice_Steel|0.4164469312746641|
|Poison_Psychic|0.4173130163950025|
|Ghost|0.4218003847212582|
|Fairy_Psychic|0.42977354428663195|
|Dragon_Flying|0.4375446729965155|
|Ice_Poison|0.4455425088988257|
|Flying_Grass|0.4546861357424844|
|Electric|0.45500197922404123|
|Dark_Psychic|0.4623696064230015|
|Dragon_Psychic|0.4650957822830549|
|Dragon_Normal|0.46642052751510443|
|Fairy_Flying|0.4718249358389605|
|Fairy_Rock|0.47487185430504075|
|Dark|0.4804803363457828|
|Normal_Rock|0.48137812456496226|
|Dragon_Grass|0.48155346977392305|
|Fairy_Normal|0.4839800524371323|
|Fairy_Poison|0.48461171025969524|
|Dark_Ghost|0.4860859422336145|
|Fairy_Grass|0.48970459783872894|
|Psychic_Rock|0.4929345110466819|
|Dragon_Poison|0.49949776363423387|
|Dragon_Rock|0.49966545608341617|
|Grass_Rock|0.5059847181844994|
|Grass_Poison|0.509214876823372|
|Steel|0.5192255866486736|
|Bug_Steel|0.5236098017588044|
|Flying_Rock|0.5261777492449691|
|Bug_Fire|0.5281351634453763|
|Electric_Rock|0.5296689165907413|
|Bug_Ghost|0.5344131926084729|
|Grass_Psychic|0.5349966582640058|
|Grass_Normal|0.5363214034960553|
|Dark_Normal|0.5428633895433401|
|Flying_Ghost|0.5450707149395352|
|Dragon_Fairy|0.5554956892416868|
|Ghost_Ice|0.568241013705153|
|Ghost_Poison|0.5707193631617431|
|Fighting_Poison|0.5736626089639957|
|Fire_Rock|0.5812521168820382|
|Ice_Water|0.5827115617608845|
|Ghost_Normal|0.5828623787054683|
|Bug_Dark|0.5839942421081945|
|Rock_Steel|0.5920699541499254|
|Fairy_Ghost|0.5954057397485444|
|Electric_Ice|0.5958010020236163|
|Fire_Poison|0.6013373391776965|
|Fighting_Normal|0.6013617397093574|
|Dark_Ice|0.6041209115697699|
|Fighting_Psychic|0.6055420352888706|
|Poison_Steel|0.6082377143370581|
|Fire_Flying|0.6092296309037835|
|Fire_Grass|0.6119310404376502|
|Water|0.6162118108598571|
|Electric_Poison|0.6191364841081185|
|Dark_Flying|0.623686323452041|
|Fighting_Grass|0.6262730803020056|
|Ground|0.6284536213648816|
|Dragon_Fighting|0.6310410307056707|
|Dragon_Ghost|0.6325877649805542|
|Dark_Dragon|0.6404345219998884|
|Fire_Steel|0.641207187715178|
|Ghost_Rock|0.6424917848453274|
|Electric_Grass|0.6431532109441871|
|Bug_Electric|0.6483664348522812|
|Fire_Normal|0.649651041486586|
|Grass_Steel|0.6505544354168777|
|Dark_Poison|0.6549852815325001|
|Fighting_Ice|0.6601718082458468|
|Dragon_Fire|0.6624372504324374|
|Electric_Flying|0.6651568977605132|
|Fighting_Flying|0.6668560884143488|
|Fairy_Fighting|0.6732265235753935|
|Dark_Fairy|0.6790769175977559|
|Ghost_Grass|0.6837318113267123|
|Electric_Fire|0.6855187678079105|
|Bug_Ground|0.6857214048500657|
|Electric_Psychic|0.6861201780490983|
|Fairy_Steel|0.6871768350761183|
|Grass_Water|0.6873584891656889|
|Electric_Normal|0.6874449232811479|
|Dark_Rock|0.6889019201812777|
|Fairy_Fire|0.6889246767677362|
|Fire_Water|0.6897211525477253|
|Grass_Ground|0.6960273958594771|
|Flying_Steel|0.6968716905456974|
|Fighting_Ghost|0.700226682255542|
|Fighting_Ground|0.7034962658131356|
|Dark_Fighting|0.703904204112466|
|Fire_Psychic|0.7131387096378101|
|Psychic_Steel|0.7203215260686708|
|Ground_Ice|0.7230430459734936|
|Rock_Water|0.7248374098551155|
|Flying_Ground|0.7282078242570466|
|Dragon_Steel|0.7284365753889037|
|Ground_Psychic|0.7310522783959741|
|Electric_Ghost|0.7316175124589173|
|Normal_Steel|0.7319702755917116|
|Fighting_Fire|0.733152454339556|
|Ground_Rock|0.7365406500658638|
|Dragon_Electric|0.7402021345942079|
|Electric_Fairy|0.7409370649217067|
|Dragon_Water|0.7468780673097063|
|Dragon_Ground|0.7538630025216971|
|Fighting_Rock|0.7577863151803542|
|Ground_Normal|0.7582689799253365|
|Fire_Ghost|0.7586360440476289|
|Flying_Water|0.7653672067349649|
|Dark_Grass|0.7728797581251546|
|Ghost_Ground|0.7744271716141071|
|Fire_Ground|0.7815335606537475|
|Bug_Water|0.7855120732537924|
|Ground_Poison|0.7957752066116389|
|Dark_Fire|0.7971310484448545|
|Psychic_Water|0.7980297173711932|
|Normal_Water|0.7993544626032428|
|Dark_Electric|0.8020086296225667|
|Electric_Water|0.814653440088041|
|Electric_Steel|0.8270377860660705|
|Electric_Fighting|0.8315615082620414|
|Ghost_Water|0.8435270517810121|
|Fairy_Ground|0.8493306510546246|
|Fairy_Water|0.8528466042438018|
|Poison_Water|0.8648750867785436|
|Dark_Ground|0.8728326862667551|
|Fighting_Steel|0.8749433175912099|
|Ghost_Steel|0.8908339675941432|
|Electric_Ground|0.9055584501937282|
|Dark_Steel|0.91156366762475|
|Dark_Water|0.9139181689446616|
|Ground_Water|0.9196989503933978|
|Steel_Water|0.9220391866886416|
|Fighting_Water|0.9322989546971218|
|Ground_Steel|1.0|