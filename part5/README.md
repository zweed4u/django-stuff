# Part 5  

In this section we learned all about automated testing to ensure our app yielded  
expected results.  
We fired up the interactive shell again and checked our was_recently_published() method to find that future questions would return True.  
This not being the case needed further investigation.  

We wrote a test to ensure that this was in fact a bug.  

We made the test in the polls directory under tests.py  
We made a TestCase subclass QuestionModelTests and asserted that a crafted future question with a future publish date would return False from the was_published_recently method.

We ran the tests via `python3 manage.py test polls` to see that it failed indicating that this in fact is a bug.  
Unknowingly we had just taken part of test-driven development.  

We went into the model to fix the bug in our method.  
Come to find out, we weren't constraining the pub_date on the 'upper end'.  
This is to say, any questions newer than a day old were to be considered published recently even future questions.  
We added the constraint and tested again to see that our test now passed.  

We then wrote more comprehensive tests checking edge cases with equivalence classes to ensure our method was now rock solid.  
We tested questions that fell within and just out of our 24 hour constrained method, resulting in True and False respectively. 

We then even wrote a test for our view.  
In the shell we saw calling `setup_test_environment()` after import was needed to setup the test environment.  

We instantiated a client object for which we tested status codes for GETting various pages/views as well as expected contents/context.  
We then made our polls index view not include/show polls that aren't published yet.  
This was taken care of with get_queryset method.  
We then tested the new and improved view extensively with various questions in count and pub_dates.  

We finally tested the detail view in a similar fashion making sure that response status codes looked OK.  
 

