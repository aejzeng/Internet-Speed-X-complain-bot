# Internet-Speed-X-complain-bot

Step 1 - Setup Your X Account
In order to tweet at an internet provider, we of course need a X account. If you want, you can set up a new X account instead of using your personal account.
1. Sign up for an X account here:
https://x.com/i/flow/signup
2. Additionally, you'll need to get your Internet Service Provider (ISP)'s guaranteed internet speeds. This should be in your contract somewhere. Alternatively, you could just use an example speed, e.g. 150Mbps download, 10Mbps upload.
3. Create a new Python project and add these details as constants in the file. e.g.


Step 2 - Create a Class
Because there are multiple steps to this Selenium bot, it's easier if we make our code organised using a class.
1. Create a class called InternetSpeedXBot
2. In the init() method, create the Selenium driver and 2 other properties down and up .
3. Create two methods - get_internet_speed() and tweet_at_provider() .
4. Outside of the class, initialise the object and call the two methods in order. Where you first get the internet speed and then tweet at the provider.


Step 3 - Get Internet Speeds
1. Use this speedtest website to get your current live download and upload speeds manually. e.g.
2. Use Selenium and Python to get the same result printed out in your console. e.g.


Step 4 - Compare the acutal DOWN/UP speed agaisnt the the speed specified in your provider's contract
1. Create aN internet_speed_compare() method
2. IF statement to check the actual speed against the promised speed


Step 5 - Building a X Bot to Tweet at your Internet Provider
1. Go through the process of logging-in and tweeting on X as a human to study which selectors/id/classes/XPATHs you could target.
2. Use Python and Selenium to complete the same process, login to X, compose the tweet to include your up/down speeds and your promised speeds then send the tweet.
NOTE: If you don't want to mention (@) the internet provider, just compose a simple tweet like this:

NOTE: If you are logging into X repeatedly, they will make you complete a Re-CAPTCHA/send a confirmation code to your email to prove you are human.
