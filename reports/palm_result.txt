# Report for Model: palm

## Different Types of Likelihood Calculation

### Type 1, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        264 |         10 |         110 |     384 |      68.75   |      2.60417 |     28.6458  |
| beauty_profession | positive      |        274 |         75 |          92 |     441 |      62.1315 |     17.0068  |     20.8617  |
| instituition      | positive      |        668 |        218 |          85 |     971 |      68.7951 |     22.4511  |      8.75386 |
| nationality       | positive      |        472 |        121 |         107 |     700 |      67.4286 |     17.2857  |     15.2857  |
| ageism            | positive      |        216 |        144 |          64 |     424 |      50.9434 |     33.9623  |     15.0943  |



### Type 1, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |         14 |        318 |          44 |     376 |       3.7234 |      84.5745 |     11.7021  |
| beauty_profession | negative      |        136 |        179 |         140 |     455 |      29.8901 |      39.3407 |     30.7692  |
| instituition      | negative      |        397 |        478 |          92 |     967 |      41.0548 |      49.4312 |      9.51396 |
| nationality       | negative      |        374 |        203 |          94 |     671 |      55.7377 |      30.2534 |     14.0089  |
| ageism            | negative      |        121 |        254 |          52 |     427 |      28.3372 |      59.4848 |     12.178   |



### Type 1, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |      nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|---------:|
| beauty            |        278 |        328 |         154 |     760 | 36.5789 | 43.1579 | 20.2632  |
| beauty_profession |        410 |        254 |         232 |     896 | 45.7589 | 28.3482 | 25.8929  |
| instituition      |       1065 |        696 |         177 |    1938 | 54.9536 | 35.9133 |  9.13313 |
| nationality       |        846 |        324 |         201 |    1371 | 61.7068 | 23.6324 | 14.6608  |
| ageism            |        337 |        398 |         116 |     851 | 39.6005 | 46.7685 | 13.631   |



### Type 2, Positive Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      |        192 |        124 |         146 |     462 |      41.5584 |      26.8398 |     31.6017  |
| beauty_profession | positive      |         81 |        182 |         106 |     369 |      21.9512 |      49.3225 |     28.7263  |
| instituition      | positive      |        551 |        205 |          69 |     825 |      66.7879 |      24.8485 |      8.36364 |
| nationality       | positive      |        228 |         14 |         136 |     378 |      60.3175 |       3.7037 |     35.9788  |
| ageism            | positive      |        372 |        124 |         150 |     646 |      57.5851 |      19.195  |     23.2198  |



### Type 2, Negative Attribute

| bias_type         | target_term   |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      |         17 |        290 |          35 |     342 |      4.97076 |      84.7953 |      10.2339 |
| beauty_profession | negative      |         42 |        235 |          95 |     372 |     11.2903  |      63.172  |      25.5376 |
| instituition      | negative      |        242 |        447 |         126 |     815 |     29.6933  |      54.8466 |      15.4601 |
| nationality       | negative      |        100 |        100 |         117 |     317 |     31.5457  |      31.5457 |      36.9085 |
| ageism            | negative      |        208 |        330 |         110 |     648 |     32.0988  |      50.9259 |      16.9753 |



### Type 2, Combined Attribute

| bias_type         |   positive |   negative |   unrelated |   total |      pl |      nl |     nul |
|:------------------|-----------:|-----------:|------------:|--------:|--------:|--------:|--------:|
| beauty            |        209 |        414 |         181 |     804 | 25.995  | 51.4925 | 22.5124 |
| beauty_profession |        123 |        417 |         201 |     741 | 16.5992 | 56.2753 | 27.1255 |
| instituition      |        793 |        652 |         195 |    1640 | 48.3537 | 39.7561 | 11.8902 |
| nationality       |        328 |        114 |         253 |     695 | 47.1942 | 16.4029 | 36.4029 |
| ageism            |        580 |        454 |         260 |    1294 | 44.8223 | 35.085  | 20.0927 |



### Type 1, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |         83 |          2 |          41 |     126 |      65.873  |      1.5873  |     32.5397  |
| beauty            | positive      | female        |         91 |          3 |          37 |     131 |      69.4656 |      2.29008 |     28.2443  |
| beauty            | positive      | not_spacified |         90 |          5 |          32 |     127 |      70.8661 |      3.93701 |     25.1969  |
| beauty_profession | positive      | male          |        103 |         19 |          26 |     148 |      69.5946 |     12.8378  |     17.5676  |
| beauty_profession | positive      | female        |         89 |         26 |          29 |     144 |      61.8056 |     18.0556  |     20.1389  |
| beauty_profession | positive      | not_spacified |         82 |         30 |          37 |     149 |      55.0336 |     20.1342  |     24.8322  |
| instituition      | positive      | male          |        214 |         84 |          32 |     330 |      64.8485 |     25.4545  |      9.69697 |
| instituition      | positive      | female        |        233 |         76 |          27 |     336 |      69.3452 |     22.619   |      8.03571 |
| instituition      | positive      | not_spacified |        221 |         58 |          26 |     305 |      72.459  |     19.0164  |      8.52459 |
| nationality       | positive      | male          |        143 |         46 |          45 |     234 |      61.1111 |     19.6581  |     19.2308  |
| nationality       | positive      | female        |        163 |         37 |          33 |     233 |      69.9571 |     15.8798  |     14.1631  |
| nationality       | positive      | not_spacified |        166 |         38 |          29 |     233 |      71.2446 |     16.309   |     12.4464  |
| ageism            | positive      | male          |         64 |         52 |          25 |     141 |      45.3901 |     36.8794  |     17.7305  |
| ageism            | positive      | female        |         77 |         41 |          24 |     142 |      54.2254 |     28.8732  |     16.9014  |
| ageism            | positive      | not_spacified |         75 |         51 |          15 |     141 |      53.1915 |     36.1702  |     10.6383  |



### Type 1, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        607 |        203 |         169 |     979 |      62.002  |      20.7354 |      17.2625 |
| female        |        653 |        183 |         150 |     986 |      66.2272 |      18.5598 |      15.213  |
| not_spacified |        634 |        182 |         139 |     955 |      66.3874 |      19.0576 |      14.555  |



### Type 1, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |          3 |        108 |          14 |     125 |       2.4    |      86.4    |     11.2     |
| beauty            | negative      | female        |          6 |        103 |          17 |     126 |       4.7619 |      81.746  |     13.4921  |
| beauty            | negative      | not_spacified |          5 |        107 |          13 |     125 |       4      |      85.6    |     10.4     |
| beauty_profession | negative      | male          |         53 |         49 |          50 |     152 |      34.8684 |      32.2368 |     32.8947  |
| beauty_profession | negative      | female        |         37 |         72 |          42 |     151 |      24.5033 |      47.6821 |     27.8146  |
| beauty_profession | negative      | not_spacified |         46 |         58 |          48 |     152 |      30.2632 |      38.1579 |     31.5789  |
| instituition      | negative      | male          |        120 |        187 |          30 |     337 |      35.6083 |      55.4896 |      8.90208 |
| instituition      | negative      | female        |        136 |        164 |          28 |     328 |      41.4634 |      50      |      8.53659 |
| instituition      | negative      | not_spacified |        141 |        127 |          34 |     302 |      46.6887 |      42.053  |     11.2583  |
| nationality       | negative      | male          |        108 |         85 |          33 |     226 |      47.7876 |      37.6106 |     14.6018  |
| nationality       | negative      | female        |        130 |         57 |          36 |     223 |      58.296  |      25.5605 |     16.1435  |
| nationality       | negative      | not_spacified |        136 |         61 |          25 |     222 |      61.2613 |      27.4775 |     11.2613  |
| ageism            | negative      | male          |         42 |         82 |          18 |     142 |      29.5775 |      57.7465 |     12.6761  |
| ageism            | negative      | female        |         43 |         81 |          18 |     142 |      30.2817 |      57.0423 |     12.6761  |
| ageism            | negative      | not_spacified |         36 |         91 |          16 |     143 |      25.1748 |      63.6364 |     11.1888  |



### Type 1, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        326 |        511 |         145 |     982 |      33.1976 |      52.0367 |      14.7658 |
| female        |        352 |        477 |         141 |     970 |      36.2887 |      49.1753 |      14.5361 |
| not_spacified |        364 |        444 |         136 |     944 |      38.5593 |      47.0339 |      14.4068 |



### Type 2, Positive Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | positive      | male          |         50 |         44 |          60 |     154 |      32.4675 |     28.5714  |     38.961   |
| beauty            | positive      | female        |         75 |         36 |          44 |     155 |      48.3871 |     23.2258  |     28.3871  |
| beauty            | positive      | not_spacified |         67 |         44 |          42 |     153 |      43.7908 |     28.7582  |     27.451   |
| beauty_profession | positive      | male          |         24 |         62 |          37 |     123 |      19.5122 |     50.4065  |     30.0813  |
| beauty_profession | positive      | female        |         34 |         57 |          33 |     124 |      27.4194 |     45.9677  |     26.6129  |
| beauty_profession | positive      | not_spacified |         23 |         63 |          36 |     122 |      18.8525 |     51.6393  |     29.5082  |
| instituition      | positive      | male          |        194 |         75 |          20 |     289 |      67.128  |     25.9516  |      6.92042 |
| instituition      | positive      | female        |        167 |         77 |          24 |     268 |      62.3134 |     28.7313  |      8.95522 |
| instituition      | positive      | not_spacified |        190 |         53 |          25 |     268 |      70.8955 |     19.7761  |      9.32836 |
| nationality       | positive      | male          |         77 |          7 |          42 |     126 |      61.1111 |      5.55556 |     33.3333  |
| nationality       | positive      | female        |         68 |          4 |          53 |     125 |      54.4    |      3.2     |     42.4     |
| nationality       | positive      | not_spacified |         83 |          3 |          41 |     127 |      65.3543 |      2.3622  |     32.2835  |
| ageism            | positive      | male          |        114 |         46 |          56 |     216 |      52.7778 |     21.2963  |     25.9259  |
| ageism            | positive      | female        |        123 |         38 |          53 |     214 |      57.4766 |     17.757   |     24.7664  |
| ageism            | positive      | not_spacified |        135 |         40 |          41 |     216 |      62.5    |     18.5185  |     18.9815  |



### Type 2, Positive, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        459 |        234 |         215 |     908 |      50.5507 |      25.7709 |      23.6784 |
| female        |        467 |        212 |         207 |     886 |      52.7088 |      23.9278 |      23.3634 |
| not_spacified |        498 |        203 |         185 |     886 |      56.2077 |      22.912  |      20.8804 |



### Type 2, Negative Attribute

| bias_type         | target_term   | gender        |   positive |   negative |   unrelated |   total |   neg_to_pos |   neg_to_neg |   neg_to_neu |
|:------------------|:--------------|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| beauty            | negative      | male          |          4 |         97 |          13 |     114 |      3.50877 |      85.0877 |     11.4035  |
| beauty            | negative      | female        |          8 |         96 |          11 |     115 |      6.95652 |      83.4783 |      9.56522 |
| beauty            | negative      | not_spacified |          5 |         97 |          11 |     113 |      4.42478 |      85.8407 |      9.73451 |
| beauty_profession | negative      | male          |         11 |         81 |          31 |     123 |      8.94309 |      65.8537 |     25.2033  |
| beauty_profession | negative      | female        |         20 |         76 |          28 |     124 |     16.129   |      61.2903 |     22.5806  |
| beauty_profession | negative      | not_spacified |         11 |         78 |          36 |     125 |      8.8     |      62.4    |     28.8     |
| instituition      | negative      | male          |         79 |        152 |          39 |     270 |     29.2593  |      56.2963 |     14.4444  |
| instituition      | negative      | female        |         83 |        153 |          47 |     283 |     29.3286  |      54.0636 |     16.6078  |
| instituition      | negative      | not_spacified |         80 |        142 |          40 |     262 |     30.5344  |      54.1985 |     15.2672  |
| nationality       | negative      | male          |         35 |         34 |          39 |     108 |     32.4074  |      31.4815 |     36.1111  |
| nationality       | negative      | female        |         33 |         28 |          45 |     106 |     31.1321  |      26.4151 |     42.4528  |
| nationality       | negative      | not_spacified |         32 |         38 |          33 |     103 |     31.068   |      36.8932 |     32.0388  |
| ageism            | negative      | male          |         63 |        120 |          33 |     216 |     29.1667  |      55.5556 |     15.2778  |
| ageism            | negative      | female        |         66 |        108 |          42 |     216 |     30.5556  |      50      |     19.4444  |
| ageism            | negative      | not_spacified |         79 |        102 |          35 |     216 |     36.5741  |      47.2222 |     16.2037  |



### Type 2, Negative, Gender

| bias_type     |   positive |   negative |   unrelated |   total |   pos_to_pos |   pos_to_neg |   pos_to_neu |
|:--------------|-----------:|-----------:|------------:|--------:|-------------:|-------------:|-------------:|
| male          |        192 |        484 |         155 |     831 |      23.1047 |      58.2431 |      18.6522 |
| female        |        210 |        461 |         173 |     844 |      24.8815 |      54.6209 |      20.4976 |
| not_spacified |        207 |        457 |         155 |     819 |      25.2747 |      55.7998 |      18.9255 |



## Kendall Tau Calculation

Total data: 5816

Kendall's Tau Correlation for type 1: 0.33803064732493393

P-Value: 4.957858450397331e-133

Total data: 5175

Kendall's Tau Correlation for type 2: 0.3670800065345749

P-Value: 3.1226561559986214e-133

## Kendall Tau Calculation considering if there are any positive likelihood towards feminine gendered pronoun

Total data: 5816

Kendall's Tau Correlation for type1 Considering more positive likelihood towards feminine gendered pronoun: 0.025592345689640493

P-Value: 0.02284816987651979

Total data: 5175

Kendall's Tau Correlation for type2 Considering more positive likelihood towards feminine gendered pronoun: 0.016528628439403486

P-Value: 0.1758207603179185

## Kendall Tau Calculation considering if there are any positive likelihood towards teacher education level for institutional bias

Total data: 5816

Kendall's Tau Correlation for type1 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

Total data: 5175

Kendall's Tau Correlation for type2 Considering more positive likelihood towards TEACHER: nan

P-Value: nan

