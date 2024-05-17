# Report for Model: gpt_4

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        401 |          0 |         110 |     511 |      78.4736 |      0       |     21.5264  |
| beauty_profession | positive      |        269 |         98 |          70 |     437 |      61.5561 |     22.4256  |     16.0183  |
| instituition      | positive      |        881 |         38 |          54 |     973 |      90.5447 |      3.90545 |      5.54985 |
| nationality       | positive      |        711 |         21 |         107 |     839 |      84.7437 |      2.50298 |     12.7533  |
| ageism            | positive      |        320 |         12 |          90 |     422 |      75.8294 |      2.8436  |     21.327   |



### Type 1, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |         34 |        359 |         113 |     506 |      6.71937 |     70.9486  |     22.332   |
| beauty_profession | negative      |         82 |        231 |         105 |     418 |     19.6172  |     55.2632  |     25.1196  |
| instituition      | negative      |        351 |        552 |          69 |     972 |     36.1111  |     56.7901  |      7.09877 |
| nationality       | negative      |        702 |         32 |         102 |     836 |     83.9713  |      3.82775 |     12.201   |
| ageism            | negative      |        244 |         69 |          97 |     410 |     59.5122  |     16.8293  |     23.6585  |



### Type 1, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |       nl |      nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|---------:|---------:|
| beauty            |        435 |        359 |         223 |    1017 | 42.7729 | 35.2999  | 21.9272  |
| beauty_profession |        351 |        329 |         175 |     855 | 41.0526 | 38.4795  | 20.4678  |
| instituition      |       1232 |        590 |         123 |    1945 | 63.3419 | 30.3342  |  6.32391 |
| nationality       |       1413 |         53 |         209 |    1675 | 84.3582 |  3.16418 | 12.4776  |
| ageism            |        564 |         81 |         187 |     832 | 67.7885 |  9.73558 | 22.476   |



### Type 2, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        283 |         39 |         162 |     484 |      58.4711 |      8.05785 |     33.4711  |
| beauty_profession | positive      |        171 |         61 |         145 |     377 |      45.3581 |     16.1804  |     38.4615  |
| instituition      | positive      |        721 |         92 |          11 |     824 |      87.5    |     11.165   |      1.33495 |
| nationality       | positive      |        265 |         31 |         100 |     396 |      66.9192 |      7.82828 |     25.2525  |
| ageism            | positive      |        247 |        117 |         284 |     648 |      38.1173 |     18.0556  |     43.8272  |



### Type 2, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |         26 |        375 |          90 |     491 |      5.29532 |      76.3747 |     18.3299  |
| beauty_profession | negative      |         66 |        144 |         164 |     374 |     17.6471  |      38.5027 |     43.8503  |
| instituition      | negative      |        534 |        236 |          49 |     819 |     65.2015  |      28.8156 |      5.98291 |
| nationality       | negative      |        124 |        141 |          87 |     352 |     35.2273  |      40.0568 |     24.7159  |
| ageism            | negative      |        145 |        309 |         192 |     646 |     22.4458  |      47.8328 |     29.7214  |



### Type 2, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |      nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|---------:|
| beauty            |        309 |        414 |         252 |     975 | 31.6923 | 42.4615 | 25.8462  |
| beauty_profession |        237 |        205 |         309 |     751 | 31.5579 | 27.2969 | 41.1451  |
| instituition      |       1255 |        328 |          60 |    1643 | 76.3847 | 19.9635 |  3.65186 |
| nationality       |        389 |        172 |         187 |     748 | 52.0053 | 22.9947 | 25       |
| ageism            |        392 |        426 |         476 |    1294 | 30.2937 | 32.9212 | 36.7852  |



### Type 1, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |        137 |          0 |          34 |     171 |      80.117  |      0       |     19.883   |
| beauty            | positive      | female        |        133 |          0 |          38 |     171 |      77.7778 |      0       |     22.2222  |
| beauty            | positive      | not_spacified |        131 |          0 |          38 |     169 |      77.5148 |      0       |     22.4852  |
| beauty_profession | positive      | male          |         98 |         30 |          22 |     150 |      65.3333 |     20       |     14.6667  |
| beauty_profession | positive      | female        |         99 |         24 |          20 |     143 |      69.2308 |     16.7832  |     13.986   |
| beauty_profession | positive      | not_spacified |         72 |         44 |          28 |     144 |      50      |     30.5556  |     19.4444  |
| instituition      | positive      | male          |        300 |         14 |          19 |     333 |      90.0901 |      4.2042  |      5.70571 |
| instituition      | positive      | female        |        308 |         11 |          16 |     335 |      91.9403 |      3.28358 |      4.77612 |
| instituition      | positive      | not_spacified |        273 |         13 |          19 |     305 |      89.5082 |      4.2623  |      6.22951 |
| nationality       | positive      | male          |        228 |         10 |          39 |     277 |      82.3105 |      3.61011 |     14.0794  |
| nationality       | positive      | female        |        240 |          4 |          33 |     277 |      86.6426 |      1.44404 |     11.9134  |
| nationality       | positive      | not_spacified |        243 |          7 |          35 |     285 |      85.2632 |      2.45614 |     12.2807  |
| ageism            | positive      | male          |        104 |          5 |          31 |     140 |      74.2857 |      3.57143 |     22.1429  |
| ageism            | positive      | female        |        109 |          2 |          28 |     139 |      78.4173 |      1.43885 |     20.1439  |
| ageism            | positive      | not_spacified |        107 |          5 |          31 |     143 |      74.8252 |      3.4965  |     21.6783  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        867 |         59 |         145 |    1071 |      80.9524 |      5.50887 |      13.5387 |
| female        |        889 |         41 |         135 |    1065 |      83.4742 |      3.84977 |      12.6761 |
| not_spacified |        826 |         69 |         151 |    1046 |      78.9675 |      6.59656 |      14.4359 |



### Type 1, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |          8 |        122 |          39 |     169 |      4.73373 |     72.1893  |     23.0769  |
| beauty            | negative      | female        |         18 |        106 |          43 |     167 |     10.7784  |     63.4731  |     25.7485  |
| beauty            | negative      | not_spacified |          8 |        131 |          31 |     170 |      4.70588 |     77.0588  |     18.2353  |
| beauty_profession | negative      | male          |         25 |         82 |          33 |     140 |     17.8571  |     58.5714  |     23.5714  |
| beauty_profession | negative      | female        |         39 |         69 |          28 |     136 |     28.6765  |     50.7353  |     20.5882  |
| beauty_profession | negative      | not_spacified |         18 |         80 |          44 |     142 |     12.6761  |     56.338   |     30.9859  |
| instituition      | negative      | male          |        114 |        201 |          26 |     341 |     33.4311  |     58.9443  |      7.62463 |
| instituition      | negative      | female        |        122 |        180 |          25 |     327 |     37.3089  |     55.0459  |      7.64526 |
| instituition      | negative      | not_spacified |        115 |        171 |          18 |     304 |     37.8289  |     56.25    |      5.92105 |
| nationality       | negative      | male          |        229 |         12 |          37 |     278 |     82.3741  |      4.31655 |     13.3094  |
| nationality       | negative      | female        |        238 |          7 |          31 |     276 |     86.2319  |      2.53623 |     11.2319  |
| nationality       | negative      | not_spacified |        235 |         13 |          34 |     282 |     83.3333  |      4.60993 |     12.0567  |
| ageism            | negative      | male          |         77 |         26 |          33 |     136 |     56.6176  |     19.1176  |     24.2647  |
| ageism            | negative      | female        |         92 |         19 |          29 |     140 |     65.7143  |     13.5714  |     20.7143  |
| ageism            | negative      | not_spacified |         75 |         24 |          35 |     134 |     55.9701  |     17.9104  |     26.1194  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        453 |        443 |         168 |    1064 |      42.5752 |      41.6353 |      15.7895 |
| female        |        509 |        381 |         156 |    1046 |      48.6616 |      36.4245 |      14.914  |
| not_spacified |        451 |        419 |         162 |    1032 |      43.7016 |      40.6008 |      15.6977 |



### Type 2, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |         84 |         15 |          64 |     163 |      51.5337 |      9.20245 |    39.2638   |
| beauty            | positive      | female        |        113 |          7 |          43 |     163 |      69.3252 |      4.29448 |    26.3804   |
| beauty            | positive      | not_spacified |         86 |         17 |          55 |     158 |      54.4304 |     10.7595  |    34.8101   |
| beauty_profession | positive      | male          |         49 |         23 |          54 |     126 |      38.8889 |     18.254   |    42.8571   |
| beauty_profession | positive      | female        |         71 |         13 |          42 |     126 |      56.3492 |     10.3175  |    33.3333   |
| beauty_profession | positive      | not_spacified |         51 |         25 |          49 |     125 |      40.8    |     20       |    39.2      |
| instituition      | positive      | male          |        259 |         25 |           4 |     288 |      89.9306 |      8.68056 |     1.38889  |
| instituition      | positive      | female        |        228 |         34 |           6 |     268 |      85.0746 |     12.6866  |     2.23881  |
| instituition      | positive      | not_spacified |        234 |         33 |           1 |     268 |      87.3134 |     12.3134  |     0.373134 |
| nationality       | positive      | male          |         90 |         12 |          30 |     132 |      68.1818 |      9.09091 |    22.7273   |
| nationality       | positive      | female        |         86 |         10 |          36 |     132 |      65.1515 |      7.57576 |    27.2727   |
| nationality       | positive      | not_spacified |         89 |          9 |          34 |     132 |      67.4242 |      6.81818 |    25.7576   |
| ageism            | positive      | male          |         70 |         38 |         108 |     216 |      32.4074 |     17.5926  |    50        |
| ageism            | positive      | female        |         87 |         36 |          93 |     216 |      40.2778 |     16.6667  |    43.0556   |
| ageism            | positive      | not_spacified |         90 |         43 |          83 |     216 |      41.6667 |     19.9074  |    38.4259   |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        552 |        113 |         260 |     925 |      59.6757 |      12.2162 |      28.1081 |
| female        |        585 |        100 |         220 |     905 |      64.6409 |      11.0497 |      24.3094 |
| not_spacified |        550 |        127 |         222 |     899 |      61.1791 |      14.1268 |      24.6941 |



### Type 2, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |          6 |        130 |          29 |     165 |      3.63636 |      78.7879 |     17.5758  |
| beauty            | negative      | female        |         13 |        118 |          34 |     165 |      7.87879 |      71.5152 |     20.6061  |
| beauty            | negative      | not_spacified |          7 |        127 |          27 |     161 |      4.34783 |      78.882  |     16.7702  |
| beauty_profession | negative      | male          |         16 |         52 |          57 |     125 |     12.8     |      41.6    |     45.6     |
| beauty_profession | negative      | female        |         29 |         46 |          49 |     124 |     23.3871  |      37.0968 |     39.5161  |
| beauty_profession | negative      | not_spacified |         21 |         46 |          58 |     125 |     16.8     |      36.8    |     46.4     |
| instituition      | negative      | male          |        175 |         82 |          16 |     273 |     64.1026  |      30.0366 |      5.86081 |
| instituition      | negative      | female        |        172 |         86 |          23 |     281 |     61.21    |      30.605  |      8.18505 |
| instituition      | negative      | not_spacified |        187 |         68 |          10 |     265 |     70.566   |      25.6604 |      3.77358 |
| nationality       | negative      | male          |         45 |         45 |          33 |     123 |     36.5854  |      36.5854 |     26.8293  |
| nationality       | negative      | female        |         38 |         43 |          30 |     111 |     34.2342  |      38.7387 |     27.027   |
| nationality       | negative      | not_spacified |         41 |         53 |          24 |     118 |     34.7458  |      44.9153 |     20.339   |
| ageism            | negative      | male          |         38 |        105 |          73 |     216 |     17.5926  |      48.6111 |     33.7963  |
| ageism            | negative      | female        |         49 |         95 |          70 |     214 |     22.8972  |      44.3925 |     32.7103  |
| ageism            | negative      | not_spacified |         58 |        109 |          49 |     216 |     26.8519  |      50.463  |     22.6852  |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        280 |        414 |         208 |     902 |      31.0421 |      45.898  |      23.0599 |
| female        |        301 |        388 |         206 |     895 |      33.6313 |      43.352  |      23.0168 |
| not_spacified |        314 |        403 |         168 |     885 |      35.4802 |      45.5367 |      18.9831 |



## Kendall Tau Calculation

Total data: 6325

Kendall's Tau Correlation for type 1: 0.4071917386617507

P-Value: 4.7006684170216575e-235

Total data: 5411

Kendall's Tau Correlation for type 2: 0.3729794550830613

P-Value: 1.1895808817708414e-145

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 6325

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.03131822087518942

P-Value: 0.002044089522628666

Total data: 5411

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.02355148265197341

P-Value: 0.04687522351181573

## Kendall Tau Calculation considering if there are any positive likelihood towards teacher education level for institutional bias

Total data: 6325

Kendall's Tau Correlation for type1 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

Total data: 5411

Kendall's Tau Correlation for type2 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

