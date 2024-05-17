# Report for Model: llama2-13B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        303 |         79 |         119 |     501 |      60.479  |      15.7685 |      23.7525 |
| beauty_profession | positive      |        197 |        109 |         128 |     434 |      45.3917 |      25.1152 |      29.4931 |
| instituition      | positive      |        596 |        148 |         193 |     937 |      63.6073 |      15.7951 |      20.5977 |
| nationality       | positive      |        461 |        169 |         194 |     824 |      55.9466 |      20.5097 |      23.5437 |
| ageism            | positive      |        255 |         60 |          96 |     411 |      62.0438 |      14.5985 |      23.3577 |



### Type 1, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |        197 |        163 |         135 |     495 |      39.798  |      32.9293 |      27.2727 |
| beauty_profession | negative      |        158 |        139 |         152 |     449 |      35.1893 |      30.9577 |      33.853  |
| instituition      | negative      |        479 |        334 |         132 |     945 |      50.6878 |      35.3439 |      13.9683 |
| nationality       | negative      |        460 |        205 |         173 |     838 |      54.8926 |      24.463  |      20.6444 |
| ageism            | negative      |        220 |         86 |         103 |     409 |      53.7897 |      21.0269 |      25.1834 |



### Type 1, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| beauty            |        500 |        242 |         254 |     996 | 50.2008 | 24.2972 | 25.502  |
| beauty_profession |        355 |        248 |         280 |     883 | 40.2039 | 28.0861 | 31.7101 |
| instituition      |       1075 |        482 |         325 |    1882 | 57.1201 | 25.6111 | 17.2689 |
| nationality       |        921 |        374 |         367 |    1662 | 55.4152 | 22.503  | 22.0818 |
| ageism            |        475 |        146 |         199 |     820 | 57.9268 | 17.8049 | 24.2683 |



### Type 2, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        279 |         93 |         114 |     486 |      57.4074 |     19.1358  |      23.4568 |
| beauty_profession | positive      |        218 |         82 |          71 |     371 |      58.7601 |     22.1024  |      19.1375 |
| instituition      | positive      |        611 |         79 |         102 |     792 |      77.1465 |      9.97475 |      12.8788 |
| nationality       | positive      |        180 |         85 |          98 |     363 |      49.5868 |     23.416   |      26.9972 |
| ageism            | positive      |        202 |        221 |         220 |     643 |      31.4152 |     34.3701  |      34.2146 |



### Type 2, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |        162 |        234 |          92 |     488 |     33.1967  |      47.9508 |      18.8525 |
| beauty_profession | negative      |        154 |        140 |          79 |     373 |     41.2869  |      37.5335 |      21.1796 |
| instituition      | negative      |         57 |        611 |         100 |     768 |      7.42188 |      79.5573 |      13.0208 |
| nationality       | negative      |        110 |        155 |          96 |     361 |     30.4709  |      42.9363 |      26.5928 |
| ageism            | negative      |        133 |        278 |         234 |     645 |     20.6202  |      43.1008 |      36.2791 |



### Type 2, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| beauty            |        441 |        327 |         206 |     974 | 45.2772 | 33.5729 | 21.1499 |
| beauty_profession |        372 |        222 |         150 |     744 | 50      | 29.8387 | 20.1613 |
| instituition      |        668 |        690 |         202 |    1560 | 42.8205 | 44.2308 | 12.9487 |
| nationality       |        290 |        240 |         194 |     724 | 40.0552 | 33.1492 | 26.7956 |
| ageism            |        335 |        499 |         454 |    1288 | 26.0093 | 38.7422 | 35.2484 |



### Type 1, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |        101 |         28 |          38 |     167 |      60.479  |      16.7665 |      22.7545 |
| beauty            | positive      | female        |        107 |         22 |          40 |     169 |      63.3136 |      13.0178 |      23.6686 |
| beauty            | positive      | not_spacified |         95 |         29 |          41 |     165 |      57.5758 |      17.5758 |      24.8485 |
| beauty_profession | positive      | male          |         80 |         24 |          42 |     146 |      54.7945 |      16.4384 |      28.7671 |
| beauty_profession | positive      | female        |         53 |         45 |          46 |     144 |      36.8056 |      31.25   |      31.9444 |
| beauty_profession | positive      | not_spacified |         64 |         40 |          40 |     144 |      44.4444 |      27.7778 |      27.7778 |
| instituition      | positive      | male          |        195 |         51 |          72 |     318 |      61.3208 |      16.0377 |      22.6415 |
| instituition      | positive      | female        |        206 |         47 |          71 |     324 |      63.5802 |      14.5062 |      21.9136 |
| instituition      | positive      | not_spacified |        195 |         50 |          50 |     295 |      66.1017 |      16.9492 |      16.9492 |
| nationality       | positive      | male          |        147 |         63 |          65 |     275 |      53.4545 |      22.9091 |      23.6364 |
| nationality       | positive      | female        |        171 |         46 |          60 |     277 |      61.7329 |      16.6065 |      21.6606 |
| nationality       | positive      | not_spacified |        143 |         60 |          69 |     272 |      52.5735 |      22.0588 |      25.3676 |
| ageism            | positive      | male          |         85 |         15 |          36 |     136 |      62.5    |      11.0294 |      26.4706 |
| ageism            | positive      | female        |         93 |         16 |          29 |     138 |      67.3913 |      11.5942 |      21.0145 |
| ageism            | positive      | not_spacified |         77 |         29 |          31 |     137 |      56.2044 |      21.1679 |      22.6277 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        608 |        181 |         253 |    1042 |      58.3493 |      17.3704 |      24.2802 |
| female        |        630 |        176 |         246 |    1052 |      59.8859 |      16.73   |      23.384  |
| not_spacified |        574 |        208 |         231 |    1013 |      56.6634 |      20.5331 |      22.8036 |



### Type 1, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |         60 |         59 |          44 |     163 |      36.8098 |      36.1963 |      26.9939 |
| beauty            | negative      | female        |         68 |         53 |          42 |     163 |      41.7178 |      32.5153 |      25.7669 |
| beauty            | negative      | not_spacified |         69 |         51 |          49 |     169 |      40.8284 |      30.1775 |      28.9941 |
| beauty_profession | negative      | male          |         55 |         47 |          47 |     149 |      36.9128 |      31.5436 |      31.5436 |
| beauty_profession | negative      | female        |         60 |         43 |          46 |     149 |      40.2685 |      28.8591 |      30.8725 |
| beauty_profession | negative      | not_spacified |         43 |         49 |          59 |     151 |      28.4768 |      32.4503 |      39.0728 |
| instituition      | negative      | male          |        159 |        125 |          46 |     330 |      48.1818 |      37.8788 |      13.9394 |
| instituition      | negative      | female        |        171 |        106 |          38 |     315 |      54.2857 |      33.6508 |      12.0635 |
| instituition      | negative      | not_spacified |        149 |        103 |          48 |     300 |      49.6667 |      34.3333 |      16      |
| nationality       | negative      | male          |        144 |         77 |          60 |     281 |      51.2456 |      27.4021 |      21.3523 |
| nationality       | negative      | female        |        164 |         61 |          52 |     277 |      59.2058 |      22.0217 |      18.7726 |
| nationality       | negative      | not_spacified |        152 |         67 |          61 |     280 |      54.2857 |      23.9286 |      21.7857 |
| ageism            | negative      | male          |         69 |         27 |          44 |     140 |      49.2857 |      19.2857 |      31.4286 |
| ageism            | negative      | female        |         73 |         29 |          29 |     131 |      55.7252 |      22.1374 |      22.1374 |
| ageism            | negative      | not_spacified |         78 |         30 |          30 |     138 |      56.5217 |      21.7391 |      21.7391 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        487 |        335 |         241 |    1063 |      45.8137 |      31.5146 |      22.6717 |
| female        |        536 |        292 |         207 |    1035 |      51.7874 |      28.2126 |      20      |
| not_spacified |        491 |        300 |         247 |    1038 |      47.3025 |      28.9017 |      23.7958 |



### Type 2, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |         89 |         35 |          37 |     161 |      55.2795 |     21.7391  |      22.9814 |
| beauty            | positive      | female        |         95 |         29 |          38 |     162 |      58.642  |     17.9012  |      23.4568 |
| beauty            | positive      | not_spacified |         95 |         29 |          39 |     163 |      58.2822 |     17.7914  |      23.9264 |
| beauty_profession | positive      | male          |         69 |         31 |          26 |     126 |      54.7619 |     24.6032  |      20.6349 |
| beauty_profession | positive      | female        |         75 |         25 |          24 |     124 |      60.4839 |     20.1613  |      19.3548 |
| beauty_profession | positive      | not_spacified |         74 |         26 |          21 |     121 |      61.157  |     21.4876  |      17.3554 |
| instituition      | positive      | male          |        213 |         28 |          32 |     273 |      78.022  |     10.2564  |      11.7216 |
| instituition      | positive      | female        |        206 |         22 |          31 |     259 |      79.5367 |      8.49421 |      11.9691 |
| instituition      | positive      | not_spacified |        192 |         29 |          39 |     260 |      73.8462 |     11.1538  |      15      |
| nationality       | positive      | male          |         61 |         24 |          33 |     118 |      51.6949 |     20.339   |      27.9661 |
| nationality       | positive      | female        |         63 |         32 |          25 |     120 |      52.5    |     26.6667  |      20.8333 |
| nationality       | positive      | not_spacified |         56 |         29 |          40 |     125 |      44.8    |     23.2     |      32      |
| ageism            | positive      | male          |         60 |         68 |          87 |     215 |      27.907  |     31.6279  |      40.4651 |
| ageism            | positive      | female        |         68 |         75 |          69 |     212 |      32.0755 |     35.3774  |      32.5472 |
| ageism            | positive      | not_spacified |         74 |         78 |          64 |     216 |      34.2593 |     36.1111  |      29.6296 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        492 |        186 |         215 |     893 |      55.0952 |      20.8287 |      24.0761 |
| female        |        507 |        183 |         187 |     877 |      57.8107 |      20.8666 |      21.3227 |
| not_spacified |        491 |        191 |         203 |     885 |      55.4802 |      21.5819 |      22.9379 |



### Type 2, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |         45 |         89 |          30 |     164 |     27.439   |      54.2683 |      18.2927 |
| beauty            | negative      | female        |         59 |         77 |          27 |     163 |     36.1963  |      47.2393 |      16.5644 |
| beauty            | negative      | not_spacified |         58 |         68 |          35 |     161 |     36.0248  |      42.236  |      21.7391 |
| beauty_profession | negative      | male          |         51 |         45 |          30 |     126 |     40.4762  |      35.7143 |      23.8095 |
| beauty_profession | negative      | female        |         51 |         45 |          26 |     122 |     41.8033  |      36.8852 |      21.3115 |
| beauty_profession | negative      | not_spacified |         52 |         50 |          23 |     125 |     41.6     |      40      |      18.4    |
| instituition      | negative      | male          |         22 |        191 |          39 |     252 |      8.73016 |      75.7937 |      15.4762 |
| instituition      | negative      | female        |         16 |        217 |          31 |     264 |      6.06061 |      82.197  |      11.7424 |
| instituition      | negative      | not_spacified |         19 |        203 |          30 |     252 |      7.53968 |      80.5556 |      11.9048 |
| nationality       | negative      | male          |         42 |         48 |          28 |     118 |     35.5932  |      40.678  |      23.7288 |
| nationality       | negative      | female        |         38 |         52 |          31 |     121 |     31.405   |      42.9752 |      25.6198 |
| nationality       | negative      | not_spacified |         30 |         55 |          37 |     122 |     24.5902  |      45.082  |      30.3279 |
| ageism            | negative      | male          |         35 |        100 |          80 |     215 |     16.2791  |      46.5116 |      37.2093 |
| ageism            | negative      | female        |         53 |         91 |          71 |     215 |     24.6512  |      42.3256 |      33.0233 |
| ageism            | negative      | not_spacified |         45 |         87 |          83 |     215 |     20.9302  |      40.4651 |      38.6047 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        195 |        473 |         207 |     875 |      22.2857 |      54.0571 |      23.6571 |
| female        |        217 |        482 |         186 |     885 |      24.5198 |      54.4633 |      21.0169 |
| not_spacified |        204 |        463 |         208 |     875 |      23.3143 |      52.9143 |      23.7714 |



## Kendall Tau Calculation

Total data: 6246

Kendall's Tau Correlation for type 1: 0.12963798592226147

P-Value: 1.4082164789028954e-22

Total data: 5294

Kendall's Tau Correlation for type 2: 0.40182975816118754

P-Value: 1.047449638253271e-161

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 6246

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.026058252689982877

P-Value: 0.016082181127597246

Total data: 5294

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.00745599618874123

P-Value: 0.5380280371391549

## Kendall Tau Calculation considering if there are any positive likelihood towards teacher education level for institutional bias

Total data: 6246

Kendall's Tau Correlation for type1 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

Total data: 5294

Kendall's Tau Correlation for type2 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

