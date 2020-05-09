import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class BookingTest {

    static WebDriver driver= new ChromeDriver();


    public static void main(String[] args) throws InterruptedException {
        //System.setProperty("webdriver.chrome.silentOutput", "true");
        driver.get("https://www.booking.com/");
        WebElement element_enter;
        element_enter = driver.findElement(By.xpath("//*[@id=\"ss\"]"));
        element_enter.findElement(By.xpath("//*[@id=\"ss\"]")).sendKeys("Париж");
        //driver.findElement(By.xpath("/html/body/div[5]/div/div/div[2]/form/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]")).click();


        Calendar calendar=Calendar.getInstance();
        calendar.add(Calendar.DAY_OF_YEAR,3);
        Date threeDay=calendar.getTime();
        calendar.add(Calendar.DAY_OF_YEAR,7);
        Date tenDay=calendar.getTime();
        SimpleDateFormat dateFormat= new SimpleDateFormat("yyyy-MM-dd");
        String datePlusThreeDays=dateFormat.format(threeDay);
        String datePlusTenDays=dateFormat.format(tenDay);

        //select date
        driver.findElement(By.xpath("//*[@id=\"frm\"]/div[1]/div[2]")).click();

        driver.findElement(By.xpath("//*[@data-date='"+datePlusThreeDays+"']")).click();
        Thread.sleep(2000);
        driver.findElement(By.xpath("//*[@data-date='"+datePlusTenDays+"']")).click();

        //select number of people
        driver.findElement(By.xpath("//*[@id=\"frm\"]/div[1]/div[3]")).click();
       WebElement adults = driver.findElement(By.xpath("//*[@id=\"xp__guests__inputs-container\"]/div/div/div[1]/div/div[2]/button[2]"));
       adults.click();
       adults.click();

        WebElement rooms = driver.findElement(By.xpath("//*[@id=\"xp__guests__inputs-container\"]/div/div/div[3]/div/div[2]/button[2]"));
        rooms.click();

        driver.findElement(By.xpath("//*[@id=\"frm\"]/div[1]/div[4]/div[2]/button")).click();
        Thread.sleep(2000);

        driver.findElement(By.xpath("//*[@id=\"filter_price\"]/div[2]/a[5]/label")).click();
        Thread.sleep(2000);


        driver.findElement(By.xpath("//*[@id=\"sort_by\"]/ul/li[3]")).click();
        Thread.sleep(2000);

        //String cost1=driver.findElement(By.xpath())





        //driver.close();
        //System.setProperty("webdriver.chrome.drivers","C:\\Server");
       // driver.get("https://www.google.com/");
        //System.out.println(driver.getTitle());
        //System.out.println(driver.getCurrentUrl());
        //driver.close();
        //driver.navigate().to("https://www.google.com/");
       // driver.navigate().to("https://ya.ru/");
        //driver.navigate().forward();
        //driver.navigate().back();
        //driver.navigate().refresh();
       // searchBox.click();

    }
}
