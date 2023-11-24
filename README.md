Problem's Solution for the **Livewire Hackengers** Final Round won by Team Sigma.


**PS: Unlocking Access with Voice: Enhancing GUI Login Pages through Speech Recognition**

![image](https://github.com/Makarand-sdw/Livewire/assets/132384262/912b5d3d-f3dd-4361-aa30-f88a56375bd2)


This Python code is an implementation of a simple login page with speech recognition functionality. Here are the key things it is doing:
1.	It imports the necessary libraries:
•	**tkinter** for building the GUI
•	**speech_recognition** for speech-to-text
2.	The **recognize_speech()** function uses the speech_recognition library to listen to microphone input and convert it to text.
3.	The **login()** function checks the entered username and password against some hardcoded values and shows either a success or error message box.
4.	The **speech_to_text()** function takes the recognized speech and inserts it into a given text entry widget.
5.	In the GUI:
•	It shows a logo image at the top
•	**Username and password** fields with labels
•	**Buttons** next to each text entry to trigger speech recognition
•	A **login** button to submit and check the credentials
6.	When the speech buttons are clicked, it will invoke speech_to_text() to populate the corresponding text entry field.
7.	Clicking the login button checks the credentials by calling the login() function.

