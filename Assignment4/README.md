
<h1>Assignment 4: Hold-On</h1>

<b>This project is due at 11:59pm on December 14, 2017.</b>

<p>
    In this assignment you will develop a DNS client that rejects forged DNS replies, as described in
    <b>
        <a href="http://conferences.npl.co.uk/satin/papers/satin2012-Duan.pdf">this paper</a>
    </b>.
</p>

<h3>Description</h3>
<p>
    Familiarize yourself with the
    <a href="http://conferences.npl.co.uk/satin/papers/satin2012-Duan.pdf">paper</a>. Then, implement a "Hold-On" DNS client as described in the paper.
    <br>
    <br>

    <b>Testing</b>: We will run a testing server that may inject a forged DNS reply for falun.com.
The DNS server is located at elsrv2.cs.umass.edu:<b>5300</b>. 
(DNS is typically run on port 53, but this is blocked by UMass firewalls)
    <br>
    <br>

    <b>Bonus 2% (of final grade)</b>: Implement a DNS proxy that can be used by any client to protect themselves from this type
    of injection. Test this with a second DNS client.
</p>
<h3>Questions</h3>
<p>
    <ol>
        <li>How would you localize a partial proxy that 
            operates only on Web connections?</li>
        
        <li>How would you detect a flow terminating proxy?</li>
        
        <li>How would you detect a flow rewriting proxy?</li>
        
        <li>How can you detect on-path censors?</li>
        
        <li>What can servers do to resist censorship?</li>
        

        <li>How can you determine if a particular filtering product is being used
            for censorship?</li>
        
        <li>You are browsing the web and a site doesn't work. 
            You suspect that this site is being censored in your country. What
            are strategies you can use to confirm this? 
            How would you differentiate censorship from glitches?</li>
        <li>Your country decides to block all encrypted traffic. 
            What is a strategy you could use to send a secret message to
            someone else? How would you make this method scalable?
        </li>
        <li>
            What methods would non-net neutral ISPs likely use to prioritize traffic? 
            What experiments could you do to detect these methods?
        </li>
       
    </ol>
</p>
<h3>What to submit</h3>
<p>
    Zip a directory that contains:
    <ul>
        <li>all required source code files, an appropriate Makefile, and instructions for installing any library dependencies/packages
            (if needed) </li>
        <li>a short report (.txt file is fine) with a brief description of your programs, the results of your experiments, and
            bonus (if submitting it).</li>
        <li>a Wireshark capture showing your tool intercepting responses (and forwarding the correct one, if applicable).</li>
        <li>your responses to the questions.</li>

    </ul>
</p>
