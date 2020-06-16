# open_spiel_resume_files
Files used to resume training of the AlphaZero algorithm in the OpenSpiel framework.

This repository contains two folders, 'combined' and 'separate'.
- The files in 'combined', in particular alpha_zero_v2.py, modify the existing alpha_zero.py algorithm of OpenSpiel to account support resuming training. In this sense, both starting and resuming training can be done by calling the same python file.
- The files in 'separate', in particular from_checkpoint.py, only supports resuming training from an existing checkpoint. To begin training, alpha_zero.py from OpenSpiel must be used.
