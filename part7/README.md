# Part 7  

In this final section we tweaked the admin portion of the app.  
We customized the admin form (seen in polls.admin) and added the Choice object as it should be accessible as well.  
However, we found that this was inefficient and that we should instead make it accessible when adding a question instead of having it float around.  

We made necessary tweaks and even made fieldsets which acted as subsections in the admin view.  
We saw how we could reorder fields on the page and make it so that fields would take up less page space inline.  

We then customized the change list and added different headers - also in polls.admin.  
Furthermore, we changed header text and made the value of such headers for entries prettier. This was accomplished in polls.models under the method we wanted to include in the admin view under list_display in polls.admin.

We then added a search field and filtering of pub date in polls.admin.

Wrapping it all up we borrowed some of django's provided source templates.
- We found this dir via: `python3 -c "import django; print(django.__path__)"`
- in mysite.settings we needed to include the path to the templates respective of the project's base directory to load the provided template which we took in
- we customized the base_site html template example to show that we could modify the sitename via generic templates
