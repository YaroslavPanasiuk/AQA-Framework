import time
import logging
from behave import *


@then('link to report should exist')
def implement(context):
    assert context.jenkins_page.report_link_exists(), "Report is not generated"
