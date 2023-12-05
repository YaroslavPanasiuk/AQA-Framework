Feature: Example Feature
    Scenario: Sort by name ascending
        Given open website "http://opencart.qatestlab.net/"
        When enter "pet" in search field
        And select sort by "Name (A - Z)"
        Then results should be sorted by "name" "ascending"

    Scenario: Sort by name descending
        Given open website "http://opencart.qatestlab.net/"
        When enter "pet" in search field
        And select sort by "Name (Z - A)"
        Then results should be sorted by "name" "descending"

    Scenario: Sort by price ascending
        Given open website "http://opencart.qatestlab.net/"
        When enter "pet" in search field
        And select sort by "Price (Low > High)"
        Then results should be sorted by "price" "ascending"

    Scenario: Sort by price descending
        Given open website "http://opencart.qatestlab.net/"
        When enter "pet" in search field
        And select sort by "Price (High > Low)"
        Then results should be sorted by "price" "descending"

    Scenario: Sort by rating ascending
        Given open website "http://opencart.qatestlab.net/"
        When enter "pet" in search field
        And select sort by "Rating (Lowest)"
        Then results should be sorted by "rating" "ascending"

    Scenario: Sort by rating descending
        Given open website "http://opencart.qatestlab.net/"
        When enter "pet" in search field
        And select sort by "Rating (Highest)"
        Then results should be sorted by "rating" "descending"
