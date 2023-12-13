Feature: Parallel testing
    Scenario: Check build results
        Given open website "http://192.168.1.3:8080/job/AQA%20Framework/"
        When entered jenkins credentials
        Then Parallel tests should have passed
        And Time taken should be less than "10" minutes
