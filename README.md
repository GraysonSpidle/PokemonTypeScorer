# PokemonTypeScorer
This project was inspired by GameFreak's Pokemon games that debuted in the 90s. If you haven't played them, I highly recommend that you do. Anyway, I grew up playing these games and still do to this day. The idea for this program spawned from a question I consistently ask myself: what is the best Pokemon type in this game? So this program is an attempt to rate all Pokemon types based on a given generation. I did this to practice my programming skills and answer a question I've asked myself for a long time.

PS: My favorite type is Normal. Snorlax and Slacking FTW!

## Installation
Just download the source code and you're good.
It does rely on the `json` and `tkinter` modules, which I believe come standard with Python. If not, they'll likely be made available with `pip install`

This was written in Python 3.6.8 and I don't intend on making it compatible with Python 2. 

## Usage
You'll find a Python script titled `main.py` that is set up to print out the ratings. You are welcome to change the weight functions in `main.py` and/or change the `rate(self, *args, **kwargs)` function which can be found in `matchupManager.py`.

## Generation VII Results
In case you don't want to download the source code to just see my results for Generation VII, here they are: 

|Type Name|Rating|
|:--------|-----:|
| Ice_Rock | 0.0 |
| Bug_Ice | 0.004473351067906404 |
| Fairy_Ice | 0.10065657671210156 |
| Ghost_Psychic | 0.1791786708592658 |
| Bug_Grass | 0.18000740179766905 |
| Flying_Ice | 0.18273717816849566 |
| Grass_Ice | 0.19684931906631192 |
| Ice_Psychic | 0.21529522305017285 |
| Ice | 0.23098559293040988 |
| Fire_Ice | 0.24723522936521286 |
| Bug_Flying | 0.24758630458034525 |
| Ice_Normal | 0.26213704635459045 |
| Fighting_Ice | 0.264027886415211 |
| Bug_Rock | 0.27374884823876455 |
| Fairy_Rock | 0.28369279921508156 |
| Ghost_Ice | 0.2888567704830329 |
| Ground_Ice | 0.289352870144492 |
| Grass_Rock | 0.2990527771101704 |
| Dark_Ice | 0.3180371038118877 |
| Bug_Fighting | 0.31846870726408844 |
| Dragon_Ice | 0.32294181187493165 |
| Dark_Psychic | 0.3405347430277601 |
| Fire_Rock | 0.3439194504406743 |
| Bug_Psychic | 0.3576826324651116 |
| Ice_Poison | 0.3582751095123287 |
| Psychic | 0.36219371591034616 |
| Fairy_Ghost | 0.3795283807502743 |
| Fairy_Psychic | 0.3801623804749744 |
| Fighting_Psychic | 0.3816891341742239 |
| Electric_Ice | 0.38485260973711927 |
| Bug | 0.3851990078593329 |
| Bug_Ghost | 0.3897090056757889 |
| Ghost | 0.39709429298106247 |
| Ice_Steel | 0.39938156395141144 |
| Ice_Water | 0.40474999733974587 |
| Flying_Grass | 0.40547945526648627 |
| Ground_Rock | 0.40896833682320555 |
| Dark_Fighting | 0.4105854233113868 |
| Poison_Rock | 0.4160587797547054 |
| Dragon_Grass | 0.41729559917681325 |
| Flying_Psychic | 0.4184980924029556 |
| Electric_Rock | 0.4200930127251923 |
| Psychic_Rock | 0.4287885263483666 |
| Normal | 0.4320588880317229 |
| Grass_Ground | 0.43252865010282887 |
| Fighting_Ghost | 0.4327461310270449 |
| Bug_Poison | 0.4366216438414724 |
| Dark_Normal | 0.43772559316332343 |
| Fighting | 0.4391596688928627 |
| Bug_Normal | 0.43937381010047266 |
| Rock | 0.4444788962286035 |
| Normal_Psychic | 0.4473137756859137 |
| Dark_Ghost | 0.44800936092193966 |
| Flying_Ghost | 0.4483211734734691 |
| Flying | 0.45047857499677496 |
| Bug_Fairy | 0.4505488863282151 |
| Fighting_Grass | 0.4507645145164993 |
| Bug_Ground | 0.4541011264930784 |
| Poison_Psychic | 0.4548334078564141 |
| Fairy | 0.45505996977344965 |
| Ghost_Rock | 0.4568606822174756 |
| Ghost_Poison | 0.45752680928544526 |
| Dragon_Rock | 0.46111026951855216 |
| Grass_Psychic | 0.4692816968082915 |
| Fairy_Fighting | 0.4695297618574883 |
| Grass | 0.46976487170574316 |
| Bug_Fire | 0.4708562546301029 |
| Normal_Rock | 0.4756303496527842 |
| Fighting_Flying | 0.47685346914181437 |
| Ghost_Grass | 0.4780146518895309 |
| Fighting_Rock | 0.47883362758153564 |
| Ghost_Ground | 0.48066300963910813 |
| Ground | 0.4829814330242594 |
| Bug_Dragon | 0.4837603961085477 |
| Dark | 0.48795894548902013 |
| Fighting_Ground | 0.49026297831892507 |
| Ground_Psychic | 0.4912518241321427 |
| Fighting_Poison | 0.4940355925971957 |
| Bug_Dark | 0.49527386755777 |
| Dark_Fairy | 0.49657156960568904 |
| Flying_Ground | 0.497878977602796 |
| Flying_Normal | 0.5046533772379148 |
| Poison | 0.505173602372502 |
| Fairy_Grass | 0.5067148143085565 |
| Fairy_Flying | 0.5091610541258953 |
| Fairy_Normal | 0.5092347720145894 |
| Dragon_Fighting | 0.5113543164546465 |
| Fighting_Normal | 0.5172952321221228 |
| Ghost_Normal | 0.5208753231187737 |
| Rock_Steel | 0.5217661047038408 |
| Grass_Poison | 0.5220530861951753 |
| Dragon_Ground | 0.5246493376916962 |
| Dragon | 0.5314284784993965 |
| Dark_Rock | 0.5315304071100815 |
| Fairy_Poison | 0.5333990007064086 |
| Dragon_Psychic | 0.5396988696072799 |
| Flying_Rock | 0.541105634771753 |
| Bug_Electric | 0.5418576342703907 |
| Rock_Water | 0.544397228073737 |
| Grass_Normal | 0.5479004349350032 |
| Fairy_Ground | 0.5536609972000324 |
| Dragon_Flying | 0.5557506215675201 |
| Dark_Flying | 0.5560893274956138 |
| Normal_Poison | 0.5593484046136417 |
| Dark_Dragon | 0.5601535930508039 |
| Ground_Normal | 0.5611169962535195 |
| Dark_Poison | 0.5683424405004681 |
| Dragon_Ghost | 0.5745994466779961 |
| Flying_Poison | 0.579377263946935 |
| Ground_Poison | 0.5807803800480954 |
| Fire_Grass | 0.5820417392728789 |
| Electric_Grass | 0.5904712153657347 |
| Dark_Grass | 0.5950469263869654 |
| Bug_Steel | 0.5951443252957928 |
| Electric_Fairy | 0.6089269865801589 |
| Dragon_Normal | 0.6095640417286567 |
| Dragon_Fire | 0.6135188312439903 |
| Electric | 0.6136128279393608 |
| Dark_Ground | 0.6170170537108167 |
| Dragon_Poison | 0.617081330867826 |
| Fire_Ground | 0.6199581713250402 |
| Electric_Psychic | 0.6218832190472442 |
| Fire_Poison | 0.623239985181981 |
| Fighting_Fire | 0.645688804616167 |
| Grass_Water | 0.6476389978526136 |
| Electric_Fighting | 0.6479675592922929 |
| Dragon_Fairy | 0.655776672989077 |
| Electric_Ghost | 0.6567837961179605 |
| Fairy_Fire | 0.661666483876351 |
| Fire_Flying | 0.6621672486837461 |
| Electric_Poison | 0.6626048029997861 |
| Electric_Fire | 0.6723989914243589 |
| Fire | 0.6730197245753147 |
| Dragon_Water | 0.6762085327399415 |
| Fire_Psychic | 0.6768260084835999 |
| Bug_Water | 0.6844499587079786 |
| Electric_Normal | 0.691748391168621 |
| Fire_Steel | 0.6995692270049381 |
| Fire_Water | 0.7007330554799108 |
| Electric_Ground | 0.703831156160116 |
| Fire_Ghost | 0.7095232934141525 |
| Electric_Flying | 0.7180906853024093 |
| Fairy_Water | 0.7235025276246553 |
| Water | 0.7281883689838572 |
| Psychic_Water | 0.7364587600917406 |
| Poison_Steel | 0.745183910752115 |
| Dark_Electric | 0.7476484486259182 |
| Dark_Fire | 0.7488854239580869 |
| Flying_Water | 0.7510834852589852 |
| Fire_Normal | 0.7511552878045747 |
| Grass_Steel | 0.7515898913043245 |
| Dragon_Electric | 0.7551656988852283 |
| Fighting_Steel | 0.7640939892121479 |
| Ghost_Water | 0.7713593371624567 |
| Ground_Water | 0.7851398959044558 |
| Electric_Water | 0.8057543571918417 |
| Normal_Water | 0.8063239322131173 |
| Fairy_Steel | 0.8087532995471727 |
| Electric_Steel | 0.8098116510697049 |
| Fighting_Water | 0.8134247130742571 |
| Psychic_Steel | 0.8388512254613573 |
| Ground_Steel | 0.8619287130973319 |
| Dark_Water | 0.8622239896704146 |
| Poison_Water | 0.8714767075714441 |
| Dragon_Steel | 0.8749518663257463 |
| Dark_Steel | 0.8856849599432772 |
| Steel | 0.8864269820211673 |
| Ghost_Steel | 0.8884879012686986 |
| Flying_Steel | 0.9017658181018702 |
| Normal_Steel | 0.9175784354453479 |
| Steel_Water | 1.0 |


