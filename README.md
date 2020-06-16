# open_spiel_resume_files
Files used to resume training of the AlphaZero algorithm in the OpenSpiel framework.

This repository contains two folders, 'combined' and 'separate'.
- The files in 'combined', in particular **alpha_zero_v2.py**, modify the existing alpha_zero.py algorithm of OpenSpiel to  support resuming training. In this sense, both starting and resuming training can be done by calling the same python file.
- The files in 'separate', in particular **from_checkpoint.py**, only supports resuming training from an existing checkpoint. To begin training, alpha_zero.py from OpenSpiel must be used.

## Difference between 'combined' and 'separate':
Apart from the differences mentioned above, the code in the 'separate' files (particularly from_checkpoint.py) is a little cleaner and doesn't infringe on the original OpenSpiel files as much, but reuses a lot of code from the original alpha_zero.py.

In the 'combined' files, alpha_zero_v2.py can completely replace alpha_zero.py, but the code is not as clean just due to the fact that some extra stuff/statements had to be included to work around supporting both starting and resuming training.

Despite this, both the files in 'combined' and 'separate' were made so that no other element of OpenSpiel relies on them, so there's no repercussion in adding or removing them (as long as you put the original data_logger.py back of course).

## How to use:
### To use the 'combined' files:
**NOTE:** The following paths are all relative to the open_spiel directory.
- Move (and replace) **data_logger.py** into open_spiel/python/utils/
- Move **alpha_zero_v2_example.py** into open_spiel/python/examples/
- Move **alpha_zero_v2.py** into open_spiel/python/algorithms/alpha_zero/

You can now begin training using the command:

  ```python3 open_spiel/python/examples/alpha_zero_v2_example.py --game=tic_tac_toe --uct_c=...```

Or resume training from an existing checkpoint (only specifying the checkpoint, max_steps, and path flags):

  ```python3 open_spiel/python/examples/alpha_zero_v2_example.py --checkpoint=25 --max_steps=10 --path=...```

Where ```checkpoint``` is the checkpoint to start from (must have model weights for that checkpoint, use ```--checkpoint=-1``` for the most recent checkpoint), ```max_steps``` is the number of training steps to do in this resumed training session, and ```path``` is the path to the directory containing the checkpoint weights, config.json, and learner.jsonl.

### To use the 'separate' files:
**NOTE:** The following paths are all relative to the open_spiel directory.
- Move (and replace) **data_logger.py** into open_spiel/python/utils/
- Move **alpha_zero_from_checkpoint.py** into open_spiel/python/examples/
- Move **from_checkpoint.py** into open_spiel/python/algorithms/alpha_zero/

You can now begin training using the command:

  ```python3 open_spiel/python/examples/alpha_zero.py --game=tic_tac_toe --uct_c=...```

Or resume training from an existing checkpoint (only specifying the ```checkpoint```, ```max_steps```, and ```path``` flags):

  ```python3 open_spiel/python/examples/alpha_zero_from_checkpoint.py --checkpoint=25 --steps=10 --path=...```

Where ```checkpoint``` is the checkpoint to start from (must have model weights for that checkpoint, use ```--checkpoint=-1``` for the most recent checkpoint), ```steps``` is the number of training steps to do in this resumed training session, and ```path``` is the path to the directory containing the checkpoint weights, config.json, and learner.jsonl.
