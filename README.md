# pytube
کتابخانه pytube یک کتابخونه کامل و کار امد برای دانلود و گرفتن اطلاعات ویدئو های یوتیوب میباشد <br>
برای نصب این کتابخونه میتونید از کد زیر استفاده کنید:<br>
```
pip install pytube
```
برای مثال برای دانلود یک ویدئو به صورت ساده میتوانید از کد زیر استفاده کنید:<br>

```
from pytube import YouTube

# your video link
yt = YouTube('Link')

# resolution="240p" , resolution="360p" , resolution="480p" , resolution="720p" , resolution="1080p"
yt.streams.filter(mime_type="video/mp4", resolution="360p", progressive=True).first().download()
```

به جای `Link` باید لینک ویدئو خودتون رو هنگام به اشتراک گذاشتن ویدئو کپی کنید و قرار بدید <br>
و یا به جای `360p` کیفیت مورد نظر را قرار دهید (توجه کنید که باید ویدئو دارای همچین کیفیتی باشد در غیر اینصورت با ارور مواجه میشوید) <br> <br>

این یک مثال ساده بود و باید ببینیم وقعا چه اتفاقی اینجا افتاده؟ <br>
در خط اول با کد زیر کلاس اصلی pytube که ازش استفاده میکنیم رو ایمپورت میکنیم: <br>
`from pytube import YouTube` <br> <br>

و بعد با کد زیر یک اینستنس ازش میسازیم:<br>
`yt = YouTube('Link')`<br><br>

حالا در خط اخر چه اتفاقی می افته؟<br>
در خط اخر با استفاده از اینستنس ساخته شده `yt` و متد `streams` یک لیست از حالت های مختلف مثل صدای ویدئو و یا ویدئو در کیفیت های مختلف بازگشت داده میشه که میتوان با استفاده از متد فیلتر `filter` اونها رو فیلتر کرد و اونی که دلمون میخواد رو برداریم. که حالا خود همین متد پارامتر های مختلفی داره که پارامتر اول که ارگومان "video/mp4" رو بهش دادیم نوع فایل رو میگیره که بهش گفتیم فایل ویدئویی <br><br>

پارامتر دوم که کیفیت ویدئو رو میگیره و چیز خاصی نیس<br><br>
بعد پرانتز رو میبندیم و خب به خاطر اینکه متد فیلتر یک لیست با فیلتر هایی که گذاشتید برمیگردونه و فیلتر هایی که ما داریم به یک ایتم میرسه یک لیست با 1 ایتم به ما میده که ما با متد `first` اولیش رو انتخاب میکنیم.<br><br>

و خب تا اینجا ما ویدئو مورد نظر رو انتخاب کردیم اما دانلود نشده و بهش دسترسی نداریم. پس با متد `download` اون ویدئو رو دانلود میکنیم<br><br><br>


خب همونطور که گفتم این یک مثال ساده بود برای دانلود ویدئو ،  صد در صد کلی کار های دیگه میشه کرد مثلا گرفتن اطلاعات ویدئو مثل توضیحات ، تامنیل و یا تعداد ویو ها یا حتی مدت ویدئو. و خیلی چیز های دیگه داره که من همه اشو نمیتونم بگم و یا نمیدونم(شایدم میدونم) و خودتون باید کشف کنید.<br>
داکیومنشن اصلی pytube:<br>
```
https://pytube.io/en/latest
```
