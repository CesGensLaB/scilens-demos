import os

from scilens import StandaloneTaskRunner


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

runner = StandaloneTaskRunner(f"{SCRIPT_DIR}/scilens.yml", config_override=f"{SCRIPT_DIR}/scilens.override.yml")
results = runner.process(SCRIPT_DIR, origin_working_dir=SCRIPT_DIR)

