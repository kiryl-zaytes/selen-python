@browser=firefox
Feature: Main page functionality
  Perform base actions check

  Scenario: Open search page
	Given "firefox" browser
	When navigate to "http://google.com"
	Then page appears with title "Google"
