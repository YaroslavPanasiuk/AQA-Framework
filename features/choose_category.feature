Feature: Example Feature
    Scenario: Choose category "Dogs"
        Given open website "http://opencart.qatestlab.net/"
        When click on "Dogs" in menu
        Then Products header should be "Dogs"
    Scenario: Choose category "Cats"
        Given open website "http://opencart.qatestlab.net/"
        When click on "Cats" in menu
        Then Products header should be "Cats"
    Scenario: Choose category "Small Pets"
        Given open website "http://opencart.qatestlab.net/"
        When click on "Small Pets" in menu
        Then Products header should be "Small Pets"
    Scenario: Choose category "Fishes"
        Given open website "http://opencart.qatestlab.net/"
        When click on "Fishes" in menu
        Then Products header should be "Fishes"
    Scenario: Choose category "Birds"
        Given open website "http://opencart.qatestlab.net/"
        When click on "Birds" in menu
        Then Products header should be "Birds"
    Scenario: Choose category "Food"
        Given open website "http://opencart.qatestlab.net/"
        When click on "Food" in menu
        Then Products header should be "Food"