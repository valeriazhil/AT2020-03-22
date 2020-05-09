import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.interactions.Actions;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class test2 {


   // static WebDriver driver= new ChromeDriver();

    public static void main(String[] args) throws InterruptedException {

        System.setProperty("webdriver.chrome.silentOutput", "true");
        WebDriver driver= new ChromeDriver();

        driver.manage().window().maximize(); //all
        driver.get("https://www.booking.com/");

        //select city
        WebElement direction = driver.findElement(By.id("ss"));
        direction.sendKeys("Москва");

        //select days
        WebElement days = driver.findElement(By.xpath("//*[@data-mode='checkin']"));
        days.click();

        //select date
        Calendar calendar = Calendar.getInstance();
        calendar.add(Calendar.DAY_OF_YEAR, 10);
        Date tenDays = calendar.getTime();
        calendar.add(Calendar.DAY_OF_YEAR, 5);
        Date fifteenDays = calendar.getTime();
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
        String datePlusThreeDays = dateFormat.format(tenDays);
        String datePlusTenDays = dateFormat.format(fifteenDays);
        WebElement checkIn = driver.findElement(By.xpath(String.format("//*[@data-date='%s']", datePlusThreeDays)));
        checkIn.click();
        WebElement checkOut = driver.findElement(By.xpath(String.format("//*[@data-date='%s']", datePlusTenDays)));
        checkOut.click();

        WebElement search = driver.findElement(By.xpath("//*[@class='sb-searchbox__button ']"));
        search.click();
        Thread.sleep(5000);

        //select guests
        Actions actions = new Actions(driver);

        WebElement adults = driver.findElement(By.cssSelector("#group_adults"));
        actions.click(adults).sendKeys(Keys.ARROW_DOWN).sendKeys(Keys.ARROW_DOWN).sendKeys(Keys.ENTER).build().perform();

        //select rooms
        WebElement rooms = driver.findElement(By.cssSelector("#no_rooms"));
        actions.click(rooms).sendKeys(Keys.ARROW_DOWN).sendKeys(Keys.ENTER).build().perform();


        WebElement newSearch = driver.findElement(By.xpath("//*[@class='sb-searchbox__button ']"));
        newSearch.click();
        Thread.sleep(5000);

        WebElement budget = driver.findElement(By.xpath("//*[@data-id='pri-1']"));
        budget.click();
        String budgetUpTo = budget.getText().substring(budget.getText().indexOf("-")).replaceAll("[^0-9]+", "");
        System.out.println("Budget per night up to " + budgetUpTo);
        int budgetPerNight = Integer.parseInt(budgetUpTo);
        Thread.sleep(5000);

        WebElement firstOnTheList = driver.findElement(By.xpath("//*[@data-hotelid][1]//div[contains(@class,'bui-price-display__value prco-inline-block-maker-helper')]"));
        String priceOfFirstOnTheList = firstOnTheList.getText().replaceAll("[^0-9]+", "");
        int hotelPerNight = Integer.parseInt(priceOfFirstOnTheList) / 5;
        System.out.println("Price per night of first on the list from " + hotelPerNight);


        Assert.assertTrue("Something wrong", hotelPerNight <= budgetPerNight);
        //driver.quit();



    }
   //@Test
    //    public void verifyTitle(int hotelPerNight,int budgetPerNight)
    //    {
    //        Assert.assertTrue("Something wrong", hotelPerNight <= budgetPerNight);
    //        System.out.println("Something wrong");
    //    }
}