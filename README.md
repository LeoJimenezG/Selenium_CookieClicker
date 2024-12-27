# Selenium_CookieClicker 🍪
A program to automatically play Cookie Clicker using Selenium WebDriver.  

---

## 🎮 About the Game  
Cookie Clicker is a fun incremental game where you click on a cookie to earn points and unlock upgrades.  
Try the game here: [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/).  

*Note: This is not the original website, but a dedicated version for testing automated processes.*  

---

## 📘 How It Works

1. **Window Launch**:  
   - When you run the program, a new browser window will open automatically.  
     ![Window Example](https://github.com/user-attachments/assets/fbd6bfc9-a3cc-47fe-b774-f7310055a814)  

2. **Cookie Clicking**:  
   - The program will start clicking on the cookie continuously.  

3. **Upgrades**:  
   - Every 10 seconds (by default), the program will check for upgrades or items to purchase. If there are enough cookies, it will buy the available upgrades.  

4. **Duration**:  
   - The automation runs for 5 minutes (by default). After this period, the clicking stops, but the browser window remains open.  

---

## ⚙️ Customization 

### 1. Cooldown Time for Upgrades  
   - Adjust the frequency for checking and buying upgrades by modifying the `buy_time` variable.  
   - Change the value `10` to the desired number of seconds.

     ![Cooldown Time Example](https://github.com/user-attachments/assets/5029ca66-6707-48a4-84aa-a1235c73d36a)  

### 2. Duration of the Automation
   - Modify the `duration` variable to set how long the automation runs.   
   - Change the value `5` to the desired number of minutes.

     ![Duration Example](https://github.com/user-attachments/assets/2ff7a14e-5389-4855-b577-9700bbb388b9)  

---

## 📚 Useful Resources
- [Selenium docs](https://www.selenium.dev/documentation/)  
- [Cookie Clicker - Experiments Version](https://orteil.dashnet.org/experiments/cookie/)

---

## 💡 Notes
- At the end of the process, the browser window will remain open. You can manually close it.  
- Ensure that Selenium WebDriver and the appropriate browser driver (e.g., ChromeDriver) are properly installed on your system.  
- This code is meant to showcase how Selenium can automate browser-based tasks.  


Enjoy automating Cookie Clicker!  
