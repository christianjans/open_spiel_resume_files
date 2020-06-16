# open_spiel_resume_files
Files used to resume training of the AlphaZero algorithm in the OpenSpiel framework.

This repository contains two folders, 'combined' and 'separate'.
- The files in 'combined', in particular **alpha_zero_v2.py**, modify the existing alpha_zero.py algorithm of OpenSpiel to  support resuming training. In this sense, both starting and resuming training can be done by calling the same python file.
- The files in 'separate', in particular **from_checkpoint.py**, only supports resuming training from an existing checkpoint. To begin training, alpha_zero.py from OpenSpiel must be used.

## To use the 'combined' files:
**NOTE:** The following paths are all relative to the open_spiel directory.
- Move (and replace) **data_logger.py** into open_spiel/python/utils/
- Move **alpha_zero_v2_example.py** into open_spiel/python/examples/
- Move **alpha_zero_v2.py** into open_spiel/python/algorithms/alpha_zero/

You can now begin training using the command:

  ```python3 open_spiel/python/examples/alpha_zero_v2_example.py --game=tic_tac_toe --path=...```

Or resume training from an existing checkpoint:

  ```python3 open_spiel/python/examples/alpha_zero_v2_example.py --checkpoint=25 --max_steps=10 --path=...```

