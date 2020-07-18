const { Builder, By, Key, util } = require("selenium-webdriver");
async function example() {
    let driver = await new Builder().forBrowser('chrome').build();
    await driver.get("http://youtube.com");
    // await driver.findElement(By.name('q')).sendKeys("Hello World!", Key.RETURN);
}
example();