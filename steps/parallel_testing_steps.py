import time
import logging
from behave import *

logging.basicConfig(level=logging.INFO)


@when('entered jenkins credentials')
def implement(context):
    try:
        context.jenkins_page.confirm_entering_website()
        time.sleep(10)
    except:
        time.sleep(0)
    context.jenkins_page.enter_credentials()
    time.sleep(10)


@then('Parallel tests should have passed')
def implement(context):
    assert context.jenkins_page.build_failed() is False, "Last build has failed"


@step('Time taken should be less than "{max_minutes}" minutes')
def implement(context, max_minutes):
    current_time = context.jenkins_page.count_time_taken()
    assert current_time < int(max_minutes), f"Took too much time: {current_time}"
