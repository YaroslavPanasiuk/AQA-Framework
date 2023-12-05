Feature: Example Feature
    Scenario: Change language to German
        Given open website "http://opencart.qatestlab.net/"
        When change language to "De"
        Then "schedule" should be written in "German"
        And "phone" should be written in "German"
        And "search" should be written in "German"

    Scenario: Change language to Ukrainian
        Given open website "http://opencart.qatestlab.net/"
        When change language to "Ua"
        Then "search" should be written in "Ukrainian"
        And "phone" should be written in "Ukrainian"
        And "achedule" should be written in "Ukrainian"

    Scenario: Change language to English
        Given open website "http://opencart.qatestlab.net/"
        When change language to "En"
        Then "schedule" should be written in "English"
        And "phone" should be written in "English"
        And "search" should be written in "English"