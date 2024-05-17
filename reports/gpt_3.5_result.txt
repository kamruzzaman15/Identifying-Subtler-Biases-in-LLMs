# Report for Model: gpt_3.5

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        390 |         25 |          79 |     494 |      78.9474 |      5.06073 |     15.9919  |
| beauty_profession | positive      |        225 |        115 |         101 |     441 |      51.0204 |     26.0771  |     22.9025  |
| instituition      | positive      |        731 |        132 |          84 |     947 |      77.1911 |     13.9388  |      8.87012 |
| nationality       | positive      |        687 |         94 |          66 |     847 |      81.1098 |     11.098   |      7.79221 |
| ageism            | positive      |        267 |        108 |          52 |     427 |      62.5293 |     25.2927  |     12.178   |



### Type 1, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |         48 |        370 |          49 |     467 |      10.2784 |      79.2291 |     10.4925  |
| beauty_profession | negative      |         69 |        249 |         123 |     441 |      15.6463 |      56.4626 |     27.8912  |
| instituition      | negative      |        561 |        318 |          76 |     955 |      58.7435 |      33.2984 |      7.95812 |
| nationality       | negative      |        598 |        196 |          48 |     842 |      71.0214 |      23.2779 |      5.70071 |
| ageism            | negative      |        178 |        201 |          47 |     426 |      41.784  |      47.1831 |     11.0329  |



### Type 1, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |      nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|---------:|
| beauty            |        438 |        395 |         128 |     961 | 45.5775 | 41.103  | 13.3195  |
| beauty_profession |        294 |        364 |         224 |     882 | 33.3333 | 41.2698 | 25.3968  |
| instituition      |       1292 |        450 |         160 |    1902 | 67.9285 | 23.6593 |  8.4122  |
| nationality       |       1285 |        290 |         114 |    1689 | 76.0805 | 17.1699 |  6.74956 |
| ageism            |        445 |        309 |          99 |     853 | 52.1688 | 36.2251 | 11.6061  |



### Type 2, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        256 |         34 |          56 |     346 |      73.9884 |      9.82659 |      16.185  |
| beauty_profession | positive      |        189 |        125 |          58 |     372 |      50.8065 |     33.6022  |      15.5914 |
| instituition      | positive      |        515 |        204 |          90 |     809 |      63.6588 |     25.2163  |      11.1248 |
| nationality       | positive      |        268 |         44 |          82 |     394 |      68.0203 |     11.1675  |      20.8122 |
| ageism            | positive      |        253 |        164 |         230 |     647 |      39.1036 |     25.3478  |      35.5487 |



### Type 2, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |         34 |        348 |          20 |     402 |      8.45771 |      86.5672 |      4.97512 |
| beauty_profession | negative      |        102 |        211 |          57 |     370 |     27.5676  |      57.027  |     15.4054  |
| instituition      | negative      |        307 |        365 |         131 |     803 |     38.2316  |      45.4545 |     16.3138  |
| nationality       | negative      |        134 |        140 |         113 |     387 |     34.6253  |      36.1757 |     29.199   |
| ageism            | negative      |        178 |        267 |         199 |     644 |     27.6398  |      41.4596 |     30.9006  |



### Type 2, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| beauty            |        290 |        382 |          76 |     748 | 38.7701 | 51.0695 | 10.1604 |
| beauty_profession |        291 |        336 |         115 |     742 | 39.2183 | 45.283  | 15.4987 |
| instituition      |        822 |        569 |         221 |    1612 | 50.9926 | 35.2978 | 13.7097 |
| nationality       |        402 |        184 |         195 |     781 | 51.4725 | 23.5595 | 24.968  |
| ageism            |        431 |        431 |         429 |    1291 | 33.385  | 33.385  | 33.2301 |



### Type 1, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |        134 |          8 |          23 |     165 |      81.2121 |      4.84848 |     13.9394  |
| beauty            | positive      | female        |        125 |          8 |          30 |     163 |      76.6871 |      4.90798 |     18.4049  |
| beauty            | positive      | not_spacified |        131 |          9 |          26 |     166 |      78.9157 |      5.42169 |     15.6627  |
| beauty_profession | positive      | male          |         81 |         34 |          34 |     149 |      54.3624 |     22.8188  |     22.8188  |
| beauty_profession | positive      | female        |         80 |         35 |          32 |     147 |      54.4218 |     23.8095  |     21.7687  |
| beauty_profession | positive      | not_spacified |         64 |         46 |          35 |     145 |      44.1379 |     31.7241  |     24.1379  |
| instituition      | positive      | male          |        242 |         51 |          30 |     323 |      74.9226 |     15.7895  |      9.28793 |
| instituition      | positive      | female        |        255 |         45 |          24 |     324 |      78.7037 |     13.8889  |      7.40741 |
| instituition      | positive      | not_spacified |        234 |         36 |          30 |     300 |      78      |     12       |     10       |
| nationality       | positive      | male          |        211 |         40 |          29 |     280 |      75.3571 |     14.2857  |     10.3571  |
| nationality       | positive      | female        |        242 |         25 |          15 |     282 |      85.8156 |      8.86525 |      5.31915 |
| nationality       | positive      | not_spacified |        234 |         29 |          22 |     285 |      82.1053 |     10.1754  |      7.7193  |
| ageism            | positive      | male          |         95 |         30 |          17 |     142 |      66.9014 |     21.1268  |     11.9718  |
| ageism            | positive      | female        |         94 |         33 |          15 |     142 |      66.1972 |     23.2394  |     10.5634  |
| ageism            | positive      | not_spacified |         78 |         45 |          20 |     143 |      54.5455 |     31.4685  |     13.986   |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        763 |        163 |         133 |    1059 |      72.0491 |      15.3919 |      12.559  |
| female        |        796 |        146 |         116 |    1058 |      75.2363 |      13.7996 |      10.9641 |
| not_spacified |        741 |        165 |         133 |    1039 |      71.3186 |      15.8807 |      12.8008 |



### Type 1, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |         12 |        127 |          15 |     154 |      7.79221 |      82.4675 |      9.74026 |
| beauty            | negative      | female        |         22 |        110 |          22 |     154 |     14.2857  |      71.4286 |     14.2857  |
| beauty            | negative      | not_spacified |         14 |        133 |          12 |     159 |      8.80503 |      83.6478 |      7.54717 |
| beauty_profession | negative      | male          |         23 |         81 |          41 |     145 |     15.8621  |      55.8621 |     28.2759  |
| beauty_profession | negative      | female        |         24 |         85 |          40 |     149 |     16.1074  |      57.047  |     26.8456  |
| beauty_profession | negative      | not_spacified |         22 |         83 |          42 |     147 |     14.966   |      56.4626 |     28.5714  |
| instituition      | negative      | male          |        176 |        129 |          29 |     334 |     52.6946  |      38.6228 |      8.68263 |
| instituition      | negative      | female        |        198 |         99 |          24 |     321 |     61.6822  |      30.8411 |      7.47664 |
| instituition      | negative      | not_spacified |        187 |         90 |          23 |     300 |     62.3333  |      30      |      7.66667 |
| nationality       | negative      | male          |        190 |         70 |          21 |     281 |     67.6157  |      24.911  |      7.47331 |
| nationality       | negative      | female        |        208 |         55 |          17 |     280 |     74.2857  |      19.6429 |      6.07143 |
| nationality       | negative      | not_spacified |        200 |         71 |          10 |     281 |     71.1744  |      25.2669 |      3.55872 |
| ageism            | negative      | male          |         59 |         70 |          13 |     142 |     41.5493  |      49.2958 |      9.15493 |
| ageism            | negative      | female        |         66 |         61 |          15 |     142 |     46.4789  |      42.9577 |     10.5634  |
| ageism            | negative      | not_spacified |         53 |         70 |          19 |     142 |     37.3239  |      49.2958 |     13.3803  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        460 |        477 |         119 |    1056 |      43.5606 |      45.1705 |      11.2689 |
| female        |        518 |        410 |         118 |    1046 |      49.522  |      39.1969 |      11.2811 |
| not_spacified |        476 |        447 |         106 |    1029 |      46.2585 |      43.4402 |      10.3013 |



### Type 2, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |         73 |         13 |          20 |     106 |      68.8679 |     12.2642  |     18.8679  |
| beauty            | positive      | female        |         96 |          7 |          20 |     123 |      78.0488 |      5.69106 |     16.2602  |
| beauty            | positive      | not_spacified |         87 |         14 |          16 |     117 |      74.359  |     11.9658  |     13.6752  |
| beauty_profession | positive      | male          |         57 |         44 |          24 |     125 |      45.6    |     35.2     |     19.2     |
| beauty_profession | positive      | female        |         78 |         29 |          16 |     123 |      63.4146 |     23.5772  |     13.0081  |
| beauty_profession | positive      | not_spacified |         54 |         52 |          18 |     124 |      43.5484 |     41.9355  |     14.5161  |
| instituition      | positive      | male          |        186 |         62 |          35 |     283 |      65.7244 |     21.9081  |     12.3675  |
| instituition      | positive      | female        |        149 |         76 |          36 |     261 |      57.0881 |     29.1188  |     13.7931  |
| instituition      | positive      | not_spacified |        180 |         66 |          19 |     265 |      67.9245 |     24.9057  |      7.16981 |
| nationality       | positive      | male          |         88 |         18 |          26 |     132 |      66.6667 |     13.6364  |     19.697   |
| nationality       | positive      | female        |         87 |         13 |          31 |     131 |      66.4122 |      9.92366 |     23.6641  |
| nationality       | positive      | not_spacified |         93 |         13 |          25 |     131 |      70.9924 |      9.92366 |     19.084   |
| ageism            | positive      | male          |         62 |         65 |          89 |     216 |      28.7037 |     30.0926  |     41.2037  |
| ageism            | positive      | female        |         89 |         43 |          84 |     216 |      41.2037 |     19.9074  |     38.8889  |
| ageism            | positive      | not_spacified |        102 |         56 |          57 |     215 |      47.4419 |     26.0465  |     26.5116  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        466 |        202 |         194 |     862 |      54.0603 |      23.4339 |      22.5058 |
| female        |        499 |        168 |         187 |     854 |      58.4309 |      19.6721 |      21.897  |
| not_spacified |        516 |        201 |         135 |     852 |      60.5634 |      23.5915 |      15.8451 |



### Type 2, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |          8 |        118 |           6 |     132 |      6.06061 |      89.3939 |      4.54545 |
| beauty            | negative      | female        |         21 |        112 |           8 |     141 |     14.8936  |      79.4326 |      5.67376 |
| beauty            | negative      | not_spacified |          5 |        118 |           6 |     129 |      3.87597 |      91.4729 |      4.65116 |
| beauty_profession | negative      | male          |         19 |         79 |          25 |     123 |     15.4472  |      64.2276 |     20.3252  |
| beauty_profession | negative      | female        |         48 |         58 |          18 |     124 |     38.7097  |      46.7742 |     14.5161  |
| beauty_profession | negative      | not_spacified |         35 |         74 |          14 |     123 |     28.4553  |      60.1626 |     11.3821  |
| instituition      | negative      | male          |         93 |        124 |          48 |     265 |     35.0943  |      46.7925 |     18.1132  |
| instituition      | negative      | female        |         97 |        137 |          44 |     278 |     34.8921  |      49.2806 |     15.8273  |
| instituition      | negative      | not_spacified |        117 |        104 |          39 |     260 |     45       |      40      |     15       |
| nationality       | negative      | male          |         42 |         45 |          42 |     129 |     32.5581  |      34.8837 |     32.5581  |
| nationality       | negative      | female        |         46 |         43 |          42 |     131 |     35.1145  |      32.8244 |     32.0611  |
| nationality       | negative      | not_spacified |         46 |         52 |          29 |     127 |     36.2205  |      40.9449 |     22.8346  |
| ageism            | negative      | male          |         44 |        101 |          70 |     215 |     20.4651  |      46.9767 |     32.5581  |
| ageism            | negative      | female        |         77 |         82 |          57 |     216 |     35.6481  |      37.963  |     26.3889  |
| ageism            | negative      | not_spacified |         57 |         84 |          72 |     213 |     26.7606  |      39.4366 |     33.8028  |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        206 |        467 |         191 |     864 |      23.8426 |      54.0509 |      22.1065 |
| female        |        289 |        432 |         169 |     890 |      32.4719 |      48.5393 |      18.9888 |
| not_spacified |        260 |        432 |         160 |     852 |      30.5164 |      50.7042 |      18.7793 |



## Kendall Tau Calculation

Total data: 6287

Kendall's Tau Correlation for type 1: 0.29949444635301564

P-Value: 9.717674947421988e-123

Total data: 5174

Kendall's Tau Correlation for type 2: 0.34523693367972746

P-Value: 9.651643898311717e-119

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 6287

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.032348101592635535

P-Value: 0.0018286543172797334

Total data: 5174

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.04269414331028937

P-Value: 0.00044993405172989004

## Kendall Tau Calculation considering if there are any positive likelihood towards teacher education level for institutional bias

Total data: 6287

Kendall's Tau Correlation for type1 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

Total data: 5174

Kendall's Tau Correlation for type2 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

