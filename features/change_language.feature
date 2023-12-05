Feature: Example Feature
    Scenario: Change language to German
        Given open website "http://opencart.qatestlab.net/"
        When change language to "De"
        Then view "schedule" should be written in "German"
        And view "phone" should be written in "German"
        And view "search" should be written in "German"

    Scenario: Change language to Ukrainian
        Given open website "http://opencart.qatestlab.net/"
        When change language to "Ua"
        Then view "search" should be written in "Ukrainian"
        And view "phone" should be written in "Ukrainian"
        And view "achedule" should be written in "Ukrainian"

    Scenario: Change language to English
        Given open website "http://opencart.qatestlab.net/"
        When change language to "En"
        Then view "schedule" should be written in "English"
        And view "phone" should be written in "English"
        And view "search" should be written in "English"