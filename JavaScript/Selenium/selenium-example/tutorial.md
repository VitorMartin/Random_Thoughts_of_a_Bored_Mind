# Step by step to create and run your Selenium project

## Preparing environment

### 1. Install **Node.js**
- Download from [nodejs.org](https://nodejs.org/)
- Test if **Node.js** is working by typing `node -v` in a terminal window
- Test if **npm** is working by typing `npm -v` in a terminal window

### 2. Install **selenium-webdriver**
- Download from [npmjs.com](https://www.npmjs.com/)
- Choose the right driver for your specific browser
- Extract the zipped file
- Add the executable to your Environment Variables (PATH)
- Test if it works by typing `start [web driver name]` in a terminal window
- For example, if you downloaded Google Chrome's web driver, type `start chromedriver.exe`

## Creating a Selenium project

### 3. Create an empty project folder

### 4. Create a package for the project
- Open the project folder on your terminal
- Create a `package.json` by typing `npm init` on the terminal and following the instructions

### 5. Install the **selenium-webdriver** npm module
- Open a terminal inside the project folder
- Type `npm install selenium-webdriver`

### 6. Create your JavaScript file
- The name **must be the same** as you specified on the `package.json`!
- Here you can create your custom JS script

## Running your application

### 7. Run node command
- Open a terminal on the same path as your JS file
- Type `node [js file name]`
- For example, if you named your JS file as `index.js`, type `node index`

# Video tutorial from CodingSrc
https://www.youtube.com/watch?v=fj0Ud16YJJw