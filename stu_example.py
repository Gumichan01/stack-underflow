
"""
    This file contains some questions you might want to test
"""

ex_cpp_title   = "combination issue : operator '==' and operator '-'"
ex_cpp_content = """<p>I have a weird error when I try to compile this piece of code.
I will explain my problem.<br>
I defined a vector2D as following:</p>

<pre><code>typedef struct LX_Vector2D
{
    float vx;
    float vy;

    LX_Vector2D&amp; operator =(const LX_Vector2D v);  // Defined

} LX_Vector2D;
</code></pre>

<p>I also defined two operators on this vector:</p>

<pre><code>bool operator ==(LX_Vector2D&amp; u,LX_Vector2D&amp; v); // Are u and v equal?
LX_Vector2D operator -(LX_Vector2D&amp; u);          // Get the opposite vector
</code></pre>

<p>All of these overloaded operators was defined.<br>
So I tested these operators in the following code:</p>

<pre><code>LX_Vector2D u = {3.14,-2.56};
LX_Vector2D expected_vec = {-u.vx,-u.vy};

if(expected_vec == (-u))    // ERROR
    cout &lt;&lt; "OK" &lt;&lt; endl;
else
    cout &lt;&lt; "NO" &lt;&lt; endl;
</code></pre>

<p>When I compile this code, I have this error:<br>
<strong><em>no match for ‘operator==’ in ‘expected_vec == operator-((* &amp; u))‘</em></strong></p>

<p>I have no problem with '=' and '==' because I defined and tested them before I implemented '-'.</p>

<p>But when I modify this code to get this: </p>

<pre><code>u = -u;
if(expected_vec == u)    // OK
</code></pre>

<p>I have no error.
I do not understand that, because it seems these two pieces of code are semantically identical.</p>

<p>Here is the definition of <em>operator '-'</em>:</p>

<pre><code>LX_Vector2D operator -(LX_Vector2D&amp; u)
{
    return {-u.vx,-u.vy};
}
</code></pre>

<p>So my question is:<br>
Why doesn't my compiler recognize <em>‘expected_vec == (-u)‘</em> as a call of <em>operator '=='</em> with <em>expected_vec</em> and <em>(-u)</em> as parameters?</p>

<p>Another question:<br>
How can I have the possibility to use <em>if(expected_vec == (-u))</em> without any problem, if it is possible?</p>

<p>I use g++ 4.6.1.</p>"""

ex_java_title = """Is Java “pass-by-reference” or “pass-by-value”?"""
ex_java_content = """<p>I always thought Java was <strong>pass-by-reference</strong>; however I've seen a couple of blog posts (For example, <a href="http://javadude.com/articles/passbyvalue.htm" rel="noreferrer">this blog</a>) that claim it's not. I don't think I understand the distinction they're making. </p>

<p>What is the explanation?</p>"""
