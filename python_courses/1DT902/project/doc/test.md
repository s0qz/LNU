# Testing Termostatuller
## Requirements of the project
The municipalty wants to be able to read temperature, decibel, humidity and co2 values in their locals in real time. Based on this, the projects requirements was set. To start the project we should calculate the temperature and humidity. Its data should be sent to a database every fifth minute and the data should be published on a webpage. The product should be stand-alone and using a wireless connection such as wifi. It should use an 9V battery and have a lifespan of atleast a quarter before having to change battery. The values sent to the database should be saved for 7 days and a graph for all the values the last 7 days should be presented on the webpage. The last value read and a graph for the last day should also be presented on the webpage. The webpage shall be written in HTML5, css and javascript for the connection to the datbase. The code for the sensors and hardware is to be written in micropython. In later stages both a co2 sensor and a decibel reader should be able to be connected to the harware without major work to be done.
These requirements could be broken down in to smaller parts.
- The sensors shows the correct value for temperature and humidity

- The municipality wants to be able to read the temperature and humidity in real time

- The values should be sent to the database every five minutes

- The website should show values for the last 7 days and 24 
hours in a graph

- The project should be prepared for external sensors to be attached in later stages

- The battery should last for a quarter


## Exploratory testing
The municipality wants to see the real time value of temperature and humidity.

A successful testing would look like this:

We launch or website and our database - We start the application on the computer- We connect to the hardware via wifi using vscode - we start running our program - our values are presented on the website with 5 minutes between.

The result:

When testing the full system was a success as the real time values is presented on the website. The update frequency is 5 minutes and there are two graphs for each value, one for last 24 hours and one for last 7 days. The values can also seen being sent through the databse.


# Manual testing
## Testing the DHT11
### Temperature:
* Test 1 - The temperature is correct inside

Prereq:

Input:

Behavior:



Result:

|Room | Temperature meter |DHT11|
| ------ | ------|----- |
|Inside| 22 degrees | 22 degrees|

This resulr .....

* Test 2 - The temperature changes when going outside

Prereq:

Input:

Behavior:



Result:

|Room | Temperature meter |DHT11|
| ------ | ------|----- |
|Outside| 22 degrees | 22 degrees|


### Humidity:
Test 1 - The humidity is correct
Prereq:

Input:

Behavior:



Result:
Test 2 - The humidity changes when blowing air on the sensor
Prereq:

Input:

Behavior:



Result:

## Testing the KY-028
Test 1 - The temperature is correct inside
Prereq:

Input:

Behavior:



Result:
|Room | Temperature meter |KY-028|
| ------ | ------|----- |
|Outside| 22 degrees | 22 degrees|
Test 2 - The temperature changes when going outside
Prereq:

Input:

Behavior:



Result:
|Room | Temperature meter |KY-028|
| ------ | ------|----- |
|Outside| 22 degrees | 22 degrees|

## Testing the battery life
### Requirement being tested
- The battery should last for a quarter

Test 1 - Calculating expected battery life using values over last 24 hours

Prereq:

Input:

Behavior:

Result: