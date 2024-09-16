# Contents 
*Scripts are tailored to the furniture sub-corpus in the singular condition*

```load_tuna.py```
- Downloads and unzips TUNA corpus

``` convert_to_json.py```

- Converts corpus from XML to json

```refine_tuna.py```

- Removes episodes whose descriptions use location

```visualize_tuna_sets.py```

- Creates a csv, html and html+images table containing 1. all episodes, and 2. only the 7 unique sets (6 files in total)

```identify_targets.py```

- Separates target and distractor images. Creates 2 csv files (Let to the conclusion that an image is either used as taget OR distractor, never both.)

```extract_all_imgs.py```

- Creates folder containing only the images used in the episodes left

```attribute_set.py```

- Work in progress, contains small algorithm to come up with minimal distinguishing expression based on available attributes