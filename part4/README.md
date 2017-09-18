# Part 4  

We started off by writing a simple form in the polls.detail template.  
This provided us with radio buttons and a vote button for a given question.  

We went to polls.urls to map a view to handle submitted data from the form.
The view was them written in polls.views to account for POSTed data and HTTPResponseRedirect.  
We also made use of incrementing a counter to keep track of votes submitted on the form.  

We then wrote a results view that would be seen/used after the vote had been posted.  
We made use of a template under polls.results html. This view showed the question, choices, and number of votes for the choices and a vote again button.  

We then sought to make our views more generic - we converted the urlconf, removed some unneeded views, and made new generic views.  
- We made use of <pk> in the urlconf which had the same effect as the replaced <question_id>
- We made classes for most of our views, removing the old ones. Each class had a model and template_name attribute and inherited from a generic view.  

