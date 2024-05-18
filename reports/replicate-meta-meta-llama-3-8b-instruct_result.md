# Report for Model: replicate/meta/meta-llama-3-8b-instruct

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        288 |          6 |         102 |     396 |      72.7273 |      1.51515 |      25.7576 |
| beauty_profession | positive      |        143 |         20 |          44 |     207 |      69.0821 |      9.66184 |      21.256  |
| instituition      | positive      |        474 |        273 |          89 |     836 |      56.6986 |     32.6555  |      10.6459 |
| nationality       | positive      |        569 |        179 |          79 |     827 |      68.8029 |     21.6445  |       9.5526 |
| ageism            | positive      |        138 |         82 |          36 |     256 |      53.9062 |     32.0312  |      14.0625 |



### Type 1, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |          8 |        366 |          24 |     398 |      2.01005 |      91.9598 |      6.03015 |
| beauty_profession | negative      |         60 |         54 |          47 |     161 |     37.2671  |      33.5404 |     29.1925  |
| instituition      | negative      |        302 |        440 |          62 |     804 |     37.5622  |      54.7264 |      7.71144 |
| nationality       | negative      |        389 |        383 |          64 |     836 |     46.5311  |      45.8134 |      7.6555  |
| ageism            | negative      |         88 |        155 |          17 |     260 |     33.8462  |      59.6154 |      6.53846 |



### Type 1, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |      nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|---------:|
| beauty            |        296 |        372 |         126 |     794 | 37.2796 | 46.8514 | 15.869   |
| beauty_profession |        203 |         74 |          91 |     368 | 55.163  | 20.1087 | 24.7283  |
| instituition      |        776 |        713 |         151 |    1640 | 47.3171 | 43.4756 |  9.20732 |
| nationality       |        958 |        562 |         143 |    1663 | 57.6067 | 33.7943 |  8.59892 |
| ageism            |        226 |        237 |          53 |     516 | 43.7984 | 45.9302 | 10.2713  |



### Type 2, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        196 |        184 |          94 |     474 |      41.3502 |     38.8186  |      19.8312 |
| beauty_profession | positive      |        114 |        194 |          67 |     375 |      30.4    |     51.7333  |      17.8667 |
| instituition      | positive      |        139 |        168 |         113 |     420 |      33.0952 |     40       |      26.9048 |
| nationality       | positive      |        277 |         33 |          79 |     389 |      71.2082 |      8.48329 |      20.3085 |
| ageism            | positive      |        136 |        202 |         310 |     648 |      20.9877 |     31.1728  |      47.8395 |



### Type 2, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |          5 |        440 |          22 |     467 |      1.07066 |      94.2184 |      4.71092 |
| beauty_profession | negative      |         41 |        278 |          58 |     377 |     10.8753  |      73.7401 |     15.3846  |
| instituition      | negative      |         94 |        203 |         173 |     470 |     20       |      43.1915 |     36.8085  |
| nationality       | negative      |        113 |        185 |          77 |     375 |     30.1333  |      49.3333 |     20.5333  |
| ageism            | negative      |         92 |        365 |         191 |     648 |     14.1975  |      56.3272 |     29.4753  |



### Type 2, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| beauty            |        201 |        624 |         116 |     941 | 21.3603 | 66.3124 | 12.3273 |
| beauty_profession |        155 |        472 |         125 |     752 | 20.6117 | 62.766  | 16.6223 |
| instituition      |        233 |        371 |         286 |     890 | 26.1798 | 41.6854 | 32.1348 |
| nationality       |        390 |        218 |         156 |     764 | 51.0471 | 28.534  | 20.4188 |
| ageism            |        228 |        567 |         501 |    1296 | 17.5926 | 43.75   | 38.6574 |



### Type 1, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |         94 |          2 |          36 |     132 |      71.2121 |      1.51515 |     27.2727  |
| beauty            | positive      | female        |         91 |          0 |          32 |     123 |      73.9837 |      0       |     26.0163  |
| beauty            | positive      | not_spacified |        103 |          4 |          34 |     141 |      73.0496 |      2.83688 |     24.1135  |
| beauty_profession | positive      | male          |         58 |          3 |          14 |      75 |      77.3333 |      4       |     18.6667  |
| beauty_profession | positive      | female        |         50 |          6 |          12 |      68 |      73.5294 |      8.82353 |     17.6471  |
| beauty_profession | positive      | not_spacified |         35 |         11 |          18 |      64 |      54.6875 |     17.1875  |     28.125   |
| instituition      | positive      | male          |        145 |        101 |          39 |     285 |      50.8772 |     35.4386  |     13.6842  |
| instituition      | positive      | female        |        181 |         78 |          26 |     285 |      63.5088 |     27.3684  |      9.12281 |
| instituition      | positive      | not_spacified |        148 |         94 |          24 |     266 |      55.6391 |     35.3383  |      9.02256 |
| nationality       | positive      | male          |        167 |         79 |          30 |     276 |      60.5072 |     28.6232  |     10.8696  |
| nationality       | positive      | female        |        198 |         54 |          27 |     279 |      70.9677 |     19.3548  |      9.67742 |
| nationality       | positive      | not_spacified |        204 |         46 |          22 |     272 |      75      |     16.9118  |      8.08824 |
| ageism            | positive      | male          |         45 |         26 |          13 |      84 |      53.5714 |     30.9524  |     15.4762  |
| ageism            | positive      | female        |         54 |         21 |          12 |      87 |      62.069  |     24.1379  |     13.7931  |
| ageism            | positive      | not_spacified |         39 |         35 |          11 |      85 |      45.8824 |     41.1765  |     12.9412  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        509 |        211 |         132 |     852 |      59.7418 |      24.7653 |      15.493  |
| female        |        574 |        159 |         109 |     842 |      68.171  |      18.8836 |      12.9454 |
| not_spacified |        529 |        190 |         109 |     828 |      63.8889 |      22.9469 |      13.1643 |



### Type 1, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |          2 |        126 |           5 |     133 |      1.50376 |      94.7368 |      3.7594  |
| beauty            | negative      | female        |          5 |        107 |          12 |     124 |      4.03226 |      86.2903 |      9.67742 |
| beauty            | negative      | not_spacified |          1 |        133 |           7 |     141 |      0.70922 |      94.3262 |      4.96454 |
| beauty_profession | negative      | male          |         23 |         12 |          12 |      47 |     48.9362  |      25.5319 |     25.5319  |
| beauty_profession | negative      | female        |         17 |         19 |          20 |      56 |     30.3571  |      33.9286 |     35.7143  |
| beauty_profession | negative      | not_spacified |         20 |         23 |          15 |      58 |     34.4828  |      39.6552 |     25.8621  |
| instituition      | negative      | male          |         85 |        177 |          19 |     281 |     30.2491  |      62.9893 |      6.76157 |
| instituition      | negative      | female        |        113 |        137 |          22 |     272 |     41.5441  |      50.3676 |      8.08824 |
| instituition      | negative      | not_spacified |        104 |        126 |          21 |     251 |     41.4343  |      50.1992 |      8.36653 |
| nationality       | negative      | male          |        108 |        150 |          24 |     282 |     38.2979  |      53.1915 |      8.51064 |
| nationality       | negative      | female        |        141 |        116 |          23 |     280 |     50.3571  |      41.4286 |      8.21429 |
| nationality       | negative      | not_spacified |        140 |        117 |          17 |     274 |     51.0949  |      42.7007 |      6.20438 |
| ageism            | negative      | male          |         31 |         52 |           6 |      89 |     34.8315  |      58.427  |      6.74157 |
| ageism            | negative      | female        |         36 |         44 |           7 |      87 |     41.3793  |      50.5747 |      8.04598 |
| ageism            | negative      | not_spacified |         21 |         59 |           4 |      84 |     25       |      70.2381 |      4.7619  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        249 |        517 |          66 |     832 |      29.9279 |      62.1394 |      7.93269 |
| female        |        312 |        423 |          84 |     819 |      38.0952 |      51.6484 |     10.2564  |
| not_spacified |        286 |        458 |          64 |     808 |      35.396  |      56.6832 |      7.92079 |



### Type 2, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |         53 |         64 |          41 |     158 |      33.5443 |     40.5063  |      25.9494 |
| beauty            | positive      | female        |         76 |         53 |          27 |     156 |      48.7179 |     33.9744  |      17.3077 |
| beauty            | positive      | not_spacified |         67 |         67 |          26 |     160 |      41.875  |     41.875   |      16.25   |
| beauty_profession | positive      | male          |         24 |         78 |          24 |     126 |      19.0476 |     61.9048  |      19.0476 |
| beauty_profession | positive      | female        |         61 |         44 |          20 |     125 |      48.8    |     35.2     |      16      |
| beauty_profession | positive      | not_spacified |         29 |         72 |          23 |     124 |      23.3871 |     58.0645  |      18.5484 |
| instituition      | positive      | male          |         50 |         58 |          40 |     148 |      33.7838 |     39.1892  |      27.027  |
| instituition      | positive      | female        |         44 |         57 |          38 |     139 |      31.6547 |     41.0072  |      27.3381 |
| instituition      | positive      | not_spacified |         45 |         53 |          35 |     133 |      33.8346 |     39.8496  |      26.3158 |
| nationality       | positive      | male          |         89 |         18 |          21 |     128 |      69.5312 |     14.0625  |      16.4062 |
| nationality       | positive      | female        |         85 |         11 |          35 |     131 |      64.8855 |      8.39695 |      26.7176 |
| nationality       | positive      | not_spacified |        103 |          4 |          23 |     130 |      79.2308 |      3.07692 |      17.6923 |
| ageism            | positive      | male          |         42 |         75 |          99 |     216 |      19.4444 |     34.7222  |      45.8333 |
| ageism            | positive      | female        |         44 |         58 |         114 |     216 |      20.3704 |     26.8519  |      52.7778 |
| ageism            | positive      | not_spacified |         50 |         69 |          97 |     216 |      23.1481 |     31.9444  |      44.9074 |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        258 |        293 |         225 |     776 |      33.2474 |      37.7577 |      28.9948 |
| female        |        310 |        223 |         234 |     767 |      40.4172 |      29.0743 |      30.5085 |
| not_spacified |        294 |        265 |         204 |     763 |      38.5321 |      34.7313 |      26.7366 |



### Type 2, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |          2 |        146 |           8 |     156 |      1.28205 |      93.5897 |      5.12821 |
| beauty            | negative      | female        |          3 |        147 |           8 |     158 |      1.89873 |      93.038  |      5.06329 |
| beauty            | negative      | not_spacified |          0 |        147 |           6 |     153 |      0       |      96.0784 |      3.92157 |
| beauty_profession | negative      | male          |          7 |        101 |          18 |     126 |      5.55556 |      80.1587 |     14.2857  |
| beauty_profession | negative      | female        |         16 |         88 |          21 |     125 |     12.8     |      70.4    |     16.8     |
| beauty_profession | negative      | not_spacified |         18 |         89 |          19 |     126 |     14.2857  |      70.6349 |     15.0794  |
| instituition      | negative      | male          |         29 |         66 |          62 |     157 |     18.4713  |      42.0382 |     39.4904  |
| instituition      | negative      | female        |         31 |         81 |          55 |     167 |     18.5629  |      48.503  |     32.9341  |
| instituition      | negative      | not_spacified |         34 |         56 |          56 |     146 |     23.2877  |      38.3562 |     38.3562  |
| nationality       | negative      | male          |         34 |         64 |          27 |     125 |     27.2     |      51.2    |     21.6     |
| nationality       | negative      | female        |         43 |         55 |          27 |     125 |     34.4     |      44      |     21.6     |
| nationality       | negative      | not_spacified |         36 |         66 |          23 |     125 |     28.8     |      52.8    |     18.4     |
| ageism            | negative      | male          |         27 |        129 |          60 |     216 |     12.5     |      59.7222 |     27.7778  |
| ageism            | negative      | female        |         31 |        104 |          81 |     216 |     14.3519  |      48.1481 |     37.5     |
| ageism            | negative      | not_spacified |         34 |        132 |          50 |     216 |     15.7407  |      61.1111 |     23.1481  |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |         99 |        506 |         175 |     780 |      12.6923 |      64.8718 |      22.4359 |
| female        |        124 |        475 |         192 |     791 |      15.6764 |      60.0506 |      24.2731 |
| not_spacified |        122 |        490 |         154 |     766 |      15.9269 |      63.9687 |      20.1044 |



## Kendall Tau Calculation

Total data: 6456

Kendall's Tau Correlation for type 1: 0.32583812028886033

P-Value: 2.8284199967042556e-128

Total data: 5484

Kendall's Tau Correlation for type 2: 0.30737744601229705

P-Value: 3.735783174904031e-99

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 6456

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.05554068029279124

P-Value: 4.897791682647787e-07

Total data: 5484

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.04422144308407829

P-Value: 0.00019598336493404183

## Kendall Tau Calculation considering if there are any positive likelihood towards teacher education level for institutional bias

Total data: 6456

Kendall's Tau Correlation for type1 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

Total data: 5484

Kendall's Tau Correlation for type2 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

