Feature: Generating report
    Scenario: Check build results
        Given open website "https://a91d-178-94-146-229.ngrok-free.app/job/AQA%20Framework/"
        When entered jenkins credentials
        Then link to report should exist