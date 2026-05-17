# IoT\_Smart-ChAIr

## The link to the common folder is [here](https://drive.google.com/drive/folders/1vy685r2IYYLLrJJtexPPP0kG4qTNNphn?usp=sharing).







### Sebghat Yarzada Update on 18.05.2026



### **# Part List is Done!**



#### **Hello everyone,**



I have prepared two versions of the part list for our Smart Chair project.



\## 1. Original Version



This version follows Arturo’s original component list:



\* 2 × Arduino Uno boards

\* 2 × ESP8266 Wi-Fi modules



\## 2. Alternative ESP32 Version



In this version, the two Arduino boards and the two separate Wi-Fi modules are replaced by:



\* 2 × ESP32 Development Boards



Since the ESP32 already includes built-in Wi-Fi, this reduces cost and simplifies the hardware setup.



Please review both files and decide which version we would like to submit to the instructors.



## \## Request to Arturo



Arturo, could you please:



\* Open each product link.

\* Verify that the link opens the correct product page.

\* Check that the selected product matches the part name and model description.

\* Confirm that the selected components are technically suitable for our project.

\* Let us know which of the two versions you recommend.



Once we agree on the preferred version, we can remove the other file.



\## Notes



\* The file names have been updated to match our group name.

\* The comments included in the university template have been taken into account.

\* Please let me know if any component, price, or link should be corrected.



Thank you!







//////////////////////////////////////////////////////////////////////////////////////////////////////



### Meeting on Sunday, May 17th:

#### What exactly are we going to do?

* We are going to use a chair with several  sensors to detect how well seated are you. Two measuring stations are going to be made.

  * In the Chair:

    * Pressure sensors to detect the posture of the user.
    * Measure the distance from the chair to your head.
    * Measure the movement in front of the chair to detect if you are moving the legs or not.
  * In the Table:

    * Measure the distance from the computer to your head.
    * Measure the pressure on the table to detect if you are leaning on it or not.
* Our computer will collect the information from both stations and:

  * It will show everything in a website in a user-friendly way. ***ONLY IF THE TEACHERS SAY THAT OUR PROJECT IS NOT ENOUGH FOR 4 PEOPLE.***
  * It will activate a buzzer in one of the stations if the user is not well seated for a long time.



#### What pieces do we need?

* A high chair to be able to add the distance sensor
* Pressure sensors (the more, the better). At least 4, but ideally 8 or more.
* 2 Distance sensors
* A buzzer
* 2 Arduino boards (one for each station)
* A PIR sensor (or other kind of movement sensor) to detect if the user is moving the legs or not.
* 2 WiFi modules to connect the Arduinos to the computer.



### Task to be split:

* **Atenea** (28/05): Finding the pieces and prepare the Part List for the project
* **Sebghat** (22/05): Preparing the slides for the Pitch
* **Michael** (28/05): How to measure if a user is well seated or not with the information from the sensors.
* **Arturo** (28/05): How to communicate your computer with both Arduinos, process that information and send the activation of the Buzzer to one of them.

