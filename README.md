# PokemonTypeScorer
This project was inspired by GameFreak's Pokemon games that debuted in the 90s. If you haven't played them, I highly recommend that you do. Anyway, I grew up playing these games and still do to this day. The idea for this program spawned from a question I consistently ask myself: what is the best Pokemon type in this game? So this program is an attempt to rate all Pokemon types based on a given generation. I did this to practice my programming skills and answer a question I've asked myself for a long time.

PS: My favorite type is Normal. Snorlax and Slacking FTW!

## Installation
Just download the source code and you're good.
It does rely on the `json` and `tkinter` modules, which I believe come standard with Python. If not, they'll likely be made available with `pip install`

This was written in Python 3.6.8 and I don't intend on making it compatible with Python 2. 

## Usage
You'll find a Python script titled `main.py` that is set up to print out the ratings. You are welcome to change the weight functions in `main.py` and/or change the `rate(self, *args, **kwargs)` function which can be found in `matchupManager.py`.

You can also execute the `matchupView.py` file for a much easier matchup viewing experience. Though, there is still much to be desired.

## Generation VII Results
In case you don't want to download the source code to just see my results for Generation VII, here they are: 

|Type Name|Rating|
|:--------|-----:|
|Bug|0.0|
|Bug_Ice|0.10535968556240363|
|Poison|0.11575596661309503|
|Ice|0.12843112755994104|
|Normal|0.14488534489674298|
|Bug_Grass|0.1508628182100872|
|Fairy_Ice|0.1663981400730134|
|Psychic|0.19379548153453324|
|Ice_Rock|0.19665357649089|
|Flying|0.22678804917960568|
|Bug_Flying|0.23081291975949272|
|Grass|0.24059641244692587|
|Flying_Ice|0.2623965910302818|
|Grass_Ice|0.275783993333419|
|Fairy|0.2764511169574321|
|Bug_Normal|0.2836813251400328|
|Ghost_Psychic|0.2882867783098895|
|Bug_Fairy|0.28902995111848395|
|Bug_Poison|0.29011914487739954|
|Dragon|0.29109525137713294|
|Flying_Normal|0.2937078058003376|
|Normal_Poison|0.29895217736508034|
|Ice_Normal|0.30039112075191804|
|Ice_Psychic|0.31225778674129967|
|Flying_Psychic|0.31653178035887036|
|Bug_Fighting|0.32459632743163785|
|Rock|0.32836326172919666|
|Bug_Rock|0.3291000302919666|
|Bug_Psychic|0.3306485155998534|
|Dragon_Ice|0.33455011269837803|
|Normal_Psychic|0.3408643558559608|
|Fighting|0.343581878427356|
|Bug_Dragon|0.34374071212480867|
|Ice_Steel|0.3593114486636101|
|Fairy_Psychic|0.36257945676094133|
|Poison_Rock|0.3796479596084946|
|Fire_Ice|0.3823394926981217|
|Ghost|0.3846130824125717|
|Poison_Psychic|0.3880177839818869|
|Fairy_Rock|0.389230159468923|
|Flying_Poison|0.38935517887487353|
|Ice_Poison|0.40024779255694237|
|Dark_Psychic|0.40828223985556716|
|Dragon_Flying|0.4179548015970566|
|Fairy_Flying|0.4191475933257692|
|Dark_Ghost|0.42173736198634104|
|Fairy_Normal|0.42223376162366133|
|Dragon_Psychic|0.4287759355999525|
|Dark|0.42925782307267474|
|Flying_Grass|0.4307206245260697|
|Dragon_Normal|0.4313924895150847|
|Normal_Rock|0.4360477936732672|
|Fire|0.4387342459700596|
|Psychic_Rock|0.4479144596626489|
|Fairy_Poison|0.44884477482006063|
|Dragon_Grass|0.4513797902326598|
|Fairy_Grass|0.4560283921564419|
|Dragon_Rock|0.4560700887412498|
|Grass_Rock|0.45908338618160943|
|Electric|0.4594167466696051|
|Bug_Ghost|0.4642542408775675|
|Dark_Normal|0.46881293072238023|
|Bug_Steel|0.4719122955191225|
|Dragon_Poison|0.4804313801856124|
|Flying_Ghost|0.48666480904300624|
|Ghost_Ice|0.48798817798300503|
|Flying_Rock|0.49533405223299753|
|Grass_Poison|0.4975902050030027|
|Grass_Psychic|0.49800197207896824|
|Grass_Normal|0.5017136526140645|
|Electric_Rock|0.5023068984389367|
|Dragon_Fairy|0.5122143447233221|
|Fairy_Ghost|0.5123823667245763|
|Bug_Fire|0.5141204214808414|
|Ghost_Normal|0.5165947470976661|
|Bug_Dark|0.5181463923595728|
|Dark_Ice|0.518330564481073|
|Ghost_Poison|0.5185680754447808|
|Steel|0.5219634409777499|
|Electric_Ice|0.5436164562470156|
|Rock_Steel|0.5476003825971897|
|Fire_Rock|0.5540142499680889|
|Ice_Water|0.5603377589083262|
|Fighting_Normal|0.5650894176886961|
|Dark_Flying|0.5653337975064693|
|Dark_Dragon|0.5785485339764879|
|Dragon_Ghost|0.5801860014220833|
|Poison_Steel|0.5854866864489514|
|Fighting_Psychic|0.5858390048266529|
|Fighting_Poison|0.5862087202438602|
|Ghost_Rock|0.5932806562124012|
|Dark_Fairy|0.5974467540811281|
|Dark_Poison|0.5986128904150144|
|Ground|0.6054471920284821|
|Fighting_Ice|0.6072164806080254|
|Fighting_Grass|0.6110456482283684|
|Dragon_Fighting|0.6125719628083435|
|Bug_Electric|0.6189592462414732|
|Grass_Steel|0.6219942256639057|
|Fire_Poison|0.6232219783570561|
|Fire_Flying|0.6294535723891114|
|Dark_Rock|0.629486046240369|
|Ghost_Grass|0.6296185576797582|
|Electric_Poison|0.6307749915633118|
|Fairy_Fighting|0.6329248201246154|
|Fighting_Flying|0.6394608479095035|
|Fire_Grass|0.6412456888024748|
|Dark_Fighting|0.6421225077384642|
|Fire_Steel|0.6443053576126524|
|Fairy_Steel|0.645049312456264|
|Electric_Grass|0.6471672451144912|
|Water|0.64801449641585|
|Fighting_Ghost|0.6503095936913802|
|Dragon_Fire|0.6624225916208107|
|Fire_Normal|0.6649889935428004|
|Electric_Psychic|0.6665851561394737|
|Electric_Normal|0.6692017100546059|
|Bug_Ground|0.6728841891188994|
|Electric_Flying|0.6737843445022573|
|Fairy_Fire|0.6741529603604327|
|Fighting_Ground|0.6869057411070673|
|Flying_Steel|0.6921012979431777|
|Ground_Ice|0.69371914550207|
|Rock_Water|0.6942562458444963|
|Electric_Fairy|0.6974447505164465|
|Psychic_Steel|0.6981036368978272|
|Grass_Ground|0.6999160092860578|
|Electric_Ghost|0.7009066211992379|
|Normal_Steel|0.7041029964586|
|Grass_Water|0.7045876690976068|
|Ground_Rock|0.7078512690427434|
|Dragon_Steel|0.7086887597971739|
|Ground_Psychic|0.7136416276361534|
|Fire_Psychic|0.7160589876046447|
|Electric_Fire|0.7162312413813461|
|Dark_Grass|0.7185579697232553|
|Flying_Ground|0.7250227668973548|
|Fighting_Rock|0.7285737267728729|
|Fighting_Fire|0.7290426128450062|
|Dragon_Electric|0.7390538123382727|
|Ground_Normal|0.7443219085072512|
|Fire_Water|0.7452140356865243|
|Ghost_Ground|0.7456626249599303|
|Fire_Ghost|0.7501048068450045|
|Dragon_Water|0.7517177738740022|
|Dragon_Ground|0.7550191317556247|
|Dark_Electric|0.7700525530213941|
|Bug_Water|0.777238296026157|
|Dark_Fire|0.7834285608006955|
|Flying_Water|0.7867575952524771|
|Fire_Ground|0.795375377191005|
|Ground_Poison|0.8001270192686141|
|Psychic_Water|0.8025635125051263|
|Normal_Water|0.8051800664202584|
|Electric_Steel|0.8120259350548442|
|Fairy_Ground|0.8242666946579214|
|Electric_Fighting|0.8290900959207844|
|Fairy_Water|0.833423106882099|
|Ghost_Water|0.8368849775648902|
|Dark_Ground|0.8451727514740395|
|Electric_Water|0.8516343577432252|
|Fighting_Steel|0.8522017828395658|
|Ghost_Steel|0.8580630334929928|
|Dark_Steel|0.8666885410604033|
|Poison_Water|0.8913493718735745|
|Dark_Water|0.9060309093870466|
|Steel_Water|0.9291024811127849|
|Electric_Ground|0.9295254298983221|
|Ground_Water|0.9449769620370052|
|Fighting_Water|0.9526662875991465|
|Ground_Steel|1.0|




