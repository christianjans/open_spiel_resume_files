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

from open_spiel.python.algorithms.alpha_zero import alpha_zero_v2
from open_spiel.python.utils import spawn


flags.DEFINE_string("path", None, "Where to save checkpoints.")
flags.DEFINE_integer(
    "checkpoint", None, "The checkpoint to resume training from.")
flags.DEFINE_integer("max_steps", 0, "How many learn steps before exiting.")

FLAGS = flags.FLAGS


def main(unused_argv):
  if FLAGS.checkpoint is not None:
    alpha_zero_v2.from_checkpoint(FLAGS.path, FLAGS.checkpoint, FLAGS.max_steps)
  else:
    config = alpha_zero_v2.Config(
        game="tic_tac_toe",
        path=FLAGS.path,
        learning_rate=0.01,
        weight_decay=1e-4,
        train_batch_size=128,
        replay_buffer_size=2**14,
        replay_buffer_reuse=4,
        max_steps=FLAGS.max_steps,  # how many steps in training
        checkpoint_freq=FLAGS.max_steps,  # how often it saves the model

        actors=4,
        evaluators=4,
        uct_c=1,
        max_simulations=20,
        policy_alpha=0.25,
        policy_epsilon=1,
        temperature=1,
        temperature_drop=4,
        evaluation_window=50,
        eval_levels=7,

        nn_model="resnet",
        nn_width=128,
        nn_depth=2,
        observation_shape=None,
        output_size=None,

        quiet=True,
    )
    alpha_zero_v2.alpha_zero(config)


if __name__ == "__main__":
  with spawn.main_handler():
    app.run(main)