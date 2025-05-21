import os

from scilens import StandaloneTaskRunner


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

runner = StandaloneTaskRunner(f"{SCRIPT_DIR}/scilens.yml")

runner.config.report.description = "This is a description included in the generated reports. It could explains the context, a use case, a test, ... ."

html_report = runner.config.report.html
html_report.custom_style       = "h1, h2, h3, h4 { color: #f2008f; }"
html_report.extra_html_start   = "<h2>Extra HTML start</h2><div>Some extra HTML at the start of the report</div>"
html_report.extra_html_summary = "<h3>Extra HTML summary</h3><div>Some extra HTML in the summary of the report</div>"
html_report.extra_html_end     = "<h2>Extra HTML end</h2><div>Some extra HTML at the end of the report</div>"
html_report.custom_script_head = "console.log('Custom script in the head of the report')"
html_report.custom_script_body = "console.log('Custom script in the body of the report')"


results = runner.process(SCRIPT_DIR, origin_working_dir=SCRIPT_DIR)

print(results.error)
print(results.processor_results.errors)
