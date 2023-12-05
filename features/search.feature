Feature: Example Feature
    Scenario: Search for "Корм"
        Given open website "http://opencart.qatestlab.net/"
        When enter "Корм" in search field
        Then I should see search results related to "Корм"
    Scenario: Search for "Ноутбуки"
        Given open website "http://opencart.qatestlab.net/"
        When enter "Ноутбуки" in search field
        Then I should see search results related to "Ноутбуки"
