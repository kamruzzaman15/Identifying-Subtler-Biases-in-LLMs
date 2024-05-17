# Report for Model: mistral-7B

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        307 |         76 |         128 |     511 |      60.0783 |      14.8728 |      25.0489 |
| beauty_profession | positive      |        217 |        102 |         135 |     454 |      47.7974 |      22.467  |      29.7357 |
| instituition      | positive      |        625 |        166 |         183 |     974 |      64.1684 |      17.0431 |      18.7885 |
| nationality       | positive      |        390 |        302 |         162 |     854 |      45.6674 |      35.363  |      18.9696 |
| ageism            | positive      |        178 |        161 |          87 |     426 |      41.784  |      37.7934 |      20.4225 |



### Type 1, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |        114 |        270 |         127 |     511 |      22.3092 |      52.8376 |      24.8532 |
| beauty_profession | negative      |        153 |        147 |         152 |     452 |      33.8496 |      32.5221 |      33.6283 |
| instituition      | negative      |        596 |        223 |         154 |     973 |      61.2539 |      22.9188 |      15.8273 |
| nationality       | negative      |        324 |        375 |         155 |     854 |      37.9391 |      43.911  |      18.1499 |
| ageism            | negative      |        162 |        163 |         104 |     429 |      37.7622 |      37.9953 |      24.2424 |



### Type 1, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| beauty            |        421 |        346 |         255 |    1022 | 41.1937 | 33.8552 | 24.9511 |
| beauty_profession |        370 |        249 |         287 |     906 | 40.8389 | 27.4834 | 31.6777 |
| instituition      |       1221 |        389 |         337 |    1947 | 62.7119 | 19.9795 | 17.3087 |
| nationality       |        714 |        677 |         317 |    1708 | 41.8033 | 39.637  | 18.5597 |
| ageism            |        340 |        324 |         191 |     855 | 39.7661 | 37.8947 | 22.3392 |



### Type 2, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        270 |         93 |         128 |     491 |      54.9898 |      18.9409 |      26.0692 |
| beauty_profession | positive      |        164 |        105 |         106 |     375 |      43.7333 |      28      |      28.2667 |
| instituition      | positive      |        329 |        202 |         260 |     791 |      41.5929 |      25.5373 |      32.8698 |
| nationality       | positive      |        220 |         87 |          89 |     396 |      55.5556 |      21.9697 |      22.4747 |
| ageism            | positive      |        159 |        233 |         256 |     648 |      24.537  |      35.9568 |      39.5062 |



### Type 2, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |         92 |        293 |         107 |     492 |      18.6992 |      59.5528 |      21.748  |
| beauty_profession | negative      |        125 |        139 |         111 |     375 |      33.3333 |      37.0667 |      29.6    |
| instituition      | negative      |        234 |        276 |         297 |     807 |      28.9963 |      34.2007 |      36.803  |
| nationality       | negative      |        133 |        141 |         122 |     396 |      33.5859 |      35.6061 |      30.8081 |
| ageism            | negative      |        160 |        185 |         303 |     648 |      24.6914 |      28.5494 |      46.7593 |



### Type 2, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| beauty            |        362 |        386 |         235 |     983 | 36.826  | 39.2675 | 23.9064 |
| beauty_profession |        289 |        244 |         217 |     750 | 38.5333 | 32.5333 | 28.9333 |
| instituition      |        563 |        478 |         557 |    1598 | 35.2315 | 29.9124 | 34.8561 |
| nationality       |        353 |        228 |         211 |     792 | 44.5707 | 28.7879 | 26.6414 |
| ageism            |        319 |        418 |         559 |    1296 | 24.6142 | 32.2531 | 43.1327 |



### Type 1, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |        111 |         20 |          39 |     170 |      65.2941 |      11.7647 |      22.9412 |
| beauty            | positive      | female        |         98 |         29 |          44 |     171 |      57.3099 |      16.9591 |      25.731  |
| beauty            | positive      | not_spacified |         98 |         27 |          45 |     170 |      57.6471 |      15.8824 |      26.4706 |
| beauty_profession | positive      | male          |         73 |         33 |          46 |     152 |      48.0263 |      21.7105 |      30.2632 |
| beauty_profession | positive      | female        |         66 |         35 |          51 |     152 |      43.4211 |      23.0263 |      33.5526 |
| beauty_profession | positive      | not_spacified |         78 |         34 |          38 |     150 |      52      |      22.6667 |      25.3333 |
| instituition      | positive      | male          |        196 |         72 |          65 |     333 |      58.8589 |      21.6216 |      19.5195 |
| instituition      | positive      | female        |        225 |         52 |          58 |     335 |      67.1642 |      15.5224 |      17.3134 |
| instituition      | positive      | not_spacified |        204 |         42 |          60 |     306 |      66.6667 |      13.7255 |      19.6078 |
| nationality       | positive      | male          |        121 |        112 |          52 |     285 |      42.4561 |      39.2982 |      18.2456 |
| nationality       | positive      | female        |        139 |         93 |          53 |     285 |      48.7719 |      32.6316 |      18.5965 |
| nationality       | positive      | not_spacified |        130 |         97 |          57 |     284 |      45.7746 |      34.1549 |      20.0704 |
| ageism            | positive      | male          |         64 |         50 |          28 |     142 |      45.0704 |      35.2113 |      19.7183 |
| ageism            | positive      | female        |         64 |         53 |          25 |     142 |      45.0704 |      37.3239 |      17.6056 |
| ageism            | positive      | not_spacified |         50 |         58 |          34 |     142 |      35.2113 |      40.8451 |      23.9437 |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        565 |        287 |         230 |    1082 |      52.2181 |      26.525  |      21.2569 |
| female        |        592 |        262 |         231 |    1085 |      54.5622 |      24.1475 |      21.2903 |
| not_spacified |        560 |        258 |         234 |    1052 |      53.2319 |      24.5247 |      22.2433 |



### Type 1, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |         47 |         87 |          37 |     171 |      27.4854 |      50.8772 |      21.6374 |
| beauty            | negative      | female        |         34 |         97 |          40 |     171 |      19.883  |      56.7251 |      23.3918 |
| beauty            | negative      | not_spacified |         33 |         86 |          50 |     169 |      19.5266 |      50.8876 |      29.5858 |
| beauty_profession | negative      | male          |         51 |         49 |          51 |     151 |      33.7748 |      32.4503 |      33.7748 |
| beauty_profession | negative      | female        |         52 |         44 |          55 |     151 |      34.4371 |      29.1391 |      36.4238 |
| beauty_profession | negative      | not_spacified |         50 |         54 |          46 |     150 |      33.3333 |      36      |      30.6667 |
| instituition      | negative      | male          |        190 |         98 |          53 |     341 |      55.7185 |      28.739  |      15.5425 |
| instituition      | negative      | female        |        208 |         64 |          55 |     327 |      63.6086 |      19.5719 |      16.8196 |
| instituition      | negative      | not_spacified |        198 |         61 |          46 |     305 |      64.918  |      20      |      15.082  |
| nationality       | negative      | male          |        113 |        121 |          50 |     284 |      39.7887 |      42.6056 |      17.6056 |
| nationality       | negative      | female        |        100 |        130 |          55 |     285 |      35.0877 |      45.614  |      19.2982 |
| nationality       | negative      | not_spacified |        111 |        124 |          50 |     285 |      38.9474 |      43.5088 |      17.5439 |
| ageism            | negative      | male          |         57 |         51 |          35 |     143 |      39.8601 |      35.6643 |      24.4755 |
| ageism            | negative      | female        |         56 |         56 |          31 |     143 |      39.1608 |      39.1608 |      21.6783 |
| ageism            | negative      | not_spacified |         49 |         56 |          38 |     143 |      34.2657 |      39.1608 |      26.5734 |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        458 |        406 |         226 |    1090 |      42.0183 |      37.2477 |      20.7339 |
| female        |        450 |        391 |         236 |    1077 |      41.7827 |      36.3045 |      21.9127 |
| not_spacified |        441 |        381 |         230 |    1052 |      41.9202 |      36.2167 |      21.8631 |



### Type 2, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |         87 |         37 |          40 |     164 |      53.0488 |      22.561  |      24.3902 |
| beauty            | positive      | female        |         95 |         31 |          37 |     163 |      58.2822 |      19.0184 |      22.6994 |
| beauty            | positive      | not_spacified |         88 |         25 |          51 |     164 |      53.6585 |      15.2439 |      31.0976 |
| beauty_profession | positive      | male          |         53 |         42 |          29 |     124 |      42.7419 |      33.871  |      23.3871 |
| beauty_profession | positive      | female        |         66 |         24 |          35 |     125 |      52.8    |      19.2    |      28      |
| beauty_profession | positive      | not_spacified |         45 |         39 |          42 |     126 |      35.7143 |      30.9524 |      33.3333 |
| instituition      | positive      | male          |        108 |         77 |          91 |     276 |      39.1304 |      27.8986 |      32.971  |
| instituition      | positive      | female        |        106 |         62 |          89 |     257 |      41.2451 |      24.1245 |      34.6304 |
| instituition      | positive      | not_spacified |        115 |         63 |          80 |     258 |      44.5736 |      24.4186 |      31.0078 |
| nationality       | positive      | male          |         66 |         35 |          31 |     132 |      50      |      26.5152 |      23.4848 |
| nationality       | positive      | female        |         69 |         25 |          38 |     132 |      52.2727 |      18.9394 |      28.7879 |
| nationality       | positive      | not_spacified |         85 |         27 |          20 |     132 |      64.3939 |      20.4545 |      15.1515 |
| ageism            | positive      | male          |         48 |         74 |          94 |     216 |      22.2222 |      34.2593 |      43.5185 |
| ageism            | positive      | female        |         55 |         81 |          80 |     216 |      25.463  |      37.5    |      37.037  |
| ageism            | positive      | not_spacified |         56 |         78 |          82 |     216 |      25.9259 |      36.1111 |      37.963  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        362 |        265 |         285 |     912 |      39.693  |      29.057  |       31.25  |
| female        |        391 |        223 |         279 |     893 |      43.785  |      24.972  |       31.243 |
| not_spacified |        389 |        232 |         275 |     896 |      43.4152 |      25.8929 |       30.692 |



### Type 2, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |         27 |        102 |          35 |     164 |      16.4634 |      62.1951 |      21.3415 |
| beauty            | negative      | female        |         34 |         94 |          36 |     164 |      20.7317 |      57.3171 |      21.9512 |
| beauty            | negative      | not_spacified |         31 |         97 |          36 |     164 |      18.9024 |      59.1463 |      21.9512 |
| beauty_profession | negative      | male          |         43 |         45 |          37 |     125 |      34.4    |      36      |      29.6    |
| beauty_profession | negative      | female        |         49 |         41 |          36 |     126 |      38.8889 |      32.5397 |      28.5714 |
| beauty_profession | negative      | not_spacified |         33 |         53 |          38 |     124 |      26.6129 |      42.7419 |      30.6452 |
| instituition      | negative      | male          |         63 |         93 |         109 |     265 |      23.7736 |      35.0943 |      41.1321 |
| instituition      | negative      | female        |         88 |         97 |          96 |     281 |      31.3167 |      34.5196 |      34.1637 |
| instituition      | negative      | not_spacified |         83 |         86 |          92 |     261 |      31.8008 |      32.9502 |      35.249  |
| nationality       | negative      | male          |         47 |         43 |          42 |     132 |      35.6061 |      32.5758 |      31.8182 |
| nationality       | negative      | female        |         41 |         46 |          45 |     132 |      31.0606 |      34.8485 |      34.0909 |
| nationality       | negative      | not_spacified |         45 |         52 |          35 |     132 |      34.0909 |      39.3939 |      26.5152 |
| ageism            | negative      | male          |         53 |         63 |         100 |     216 |      24.537  |      29.1667 |      46.2963 |
| ageism            | negative      | female        |         55 |         59 |         102 |     216 |      25.463  |      27.3148 |      47.2222 |
| ageism            | negative      | not_spacified |         52 |         63 |         101 |     216 |      24.0741 |      29.1667 |      46.7593 |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        233 |        346 |         323 |     902 |      25.8315 |      38.3592 |      35.8093 |
| female        |        267 |        337 |         315 |     919 |      29.0533 |      36.6703 |      34.2764 |
| not_spacified |        244 |        351 |         302 |     897 |      27.2018 |      39.1304 |      33.6678 |



## Kendall Tau Calculation

Total data: 6438

Kendall's Tau Correlation for type 1: 0.13943866416791184

P-Value: 9.391274824197845e-26

Total data: 5419

Kendall's Tau Correlation for type 2: 0.17505376451006674

P-Value: 2.4798212417220615e-32

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 6438

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.011069526318425634

P-Value: 0.3076518247015557

Total data: 5419

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.02793231159452394

P-Value: 0.020697295711181653

## Kendall Tau Calculation considering if there are any positive likelihood towards teacher education level for institutional bias

Total data: 6438

Kendall's Tau Correlation for type1 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

Total data: 5419

Kendall's Tau Correlation for type2 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

