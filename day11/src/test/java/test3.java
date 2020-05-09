import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class test3 {

    static WebDriver driver= new ChromeDriver();

    public static void main(String[] args) throws InterruptedException {

        System.setProperty("webdriver.chrome.silentOutput", "true");


        driver.manage().window().maximize();
        driver.get("https://www.booking.com/");

        //select city
        WebElement direction = driver.findElement(By.id("ss"));
        direction.sendKeys("Осло");

        //select days
        WebElement period = driver.findElement(By.xpath("//*[@data-mode='checkin']"));
        period.click();


        Calendar calendar = Calendar.getInstance();
        calendar.add(Calendar.DAY_OF_YEAR, 1);
        Date oneDay = calendar.getTime();
        calendar.add(Calendar.DAY_OF_YEAR, 1);
        Date twoDays = calendar.getTime();
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
        String datePlusThreeDays = dateFormat.format(oneDay);
        String datePlusTenDays = dateFormat.format(twoDays);
        WebElement checkIn = driver.findElement(By.xpath(String.format("//*[@data-date='%s']", datePlusThreeDays)));
        checkIn.click();
        WebElement checkOut = driver.findElement(By.xpath(String.format("//*[@data-date='%s']", datePlusTenDays)));
        checkOut.click();

        //select guests
        WebElement guests = driver.findElement(By.xpath("//*[@id='xp__guests__toggle']"));
        guests.click();

        WebElement children = driver.findElement(By.xpath("//*[@aria-describedby='group_children_desc'][2]"));
        children.click();

        WebElement search = driver.findElement(By.xpath("//*[@class='sb-searchbox__button ']"));
        search.click();
        Thread.sleep(4000);


        //select stars
        WebElement threeStarHotels = driver.findElement(By.xpath("//*[@data-id='class-3']"));
        threeStarHotels.click();
        Thread.sleep(4000);

        WebElement fourStarHotels = driver.findElement(By.xpath("//*[@data-id='class-4']"));
        fourStarHotels.click();
        Thread.sleep(4000);

        Actions builder = new Actions(driver);

        WebElement tenthHotel = driver.findElement(By.xpath("//*[@data-hotelid][10]"));
        builder.moveToElement(tenthHotel).perform();
        Thread.sleep(3000);

        WebElement nameOfTenthHotel = driver.findElement(By.xpath("//*[@data-hotelid][10]//span[contains(@class,'sr-hotel__name')]"));
        builder.moveToElement(nameOfTenthHotel).perform();
        Thread.sleep(3000);

        WebElement highLightTenthHotel = driver.findElement(By.xpath("//*[@data-hotelid][10]"));
        builder.moveToElement(highLightTenthHotel).perform();
        LightBackgroundInGreen(highLightTenthHotel);
        Thread.sleep(3000);

        WebElement highLightNameOfTenthHotel = driver.findElement(By.xpath("//*[@data-hotelid][10]//span[contains(@class,'sr-hotel__name')]"));
        builder.moveToElement(highLightNameOfTenthHotel).perform();
        LightTextInRed(highLightNameOfTenthHotel);
        Thread.sleep(3000);

        Assert.assertEquals("Something wrong", "color: red;", highLightNameOfTenthHotel.getAttribute("style"));
        //driver.quit();
    }

    public static void LightBackgroundInGreen(WebElement element) {

        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("arguments[0].setAttribute('style','background: green;');", element);
    }

    public static void LightTextInRed(WebElement text) {

        JavascriptExecutor js = (JavascriptExecutor) driver;
        js.executeScript("arguments[0].setAttribute('style','color: red;');", text);
    }
}