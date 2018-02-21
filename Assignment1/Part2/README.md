
<h2>Assignment 1 (part 2): Web Crawler</h2>
<p>
<b>This project is due at 11:59pm on September 20, 2017.</b>
</p><p>
<h2>Description</h2>
This assignment is intended to familiarize you with the HTTP protocol. HTTP is (arguably)
the most important application level protocol on the Internet today: the Web runs on HTTP,
and increasingly other applications use HTTP as well (including Bittorrent, streaming video,
Facebook and Twitter's social APIs, etc.).
<p></p>
Your goal in this assignment is to implement a web crawler that gathers data from a fake
social networking website that we have set up for you. The site is available here:
<a href="http://elsrv2.cs.umass.edu/">Fakebook</a>.
</p><p>
<h2>What is a Web Crawler?</h2>
A web crawler (sometimes known as a robot, a spider, or a screen scraper) is a piece of
software that automatically gathers and traverses documents on the web. For example,
lets say you have a crawler and you tell it to start at www.wikipedia.com. The software
will first download the Wikipedia homepage, then it will parse the HTML and locate all
hyperlinks (i.e. anchor tags) embedded in the page. The crawler then downloads
all the HTML pages specified by the URLs on the homepage, and parses them looking for more
hyperlinks. This process continues until all of the pages on Wikipedia are downloaded and
parsed.
</p><p>
Web crawlers are a fundamental component of today's web. For example, Googlebot is Google's
web crawler. Googlebot is constantly scouring the web, downloading pages in search of new
and updated content. All of this data forms the backbone of Google's search engine infrastructure.
</p><p>
<h2>Fakebook</h2>
We have set up a fake social network for this project called <a href="http://elsrv2.cs.umass.edu/">Fakebook</a>.
Fakebook is a very
simple website that consists of the following pages:
<ul><li><b>Homepage</b>: The Fakebook homepage displays some welcome text, as well as links
to several random Fakebook users' personal profiles.</li>
<li><b>Personal Profiles</b>: Each Fakebook user has a profile page that includes their
name, some basic demographic information, as well as a link to their list of friends.</li>
<li><b>Friends List</b>: Each Fakebook user is friends with one or more other Fakebook
users. This page lists the user's friends and has links to their personal profiles.</li>
</ul>
In order to browse Fakebook, you must first login with a username and password. We will email
each student to give them a unique username and password.
</p><p>
<h2>WARNING: DO NOT TEST YOUR CRAWLERS ON PUBLIC WEBSITES</h2>
Many web server administrators view crawlers as a nuisance, and they get very mad if
they see strange crawlers traversing their sites. <b>Only test your crawler against
Fakebook, do not test it against any other websites</b>.
</p><p>
<h2>High Level Requirements</h2>
Your goal is to collect 5 <i>secret flags</i> that have been hidden somewhere on the Fakebook website.
The flags are unique for each student, and the pages that contain the flags will be different for each student.
Since you have no idea what pages the secret flags will appear on, your only option is to write a web
crawler that will traverse Fakebook and locate your flags. 
</p><p>
Your web crawler must execute on the command line using the following syntax:
</p><p>
./webcrawler [username] [password]
</p><p>
<i>username</i> and <i>password</i> are used by your crawler to log-in to Fakebook. You may assume
that the root page for Fakebook is available at <a href="http://elsrv2.cs.umass.edu/">
http://elsrv2.cs.umass.edu/</a>. You may also assume that the log-in form for Fakebook is available
at <a href="http://elsrv2.cs.umass.edu/accounts/login/?next=/fakebook/">
http://elsrv2.cs.umass.edu/accounts/login/?next=/fakebook/</a>.
</p><p>
Your web crawler should print <b>exactly fives lines of output</b>: the five <i>secret flags</i> discovered
during the crawl of Fakebook. If your program encounters an unrecoverable error, it may print an error
message before terminating.
</p><p>
Secret flags may be hidden on any page on Fakebook, and their relative location on each page may be different.
Each secret flag is a 64 character long sequences of random alphanumerics.
All secret flags will appear in the following format (which makes them easy to identify):
</p><p>
&lt;h2 class='secret_flag' style="color:red"&gt;FLAG: 64-characters-of-random-alphanumerics&lt;/h2&gt;
</p>

<p>
There are a few key things that all web crawlers must do in order function:
<ul>
<li><b>Track the Frontier</b>: As your crawler traverses Fakebook it will observe many URLs.
Typically, these uncrawled URLs are stored in a queue, stack, or list until the crawler is 
ready to visit them.  These uncrawled URLs are known as the frontier.</li>
<li><b>Watch Out for Loops</b>: Your crawler needs to keep track of where it has been, i.e. the
URLs that it has already crawled. Obviously, it isn't efficient to revisit the same pages over
and over again. If your crawler does not keep track of where it has been, it will almost
certainly enter an infinite loop. For example, if users A and B are friends on Fakebook, then that
means A's page links to B, and B's page links to A. Unless the crawler is smart, it will ping-pong
back and forth going A->B, B->A, A->B, B->A, ..., etc.</li>
<li><b>Only Crawl The Target Domain</b>: Web pages may include links that point to arbitrary
domains (e.g. a link on google.com that points to cnn.com). <b>Your crawler should only traverse
URLs that point to pages on elsrv2.cs.umass.edu</b>. For example, it would be valid to crawl
<i>http://elsrv2.cs.umass.edu/fakebook/018912/</i>, but it would not be valid to crawl
<i>http://www.facebook.com/018912/</i>.
</ul>
</p><p>
</p><p>
In order to build a successful web crawler, you will need to handle several different aspects of the HTTP
protocol:
<ul><li>HTTP GET - These requests are necessary for downloading HTML pages.</li>
<li>HTTP POST - You will need to implement HTTP POST so that your code can login to Fakebook. As
shown above, you will pass a 
username and password to your crawler on the command line. The crawler will then use
these values as parameters in an HTTP POST in order to log-in to Fakebook.</li>
<li>Cookie Management - Fakebook uses cookies to track whether clients are logged in to the site. If
your crawler successfully logs in to Fakebook using an HTTP POST,
Fakebook will return a session cookie to your crawler. Your crawler should
store this cookie, and submit it along with each HTTP GET request as it crawls Fakebook.
If your crawler fails to handle cookies properly, then your software will not be able
to successfully crawl Fakebook.</li>
</ul>
</p><p>
In addition to crawling Fakebook, your web crawler must be able to correctly handle <a href="http://en.wikipedia.org/wiki/List_of_HTTP_status_codes">HTTP status codes</a>. Obviously, you need to handle 200, since that means
everything is okay. Your code must also handle:
<ul>
<li>301 - Moved Permanently: This is known as an HTTP redirect. Your crawler should try the request 
again using the new URL given by the server.</li>
<li>403 - Forbidden and 404 - Not Found: Our web server may return these codes in order to trip up your
crawler. In this case, your crawler should abandon the URL that generated the error code.</li>
<li>500 - Internal Server Error: Our web server may <b>randomly</b> return this error code to your
crawler. In this case, your crawler should re-try the request for the URL until the request is
successful.</li>
</ul>
</p><p>
I highly recommend the <a href="http://www.jmarshall.com/easy/http/">HTTP Made Really Easy</a>
tutorial as a starting place for students to learn about the HTTP protocol. Furthermore, the
developer tools built-in to the Chrome browser, as well as the <a href="http://getfirebug.com/">Firebug</a>
extension for Firefox, are both excellent tools for inspecting and understanding
HTTP requests.
</p><p>
<h2>Logging in to Fakebook</h2>
In order to write code that can successfully log-in to Fakebook, you will need to
reverse engineer the HTML form on the log-in page. Students should carefully inspect
the form's code, since it may not be as simple as it initially appears.
</p><p>
<h2>Development</h2>
You can write your code in whatever language you choose, as long as your code compiles and runs
on <b>unmodified</b> EdLab Linux machines <b>on the command line</b>. Do not use libraries that are not
installed by default on EdLab machines. Similarly, your code must compile and run on the
command line. You may use IDEs (e.g. Eclipse) during development, but do not turn in your IDE
project without a Makefile. Make sure you code has <b>no dependencies</b> on your IDE.
</p><p>
<h2>Legal Libraries and Modules</h2>
Students may use any available libraries to create socket connections, parse URLs,
and parse HTML. However, <b>all HTTP request code must be written by the student, from scratch</b>.
Your code must build all HTTP messages, parse HTTP responses, and manage all cookies.
</p><p>
For example, if you were to write your crawler in Python, the following modules would
all be allowed: <i>socket</i>, <i>parseurl</i>, <i>html</i>, <i>html.parse</i>, and <i>xml</i>.
However, the following modules would <b>not</b> be allowed: <i>urllib</i>, <i>urllib2</i>,
<i>httplib</i>, and <i>cookielib</i>.
</p><p>
Similarly, if you were to write your crawler in Java, it would <b> not be legal</b> to use <i>java.net.CookieHandler</i>,
<i>java.net.CookieManager</i>, <i>java.net.HttpCookie</i>, <i>java.net.HttpUrlConnection</i>, <i>java.net.URLConnection</i>,
<i>URL.openConnection()</i>, <i>URL.openStream()</i>, or <i>URL.getContent()</i>. 
</p><p>
If students have any questions about the legality of any libraries please post them to Piazza.
It is much safer to ask ahead of time, rather than turn in code that uses a questionable
library and receive points off for the assignment after the fact. 
</p><p>
<h2>Submitting Your Project</h2>
To turn-in your project, you should submit your (thoroughly documented) code along with three other files:
<ul><li>A Makefile that compiles your code (if needed).</li>
<li>A plain-text (no Word or PDF) README file. In this file, you should briefly describe your high-level
approach, any challenges you faced, and an overview of how you tested your code.</li>
<li>A file called <i>secret_flags</i>. This file should contain the <i>secret flags</i> in plain ASCII.</li>
</ul>
Submit your project as a zip file containing these files in the root directory on Moodle. Do not put the files in a subdirectory.
</p><p>
<h2>Grading</h2>
This project is worth 8 points. You will receive full credit if 1) your code compiles, runs, and produces the
expected output, 2) you have not used any illegal libraries, and 3) you successfully submit the
<i>secret flags</i>. All student code will be scanned by plagarism
detection software to ensure that students are not copying code from the Internet or each other.
</p><p>
