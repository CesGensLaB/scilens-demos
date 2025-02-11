import os

from scilens import StandaloneTaskRunner


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

runner = StandaloneTaskRunner(f"{SCRIPT_DIR}/scilens.yml")
results = runner.process(SCRIPT_DIR, origin_working_dir=SCRIPT_DIR)

if results.error:
    raise Exception(results.error)
else:
    # here we expect no errors and no warnings
    # but this demo will raise an AssertionError
    assert not results.processor_results.errors and not results.processor_results.warnings
