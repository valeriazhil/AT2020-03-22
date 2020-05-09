import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class test1 {

    //static WebDriver driver= new ChromeDriver();

    public static void main(String[] args) throws InterruptedException {

        System.setProperty("webdriver.chrome.silentOutput", "true");
        WebDriver driver= new ChromeDriver();

        //open booking
        driver.get("https://www.booking.com/");

        //select city
        WebElement direction = driver.findElement(By.id("ss"));
        direction.sendKeys("Париж");

        //select days
        WebElement days= driver.findElement(By.xpath("//*[@data-mode='checkin']"));
        days.click();

        //select date
        Calendar calendar = Calendar.getInstance();
        calendar.add(Calendar.DAY_OF_YEAR, 3);
        Date threeDays = calendar.getTime();
        calendar.add(Calendar.DAY_OF_YEAR, 7);
        Date tenDays = calendar.getTime();
        SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd");
        String datePlusThreeDays = dateFormat.format(threeDays);
        String datePlusTenDays = dateFormat.format(tenDays);

        WebElement checkIn = driver.findElement(By.xpath(String.format("//*[@data-date='%s']", datePlusThreeDays)));
        checkIn.click();
        WebElement checkOut = driver.findElement(By.xpath(String.format("//*[@data-date='%s']", datePlusTenDays)));
        checkOut.click();

        //select guests
        driver.findElement(By.xpath("//*[@id=\"frm\"]/div[1]/div[3]")).click();
        WebElement adults = driver.findElement(By.xpath("//*[@id=\"xp__guests__inputs-container\"]/div/div/div[1]/div/div[2]/button[2]"));
        adults.click();
        adults.click();

        //select rooms
        WebElement rooms = driver.findElement(By.xpath("//*[@id=\"xp__guests__inputs-container\"]/div/div/div[3]/div/div[2]/button[2]"));
        rooms.click();


        WebElement search = driver.findElement(By.xpath("//*[@class='sb-searchbox__button ']"));
        search.click();
        Thread.sleep(4000);

        //select  "BYN 1 060 + за ночь"
        WebElement budget = driver.findElement(By.xpath("//*[@data-id='pri-5']"));
        budget.click();

        //get budget per night
        String budgetFrom = budget.getText().replaceAll("[^0-9]+", "");
        System.out.println("Budget per night from " + budgetFrom);
        int budgetPerNight = Integer.parseInt(budgetFrom);
        Thread.sleep(3000);

        WebElement lowest = driver.findElement(By.xpath("//*[@class=' sort_category   sort_price ']"));
        lowest.click();
        Thread.sleep(3000);

        WebElement MinFromMax = driver.findElement(By.xpath("//*[@data-hotelid][1]//div[contains(@class,'bui-price-display__value prco-inline-block-maker-helper')]"));
        String minPriceFromMax = MinFromMax.getText().replaceAll("[^0-9]+", "");
        int hotelPerNight = Integer.parseInt(minPriceFromMax) / 7;
        System.out.println("Minimum price per night from " + hotelPerNight);

        Assert.assertTrue("Something wrong! Minimum price per night is higher than budget per night. ", hotelPerNight <= budgetPerNight);
       // driver.quit();
    }
}
