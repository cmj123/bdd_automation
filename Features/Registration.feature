Feature: Verfying registration functionality

@sanity
Scenario: Registration with valid data 
Given User is on Registration page 
When User enters username
And User enter email id 
And User enter password
And User click on signup button 
Then User should be registered successfully 

@sanity @smoke
Scenario: Registration with duplicate username data
Given User is on Registration page 
When User enters duplicate username
And User enter email id 
And User enter password
And User click on signup button 
Then User should be registered successfully

@abc
Scenario: Registration with duplicate username data
Given User is on Registration page 
When User enters duplicate username
And User enter email id 
And User enter password
And User click on signup button 
Then User should be registered successfully