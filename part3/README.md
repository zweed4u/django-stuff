# Part 3
We continued on by writing even more views, this time for details, results and votes for questions.  
We then mapped these views to urls in polls.urls as we did before for mysite.

We made the views actually do stuff - we made the index show the last 5 questions orded by published dates.  
We then introduced templates html which could then be used in our views.

We learned about the render() method which removed the need for explicitly loading the template.  
After tricking out our view we further embellished it by implementing a 404 exception handler.  
A detail html file provided for a simple view/test for this

We learned about another shortcut other than render() in get_object_or_404.  
This allowed the try-catch block to be removed in our view and to simply just call this method and return the result as 'quesiton'.  

We further explored templates and made the detail.html prettier to include question and choice text.  
In polls.index we removed the hardcoded url which made use of polls.urls.

In polls.urls we even mapped up a new url to reflect the same view as detail under the 'specifics/' url path.  
We then learned about namespacing and that for projects with many apps, it is beneficial.  
All that was needed was to define the app name in polls.urls and then use the namespaced detail view 'polls:detail' in the polls.index under templates.  

