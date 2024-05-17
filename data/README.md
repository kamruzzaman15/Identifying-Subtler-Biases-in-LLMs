# Dataset Descriptions

There are 8 columns in our dataset. The description of each column is given below:

### 1. bias_type
This column indicates different types of biases. 

### 2. target_gender
This column indicates the particular gender type. There are three unique gender types namely 'male', 'female', and 'not_spacified', and we refer these three gender types as 'masculine', 'feminine', and 'non_binary' respectively in our paper writing.

male =  masculine
female  = feminine
not_spacified = non_binary

### 3. context
This column indicates different sentences. These are the context sentences.

### 4. item_category
This column is either 'positive' or 'negative'. When the attribute or stimulus in the context sentence is positive, we named it as 'positive' and when the attribute or stimulus is negative, then we named it as 'negative'.   

### 5. type_category
This columns tells us, which direction the data is. There are two different types of direction, namely type1 and type2. We refer these two directions as Stimulus to Attribute Inference (SAI) and Attribute to Stimulus Association (ASA) in our paper. 

type1 =  Stimulus to Attribute Inference (SAI)
type2 = Attribute to Stimulus Association (ASA)

### 6. anti_stereotype
When the 'item_category' column is 'negative', then this column contains attribute/stimulus that is positive among the options according to our definition. On the other hand, when the 'item_category' column is 'positive', then this column contains attribute/stimulus that is negative among the options according to our definition in paper. 

### 7. stereotype
This column is opposite of 'anti_stereotype' column. When the 'item_category' column is 'negative', then this column contains attribute/stimulus that is negative among the options according to our definition. On the other hand, when the 'item_category' column is 'positive', then this column contains attribute/stimulus that is positive among the options according to our definition in paper.

### 8. unrelated
This column contains the neutral attributes or stimuli according to our definition in paper. 


