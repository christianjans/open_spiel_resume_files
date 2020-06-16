# Copyright 2019 DeepMind Technologies Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Starting point for playing with the AlphaZero algorithm."""

from absl import app
from absl import flags

from open_spiel.python.algorithms.alpha_zero import from_checkpoint
from open_spiel.python.utils import spawn

flags.DEFINE_string("path", None, "Where to save checkpoints.")
flags.DEFINE_integer("checkpoint", -1, "The checkpoint to resume training.")
flags.DEFINE_integer("steps", 25, "How many more training steps to do.")

FLAGS = flags.FLAGS


def main(unused_argv):
  from_checkpoint.from_checkpoint(FLAGS.path, FLAGS.checkpoint, FLAGS.steps)


if __name__ == "__main__":
  with spawn.main_handler():
    app.run(main)
