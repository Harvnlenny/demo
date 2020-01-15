Feature: Search Players

    Scenario: Search Players
        Given the User is on Football Reference
        When a name is typed into the search field
        Then the User will be on the page of the Player
