Feature: Parallel testing
    Scenario: Check build results
        Given open website "https://exact-sculpin-blessed.ngrok-free.app/job/AQA%20Framework/"
        When entered jenkins credentials
        Then Parallel tests should have passed
        And Time taken should be less than "10" minutes
