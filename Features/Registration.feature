Feature: Verfying registration functionality

Scenario: Registration with valid data 
Given User is on Registration page 
When User enters username
And User enter email id 
And User enter password
And User click on signup button 
Then User should be registered successfully 

Scenario: Registration with duplicate username data
Given User is on Registration page 
When User enters duplicate username
And User enter email id 
And User enter password
And User click on signup button 
Then User should be registered successfully