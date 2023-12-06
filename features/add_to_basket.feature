Feature: Add items to basket
    Scenario: search for "Pet" and add first item to basket
        Given open website "http://opencart.qatestlab.net/"
        When enter "Pet" in search field
        And choose item #"1"
        And choose "default size" and "default color" options
        And click buy
        And go to basket
        Then basket should have "1" items

    Scenario: search for "Pet" and add second item to basket
        Given open website "http://opencart.qatestlab.net/"
        When enter "Pet" in search field
        And choose item #"2"
        And choose "default size" and "default color" options
        And click buy
        And go to basket
        Then basket should have "1" items

    Scenario: search for "Pet" and add second and fourth item to basket
        Given open website "http://opencart.qatestlab.net/"
        When enter "Pet" in search field
        And choose item #"2"
        And choose "default size" and "default color" options
        And click buy
        And enter "Pet" in search field
        And choose item #"4"
        And choose "default size" and "default color" options
        And click buy
        And go to basket
        Then basket should have "3" items